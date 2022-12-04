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