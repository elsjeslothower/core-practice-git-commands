import pytest


def always_returns_true():
    return True
    print("Hi Geiselle!!")
    print("Nice working with you too!!")


def test_always_returns_true():
    assert always_returns_true()
