from enum import Enum


class TokenClass(Enum):
    KEYWORD = 1,
    OPERATOR = 2,
    DELIMITER = 3,
    INT_CONSTANT = 4,
    FLOAT_CONSTANT = 5
    TEXTICAL_CONSTANT = 6,
    ID = 7,
    COMMENT = 8


class Token:
    def __init__(self, token_class: TokenClass, token_value):
        self.token_class = token_class
        self.token_value = token_value
    def __str__(self) -> str:
        return f'<Token class: {self.token_class}, value: {self.token_value}>'
