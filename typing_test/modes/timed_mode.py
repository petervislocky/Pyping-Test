import time

from blessed import Terminal
from rich.console import Console

from reference_text import ReferenceText
import renderer
import input_handler
import metrics


# TODO: Add a live timer
def run_timed_mode(
    term: Terminal,
    console: Console,
    rf: ReferenceText,
    reference_text: list[str],
    duration_sec: int,
) -> None:
    typed_text = []
    start_time = 0

    # Because `reference_text` can (and does here) take None as a value
    # for `word_count`, reference_text can (will) initially be None when
    # passed to this method and therefore needs to be generated below
    # in order to have initial text to render
    if not reference_text:
        rf.gen_reference_text(100)
        reference_text = rf.get_selected_chars()

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

            # If user runs out of text to type more is generated here
            if len(typed_text) == len(reference_text) - 15:
                rf.gen_reference_text(50)
                reference_text = rf.get_selected_chars()

    mistakes = metrics.find_mistakes(typed_text, reference_text)
    time_elapsed_seconds = time.time() - start_time
    time_elapsed_minutes = time_elapsed_seconds / 60

    console.print(f"[bold green]Timed mode:[/] {int( time_elapsed_seconds )} seconds")
    console.print(
        f"[bold red]Words per minute:[/] {metrics.adjusted_wpm(len(typed_text), mistakes, time_elapsed_minutes):.2f} wpm"
    )
    console.print(
        f"[bold dark_red]Raw words per minute:[/] {metrics.wpm(len(typed_text),time_elapsed_minutes):.2f} wpm"
    )
    console.print(
        f"[bold blue]Accuracy:[/] "
        f"{metrics.timed_accuracy(typed_text, reference_text):.2f} %"
    )
