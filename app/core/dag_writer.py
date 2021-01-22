# coding: utf-8
'''
class that generates the python code class.
'''


class PyClass:

    def __init__(self):
        self.ObjectType = "Class"
        self.name = ''
        self.inhnerit_list = []
        self.sub_class_list = []
        self.function_list = []
        self.with_list = []
        self.class_lines = []

    def set_name(self, val):
        self.name = val

    def set_inheritance(self, val):
        self.inhnerit_list.append(val)

    def add_line(self, val):
        self.class_lines.append(val)

    def add_subclass(self, val):
        self.sub_class_list.append(val)

    def add_function(self, val):
        self.function_list.append(val)

    def add_with(self, val):
        self.with_list.append(val)

    def ident(self, val=1):
        val2 = ' '
        return ((4 * val) * val2)

    def line_break(self, val):
        return val * '\n'

    def __repr__(self):
        res = "class %s" % (self.name,)
        for pos, inheritance in enumerate(self.inhnerit_list):
            if pos == 0:
                res += '('
            if pos > 0:
                res += ', '
            res += inheritance
        if self.inhnerit_list:
            res += ')'
        res += ':'
        res += self.line_break(2)
        for sline in self.class_lines:
            res += self.ident() + sline
            res += self.line_break(1)
        for sclass in self.sub_class_list:
            res += sclass
            res += self.line_break(2)
        for funct in self.function_list:
            res += funct
            res += self.line_break(2)
        for this_with in self.with_list:
            res += this_with
            res += self.line_break(2)
        return res

    def __add__(self, other):
        return self.__repr__() + other

    def __radd__(self, other):
        return other + self.__repr__()

    ''' print the python code '''

    def _print(self):
        print(self)

    '''return the python code as string'''

    def _return(self):
        return str(self)


'''
Class that generates the sublcass of python code 
within another class.
'''


class PySubClass(PyClass):

    def __repr__(self):
        res = self.line_break(1)
        res += self.ident() + "class %s" % (self.name,)
        for pos, inheritance in enumerate(self.inhnerit_list):
            if pos == 0:
                res += '('
            if pos > 0:
                res += ', '
            res += inheritance
        if self.inhnerit_list:
            res += ')'
        res += ':'
        res += self.line_break(1)
        for sline in self.class_lines:
            res += self.ident(2) + sline
            res += self.line_break(1)
        for sclass in self.sub_class_list:
            res += sclass
            res += self.line_break(2)
        for funct in self.function_list:
            res += funct
            res += self.line_break(2)
        return res

    def __add__(self, other):
        return self.__repr__() + other

    def __radd__(self, other):
        return other + self.__repr__()

    def _print(self):
        print(self)

    def _return(self):
        return str(self)


'''
Class generates python code functions inside or outside a class
'''


class PyFunction:

    def __init__(self):
        self.ObjectType = "Function"
        self.static_method = '@staticmethod'
        self.name = self.args = self.kwargs = ''
        self.param_list = []
        self.function_lines = []
        self.in_class = False
        self.is_static = False

    def set_name(self, val):
        self.name = val

    def set_self(self):
        self.in_class = True

    def set_static(self):
        self.is_static = True

    def set_param(self, val):
        self.param_list.append(val)

    def add_line(self, val):
        self.function_lines.append(val)

    def ident(self, val=1):
        val2 = ' '
        return ((4 * val) * val2)

    def line_break(self, val):
        return val * '\n'

    def __repr__(self):
        if self.in_class:
            if self.is_static:
                res = self.ident() + self.static_method
                res += self.line_break(1)
                res += self.ident() + 'def %s(' % (self.name,)
            else:
                res = self.ident() + 'def %s(' % (self.name,)

            if len(self.param_list) > 0:
                res += 'self, '
            else:
                res += 'self'
        else:
            res = 'def %s(' % (self.name,)
        for pos, params in enumerate(self.param_list):
            if pos > 0:
                res += ', '
            res += params
        res += '):'
        res += self.line_break(1)
        for f_line in self.function_lines:
            res += self.ident(2) + f_line + self.line_break(1)
        return res

    def __add__(self, other):
        return self.__repr__() + other

    def __radd__(self, other):
        return other + self.__repr__()

    def _print(self):
        print(self)

    def _return(self):
        return str(self)


