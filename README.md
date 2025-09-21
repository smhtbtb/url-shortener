# URL Shortener (FastAPI)

## Run (dev)
1. Create DB & env:
   ```bash
   cp .env.example .env
   ```

2. Install deps:
   ```bash
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Start server:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. Docs: http://localhost:8000/docs
---
## Run with Docker Compose

```bash
docker compose up --build
```
---
