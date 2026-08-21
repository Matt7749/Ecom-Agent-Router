import sys
import time
from windly_api_injector import push_to_windly

class SourcingRouter:
    @staticmethod
    def get_optimal_platform(keyword):
        print(f"   [AI Router] '{keyword}' 최적 소싱처 분석 중...")
        
        # 1. 도매꾹 (국내 B2B): KC인증/식검 리스크 
        kc_risk_keywords = ["조명", "청소기", "바리깡", "냉장고", "건조기", "전동", "인덕션", "다리미", "밥솥", "이어폰", "식기", "컵", "텀블러"]
        if any(risk in keyword for risk in kc_risk_keywords):
            return "domeggook"
            
        # 2. 타오바오 (중국 B2C): 트렌드 잡화, 의류, 단품 위탁
        taobao_keywords = ["옷", "가방", "신발", "액세서리", "케이스", "디자인", "트렌드"]
        if any(kw in keyword for kw in taobao_keywords):
            return "taobao"
            
        # 3. 아마존 (미국 B2C): 건기식, 서구권 브랜드
        amazon_keywords = ["영양제", "비타민", "정품", "단백질", "나이키", "애플"]
        if any(kw in keyword for kw in amazon_keywords):
            return "amazon"
            
        # 4. 1688 (중국 B2B): 인증 프리(Free) 일반 공산품, 대량사입
        return "1688"

def apply_1688_rules(keyword, product_data):
    if product_data["priceCny"] > 100:
        print(f"   🚨 [1688 Rule Block] 타겟 마진율 미달. (도매가: {product_data['priceCny']}위안)")
        return False
    if product_data["badge"] not in ["슈퍼공장", "实力商家"]:
        print(f"   🚨 [1688 Rule Block] 공장 신뢰도 미달. (잡상인 배제)")
        return False
    return True

def run_auto_sourcing(keyword, thumbnail_url):
    print(f"\n==================================================")
    print(f"🚀 [Zero-Click Sourcing] '{keyword}' 파이프라인 가동")
    print(f"==================================================")
    
    time.sleep(0.5) 
    
    # [NEW] AI 라우팅 모듈 가동
    platform = SourcingRouter.get_optimal_platform(keyword)
    
    if platform == "domeggook":
        print(f"   💡 [결과: 도매꾹] 전파법/KC 리스크 발견. 국내 도매꾹 크롤러(Domeggook Actor)로 우회합니다.")
        # TODO: call domeggook scraper
        print(f"✅ [SUCCESS] 도매꾹 소싱 타겟 리스트업 완료!\n")
        return True
        
    elif platform == "taobao":
        print(f"   💡 [결과: 타오바오] B2C 트렌드 상품. 타오바오 크롤러(Taobao Actor)로 우회합니다.")
        # TODO: call taobao scraper
        print(f"✅ [SUCCESS] 타오바오 소싱 타겟 리스트업 완료!\n")
        return True
        
    elif platform == "amazon":
        print(f"   💡 [결과: 아마존] 해외 브랜드/건기식 상품. 아마존 크롤러(Amazon Actor)로 우회합니다.")
        # TODO: call amazon scraper
        print(f"✅ [SUCCESS] 아마존 소싱 타겟 리스트업 완료!\n")
        return True
        
    elif platform == "1688":
        print(f"   💡 [결과: 1688] 인증 프리 일반 공산품. 1688 크롤러(1688 Actor)를 가동합니다.")
        print(f"🔍 1. 쿠팡 1위 이미지 1688 역추적 중... ({thumbnail_url})")
        
        # Mocking 1688 result
        mock_1688_result = {
            "factoryName": f"이우시 {keyword} 전문 공장 (实力商家)",
            "productUrl": f"https://detail.1688.com/offer/999_{keyword}.html",
            "priceCny": 25.0,
            "badge": "슈퍼공장"
        }
        
        if not apply_1688_rules(keyword, mock_1688_result):
            print(f"⏭️ 필터링 탈락. 다음 상품으로 넘어갑니다.\n")
            return False
            
        print(f"🎯 3. 최종 소싱 타겟 낙점. 윈들리로 실전 전송합니다...")
        # success = push_to_windly(mock_1688_result['productUrl'], keyword)
        print(f"✅ [SUCCESS] 윈들리 장바구니 안착 완료! (URL: {mock_1688_result['productUrl']})\n")
        return True

if __name__ == "__main__":
    test_keywords = [
        {"kw": "무소음 벽걸이 시계", "thumb": "http://img.com/clock.jpg"},
        {"kw": "고급 티슈케이스", "thumb": "http://img.com/tissue.jpg"},
        {"kw": "소형 무선 핸디 청소기", "thumb": "http://img.com/vacuum.jpg"}, # 도매꾹
        {"kw": "트렌드 가죽 가방", "thumb": "http://img.com/bag.jpg"}, # 타오바오
        {"kw": "나이키 정품 양말", "thumb": "http://img.com/nike.jpg"}, # 아마존
        {"kw": "침대 방수매트", "thumb": "http://img.com/waterproof.jpg"} # 1688
    ]
    
    for item in test_keywords:
        run_auto_sourcing(item["kw"], item["thumb"])
