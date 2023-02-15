tanish0 = {
    'ismi': 'ANONYMOUS',
    'turi': ':):):)',
    'yoshi': '15',
    'bo\'yi': '1.65',
    'tug\'ilgan sanasi': None,
    'yashash joyi': 'Toshkent G\'uncha (Tinchlik metro)'
}
tanish1 = {
    'ismi': 'SECRET',
    'turi': 'yaqin do\'st',
    'yoshi': '16',
    'bo\'yi': '1.73',
    'tug\'ilgan sanasi': None,
    'yashash joyi': 'Qarshi Beshkent Xtaykenti'
}
tanish2 = {
    'ismi': 'NONE',
    'turi': 'akam',
    'yoshi': '19',
    'bo\'yi': '1.80',
    'tug\'ilgan sanasi': None,
    'yashash joyi': 'Namangan'
}

tanishlar = [tanish0, tanish1, tanish2]
for tanish in tanishlar:
    print(f'Bu yerda meni tanishlarimni ma\'lumotlari bor:\n{tanish.values()}')