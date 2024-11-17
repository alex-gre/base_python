import urllib.request
response = urllib.request.urlopen('https://httpbin.org/get')
print(f'Read: {response.read()}')
print(' Server: ',response.getheader('Server'))
print(' Code:  ',response.getcode())