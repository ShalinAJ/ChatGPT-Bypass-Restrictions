import openai

openai.api_key = "PUT YOUR API KEY HERE"


prompt_text = str(input("Type here: "))
# Set up the request parameters
model_engine = "text-davinci-002"
prompt = prompt_text

completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

# Get the response from the API
response = completions.choices[0].text
print(response)