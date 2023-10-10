def sem_parametros(*args):
    argumentos = list(args)
    print(argumentos)

    total = 0
    for i in args:
        total += i

    print(total)
  
sem_parametros(1, 2, 3)

### ===== Output ===== ###
# [1, 2, 3]
# 6
