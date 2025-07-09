import input_handler
from reference_text import REFERENCE_TEXT
from blessed import Terminal


def main():
    term = Terminal()
    mistakes = 0
    print(''.join(REFERENCE_TEXT))
    typed_text, backspace_pressed = input_handler.input_list(term) 
    # print(typed_text) #debugging
    for i, char in enumerate(typed_text):
        if i >= len(REFERENCE_TEXT):
            mistakes += 1
            break
        if char == REFERENCE_TEXT[i]:
            continue
        else:
            mistakes += 1            
    final_mistakes = mistakes + backspace_pressed
    print(f'Completed with {final_mistakes} mistakes')

if __name__ == '__main__':
    main()
