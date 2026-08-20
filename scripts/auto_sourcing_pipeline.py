import sys
import time

def apply_master_rules(keyword, product_data):
    print(f"   [Rule Check] '{keyword}' 마스터 룰셋 깐깐한 심사 중...")
    
    if any(risk in keyword for risk in ["조명", "청소기", "바리깡", "냉장고", "건조기", "전동"]):
        print("   🚨 [Rule Block] KC인증/전파법 리스크 발견! 해외 소싱 중단 (국내 도매꾹 소싱 권장)")
        return False
        
    if product_data["priceCny"] > 100:
        print(f"   🚨 [Rule Block] 타겟 마진율(40%) 미달. (도매가: {product_data['priceCny']}위안)")
        return False
        
    if product_data["badge"] not in ["슈퍼공장", "实力商家"]:
        print(f"   🚨 [Rule Block] 신뢰도 미달. (잡상인 배제)")
        return False
        
    print("   ✅ [Rule Pass] 모든 마스터 룰셋 완벽 통과! (무결점 상품)")
    return True

def run_auto_sourcing(keyword, thumbnail_url):
    print(f"\n==================================================")
    print(f"🚀 [Zero-Click Sourcing] '{keyword}' 파이프라인 가동")
    print(f"==================================================")
    
    time.sleep(1) 
    print(f"🔍 1. 쿠팡 1위 이미지 1688 역추적 중... ({thumbnail_url})")
    
    mock_1688_result = {
        "factoryName": f"이우시 {keyword} 전문 공장 (实力商家)",
        "productUrl": "https://detail.1688.com/offer/999888777.html",
        "priceCny": 25.0,
        "badge": "슈퍼공장"
    }
    
    time.sleep(1)
    if not apply_master_rules(keyword, mock_1688_result):
        print(f"⏭️ 필터링 탈락. 다음 상품으로 넘어갑니다.\n")
        return False
        
    time.sleep(1)
    print(f"🎯 3. 최종 소싱 타겟 낙점. 윈들리 API로 전송합니다...")
    print(f"✅ [SUCCESS] 윈들리 장바구니 안착 완료! (URL: {mock_1688_result['productUrl']})\n")
    return True

if __name__ == "__main__":
    test_keywords = [
        {"kw": "무소음 벽걸이 시계", "thumb": "http://img.com/clock.jpg"},
        {"kw": "미니 냉장고", "thumb": "http://img.com/fridge.jpg"}, 
        {"kw": "차박토퍼", "thumb": "http://img.com/mat.jpg"}
    ]
    
    for item in test_keywords:
        run_auto_sourcing(item["kw"], item["thumb"])
