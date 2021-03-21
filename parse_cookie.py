def parse_cookie(query: str) -> dict:
    res = {}
    if query:
        data = query.split(';')
        for i in data:
            if '=' in i:
                res[i.split('=')[0]] = '='.join(i.split('=')[1:])

    return res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
