import numpy as np
import pandas as pd

from great_expectations.core.batch import Batch
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.core.expectation_validation_result import (
    ExpectationValidationResult,
)
from great_expectations.execution_engine import PandasExecutionEngine
from great_expectations.expectations.core.expect_column_mean_to_be_between import (
    ExpectColumnMeanToBeBetween,
)


def test_expect_column_mean_to_be_between_impl():
    df = pd.DataFrame({"a": [2, 2, 2]})
    expectationConfiguration = ExpectationConfiguration(
        expectation_type="expect_column_mean_to_be_between",
        kwargs={"column": "a", "min_value": 0, "max_value": 4},
    )
    expectation = ExpectColumnMeanToBeBetween(expectationConfiguration)
    batch = Batch(data=df)
    result = expectation.validate(
        batches={"batch_id": batch}, execution_engine=PandasExecutionEngine()
    )
    assert result == ExpectationValidationResult(success=True,)