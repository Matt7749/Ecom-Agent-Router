# 🚀 Ecom-Agent-Router (Cross-Border E-Commerce AI Agent)

> **Autonomous AI Agent Framework optimized for Cross-Border Sourcing (Domeggook/1688/Taobao) ➔ Korea Domestic Selling (Naver SmartStore, Coupang)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Agent Skills Compliant](https://img.shields.io/badge/Agent_Skills-v1.0-green.svg)](https://agentskills.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[**English (Global)**](./README.md) | [**한국어 가이드**](./README_KR.md)

---

## 🌟 Key Global Features

- **🌐 Cross-Border Selling Optimization**: Specialized for sourcing from local wholesale (Domeggook) and global B2B platforms (1688, Taobao) via Windly, and generating optimized output CSVs strictly formatted for Korea's top domestic marketplaces (Naver Shopping, Coupang).
- **🎭 Dynamic MD Persona Switching**: Automatically routes items to specialized Merchandiser (MD) personas (e.g., *Korean Trend Style MD*, *Living & Tech Specialist MD*, *Pet Life MD*) based on category detection.
- **🕵️‍♂️ Global Competitor Intelligence**: Integrates with Apify REST API to scrape Amazon Bestsellers, Shopify catalog stores, AliExpress, and Coupang to extract high-converting Unique Selling Points (USPs).
- **🛡️ US/EU Brand & Compliance Shield**: Built-in regex and heuristic filters for Amazon Brand Registry & US/EU trademark protection (removes restricted brand keywords like Apple, Dyson, Xiaomi) and prevents false claim violations.
- **⚡ Scale-Proof Category Architecture**: Extend category-specific domain rules inside `.agents/rules/categories/` as simple Markdown modules without rewrites.
- **📊 Global Batch Export**: Formats raw supplier CSVs (Windly, 1688, Taobao, CJ Dropshipping) into Amazon Title (200 chars), 15 search keywords/tags, bullet points (USPs), and cleaned variant options into CSV & Markdown.

---

## 🔄 5-Step Master Seller Workflow

```text
[Step 1] Seller inputs global target keywords (e.g., "mini air fryer", "portable desk fan")
   ↓
[Step 2] Apify Scraper crawls top 1% Amazon / Shopify / Naver / Coupang competitor listings automatically
   ↓
[Step 3] AI (@competitor-analyzer) delivers Phase 1 Global Competitor Intelligence Report (Pain points, USPs, Tags)
   ↓
[Step 4] Seller places raw sourced supplier CSV (1688, Taobao, Windly) in ./input folder
   ↓
[Step 5] AI (@product-customizer) generates Final Marketplace Upload CSV (output/final_upload_products.csv) targeting competitor weaknesses!
```

---

## 🤖 Compatible AI Tools & Setup Guide

| AI Tool / Framework | Integration Difficulty | Recommended | How to Connect & Run |
| :--- | :---: | :---: | :--- |
| **Antigravity / Claude Code** | 1-Second | ⭐⭐⭐⭐⭐ | Open folder workspace ➔ Type `@product-customizer process input/` |
| **Cursor AI / VS Code** | 10-Seconds | ⭐⭐⭐⭐⭐ | Open folder ➔ Reference `.agents/` rules in Chat |
| **ChatGPT Custom GPTs** | 1-Minute | ⭐⭐⭐⭐☆ | Paste `pro-seller-product-rules.md` into Custom GPT Instructions |
| **Claude Web / ChatGPT** | 30-Seconds | ⭐⭐⭐☆☆ | Paste `pro-seller-product-rules.md` at top of chat prompt |
| **Python CLI SDK** | Developer | ⭐⭐⭐⭐⭐ | Run `pip install -e .` ➔ `ecom-agent run` |

---


---

## 🚀 [Killer Feature] Autonomous AI Mode (Apify MCP Server Integration)

By integrating the **Apify MCP Server** into Claude Desktop or Cursor, you can achieve **Zero-Click Automation**. The AI will autonomously run scrapers, fetch data, and generate final upload CSVs directly from your chat prompt!

### ⚙️ How to Connect (Claude Desktop / Cursor)

1. Ensure [Node.js](https://nodejs.org/) is installed on your system.
2. Copy the contents of the provided `mcp_config_template.json` file.
3. Replace `YOUR_APIFY_API_TOKEN_HERE` with your actual token.
4. Paste it into your AI tool's config file and restart:
   - **Claude Desktop (Windows)**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Claude Desktop (Mac)**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Cursor**: `Cursor Settings ➔ Features ➔ MCP ➔ Add New (Type: command, Command: npx -y @apify/mcp-server)`

### 💬 Example Autonomous Prompt
> *"AI, use the Apify MCP server to run the Coupang Scraper for 'mini air fryer' (max 20 items). Once done, analyze the data and generate the final marketplace upload CSV targeting their weaknesses!"*

## 🛒 Setting Up Amazon, Shopify & AliExpress Scraping on Apify

1. **Sign up at [Apify Store](https://apify.com/store)**.
2. **Search Global Scrapers**:
   - **Amazon:** `Amazon Product Scraper` or `Amazon Bestsellers Scraper`
   - **Shopify:** `Shopify Product Scraper`
   - **AliExpress / 1688:** `AliExpress Product Scraper`
   - **Korean Top Markets:** `Naver Shopping Product Scraper` / `Coupang Scraper`
3. **Configure Search Keywords / Store URLs** under `searchKeywords` or `startUrls`.
4. Click **`Start / Run`** ➔ Crawled datasets automatically download into your `./input/` folder.

---

## 🚧 Roadmap & Upcoming Features

- [ ] **[Step 0] Automated AI Trend Keyword Discovery Engine (In Development / Coming Soon 🚀)**:
  - Automatically mines and suggests seasonal/trending blue-ocean keywords Top 10 from Google Trends & Amazon Search Volume.
- [ ] **[Next-Gen Sourcing Engine] Direct Competitor Product Auto-Sourcing (Planned / Next-Gen 🌟)**:
  - Direct 1:1 identical and similar product auto-sourcing from Domeggook/1688/Taobao using AI computer vision & spec matching.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.
