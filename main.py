from agenda.models import criar_tabela
from agenda.ui import criar_interface

def main():
    # Cria a tabela no banco de dados, se ainda não existir
    criar_tabela()
    
    # Inicia a interface com o usuário
    criar_interface()

if __name__ == '__main__':
    main()
