import requests

cookies = {
    "session": "53616c7465645f5f78b40da452e714654c2ea94b98cbdc8aa3f16412fd3a08452883dc40fdaa72aad83faa6887a296918f25d123123fe0a3e4fad3db87858aa4",
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-GB,en;q=0.5",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    # 'cookie': 'session=53616c7465645f5f78b40da452e714654c2ea94b98cbdc8aa3f16412fd3a08452883dc40fdaa72aad83faa6887a296918f25d123123fe0a3e4fad3db87858aa4',
}

response = requests.get(
    "https://adventofcode.com/2015/day/3/input", cookies=cookies, headers=headers
)


headers = {
    "sec-ch-ua-platform": '"macOS"',
    "Referer": "https://adventofcode.com/2015/day/3/input",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
}

response = requests.get("https://adventofcode.com/favicon.ico", headers=headers)
