def response(message):
""" Lackadasical teenager response simulator. """
    message = message.strip()
    
    if not message:
        return "Fine. Be that way!"
    
    if is_shouting(message) and is_question(message):
        return "Calm down, I know what I'm doing!"
    
    if is_shouting(message):
        return "Whoa, chill out!"
    
    if is_question(message):
        return "Sure."

    return "Whatever."

def is_question(message):
    return message.endswith("?")

def is_shouting(message):
    return message.isupper()
