import time

from blessed import Terminal
from rich.console import Console

import renderer
import input_handler
import metrics


def run_timed_mode(
    term: Terminal, console: Console, reference_text: list[str], duration_sec: int = 30
):
    typed_text = []
    start_time = 0
    mistakes = 0

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        renderer.render_timed_test(typed_text, reference_text, term, console)

        for key in input_handler.capture_typing(term):
            if key is None:  # None means key is ESC
                print(term.move_down + "Test canceled")
                return

            current_time = time.time()

            if start_time and (current_time - start_time >= duration_sec):
                break

            if key.name == "KEY_BACKSPACE":
                if typed_text:
                    typed_text.pop()

            if len(typed_text) < len(reference_text) and key.name not in (
                "KEY_ESCAPE",
                "KEY_ENTER",
                "KEY_BACKSPACE",
            ):
                typed_text.append(str(key))

                if start_time == 0:
                    start_time = time.time()

            renderer.render_timed_test(typed_text, reference_text, term, console)
            # mistakes only counts mistakes that were not corrected
            mistakes = metrics.count_mistakes(typed_text, reference_text)

            if "".join(typed_text) == "".join(reference_text):
                break

    time_elapsed_seconds = time.time() - start_time
    time_elapsed_minutes = time_elapsed_seconds / 60

    console.print(f"[bold green]Timed mode:[/] {time_elapsed_seconds:.2f}")
    console.print(
        f"[bold red]WPM:[/] {metrics.adjusted_wpm(len(typed_text), mistakes, time_elapsed_minutes):.2f}"
    )
    console.print(
        f"[bold blue]Accuracy:[/] "
        f"{metrics.accuracy(mistakes, len(reference_text), len(typed_text)):.2f}%"
    )
