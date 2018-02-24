from bs4 import BeautifulSoup
import requests
import json
#Lists required in data structure
list_app_data = []
list_utilities = []
list_devops = []
list_b_tools = []

#Response data structure
data = {
        "Application and Data" : list_app_data,
        "Utilities":list_utilities,
        "DevOps":list_devops,
        "Business Tools":list_b_tools
        }

#scrapping function
def techinside(company):
    del list_app_data[:]
    del list_utilities[:]
    del list_devops[:]
    del list_b_tools[:]
    try: #exception handling
        #getting html data into a variable named soup
        html_doc = requests.get("https://stackshare.io/"+company).text
        soup = BeautifulSoup(html_doc, 'html.parser')

        try:
            #searching for particular div
            all_divs = soup.find_all("div", {"class": "show-layer-d"})
        except:
            return "Not found"

        #categorizing data
        for div in all_divs:
            if "Application and Data" in div.text:
                app_data = div
            elif "Utilities" in div.text:
                utilities = div
            elif "DevOps" in div.text:
                devops = div
            elif "Business Tools" in div.text:
                b_tools = div
        #appending data
        for a in app_data.find_all('a'):
            try:
                list_app_data.append(a['data-hint'])
            except:
                pass
        for a in utilities.find_all('a'):
            try:
                list_utilities.append(a['data-hint'])
            except:
                pass
        for a in devops.find_all('a'):
            try:
                list_devops.append(a['data-hint'])
            except:
                pass
        for a in b_tools.find_all('a'):
            try:
                list_b_tools.append(a['data-hint'])
            except:
                pass
        #Response
        return json.dumps(data)#json.dumps dump the python dict to json
    except:
        return "Not found"
