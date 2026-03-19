#!/usr/bin/env python3
import os
import sys
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print('ERROR: Define GITHUB_TOKEN en el entorno antes de ejecutar.')
        print('  PowerShell: $env:GITHUB_TOKEN="tu_token"')
        sys.exit(1)

    user = os.environ.get('GITHUB_USER')
    if not user:
        print('ERROR: Define GITHUB_USER con tu usuario de GitHub.')
        sys.exit(1)

    repo_name = 'forja-nova-web'
    payload = {
        'name': repo_name,
        'description': 'Forja Nova - Web de estado (generated from local project)',
        'private': False,
        'has_issues': True,
        'has_projects': False,
        'has_wiki': False
    }

    data = json.dumps(payload).encode('utf-8')
    url = 'https://api.github.com/user/repos'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'token {token}',
        'Content-Type': 'application/json'
    }

    req = Request(url, data=data, headers=headers, method='POST')
    try:
        with urlopen(req) as res:
            body = res.read().decode('utf-8')
            info = json.loads(body)
            print('Repositorio creado con éxito:')
            print(info.get('html_url'))
    except HTTPError as e:
        err = e.read().decode('utf-8')
        print('ERROR al crear repositorio:', e.code)
        print(err)
        sys.exit(1)
