from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

class NameRequest(BaseModel):
    name: str

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key="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"
)

@app.post("/generate-email")
def generate_email(req: NameRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f'''اكتب لي الإيميل بالصيغة التالية فقط:
الاسم الأول_الاسم الثاني_الاسم الثالث@mail.com
بشرط أن يكون أول حرف من كل اسم كبير (Capital) والباقي صغير (Small)، دون أي إضافات أو شرح.

الآن حول:
{req.name}
                    '''
                }
            ],
            temperature=0.5,
            max_tokens=100,
            top_p=1
        )
        return {"email": response.choices[0].message.content.strip()}
    except Exception as e:
        return {"error": str(e)}
