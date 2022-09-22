import pytest

from symbol import pass_stmt


def always_returns_true():
    print("Nice working with you!!!")
    return True
    print("Hi Geiselle!!")

    pass
    print("Helloooooooooo")


def test_always_returns_true():
    assert always_returns_true()
