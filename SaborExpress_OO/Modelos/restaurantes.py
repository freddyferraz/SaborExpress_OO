from Modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []
    def __init__(self, Id, nome, categoria):
        self.id = Id
        self.nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes(cls):
        print(f'{'ID'.ljust(3)} | {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.id}   | {restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')
           
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alternar_estado(cls):
        cls.listar_restaurantes(Restaurante)
        id = int(input('Digite o ID do restaurante para alterar o seu status: '))
        for restaurante in cls.restaurantes:
            if restaurante.id == id:
                restaurante._ativo = not restaurante._ativo
                print(f'O restaurante {restaurante.nome} teve o status alterado para {restaurante.ativo} com sucesso')
                break
    
    def receber_avaliacao(cls):
        nota = -1
        cls.listar_restaurantes(Restaurante)
        id = int(input('Digite o ID do restaurante para avaliar: '))
        for restaurante in cls.restaurantes:
            if restaurante.id == id:
                cliente = input('Informe o seu nome: ')
                while(nota < 0 or nota > 5):
                    nota = int(input(f'Informe a nota para o restaurante {restaurante.nome}: '))
                avaliacao = Avaliacao(cliente, nota)
                restaurante._avaliacao.append(avaliacao)
                break
        
    
    def cadastrar_restaurante(cls):
        id = 0
        for restaurante in cls.restaurantes:
            id = restaurante.id
        id= id+1
        nome_restaurante = input('Informe o nome do Restaurante a ser cadastrado: ')
        categoria_restaurante = input(f'Informe a categoria do Restaurante {nome_restaurante} ')
        restaurante = Restaurante(id,nome_restaurante,categoria_restaurante)
        return 0
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem Avaliação'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
 


