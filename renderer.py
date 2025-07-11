from rich.console import Console
from rich.text import Text

console = Console()

def render_text(typed_text, reference_text, term):
    text = Text()

    for i, char in enumerate(reference_text):
        if i < len(typed_text):
            if typed_text[i] == char:
                text.append(char, style='green')
            else:
                text.append(char, style='red')
        else:
            text.append(char, style='dim')

    print(term.home + term.clear, end='')
    console.print(text)
