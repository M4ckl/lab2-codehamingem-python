number = input("Number:")
if len(number) != 15:
    print("Number incorrect")
else:
    r1 = int(number[0])
    r2 = int(number[1])
    i1 = int(number[2])
    r3 = int(number[3])
    i2 = int(number[4])
    i3 = int(number[5])
    i4 = int(number[6])
    r4 = int(number[7])
    i5 = int(number[8])
    i6 = int(number[9])
    i7 = int(number[10])
    i8 = int(number[11])
    i9 = int(number[12])
    i10= int(number[13])
    i11= int(number[14])
    s1,s2,s3,s4 = 0,0,0,0
    s1 = r1 ^ i1 ^ i2 ^ i4 ^ i5 ^ i7 ^ i9 ^ i11
    s2 = r2 ^ i1 ^ i3 ^ i4 ^ i6 ^ i7 ^ i10 ^ i11
    s3 = r3 ^ i2 ^ i3 ^ i4 ^ i8 ^ i9 ^ i10 ^ i11
    s4 = r4 ^ i5 ^ i6 ^ i7 ^ i8 ^ i9 ^ i10 ^ i11
    print(f"\nS1 = {r1} ⊕  {i1} ⊕  {i2} ⊕  {i4} ⊕  {i5} ⊕  {i7} ⊕  {i9} ⊕  {i11} = {s1}\n" +
            f"S2 = {r2} ⊕  {i1} ⊕  {i3} ⊕  {i4} ⊕  {i6} ⊕  {i7} ⊕  {i10} ⊕  {i11} = {s2}\n" +
            f"S3 = {r3} ⊕  {i2} ⊕  {i3} ⊕  {i4} ⊕  {i8} ⊕  {i9} ⊕  {i10} ⊕  {i11} = {s3}\n"+
            f"S4 = {r4} ⊕  {i5} ⊕  {i6} ⊕  {i7} ⊕  {i8} ⊕  {i9} ⊕  {i10} ⊕  {i11} = {s4}\n")
    errorBit = int(str(s4)+str(s3)+str(s2)+str(s1),2)
    if errorBit == 0:
        print("Вся информация была передана без ошибок!\n")
    else:
        print(f"Ошибка в бите {errorBit}. Правильное сообщение: ", end="")
        for i in range(len(number)):
            if i == errorBit-1:
                if number[i] == "0":
                    print(1, end="")
                else:
                    print(0, end="")
            else:
                print(number[i], end="")