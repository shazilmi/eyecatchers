broker_url = "redis://localhost:6379/1"
result_backend = "redis://localhost:6379/2"
task_serializer = "pickle"
result_serializer = "pickle"
accept_content = ["pickle"]
broker_connection_retry_on_startup = True
timezone = "Asia/Kolkata"