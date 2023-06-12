import subprocess

#HPING3 CHANGEMAC

def d():
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
        tout_les_nom_de_wifi.append(ele)

    return tout_les_nom_de_wifi


wifi = "ELAB2-2.4GHZ"

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
else:
    fin = fin2

sms_couper1 = sms_corriger[debut:fin]
indice2 = sms_couper1.find(":")
sms_couper2 = sms_couper1[indice2 + 2:len(sms_couper1) -1]

print(len(sms_couper2))
print(sms_couper2)