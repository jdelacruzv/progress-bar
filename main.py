import time
import os

icon_list = ['#', '$', '@', '=', '|']
INITIAL_COLOR = '\033[0;30;42m'
FINAL_COLOR = '\033[0;m'


def main():
	while True:
		try:
			bar_length = int(input('Ingrese longitud [ >= 10 ]: '))
			bar_icon = input('Ingrese ícono [ #, $, @, =, | ]: ')
			if bar_length >= 10 and bar_icon in icon_list:	
				hide_cursor()
				progress_bar(bar_length, bar_icon)
				show_cursor()
				leave_sys()
			else:
				print('Entrada no válida...')
				leave_sys()
		except:
			print('Entrada no válida...')
			leave_sys()


def hide_cursor():
	print('\033[?25l', end='')


def show_cursor():
	print('\033[?25h', end='')


def progress_bar(bar_length, bar_icon):
    for i in range(bar_length + 1):
        time.sleep(0.1)
        percentaje = f'{int(i * (100 / bar_length))}%'.rjust(4)
        progress = i * f'{bar_icon}'
        block = (bar_length - i) * '.'
        suffix = '\r'  # Overwrites current line
        bar_animation = f'{INITIAL_COLOR}Progress: [{percentaje}]{FINAL_COLOR} [{progress}{block}]{suffix}'
        print(bar_animation, end='')
    print()


def leave_sys():
	while True:
		leave = input('¿Desea continuar? (S / N): ').lower()
		if leave == 's':
			main()
		elif leave == 'n':
			os._exit(0)
		else:
			print('Entrada no válida')


# If the program is run (instead of imported), run the main:
if __name__ == '__main__':
	main()