# 🧩 FastAPI Modular App with File Storage

This project has two FastAPI services:

- **app-service**: Handles products and image associations.
- **storage-service**: Handles file uploads and serves them via URL.

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/mofalih64/presigned-url-File-storing-microservices.git
   cd presigned-url-File-storing-microservices
2. Setup environment

Inside each service (app-service/, storage-service/):

Copy .env.example to .env

you are now ready to run the project

3. Run the project
docker-compose up --build

4.🔗 API Docs
App Service: http://localhost:8000/docs#/

Storage Service: http://localhost:8001/docs#/

5.📝 Notes
---
A- File uploads are secured using signed tokens based on file metadata.

B-Uploaded files are stored locally and accessible via generated public URLs.

C-Image IDs are validated before associating with products.

D- each service has its own database.

