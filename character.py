import os
from clock import Time
from time import sleep
from random import randint
from datetime import datetime

class Character:
    def __init__(self, name, age, generation, energy=0, money=0, anxiety=0,status=0):
        self.__name = name
        self.__age = age
        self.__energy = energy
        self.__money = money
        self.__anxiety = anxiety
        self.__status = status
        self.__generation = generation
        self.__stage = 0

    def __str__(self):
        return f'''
        ESTAGIÁRIO {self.generation.upper()}:

        Personagem: {self.name}
        Idade: {self.age}
        Energia: {self.energy}
        Dinheiro: {self.money}
        Ansiedade: {self.anxiety}
        Geração: {self.generation}
        Status Atual: {self.statusDef()}

        '''

    def statusDef(self):
        if self.__status > 0:
            return 'Boomer'
        else:
            return 'Geração Z'

    @property
    def name(self):
        return self.__name 

    @property
    def age(self):
        return self.__age

    @property
    def energy(self):
        return self.__energy

    @property
    def generation(self):
        return self.__generation
    
    @property
    def status(self):
        return self.__status

    @energy.setter
    def energy(self, value):
        self.__energy += value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money += value

    @property
    def anxiety(self):
        return self.__anxiety

    @anxiety.setter
    def anxiety(self, value):
        self.__anxiety -= value

   
    def wakeup(self, choice):
        if choice == '1':    
            self.__energy -= 5
            self.__money -= 0
            self.__anxiety += 10
            self.__status += 5
        else:
            self.__energy += 5
            self.__money -= 0
            self.__anxiety -= 10
            self.__status -= 5

    def meal(self, choice):
        if choice == '1':
            self.__energy += 5
            self.__money -= 20
            self.__anxiety -= 20
            self.__status -= 10
            
        elif choice == '2':
            self.__energy += 5
            self.__money -= 5
            self.__anxiety -= 5
            self.__status += 5

        elif choice == '3':
            self.__energy -= 10
            self.__money += 0
            self.__anxiety += 5
            self.__status -= 0

        else:
            self.__energy -= 20
            self.__money += 0
            self.__anxiety += 20
            self.__status += 0

    def takeshower(self, choice):
        if choice == '1':
            self.__energy -= 5
            self.__money -= 0
            self.__anxiety -= 10
            self.__status += 5
            
        else:
            self.__energy -= 0
            self.__money += 0
            self.__anxiety += 10
            self.__status -=5 

    def route(self, choice):
        if choice == '1':
            self.__energy -= 10 
            self.__money += 0
            self.__anxiety -= 10
            self.__status += 5
            
        elif choice == '2':
            self.__energy -= 5
            self.__money -= 5
            self.__anxiety += 5
            self.__status += 0

        else:
            self.__energy -= 5
            self.__money -= 20
            self.__anxiety += 0
            self.__status -= 5

    def bugwork(self, choice):
        if self.anxiety > 35:
            print('Sua ansiedade está alta demais, você não consegue manter a paciência.')
            sleep(5)
            choice == '3'
            self.__energy -= 20
            self.__money -= 0
            self.__anxiety += 20
            if self.generation=='boomer':
                self.__status-=10
            else:
                self.__status+=10
        
        if choice == '1':
            self.__energy -= 10 
            self.__money += 0
            self.__anxiety -= 10
            self.__status += 10
            
        elif choice == '2':
            self.__energy -= 10
            self.__money -= 0
            self.__anxiety += 10
            self.__status -= 10
        
        else:
            self.__energy -= 20
            self.__money -= 0
            self.__anxiety += 20
            if self.generation=='boomer':
                self.__status-=10
            else:
                self.__status+=10

    def promotion(self,choice):
        if self.anxiety > 35:
            print('Sua ansiedade está alta demais, você não consegue manter a paciência.')
            sleep(5)
            choice == '3'
            self.__energy -= 20
            self.__money -= 0
            if self.generation=='boomer':
                self.__status-=10
            else:
                self.__status+=10
        else:
            if choice == '1':
                self.__energy -= 10 
                self.__money += 0
                self.__anxiety -= 10
                self.__status += 10
                
            elif choice == '2':
                self.__energy -= 10
                self.__money -= 0
                self.__anxiety += 10
                self.__status -= 10
            
            else:
                self.__energy -= 20
                self.__money -= 0
                self.__anxiety += 20
                if self.generation=='boomer':
                    self.__status-=10
                else:
                    self.__status+=10
    
    def happyhour(self, choice):
        if choice == '1':
            self.__energy -= 20
            self.__money -= 0
            self.__anxiety -= 20
            self.__status -= 10
            
        else:
            self.__energy -= 5
            self.__money += 0
            self.__anxiety += 20
            self.__status +=10

    def choice(self):
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

        choice = str(input('''
        CHOOSE YOUR FIGHTER
        [1] DONA CIDA
        [2] ENZO GABRIEL
        [3] ALEATÓRIO

        ''')).strip().upper()[0]
        while choice not in '123':
            choice = str(input('''
            OPÇÃO INVÁLIDA!
            CHOOSE YOUR FIGHTER
            [1] DONA CIDA
            [2] ENZO GABRIEL
            [3] ALEATÓRIO
            ''')).strip().upper()[0]
        if choice == '3':
            choice = str(randint(1,2))
        if choice == '1':
            self.__name = 'Dona Cida'
            self.__age = datetime.now().year - 1957
            self.__energy = 50
            self.__money = 100
            self.__anxiety = 0
            self.__generation = 'Boomer'
            self.__status = 1
        else:
            self.__name = 'Enzo Gabriel'
            self.__age = datetime.now().year - 2003
            self.__energy = 100
            self.__money = 50
            self.__anxiety = 50
            self.__generation = 'Geração Z'
            self.__status = -1

        character = Character(self.__name, self.__age, self.__energy, self.__money, self.__anxiety, self.__status)
        print(f'''
        PERSONAGEM ESCOLHIDO!!
        {character.name.upper()}
        CARREGANDO A PRÓXIMA FASE...
        ''')
        sleep(5)

    def next_stage(self):
        self.stage += 1

    def clean(self):
        os.system('cls||clear')

    def statusPar(self):
        if self.energy <= 0 or self.money <= 0 or self.anxiety >= 150:
            if self.energy <= 0:
                print(f'{self.name} morreu por falta de energia.')
            elif self.money <= 0:
                print(f'{self.name} ficou sem dinheiro.')
            elif self.anxiety >= 150:
                print(f'{self.name} morreu de ansiedade.')
            return True

    def win(self):
        return '''VOCÊ VENCEU! PARABÉNS, CHEGOU VIVO AO FINAL DE UM DIA DE TRABALHO!'''

    def lost(self):
        return '''VOCÊ PERDEU! FIM DE JOGO...'''

    def genidentity(self):
        if self.__status != self.__generation:
            print(f'Você é {self.__generation} e se comportou como um {self.__status} durante o dia! FIM DE JOGO...')
            return True

    def giveup(self):
        return '''
        JÁ DESISTIU?
        TINHA QUE SER O ESTAGIÁRIO MESMO!
        FIM DE JOGO...
        '''