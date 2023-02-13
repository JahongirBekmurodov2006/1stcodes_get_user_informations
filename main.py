#Userdan qaysi universitetga topshirishini so'rovchi dastur
#MY FIRST PYTHON APPLICATION PROGRAM :)

univers = ['mit', 'harvard', 'stanford', 'yale', 'cambridge', 'oxford']
user_portfolio = []
user = input("Universitetni tanlang \n>>> ")
if user.lower() in univers:
    print(f"{user.upper()} universitetiga qabul hozirda mavjud, biz bilan topshirishingiz mumkin!")

    print(f'\nDemak siz {user.upper()} ga topshirmoqchimisz')
    a = 'ha'
    javob = input('ha/yoq \n>>> ')
    if javob == a:
        print('Agar tog\'ri bo\'lsa portfolioingizda nimalar borligini kiriting')
        portfolio = user_portfolio.append(input('Qani boshladik portfolioni kiritishni \n>>> '))

        print(user_portfolio)

        print("Biz o\'zimiz siz bilan bog\'lanamiz! RAHMAT tashrif uchun!")
    else:
        print('Hayr, yaxshi dam oling!')

else:
    print('Bu universitet bizda mavjud emas yoki xato yozdingiz iltimos tog\'ri va qabul ochiqligini tekshiring\n')
    print(f'Bizda hozirda shu universitetlar uchun qabul ochiq \n{univers}')


