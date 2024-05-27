import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    '''
    O objetivo é exibir o nome do programa.
    '''
    print("""
  ██████  ▄▄▄       ▄▄▄▄    ▒█████   ██▀███      ▓█████▒██   ██▒ ██▓███   ██▀███  ▓█████  ██████   ██████ 
▒██    ▒ ▒████▄    ▓█████▄ ▒██▒  ██▒▓██ ▒ ██▒    ▓█   ▀▒▒ █ █ ▒░▓██░  ██ ▓██ ▒ ██▒▓█   ▀▒██    ▒ ▒██    ▒ 
░ ▓██▄   ▒██  ▀█▄  ▒██▒ ▄██▒██░  ██▒▓██ ░▄█ ▒    ▒███  ░░  █   ░▓██░ ██▓▒▓██ ░▄█ ▒▒███  ░ ▓██▄   ░ ▓██▄   
  ▒   ██▒░██▄▄▄▄██ ▒██░█▀  ▒██   ██░▒██▀▀█▄      ▒▓█  ▄ ░ █ █ ▒ ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄  ▒   ██▒  ▒   ██▒
▒██████▒▒ ▓█   ▓██▒░▓█  ▀█▓░ ████▓▒░░██▓ ▒██▒    ░▒████▒██▒ ▒██▒▒██▒ ░  ░░██▓ ▒██▒░▒████▒██████▒▒▒██████▒▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░    ░░ ▒░ ▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
░ ░▒  ░    ░   ▒▒ ░▒░▒   ░   ░ ▒ ▒░   ░▒ ░ ▒░     ░ ░  ░░   ░▒ ░░▒ ░       ░▒ ░ ▒░ ░ ░  ░ ░▒  ░  ░ ░▒  ░  
░  ░  ░    ░   ▒    ░    ░ ░ ░ ░ ▒     ░   ░        ░   ░    ░  ░░          ░   ░    ░  ░  ░  ░  ░  ░  ░  
      ░        ░  ░ ░          ░ ░     ░            ░   ░    ░              ░        ░        ░        ░  
    
                                    █▄ ▄█ ▄▀▄ ▀█▀ █▄█ ██▀ █ █ ▄▀▀
                                    █ ▀ █ █▀█  █  █ █ █▄▄ ▀▄█ ▄██


""")

def exibir_opcoes():
    '''
    O objetivo é exibir as opções do restaurante.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''
    O objetivo é apontar a opção de finalizar o programa.
    '''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''
    O objetivo é apontar a opção de voltar ao menu inicial do programa.
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''
    O objetivo é apontar quando o usuario não coloca uma opção listada no menu.
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''
    O objetivo é exibir um subtitulo do restaurante.
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''O objetivo da função é cadastrar um novo restaurante
    inputs:
    - nome do do restaurante
    - categoria do restaurante
    outputs:
    - adiciona um novo restaurante no dicionário restaurante'''


    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavel por listar os restaurantes criados'''

    exibir_subtitulo('Listando restaurantes')

    #print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''O objetivo é alterar o estado do restaurante.
    Inputs:
    - nome do restaurante
    Outputs: Altera o modelo de estado atual do restaurante.
    '''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    '''O objetivo é demonstrar opções para que o usuario escolha.'''
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
    '''
    O objetivo é armazenar as principais exibições e funções dadas anteriormente.
    '''
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()