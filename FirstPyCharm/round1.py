def fight():#定义函数
    #定义变量
    my_hp = 1000
    my_power = 200
    enemy_hp =1000
    enemy_power =200
    #定义血量计算方式
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp =enemy_hp - my_power
        if  my_hp <= 0 :
             print ("我输了")
             break
        elif enemy_hp <= 0 :
             print ("我赢了")
             break
fight()