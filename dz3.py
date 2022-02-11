class Url:
    """
    Реализовать класс Url который будет представлять URL:
    a: Его параметрами должны быть все параметры URL (scheme, authority, path, query, fragment).
       Их должен принимать конструктор.
    b: Переопределить операцию == для Url.
       При сравнении Url со строкой должно возвращаться True в случае если строка соответствует Url.
    c: Реализовать метод __str__ который будет формировать строку из Url
    """
    def __init__(self, scheme='', authority='', path=None, query=None, fragment=''):
        self.scheme: str = scheme
        self.authority: str = authority
        self.path: list = path
        self.query: dict = query
        self.fragment: str = fragment

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __str__(self):
        self.completed_url: str = ''

        if self.scheme != '':
            self.completed_url += self.scheme + '://'

        if self.authority != '':
            self.completed_url += self.authority

        if self.path is not None and isinstance(self.path, list) and len(self.path) > 0:
            self.completed_url += '/' + '/'.join(self.path)

        if self.query is not None and isinstance(self.query, dict) and len(self.query) > 0:
            self.completed_url += '?'
            for key, value in self.query.items():
                self.completed_url += f'{key}={value}&'
            self.completed_url = self.completed_url[:-1]

        if self.fragment != '':
            self.completed_url += '#' + self.fragment

        return self.completed_url


class HttpsUrl(Url):
    """d: Реализовать класс HttpsUrl для которого scheme будет равна 'https' (Наследник Url)"""
    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__(scheme='https', authority=authority, path=path, query=query, fragment=fragment)


class HttpUrl(Url):
    """e: Реализовать класс HttpUrl для которого scheme будет равна 'http' (Наследник Url)"""
    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__(scheme='http', authority=authority, path=path, query=query, fragment=fragment)


class GoogleUrl(HttpsUrl):
    """f: Реализовать GoogleUrl для которого authority='google.com'"""
    def __init__(self, path=None, query=None, fragment=''):
        super().__init__(authority='google.com', path=path, query=query, fragment=fragment)


class WikiUrl(HttpsUrl):
    """g: Реализовать WikiUrl для которого authority='wikipedia.org'"""
    def __init__(self, path=None, query=None, fragment=''):
        super().__init__(authority='wikipedia.org', path=path, query=query, fragment=fragment)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'
