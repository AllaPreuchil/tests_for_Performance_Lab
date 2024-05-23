import json


def create_report(test, results):
    for i in results:
        if i['id'] == test['id']:
            test['value'] = i['value']
    if 'values' in test.keys():
        for x in test['values']:
            create_report(x, results)


if __name__ == '__main__':

    with open('tests.json', 'r') as tests:
        tests_data = json.load(tests)
        
    with open('values.json', 'r') as tests:
        values_data = json.load(tests)

    for item in tests_data['tests']:
        create_report(item, values_data['values'])

    with open('report.json', 'w') as file:
        json.dump(tests_data, file, indent=4)
