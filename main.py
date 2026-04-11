# CLI



from system.database import criar_tabela
from services.livro_service import cadastrar_livro, listar_livros, emprestar_livro, devolver_livro
criar_tabela()
def mostrar_menu():
    print("1 - Cadastrar livro")
    print("2 - Ver livros")
    print("3 - Alugar livros")
    print("4 - Devolver livro")
    print("5 - Sair")
def main():
    print("Olá, digite o número do serviço que deseja")
    while True:
        mostrar_menu()
        choice = input("\n>> ").strip()
        if not choice.isdigit():
            print("Digite apenas números.")
            continue
        if choice == "1":
            cadastrar_livro()
        elif choice == "2":
            listar_livros()
        elif choice == "3":
            emprestar_livro()
        elif choice == "4":
            devolver_livro()
        elif choice == "5":
            print("Até mais!")
            break
        else:
            print(f"\"{choice}\" não é uma opção válida")
if __name__ == "__main__":
    main()