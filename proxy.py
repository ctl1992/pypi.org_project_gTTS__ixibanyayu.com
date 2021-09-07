import requests

response = requests.get(
    "https://ipv4.webshare.io/",
    proxies={
        "http": "http://kloekkwo-rotate:2owwgq37eejp@p.webshare.io:80/",
        "https": "http://kloekkwo-rotate:2owwgq37eejp@p.webshare.io:80/"
    }
).text

print(response)
