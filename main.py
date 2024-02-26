import time
import os

def main():
	while True:
		try:
			bar_length = int(input('Ingrese longitud de la barra de progreso: '))
			if bar_length >= 10:
				progress_bar(bar_length)
				leave_sys()
			else:
				print('La longitud debe ser mayor o igual a 10')
				leave_sys()
		except:
			print('Entrada no válida...')
			leave_sys()


def progress_bar(bar_length):	
    for i in range(bar_length + 1):
        time.sleep(0.1)
        percentaje = f'{int(i * (100 / bar_length))}%'
        progress_icon = i * '#'
        bar_icon = (bar_length - i) * '.'
        suffix = '\r'  # Overwrites current line
        bar_animation = f'Progress: [{percentaje}] [{progress_icon}{bar_icon}]{suffix}'
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