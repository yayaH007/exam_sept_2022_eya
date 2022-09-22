from ecies.utils import generate_eth_key, generate_key
import ecies
from coincurve.utils import hex_to_bytes
import eth_keys

import decryptage as d 

eth_k = generate_eth_key()
secret_key_hex = eth_k.to_hex()  # hex string
public_key_hex = eth_k.public_key.to_hex()  # hex string
message = 'this is a test'
crypted_hex=ecies.encrypt(public_key_hex, message.encode("utf-8")).hex()
#
# le composant decrypt.cpp tel qu'il est donné utilise un fichier
# "ECIES_PrivateKey.key" pour lire la cle secrete
#
# modifier le composant decrypt.cpp present dans ce repertoire
# afin qu'il aie des interfaces de type chaine de caracteres
# c'est a dire que le resultat soit une chaine de caracteres
# ainsi que les 2 arguments 
# la premiere chaine etant la cle secrete,
# la deuxieme etant le message encrypte
# 
# la ligne ci-dessous utilise la bibliotheque python ecies et
# vous donne la reponse correcte, a la difference que ecies.decrypt
# ne donne pas sa reponse directement en chaine de caracteres
# c'est pour cela que l'on doit appeler decode
# ecies.decrypt ne prend pas un second argument sous forme
# de chaine de caracteres, c'est pour cela que hex_to_bytes doit
# etre appellé, votre fonction devra pouvoir fonctionner directement
# avec des chaines de caracteres
print(ecies.decrypt(secret_key_hex, hex_to_bytes(crypted_hex)).decode("utf-8"))
# vous avez a ecrire une fonction qui puisse etre appellee
# comme suit et qui donne le meme resultat que ci-dessus
# d.decrypt_from_hex(secret_key_hex, crypted_hex)
