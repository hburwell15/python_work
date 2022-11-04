def build_profile(first, last, **user_info):
    '''Build a dictonary containing everything we know about a user.'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('hannah', 'burwell', favorite_sport='soccer', favorite_color='red', favorite_animal='bats')
print(user_profile)