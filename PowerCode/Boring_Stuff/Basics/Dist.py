team = {
    'NAME': 'VIVEK KUMAR',
    'AGE': '23',
    'TYPE': 'FULL TIME',
    'GENDER': 'MALE',
}

vivek = {
    'NAME': 'VIVEK KUMAR',
    'TYPE': 'FULL TIME',
    'AGE': '23',
    'GENDER': 'MALE',
}

# print (team['GENDER'])
# if team == vivek:
#     print(vivek)

# print (team.values())
# print(team.keys())
# print (team.items())

# for age in team.keys():
#     print(age)

# if '23' in team.values():
#     print("Hello world friend found ")


# if 'VIVEK KUMAR' in team:
    # print (team)

print (team.get('AGE',0))

