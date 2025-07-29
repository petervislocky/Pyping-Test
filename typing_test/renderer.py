from blessed import Terminal
from rich.text import Text
from rich.console import Console


def render_typing_test(
    typed_text: list[str], reference_text: list[str], term: Terminal, console: Console
):
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


# TODO: count mistakes in this method and return the number
def render_timed_test(
    typed_text: list[str], reference_text: list[str], term: Terminal, console: Console
):
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
