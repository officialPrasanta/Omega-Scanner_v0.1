from flask import json
import os

def RenderJson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'json', 'dork_list.json')
    data = json.load(open(json_url))
    return data

def ObjProcessing(target):
    x_list = []
    y_list = []
    for key in target.keys():
        x_list.append(key + ':')
        y_list.append(target.get(key))
    return x_list, y_list
                                                                                                                                                                                                                                                                                      