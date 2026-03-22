from openai import OpenAI

client = OpenAI(api_key="SUA_API_KEY_AQUI")

def recomendar_com_ia(preferencias, racas):
    prompt = f"""
    Usuário quer um cachorro com essas características:
    {preferencias}

    Escolha as melhores raças da lista abaixo e explique de forma simples:
    {racas}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
