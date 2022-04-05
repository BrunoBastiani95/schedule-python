AGENDA = {}

AGENDA['bruno'] = {
    'telefone': '41996514575',
    'email': 'bruno@teste.com.br',
    'endereco': 'av. teste - 01',
}

AGENDA['giovanna'] = {
    'telefone': '41996514576',
    'email': 'giovanna@teste.com.br',
    'endereco': 'av. teste - 02',
}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('\n Agenda vazia...')


def buscar_contato(contato):
    try:
        print()
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('E-mail:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
    except KeyError:
        print('\nContato inexistente...')
    except Exception as error:
        print('\nUm erro inesperado ocorreu.')
        print(error)

def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o e-mail do contato: ')
    endereco = input('Digite o endereco do contato: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('\nContato "{}" adicionado/editado com sucesso!'.format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print('\nContato "{}" excluído com sucesso!'.format(contato))
    except KeyError:
        print('\nContato inexistente...')
    except Exception as error:
        print('\nUm erro inesperado ocorreu.')
        print(error)


def exportar_contatos():
    try:
        with open('contatos.txt', 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('Nome: {}\n Telefone: {}\n E-mail: {}\n Endereco:{}\n\n'.format(contato, telefone, email, endereco))

        print('\nAgenda exportada com sucesso!')
    except:
        print('\nHouve um erro durante a exportação dos contatos.')


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('\nArquivo não encontrado.')
    except Exception as ex:
        print('\nOcorreu um erro inesperado: {}'.format(ex))


def imprimir_menu():
    print()
    print('1 - Mostrar contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Inserir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos para Agenda')
    print('0 - Fechar agenda')


while True:
    imprimir_menu()
    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('\nDigite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('\nDigite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\nContato já existe!')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\nEditando contato: ', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('\nConta inexistente...')

    elif opcao == '5':
        contato = input('\nDigite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '6':
        exportar_contatos()

    elif opcao == '7':
        nome_do_arquivo = input('\nDigite o nome do arquivo: ')
        importar_contatos(nome_do_arquivo)

    elif opcao == '0':
        print('\nFechando o programa... Adeus!')
        break

    else:
        print('\nOpção inválida! Tente novamente...')

