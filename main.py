import pytest


def always_returns_true():
    print("Nice working with you!!!")
    return True
    print("Hi Geiselle!!")

    print("Helloooooooooo")


def test_always_returns_true():
    assert always_returns_true()
