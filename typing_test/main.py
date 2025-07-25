import time
import argparse

from blessed import Terminal
from rich.console import Console

from reference_text import ReferenceText
import settings
import input_handler
import renderer
import metrics


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--word-count', '-w',
        type=int,
        help='overrides word count for the current run'
    )
    parser.add_argument(
        '--difficulty', '-d',
        choices=['easy', 'medium', 'hard'],
        help='overrides difficulty for the current run'
    )
    parser.add_argument(
        '--show-config',
        action='store_true',
        help='opens settings.json in text editor to edit it'
    )
    return parser.parse_args()

def main():
    # parsing args first to bypass potential config errors
    args = parse_args()
    # and handling show config before reading the config as well
    if args.show_config:
        settings.show_config_file()
        return

    term = Terminal()
    console = Console()
    
    # create_default_settings will only create a default JSON if one
    # does not already exist
    settings.create_default_settings()
    # configuration is the programs copy of the JSON once its read, so
    # can be temporarily overwritten for the runtime of the program
    configuration = settings.read_settings()
    settings.check_settings_validity(configuration)

    # handling remaining args
    if args.word_count:
        configuration['word_count'] = args.word_count
    if args.difficulty:
        configuration['difficulty'] = args.difficulty

    rf = ReferenceText(configuration['word_count'], configuration['difficulty']) 
    reference_text = rf.get_selected_chars()

    typed_text = []
    backspace_count = 0
    start_time = 0

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        renderer.render_typing_test(typed_text, reference_text, term, console)

        for key in input_handler.capture_typing(term):
            if key is None: #if key is None then ESC was pressed
                print(term.move_down + 'Test canceled')
                return # Exits the entire main method
            
            if key.name == 'KEY_BACKSPACE':
                backspace_count += 1
                typed_text.pop()
            
            if len(typed_text) < len(reference_text) and key.name not in ('KEY_ESCAPE', 'KEY_ENTER', 'KEY_BACKSPACE'):
                typed_text.append(str(key))

            if start_time == 0 and key.name not in ('KEY_BACKSPACE', 'KEY_ESCAPE', 'KEY_ENTER'):
                start_time = time.time()

            renderer.render_typing_test(typed_text, reference_text, term, console)
            
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
