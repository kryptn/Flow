from sys import argv

from flow import db

dbs = db.session

def reset(pop=False):
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    if 'start' in argv:
        db.create_all()