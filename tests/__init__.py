# import responses
# import requests
# import base64
# import json
# import unittest

# from utils.http_handler import HTTPHandler, HTTPHandlerException

# url_to_call = 'https://testserver.com/api/v1/foo'

# class TestHTTPHandler(unittest.TestCase):
#     def test_get_calls_correct_url(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(rsps.calls[0].request.url, url_to_call)
#             self.assertEqual(response['raw_response'].url, url_to_call)


#     def test_post_calls_correct_url(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.POST,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.post(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(rsps.calls[0].request.url, url_to_call)
#             self.assertEqual(response['raw_response'].url, url_to_call)
    
#     def test_put_calls_correct_url(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.PUT,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.put(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(rsps.calls[0].request.url, url_to_call)
#             self.assertEqual(response['raw_response'].url, url_to_call)

#     def test_delete_calls_correct_url(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.DELETE,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.delete(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(rsps.calls[0].request.url, url_to_call)
#             self.assertEqual(response['raw_response'].url, url_to_call)

#     def test_get_uses_get_method(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)

#     def test_post_uses_post_method(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.POST,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             handler.post(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
    
#     def test_put_uses_put_method(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.PUT,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             handler.put(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)

#     def test_delete_uses_delete_method(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.DELETE,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=200,
#                 content_type='application/json'
#             )
#             handler.delete(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)

#     def test_200(self):
#         handler = HTTPHandler()
        # with responses.RequestsMock() as rsps:
        #     rsps.add(
        #         responses.GET,
        #         url_to_call,
        #         body=json.dumps({'data': True}),
        #         status=200,
        #         content_type='application/json'
        #     )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(response['data'], {'data': True})

#     def test_201(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'data': True}),
#                 status=201,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 201)
#             self.assertEqual(response['data'], {'data': True})

#     def test_304(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=304,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call, headers={'If-None-Match': 'randomEtag'})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 304)
#             assert "If-None-Match" in rsps.calls[0].request.headers
#             self.assertEqual(rsps.calls[0].request.headers['If-None-Match'], 'randomEtag')

#     def test_400(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'error': 'Something Went Wrong...'}),
#                 status=400,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 400)
#             self.assertEqual(response['data'], {'error': 'Something Went Wrong...'})

#     def test_401(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=401,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 401)

#     def test_403(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=403,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 403)

#     def test_404(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=404,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 404)

#     def test_409(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=409,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 409)

#     def test_420(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=420,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 420)

#     def test_429(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=429,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 429)

#     def test_500(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=500,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 500)

#     def test_503(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=503,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 503)

#     def test_unhandled_status_code(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=666,
#                 content_type='application/json'
#             )
#             with self.assertRaises(HTTPHandlerException) as context:
#                 handler.get(url_to_call)
#                 self.assertEqual(context.exception.message, 'Status Code Handler for 666 Not Implemented')
#             self.assertEqual(len(rsps.calls), 1)

#     def test_proxies(self):
#         pass

#     def test_get_headers(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call, headers={'foo': 'bar'})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['foo'], 'bar')

#     def test_get_auth(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call, auth=requests.auth.HTTPBasicAuth('user', 'pass'))
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['Authorization'].replace('Basic ', ''), base64.b64encode('user:pass'.encode()).decode())
            

#     def test_get_params(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call, params={'query': 'foo', 'after': 9000})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual("query=foo&after=9000" in rsps.calls[0].request.url, True)

#     def test_post_headers(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.POST,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.post(url_to_call, headers={'foo': 'bar'})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['foo'], 'bar')

#     def test_post_auth(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.POST,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.post(url_to_call, auth=requests.auth.HTTPBasicAuth('user', 'pass'))
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['Authorization'].replace('Basic ', ''), base64.b64encode('user:pass'.encode()).decode())

#     def test_post_data(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.POST,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.post(url_to_call, data={'foo': 'bar'})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)

#     def test_put_headers(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.PUT,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.put(url_to_call, headers={'foo': 'bar'})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['foo'], 'bar')

#     def test_put_auth(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.PUT,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.put(url_to_call, auth=requests.auth.HTTPBasicAuth('user', 'pass'))
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['Authorization'].replace('Basic ', ''), base64.b64encode('user:pass'.encode()).decode())

#     def test_put_data(self):
#         pass

#     def test_delete_headers(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.DELETE,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.delete(url_to_call, headers={'foo': 'bar'})
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['foo'], 'bar')

#     def test_delete_auth(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.DELETE,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.delete(url_to_call, auth=requests.auth.HTTPBasicAuth('user', 'pass'))
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(rsps.calls[0].request.headers['Authorization'].replace('Basic ', ''), base64.b64encode('user:pass'.encode()).decode())

#     def test_html_content(self):
#         pass

#     def test_json_content(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body=json.dumps({'hello': 'world'}),
#                 status=200,
#                 content_type='application/json'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(response['data'], {'hello': 'world'})
#             self.assertEqual(type(response['data']), dict)

#     def test_plain_text_content(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 body='Hello Test',
#                 status=200,
#                 content_type='text/plain'
#             )
#             response = handler.get(url_to_call)
#             self.assertEqual(len(rsps.calls), 1)
#             self.assertEqual(response['status_code'], 200)
#             self.assertEqual(response['data'], 'Hello Test')

#     def test_unhandled_content(self):
#         handler = HTTPHandler()
#         with responses.RequestsMock() as rsps:
#             rsps.add(
#                 responses.GET,
#                 url_to_call,
#                 status=200,
#                 content_type='virtual-reality/ready-player-one'
#             )
#             with self.assertRaises(HTTPHandlerException) as context:
#                 handler.get(url_to_call)
#                 self.assertEqual(context.exception.message, 'No handler implemented for Content-Type: virtual-reality/ready-player-one')
#             self.assertEqual(len(rsps.calls), 1)
