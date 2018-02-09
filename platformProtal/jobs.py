
import time
import requests
from datetime import datetime
import threading
from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
from rws.models import TDatareportConfig


@register_job(scheduler, "interval", seconds=60, replace_existing=True)
def rws_mail():
	configs = TDatareportConfig.objects.all()
	for config in configs:
		if config.enable==1 and config.schedule:
			print(datetime.now().hour,config.schedule.hour)
			print(datetime.now().minute, config.schedule.minute)
			print('{"task":"%s"}' % config.task)
			if datetime.now().hour == config.schedule.hour\
			and datetime.now().minute ==config.schedule.minute:
				new_thread = threading.Thread(target=rws_datareportmail, args=(config.task,))
				new_thread.start()
			else:
				print("not schdule")

def rws_datareportmail(task):
	headers = {
		'content-type': "application/json"
	}
	ret = requests.post("http://api.internal.source3g.com/rws/datareportmail",
						data='{"task":"%s"}' % task,
						headers=headers).text
	print(ret)



register_events(scheduler)

scheduler.start()
print("Scheduler started!")