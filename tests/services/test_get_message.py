
import unittest
from werkzeug.exceptions import HTTPException
from topsecret.services.message_service import GetMessage


class TestMessageService(unittest.TestCase):
    def test_it_should_return_the_message_from_a_message_with_missing_words(self):
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

    def test_it_should_return_the_message_from_a_message_with_lag(self):
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

    def test_it_should_fail_with_different_words_in_the_same_position(self):
        message = GetMessage()
        kenobi_message = ["This", " ", "a", "message"]
        skywalker_message = ["Fake", " ", " ", "message"]
        sato_message = [" ", " ", " ", " ", "a", " "]
        with self.assertRaises(HTTPException) as e:
            message.get_message(
                kenobi_message,
                skywalker_message,
                sato_message
            )
        assert e.exception.code == 404

    def test_it_should_fail_if_all_words_are_scape_values(self):
        message = GetMessage()
        kenobi_message = [" ", " ", " ", " "]
        skywalker_message = [" ", " ", " ", " "]
        sato_message = [" ", " ", " ", " ", " ", " "]
        with self.assertRaises(HTTPException) as e:
            message.get_message(
                kenobi_message,
                skywalker_message,
                sato_message
            )
        assert e.exception.code == 404

