from os import system
from random import randint

class Character():
    def __init__(self,power:int,armor:int,speed:int):
        self.damage = power
        self.armor = armor
        self.speed = speed

class Player(Character):
    def __init__(self,name:str,power:int,heal:int,armor:int,speed:int):
        Character.__init__(self,power,armor,speed)
        self.name = name
        self.heal = heal
        self.live = True
    
    def Vur(self,player,enemy,enemies):
        if enemy.speed > 5:
            change = randint(1,10)
            if change > 5:
                print("Rakibe saldırmayı denedin ama hızlı bir hamleyle kaçınmayı başardı! Saldırı yapamadın!")
            else:
                damage = player.damage - enemy.armor
                if damage <= 0:
                    print(f"Rakibe {player.damage} hasarlık saldırı yaptın fakat rakibinin zırhı {enemy.armor}! Hasar veremedin!")
                else:
                    enemy.heal -= damage
                    if enemy.heal <= 0:
                        print(f"Düşmana {player.damage} değerinde bir saldırı yaptın! {enemy.armor} zırhı olmasına rağmen düşmanı öldürdün!")
                        enemies.remove(enemy)
                    else:
                        print(f"{player.damage} hasarlık saldırı yaptın ama düşmanın {enemy.armor} zırhı var!{damage} hasar verdin düşmanının {enemy.heal} canı kaldı!")
        else:
            damage = player.damage - enemy.armor
            if damage <= 0:
                print(f"Rakibe {player.damage} hasarlık saldırı yaptın fakat rakibinin zırhı {enemy.armor}! Hasar veremedin!")
            else:
                enemy.heal -= damage
                if enemy.heal <= 0:
                    print(f"Düşmana {player.damage} değerinde bir saldırı yaptın! {enemy.armor} zırhı olmasına rağmen düşmanı öldürdün!")
                    enemies.remove(enemy)
                    
                else:
                    print(f"{player.damage} hasarlık saldırı yaptın ama düşmanın {enemy.armor} zırhı var!{damage} hasar verdin düşmanının {enemy.heal} canı kaldı!")


class Enemy():
    def __init__(self):
        self.damage = randint(10,50)
        self.heal = randint(10,100)
        self.armor = randint(1,15)
        self.speed = randint(1,10)

    def Vur(self,enemy,player):
        if player.speed > 4:
            change = randint(1,10)
            if change > 5:
                print("Üstüne güçlü bir saldırı gelirken hızlı davranıp kaçınmayı başardın! Hasar almadın!")
            else:
                damage = enemy.damage - player.armor
                if damage <= 0:
                    print(f"{enemy.damage} değerinde bir saldırıya uğradın fakat {player.armor} zırhın olduğu için hasar almadın!")
                else:
                    player.heal -= damage
                    if player.heal <= 0:
                        print(f"{enemy.damage} değerinde bir saldırıya uğradın! {player.armor} kadar zırhın olmasına rağmen çok büyük acı hissettin! Gözlerin kararıyor...")
                        player.live = False
                    else:
                        print(f"{enemy.damage}'lık bir saldırıya uğradın ama zırhın {player.armor} kadar hasarı absorbe etti! {damage} hasar aldın! {player.heal} Canın kaldı!")

        else:
            damage = enemy.damage - player.armor
            if damage <= 0:
                print(f"{enemy.damage} değerinde bir saldırıya uğradın fakat {player.armor} zırhın olduğu için hasar almadın!")
            else:
                player.heal -= damage
                if player.heal <= 0:
                    print(f"{enemy.damage} değerinde bir saldırıya uğradın! {player.armor} kadar zırhın olmasına rağmen çok büyük acı hissettin! Gözlerin kararıyor...")
                    player.live = False
                else:
                    print(f"{enemy.damage}'lık bir saldırıya uğradın ama zırhın {player.armor} kadar hasarı absorbe etti! {damage} hasar aldın! {player.heal} Canın kaldı!")
            
enemies = []
for i in range(5):
    enemies.append(Enemy())

