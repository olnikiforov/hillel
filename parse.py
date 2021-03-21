def parse(query: str) -> dict:
    res = {}
    if '?' in query:
        query = query.split('?')[1]
        for i in query.split('&'):
            if '=' in i:
                i = i.split('=')
                res[i[0]] = i[1]
    return res


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
