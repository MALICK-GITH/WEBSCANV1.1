import random
import os
from colorama import Fore, Style, init
import pyfiglet

# Initialisation de colorama
init(autoreset=True)

# Liste des SNI possibles
sni_list = [
    "facebook.com", "zero.facebook.com", "m.youtube.com", "cdn.whatsapp.net",
    "api.twitter.com", "www.instagram.com", "play.google.com", "cdn.cloudflare.net",
    "www.snapchat.com", "www.netflix.com", "www.tiktok.com", "web.whatsapp.com"
]

# Affiche le logo
def banner():
    os.system("clear")
    logo = pyfiglet.figlet_format("SOLITAIRE HACK")
    print(Fore.CYAN + logo)
    print(Fore.GREEN + "       SNI Generator - By Solitaire\n")

# Génère un SNI aléatoire
def generate_sni():
    sni = random.choice(sni_list)
    print(Fore.YELLOW + "[+] Generated SNI: " + Fore.CYAN + sni + "\n")

# Menu principal
def menu():
    banner()
    while True:
        print(Fore.MAGENTA + "1 - Générer un SNI")
        print("2 - Générer plusieurs SNIs")
        print("3 - Sauvegarder dans un fichier")
        print("4 - Quitter\n")

        choice = input(Fore.WHITE + "Choix: ")

        if choice == "1":
            generate_sni()
        elif choice == "2":
            try:
                n = int(input("Combien ?: "))
                print()
                for _ in range(n):
                    generate_sni()
            except ValueError:
                print(Fore.RED + "Entrée invalide. Mets un chiffre.")
        elif choice == "3":
            try:
                n = int(input("Combien ?: "))
                filename = input("Nom du fichier: ")
                with open(filename, 'w') as f:
                    for _ in range(n):
                        sni = random.choice(sni_list)
                        f.write(sni + "\n")
                print(Fore.GREEN + f"\n[✔] {n} SNIs sauvegardés dans {filename}\n")
            except Exception as e:
                print(Fore.RED + f"Erreur : {e}")
        elif choice == "4":
            print(Fore.CYAN + "\nMerci d’avoir utilisé le générateur. À bientôt !")
            break
        else:
            print(Fore.RED + "Choix invalide.\n")

# Lancer le programme
menu()