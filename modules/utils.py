# Converts the dataclass instance to a dict (by using the factory function dict_factory). Each dataclass is converted to a dict of its fields, as name: value pairs. dataclasses, dicts, lists, and tuples are recursed into.

# cursor from the sqlite3 db call associated
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d