live = True
win = False
while live == True and win == False:
    system("clear")
    print("CEHENNEMİN DERİNLİKLERİNDEN ÇIKAN SEN, ARTIK BİZİM SONSUZ KÖLEMİZ VE YOLUMUZDA CAN VERECEK SAVAŞÇIMIZSIN!")
    print("İYİLİKLE SAVAŞMAN İÇİN SANA, SENİN ŞANSINA GÖRE GÜÇLER BAHŞEDECEĞİZ!")
    print("KORKMA ÖLÜMLÜ! SEN GİDERKEN SENDEN FAZLASINI DA YANINDA GÖTÜRECEKSİN! HAHAHAHAHA!")
    print("ÖNCE KENDİNE BİR İSİM BELİRLE ÖLÜMLÜ! BELKİ EFSANELER YARATIRSIN VE KURULACAK İMPARATORLUĞUMUZDA ADINA ŞARKILAR YAZILIR!\n")
    name = str(input("İsmin : "))

    system("clear")
    print(f"DEMEK {name}! BU NE SAÇMA İSİM BÖYLE HAHAHAHAH!")
    print("NEYSE ADINA ŞARKI YAZILMAYACAĞI KESİNLEŞTİ HAHAHAHAHAHAHA!")
    print("İSİM KOYMAYI BECEREMEDİN BARİ BİR 20'LİK ZAR AT DA GÜÇ DEĞERİNİ BELİRLE ÖLÜMLÜ!")
    print("ATTIĞIN ZAR DEĞERİNİN 5 KATINI BAĞIŞLAYACAĞIZ SANA!\n")
    input("Bir Zar Atmak İçin [ENTER]'e Bas")

    system("clear")
    damage = randint(1,20) * 5
    if damage < 50:
        print("HAHAHAHAHAHAHAHAHAHAHAHAHAHA!")
        print(f"SANA 5 KATINI BAHŞETMEMİZE RAĞMEN GÜCÜN {damage}! BİR FARE KADAR GÜÇLÜSÜN HAHAHAHAHHA!")
    else:
        print(f"HMM GÜCÜN {damage}! PEK DE FENA SAYILMAZ, İŞİMİZE YARAYACAK GİBİSİN!")
    print("BAKALIM... BİR 20'LİK DAHA AT VE CAN DEĞERİNİ BELİRLE ÖLÜMLÜ! YİNE 5 KATI BİZDEN SANA ARMAĞAN!\n")
    input("Bir Zar Atmak İçin [ENTER]'e Bas")

    system("clear")
    heal = randint(1,20) * 5
    print(f"CAN DEĞERİN {heal} OLDU! AMA ÇOK SEVİNME! SONUÇTA ÖLÜMLÜSÜN HAHAHAHAHAHAHAHAH!")
    print("BU SEFERKİ ZARI BİZİ NEŞELENDİRMEK İÇİN ATACAKSIN ÖLÜMLÜ!")
    print("10'LUK BİR ZAR AT EĞER 10 ATARSAN SANA CAN DEĞERİN KADAR ZIRH VERİCEZ! EĞER ATAMAZSAN İNSAFIMIZA KALDIN HAHAHAHAHAHAHHA!\n")
    input("Bir Zar Atmak İçin [ENTER]'e Bas")

    system("clear")
    armor = randint(1,10)
    if armor >= 9:
        armor == heal
        print(f"ÇOK ŞANSLISIN ÖLÜMLÜ! ZIRH DEĞERİN {armor}!")
    else:
        print(f"HEM BECERİKSİZSİN HEM DE ŞANSSIZ HAHAHAHAHAHAHAHAH! ZIRH DEĞERİN {armor}")
    print("SANA İYİ BİR HABERİM VAR ÖLÜMLÜ! SANA BONUS ÖZELLİKLER DE EKLEYECEĞİZ!")
    print("SANA VERECEĞİMİZ HIZ İLE RAKİPLERİNİN VURUŞLARINDAN KAÇMAYI DENEYEBİLİRSİN! HADİ ÇIK GİT ARTIK\n")
    speed = randint(1,10)
    input("Devam Etmek İçin [ENTER]'e Bas!")
    player = Player(name,damage,heal,armor,speed)

    while live == True and win == False:
        system("clear")
        print(f"""
                ADIN   : {player.name}
                CANIN  : {player.heal}
                GÜCÜN  : {player.damage}
                ZIRHIN : {player.armor}
                HIZIN  : {player.speed}

        """)

        x = 1
        for enmy in enemies:
            print(f"{x}.Düşmanın Canı: {enmy.heal}  Hasarı: {enmy.damage}  Zırhı: {enmy.armor}  Hızı: {enmy.speed}")
            x += 1

        choice = int(input("Vurmak istediğin düşmanın sırasını gir : "))
        print("\n")
        choice = choice - 1
        if choice > 5:
            print("Sadece var olan bir düşmana vurabilirsin! Boşa saldırdın!")
        else:
            player.Vur(player,enemies[choice],enemies)

        
        if not enemies:
            win = True
        else:
            enemies_number = len(enemies) - 1
            x = randint(0,enemies_number)
            enemies[x].Vur(enemies[x],player)

        input("\nDevam Etmek İçin [ENTER]'e Bas!")
        if player.live == False:
            live = False
        if not enemies:
            win = True


        
    

    

print("GAME OVER")