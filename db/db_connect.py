import os

import pymongo as pm

REMOTE = "0"
LOCAL = "1"

DORM_DB = "dormdb"

client = None


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    Returns mongo client object.
    """
    global client
    if client is None:
        print("Setting client...")
        if os.environ.get("LOCAL_MONGO", LOCAL) == LOCAL:
            print("Connecting to Mongo locally...")
            client = pm.MongoClient()


def insert_one(collection, doc, db=DORM_DB):
    """
    Insert single doc into collection.
    """
    client[db][collection].insert_one(doc)


def fetch_one(collection, filt, db=DORM_DB):
    """
    Find with filter and return first doc found.
    """
    for doc in client[db][collection].find(filt):
        return doc


def del_one(collection, filt, db=DORM_DB):
    """
    Find with filter and delete first doc found.
    """
    client[db][collection].delete_one(filt)
