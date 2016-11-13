import requests

def getReps(city):
    key = 'AIzaSyDCSzaHH_Hu_VHUHrgGNqgmXu9rUzLlVro';
    base = 'https://www.googleapis.com/civicinfo/v2/representatives';
    url = base + '?address=' + city + '&key=' + key;

    response = requests.get(url)

    entire_response  = response.json()

    alexa_string = ""

    offices_array  = entire_response['offices']
    pols_array = entire_response['officials']

    relevant_indices = []

    for entry in offices_array:
        if (("Senate" in entry['name']) or ("House of Representatives" in entry['name'])):
            relevant_indices += entry['officialIndices']

    for i in relevant_indices:
        rep = pols_array[i];

        url = rep['urls'][0] if (rep['urls'] is not None) else "p"
        name = rep['name'] if (rep['name'] is not None) else ""
        party = rep['party'] if (rep['party'] is not None) else ""
        phone = rep['phones'][0] if (rep['phones'] is not None) else ""
        title = "";


        if ("house" in url):
            title = "Representative"
        elif ("senate" in url):
            title = "Senator"

        alexa_string += party + " " + title + " " + name + " " + phone + " "


    return alexa_string

print getReps("New York")
