import time

from blessed import Terminal
from rich.console import Console

import renderer
import input_handler
import metrics


# TODO finish printing the metrics


# TODO count mistakes in the timed_test renderer method and return it to
# this method to calculate the adjusted wpm
def run_timed_mode(
    term: Terminal, console: Console, reference_text: list[str], duration_sec: int = 30
):
    typed_text = []
    start_time = 0

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        renderer.render_timed_test(typed_text, reference_text, term, console)

        for key in input_handler.capture_typing(term):
            if key is None:  # None means key is ESC
                print(term.move_down + "Test canceled")
                return

            current_time = time.time()
            if current_time - start_time >= duration_sec:
                break

            if key.name == "KEY_BACKSPACE":
                if typed_text:
                    typed_text.pop()
                typed_text.append(str(key))

            if len(typed_text) < len(reference_text) and key.name not in (
                "KEY_ESCAPE",
                "KEY_ENTER",
                "KEY_BACKSPACE",
            ):
                typed_text.append(str(key))

                if start_time == 0:
                    start_time = time.time()

            renderer.render_timed_test(typed_text, reference_text, term, console)

            if "".join(typed_text) == "".join(reference_text):
                break

    elapsed = time.time() - start_time
