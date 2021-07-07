import os
from clock import Relogio
from time import sleep
from random import randint
from datetime import datetime

class Personagem:
    def __init__(self, nome, idade, geracao, energia=0, dinheiro=0, ansiedade=0,status=0):
        self.__nome = nome
        self.__idade = idade
        self.__energia = energia
        self.__dinheiro = dinheiro
        self.__ansiedade = ansiedade
        self.__status = status
        self.__geracao = geracao
        self.__fase = 0

    def __str__(self):
        return f'''
        ESTAGIÁRIO {self.geracaoDef().upper()}:

        Personagem: {self.nome}
        Idade: {self.idade}
        Energia: {self.energia}
        Dinheiro: {self.dinheiro}
        Ansiedade: {self.ansiedade}
        Geração: {self.geracaoDef()}
        Status Atual: {self.statusDef()}

        '''
    
    def geracaoDef(self):
        if self.__nome=='boomer': 
            return 'Boomer' 
        else: 
            return 'Geração Z'

    def statusDef(self):
        if int(self.status)>=1:
            return 'Boomer' 
        else: 
            return 'Geração Z'

    @property
    def nome(self):
        return self.__nome 

    @property
    def idade(self):
        return self.__idade

    @property
    def energia(self):
        return self.__energia

    @property
    def geracao(self):
        return self.__geracao
    
    @property
    def status(self):
        return self.__status

    @energia.setter
    def energia(self, valor):
        self.__energia += valor

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, valor):
        self.__dinheiro += valor

    @property
    def ansiedade(self):
        return self.__ansiedade

    @ansiedade.setter
    def ansiedade(self, valor):
        self.__ansiedade -= valor

   
    def acordar(self, escolha):
        if escolha == 1:    
            self.__energia -= 75
            self.__dinheiro -= 100
            self.__ansiedade += 0
        else:
            self.__energia -= 100
            self.__dinheiro -= 50
            self.__ansiedade += 50

    def refeicao(self, escolha):
        if escolha == 1:
            self.__energia += 5
            self.__dinheiro -= 20
            self.__ansiedade -= 20
            self.__status -= 10
            
        elif escolha == 2:
            self.__energia += 5
            self.__dinheiro -= 5
            self.__ansiedade -= 5
            self.__status += 5

        elif escolha == 3:
            self.__energia -= 10
            self.__dinheiro += 0
            self.__ansiedade += 5
            self.__status -= 0
        else:
            self.__energia -= 20
            self.__dinheiro += 0
            self.__ansiedade += 20
            self.__status += 0

    def banho(self, escolha):
        if escolha == 1:
            self.__energia -= 5
            self.__dinheiro -= 0
            self.__ansiedade -= 10
            self.__status += 5
            
        else:
            self.__energia -= 0
            self.__dinheiro += 0
            self.__ansiedade += 10
            self.__status -=5 

    def trajeto(self,escolha):
        if escolha == 1:
            self.__energia -= 10 
            self.__dinheiro += 0
            self.__ansiedade -= 10
            self.__status += 5
            
        elif escolha == 2:
            self.__energia -= 5
            self.__dinheiro -= 5
            self.__ansiedade += 5
            self.__status += 0

        else:
            self.__energia -= 5
            self.__dinheiro -= 20
            self.__ansiedade += 0
            self.__status -= 5

    def bugtrabalho(self,escolha):
        if self.__ansiedade>35:
            print('Sua ansiedade está alta demais, você não consegue manter a paciência.')
            escolha = 3
            self.__energia -= 20
            self.__dinheiro -= 0
            if self.__geracao=='boomer':
                self.__status-=10
            else:
                self.__status+=10
        else:
            if escolha == 1:
                self.__energia -= 10 
                self.__dinheiro += 0
                self.__ansiedade -= 10
                self.__status += 10
                
            elif escolha == 2:
                self.__energia -= 10
                self.__dinheiro -= 0
                self.__ansiedade += 10
                self.__status -= 10
            
            else:
                self.__energia -= 20
                self.__dinheiro -= 0
                self.__ansiedade += 20
                if self.__geracao=='boomer':
                    self.__status-=10
                else:
                    self.__status+=10

    def promocao(self,escolha):
        if self.__ansiedade>35:
            print('Sua ansiedade está alta demais, você não consegue manter a paciência.')
            escolha = 3
            self.__energia -= 20
            self.__dinheiro -= 0
            if self.__geracao=='boomer':
                self.__status-=10
            else:
                self.__status+=10
        else:
            if escolha == 1:
                self.__energia -= 10 
                self.__dinheiro += 0
                self.__ansiedade -= 10
                self.__status += 10
                
            elif escolha == 2:
                self.__energia -= 10
                self.__dinheiro -= 0
                self.__ansiedade += 10
                self.__status -= 10
            
            else:
                self.__energia -= 20
                self.__dinheiro -= 0
                self.__ansiedade += 20
                if self.__geracao=='boomer':
                    self.__status-=10
                else:
                    self.__status+=10
    
    def happyhour(self, escolha):
        if escolha == 1:
            self.__energia -= 20
            self.__dinheiro -= 0
            self.__ansiedade -= 20
            self.__status -= 10
            
        else:
            self.__energia -= 5
            self.__dinheiro += 0
            self.__ansiedade += 20
            self.__status +=10

    def escolha(self):
        for i in range(5,0,-1):
            print(f'CARREGANDO INFORMAÇÕES EM {i}...\n')
            sleep(1)
            os.system('cls||clear')

        print('''BOOMER:

        Dona Cida está sempre olhando para a janela ou apoiada em sua sacada
        observando o que acontece na vizinhança. Não perde uma fofoca no seu bairro
        e ao mesmo tempo cuida da sua vida e da sua casa como ninguém.

        Nascimento: 1957
        Estilo de música preferida: Bossa nova
        Comida predileta: Mandioca
        Novela preferida: Tieta do Agreste
        Mora em casa própria desde os 19 anos quando casas ainda eram trocadas por linhas telefônicas.
        Profissão: Aposentada
        Hobbie: Ficar na janela cuidando da vida dos outros.

        Inteligência: 4
        Força: 1
        Carisma: 0
        Foco: 3

        Habilidades especial:
        Fuxiqueira.


        GERAÇÃO Z:

        Enzo Gabriel sempre está olhando para alguma tela, 
        tem dificuldades de se concentrar em uma coisa mas estranhamente 
        tem facilidade em ser multitarefa, nunca anda sem colírio nos bolsos.

        Nascimento: 2003
        Estilo de música preferida: Kpop
        Sobremesa preferida: Brizadeiro e Bolinho Espacial
        Série preferida: qualquer série que tenham vampiros ou zumbis (as vezes zumbis e vampiros se casando)
        Mora com os pais
        Profissão: Jovem Aprendiz
        Hobbie: YouTuber de games

        Inteligência: 5
        Força: 3
        Carisma: 4
        Foco: 0

        Habilidades especial:
        Ser multitarefa - consegue aprender qualquer coisa rapidamente mas não domina nenhum tema.
        ''')

        escolha = str(input('''
        CHOOSE YOUR FIGHTER
        [1] DONA CIDA
        [2] ENZO GABRIEL
        [3] ALEATÓRIO

        ''')).strip().upper()[0]
        while escolha not in '123':
            escolha = str(input('''
            OPÇÃO INVÁLIDA!
            CHOOSE YOUR FIGHTER
            [1] DONA CIDA
            [2] ENZO GABRIEL
            [3] ALEATÓRIO
            ''')).strip().upper()[0]
        if escolha == '3':
            escolha = str(randint(1,2))
        if escolha == '1':
            self.__nome = 'Dona Cida'
            self.__idade = datetime.now().year - 1957
            self.__energia = 50
            self.__dinheiro = 100
            self.__ansiedade = 0
        else:
            self.__nome = 'Enzo Gabriel'
            self.__idade = datetime.now().year - 2003
            self.__energia = 100
            self.__dinheiro = 50
            self.__ansiedade = 50

        personagem = Personagem(self.__nome, self.__idade, self.__energia, self.__dinheiro, self.__ansiedade, 0)
        print(f'''
        PERSONAGEM ESCOLHIDO!!
        {personagem.nome.upper()}
        CARREGANDO A PRÓXIMA FASE...
        ''')
        sleep(5)

    def passar_fase(self):
        self.__fase += 1

    def limpar(self):
        os.system('cls||clear')

    def statusPar(self):
        if self.__energia <= 0 or self.__dinheiro <= 0 or self.__ansiedade >= 150:
            True

    def venceu(self):
        return '''VOCÊ VENCEU! PARABÉNS, CHEGOU VIVO AO FINAL DE UM DIA DE TRABALHO!'''

    def perdeu(self):
        return '''VOCÊ PERDEU! FIM DE JOGO...'''

    def desistir(self):
        return '''
        JÁ DESISTIU?
        TINHA QUE SER O ESTAGIÁRIO MESMO!
        FIM DE JOGO...
        '''