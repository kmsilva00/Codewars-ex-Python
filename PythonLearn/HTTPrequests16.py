import requests

# Specify the URL you want to request data from
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Send a GET request to the URL
response = requests.get(url)

"""
# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)
else:
    print('Request failed with status code:', response.status_code)
"""



# Specify the URL where you want to send data
url2 = 'https://jsonplaceholder.typicode.com/posts'

# Define the data to send (in this case, a JSON payload)
data2 = {'title': 'New Post', 'body': 'This is the body of the post', 'userId': 1}

# Send a POST request with the data
response2 = requests.post(url, json=data2)

if response2.status_code == 201:
    new_post = response2.json()
    print('New post created with ID:', new_post['id'])
else:
    print('Request failed with status code:', response.status_code)
