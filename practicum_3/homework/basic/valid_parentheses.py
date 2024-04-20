from typing import Any

import yaml
import numpy as np
from numpy.typing import NDArray
#from src.common import ProblemCase


class Stack:
    def __init__(self, max_n: int, dtype: Any) -> None:
        self._array: NDArray = np.zeros((max_n,), dtype=dtype)  # internal array
        self._top_i: int = -1  # index of the most recently inserted element

    def empty(self) -> bool:
        return self._top_i == -1

    def push(self, x: Any) -> None:
        self._array[self._top_i + 1] = x
        self._top_i += 1


    def pop(self) -> Any:
        x = self._array[self._top_i]
        self._array[self._top_i] = 0
        self._top_i -= 1
        return x



class StackUnderflowException(BaseException):
    pass


class StackOverflowException(BaseException):
    pass


def get_starting_symbol(sym: str) -> str:
    if sym == ")":
        return "("
    elif sym == "]":
        return "["
    elif sym == "}":
        return "{"
    else:
        raise ValueError(f'Unknown parenthesis: "{sym}"')


def are_parentheses_valid(s: str) -> bool:
    stack = Stack(len(s), dtype=str)
    open = "([{"
    close = ")]}"
    for i in s:
        if i in open:
            stack.push(i)
        elif i in close:
            previous = get_starting_symbol(i)
            if stack.empty() or stack.pop() != previous:
                return False
    return stack.empty()


if __name__ == "__main__":
    # Let's solve Valid Parentheses problem from leetcode.com:
    # https://leetcode.com/problems/valid-parentheses/
    cases = []
    with open("C://Users//Alexandra//Documents//Универ//Algos//spbu-fundamentals-of-algorithms//practicum_3//homework//basic//valid_parentheses_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = are_parentheses_valid(c["input"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
