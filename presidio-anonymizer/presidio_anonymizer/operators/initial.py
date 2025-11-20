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
            initials += self._get_first_alphanumeric(self, word) + ". " # retrieve first letter of each word
        return initials[:-1] # delete last empty space

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
    
    @staticmethod
    def _get_first_alphanumeric(self, word) -> str:
        initial = "" # tracks chars to be included in initial
        for ch in word: # iterate through letters
            if ch.isalnum(): # found alphanumeric char
                initial += ch.upper() # ensure uppercase
                break # initial is complete (break out of loop)
            else: # preserve previous non-alphanumeric chars
                initial += ch
        return initial
                