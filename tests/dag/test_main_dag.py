import unittest
from airflow.models import DagBag
from unittest.mock import Mock, MagicMock
import pytest
@pytest.fixture
def dagbag():
        # Load the DAGs from the default Airflow folder
        dagbag = DagBag()
        print(dagbag.dags)
        yield dagbag

def test_dag(dagbag):
        print(dagbag.dags)
        assert dagbag.dags. is not None