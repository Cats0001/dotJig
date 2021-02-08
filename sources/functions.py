import random
from itertools import product


def dot_combos(length: int):
    dots = product(['.', ''], repeat=length)
    return list(dots)


def get_jigs(email):
    email_split = email.split('@')
    addr = list(email_split[0])  # split list at @, take the first section, and convert to list of characters
    ending = '@'+email_split[1]

    middleAddr = addr[1:-1]

    dot_length = len(addr) - 1

    combos = dot_combos(dot_length)

    addresses = []

    for combo in combos:
        new_email = combo[0]

        i = 1
        for item in middleAddr:
            new_email = new_email+item+combo[i]
            i += 1

        new_email = addr[0]+new_email+addr[-1]+ending
        addresses.append(new_email)

    return addresses


def jig_profile(profile: dict, amount: int):
    new_profiles = []
    email = profile["email"]

    jiggable_length = len(email.split('@')[0])-1
    if (2 ** jiggable_length) < amount:
        raise Exception(f'You request more jigs than possible for email: {email}, please try with a longer email.')
    elif '.' in email.split('@')[0]:
        raise Exception(f"It appears {email} has already been jigged.")

    jigs = get_jigs(email)

    for i in range(0, amount):
        index = random.randint(0, len(jigs)-1)
        new_email = jigs.pop(index)
        new_profile = profile.copy()
        new_profile['email'] = new_email
        new_profile['name'] = profile['name']+f'-dotjigged-{i}'

        new_profiles.append(new_profile)

    return new_profiles
