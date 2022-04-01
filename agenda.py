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
        print('Um erro inesperado ocorreu.')
        print(error)


def incluir_editar_contato(contato):
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o e-mail do contato: ')
    endereco = input('Digite o endereco do contato: ')

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
        print('Um erro inesperado ocorreu.')
        print(error)


def imprimir_menu():
    print()
    print('1 - Mostrar contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Inserir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')


while True:
    imprimir_menu()
    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\n Contato já existe!')
        except KeyError:
            incluir_editar_contato(contato)

    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('\n Editando contato: ', contato)
            incluir_editar_contato(contato)
        except KeyError:
            print('\nConta inexistente...')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)

    elif opcao == '0':
        print('Fechando o programa... Adeus!')
        break

    else:
        print('\nOpção inválida! Tente novamente...')

