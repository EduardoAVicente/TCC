import openai

# Substitua pela sua chave da API
openai.api_key = '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'

def gerar_resposta(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # 40.000 TPM
        # model="text-embedding-3-small", # 150.000 TPM
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()

# Exemplo de uso
prompt = "Explique como funciona a API do OpenAI em Python."

try:
    resposta = gerar_resposta(prompt)
    print(resposta)
except openai.error.OpenAIError as e:
    print(f"Erro na API: {e}")
