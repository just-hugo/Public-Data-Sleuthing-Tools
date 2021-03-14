"""
Retrieves homicide by gender report from the CDC Wonder API D140 database, aka Compressed Mortality, 1999-2016 Report.

CDC asks that automated queries get sent at least 2 minutes apart
"""

import requests

# API URL
baseURL = 'https://wonder.cdc.gov/controller/datarequest'
endpoint = '/D140'
combinedURL = baseURL + endpoint

# Response body file
fileExt = '.xml'
fileName = endpoint.replace('/', '') + '-Homicide-by-Gender' + fileExt

# Sends query parameters to the API and saves the response
with open(fileName, 'w') as file:
    with open('../../API-Responses/D140-Homicide-by-Gender.xml', 'r') as parameters:
        # The API requires the POST request include the following data
        data = {'request_xml': parameters.read(), 'accept_datause_restrictions': 'true'}
        response = requests.post(combinedURL, data=data)
        file.write(response.text)
