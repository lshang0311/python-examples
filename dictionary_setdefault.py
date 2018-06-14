# basic
d = dict()
d.setdefault('key1')  # value = None

d.setdefault('key2', ['value2'])
d.setdefault('key3', {'k': 'v'})
d.setdefault('key2', ['new value2'])  # no update
print(d)

# one key -> multiple values
DATA_SOURCE = (
    (2017, 'May'),
    (2018, 'June'),
    (2017, 'March'),
    (2017, 'March'),
    (2016, 'October'),
)

d = dict()
for year, month in DATA_SOURCE:
    d.setdefault(year, []).append(month)
print(d)

# nested
nested = dict()

store_id = 's_1'
DATA_SOURCE_STORE_1 = (
    ('fruit', ['apple', 'water melon', 'rock melon']),
    ('taste', ['sweet', 'juicy']),
    ('size', [1, 2, 3, 4, 5]),
    ('price', ['$3.20', '$5.50']),
)
for k, v in DATA_SOURCE_STORE_1:
    value = nested.setdefault(k, {})
    value[store_id] = v

store_id = 's_2'
DATA_SOURCE_STORE_2 = (
    ('fruit', ['apple', 'grape', 'banana']),
    ('taste', ['sweet', 'juicy']),
    ('size', [1, 2, 3, 4, 5]),
    ('price', ['$3.20', '$5.50']),
)
for k, v in DATA_SOURCE_STORE_2:
    value = nested.setdefault(k, {})
    value[store_id] = v

print(nested)
