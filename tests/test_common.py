import json
import pytest

from src.json2unique.parser import parse_json_to_list_of_unique

io_dict = {
    'basic': ['Users', 'id', 1, 'employee', 'department', 'tech', 'name', 'Mark',
              'project', 2, 'Test', 'status', "ok", 'mistakes', 'Alex', 3, 'parser',
              'filed', 404, 'IO error'],
    'integer': [123],
    'float': [123.456],
    'true': [True],
    'false': [False],
    'none': [None],
    'string': ['hello world!'],
    'empty_string': [''],
    'array': [1, 2, 42],
    'empty_array': [],
    'nested_array': [3, 4, 53],
    'object': ['a', 'b', 'c', 1, 2, 3],
    'empty_object': [],
    'nested_object': ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4],
    'middle_object': [0, True, 2, 3, 4, '+1 (962) 414-2420', 5, 'Susanne Francis', 'strawberry', 'Russo Parker',
                      '904 Fountain Avenue, Gambrills, Minnesota, 7689', 20, '8550aed8-e4d4-4626-a89c-fbb2c7b98edb',
                      '$3,445.53', 'Jean Robertson', 24, 'ipsum', 'rebeccamcmahon@tasmania.com',
                      'Dolore excepteur labore sint velit exercitation cillum officia culpa. Officia dolor voluptate consequat in est et reprehenderit irure eiusmod. Veniam nisi cillum magna aliqua esse. Anim adipisicing consectetur in do sit magna nulla enim sunt pariatur Lorem duis ipsum elit. Dolore tempor laborum Lorem culpa exercitation qui sit laborum aute reprehenderit irure cupidatat exercitation. Fugiat proident anim nulla est labore proident ullamco sint ea ullamco mollit eu voluptate fugiat.\r\n',
                      'longitude', 28.058095, 26.752271, 'company', 32, 'ut', 29, 31, 'Mccoy Vang', 'veniam',
                      'Padilla Cardenas', 'phone', 41.486298, 'laboris', 'address', 'Roberts Acevedo', 'esse',
                      '2020-07-30T01:36:34 -03:00', 53.99873, 'Parsons Galloway', '$3,255.89',
                      '2021-04-14T07:32:48 -03:00', '$2,972.61', 74.130555,
                      'Hello, Lisa Horn! You have 9 unread messages.', '992 Boardwalk , Bluetown, Indiana, 7227',
                      'fugiat', 'Hello, Berry Hubbard! You have 1 unread messages.', 86.107038,
                      '636b6b2e8ab879c21fb5f6f5', 90.584538, 'isActive', 'Norma Dillon',
                      'Fugiat tempor minim enim officia magna magna voluptate amet. Sit elit cupidatat ullamco veniam non. Amet adipisicing qui qui labore consectetur laborum mollit ex ea nulla labore incididunt non mollit. Do amet mollit pariatur voluptate laborum qui sit deserunt.\r\n',
                      'Pacheco Oneill', 'NIMON', 'lisahorn@songbird.com', 'ex', '+1 (801) 510-3959', 'amet', 21,
                      107.925428, 'velit', '+1 (876) 440-2775', '636b6b2e1ae62962fbae9313', 'non', 'favoriteFruit',
                      'deserunt', 'berryhubbard@spherix.com', 'elit', 'mccoyvang@panzent.com', 156.773626,
                      'Consectetur ex ut esse laboris occaecat. Veniam incididunt nisi enim in. Consequat ut sint consectetur irure consectetur. Magna veniam excepteur adipisicing occaecat proident consectetur laboris. Voluptate cupidatat officia commodo enim sint velit tempor id.\r\n',
                      'Hello, Rebecca Mcmahon! You have 8 unread messages.', 'Silva Bailey',
                      'Hello, Dominguez Pacheco! You have 7 unread messages.', 'Lorem', 'qui', 'adipisicing',
                      'registered', 'Janna Conner', '$3,751.99', 'occaecat', 'picture',
                      'fadc8c30-cb38-4c36-a191-dc819c036715', 'Burt Evans',
                      'Hello, Burt Evans! You have 6 unread messages.', '722 Elm Place, Mahtowa, New Mexico, 7834',
                      'laborum', 'OBLIQ', '2018-07-11T12:32:06 -03:00', 'green', 'irure', 'dolor', 'blue', 'Chase Cash',
                      'female',
                      'Ullamco aliquip quis voluptate dolore est qui deserunt aliquip aute officia nisi tempor ad mollit. Magna do elit ex aliqua et do ipsum elit fugiat nostrud amet laborum. Enim ea eu enim duis ipsum nulla reprehenderit tempor eu occaecat et mollit duis voluptate. Labore deserunt adipisicing ex cupidatat ullamco occaecat culpa sit eu duis eiusmod. Sit eiusmod officia laborum nostrud cupidatat. Adipisicing ipsum non excepteur est anim nulla aliqua sint nostrud ipsum nisi pariatur aliqua minim. Dolore in ullamco nostrud excepteur ipsum.\r\n',
                      '903 Nichols Avenue, National, Alabama, 8334', 'duis', 'age',
                      'Aute voluptate laboris commodo mollit deserunt cillum cupidatat eu. Sit dolore pariatur occaecat do Lorem et occaecat reprehenderit eiusmod aliqua magna eu dolor nostrud. Consequat consectetur qui enim labore quis veniam labore aliquip.\r\n',
                      '2018-02-26T11:16:12 -03:00', 'consectetur', 'cupidatat', 'minim', 'Berry Hubbard',
                      'Carmela Lynn', 'id', 'TASMANIA', 'et', 'pariatur', 'PANZENT',
                      'Hello, Mccoy Vang! You have 8 unread messages.', '2014-07-30T11:32:55 -04:00', 'email', '_id',
                      'name', '636b6b2ec6298b87674de535', 'cillum', 'dominguezpacheco@obliq.com', 'tags',
                      '636b6b2e157e6afd005dae53', 'male', '+1 (942) 509-2317', 'Nellie Harris',
                      '636b6b2ea0366d8057a94163', '5fc62bf2-320b-4b28-89da-7194e1d2d180', 'burtevans@nimon.com',
                      '972 Sackman Street, Riner, Puerto Rico, 3279', 'Odom Davis', 'officia', 'SPHERIX',
                      'Sheppard Schultz', 'Frances Gibbs', '$3,234.73', 'about', '2019-03-16T07:05:02 -03:00',
                      '+1 (915) 510-3635', 'latitude', 'friends', '1088dabc-4af2-49ae-b922-45dc0844912e', 'SONGBIRD',
                      'apple', '636b6b2e6409a68efe0b30a4', '+1 (950) 438-3553', 'eyeColor',
                      '52590c36-6d33-4745-924b-09b03e336fb2', '$3,283.93', -68.278341,
                      'Ea id consequat et laborum eu sunt dolore in. Laborum commodo sint exercitation sunt eiusmod aute consectetur reprehenderit ut nisi aute. Qui commodo ex incididunt ipsum velit sint dolore consequat cillum ad culpa sit non. Ullamco excepteur nisi in enim. Tempor amet nisi ut veniam laboris ea dolore. Anim ullamco minim excepteur tempor veniam elit.\r\n',
                      'index', -56.136277, -54.97426, 'Tiffany Weaver', 'Lisa Horn', 'greeting',
                      '2f353644-f445-4e16-92d9-234bf7695582', 'Dominguez Pacheco', 'gender', 'proident',
                      'http://placehold.it/32x32', 'Helga Aguirre', 'brown',
                      '770 Jackson Court, Carlton, New Jersey, 3096', 'guid', 'magna', 'balance', 'excepteur',
                      'Rebecca Mcmahon'],
}


@pytest.mark.parametrize('input_filename', io_dict.keys())
def test_parser(input_filename):
    with open(f'{input_filename}.json') as raw_json:
        loaded = json.load(raw_json)

    resulting_list = parse_json_to_list_of_unique(loaded)

    assert sorted([hash(elem) for elem in resulting_list]) == \
           sorted([hash(elem) for elem in io_dict[input_filename]])
