import time

from blessed import Terminal
from rich.console import Console

import renderer
import input_handler
import metrics


def run_perfect_mode(
    term: Terminal, console: Console, reference_text: list[str]
) -> None:
    typed_text = []
    backspace_count = 0
    start_time = 0

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        # Initial render call here renders the grey reference text
        renderer.render_typing_test(typed_text, reference_text, term, console)

        for key in input_handler.capture_typing(term):
            if key is None:  # if key is None then ESC was pressed
                print(term.clear + "Test canceled")
                return  # Exits the entire main method

            # backpace logic
            if key.name == "KEY_BACKSPACE" and typed_text:
                backspace_count += 1
                typed_text.pop()

            # ensuring only characters are added to typed_text list
            if len(typed_text) < len(reference_text) and key.name not in (
                "KEY_ESCAPE",
                "KEY_ENTER",
                "KEY_BACKSPACE",
            ):
                typed_text.append(str(key))

                # start time only after first key press
                if start_time == 0:
                    start_time = time.time()

            # This render call in the loop essentially refreshes the new
            # image every time a key is pressed
            renderer.render_typing_test(typed_text, reference_text, term, console)

            if "".join(typed_text) == "".join(reference_text):
                break

    end_time = time.time()
    time_elapsed_sec = end_time - start_time
    time_elapsed_min = time_elapsed_sec / 60

    console.print(f"[bold green]Time:[/] {time_elapsed_sec:.2f} seconds")
    console.print(
        f"[bold red]Speed:[/] {metrics.wpm(len(reference_text), time_elapsed_min):.2f} WPM"
    )
    console.print(
        f"[bold blue]Accuracy:[/] "
        f"{metrics.accuracy(backspace_count, len(reference_text), len(typed_text)):.2f}%"
    )
