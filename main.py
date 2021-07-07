from character import Personagem
from time import sleep
from random import randint
from datetime import datetime
from clock import Relogio
import os

personagem = Personagem('',0,0,0,0,0)
personagem.limpar()
relogio = Relogio()
personagem.fase = 1
print(f'''                                        
                            ████      ██████████████      ████                          
                          ██░░░░████  ██░░░░░░░░░░██  ████░░░░██                        
                        ██░░░░░░░░░░██████████████████░░░░░░░░░░██                      
                      ██░░░░░░░░████        ██        ████░░░░░░░░██                    
                      ██░░░░████░░██    ██████████    ██░░████░░░░██                    
                        ████  ██░░██████░░░░░░░░░░██████░░██  ████                      
                              ████░░░░░░░░░░░░░░░░░░░░░░████                            
                            ██░░░░░░░░░░██████████░░░░░░░░░░██                          
                          ██░░░░░░██████          ██████░░░░░░██                        
                        ██░░░░░░██          ██          ██░░░░░░██                      
                        ██░░░░██    ██      ██      ██    ██░░░░██                      
                      ██░░░░░░██                          ██░░░░░░██                    
                      ██░░░░██  ██          ██          ██  ██░░░░██                    
                    ██░░░░██              ██████              ██░░░░██                  
                    ██░░░░██                ██                ██░░░░██                  
                    ██░░░░██                ██  ██            ██░░░░██                  
                    ██░░░░██  ████          ████████    ████  ██░░░░██                  
        ░░      ░░  ██░░░░██                    ██            ██░░░░██    ░░      ░░    
                    ██░░░░██      ██                  ██      ██░░░░██                  
                      ██░░██    ██                      ██    ██░░██                    
                      ██░░░░██        ██          ██        ██░░░░██                    
                        ██░░░░██    ██      ██      ██    ██░░░░██                      
                        ██░░░░░░██          ██          ██░░░░░░██                      
                          ██░░░░░░██████          ██████░░░░░░██                        
                            ██░░░░░░░░░░██████████░░░░░░░░░░██                          
                              ████░░░░░░░░░░░░░░░░░░░░░░████                            
                                  ██████░░░░░░░░░░██████                                
                                  ██████████████████████                                
░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░████████░░▓▓▓▓▓▓░░████████░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░

{relogio}
O DESPERTADOR TOCOU E COMEÇA MAIS UM DIA DE TRABALHO NA JORNADA DO ESTAGIÁRIO.
''')

preparado = input('Você está preparado para jogar [S/N]? ').strip().upper()[0]
while preparado not in 'SN':
    preparado = input('Opção inválida! Você está preparado para jogar [S/N]? ').strip().upper()[0]
