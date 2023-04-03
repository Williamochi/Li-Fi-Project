# 點擊下方圖片觀看 Li-Fi 傳輸操作過程完整影片
[![IMAGE ALT TEXT](https://github.com/Williamochi/project/blob/main/LiFipicture.png)](https://youtu.be/08VAHlQcgLw "Li-Fi 傳輸操作過程完整影片")
(Li-Fi 傳輸平台執行運作過程展示在此連結：https://youtu.be/bG3SWu7AGBg)
## 操作流程
1. 首先開啟傳送端的程式介面程式，點擊open選取欲傳輸圖片，原始圖片呈現在介面左方。
2. 點擊 DCT，會在右方呈現原始圖片經由DCT轉換後的圖像，選擇Arduino上的COM點等待之後傳送終端與傳輸平台溝通。
3. 點擊 show 會在右方介面產生已壓縮圖像，選擇不同的 rho 值調整量化比例再點擊show，能夠呈現出對應圖像。
4. 另外若點擊介面左方或是右方圖片，下方的三個方格會呈現該點擊位置之8x8區域，分別是原圖、DCT圖像以及已壓縮圖像。
5. 先點擊接收介面的 Start Receive 等待接收，再點擊transmit進行資料傳送，接收端接收完資料並解碼後，接收終端彈出介面，呈現經過光傳輸後之圖像。
6. 點擊圖片也能查看該點擊位置之8x8區域，上方也能夠點擊save來儲存圖片。
