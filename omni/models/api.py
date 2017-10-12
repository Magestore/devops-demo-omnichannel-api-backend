# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

## API client

API_KEY = '123'

API_HOST = 'https://demo-omnichannel.magestore.com/api/v1/'

## api call for all
def call(api='', data='', headers='', method='GET'):
    ## headers = {'user-agent': 'my-app/0.0.1'}
    ## r = requests.get(url, headers=headers)
    ## r = requests.get(url, data={key: value})
    ## r = requests.get('http://github.com', allow_redirects=False, timeout=0.001)
    ## r.status_code
    ## r.url
    ## r.content
    ## r.text
    ## r.json() ValueError: No JSON object could be decoded.
    ## r.headers()
    ## r.cookies['example_cookie_name']
    ## r.history
    ## r.raise_for_status() ConnectionError exception
    if data == '':
        data = {}
    if headers == '':
        headers = {}
    url = API_HOST + api.strip(' ', '/')
    headers['Authorization'] = 'Basic '+API_KEY

    if method.uppercase() == 'GET':
        requests.get(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'POST':
        requests.post(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'PUT':
        requests.put(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'HEAD':
        requests.head(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'PATCH':
        requests.patch(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'UPDATE':
        requests.update(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'OPTIONS':
        requests.options(url, data=data, headers=headers, allow_redirects=False)
    elif method.uppercase() == 'DELETE':
        requests.delete(url, data=data, headers=headers, allow_redirects=False)

    try:
        r_data = r.json()
    except ValueError, e:
        return {"status": "error", "message": repr(e)}
    except ConnectionError, e:
        return {"status": "error", "message": repr(e)}
    except Exception, e:
        return {"status": "error", "message": repr(e)}
    return r_data

## create a demo site from existed templates
def createDemo(url_path, template, name='', admin_user='', admin_password=''):
    data = {'url_path': url_path, 'template_name': template}
    if name != '':
        data = {'name': name}
    if admin_user != '' and admin_password != '':
        data = {'admin_user': admin_user, 'admin_password': admin_password}
    r = call('sites', data=data, method='POST')
    if r['status'] == 'success':
        return True
    return False

## create a demo site from existed templates
def cloneDemo(url_path, site_name, name='', admin_user='', admin_password=''):
    data = {'url_path': url_path, 'site_name': site_name}
    if name != '':
        data = {'name': name}
    if admin_user != '' and admin_password != '':
        data = {'admin_user': admin_user, 'admin_password': admin_password}
    r = call('sites', data=data, method='PUT')
    if r['status'] == 'success':
        return True
    return False

def createTemplate(name, from_site, title='', description=''):
    data = {'name': name, 'from_site': from_site}
    if title != '':
        data = {'title': title}
    if description != '':
        data = {'description': description}
    r = call('templates', data=data, method='POST')
    if r['status'] == 'success':
        return True
    return False

## delete old templat and create new one with old name
def updateTemplate(name, from_site, title='', description=''):
    data = {'name': name, 'from_site': from_site}
    if title != '':
        data = {'title': title}
    if description != '':
        data = {'description': description}
    r = call('templates', data=data, method='PUT')
    if r['status'] == 'success':
        return True
    return False

## param name is url_path or name unique
def getSite(name):
    return call('sites/'+name)

## get all sites
def getSiteList():
    return call('sites')

## get one template by name
def getTemplate(name):
    if name == '':
        return False
    return call('templates/'+name)

## get all templates
def getTemplateList():
    return call('templates')

## get all templates
def deleteTemplate(name):
    if name == '':
        return False
    return call('templates/'+name, method='DELETE')

