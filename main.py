import time
import os

icon_list = ['#', '$', '@', '=', '|']


def main():
	while True:
		try:
			bar_length = int(input('Ingrese longitud [ >= 10 ]: '))
			bar_icon = input('Ingrese ícono [ #, $, @, =, |, ]: ')
			if bar_length >= 10 and bar_icon in icon_list:
				progress_bar(bar_length, bar_icon)
				leave_sys()
			else:
				print('Entrada no válida...')
				leave_sys()
		except:
			print('Entrada no válida...')
			leave_sys()


def progress_bar(bar_length, bar_icon) :	
    for i in range(bar_length + 1):
        time.sleep(0.1)
        percentaje = f'{int(i * (100 / bar_length))}%'
        progress = i * f'{bar_icon}'
        block = (bar_length - i) * '.'
        suffix = '\r'  # Overwrites current line
        bar_animation = f'Progress: [{percentaje}] [{progress}{block}]{suffix}'
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