# 🚀 Ecom-Agent-Router (윈들리 AI 상품 가공 조수)

> **"엑셀만 넣으면 월 1억 셀러 MD가 상품명, 태그, 상세설명을 알아서 뚝딱 고쳐주는 셀러 전용 AI 자동화 도구"**

[**English Guide**](./README.md) | [**쉽게 배우는 한국어 가이드**](./README_KR.md)

---

## 💡 이 도구는 무엇인가요?
---

## 🔄 5단계 마스터 셀러 프로세스 (Master Workflow)

이 프로젝트는 프로셀러의 실전 판매 루틴을 5단계 완벽 자동화 파이프라인으로 구현했습니다.

```text
[1단계] 대표님이 트렌드 키워드 전달 ("미니 에어프라이어" 등)
   ↓
[2단계] Apify 연동으로 네이버/쿠팡 상위 1% 경쟁사 데이터 실시간 자동 크롤링
   ↓
[3단계] AI (@competitor-analyzer) 가 경쟁사 약점/가격/키워드 '1차 분석 리포트' 제공
   ↓
[4단계] 대표님이 소싱한 윈들리 원본 엑셀을 input/ 폴더에 전달
   ↓
[5단계] AI (@product-customizer) 가 경쟁사 약점을 역공격하는 최종 업로드용 엑셀 (output/final_upload_products.csv) 짠! 자동 출간
```

### 📋 5단계 세부 동작표

| 단계 | 주체 | 동작 및 전달 내용 | 결과물 |
| :---: | :---: | :--- | :--- |
| **1단계** | **셀러** | 트렌드 키워드 리스트 전달 | 키워드 접수 |
| **2단계** | **Apify 연동** | 네이버/쿠팡 200여 개 상품 실시간 크롤링 | `input/apify_naver_dataset.json` |
| **3단계** | **AI 브리핑** | **1차 경쟁사 분석 리포트 제공**<br>*(경쟁사 약점, 상위 소구점, 틈새 키워드)* | `output/competitor_analysis_20_keywords.md` |
| **4단계** | **셀러** | 윈들리 소싱 원본 엑셀 전달 | `input/` 폴더 저장 |
| **5단계** | **AI 가공** | **경쟁사 약점 역공격 최종 엑셀** 생성 | `output/final_upload_products.csv` |


윈들리(Windly)나 도매 사이트에서 가져온 해외 상품 데이터는 **상품명이 어색하고, 상표권 위험 단어가 섞여 있으며, 그대로 올리면 안 팔립니다.**

이 도구를 사용하면 AI가 **인기 카테고리별 1등 전문 MD(상품기획자)**로 변신하여, 네이버 쇼핑과 쿠팡에서 검색이 잘 되고 잘 팔리는 프로셀러 수준의 상품으로 **3초 만에 자동으로 재작성**해 줍니다!

---

## 🤖 지원 가능한 AI 도구 & 연결 방법 상세 안내

이 프로젝트는 다양한 AI 도구에서 활용할 수 있습니다. 본인이 사용 중인 AI 도구를 선택하여 연결해 보세요.

| 연동 도구 | 적용 난이도 | 추천도 | 연결 및 사용 방법 요약 |
| :--- | :---: | :---: | :--- |
| **Antigravity / Claude Code** | 초간단 (1초) | ⭐⭐⭐⭐⭐ | 폴더 열기 ➔ `@product-customizer input 폴더 가공해줘` 입력 |
| **Cursor AI / VS Code** | 간단 (10초) | ⭐⭐⭐⭐⭐ | Cursor에서 폴더 열기 ➔ Chat창에서 `.agents/` 지침 참조하여 가공 |
| **ChatGPT (Custom GPTs)** | 쉬움 (1분) | ⭐⭐⭐⭐☆ | Custom GPTs에 `pro-seller-product-rules.md` 지침 복사 등록 |
| **Claude 웹 / ChatGPT 일반** | 쉬움 (30초) | ⭐⭐⭐☆☆ | `pro-seller-product-rules.md` 텍스트 복사 ➔ 채팅창에 붙여넣기 |
| **개발자 파이썬 CLI** | 개발자용 | ⭐⭐⭐⭐⭐ | `pip install -e .` ➔ `ecom-agent run` 명령어 실행 |

---

