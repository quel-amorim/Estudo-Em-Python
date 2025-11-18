from Models.CREATEMOBS import Mob
from Models.CREATEPLAYERS import Player

def main():
    print("=== MENU RPG ===")
    print("1 - Criar Mobs")
    print("2 - Criar Players")
    print("3 - Ver Players")
    print("4 - Ver Mobs")
    print("5 - Sair")

    while True:
        op = input("\nEscolha: ")

        match op:
            case "1":
                Mob().addInsert()
            case "2":
                Player().addInsert()
            case "3":
                Player().viewerPlayer()
            case "4":
                Mob().viewerMob()
            case "5":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    main()