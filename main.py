import time

from blessed import Terminal
from rich.console import Console

from reference_text import ReferenceText
import settings
import input_handler
import renderer
import metrics


def main():
    term = Terminal()
    console = Console()
    settings.create_default_settings()
    settings_json = settings.read_settings()
    rf = ReferenceText(settings_json['word_count']) 
    reference_text = rf.get_selected_chars()

    typed_text = []
    backspace_count = 0
    start_time = 0
    

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        renderer.render_typing_test(typed_text, reference_text, term)

        for key in input_handler.capture_typing(term):
            if key is None: #if key is None then ESC was pressed
                print(term.move_down + 'Test canceled')
                return # Exits the entire main method
            
            if key.name == 'KEY_BACKSPACE':
                backspace_count += 1
                if typed_text:
                    typed_text.pop()
            
            if len(typed_text) < len(reference_text) and key.name != 'KEY_BACKSPACE':
                if key.name not in ('KEY_ESCAPE', 'KEY_ENTER'):
                    typed_text.append(str(key))

            if start_time == 0 and key.name not in ('KEY_BACKSPACE', 'KEY_ESCAPE', 'KEY_ENTER'):
                start_time = time.time()

            renderer.render_typing_test(typed_text, reference_text, term)
            
            if ''.join(typed_text) == ''.join(reference_text):
                break

    end_time = time.time()
    time_elapsed_sec = end_time - start_time
    time_elapsed_min = time_elapsed_sec / 60

    console.print(f'[bold green]Time:[/] {time_elapsed_sec:.2f} seconds')
    console.print(
        f'[bold red]Speed:[/] {metrics.wpm(len(reference_text), time_elapsed_min):.2f} WPM'
        )
    console.print(
        f'[bold blue]Accuracy:[/] ' 
        f'{metrics.mistakes_count(backspace_count, len(reference_text), len(typed_text)):.2f}%'
        )

if __name__ == '__main__':
    main()
