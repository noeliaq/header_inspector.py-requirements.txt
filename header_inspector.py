import requests
import json
BASE_URL = "https://jsonplaceholder.typicode.com"


def header_inspector(response):


    print (f"\n=== Request Headers===")
    for key, value in response.request.headers.items():
        print(f" {key} {value}")

    print (f"\n=== Response Headers===")
    print (f" Status: {response.status_code} {response.reason}")

    #content type from response
    content_type = response.headers.get("Content-Type", "Not specified")
    print(f" Content-Type: {content_type}")

    #content length from response
    content_length = response.headers.get("Content-Length" , "Not specified")  
    print (f" Content-Length: {content_length}")

#Cache checking
    headers = response.headers

    has_cache = (
        "Cache-Control" in headers
        or "ETag" in headers
        or "Expires" in headers
        or "Age" in headers
    )
    print (f" Caching headers present: {has_cache}")

#Rate-limiting check:
    has_rate_limit = False
    for name in headers:
         if "ratelimit" in name.lower():
              has_rate_limit = True
              print(f" Found rate limit header {name} = {headers[name]}")
         
    print (f" Rate-limiting headers present {has_rate_limit}")


    for key, value in response.headers.items():
            print(f" {key} {value}")

    
    total_response_headers = len(response.headers)
    print(f" The Total Response Headers is: {total_response_headers}")

print (f"\n{'*' *15} GET posts/1 {'*' *15}")
result_get_posts_1 = requests.get(f"{BASE_URL}/posts/1")
header_inspector(result_get_posts_1)

print (f"\n{'*' *15} GET users/1 {'*' *15}")
result_get_users_1= requests.get(f"{BASE_URL}/users/1")
header_inspector(result_get_users_1)

print (f"\n{'*' *15} GET /get{'*' *15}")
result_get= requests.get("https://httpbin.org/get")
header_inspector(result_get)

print (f"\n{'*' *15} POST /posts{'*' *15}")

result_post= requests.post("https://httpbin.org/post",
    json={
     "title": "REST API Fundamentals",
     "description": "Introduces students, web developers, and software engineers to the core concepts of designing, consuming, and testing Representational State Transfer (REST) APIs",
     "instructor": "Daniel Sanchez"}, headers = { "X-Student-Name": "Noelia Quiroga"}
     )

header_inspector(result_post)

result = result_post.json()
print(json.dumps(result, indent=2))
# header_inspector(result)
