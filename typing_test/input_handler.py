from typing import Iterator

from blessed import Terminal
from blessed.keyboard import Keystroke


# TODO: add async here
def capture_typing(term: Terminal) -> Iterator[None | Keystroke]:
    """
    Takes a blessed terminal object and uses cbreak to capture user
    keystrokes.

    If user presses esc, yields None, else it yields each
    keystroke one at a time.
    """
    with term.cbreak():
        while True:
            key = term.inkey()
            if key.name == "KEY_ESCAPE":
                # I'm yielding None because return stops an iterable
                # object like this one so None wouldn't get returned
                yield None
            yield key
