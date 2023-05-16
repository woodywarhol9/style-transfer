# Style Transfer Web App
- Basic ML Service using `FastAPI`, `Streamlit`

### Project Structure
---
``` bash
├── README.md
├── backend
│   ├── Dockerfile
│   ├── __init__.py
│   ├── config.py
│   ├── inference.py
│   ├── main.py
│   ├── models
│   ├── poetry.lock
│   └── pyproject.toml
├── docker-compose.yml
├── download_models.sh
├── frontend
│   ├── Dockerfile
│   ├── main.py
│   ├── poetry.lock
│   └── pyproject.toml
└── storage
    └── bdbc59f5-f695-4dee-9d78-86eb2a6061f3.jpg
```
### How to Run
---
**1. Download the models**
``` bash
sudo bash download_models.sh
```

</br>

**2. Build Service**
``` docker
docker compose up -d --build
```

</br>

**3. Run**
``` http
localhost:8501
```


![image](https://github.com/woodywarhol9/hydra-practice/assets/86637320/f07ee8f3-eaf1-4fee-a1e2-1ad382acee44)

---
**References**
- https://testdriven.io/blog/fastapi-streamlit/