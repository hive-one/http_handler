import requests

from bs4 import BeautifulSoup

class HTTPHandlerException(Exception):
    def __init__(self, error_msg=''):
        super().__init__() 
        self.error_msg = error_msg

class HTTPHandler:
    def __init__(self, proxies=None):
        if not proxies:
            proxies = {}
        self.proxies = proxies

    def get(self, url: str, params: dict = {}, headers: dict = {}, cookies: dict = {}, auth = (), **kwargs) -> dict:
        """ GET Request

        Parameters:
        url (string): URL to connect to
        params (dict): Dict of URL params to append to the end of the URL
        headers (dict): Dict of request headers
        cookies (dict): Dict of cookies
        auth (tuple): Auth credentials

        Returns:
        dict: Returns a dict with the parsed_data response, status_code and the raw requests.Response object

        """
        try:
            response = requests.get(
                url,
                headers=headers,
                cookies=cookies,
                params=params,
                proxies=self.proxies,
                auth=auth,
                **kwargs
            )
        except requests.exceptions.RequestException as error:
            raise HTTPHandlerException(error_msg=error)

        return self.response_handle(response)

    def post(self, url: str, data: dict = {}, headers: dict = {}, cookies: dict = {}, auth = (), **kwargs) -> dict:
        """ POST Request

        Parameters:
        url (string): URL to connect to
        data (dict): Data to send to the URL
        headers (dict): Dict of request headers
        cookies (dict): Dict of cookies
        auth (tuple): Auth credentials

        Returns:
        dict: Returns a dict with the parsed_data response, status_code and the raw requests.Response object

        """
        # TODO: What if we want to send form-data and not json data?
        try:
            response = requests.post(
                url,
                json=data,
                headers=headers,
                cookies=cookies,
                proxies=self.proxies,
                auth=auth,
                **kwargs
            )
        except requests.exceptions.RequestException as error:
            raise HTTPHandlerException(error_msg=error)

        return self.response_handle(response)

    def put(self, url: str, data: dict = {}, headers: dict = {}, cookies: dict = {}, auth = (), **kwargs) -> dict:
        """ GET Request

        Parameters:
        url (string): URL to connect to
        data (dict): Data to send to the URL
        headers (dict): Dict of request headers
        cookies (dict): Dict of cookies
        auth (tuple): Auth credentials

        Returns:
        dict: Returns a dict with the parsed_data response, status_code and the raw requests.Response object

        """
        try:
            response = requests.put(
                url,
                data=data,
                headers=headers,
                cookies=cookies,
                proxies=self.proxies,
                auth=auth,
                **kwargs
            )
        except requests.exceptions.RequestException as error:
            raise HTTPHandlerException(error_msg=error)

        return self.response_handle(response)

    def delete(self, url: str, headers: dict = {}, cookies: dict = {}, auth = (), **kwargs) -> dict:
        """ GET Request

        Parameters:
        url (string): URL to connect to
        headers (dict): Dict of request headers
        cookies (dict): Dict of cookies
        auth (tuple): Auth credentials

        Returns:
        dict: Returns a dict with the parsed_data response, status_code and the raw requests.Response object

        """
        try:
            response = requests.delete(
                url,
                headers=headers,
                cookies=cookies,
                proxies=self.proxies,
                auth=auth,
                **kwargs
            )
        except requests.exceptions.RequestException as error:
            raise HTTPHandlerException(error_msg=error)

        return self.response_handle(response)

    def request_log(self, response: requests.Response):
        """ Logs all requests & responses to debug logger

        Parameters:
        response (requests.Response): Response objects from the requests lib

        """
        # log.debug({
        #     "type": "request",
        #     "url": response.url,
        #     "method": response.request.method,
        #     "request_headers": response.request.headers,
        #     "response_headers": response.headers,
        #     "raw_content": response.content
        # })

    def response_handle(self, response: requests.Response) -> dict:
        """ Handles HTTP response, deals with status_codes

        Parameters:
        response (requests.Response)

        Returns:
        dict: Returns a dict with the parsed_data response, status_code and the raw requests.Response object

        """
        self.request_log(response)
        return {
            'data': self.get_response_content(response),
            'status_code': response.status_code,
            'raw_response': response
        }

    def get_response_content(self, response: requests.Response):
        # TODO: Handle JSON Decode Error
        # TODO: Handle BeautifulSoup Errors
        if 'Content-Type' in response.headers:
            if 'text/html' in response.headers['Content-Type']:
                return BeautifulSoup(response.content)
            elif 'text/plain' in response.headers['Content-Type']:
                return response.text
            elif 'json' in response.headers['Content-Type']:
                return response.json()
            else:
                raise HTTPHandlerException(f'No handler implemented for Content-Type: {response.headers["Content-Type"]}')
        return None
