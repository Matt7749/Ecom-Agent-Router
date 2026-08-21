import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import os
TOKEN = os.environ.get("APIFY_API_TOKEN", "")

items = [
    ("벽걸이 시계", "静音挂钟"),
    ("고급 티슈케이스", "高档纸巾盒"),
    ("간접 조명", "无线护眼氛围灯"),
    ("무선 핸디 청소기", "无刷电机手持吸尘器"),
    ("미니금고", "迷你保险箱 加厚"),
    ("이어폰/이어셋", "无痛佩戴蓝牙耳机"),
    ("바리깡", "静音理发器"),
    ("보온병", "大容量保温杯 316"),
    ("1구인덕션", "静音单眼电磁炉"),
    ("미니밥솥", "迷你电饭煲 立体加热"),
    ("차량용 냉장고", "车载冰箱 静音压缩机"),
    ("여행용 스팀다리미", "便携式挂烫机 防漏水"),
    ("방수매트", "防水床垫 静音"),
    ("차박토퍼", "车载床垫 折叠"),
    ("농업용 방충망/비닐", "农业防虫网 加厚"),
    ("강아지 유모차", "宠物推车 一键折叠 避震"),
    ("좌욕기", "坐浴盆 加厚硅胶"),
    ("강아지 구명조끼", "宠物救生衣 高浮力"),
    ("에어컨실외기 덮개", "空调外机罩 磁吸"),
    ("전동그라인더", "电动咖啡豆研磨机 可拆洗"),
    ("식품건조기", "食品烘干机 静音 定时"),
    ("파크골프채", "公园高尔夫球杆 防滑"),
    ("스텝퍼", "静音踏步机 液压")
]

def run_scraper(item):
    kr, zh = item
    payload = {
        "keywords": [zh],
        "maxItems": 1
    }
    
    run_url = f"https://api.apify.com/v2/acts/ghXSMZcW3GxsCrkiR/runs?token={TOKEN}"
    try:
        resp = requests.post(run_url, json=payload).json()
        run_id = resp['data']['id']
        dataset_id = resp['data']['defaultDatasetId']
        
        while True:
            status = requests.get(f"https://api.apify.com/v2/actor-runs/{run_id}?token={TOKEN}").json()['data']['status']
            if status in ['SUCCEEDED', 'FAILED', 'ABORTED']: 
                break
            time.sleep(3)
        
        items_resp = requests.get(f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={TOKEN}").json()
        for res in items_resp:
            url = res.get('detailUrl') or res.get('url') or res.get('productUrl')
            title = res.get('title', '').replace(',', ' ')
            if url:
                return f"{url},{kr},{title}\n"
    except Exception as e:
        print(f"Error on {kr}: {e}")
        return ""
    
    return ""

results = []
print("Starting 23 parallel Apify runs...")
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(run_scraper, item) for item in items]
    for future in as_completed(futures):
        res = future.result()
        if res:
            results.append(res)
            print(f"Got result: {res.strip()}")

with open('windly_final_upload.csv', 'w', encoding='utf-8') as f:
    f.write("상품 URL,타겟 키워드,1688 상품명\n")
    for r in results:
        f.write(r)

print("All done! Created windly_final_upload.csv")

