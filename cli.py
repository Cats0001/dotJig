import json
from sources.functions import jig_profile
from PyInquirer import prompt

if __name__ == '__main__':
    finding_profiles = True
    while finding_profiles:
        profile_file = input('Profiles File: ')
        try:
            with open(profile_file, 'r') as file:
                profiles_data = json.load(file)
                finding_profiles = False
        except FileNotFoundError:
            print('File Not Found. \n')
        except json.JSONDecodeError:
            print('Invalid JSON. \n')

    question_prompt = [{
        'type': 'checkbox',
        'name': 'profiles',
        'message': 'Select Profiles to Jig:',
        'choices': []
    },
        {
            'type': 'input',
            'name': 'amount',
            'message': 'How many new profiles would you like to make per original?',
            'filter': lambda val: int(val)
        }]

    index = 0
    for profile in profiles_data:
        question_prompt[0]['choices'].append({
            'key': index,
            'name': profile['name'],
            'value': index
        })
        index += 1

    answer = prompt(question_prompt)

    new_profiles = []

    for profile_index in answer['profiles']:
        print(f'Jigging Profile at index: {profile_index}')
        new_profiles.extend(jig_profile(
            profiles_data[profile_index],
            answer['amount']))

    with open('jiggedProfiles.json', 'w') as saveFile:
        json.dump(new_profiles, saveFile)
        input('Done! Press any key to exit.')