'''
Class generates python code with inside or outside a class
'''


class PyWith:

    def __init__(self):
        self.ObjectType = "With"
        self.static_method = '@staticmethod'
        self.name = self.args = self.kwargs = self.set_as = ''
        self.param_list = []
        self.with_lines = []
        self.task_list = []
        self.in_class = False
        self.is_static = False

    def set_name(self, val):
        self.name = val

    def set_as(self, val):
        self.set_as = val

    def set_self(self):
        self.in_class = True

    def set_static(self):
        self.is_static = True

    def set_param(self, val):
        self.param_list.append(val)

    def add_line(self, val):
        self.with_lines.append(val)

    def add_task(self, val):
        self.task_list.append(val)

    def ident(self, val=1):
        val2 = ' '
        return ((4 * val) * val2)

    def line_break(self, val):
        return val * '\n'

    def __repr__(self):
        if self.in_class:
            if self.is_static:
                res = self.ident() + self.static_method
                res += self.line_break(1)
                res += self.ident() + 'with %s(' % (self.name,)
            else:
                res = self.ident() + 'with %s(' % (self.name,)

        else:
            res = 'with %s(' % (self.name,)
        for pos, params in enumerate(self.param_list):
            if pos > 0:
                res += ', '
            res += params
        if self.set_as:
            res += ') as {}:'.format(self.set_as)
        else:
            res += '):'
        res += self.line_break(2)

        for f_line in self.with_lines:
            res += self.ident(1) + f_line + self.line_break(1)

        for task in self.task_list:
            res += self.ident(1) + task + self.line_break(1)
        return res

    def __add__(self, other):
        return self.__repr__() + other

    def __radd__(self, other):
        return other + self.__repr__()

    def _print(self):
        print(self)

    def _return(self):
        return str(self)


'''
Class generates python code with inside or outside a class
'''


class PyDag:

    def __init__(self):
        self.ObjectType = "Dag"
        self.name = 'DAG'
        self.args = self.kwargs = self.operator = self.dag_id = ''
        self.param_list = []
        self.task_list = []
        self.in_class = False
        self.context = False
        self.catchup = False
        self.ident_val = 0

    def set_context(self, val=True):
        self.context = val

    def set_catchup(self, val=True):
        self.catchup = val

    def set_operator(self, val):
        self.operator = val

    def set_self(self):
        self.in_class = True

    def set_param(self, name, val):
        self.param_list.append({name: val})

    def add_task(self, val):
        self.task_list.append(val)

    def ident(self, val=1):
        self.ident_val = val
        val2 = ' '
        return (4 * val) * val2

    def line_break(self, val):
        return val * '\n'

    def set_dag_id(self, val):
        self.dag_id = val

    def set_param_value(self, val_dict):
        key = val_dict.keys()[0]
        val = val_dict.values()[0]
        if val in ('int', 'integer', 'variable', 'bool', 'dict', 'list', 'tuple'):
            # if val == 'dict':
            #     res = '{'
            #     key_dict = simplejson.loads(key)
            #     res += self.line_break(1)
            #     for k, v in key_dict.iteritems():
            #         res += '{} : {}'.format(k,v)
            #         res += ', '
            #         res += self.line_break(1)
            #     return res
            return '{}'.format(key)
        return "'{}'".format(key)

    def __repr__(self):
        if self.in_class:
            res = self.ident() + 'with {}('.format(self.name)
        else:
            res = 'with {}('.format(self.name)

        self.set_param('dag_id', {self.dag_id: 'str'})
        # res += self.line_break(1)

        if self.context:
            self.set_param('provide_context', {'True': 'bool'})
        if self.catchup:
            self.set_param('catchup', {'True': 'bool'})

        for pos, params in enumerate(self.param_list):
            for key, val_dict in params.iteritems():
                if pos > 0:
                    res += ', '
                    res += self.line_break(1)
                    res += self.ident(2)
                res += '{} = {}'.format(key, self.set_param_value(val_dict))
        else:
            res += ') as dag:'
        res += self.line_break(2)

        for task in self.task_list:
            res += self.ident(1) + task + self.line_break(1)

        return res

    def __add__(self, other):
        return self.__repr__() + other

    def __radd__(self, other):
        return other + self.__repr__()

    def _print(self):
        print(self)

    def _return(self):
        return str(self)


