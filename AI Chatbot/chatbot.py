import json
import difflib

def load_responses(file_path):
    with open(file_path, 'r') as file:
        responses = json.load(file)
    return responses

def save_responses(file_path, responses):
    with open(file_path, 'w') as file:

        json.dump(responses, file, indent=4)

def get_response(input_text, responses):
    if input_text in responses:
        return responses[input_text]
    else:
        closest_match = difflib.get_close_matches(input_text, responses.keys(), n=1, cutoff=0.8)
        if closest_match:
            return responses[closest_match[0]]
        else:
            return None

def main():
    file_path = "knowledge_base.json" 
    responses = load_responses(file_path)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input, responses)
        if response:
            print("Bot:", response)
        else:
            new_response = input("Bot: I'm sorry, I don't know the answer to that. What should I respond? ")
            responses[user_input] = new_response
            save_responses(file_path, responses)
            print("Bot: Thanks! I'll remember that.")

if __name__ == "__main__":
    main()


