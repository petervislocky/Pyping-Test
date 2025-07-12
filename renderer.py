from rich.console import Console
from rich.text import Text

console = Console()

def render_text(typed_text, reference_text, term):
    text = Text()
    error_mode = False

    for i, char in enumerate(reference_text):
        if i < len(typed_text):
            if error_mode:
                text.append(char, style='bold bright_red on pale_violet_red1')
            else:
                if typed_text[i] == char:
                    text.append(char, style='bold bright_green')
                else:
                    error_mode = True
                    text.append(char, style='bold bright_red on pale_violet_red1')
        else:
            text.append(char, style='bold dim')

    print(term.home + term.clear, end='')
    console.print(text)
