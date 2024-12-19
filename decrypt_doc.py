from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Charger la clé
key_file = "key.bin"
if not os.path.exists(key_file):
    raise FileNotFoundError("Le fichier contenant la clé (key.bin) est introuvable.")
with open(key_file, "rb") as f:
    key = f.read()

# Déchiffrement du message
def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext

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
                    ciphertext = doc.read()

                decrypted_msg = decrypt_message(ciphertext, key)

                with open(chemin_fichier, "wb") as doc:
                    doc.write(decrypted_msg)

                print(f"Le fichier {filename} a été déchiffré avec succès.")
            except Exception as e:
                print(f"Erreur lors du déchiffrement du fichier {filename}: {e}")
except Exception as e:
    print(f"Une erreur s'est produite: {e}")