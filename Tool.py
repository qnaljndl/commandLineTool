import argparse
import DatabaseLayer


def data_parser():
    parser_data = argparse.ArgumentParser(prog='Operation to execute',
                                          usage='Operation to execute',
                                          description='------------------------------------------------------------\n'
                                                      'Please provide values to do Operations in DB\n'
                                                      'For Example (INSERT)- filename -o insert -u Kunal -l Mumbai\n'
                                                      'For Example (GET)   - filename -o get -u Kunal / -l Mumbai\n'
                                                      'For Example (DELETE) -filename -o delete -u Kunal / -l Mumbai\n'
                                                      '-------------------------------------------------------------',
                                          formatter_class=argparse.RawTextHelpFormatter,
                                          add_help=True
                                          )

    parser_data.add_argument("-o", type=str,
                             help="Choose value from given list only ['insert','get','delete']",
                             metavar='Operation_to_execute', required=True)

    parser_data.add_argument("-u", type=str, help="Enter Data, For Example: -u Kunal",
                             metavar='username', required=False)

    parser_data.add_argument("-l", type=str, help="Enter Data, For Example: -l Mumbai",
                             metavar='location', required=False)

    parser_data.add_argument("-f", type=str, help="Enter Fields you want to get in your output, For Example: -f username / location",
                             metavar='fields', required=False)

    arg_parser = parser_data.parse_args()
    args_dictionary = arg_parser.__dict__
    operation_to_execute = args_dictionary.get('o')
    username = args_dictionary.get('u')
    location = args_dictionary.get('l')
    fields = args_dictionary.get('f')
    operation_to_execute_set = {'insert', 'get', 'delete'}

    if operation_to_execute not in operation_to_execute_set:
        error = "Please enter valid operation value"
        return ValueError(error)

    if operation_to_execute == 'insert':
        insert_data_json = {'username': username, 'location': location}
        inserted_data = DatabaseLayer.insert_data(insert_data_json)
        return inserted_data

    elif operation_to_execute == 'get':
        if username is not None:
            fetched_data = DatabaseLayer.get_data('username', username, fields)
            return fetched_data
        elif location is not None:
            fetched_data = DatabaseLayer.get_data('location', location, fields)
            return fetched_data
        elif location is not None and username is not None:
            print("Please pass only one parameter either username or location, while fetching data!!!!!")
            return None
        else:
            error = "Invalid Parameters"
            return ValueError(error)


    elif operation_to_execute == 'delete':
        if username is not None:
            deleted_data = DatabaseLayer.delete_data('username', username)
            return deleted_data
        elif location is not None:
            deleted_data = DatabaseLayer.delete_data('location', location)
            return deleted_data
        elif location is not None and username is not None:
            print("Please pass only one parameter either username or location, while deleting data!!!!!")
            return None
        else:
            error = "Invalid Parameters"
            return ValueError(error)



