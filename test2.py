import curses
from curses import wrapper

template = 'dfjkl\n'

char_list = []
# Ta biblioteka nie tyle pozwala na lepsze edytowanie terminala
# co raczej tworzy w nim swoj wlasny ekran tak jakby
# inicjalizuje sie to troche tak jak w pyqt albo cos no nie
def main(stdscr):
    stdscr.addstr(template)
    while len(char_list) < len(template):
        c = stdscr.getkey()
        if c == 'q':
            break  # Exit the while loop
        elif c == '\n':
            pass  # IGNORUJE JEBANE ENTERY
        elif c == '\x08':
            stdscr.delch(0, len(char_list) - 1) # Usuwanie ostatniego znaku tak z listy jak i z konsoli
            if char_list:
                char_list.pop()
            stdscr.refresh()
        else:
            char_list.append(c)  # Dodaje wpisany klawisz do listy i sprawdza czy zgadza sie z templatem
            if char_list[-1] == template[len(char_list) - 1]:
                stdscr.addch(c)  # wypisuje poprawny
            else:
                stdscr.standout()  # Wypisuje ze bledny
                stdscr.addch(c)
                stdscr.standend()
                # char_list.pop()


wrapper(main)
print(char_list)

# Trzeba będzie chyba przepisać całego maina jeżeli chcemy korzystać z tej biblioteki, ja zrobilem
# na razie tyle i ide ogarnac kilka innych rzeczy
# Nie rozkminiłem jeszcze opcji kolorowania, ale to moze sie przydac do tego co ty chciałeś
# curses.use_default_colors()