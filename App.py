import requests,json
import pandas as pd
userName = []
title =  []
review = []
rating = []
date = []

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNSRjVITkJHUFEifQ.eyJpc3MiOiI4Q1UyNk1LTFM0IiwiaWF0IjoxNzEzMzY5MDc0LCJleHAiOjE3MjA2MjY2NzQsInJvb3RfaHR0cHNfb3JpZ2luIjpbImFwcGxlLmNvbSJdfQ.n3Qn-2LZW7iy-X79yHU7f41K05iTBuN3ycm_Bqp_nqHpaMyLKCG-zpiuBkVExYMj7YtJShSIxaFLJTvFB6vATA',
    'dnt': '1',
    'origin': 'https://podcasts.apple.com',
    'priority': 'u=1, i',
    'referer': 'https://podcasts.apple.com/',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}
for i in range(0,220,10):

    params = {
        'l': 'en-US',
        'offset': str(i),
    }

    response = requests.get(
        'https://amp-api.podcasts.apple.com/v1/catalog/us/podcasts/1344850656/reviews',
        params=params,
        headers=headers,
    )

    data = response.json()
    reviews = data.get("data")
    for i in reviews:
        item = i.get("attributes")
        userName.append(item['userName'])
        title.append(item['title'])
        review.append(item['review'])
        rating.append(item['rating'])
        date.append(item['date'])

data = {
    "Name": userName,
    "Title": title,
    "Review": review,
    "Rating": rating,
    "Date": date
}
df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False, sheet_name='Sheet1')