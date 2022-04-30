import os
import sys

# função para alternando a rede
def wifi():
    # abrir o txt e ver qual no nome dentro
    with open("cache.txt", "r+") as f:
        nome = f.read().split()

        # verificar se existe o nome
        for SSID in nome:

            # Condições para verificar a rede no cache
            if "SILVA" in SSID:
                # limpar chace
                with open("cache.txt",'w') as f:
                    # escrever no chace
                    f.write("PUGNO")

                    # altera rede
                    os.system(f'''cmd /c "netsh wlan connect name={SSID}"''')
                    print(f"Alternando para rede {SSID}!")

            elif "PUGNO" in SSID:
                with open("cache.txt",'w') as f:
                    f.write("SILVA")

                    os.system(f'''cmd /c "netsh wlan connect name={SSID}"''')
                    print(f"Alternando para rede {SSID}!")
