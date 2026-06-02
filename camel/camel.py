def main():
    #  Récupérer l'input proprement
    camel_case = input("camelCase: ").strip()
    
    # On crée la liste modifiée directement en mémoire en une seule ligne
    snake_case = "".join(["_" + c.lower() if c.isupper() else c for c in camel_case])
    
    #  Afficher le résultat final d'un seul coup
    print("snake_case:", snake_case)

if __name__ == "__main__": 
    main()