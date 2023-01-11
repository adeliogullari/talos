from requests_mock import Mocker


def test_create_request_url(talos):
    kwargs = {'protocol': 'https',
              'host': 'localhost',
              'port': '8080',
              'path': 'product/{productId}',
              'path_params': {'productId': '1234'},
              'query_params': {'productName': 'Hobbit', 'productCategory': 'Fiction'},
              'fragment': 'productpage=2'}
    request_url = talos.run_keyword(name="create_request_url", args=[], kwargs=kwargs)
    assert request_url == "https://localhost:8080/product/1234?productName=Hobbit&productCategory=Fiction#productpage=2"


def test_send_get_request(talos):
    with Mocker(real_http=True) as mocker:
        mock_data = {"key": "value"}
        mocker.register_uri('GET', 'https://localhost:8080', json=mock_data)
        kwargs = {'url': 'https://localhost:8080', 'headers': {}}
        response = talos.run_keyword(name="send_get_request", args=[], kwargs=kwargs)
        assert (200, mock_data) == (response.status_code, response.json())


def test_send_post_request(talos):
    with Mocker(real_http=True) as mocker:
        mock_data = {"key": "value"}
        mocker.register_uri('POST', 'https://localhost:8080', json=mock_data)
        kwargs = {'url': 'https://localhost:8080', 'data': mock_data, 'headers': {}}
        response = talos.run_keyword(name="send_post_request", args=[], kwargs=kwargs)
        assert (201, mock_data) == (response.status_code, response.json())


def test_send_patch_request(talos):
    with Mocker(real_http=True) as mocker:
        mock_data = {"key": "value"}
        mocker.register_uri('PATCH', 'https://localhost:8080', json=mock_data)
        kwargs = {'url': 'https://localhost:8080', 'data': mock_data, 'headers': {}}
        response = talos.run_keyword(name="send_patch_request", args=[], kwargs=kwargs)
        assert (200, mock_data) == (response.status_code, response.json())


def test_send_put_request(bionic):
    with Mocker(real_http=True) as mocker:
        mock_data = {"key": "value"}
        mocker.register_uri('PUT', 'https://localhost:8080', json=mock_data)
        kwargs = {'url': 'https://localhost:8080', 'data': mock_data, 'headers': {}}
        response = bionic.run_keyword(name="send_put_request", args=[], kwargs=kwargs)
        assert (200, mock_data) == (response.status_code, response.json())


def test_send_delete_request(talos):
    with Mocker(real_http=True) as mocker:
        mock_data = {"key": "value"}
        mocker.register_uri('DELETE', 'https://localhost:8080', json=mock_data)
        kwargs = {'url': 'https://localhost:8080', 'headers': {}}
        response = talos.run_keyword(name="send_delete_request", args=[], kwargs=kwargs)
        assert (200, mock_data) == (response.status_code, response.json())


# def test_send_get_request(bionic):
#     with requests_mock.Mocker(real_http=True) as mocker:
#         mock_data = {"key": "value"}
#         mocker.register_uri('GET', 'http://test.com', json=mock_data)
#         kwargs = {'url': 'http://test.com', 'headers': {}}
#         response = bionic.run_keyword(name="send_get_request", args=[], kwargs=kwargs)
#         assert (200, mock_data) == (response.status_code, response.json())


