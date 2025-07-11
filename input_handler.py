def capture_typing(term):
    """takes a blessed terminal object and uses cbreak to capture user keystrokes,
    if user presses esc, returns None, else it yields each keystroke one. This method
    becomes an iterable because of the yield"""
    with term.cbreak():
        while True:
            key = term.inkey()
            if key.name == 'KEY_ESCAPE':
                return None
            yield key

def input_list(term):
    """takes a blessed terminal object to pass to capture_typing, iterates through all keys
    returned from capture_typing and appends them to a list, if backspace is pressed it pops
    the list, returns the list of typed text and count of backspace pressed"""
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
