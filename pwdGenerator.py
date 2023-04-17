import random
import string
from termcolor import colored
from time import sleep


def generate_password(length: int, uppercase: bool = True, lowercase: bool = True, digits: bool = True, symbols: bool = True) -> str:
    """
    Fonction pour générer un mot de passe aléatoire en utilisant des caractères alphanumériques et des symboles.

    :param length: longueur du mot de passe à générer.
    :param uppercase: booléen pour inclure ou non des lettres majuscules.
    :param lowercase: booléen pour inclure ou non des lettres minuscules.
    :param digits: booléen pour inclure ou non des chiffres.
    :param symbols: booléen pour inclure ou non des symboles.
    :return: le mot de passe généré.
    """
    if not any((uppercase, lowercase, digits, symbols)):
        raise ValueError("Au moins un type de caractère doit être sélectionné.")
    
    characters = "".join([
        string.ascii_uppercase if uppercase else "",
        string.ascii_lowercase if lowercase else "",
        string.digits if digits else "",
        string.punctuation if symbols else "",
    ])
    
    password = "".join(random.choice(characters) for _ in range(length))
    
    return password


def get_int_input(prompt: str) -> int:
    while True:
        try:
            num = int(input(colored(prompt, "blue")))
            if num > 0:
                return num
            else:
                print(colored("Veuillez entrer un entier supérieur à 0.", "red"))
        except ValueError:
            print(colored("Veuillez entrer un entier.", "red"))


def get_bool_input(prompt: str) -> bool:
    response = input(colored(prompt, "blue")).lower()
    return response in ("oui", "")


def main() -> None:
    """
    Fonction principale pour demander des entrées utilisateur et générer des mots de passe aléatoires.
    """
    print(colored("[*] Lancement...", "blue"))
    print()
    sleep(1)
    
    num_passwords = get_int_input("[?] Combien de mots de passe voulez-vous générer : ")
    password_length = get_int_input("[?] Quelle longueur de mot de passe voulez-vous : ")
    use_uppercase = get_bool_input("[?] Utiliser des lettres majuscules : (oui ou non) ")
    use_lowercase = get_bool_input("[?] Utiliser des lettres minuscules : (oui ou non) ")
    use_digits = get_bool_input("[?] Utiliser des chiffres : (oui ou non) ")
    use_symbols = get_bool_input("[?] Utiliser des symboles : (oui ou non) ")
    
    if not any((use_uppercase, use_lowercase, use_digits, use_symbols)):
        raise ValueError("Au moins un type de caractère doit être sélectionné.")
    
    passwords = [generate_password(password_length, uppercase=use_uppercase, lowercase=use_lowercase, digits=use_digits, symbols=use_symbols) for _ in range(num_passwords)]
    print()
    if num_passwords == 1:
        print(colored("Un mot de passe sera généré.", "blue"))
    else:
        print(colored(str(num_passwords) + " mots de passe seront générés.", "blue"))
    print()
    print(colored("[*] Génération... ", "blue"))
    sleep(1.5)
    print()
    
    for password in passwords:
        print(colored(password, "blue"))
        
    print()
    print(colored("Mission accomplie !", "blue"))

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(colored("[!] Erreur : " + str(e), "red"))
    except KeyboardInterrupt:
        print(colored("[!] Interruption de l'utilisateur.", "red"))