# import requests_mock
# from collections import defaultdict
# from typing import AnyStr, DefaultDict, Mapping
# import re
#
# url_configuration_variables_default_dict = defaultdict(
#     Mapping[str, defaultdict],
#     {'API PROTOCOL': 'http',
#      'API HOST': 'localhost',
#      'API PORT': '8080',
#      'API SAP': 'LOY',
#      'API VERSION': 'v1',
#      'API PROJECT TYPE': 'programs',
#      'PROGRAM OWNER': 'DY',
#      'PROGRAM CODE': 'EP'
#      })
#
# header_configuration_variables_default_dict = defaultdict(
#     Mapping[str, defaultdict],
#     {'LSS USERS': [{"office_id": "NCE1A0955", "sign": "5706FM", "organization": "1A", "user_id": "DEFAULT_USER"}],
#      'SAP': 'SAP',
#      'USER ID': 'DEFAULT_USER',
#      'CONTENT TYPE': 'application/vnd.amadeus+json'
#      })
#
#
# def url_configuration_side_effect(variable_name: AnyStr):
#     return url_configuration_variables_default_dict.get(re.search("[A-Za-z0-9\\s]+", variable_name).group())
#
#
# def headers_configuration_side_effect(variable_name: AnyStr):
#     return header_configuration_variables_default_dict.get(re.search("[A-Za-z0-9\\s]+", variable_name).group())
#
#
# def test_create_request_url_with_custom_arguments(bionic, mocker):
#     mocker.patch("robot.libraries.BuiltIn.BuiltIn.get_variable_value", side_effect=url_configuration_side_effect)
#     kwargs = {'protocol': 'http', 'host': 'localhost', 'port': '8080', 'sap': 'LOY', 'version': 'v1',
#               'program_owner': 'VEL', 'program_code': 'VEL', 'path': 'membership', 'membershipId': '12345'}
#     request_url = bionic.run_keyword(name="create_request_url", args=[], kwargs=kwargs)
#     assert request_url == "http://localhost:8080/LOY/v1/loyalty/VEL/programs/VEL/membership?membershipId=12345"
#
#
# def test_create_request_url_with_default_configurations(bionic, mocker):
#     mocker.patch("robot.libraries.BuiltIn.BuiltIn.get_variable_value", side_effect=url_configuration_side_effect)
#     kwargs = {'path': 'membership', 'membershipId': '12345'}
#     request_url = bionic.run_keyword(name="create_request_url", args=[], kwargs=kwargs)
#     assert request_url == "http://localhost:8080/LOY/v1/loyalty/DY/programs/EP/membership?membershipId=12345"
#
#
# def test_generate_request_headers_with_custom_arguments(bionic, mocker):
#     mocker.patch("robot.libraries.BuiltIn.BuiltIn.get_variable_value", side_effect=headers_configuration_side_effect)
#     kwargs = {'sap': '1ASIULOYINTD', 'user_id': 'DEFAULT_USER', 'if_match': 'IF-MATCH'}
#     request_headers = bionic.run_keyword(name="generate_request_headers", args=[], kwargs=kwargs)
#     assert '<OFFICEID VALUE="NCE1A0955"/>' in request_headers['Ama-Internal-DCX'] and \
#            '<ORGANIZATION VALUE="1A"/>' in request_headers['Ama-Internal-DCX'] and \
#            '<SAP NAME="1ASIULOYINTD" FARM="EXT"/>' in request_headers['Ama-Internal-DCX'] and \
#            'IF-MATCH' in request_headers['If-Match']
#
#
# def test_generate_request_headers_with_default_configurations(bionic, mocker):
#     mocker.patch("robot.libraries.BuiltIn.BuiltIn.get_variable_value", side_effect=headers_configuration_side_effect)
#     kwargs = {'sap': '1ASIULOYINT', 'user_id': 'DEFAULT_USER'}
#     request_headers = bionic.run_keyword(name="generate_request_headers", args=[], kwargs=kwargs)
#     assert '<OFFICEID VALUE="NCE1A0955"/>' in request_headers['Ama-Internal-DCX'] and \
#            '<ORGANIZATION VALUE="1A"/>' in request_headers['Ama-Internal-DCX']
#
#
# def test_send_get_request(bionic):
#     with requests_mock.Mocker(real_http=True) as mocker:
#         mock_data = {"key": "value"}
#         mocker.register_uri('GET', 'http://test.com', json=mock_data)
#         kwargs = {'url': 'http://test.com', 'headers': {}}
#         response = bionic.run_keyword(name="send_get_request", args=[], kwargs=kwargs)
#         assert (200, mock_data) == (response.status_code, response.json())
#
#
# def test_send_post_request(bionic):
#     with requests_mock.Mocker(real_http=True) as mocker:
#         mock_data = {"key": "value"}
#         mocker.register_uri('POST', 'http://test.com', json=mock_data)
#         kwargs = {'url': 'http://test.com', 'data': mock_data, 'headers': {}}
#         response = bionic.run_keyword(name="send_post_request", args=[], kwargs=kwargs)
#         assert mock_data == response.json()
#
#
# def test_send_patch_request(bionic):
#     with requests_mock.Mocker(real_http=True) as mocker:
#         mock_data = {"key": "value"}
#         mocker.register_uri('PATCH', 'http://test.com', json=mock_data)
#         kwargs = {'url': 'http://test.com', 'data': mock_data, 'headers': {}}
#         response = bionic.run_keyword(name="send_patch_request", args=[], kwargs=kwargs)
#         assert (200, mock_data) == (response.status_code, response.json())
#
#
# def test_send_put_request(bionic):
#     with requests_mock.Mocker(real_http=True) as mocker:
#         mock_data = {"key": "value"}
#         mocker.register_uri('PUT', 'http://test.com', json=mock_data)
#         kwargs = {'url': 'http://test.com', 'data': mock_data, 'headers': {}}
#         response = bionic.run_keyword(name="send_put_request", args=[], kwargs=kwargs)
#         assert mock_data == response.json()
#
#
# def test_send_delete_request(bionic):
#     with requests_mock.Mocker(real_http=True) as mocker:
#         mock_data = {"key": "value"}