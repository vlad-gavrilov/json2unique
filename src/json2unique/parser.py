def parse_json_to_list_of_unique(input_item):
    result = set()

    if type(input_item) == dict:
        for key, value in input_item.items():
            result.add(key)
            result.update(parse_json_to_list_of_unique(value))
    elif type(input_item) == list:
        for element in input_item:
            result.update(parse_json_to_list_of_unique(element))
    else:
        result.add(input_item)

    return list(result)