'''
Class generates python code with inside or outside a class
'''


class PyTask:

    def __init__(self):
        self.ObjectType = "With"
        self.name = self.args = self.kwargs = self.operator = self.task_id = ''
        self.param_list = []
        self.upstream_list = []
        self.downstream_list = []
        self.in_class = False
        self.context = False
        self.ident_val = 0

    def set_name(self, val):
        self.name = val

    def set_context(self, val=True):
        self.context = val

    def set_operator(self, val):
        self.operator = val

    def set_self(self):
        self.in_class = True

    def set_param(self, name, val):
        self.param_list.append({name: val})

    def ident(self, val=1):
        self.ident_val = val
        val2 = ' '
        return (4 * val) * val2

    def line_break(self, val):
        return val * '\n'

    def set_task_id(self, val):
        self.task_id = val

    def set_param_value(self, val_dict):
        key = val_dict.keys()[0]
        val = val_dict.values()[0]
        if val in ('int', 'integer', 'variable', 'bool', 'dict', 'list', 'tuple'):
            # if val == 'dict':
            #     res = '{'
            #     key_dict = simplejson.loads(key)
            #     res += self.line_break(1)
            #     for k, v in key_dict.iteritems():
            #         res += '{} : {}'.format(k,v)
            #         res += ', '
            #         res += self.line_break(1)
            #     return res
            return '{}'.format(key)
        return "'{}'".format(key)

    def set_downstream(self, task_obj):
        if type(task_obj).__name__ == 'instance':
            self.downstream_list.append(task_obj.name)
        else:
            self.downstream_list.append(task_obj)

    def set_upstream(self, task_obj):
        print('type', type(task_obj))
        if type(task_obj).__name__ == 'instance':
            self.upstream_list.append(task_obj.name)
        else:
            self.upstream_list.append(task_obj)

    def _print_workflow(self):
        if self.downstream_list:
            for down in self.downstream_list:
                print('{}.set_downstream({})'.format(self.name, down))
        if self.upstream_list:
            for up in self.downstream_list:
                print('{}.set_upstream({})'.format(self.name, up))

    def __repr__(self):
        if self.in_class:
            res = self.ident() + '{} = {}('.format(self.name, self.operator)
        else:
            res = '{} = {}('.format(self.name, self.operator)
        res += self.line_break(1)

        self.set_param('task_id', {self.task_id: 'str'})

        if self.context:
            self.set_param('provide_context', {'True': 'bool'})

        for pos, params in enumerate(self.param_list):
            for key, val_dict in params.iteritems():
                if pos > 0:
                    res += ', '
                    res += self.line_break(1)
                res += self.ident(2) + '{} = {}'.format(key, self.set_param_value(val_dict))
        else:
            res += ')'
        res += self.line_break(1)
        return res

    def __add__(self, other):
        return self.__repr__() + other

    def __radd__(self, other):
        return other + self.__repr__()

    def _print(self):
        print(self)

    def _return(self):
        return str(self)


'''
Class generates python code modules inside or outside a class
'''


class PyModule:
    def __init__(self):
        self.ObjectType = "Module"
        self.module_lines = []
        self.is_top = True

    def set_not_top(self):
        self.is_top = False

    def add_line(self, val):
        self.module_lines.append(val)

    def add_break(self, val=0):
        self.module_lines.append(val * '\n')

    def ident(self, val=1):
        val2 = ' '
        return (4 * val) * val2

    def line_break(self, val):
        return val * '\n'

    def __repr__(self):
        res = ''
        if self.is_top:
            res = '# -*- coding: utf-8 -*-'
            res += self.line_break(1)
        for line in self.module_lines:
            res += str(line) + self.line_break(1)
        res += self.line_break(1)
        return res

    def _print(self):
        pass

    def _return(self):
        return str(self)
