# 今天吃什麼？ The Daily Bite

把猶豫留給下一餐。一個以繁體中文製作的餐點抽選器，使用 HTML、CSS 與原生 JavaScript，所有程式都放在單一 `index.html`。

## 使用方式

下載 `index.html`，用 Chrome、Edge、Firefox 或 Safari 開啟即可使用。不需要安裝套件，也不需要 API 金鑰。

1. 選擇料理類型與預算，可另外勾選蔬食或只從收藏中抽選。
2. 按「幫我選一餐」，取得符合條件的餐點。
3. 按「收藏這道」保留喜歡的選項，或按「就吃這個」記錄這一餐。
4. 按「加一道私房餐點」，把自己的餐點加入名單。

## 功能

- 24 道內建餐點，包含台式、日韓、西式及輕食。
- 料理、預算、蔬食與收藏交叉篩選。
- 隨機抽選動畫；有多個選項時不會連續抽到同一道。
- 收藏、自訂餐點、最近 8 次選餐紀錄。
- localStorage 保存資料，重新整理後仍可保留。
- 響應式排版、鍵盤焦點樣式、動態減少模式與狀態提示。
- 零外部依賴；網頁唯一必要檔案是 `index.html`。

內建價格是示範估價，並非店家即時報價；蔬食的實際食材與湯底需自行確認。資料只保存在目前瀏覽器，直接開啟檔案時的儲存支援依瀏覽器而異。

## 作業檔案

| 檔案 | 用途 |
| --- | --- |
| `index.html` | 完整可操作的互動網頁 |
| `規格書.md` | 構想、使用流程、功能規則、技術與驗收標準 |
| `README.md` | 使用與發布說明 |

## GitHub Pages 上線步驟

1. 登入 GitHub，建立一個新的 **Public** 儲存庫，例如 `what-to-eat`。
2. 在儲存庫頁面使用 **Add file → Upload files**，將 `index.html` 上傳到根目錄並提交。規格書與本說明可一起上傳。
3. 打開儲存庫的 **Settings → Pages**。
4. 在 **Build and deployment → Source** 選擇 **Deploy from a branch**。
5. Branch 選 **main**，資料夾選 **/(root)**，按 **Save**。
6. 等待部署完成，開啟 Pages 頁面提供的網址；網站應能操作抽選與篩選。

儲存庫網址和網站網址不同：

- 儲存庫：`https://github.com/你的帳號/what-to-eat`
- 網站：`https://你的帳號.github.io/what-to-eat/`

要複製儲存庫網址，只要打開 GitHub 專案首頁，複製瀏覽器網址列即可。不要複製帳號設定頁面，也不要把 `index.html` 上傳到額外一層資料夾。

操作依據：[GitHub 官方建立網站教學](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)、[設定發布來源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 驗證紀錄

2026-10-16：已通過 JavaScript 語法與模擬 DOM 邏輯測試，範圍包括：

- 預算上限、交叉篩選、無符合項目與重設條件。
- 單一候選抽選、連續 20 次抽選不立即重複。
- 收藏、重新載入保存資料、自訂餐點新增與刪除。
- 空白名稱、重複名稱、不合法價格與使用者文字跳脫。
- 同次結果不重複記錄、最近紀錄上限 8 筆、清除紀錄。
- 無法儲存或原有資料損壞時的提示與降級處理。

本機瀏覽器預覽受環境與安全政策限制，因此尚未完成真實瀏覽器的桌機／手機視覺、動畫及鍵盤互動驗收。邏輯測試不等同於這些實際瀏覽器驗證。

## 課堂展示順序（約 1 分鐘）

1. 說明問題：每天想不到下一餐吃什麼。
2. 選「台式」、預算「NT$80 以內」，示範篩選數量改變。
3. 按抽選，介紹結果符合條件，並且可以收藏。
4. 按「就吃這個」，展示最近紀錄。
5. 新增一個自訂餐點，說明資料保存在瀏覽器。
6. 展示規格書與 GitHub Pages 網址，說明從構想到規格、程式實作與公開發布的流程。

