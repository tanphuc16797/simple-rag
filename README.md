---

# RAG Python

Dự án mẫu triển khai **Retrieval-Augmented Generation (RAG)** bằng Python.

---

## Cài đặt

1. Cài các thư viện cần thiết:

   ```bash
   pip install -r scripts/requirements.txt
   ```

2. Chạy chương trình:

   ```bash
   cd src && python src/console.py
   ```

---

## Sử dụng

* Sau khi chạy, nhập câu hỏi trực tiếp vào **console**.
* Hệ thống sẽ tự động truy xuất thông tin liên quan và sinh câu trả lời dựa trên dữ liệu có sẵn.

---

## Cấu trúc đơn giản

```
.
├── requirements.txt
├── src/
│   ├── console.py       # Giao diện dòng lệnh
│   ├── ...              # Các module xử lý
│   └── .env             # Các biến môi trường
└── README.md
```

---

## Ghi chú

* Nên tạo môi trường ảo trước khi cài đặt:

  ```bash
  python -m venv venv
  source venv/bin/activate   # hoặc venv\Scripts\activate trên Windows
  ```
* Yêu cầu Python 3.9+.

---
