import json
def write_response(responses):
        with open('all_responses.json', 'a') as file:
                json.dump(responses, file)