### 1. Antigravity / Claude Code 연결 방법 (가장 편리)
1. Antigravity 또는 Claude Code에서 다운로드한 `Windly-Product-Custom` 폴더를 워크스페이스로 엽니다.
2. `input/` 폴더에 윈들리 엑셀 파일을 저장합니다.
3. 채팅창에 아래 문장을 그대로 입력합니다:
   ```text
   @product-customizer input 폴더 엑셀 가공해줘.
   ```
   *(AI가 `.agents/agents/product-customizer.md` 지침을 자동으로 인지하여 가공합니다.)*

---

### 2. ChatGPT (Plus/Team) - 나만의 'Custom GPT'로 만들기
매번 프롬프트를 복사할 필요 없이 챗GPT에 나만의 전용 툴로 등록하는 방법입니다.

1. 챗GPT 웹사이트([chatgpt.com](https://chatgpt.com)) 접속 ➔ 왼쪽 메뉴의 **Explore GPTs** ➔ 오른쪽 상단 **+ Create** 클릭
2. **Configure** 탭 클릭 후 설정:
   - **Name:** 윈들리 1등 셀러 MD
   - **Instructions:** 프로젝트에 있는 `pro-seller-product-rules.md` 파일의 전체 내용을 복사해서 붙여넣기
3. **Save**를 누르면 끝! 이제 챗GPT에 엑셀 파일만 올려주면 자동으로 1등 셀러 수준으로 가공해 줍니다.

---

### 3. Cursor AI / VS Code (Continue, Cline, Roo Code) 연결 방법
1. Cursor AI 또는 VS Code에서 `Windly-Product-Custom` 폴더를 엽니다.
2. AI 대화창(Ctrl+L 또는 Cmd+L)을 열고 아래와 같이 요청합니다:
   ```text
   .agents/rules/pro-seller-product-rules.md 지침을 참조해서 input/ 폴더의 상품 엑셀을 가공해줘.
   ```

---

### 4. Claude 웹사이트 (claude.ai) / ChatGPT 대화창에 직접 쓰기
1. 프로젝트 폴더의 `pro-seller-product-rules.md` 파일을 메모장으로 엽니다.
2. 전체 내용을 복사하여 챗GPT나 Claude 대화창 상단에 붙여넣습니다.
3. 이어서 가공할 상품명이나 엑셀 텍스트를 붙여넣고 *"이 규칙대로 가공해줘"* 라고 하면 즉시 가공됩니다.

---

### 5. 개발자용 파이썬 CLI 명령어 사용
개발자나 자동화 스크립트를 쓰시는 분들은 명령창에서 한 줄로 실행할 수 있습니다:

```bash
# 패키지 설치
pip install -e .

# input 폴더 데이터 일괄 가공
ecom-agent run --input ./input --output ./output
```

---

## 🔥 3가지 핵심 자랑거리

1. **🎭 카테고리별 AI MD 페르소나 자동 스위칭**: 미니가전, 패션, 테크, 펫용품 등 카테고리에 맞는 7년차 베테랑 MD의 화법과 소구점으로 자동 변신합니다.
2. **🕵️‍♂️ 경쟁사 불만/약점 역공격**: 쿠팡/네이버 상위 1등 경쟁사의 고객 불만 리뷰를 파악하여 우리 상품의 강점으로 강조합니다.
3. **🛡️ 상표권 & 금지어 100% 안심 정제**: 샤오미, 애플 등 타사 브랜드 무단 도용 및 과대광고 표현을 100% 자동 교정합니다.

---

## 📄 라이선스

본 프로젝트는 누구나 자유롭게 수정하고 활용할 수 있는 **MIT License** 하에 제공됩니다.


---

## 🚧 로드맵 & 개발 중인 기능 (In Development)

- [ ] **[Step 0] AI 자동 트렌드 키워드 자동 추출 & 제안 엔진 (개발 중 / Coming Soon 🚀)**:
  - 셀러가 키워드를 직접 찾지 않아도, AI가 실시간 급상승/시즌별 블루오션 키워드 Top 10을 자동 분석하여 먼저 추천해 주는 기능.
- [ ] **[차세대 소싱 엔진] 경쟁사 1등 상품 1:1 동일·유사 상품 AI 자동 소싱 (개발 예정 / Next-Gen 🌟)**:
  - 윈들리에 의존하지 않고, 알리/타오바오/1688 등 도매몰에서 경쟁사 상위 노출 상품과 가장 동일/유사한 상품을 AI 이미지 픽셀 및 스펙 매칭으로 직접 자동 소싱해 주는 독립형 기능.


---

## 🔑 Apify API 무료 토큰 발급 방법 (1분 완료)

경쟁사 상품 데이터(네이버 쇼핑/쿠팡)를 실시간 크롤링하기 위해 Apify 무료 API 토큰이 필요합니다.

1. **[Apify 웹사이트](https://apify.com/) 접속 및 무료 회원가입** (Google 계정 간편 가입 가능)
2. 로그인 후 오른쪽 상단 프로필 클릭 ➔ **Settings** ➔ **Integrations** 탭 선택
3. **API Tokens** 항목에서 **Personal API Token** 복사 (`apify_api_...`)
4. 프로젝트 폴더의 `.env.example` 파일을 복사하여 `.env` 파일을 만들고 토큰을 입력합니다:
   ```ini
   APIFY_API_TOKEN=your_apify_api_token_here
   ```
> ⚠️ **보안 주의**: `.env` 파일은 `.gitignore`에 자동 등록되어 있어 개인 API 토큰이 GitHub에 절대로 노출되지 않습니다.


---


---

## 🚀 [초특급 기능] AI 자율주행 모드 (Apify MCP 연동)

Claude Desktop이나 Cursor 편집기에 **Apify MCP Server**를 연동하면, 웹사이트 접속 없이 **채팅창 명령어 한 줄**로 AI가 스스로 크롤링부터 엑셀 생성까지 논스톱으로 수행합니다! (Zero-Click 자동화)

### ⚙️ 연동 방법 (Claude Desktop / Cursor)

1. PC에 [Node.js](https://nodejs.org/)가 설치되어 있어야 합니다.
2. 프로젝트에 제공된 `mcp_config_template.json`의 내용을 복사합니다.
3. 본인의 `APIFY_TOKEN`을 입력합니다.
4. 아래 경로의 설정 파일에 붙여넣고 AI 도구를 재시작하세요:
   - **Claude Desktop (Windows)**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Claude Desktop (Mac)**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Cursor**: `Cursor Settings ➔ Features ➔ MCP ➔ Add New (Type: command, Command: npx -y @apify/mcp-server)`
   - **Antigravity**: `C:\Users\<User>\.gemini\config\mcp_config.json` 파일에 설정 내용 붙여넣기

### 💬 실제 사용 명령어 예시
> *"AI야, Apify MCP를 사용해서 쿠팡(Coupang Scraper)에서 '미니 에어프라이어' 상위 20개 데이터를 긁어와 줘. 그 다음 수집된 데이터를 바탕으로 경쟁사 약점 리포트와 최종 마켓 업로드 엑셀(final_upload_products.csv)을 만들어줘!"*

## 🛒 Apify에서 네이버 쇼핑 & 쿠팡 검색 등록하는 방법 (초간단 4단계)

Apify 콘솔에서 원하는 경쟁사 키워드(예: *미니 에어프라이어*, *1인 전기밥솥*)를 등록하고 크롤링하는 방법입니다.

### 1단계: Apify Store에서 스크래퍼 검색
- [Apify Store](https://apify.com/store)에 접속합니다.
- 상단 검색창에 **`naver shopping`** 또는 **`coupang`**을 입력합니다.

### 2단계: 스크래퍼(Actor) 선택
- **네이버 쇼핑:** `Naver Shopping Product Scraper` 선택
- **쿠팡:** `Coupang Scraper` 선택

### 3단계: 검색어 (Input) 입력 설정
- **`searchKeywords`** 또는 **`queries`** 란에 조사하고 싶은 키워드를 입력합니다.
  - 예시: `미니 에어프라이어`, `1인 전기밥솥`, `핸디 무선청소기`
- **`maxItems`**: 수집할 상품 개수를 설정합니다 (예: 50~100개 권장).

### 4단계: `Start / Run` 버튼 클릭!
- 오른쪽 하단 **`Start`** (또는 **`Run`**) 버튼을 누르면 끝!
- 몇 초 뒤 크롤링이 완료되며, 수집 데이터가 프로젝트의 `input/` 폴더로 자동 연동됩니다.
