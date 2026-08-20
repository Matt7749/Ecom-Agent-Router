import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_1688_SEARCH_KEY")
IMAGE_SEARCH_API_URL = "https://api.thirdparty-1688.com/v1/image-search"

def reverse_image_search(image_url, keyword):
    """
    쿠팡/네이버 경쟁사 썸네일을 1688 API로 쏴서 원본 공장을 찾아내는 모듈
    """
    if not API_KEY:
        print("🚨 [ERROR] API_1688_SEARCH_KEY 가 설정되지 않았습니다. (테스트 모드로 동작합니다)")
    
    print(f"🔍 [Vision AI] '{keyword}' 경쟁사 이미지 1688 역추적 시작...")
    print(f"   - Target Image URL: {image_url}")
    
    try:
        # [MOCK DATA] API가 정상적으로 황소마크 공장을 찾아냈다고 가정
        mock_results = [
            {
                "factoryName": "이우시 미니멀 공장 (实力商家)",
                "productUrl": "https://detail.1688.com/offer/987654321.html",
                "priceCny": 15.5,
                "badge": "슈퍼공장",
                "matchRate": "98%"
            },
            {
                "factoryName": "광저우 잡화점",
                "productUrl": "https://detail.1688.com/offer/111111111.html",
                "priceCny": 12.0,
                "badge": "일반상인",
                "matchRate": "85%"
            }
        ]
        
        print("💡 1688 검색 완료! 최적의 공장을 필터링합니다.")
        
        # [로직] 가장 신뢰도(badge)가 높고 매칭율이 높은 곳을 1순위로 리턴
        best_match = None
        for item in mock_results:
            if item["badge"] in ["슈퍼공장", "实力商家"] and float(item["matchRate"].strip("%")) > 95:
                best_match = item
                break
        
        if not best_match:
            best_match = mock_results[0]
            
        print(f"🎯 [최종 소싱 타겟 낙점] 공장명: {best_match['factoryName']} | 도매가: {best_match['priceCny']}위안")
        return best_match["productUrl"]

    except Exception as e:
        print(f"❌ [FAIL] 1688 이미지 검색 실패: {e}")
        return None

if __name__ == "__main__":
    test_thumb = "https://coupang.com/test-thumbnail-wallclock.jpg"
    found_url = reverse_image_search(test_thumb, "무소음 벽걸이 시계")
    print(f"Result URL: {found_url}")
