# -*- coding: utf-8 -*-
from fabric.api import env, cd, run, prefix


env.hosts = ['root@konstantin.djigitdev.com']


def deploy():
    """
    Комманда может создать файл `local.py` на удаленном сервере, если он ещё не
    создан. Если к базе данных требуется пароль, передайте параметр `db_password`.
    Пример:
        $ fab deploy
    :param db_password:
    """
    environment = prefix('source /root/project/env/bin/activate')

    with cd('/root/project/vacation'):
        with environment:
            run('git pull')
            run('pip install -r requirements.txt')
            run('python ./manage.py migrate')
            #run('python ./manage.py collectstatic --noinput')


