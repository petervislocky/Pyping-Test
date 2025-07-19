def capture_typing(term):
    """takes a blessed terminal object and uses cbreak to capture user keystrokes,
    if user presses esc, returns None, else it yields each keystroke one. This method
    becomes an iterable because of the yield"""
    with term.cbreak():
        while True:
            key = term.inkey()
            if key.name == 'KEY_ESCAPE':
                yield None # I'm yielding None because return stops an iterable object like this one so None doesn't get returned
            yield key

