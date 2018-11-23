import importlib.machinery
from distutils.sysconfig import get_python_lib

# if local environment, use psycopg2 installed in python library (site-packages), otherwise use from binary (psycopg2 subdirectory in this folder)
try:
    psycopg2 = importlib.machinery.SourceFileLoader('psycopg2', get_python_lib()+'/psycopg2/__init__.py').load_module()
except:
    import psycopg2

# connect to database
def connect():
    dbname = "xxxxx"
    user = "xxxxx"
    host = "xxxxx.eu-west-1.rds.amazonaws.com"
    password = "xxxxx"
    try:
        return psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password))
    except:
        print("I am unable to connect to the database")
