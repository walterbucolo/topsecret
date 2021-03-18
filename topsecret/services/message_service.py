

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
        for split_words in zip(kenobi_message, skywalker_message, sato_message):
            for word in split_words:
                if not word == scape_value:
                    message_list.append(word)
                    break
        return " ".join(message_list)
