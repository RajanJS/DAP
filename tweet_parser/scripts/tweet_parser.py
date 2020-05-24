import ijson

# filename = "test.json"
filename = "test_tweets.json"
# filename = "nys_tweets_filtered_2017_0.json"

filepath = "./files/"
file = f"{filepath}{filename}"

# Parse json file


def parse_json(json_filename):
    with open(json_filename, 'rb') as input_file:
        # load json iteratively
        parser = ijson.parse(input_file)
        for prefix, event, value in parser:
            print('prefix={}, event={}, value={}'.format(prefix, event, value))

# parse_json(file);


def viewContent(json_filename):
    """   Print json content   """
    with open(file) as jsonfile:
        content = jsonfile.read()
        print(f"\n{content}\n")


def extract_user(json_filename):
    """   Extract user item from json file   """
    with open(json_filename, 'rb') as input_file:
        user = ijson.items(input_file, 'user')
        for number in user:
            print('\n user: {} \n'.format(number))


def extract_item(json_filename, item):
    """   Extract passed item from json file  """
    with open(json_filename, 'rb') as input_file:
        passedItem = ijson.items(input_file, item)
        for itm in passedItem:
            print(f'\n{item}: {itm}\n')

# viewContent(file)

# extract_user(file)


# extract_item(file, 'user')
extract_item(file, 'user.name')
# extract_item(file, 'country')
extract_item(file, 'entities.hashtags')
