from reference_text import reference_text
from blessed import Terminal
import input_handler
import renderer
import time


def main():
    term = Terminal()
    typed_text = []
    backspace_count = 0

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        renderer.render_text(typed_text, reference_text, term)
        
        start_time = 0

        for key in input_handler.capture_typing(term):
            if key is None: #if key is None then ESC was pressed
                print(term.move_down + 'Test canceled')
                return
            
            if key.name == 'KEY_BACKSPACE':
                backspace_count += 1
                if typed_text:
                    typed_text.pop()
            
            if len(typed_text) < len(reference_text) and key.name != 'KEY_BACKSPACE':
                if key.name not in ('KEY_ESCAPE', 'KEY_ENTER'):
                    typed_text.append(str(key))

            if start_time == 0 and key.name not in ('KEY_BACKSPACE', 'KEY_ESCAPE', 'KEY_ENTER'):
                start_time = time.time()

            renderer.render_text(typed_text, reference_text, term)
            
            if ''.join(typed_text) == ''.join(reference_text):
                break
    end_time = time.time()
    time_elapsed_sec = end_time - start_time
    time_elapsed_min = time_elapsed_sec / 60

    print(f'{time_elapsed_sec:.3f} seconds')

if __name__ == '__main__':
    main()