if preparado == 'S':
    personagem.limpar() # limpa o console
    personagem.escolha() # executa a função escolha para verificar o personagem
    personagem.limpar() # limpa o console
    print(relogio)
    print(personagem) # status inicial do personagem

    while True: # enquanto o jogador não quiser sair do jogo
        levantar = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, olha a hora! 
        Temos muito o que fazer antes de ir ao trabalho. 
        O que você quer fazer?
        [1] Levantar
        [2] "Só mais 5 minutinhos e eu levanto"
        [0] SAIR DO JOGO

        ''')).strip().upper()[0] # opção do jogador
        while levantar not in '012': # se o jogador inserir uma opção inválida, perguntará novamente até que a opção seja 0, 1 ou 2
            levantar = str(input(f'''
        OPÇÃO INVÁLIDA!
        {personagem.nome}, olha a hora! 
        Temos muito o que fazer antes de ir ao trabalho. 
        O que você quer fazer?
        [1] Levantar
        [2] "Só mais 5 minutinhos e eu levanto"
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]
        if levantar in '12': # se o jogador escolher 1 ou 2, executa a função levantar() na classe Personagem
            personagem.levantar(levantar) # dentro da função fazer um while levantar == '2' para incrementar mais tempo no relógio enquanto o personagem não levanta
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase() # passa de fase no jogo
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else: # se o jogador pressionar 0, ele desiste do jogo e o jogo encerra com a mensagem contida na função desistir() na classe Personagem
            print(personagem.desistir())
            break

        if personagem.statusPar() == True: # se o jogador atingir uma das condições da função status() na classe Personagem, o jogo encerra porque o jogador perdeu
            print(personagem.perdeu())
            break

        cafedamanha = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, olha o dia lindo que faz lá fora!
        Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
        O que você quer comer?
        [1] Frutas, pão, café e suco - um café da manhã bem reforçado!
        [2] A pizza amanhecida que você pediu ontem na janta com o resto de Coca-Cola
        [3] Café puro, sem açúcar e sem nada pra comer, pois você fica enjoado de manhã.
        [4] Não vai comer nem beber nada
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while cafedamanha not in '01234':
            cafedamanha = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, olha o dia lindo que faz lá fora!
        Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
        O que você quer comer?
        [1] Frutas, pão, café e suco - um café da manhã bem reforçado!
        [2] A pizza amanhecida que você pediu ontem na janta com o resto de Coca-Cola
        [3] Café puro, sem açúcar e sem nada pra comer, pois você fica enjoado de manhã.
        [4] Não vai comer nem beber nada
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]

        if cafedamanha in '1234':
            personagem.refeicao(cafedamanha)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break

        if personagem.statusPar() == True:
            print(personagem.perdeu())
            break


        banho = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, agora é hora de se preparar para o trabalho!
        Que tal tomar um banho para se refrescar e acordar de vez?
        [1] Sim, um banho é uma ótima ideia!
        [2] Nem a pau, um frio desses e eu vou tomar banho?
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while banho not in '012':
            banho = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, agora é hora de se preparar para o trabalho!
        Que tal tomar um banho para se refrescar e acordar de vez?
        [1] Sim, um banho é uma ótima ideia!
        [2] Nem a pau, um frio desses e eu vou tomar banho?
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]
        
        if banho in '12':
            personagem.banho(banho)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break
        
        if personagem.statusPar() == True:
            print(personagem.perdeu())
            break

        ida = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, hora de ir trabalhar!
        Como você irá para o trabalho?
        [1] Vou a pé ou de bicicleta, para praticar um exercício físico
        [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera
        [3] Vou de Uber porque não sou obrigadx a passar perrengue
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while ida not in '0123':
            ida = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, hora de ir trabalhar!
        Como você irá para o trabalho?
        [1] Vou a pé ou de bicicleta, para praticar um exercício físico
        [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera
        [3] Vou de Uber porque não sou obrigadx a passar perrengue
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]
        
        if ida in '123':
            personagem.trajeto(ida)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break
        
        if personagem.statusPar() == True:
            print(personagem.perdeu())
            break

        if relogio.atrasado() == True:
            print(personagem.perdeu())
            break
        
        else:
            situacao1 = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, você chegou no trabalho e o programa que você alterou ontem
        não funciona! Vários clientes estão reclamando e ameaçando cancelar o serviço com
        a empresa. Seu chefe está maluco contigo e marca uma reunião para resolver o problema.
        
        O que você faz?
        [1] Respondo o chefe educadamente e falo que vou resolver o problema. Já sento na mesa e começo a trabalhar
        [2] Fico sem reação e não consigo falar nada para o chefe, vou ao banheiro e me tranco lá para refletir
        [3] Dou um tapa na mesa, me revolto e começo a gritar com o chefe. Vou para a minha mesa e não consigo produzir nada
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]

            while situacao1 not in '0123':
                situacao1 = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, você chegou no trabalho e o programa que você alterou ontem
        não funciona! Vários clientes estão reclamando e ameaçando cancelar o serviço com
        a empresa. Seu chefe está maluco contigo e marca uma reunião para resolver o problema.
        
        O que você faz?
        [1] Respondo o chefe educadamente e falo que vou resolver o problema. Já sento na mesa e começo a trabalhar
        [2] Fico sem reação e não consigo falar nada para o chefe, vou ao banheiro e me tranco lá para refletir
        [3] Dou um tapa na mesa, me revolto e começo a gritar com o chefe. Vou para a minha mesa e não consigo produzir nada
        [0] SAIR DO JOGO

                ''')).strip().upper()[0]

            if situacao1 in '123':
                personagem.bugtrabalho(situacao1)
                personagem.limpar()
                print(relogio)
                print(personagem)
                personagem.passar_fase()
                print(f'Carregando a fase {personagem.fase:02d}')
                sleep(2)
            else:
                print(personagem.desistir())
                break
            
        if personagem.statusPar() == True:
            print(personagem.perdeu())
            break

        situacao2 = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, após resolver o problema, seu chefe te chama na sala
        de reuniões para uma conversa. Você será alocado em um novo projeto, mais
        difícil e mais importante para a empresa.

        O que você faz?
        [1] Pergunta quanto ganhará de aumento para verificar se a realocação vale a pena
        [2] Agradece e aceita a oportunidade
        [3] Recusa a oportunidade e sai da sala de reuniões
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]

        while situacao2 not in '0123':
            situacao2 = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, após resolver o problema, seu chefe te chama na sala
        de reuniões para uma conversa. Você será alocado em um novo projeto, mais
        difícil e mais importante para a empresa.

        O que você faz?
        [1] Pergunta quanto ganhará de aumento para verificar se a realocação vale a pena
        [2] Agradece e aceita a oportunidade
        [3] Recusa a oportunidade e sai da sala de reuniões
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]

        if situacao2 in '123':
            personagem.promocao(situacao2)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break

        almoco = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, o primeiro tempo do trabalho já foi!
        Seu estômago deve estar roncando de fome, não? É hora do almoço.

        Onde você vai comer?
        [1] Restaurante chique com os chefes
        [2] Marmita com os outros estagiários
        [3] Pizza amanhecida que você trouxe de casa, sozinho na copa da empresa
        [4] Não vai comer nada
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while almoco not in '01234':
            almoco = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, olha o dia lindo que faz lá fora!
        Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
        O que você quer comer?
        [1] Restaurante chique com os chefes
        [2] Marmita com os outros estagiários
        [3] Pizza amanhecida que você trouxe de casa, sozinho na copa da empresa
        [4] Não vai comer nada
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]

        if almoco in '1234':
            personagem.refeicao(almoco)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break

        if personagem.sstatusPar() == True:
            print(personagem.perdeu())
            break

        situacao3 = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, após o expediente você é convidado para
        um happy hour com a galera da empresa.

        O que você vai fazer?
        [1] Topo e vou tomar uma cervejinha com o pessoal
        [2] Digo que estou cansado e não vou
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while situacao3 not in '012':
            situacao3 = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, após o expediente você é convidado para
        um happy hour com a galera da empresa.

        O que você vai fazer?
        [1] Topo e vou tomar uma cervejinha com o pessoal
        [2] Digo que estou cansado e não vou
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]
        
        if situacao3 in '12':
            personagem.happyhour(situacao3)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break
        
        if personagem.status() == True:
            print(personagem.perdeu())
            break

        volta = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, hora de ir trabalhar!
        Como você irá para o trabalho?
        [1] Vou a pé ou de bicicleta, para praticar um exercício físico
        [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera
        [3] Vou de Uber porque não sou obrigadx a passar perrengue
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while volta not in '0123':
            volta = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, hora de ir para casa!

        Como você irá embora?
        [1] Vou a pé ou de bicicleta, para praticar um exercício físico
        [2] Vou de transporte público, para contribuir para menos emissão de carbono na atmosfera
        [3] Vou de Uber porque não sou obrigadx a passar perrengue
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]
        
        if volta in '123':
            personagem.trajeto(volta)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break
        
        if personagem.status() == True:
            print(personagem.perdeu())
            break

        if relogio.atrasado() == True:
            print(personagem.perdeu())
            break

        janta = str(input(f'''
        Fase {personagem.fase:02d}
        {personagem.nome}, o primeiro tempo do trabalho já foi!
        Seu estômago deve estar roncando de fome, não? É hora do almoço.

        Onde você vai comer?
        [1] Restaurante chique com os chefes
        [2] Marmita com os outros estagiários
        [3] Pizza amanhecida que você trouxe de casa, sozinho na copa da empresa
        [4] Não vai comer nada
        [0] SAIR DO JOGO

        ''')).strip().upper()[0]

        while janta not in '01234':
            janta = str(input(f'''
        OPÇÃO INVÁLIDA!
        Fase {personagem.fase:02d}
        {personagem.nome}, olha o dia lindo que faz lá fora!
        Seu estômago deve estar roncando de fome, não? É hora de tomar um bom café da manhã
        O que você quer comer?
        [1] Restaurante chique com os chefes
        [2] Marmita com os outros estagiários
        [3] Pizza amanhecida que você trouxe de casa, sozinho na copa da empresa
        [4] Não vai comer nada
        [0] SAIR DO JOGO

            ''')).strip().upper()[0]

        if janta in '1234':
            personagem.refeicao(janta)
            personagem.limpar()
            print(relogio)
            print(personagem)
            personagem.passar_fase()
            print(f'Carregando a fase {personagem.fase:02d}')
            sleep(2)
        else:
            print(personagem.desistir())
            break

        if personagem.statusPar() == True:
            print(personagem.perdeu())
            break
        else:
            print(personagem.venceu())

        continua = input('Deseja jogar novamente [S/N]? ').strip().upper()[0]
        while continua not in 'SN':
            continua = input('Opção inválida! Deseja jogar novamente [S/N]? ').strip().upper()[0]
            
        if continua == 'S':
            relogio.definir(6,0)
        else:
            print('Obrigado por jogar!')
            break

else:
    personagem.limpar()
    print(personagem.desistir())