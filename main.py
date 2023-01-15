from sistema import *

opcoes_basicas = 'Escolha o que quer fazer: Criar projeto | Remover Projeto | Criar Consultor | Remover Consultor | Criar Gerente | Remover Gerente | Listar | Fazer Login | Sair\n'
opcoes_comuns = 'Verificar projetos alocados | Ver nome | Alterar Nome | Ver usuário | Alterar nome de usuário | Alterar senha | Trocar usuário\n'
opcoes_consultor = 'Requisitar Avanço de etapa | Pedir retirada do projeto\n'
opcoes_gerente = 'Gerenciar pedidos de avanço | Gerenciar pedidos de retirada | Passar o projeto a outro gerente | Entregar um projeto | Gerenciar alocação em projetos\n'

""" ********Código principal **********
É de extrema importância para o bom funcionamento do código que os projetos, gerentes e consultores criados tenham nomes diferentes
Letras maiúsculas e espaços não servem para diferenciar, por exemplo: "Pedro", "pedro" e "p e d r o" seriam considerados iguais
A ideia de remover a sensibilidade à espaços e letras maiúsculas é unica e exclusivamente para facilitar a navegação do usuário visto que o programa é controlado pelo terminal
Dessa forma, não é necessário o uso de acentos, espaços e letras maiúsculas para controlar o programa
"""

def main():
    sis = Sistema() #Iniciando o sistema

    """ Usuários base para teste """
    sis.gerentes.append(Gerente('Pedro Loss','pedro','123'))
    sis.consultores.append(Consultor('Rogerio Ceni','roger','123'))
    sis.gerentes.append(Gerente('Rebecca','reb','123'))

    sis.welcome()
    escolha = ''
    while escolha.replace(' ', '').lower() != 'sair':
        if sis.usuario_atual.tipo == 'Consultor':
            logado = True
            escolha = input(opcoes_basicas + opcoes_comuns + opcoes_consultor)
        elif sis.usuario_atual.tipo == 'Gerente':
            logado = True
            escolha = input(opcoes_basicas + opcoes_comuns + opcoes_gerente)
        else:
            logado = False
            escolha = input(opcoes_basicas)
        
        match[ escolha.replace(' ', '').lower(),logado]:
            case ['criarprojeto', False | True]:
                sis.criarprojetos()
            case ['removerprojeto', False | True]:
                sis.removerprojetos()
            case ['criarconsultor', False | True]:
                sis.criar_consultor()
            case ['removerconsultor', False | True]:
                sis.remover_consultor()
            case ['criargerente', False | True]:
                sis.criar_gerente()
            case ['removergerente', False | True]:
                sis.remover_gerente()
            case ['fazerlogin', False | True]:
                sis.logar()
            case ['listar', False | True]:
                sis.listar()
            case ['verificarprojetosalocados', True]:
                sis.usuario_atual.ver_projetos_alocados()
            case ['vernome', True]:
                sis.usuario_atual.ver_nome()
            case ['alterarnome', True]:
                sis.alterar_nome_usuario()
            case ['verusuario' | 'verusuário', True]:
                sis.ver_usuario()
            case ['alterarnomedeusuario' | 'alterarnomedeusuário', True]:
                sis.alterar_nome_usuario_login()
            case ['alterarsenha', True]:
                sis.alterar_senha_usuario()
            case ['trocarusuario' | 'trocarusuário', True]:
                sis.trocar_usuario()
            case ['gerenciarpedidosdeavanço' | 'gerenciarpedidosdeavanco', True]:
                sis.gerenciar_pedidos_avanco()
            case ['gerenciarpedidosderetirada', True]:
                sis.gerenciar_pedidos_retirada()
            case ['passaroprojetoaoutrogerente', True]:
                sis.passar_projeto()
            case ['entregarumprojeto', True]:
                sis.entregar_projeto()
            case ['requisitaravançodeetapa' | 'requisitaravancodeetapa', True]:
                sis.req_avanco_etapa()
            case ['pedirretiradadoprojeto', True]:
                sis.req_retirada_projeto()
            case ['gerenciaralocaçãoemprojetos' | 'gerenciaralocacaoemprojetos', True]:
                sis.gerenciar_alocacao_projetos()
            case ['sair', False | True]:
                escolha = 'sair'
                print('Adeus!')
            case _:
                print('\nEntrada inválida\n')

if __name__ == '__main__':
    main()