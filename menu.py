from blessed import Terminal
# not doing it right now, but get rid of the import and terminal object
# and pass it in the main method
# also move all this to renderer.py
term = Terminal()

menu_options = ['Resume', 'Options', 'Exit']

def pause_menu(term):
    selected = 0
    with term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)

            height, width = term.height, term.width
            box_top = height // 2 - 3
            box_left = width // 2 - 10

            for y in range(box_top, box_top + 7):
                print(term.move_xy(box_left, y) + ' ' * 20)

            print(term.move_xy(box_left + 5, box_top) + 'Pause Menu')

            for idx, option in enumerate(menu_options):
                style = term.reverse if idx == selected else ''
                print(term.move_xy(box_left + 4, box_top + 2 + idx) + style + option + term.normal)

            key = term.inkey()
            if key.name == 'KEY_UP':
                selected = (selected - 1) % len(menu_options)
            elif key.name == 'KEY_DOWN':
                selected = (selected + 1) % len(menu_options)
            elif key.name == 'KEY_ENTER' or key == '\n':
                return menu_options[selected]

if __name__ == '__main__':
    print(term.enter_fullscreen)
    result = pause_menu(term)
    print(term.exit_fullscreen + term.clear + term.move(0,0), end='')
    print(f'You selected {result}')
