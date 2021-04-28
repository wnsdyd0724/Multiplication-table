import random
while True:


    case = input("몇 단 알려주리?")

    i = 1
    a = 1
    b = 1
    d = random.randint(1, 20)
    if case == "구구단":

            for a in range(1 , 10):
                print ("[ " + str (a) + '단 ]')
                for b in range(1, d):
                    print(str(a) + "x" + str(b) + " = " + str(a * b))
                    if (b == d):
                        b = 1
                        break
    else:
        if case.isnumeric():

            print("[ " + str(case) + '단 ]')
            for i in range(1, d):
                print(str(case) + "x" + str(i) + " = " + str(int (i) * int(case)))
                i += 1

        else :
            if case != "종료":
                print("[ 도움말 ] \n 구구단 : 구구단을 안내\n 숫자 : 숫자의 구구단을 안내\n ex) 2 2단 출력 \n 종료 : 종료합니다." )
            else :
                print ("구구단을 종료합니다.")
                break
