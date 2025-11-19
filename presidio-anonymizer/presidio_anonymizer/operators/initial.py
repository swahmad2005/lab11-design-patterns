"""Replaces the PII text entity with initals."""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Converts the identified PII text to its initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: an empty value."""
        words = text.split() # identify all words
        initials = "" # stores text to return
        for word in words:
            initials += word[0] + ". " # retrieve first letter of each word
        return initials[:-1] # delete last empty space

    def validate(self, params: Dict = None) -> None:
        """Redact does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize