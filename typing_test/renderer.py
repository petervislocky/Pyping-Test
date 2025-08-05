import time

from blessed import Terminal
from rich.text import Text
from rich.console import Console


# TODO: Use this logic to implement a blinking cursor. Run the renderers
# and input_handler in async so the rendering can refresh independent
# of keystrokes
def blink_cursor() -> bool:
    """
    Blinks the cursor twice a second.

    `time.time` converted to int truncates the decimal value, when I
    multiply by 2 before truncating the decimal value the value will get
    to the next whole number twice as fast, meaning every half second
    the value % 2 will = 0. Without multiplying by 2, it would flip to 0
    every 1 second.
    """
    return int(time.time() * 2) % 2 == 0


# TODO: Add async here
def render_typing_test(
    typed_text: list[str], reference_text: list[str], term: Terminal, console: Console
) -> None:
    """Renderer for the perfect typing test graphics"""
    text = Text()
    error_mode = False

    for i, char in enumerate(reference_text):
        if i < len(typed_text):
            if error_mode:
                text.append(char, style="bold red on pale_violet_red1")
            else:
                if typed_text[i] == char:
                    text.append(char, style="bold bright_green")
                else:
                    error_mode = True
                    text.append(char, style="bold red on pale_violet_red1")
        else:
            text.append(char, style="bold grey42")

    print(term.home + term.clear, end="")
    console.print(text)


def render_timed_test(
    typed_text: list[str], reference_text: list[str], term: Terminal, console: Console
) -> None:
    """Renderer for the timed typing test"""
    text = Text()

    for i, char in enumerate(reference_text):
        if i < len(typed_text):
            if typed_text[i] == char:
                text.append(char, style="bold bright_green")
            else:
                text.append(char, style="bold red on pale_violet_red1")
        else:
            text.append(char, style="bold grey42")

    print(term.home + term.clear, end="")
    console.print(text)
