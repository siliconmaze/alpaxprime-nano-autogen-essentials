"""Lab 6 Solution: Real-World Applications - Code Review"""
import os
from dotenv import load_dotenv
import autogen
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

config_list = [{"model": "gpt-4", "api_key": api_key}]

# Create reviewer agent
reviewer = AssistantAgent(
    name="reviewer",
    llm_config={"config_list": config_list},
    system_message="""You are an expert code reviewer.
    Review code for:
    1. Bugs and errors
    2. Security vulnerabilities
    3. Code quality
    4. Best practices
    
    Provide specific, actionable feedback."""
)

# Create code submitter
submitter = UserProxyAgent(
    name="submitter",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5
)

# Code with issues to review
code_to_review = '''
def get_user_data(user_id, db_connection):
    # Security issue: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = db_connection.cursor()
    cursor.execute(query)
    return cursor.fetchone()

def send_password(email, password):
    # Security issue: sending password in plain text
    import smtplib
    server = smtplib.SMTP("smtp.company.com")
    msg = f"Password reset: {password}"
    server.sendmail("noreply@company.com", email, msg)

def process_data(data):
    # Bug: no error handling
    result = data["key"] / 0
    return result
'''

# Start review
submitter.initiate_chat(
    reviewer,
    message=f"Please review this code for security bugs and issues:\n\n{code_to_review}"
)

print("\n✓ Code review completed!")
