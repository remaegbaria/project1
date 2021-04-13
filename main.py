import requests
 


value = input("enter a country name:\n") 
print(f'you entered {value}') 
r = requests.get('://httpbin.org/get')
print({r})
