import requests
from fabric.api import local


def update():
    local('rm jquery.layout.min.js')
    local('rm layout-default.css')
    latest_version = requests.get('https://raw.githubusercontent.com/allpro/layout/master/layout.jquery.json').json()["version"]
    print 'latest version: {0}'.format(latest_version)
    local('wget https://github.com/allpro/layout/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    local('cp layout-master/source/stable/jquery.layout.min.js .')
    local('cp layout-master/source/stable/layout-default.css .')
    local('rm -rf layout-master')
