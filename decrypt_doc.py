import os
import zipfile
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key_file = "key.bin"
if not os.path.exists(key_file):
    raise FileNotFoundError("Le fichier contenant la clé (key.bin) est introuvable.")
with open(key_file, "rb") as f:
    key = f.read()

def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return plaintext

dossier = "./dossier_confidentiel"
if not os.path.exists(dossier):
    os.makedirs(dossier)

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

zip_filename = "dossier_confidentiel.zip"
try:
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for filename in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, filename)
            if os.path.isfile(chemin_fichier):
                zipf.write(chemin_fichier, arcname=filename)
                print(f"Le fichier {filename} a été ajouté au fichier ZIP.")
    print(f"Le fichier ZIP {zip_filename} a été créé avec succès.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la création du fichier ZIP: {e}")
