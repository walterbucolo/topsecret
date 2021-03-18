
from topsecret.services.message_service import GetMessage


def test_it_should_return_the_message_from_a_message_with_missing_words():
    message = GetMessage()
    kenobi_message = ["This", " ", " ", "message"]
    skywalker_message = [" ", "is", " ", " "]
    sato_message = [" ", " ", "a", " "]
    message = message.get_message(
        kenobi_message,
        skywalker_message,
        sato_message
    )
    assert message == "This is a message"


def test_it_should_return_the_message_from_a_message_with_lag():
    message = GetMessage()
    kenobi_message = ["This", " ", "a", "message"]
    skywalker_message = [" ", " ", "is", " ", "message"]
    sato_message = [" ", " ", " ", " ", "a", " "]
    message = message.get_message(
        kenobi_message,
        skywalker_message,
        sato_message
    )
    assert message == "This is a message"
