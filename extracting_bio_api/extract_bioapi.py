import requests
import xml.etree.ElementTree as ET
import pandas as pd


def extract_data(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.content
    elif response.status_code == 400:
        print("Bad Request: The request was malformed or contains bad syntax. \n Response:", response.text)
        return None
    else:
        raise Exception(f"Failed to extract data from {api_url}, status code: {response.status_code}")


def transfer_process(output):
    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(output)

    entries = []

    for entry in root.findall('atom:entry', namespaces):
        entry_data = {
            'url_source': entry.find('atom:id', namespaces).text,
            'updated': entry.find('atom:updated', namespaces).text,
            'published': entry.find('atom:published', namespaces).text,
            'title': entry.find('atom:title', namespaces).text,
            'summary': entry.find('atom:summary', namespaces).text,
            'authors': ''.join(author.find('atom:name', namespaces).text for author in
                        entry.findall('atom:author', namespaces))
        }
        entries.append(entry_data)

    dataframe = pd.DataFrame(entries, columns=['url_source',
                                               'updated',
                                               'published',
                                               'title',
                                               'summary',
                                               'authors'])

    return dataframe
