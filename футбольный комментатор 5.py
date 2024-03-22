Goal = 0
First_Game_Score1, First_Game_Score2 = map(
    int, input().split(":"))  # ввод результата первой игры
Second_Game_Score1, Second_Game_Score2 = map(
    int, input().split(":"))  # ввод результата текущей игры
# домашняя или гостевая была игра для первой команды
Destination_Flag = int(input())
# 1 - если первая игра дома, 2 - если в гостях
First_Team_Goals = First_Game_Score1 + Second_Game_Score1
Second_Team_Goals = First_Game_Score2 + Second_Game_Score2

if First_Team_Goals > Second_Team_Goals:  # соотношение мячей положительное - ничего не делаем
    Goal = 0

elif First_Team_Goals == Second_Team_Goals:  # соотношение мячей одинаковое

    if Destination_Flag == 2:  # если первая игра гостевая
        # если в гост. игре забили больше или столько же, сколько пропустили дома
        if First_Game_Score1 > Second_Game_Score2:
            Goal = 0
        else:  # если в домашней пропустили больше, чем забили в гостевой
            Goal = Second_Game_Score2 - First_Game_Score1 + 1

    else:  # если первая домашняя игра
        # если в гост. игре забили больше или столько же, сколько пропустили дома
        if Second_Game_Score1 > First_Game_Score2:
            Goal = 0
        else:  # если в домашней пропустили больше, чем забили в гостевой
            Goal = First_Game_Score2 + Second_Game_Score2 + 1

else:  # соотношение мячей отрицательное
    if Destination_Flag == 2:  # если первая игра гостевая
        Goal = Second_Team_Goals - First_Team_Goals + 1
    else:
        Goal = Second_Team_Goals - First_Team_Goals
print(Goal)
