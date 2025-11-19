import pytest

from presidio_anonymizer.operators import Initial
from presidio_anonymizer.entities import InvalidParamError

def test_correct_name():
    assert Initial().operator_name() == "initial"

@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("     Eastern    Michigan   University ", "E. M. U.")
    ],
)
def test_given_value_for_initial(input_text, initials):
    text = Initial().operate(input_text)
    assert text == initials