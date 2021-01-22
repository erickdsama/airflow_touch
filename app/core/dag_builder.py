from datetime import timedelta

from .dag_writer import PyModule, PyWith, PyTask, PyDag


class DAG:

    default_dag_schema = {
        "imports": {
            "datetime": ["timedelta"],
            "airflow": ["DAG"],
            "airflow.utils.dates": ["days_ago"],
            "lkf_operator": ["CreateAndAssignTask", "LKFLogin"],
        },
        "args": {
            'owner': 'airflow',
            'depends_on_past': False,
            # 'start_date': days_ago(0),
            'lkf_user': 'test_lkf_username',
            'email': ['josepato@linkaform.com'],
            'email_on_failure': True,
            'email_on_retry': True,
            'name': 'test',
            'retries': 2,
            'retry_delay': timedelta(minutes=5),
            'provide_context': True,
            'init_var': False
        }
    }

    def __init__(self):
        self._module = PyModule()
        self._dag = PyDag()

    def __write_import(self, package, modules):
        modules_to_import = ",".join(modules)
        template_import = "from {} import {}"
        self._module.add_line(template_import.format(package, modules_to_import))
        self._module.add_break()

    def __default_imports(self):
        imports_schema = self.default_dag_schema.get("imports")
        for package, modules in imports_schema.items():
            self.__write_import(package, modules)
        self._module.add_break()

    def __define_imports(self, **kwargs):
        self.__default_imports()
        if kwargs:
            for package, modules in kwargs.items():
                self.__write_import(package, modules)
            self._module.add_break()

    def __define_arguments(self, **kwargs):
        default_arguments = self.default_dag_schema.get("args")
        if kwargs:
            for key, value in kwargs.items():
                default_arguments[key] = value

        self._module.add_line("default_args = " + str(default_arguments))
        self._module.add_break()

    def __set_params(self, params):
        self._module.add_line("params = " + str(params))

    def create_dag(self, json_params):
        # create imports
        imports = json_params.get("imports", {})
        self.__define_imports(**imports)

        # arguments
        args = json_params.get("args", {})
        self.__define_arguments(**args)

        # params
        params = json_params.get("params", {})
        self.__set_params(params)
        self._dag.set_dag_id()














