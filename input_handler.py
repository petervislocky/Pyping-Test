
def capture_typing(term):
    with term.cbreak():
        while True:
            key = term.inkey()
            if key.name == 'KEY_ESCAPE':
                return None
            yield key

def input_list(term):
    typed_text = []
    backspace_pressed = 0
    for key in capture_typing(term):
        if key is None:
            break
        if key.name == 'KEY_BACKSPACE':
            backspace_pressed += 1
            if typed_text:
                typed_text.pop()
        elif key.name not in ('KEY_ESCAPE', 'KEY_ENTER'):
            typed_text.append(str(key))

    return typed_text, backspace_pressed
