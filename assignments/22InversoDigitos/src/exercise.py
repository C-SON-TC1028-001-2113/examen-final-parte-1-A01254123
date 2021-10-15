def main():
    #escribe tu código abajo de esta línea
    num=int(input("Enter a number: "))
    if len(str(num))>6:
        print ('Too long')
    else:
        if int(num)<0:
            num=str(num)[0::-1]
            num=f"-{str(num)[:-1]}"
        else:
            num=str(num)[::-1]
        print(num)
if __name__=='__main__':
    main()