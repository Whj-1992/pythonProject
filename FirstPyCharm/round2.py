import random


def fight( my_hp,enemy_hp):
    #定义我的攻击力和敌人的攻击力
    my_power = 200
    enemy_power = 200

    print(f"敌人血量{my_hp},我的血量{enemy_hp}" )
    #循环处理我和敌人的血量
    while True:
         my_hp=my_hp-enemy_power
         enemy_hp=enemy_hp-my_power
         if my_hp<=enemy_hp:
            print (f"我输了{my_hp},{enemy_hp}")
            break
         else:
             print(f"我赢了{my_hp},{enemy_hp}")
             break
#利用列表推导式生成hp的值
if __name__ == '__main__':
    hp = [x for x in range(1000, 2000)]
    #my_hp从hp中随机生成
    my_hp = random.choice(hp)
    print(f"{my_hp}")
    #利用randint随机生成敌人的血量
    enemy_hp = random.randint(1000,2000)
    fight( my_hp, enemy_hp )