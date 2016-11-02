from fabric.api import local


def test():
    local("python manage.py test polls")


def commit():
    local("git add -p && git commit")

def push():
    local("git push -u origin master")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
     local("python manage.py runserver")


