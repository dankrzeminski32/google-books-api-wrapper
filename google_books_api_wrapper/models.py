
class HttpResult:
    """_summary_
    
        :param status_code: http response status code (e.g. 200, 404, etc)
        :type status_code: int
        :param message: http response message body, defaults to ''
        :type message: str, optional
        :param data: http json response data, defaults to None
        :type data: list[dict], optional
    """
    def __init__(self, status_code: int, message: str = '', data: dict = None):
        """_summary_

        :param status_code: _description_
        :type status_code: int
        :param message: _description_, defaults to ''
        :type message: str, optional
        :param data: _description_, defaults to None
        :type data: list[dict], optional
        """
        self.status_code = int(status_code)
        self.data = data if data else {}


class Book:
    def __init__(self, title: str, authors: list[str]):
        self.title = title
        self.authors = authors


# BASE_URL = "www.googleapis.com/books"

# client = RestAdapter(hostname=BASE_URL)

# json = client.get(endpoint="volumes",ep_params={'q': "cadcmalcmdacakdcadcmlad"})
    
    
# print(json)