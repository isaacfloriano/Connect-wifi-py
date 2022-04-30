import os
import sys
import random

# função para trocar a rede
def wifi():

	# Nome das redes conectadas
	ssid = "SILVA|PUGNO"

	# Conectar a rede aleatória
	name_of_router = random.choice(ssid.split("|"))
	os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
	print(f"Conectado a rede {name_of_router}!")