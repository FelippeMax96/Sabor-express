import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def exibir_nome_do_programa():
    '''Essa função exibe o programa'''
    print('Sabor Express')

def exibir_opcoes():
    '''Essa função exibe as opções'''-;ç
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa função volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa função exibe a opção invalida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Essa função exibe o subtítulo'''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar  um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    -Adiciona um novo restaurate a lista de restaurantes
    
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista os restaurantes'''
    exibir_subtitulo('Listando restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status ')
    print('-' * 60)

    if restaurantes:
        for restaurante in restaurantes:
            if isinstance(restaurante, dict): 
                nome_restaurante = restaurante['nome']
                categoria = restaurante['categoria']
                ativo = 'ativado' if restaurante['ativo'] else 'desativado'
                print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    else:
        print('Restaurante não encontrado')
    
    input('\nPressione Enter para voltar ao menu principal')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função alterna o estado do restaurante '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para mudar status ')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função escolhe a opção'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()