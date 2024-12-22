# 🛡️ **Projet Fictif : Kellogg's - Simulation de Cyberattaque**

> **⚠️ AVERTISSEMENT : Ce projet est une simulation à but éducatif et fictif.**  
> Aucune donnée réelle n’a été compromise, et ce projet n’encourage ni ne soutient les activités malveillantes.

---

## 📜 **Contexte Fictif**
Dans le cadre d’un projet de groupe, nous avons imaginé un scénario immersif mettant en scène :  
- **Une mairie corrompue** : Le maire d'une ville fictive est accusé de détournements de fonds publics.  
- **Une cyberattaque ciblée** : Un hacker anonyme a pris en otage les données sensibles de la mairie en les cryptant à l’aide d’un algorithme robuste.  
- **Une demande de rançon** : Pour récupérer ces données, le maire doit payer une rançon en cryptomonnaie, sous peine de voir ses actions illégales exposées.  

---

## 🔧 **Fonctionnalités Principales**
1. **Envoi de mails automatisés**  
   - Simulation d'une communication avec le hacker, comprenant des instructions pour le paiement de la rançon.  

2. **Cryptage de données**  
   - Implémentation d’un cryptage AES (Advanced Encryption Standard) pour protéger et verrouiller les fichiers sensibles.  

3. **Décryptage des données**  
   - Fourniture d’une clé secrète permettant de restaurer les données après paiement fictif.  

4. **Zipper le dossier confidentiel**  
   - Après avoir decrypté les deux fichiers, les intégrer dans un dossier "dossier_confidentiel" zippé 

---

## ⚙️ **Stack Technique**
- **Langage principal** : Python  
- **Bibliothèques utilisées** :  
  - `pynput` : Pour capturer des entrées clavier et simuler des interactions.
  - `pycryptodome` : Implémentation d’AES pour le cryptage et le décryptage des fichiers.  
  - **AES (Advanced Encryption Standard)** : Algorithme de cryptage utilisé pour la sécurité des données.  
  - **Ransomware logic** : Implémentation de base pour la simulation.  

---

## 🛠️ **Installation des Dépendances**
Pour exécuter ce projet, assurez-vous d'avoir Python installé, puis exécutez les commandes suivantes :  
```bash
pip install pynput
pip install pycryptodome
```

## 🚨 **Disclaimer** 
Ce projet est strictement éducatif. Il a été conçu pour comprendre les mécanismes de sécurité, les algorithmes de cryptage et pour sensibiliser aux risques liés à la cybersécurité. **Toute utilisation malveillante est strictement interdite.**

---

## 🧠 **Leçons Apprises**
- Comprendre les bases du cryptage AES et de la gestion des clés.  
- Simuler une interaction réaliste entre un hacker et une victime.  
- Renforcer l’importance de la sécurité informatique dans les systèmes municipaux.