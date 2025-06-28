from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

assistant_authenticator = IAMAuthenticator('D9eX2sLqR8mNw3TjY5bVcQpLkZrT1XoM')
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=assistant_authenticator
)
assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')

ASSISTANT_ID = 'b2c3d4e5-6789-40fa-gh56-klmnopqrstuv'

def send_message_to_assistant(message, session_id):
    response = assistant.message(
        assistant_id=ASSISTANT_ID,
        session_id=session_id,
        input={'message_type': 'text', 'text': message}
    ).get_result()
    return response

def create_session():
    session = assistant.create_session(assistant_id=ASSISTANT_ID).get_result()
    return session['session_id']