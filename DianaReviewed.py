#KOREDE AFOLAMI
#AI CHATBOT "DIANA" :)

import openai

openai.api_key = "" #IMPORT API KEY IN STRING! Not leaving my API key for the public for "security" ;) 
                    #OpenAI API's are very accessible :)

def chat_with_diana(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].messages[0].content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_diana(user_input)
        print("Diana: ", response)