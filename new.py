import random

# Define a list of symptoms and corresponding responses
symptoms = {
    "headache": "It may be due to stress or dehydration. Make sure to drink enough water and take breaks when needed.",
    "fever": "Fever can be a sign of an underlying infection. It's important to rest and monitor your temperature. If it persists or worsens, consult a doctor.",
    "cough": "Coughing can be caused by various factors such as allergies, cold, or respiratory infections. Stay hydrated and consider taking over-the-counter cough medicine.",
    "fatigue": "Fatigue can result from lack of sleep, poor diet, or excessive physical or mental exertion. Make sure to get enough rest and eat a balanced diet.",
    "nausea": "Nausea can be caused by various reasons such as food poisoning or motion sickness. Try to eat light and bland food, and rest as much as possible.",
}

# Define a function to handle user input and provide responses
def healthcare_bot():
    print("Welcome to the AI Healthcare Bot System!")
    print("I can help you with common health concerns.")
    print("Please describe your symptoms or type 'quit' to exit.")

    while True:
        user_input = input("User: ")
        
        # Check if the user wants to quit
        if user_input.lower() == "quit":
            print("Thank you for using the AI Healthcare Bot System. Take care!")
            break

        # Check if the symptom is in the list
        if user_input.lower() in symptoms:
            response = symptoms[user_input.lower()]
            print("AI Bot: " + response)
        else:
            print("AI Bot: I'm sorry, I don't have information about that symptom.")

# Run the healthcare bot system
healthcare_bot()
