import subprocess


def recupere_le_mot_de_passe_dun_wifi(wifi):
    list_commande = wifi.split(" ")
    if len(list_commande) == 1:
        commande2 = "netsh wlan show profiles " + wifi + " key=clear"
    else:
        commande2 = "netsh wlan show profiles " + '"' + wifi + '"' + " key=clear"

    objet_message = subprocess.run(commande2, shell=True, capture_output=True, universal_newlines=True)
    sms = objet_message.stdout
    sms_corriger = sms.replace("ÿ", " ").replace("‚", "é").replace("Š", "è").replace("–", "û")

    debut = sms_corriger.find("Contenu de la clé            :")
    fin1 = sms_corriger.find("Paramètres du coût")
    fin2 = sms_corriger.find("Index de la clé")
    if fin2 == -1:
        fin = fin1
        sms_couper1 = sms_corriger[debut:fin]

        indice2 = sms_couper1.find(":")
        le_mot_de_passe = sms_couper1[indice2 + 2:len(sms_couper1) - 2]

    else:
        fin = fin2
        sms_couper1 = sms_corriger[debut:fin]

        indice2 = sms_couper1.find(":")
        le_mot_de_passe = sms_couper1[indice2 + 2:len(sms_couper1) - 5]

    if not le_mot_de_passe:
        return "<--pas_de_mot_de_passe-->"
    else:
        return le_mot_de_passe


def obtenir_tous_les_nom_de_wifi():
    commande2 = "netsh wlan show profiles "
    objet_message = subprocess.run(commande2, shell=True, capture_output=True, universal_newlines=True)
    sms = objet_message.stdout
    sms_corriger = sms.replace("ÿ", " ").replace("‚", "é")

    sms_couper = sms_corriger[180:]

    ma_liste = sms_couper.split("\n")

    tout_les_nom_de_wifi = []
    for element in ma_liste:
        indice = element.find(":")
        ele = element[indice + 2:]
        if ele == "":
            continue
        tout_les_nom_de_wifi.append(ele)

    return tout_les_nom_de_wifi


def afficher_le_mdp_dun_wifi():
    while True:
        wifi_name = input("Donner le nom exacte du wifi: ")
        if not wifi_name:
            print("vous n'avez entrez aucun nom Reessayer : ")
            continue
        break
    if not wifi_name in obtenir_tous_les_nom_de_wifi():
        print()
        print("Ce wifi n'est pas enregistré sur cette ordinateur")
        print()
        input("             <press for out>")
        exit(0)

    print()
    print("               <----Mot de passe du wifi enregistrer----->")
    print()

    mdp = recupere_le_mot_de_passe_dun_wifi(wifi_name)

    print("         SSID :", wifi_name)
    print("         MOT DE PASSE:", mdp)


def afficher_le_mdp_de_tous_les_wifi(listes_des_wifi_disponible, test=False):
    if not test:
        print("""
                  Profils utilisateurs
                  --------------------------------------------------------
               """)
    listes_des_wifi_disponible.sort(key=lambda a: len(a))
    for element in listes_des_wifi_disponible:
        le_mdp = recupere_le_mot_de_passe_dun_wifi(element)
        sortie = "             " + element + " : " + le_mdp
        if not test:
            print(sortie)
        if test:
            with open("save_wifi_password.txt", "a", encoding="UTF-8") as file:
                file.write(sortie + "\n")


def afficher_la_liste_des_wifi_disponible(listes_wifi):
    print("     Liste des wifi disponible")
    print("     ____________________________________________________________")
    print()
    for element in listes_wifi:
        print("                         Profil Tous les utilisateurs     :",element)





print("made by : ")

print("""
                    __________ .__                    __        __________                __________         
                    \______   \|  |  _____     ____  |  | __    \____    /  ____    ____  \______   \   ____  
                     |    |  _/|  |  \__  \  _/ ___\ |  |/ /      /     / _/ __ \ _/ __ \  |       _/ _/ __ \ 
                     |    |   \|  |__ / __ \_\  \___ |    <      /     /_ \  ___/ \  ___/  |    |   \ \  ___/ 
                     |______  /|____/(____  / \___  >|__|_ \    /_______ \ \___  > \___  > |____|_  /  \___  >
                            \/            \/      \/      \/            \/     \/      \/         \/       \/

                                                                                     wifi password V-0-0-1
 05/11/2023-15:02                                                                                    
""")

liste_wifi = obtenir_tous_les_nom_de_wifi()
afficher_la_liste_des_wifi_disponible(liste_wifi)

print("""

""")
print("""Choisissez l'une de ses options:
        1 .afficher le mot de passe d'un wifi
        2 .afficher le mot de passe s'il existe de tous les wifi afficher si dessus
""")
choix = input("choix : ")
try:
    choix_int = int(choix)
except:
    print("Le programme s'est volontairement interomppue")
    print("veuillez choisir entre 1 et 2")
    print()
    input( "          <press for out>")
    exit(0)

if choix_int == 1:
    afficher_le_mdp_dun_wifi()
elif choix_int == 2:
    afficher_le_mdp_de_tous_les_wifi(liste_wifi)
else:
    print()
    print("Soit c'est 1 ou 2 : bayil sa xel bi nguey foyyéé !!!!!!!!!!")
    print()
    input("         <press for out>")
    exit(0)





print()
choix = input("Voulez vous enregistrer cette sortie dans un fichier[y/N]")
if choix == "y":
    afficher_le_mdp_de_tous_les_wifi(liste_wifi, True)

else:
    input("        <press for out>")
    exit(0)

print()

print("         Le processus s'est terminé avec succés !!!!!!!!!")
print()
print("<press for out>")
input()