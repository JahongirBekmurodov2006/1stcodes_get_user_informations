print("Do'stlar ro'yxatini tuzamiz:")
dostlar = []
d = 1
while True:
    savol = f'{d} do\'stingizni kiritng:\n>>>'
    dost = input(savol)
    dostlar.append(dost)
    takrorlash = input('yana qo\'shaszmi dostlarizni: ha/yoq')
    d+=1
    if takrorlash != 'ha':
        break

print('sizning do\'stlariz royxati:')
for dost in dostlar:
    print(dost.title())