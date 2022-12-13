def response(message):
    """ Lackadasical teenager response simulator. """
    message = message.strip() # Take away all whitespace from beginning and end of a string

    if not message:
        return "Fine. Be that way!"

    is_question = message.endswith("?")
    is_shouting = message.isupper()

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_shouting:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."

    return "Whatever."
