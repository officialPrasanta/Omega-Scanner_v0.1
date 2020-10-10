import whois
from googlesearch import search
from core.etc.parse_json import RenderJson, ObjProcessing


def lookup(host):
    target = whois.whois(host)
    x_info, y_info = ObjProcessing(target)
    return x_info, y_info


def dorking(host, index):
    command = RenderJson()
    choices = command['command']
    dork = choices[index]
    query = 'site: ' + host + ' ' + dork
    response_list = []
    for response in search(query, stop=10, pause=2):
        response_list.append(response)
    return response_list


def omega(host, index):
    x_info, y_info = lookup(host)
    gdork_info = dorking(host, index)
    return x_info, y_info, gdork_info