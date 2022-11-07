import requests

# single ip request
# THe ip-api processess about 45 request per minute, and you cannot go over it. 
# response = requests.get("http://ip-api.com/json/134.101.5.133").json()
# # print (response)

# print(response['lat'])
# print(response['lon'])



# Prints ip-location of from where the request is coming from.

# def get_ip():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]

# def get_location():
#     ip_address = get_ip()
#     response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
#     location_data = {
#         "ip": ip_address,
#         "city": response.get("city"),
#         "region": response.get("region"),
#         "country": response.get("country_name")
#     }
#     return location_data

# print(get_location())





# to query multiple adresses in one request. 
# Batch api

response = requests.post("http://ip-api.com/batch", json = [
    {"query": "208.80.152.201"},
    {"query": "24.48.0.1"},
    {"query": "134.101.5.133"}
]).json()

for ip_data in response:
   for j, m in ip_data.items():
    print(j, m)
   print("\n")
