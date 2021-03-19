from flask_restful import abort


class GetMessage:
    """
    This class returns the completed message the ship sent.
    """

    def get_message(self, kenobi_message, skywalker_message, sato_message):
        # check the lag
        kenobi_message_size = len(kenobi_message)
        skywalker_message_size = len(skywalker_message)
        sato_message_size = len(sato_message)
        message_size = min(kenobi_message_size, skywalker_message_size, sato_message_size)
        while (
                message_size != kenobi_message_size
                or message_size != skywalker_message_size
                or message_size != sato_message_size
        ):
            if not message_size == kenobi_message_size:
                del kenobi_message[0]
            if not message_size == skywalker_message_size:
                del skywalker_message[0]
                skywalker_message_size -= 1
            if not message_size == sato_message_size:
                del sato_message[0]
                sato_message_size -= 1

        # check missing words
        scape_value = " "
        message_list = []
        message = " "
        for words_split in zip(kenobi_message, skywalker_message, sato_message):
            words_split = {x for x in words_split if x != scape_value}
            if not len(words_split) == 1:
                abort(404, error_message='Unable to get the secret message')
            else:
                message_list += words_split
        return message.join(message_list)
