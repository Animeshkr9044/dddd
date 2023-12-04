from langchain import PromptTemplate
import json

# Define the conversation template
template = '''Hello! I'm your AI sales assistant, and I'm here to assist you with your loan application. Let's gather some information to get started:

1. Are you interested in applying for a loan? (Yes/No){loan_interest}
2. If yes, what is the desired loan amount?{loan_amount}
3. What is the purpose of the loan? (CAR/HOME/BUSINESS/PERSONAL){loan_purpose}
4. Do you file Income Tax Returns (ITR)? (Yes/No){itr_status}
5. If yes, could you provide your latest ITR details?{profession}
6. What is your profession?{annual_turnover}
   - If Business, could you provide the annual turnover based on GST records?{annual_salary}
   - If Salaried, what is your annual salary as per your salary slips?{goodbye}

Thank you for providing this information. Once we have all the necessary details, we'll proceed with your loan application. If you have any additional questions or if there's anything else you'd like to discuss, feel free to let me know.

To end our conversation, please type "Goodbye" when you're ready to conclude. Thank you!'''

# Create a PromptTemplate
sales_agent_prompt = PromptTemplate(
    input_variables=["loan_interest", "loan_amount", "loan_purpose", "itr_status", "profession", "annual_turnover", "annual_salary", "goodbye"],
    template=template,
)

# Function to simulate a conversation with the AI sales assistant
def simulate_conversation():
    user_responses = {}
    
    # Follow the fixed sequence of questions
    questions = {
        "loan_interest", "loan_amount", "loan_purpose", "itr_status", "profession", "annual_turnover", "annual_salary", "goodbye"
    }

    for variable in questions:
        user_responses[variable] = input(f"{variable.replace('_', ' ').title()}: ").strip()

    return user_responses

# Main function
def main():
    print("Simulating conversation with the AI sales assistant:")
    user_input = simulate_conversation()

    # Format the user input for the sales agent prompt
    formatted_input = {key: f'{{{key}}}' for key in sales_agent_prompt.input_variables}
    formatted_input.update(user_input)

    # Use the formatted input to create the final conversation
    conversation = sales_agent_prompt.format(**formatted_input)

    # Print the final conversation
    print("\nFinal Conversation:")
    print(conversation)

    # Extract information in the form of JSON
    loan_info_json = {
        "loan_interest": user_input["loan_interest"],
        "loan_amount": int(user_input["loan_amount"]),
        "loan_purpose": user_input["loan_purpose"],
        "itr_status": user_input["itr_status"],
        "profession": user_input["profession"],
        "annual_turnover": int(user_input["annual_turnover"]),
        "annual_salary": int(user_input["annual_salary"]) if user_input["annual_salary"].lower() != 'none' else None,
        "goodbye": user_input["goodbye"]
    }

    # Print the JSON information
    print("\nJSON Output:")
    print(json.dumps(loan_info_json, indent=4))

if __name__ == "__main__":
    main()
