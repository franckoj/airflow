import pytest
from airflow.models import DagBag

import os
import shutil

import pytest

os.environ["AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS"] = "False"  # Don't want anything to "magically" work
os.environ["AIRFLOW__CORE__LOAD_EXAMPLES"] = "False"  # Don't want anything to "magically" work
os.environ["AIRFLOW__CORE__UNIT_TEST_MODE"] = "True"  # Set default test settings, skip certain actions, etc.
os.environ["AIRFLOW_HOME"] = os.path.dirname(os.path.dirname(__file__))  # Hardcode AIRFLOW_HOME to root of this project


def test_no_import_errors():
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  assert len(dag_bag.import_errors) == 0, "No Import Failures"


def test_retries_present():
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  for dag in dag_bag.dags:
      retries = dag_bag.dags[dag].default_args.get('retries', [])
      error_msg = 'Retries not set to 2 for DAG {id}'.format(id=dag)
      assert retries == 2, error_msg