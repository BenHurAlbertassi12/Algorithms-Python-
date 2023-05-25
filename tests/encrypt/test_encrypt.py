import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('Tom Marvolo Riddle', '5')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 5)

    assert encrypt_message('Tom Marvolo Riddle', 10) == 'i am lord voldemort'
    assert encrypt_message('Tom Marvolo Riddle', 5) == 'i am lord vold_emort'
