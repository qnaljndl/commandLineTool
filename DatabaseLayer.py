import pymongo
from bson import ObjectId

connection = pymongo.MongoClient('localhost', 27017)
database = connection['commandLine_db']
collection = database['commandLine_collection']
print("Connected to Command Line Tool")


def insert_data(data):
    document = collection.insert_one(data)
    return document.acknowledged


def get_data(document_key, document_value, required_values_in_output):
    if required_values_in_output is not None:
        required_keys_in_output = set(required_values_in_output.split(','))

    data_list = []
    all_data = collection.find({document_key: document_value}, {"_id": 0})

    all_keys_set = {'username', 'location'}  # all keys required in set

    if required_values_in_output is None or len(all_keys_set - required_keys_in_output) == 0:
        for data in all_data:
            data_list.append(data)
        return data_list

    elif all_keys_set.intersection(required_keys_in_output) == {'username'}:
        for data in all_data:
            data_list.append(data.get('username'))
        return data_list

    elif all_keys_set.intersection(required_keys_in_output) == {'location'}:
        for data in all_data:
            data_list.append(data.get('location'))
        return data_list


def delete_data(document_key, document_value):
    #document_value can be Location or Username
    document = collection.delete_many({document_key: document_value})
    return document.deleted_count
