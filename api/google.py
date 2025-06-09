from google import genai

def change_cooking_setp(recipe_data, api_key :str, servings: int) -> str:
    client = genai.Client(api_key=api_key)

    prompt = f"""
    내가 지금부터 레시피를 줄게
    음식 이름 : {recipe_data.title}
    인분 : {recipe_data.servings}
    조리시간 : {recipe_data.cooking_time}
    조리 난이도 : {recipe_data.level}
    필요한 재료들 : {recipe_data.ingredients}
    조리 순서 : {recipe_data.steps}
    이 레시피에서 최대한 필요한 내용만 뽑아서 자세하게 누구나 요리할 수 있는 {servings}인분으로 버전으로 만들어줘
    """

    print(f"Prompt: {prompt}")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text
