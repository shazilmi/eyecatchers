from celery import shared_task
import flask_excel as excel
from application.mail_service import daily_reminder_influencer
from database.functions import get_influencer_reminder

@shared_task(ignore_result = False, serializer = "pickle")
def create_resource():
	csv_output = excel.make_response_from_array({"key" : "value"}, 
											 file_name= "test1.csv",
											 file_type= "csv")
	return csv_output

@shared_task(ignore_result = True)
def daily_reminder():
	emails = get_influencer_reminder()
	for i in emails:
		daily_reminder_influencer(i)
	return "Done"