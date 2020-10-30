import sys

if sys.version_info.major == 2:
    choice = raw_input('Digite 0 para MRU, 1 para MRUV: ')
elif sys.version_info.major == 3:
    choice = input('Digite 0 para MRU, 1 para MRUV: ')

if (choice == '0'):#MRU
    if sys.version_info.major == 2:
        S0 = raw_input('Digite a posição inicial em m(0, se não houver): ')
    elif sys.version_info.major == 3:
        S0 = input('Digite a posição inicial em m(0, se não houver): ')

    if sys.version_info.major == 2:
        S = raw_input('Digite a posição final em m(apenas enter, se não houver): ')
    elif sys.version_info.major == 3:
        S = input('Digite a posição final em m(apenas enter, se não houver): ')

    if sys.version_info.major == 2:
        V = raw_input('Digite a velocidade em m/s(apenas enter, se não houver): ')
    elif sys.version_info.major == 3:
        V = input('Digite a velocidade em m/s(apenas enter, se não houver): ')

    if sys.version_info.major == 2:
        t = raw_input('Digite o tempo em s(apenas enter, se não houver): ')
    elif sys.version_info.major == 3:
        t = input('Digite o tempo em s(apenas enter, se não houver): ')

    if S == "":
        S = str(int(S0)+ int(V)*int(t))
    elif V == "":
        V = str((int(S) - int(S0))/int(t))
    else:
        t = str((int(S)-int(S0))/int(V))

    print('S = ',S,', S0 = ',S0,',V = ',V,', t =',t)

else:
    print("Ainda não foi implementado")

