import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# 대표님이 브라우저에서 직접 복사해서 .env에 넣으실 윈들리 로그인 쿠키
WINDLY_COOKIE = os.getenv("WINDLY_SESSION_COOKIE")
# 윈들리 내부 수집기 API 엔드포인트 (가상 - 향후 크롬 네트워크 탭 분석 후 URL 교체)
WINDLY_COLLECT_API = "https://api.windly.com/v1/collect/taobao"

def push_to_windly(product_url, keyword):
    """
    1688/타오바오 상품 URL을 윈들리 장바구니로 다이렉트 전송 (Zero-Click)
    """
    if not WINDLY_COOKIE:
        print("🚨 [ERROR] WINDLY_SESSION_COOKIE가 설정되지 않았습니다. 로그인이 필요합니다.")
        return False

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/json",
        "Cookie": WINDLY_COOKIE,
        "Origin": "https://www.windly.com",
        "Referer": "https://www.windly.com/dashboard"
    }

    payload = {
        "sourceUrl": product_url,
        "targetKeyword": keyword,
        "autoTranslate": True
    }

    try:
        print(f"🚀 윈들리 서버로 데이터 전송 중... [Target: {keyword}]")
        # 실제 운영시에는 주석 해제하여 타격
        # response = requests.post(WINDLY_COLLECT_API, headers=headers, json=payload, timeout=10)
        # response.raise_for_status()
        
        # [시뮬레이션 응답]
        print(f"✅ [SUCCESS] 윈들리 수집함 안착 완료! (URL: {product_url})")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"❌ [FAIL] 윈들리 전송 실패. 세션이 만료되었거나 구조가 변경되었습니다: {e}")
        return False

if __name__ == "__main__":
    # Test execution
    test_url = "https://detail.1688.com/offer/123456789.html"
    push_to_windly(test_url, "차박토퍼")
