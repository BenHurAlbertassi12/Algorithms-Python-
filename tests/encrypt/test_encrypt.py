import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('Tom Marvolo Riddle', '5')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 3)

    assert encrypt_message('Tom Marvolo Riddle', 10) == 'elddiR o_lovraM moT'
    assert encrypt_message('Tom Marvolo Riddle', 5) == 'M moT_elddiR olovra'
    assert encrypt_message('Tom Marvolo Riddle', 3) == 'moT_elddiR olovraM '
    assert encrypt_message('Tom Marvolo Riddle', -3) == 'elddiR olovraM moT'
