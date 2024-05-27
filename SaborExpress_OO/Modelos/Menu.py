class Menu_Principal:
    opcoes = []
    def __init__(self,id,descricao,subtitulo):
        self.id = id
        self.descricao = descricao
        self.subtitulo = subtitulo
        self.opcoes.append(self)
    
    def listar_menu():
        for menu in Menu_Principal.opcoes:
            print(f'{menu.descricao}')
            
opcoes_menu = Menu_Principal(1,'1 - Cadastrar Restaurante','Cadastro de novos restaurantes')
opcoes_menu = Menu_Principal(2,'2 - Listar Restaurante','Listando os Restaurantes')
opcoes_menu = Menu_Principal(3,'3 - Alterar Restaurante','Alternando Status do Restaurante')
opcoes_menu = Menu_Principal(4,'4 - Avaliar Restaurante','Avaliando o Restaurante')
opcoes_menu = Menu_Principal(0,'0 - Sair','Finalizar o App')
            

         



