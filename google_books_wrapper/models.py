
class Result:
    def __init__(self, status_code: int, message: str = '', data: list[dict] = None):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []





BASE_URL = "www.googleapis.com/books"

client = RestAdapter(hostname=BASE_URL)

json = client.get(endpoint="volumes",ep_params={'q': "cadcmalcmdacakdcadcmlad"})
    
    
print(json)