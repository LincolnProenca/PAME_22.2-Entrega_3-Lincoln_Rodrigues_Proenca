from sistema import *

""" Código principal """

def main():
    sis = Sistema()
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