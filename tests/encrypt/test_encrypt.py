from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "kikuti"

    with pytest.raises(TypeError):
        encrypt_message(2, "deve retornar erro")

    assert encrypt_message(message, -1) == "itukik"

    assert encrypt_message(message, 1) == "k_ituki"

    assert encrypt_message(message, 2) == "ituk_ik"
