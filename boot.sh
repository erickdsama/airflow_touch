#!/bin/bash
exec gunicorn -b :5000 --access-logfile - --error-logfile - main:app  --reload
