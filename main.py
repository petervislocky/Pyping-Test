from reference_text import REFERENCE_TEXT
from blessed import Terminal
import input_handler
import renderer


def main():
    term = Terminal()
    typed_text = []
    backspace_count = 0

    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        renderer.render_text(typed_text, REFERENCE_TEXT, term)

        for key in input_handler.capture_typing(term):
            if key is None: #if key is None then ESC was pressed
                print(term.move_down + 'Test canceled')
                return
            
            if key.name == 'KEY_BACKSPACE':
                backspace_count += 1
                if typed_text:
                    typed_text.pop()
            
            if len(typed_text) < len(REFERENCE_TEXT) and key.name != 'KEY_BACKSPACE':
                if key.name not in ('KEY_ESCAPE', 'KEY_ENTER'):
                    typed_text.append(str(key))

            renderer.render_text(typed_text, REFERENCE_TEXT, term)
            
            if ''.join(typed_text) == ''.join(REFERENCE_TEXT):
                break

if __name__ == '__main__':
    main()
