# Zara Sales Floor Report — Static Dashboard

Dashboard tĩnh (thuần HTML/CSS/JS, không cần Python/Streamlit/backend) dựng lại từ
`EDA_Zara_Sales_Analysis.ipynb`, dữ liệu lấy từ `Zara_sales_EDA.csv` (20,252 sản phẩm).

## Cấu trúc

```
index.html              # toàn bộ giao diện + logic xử lý dữ liệu (vanilla JS)
data.json                # dữ liệu đã làm sạch & nén (~526 KB, dạng columnar + encoded categories)
vendor/chart.umd.min.js  # Chart.js đóng gói sẵn trong repo (không phụ thuộc CDN ngoài)
vercel.json              # cấu hình headers/caching cho Vercel
```

> **Lưu ý quan trọng**: phải deploy **đủ cả 4 mục trên ở cùng một cấp thư mục** (cùng root,
> kể cả thư mục con `vendor/`). Nếu thiếu `vendor/chart.umd.min.js` hoặc `data.json`, trang sẽ
> kẹt ở màn hình loading và Console sẽ báo lỗi `Chart is not defined` hoặc fetch `data.json` lỗi 404.
> Bản đầu tiên từng dùng CDN ngoài (`cdnjs.cloudflare.com`) cho Chart.js — đã đổi sang host nội bộ
> trong `vendor/` vì CDN có thể bị chặn bởi mạng/ad-blocker của một số người dùng, gây đúng lỗi
> "có giao diện nhưng biểu đồ không hiện, kẹt ở màn hình loading".

## Deploy lên Vercel

### Cách 1 — Vercel CLI (nhanh nhất)
```bash
npm i -g vercel        # nếu chưa có
cd zara-dashboard
vercel                 # làm theo hướng dẫn, chọn "Other" framework preset
vercel --prod           # deploy bản chính thức
```

### Cách 2 — Kéo thả trên vercel.com
1. Vào https://vercel.com/new
2. Chọn "Deploy" → kéo thả cả thư mục `zara-dashboard` (chứa index.html, data.json, vendor/, vercel.json) vào
3. Framework Preset chọn **Other** (không cần build command, không cần install command)
4. Bấm Deploy

### Cách 3 — Qua GitHub
1. Push **toàn bộ** thư mục này (bao gồm cả thư mục con `vendor/`) lên một repo GitHub,
   đảm bảo `index.html` nằm ở **root** của repo (không lồng trong thư mục con khác)
2. Vào vercel.com → Add New Project → Import repo đó
3. Framework Preset: **Other**, Build Command: để trống, Output Directory: để trống (root)
4. Deploy

Không cần biến môi trường, không cần build step — đây là site tĩnh thuần.

### Nếu đã deploy mà trang kẹt ở loading / biểu đồ không hiện

Đây gần như luôn là do thiếu file khi push lên GitHub. Cách kiểm tra nhanh:
1. Mở `https://<tên-app>.vercel.app/data.json` trực tiếp trên trình duyệt — phải thấy JSON, không phải 404
2. Mở `https://<tên-app>.vercel.app/vendor/chart.umd.min.js` trực tiếp — phải thấy code JS, không phải 404
3. Nếu cái nào 404 → file đó chưa có trong repo GitHub hoặc nằm sai vị trí thư mục → push lại file đó vào đúng root/vendor

## Những gì dashboard thể hiện (bám theo notebook gốc)

- **KPI tổng quan**: tổng SKU, giá TB, sản lượng TB, tỉ lệ khuyến mãi — cập nhật theo bộ lọc
- **Phân bố 1 chiều**: histogram giá & sản lượng, tỉ lệ khuyến mãi/theo mùa/phân khúc giá
- **Vị trí trưng bày** (Aisle / End-cap / Front of Store) dạng sơ đồ mặt bằng cửa hàng — vùng càng đỏ đậm sản lượng càng cao
- **Tác động khuyến mãi & mùa vụ**: so sánh sản lượng trung bình có/không khuyến mãi, theo mùa/quanh năm
- **Giá vs sản lượng**: scatter plot + đồng hồ đo hệ số tương quan Pearson (r ≈ −0.34, đúng số liệu từ notebook)
- **Phân tích theo giới tính / mùa / chất liệu**
- **Top 10 sản phẩm bán chạy nhất** theo bộ lọc hiện tại

Bộ lọc (khuyến mãi, theo mùa, giới tính, mùa, phân khúc giá) chạy hoàn toàn phía client —
mọi biểu đồ và KPI tính lại tức thời khi đổi bộ lọc, không cần gọi server.

## Tuỳ biến / cập nhật dữ liệu

Nếu muốn thay dữ liệu mới, chạy lại đoạn script Python sau (cùng logic làm sạch như
notebook: dedup, bins giá 0-30-70-150-1000, mã hoá category) để sinh `data.json` mới,
rồi thay file là xong — không cần sửa `index.html`.
