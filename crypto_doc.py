from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os

# Créer un fichier key.bin
key_file = "key.bin"
if not os.path.exists(key_file):
    with open(key_file, "wb") as f:
        # Générer une clé AES de 256 bits
        key = get_random_bytes(32)
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()

# Chiffrement du message
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return cipher.iv + ciphertext

# Dossier à traiter
dossier = "./dossier_confidentiel"
if not os.path.exists(dossier):
    os.makedirs(dossier)
    print("Le dossier a été créé.")
try:
    for filename in os.listdir(dossier):
        chemin_fichier = os.path.join(dossier, filename)
        if os.path.isfile(chemin_fichier):
            try:
                with open(chemin_fichier, "rb") as doc:
                    message = doc.read()

                cipher_msg = encrypt_message(message, key)

                with open(chemin_fichier, "wb") as doc:
                    doc.write(cipher_msg)

                print(f"Le fichier {filename} a été chiffré avec succès.")
            except Exception as e:
                print(f"Erreur lors du chiffrement du fichier {filename}: {e}")
except Exception as e:
    print(f"Une erreur s'est produite: {e}")
