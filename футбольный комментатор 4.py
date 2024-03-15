Goal = 0
First_Game_Score1, First_Game_Score2 = map(
    int, input().split(":"))  # ввод результата первой игры
Second_Game_Score1, Second_Game_Score2 = map(
    int, input().split(":"))  # ввод результата текущей игры
# домашняя или гостевая была игра для первой команды
Destination_Flag = int(input())
# 1 - если первая игра дома, 2 - если в гостях
Diff_First_Game = First_Game_Score1 - First_Game_Score2
Diff_Second_Game = Second_Game_Score1 - Second_Game_Score2
First_Team_Goals = First_Game_Score1 + Second_Game_Score1
Second_Team_Goals = First_Game_Score2 + Second_Game_Score2

if First_Team_Goals > Second_Team_Goals:  # соотношение мячей положительное - ничего не делаем
    Goal = 0

elif First_Team_Goals == Second_Team_Goals:  # соотношение мячей одинаковое
    # если первая игра гостевая и в ней забили больше
    if Destination_Flag == 2 and First_Game_Score1 > Second_Game_Score2:
        Goal = 0
    # если вторая игра гостевая и в ней уже забили больше
    elif Destination_Flag == 1 and Second_Game_Score1 > First_Game_Score2:
        Goal = 0
    else:
        Goal = 1

else:  # соотношение мячей отрицательное
    if Destination_Flag == 1:
        Goal = (First_Game_Score2+Second_Game_Score2) - \
            (First_Game_Score1+Second_Game_Score1)
    else:
        Goal = (First_Game_Score2+Second_Game_Score2) - \
            (First_Game_Score1+Second_Game_Score1)+1
print(Goal)
