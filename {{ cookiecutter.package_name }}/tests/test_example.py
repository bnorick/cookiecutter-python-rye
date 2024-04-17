import pytest
from expecter import expect


def describe_foobar():

    def it_can_pass(expect):
        expect(2 + 3) == 5

    def it_can_fail(expect):
        expect("TODO: write some tests").does_not_contain("TODO")
