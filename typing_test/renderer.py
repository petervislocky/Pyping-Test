from rich.text import Text


def render_typing_test(typed_text, reference_text, term, console):
    text = Text()
    error_mode = False

    for i, char in enumerate(reference_text):
        if i < len(typed_text):
            if error_mode:
                text.append(char, style='bold red on pale_violet_red1')
            else:
                if typed_text[i] == char:
                    text.append(char, style='bold bright_green')
                else:
                    error_mode = True
                    text.append(char, style='bold red on pale_violet_red1')
        else:
            text.append(char, style='bold grey42')

    print(term.home + term.clear, end='')
    console.print(text)

# Render a pause menu, if needed, with the method and list below
# menu_options = ['Resume', 'Options', 'Exit']
#
# def pause_menu(term):
#     selected = 0
#     with term.cbreak(), term.hidden_cursor():
#         while True:
#             print(term.home + term.clear)
#
#             height, width = term.height, term.width
#             box_top = height // 2 - 3
#             box_left = width // 2 - 10
#
#             for y in range(box_top, box_top + 7):
#                 print(term.move_xy(box_left, y) + ' ' * 20)
#
#             print(term.move_xy(box_left + 5, box_top) + 'Pause Menu')
#
#             for idx, option in enumerate(menu_options):
#                 style = term.reverse if idx == selected else ''
#                 print(term.move_xy(box_left + 4, box_top + 2 + idx) + style + option + term.normal)
#
#             key = term.inkey()
#             if key.name == 'KEY_UP':
#                 selected = (selected - 1) % len(menu_options)
#             elif key.name == 'KEY_DOWN':
#                 selected = (selected + 1) % len(menu_options)
#             elif key.name == 'KEY_ENTER' or key == '\n':
#                 return menu_options[selected]
#                 # This may not clear the pause menu after an option is
#                 # picked, haven't tested yet

