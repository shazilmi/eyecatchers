from celery import Celery, Task
import application.celeryconfig

def celery_init_app(app):
	class FlaskTask(Task):
		def __call__(self, *args, **kwargs):
			with app.app_context():
				return self.run(*args, **kwargs)

	celery_app = Celery(app.name, task_cls = FlaskTask)
	celery_app.config_from_object(application.celeryconfig)
	return celery_app