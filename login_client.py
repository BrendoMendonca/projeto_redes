import http.client
while(True):
    def login(username, password):
        conn = http.client.HTTPConnection('localhost', 8000)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        body = f'username={username}&password={password}'
        conn.request('POST', '/auth', body, headers)
        response = conn.getresponse()
        print(response.read().decode('utf-8'))

    if __name__ == "__main__":
        username = 'user'
        password = 'password'
        login(username, password)
