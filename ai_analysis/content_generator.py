import openai

class ContentGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_content_idea(self, trend):
        prompt = f"Generate a TikTok video idea based on the trend: {', '.join(trend)}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

    def suggest_hashtags(self, description):
        prompt = f"Suggest 5 relevant hashtags for this TikTok video description: {description}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip().split()
