# Review analysis

### Installing dependencies:
```bash
pip install -r requirements.txt
```
or
```bash
pip install fastapi uvicorn
```

### Launching the app:
```bash
uvicorn server.main:app --reload
```


## Query examples
### 1. Saving a review
#### 🟩 _Positive_ review
```bash
curl -X POST -d "Услуги оказали очень хорошо, буду рекомендовать знакомым!" http://localhost:8000/reviews
```

Response body: 
```json
{
  "id": 1,
  "text": "Услуги оказали очень хорошо, буду рекомендовать знакомым!",
  "sentiment": "positive",
  "created_at": "2025-07-16T14:27:22.546062+00:00"
}
```

<br>

#### 🟥 _Negative_ review
```bash
curl -X POST -d "Товар пришел плохо упакованным, очень расстроились, больше не будем так рисковать и заказывать тут :(" http://localhost:8000/reviews
```

Response body:
```json
{
  "id": 2,
  "text": "Товар пришел плохо упакованным, очень расстроились, больше не будем так рисковать и заказывать тут :(",
  "sentiment": "negative",
  "created_at": "2025-07-16T14:32:01.436840+00:00"
}
```

<br>

#### ⬜ _Neutral_ review
```bash
curl -X POST -d "В целом ничего не могу сказать, выглядит очень обычно." http://localhost:8000/reviews
```

Response body:
```json
{
  "id": 3,
  "text": "В целом ничего не могу сказать, выглядит очень обычно.",
  "sentiment": "neutral",
  "created_at": "2025-07-16T14:35:17.257017+00:00"
}
```

---

### 2. Getting reviews using a filter `sentiment`
#### 🟩 _Positive_ reviews
```bash
curl -X GET http://localhost:8000/reviews?sentiment=positive
```

Response body:
```json
[
  {
    "id": 1,
    "text": "Услуги оказали очень хорошо, буду рекомендовать знакомым!",
    "sentiment": "positive",
    "created_at": "2025-07-16T14:27:22.546062+00:00"
  }
]
```

<br>

#### 🟥 _Negative_ review
```bash
curl -X GET http://localhost:8000/reviews?sentiment=negative
```

Response body:
```json
[
  {
    "id": 2,
    "text": "Товар пришел плохо упакованным, очень расстроились, больше не будем так рисковать и заказывать тут :(",
    "sentiment": "negative",
    "created_at": "2025-07-16T14:32:01.436840+00:00"
  }
]
```

<br>

#### ⬜ _Neutral_ review
```bash
curl -X GET http://localhost:8000/reviews?sentiment=neutral
```

Response body:
```json
[
  {
    "id": 3,
    "text": "В целом ничего не могу сказать, выглядит очень обычно.",
    "sentiment": "neutral",
    "created_at": "2025-07-16T14:35:17.257017+00:00"
  }
]
```
