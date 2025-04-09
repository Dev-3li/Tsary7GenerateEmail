# FastAPI Email Formatter

API بسيط يأخذ اسم ثلاثي ويرجعه بصيغة بريد إلكتروني مرتبة مثل:
`Ahmed_Ali_Hassan@mail.com`

## Endpoint

`POST /generate-email`

### Request Body

```json
{
  "name": "الاسم الثلاثي"
}
```

### Response

```json
{
  "email": "Formatted_Email@mail.com"
}
```