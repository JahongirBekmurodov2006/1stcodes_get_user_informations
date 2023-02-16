#savol = 'Kitoblarningizni kiriting'
#savol += '\n{exit} bosing chiqadi\n>>>'
#qiymat = ''
#while True:
   # qiymat = input(savol)
  #  if qiymat == 'exit':
 #       break;


#print('Dastur tugadi!')

savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == "exit" or qiymat == "quit":
        break
    yosh = int(qiymat)

    if yosh < 7:
        narh = 2000
    elif 7 <= yosh < 18:
        narh = 3000
    elif 18 <= yosh < 65:
        narh = 10000
    else:
        narh = 0

    if narh == 0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")
