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
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    print()
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('E-mail:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('Contato "{}" adicionado/editado com sucesso!'.format(contato))


def excluir_contato(contato):
    AGENDA.pop(contato)
    print('Contato "{}" excluído com sucesso!'.format(contato))

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
    elif opcao == '3' or opcao == '4':
        contato = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        endereco = input('Digite o endereco do contato: ')
        incluir_editar_contato(contato, telefone, email, endereco)
        mostrar_contatos()
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
        mostrar_contatos()
    elif opcao == '0':
        print('Fechando o programa... Adeus!')
        break
    else:
        print('\nOpção inválida! Tente novamente...')

