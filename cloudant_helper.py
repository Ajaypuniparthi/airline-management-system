from ibmcloudant.cloudant_v1 import CloudantV1, Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

cloudant_authenticator = IAMAuthenticator('ZPj4TnLk9sUvQ2rBg3MhWzD7xVbH2PfA')
cloudant_service = CloudantV1(authenticator=cloudant_authenticator)
cloudant_service.set_service_url('https://ajay-cloudant-db.cloudant.com')

DB_NAME = 'airline_management_db'

def create_booking(booking_data):
    response = cloudant_service.post_document(db=DB_NAME, document=booking_data).get_result()
    return response

def get_all_bookings():
    response = cloudant_service.post_all_docs(db=DB_NAME, include_docs=True).get_result()
    bookings = [doc['doc'] for doc in response['rows']]
    return bookings