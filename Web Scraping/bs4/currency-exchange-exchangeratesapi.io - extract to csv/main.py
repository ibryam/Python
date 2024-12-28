import requests

base_url = "https://api.exchangeratesapi.io/latest"

response = requests.get(base_url)
response.raise_for_status()
print(response.json)


# gather the parameters of interest by prompting the user to give this information.

date = input("Please enter the data(in the format 'yyyy-mm-dd' or 'latest): ") #1
base = input("Convert from (currency): ") #2
curr = input("Convert to (currency): ") #3
quan = float(input("How much {} do you want to convert: ".format(base))) #4




# Construct the URL and send a GET request to it

url = base_url + "/" + date + "?base=" + base + "&symbols=" + curr
response = requests.get(url)
# For unsuccessful requests: print the error message

if (response.ok is False):
    print("\nError {}:".format(response.status_code))
    print(response.json()['error'])
# For successful requests: extract the relevant data and calculate the result
else:
    data = response.json()
    rate = data['rates'][curr]

    result = quan * rate

    print(f"\n{quan} {base} is equal to {result} {curr}, based upon exchange rates on {date}")



# Display the result to the user