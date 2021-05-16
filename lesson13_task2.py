def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


get_speak_func(0.7)
text = get_speak_func(0.3)
print(text('hello'))
