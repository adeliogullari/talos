import requests
from robot.libraries.BuiltIn import BuiltIn
from robotlibcore import keyword
from requests import Response
from robot.api import logger
from ..request.url import Url


class RequestKeywords:

    def __init__(self):
        pass

    @keyword
    def create_request_url(self,
                           protocol=None,
                           host=None,
                           port=None,
                           path=None,
                           path_params=None,
                           query_params=None,
                           fragment=None) -> str:
        url = Url(protocol=protocol, host=host, port=port, path=path, path_params=path_params, query_params=query_params, fragment=fragment)
        return url.build()

    @keyword
    def send_get_request(self, url: str, **kwargs) -> Response:
        response = requests.get(url=url, **kwargs)
        logger.info(f"Request Url: {url}")
        logger.info(f"Request Headers: {kwargs.get('headers')}")
        logger.info(f"Response Headers {response.headers}")
        logger.info(f"Response Data {response.json()}")
        return response

    @keyword
    def send_post_request(self, url: str, data: dict, json: dict, **kwargs) -> Response:
        response = requests.post(url=url, data=data, json=json, **kwargs)
        logger.info(f"Request Url: {url}")
        logger.info(f"Request Headers: {kwargs.get('headers')}")
        logger.info(f"Request Data: {data}")
        logger.info(f"Response Headers: {response.headers}")
        logger.info(f"Response Data: {response.json()}")
        return response

    @keyword
    def send_patch_request(self, url: str, data: str, **kwargs) -> Response:
        response = requests.patch(url=url, data=data, **kwargs)
        logger.info(f"Request Url: {url}")
        logger.info(f"Request Headers: {kwargs.get('headers')}")
        logger.info(f"Request Data: {data}")
        logger.info(f"Response Headers: {response.headers}")
        logger.info(f"Response Data: {response.json()}")
        return response

    @keyword
    def send_put_request(self, url: str, data: str, **kwargs) -> Response:
        response = requests.put(url=url, data=data, **kwargs)
        logger.info(f"Request Url: {url}")
        logger.info(f"Request Headers: {kwargs.get('headers')}")
        logger.info(f"Request Data: {data}")
        logger.info(f"Response Headers: {response.headers}")
        logger.info(f"Response Data: {response.json()}")
        return response

    @keyword
    def send_delete_request(self, url: str, **kwargs) -> Response:
        response = requests.delete(url=url, **kwargs)
        logger.info(f"Request Url: {url}")
        logger.info(f"Request Headers: {kwargs.get('headers')}")
        logger.info(f"Response Headers {response.headers}")
        logger.info(f"Response Data: {response.json()}")
        return response

# import json
# import requests
# import xmltodict
# from collections import defaultdict
# from xml.parsers.expat import errors, ExpatError
# from requests import Response
# from typing import Dict, AnyStr
# from robot.api import logger
# from robot.libraries.BuiltIn import BuiltIn
# from robotlibcore import keyword
#
#
# class RequestManagerKeywords:
#
#     def __init__(self):
#         pass
#
#     def _unparse_dict_to_xml(self, input_dict, full_document: bool = False, short_empty_elements: bool = True) -> None:
#         try:
#             return xmltodict.unparse(input_dict=input_dict, full_document=full_document, short_empty_elements=short_empty_elements)
#         except ExpatError as e:
#             logger.error(f"ExpatError Code: {e.code}")
#             logger.error(f"ExpatError Message: {errors.messages[e.code]}")
#             raise
#
#     @keyword
#     def create_request_url(self,
#                            protocol: AnyStr = None,
#                            host: AnyStr = None,
#                            port: AnyStr = None,
#                            sap: AnyStr = None,
#                            version: AnyStr = None,
#                            program_owner: AnyStr = None,
#                            project_type: AnyStr = None,
#                            program_code: AnyStr = None,
#                            path: AnyStr = None,
#                            **parameters):
#
#         protocol = protocol if protocol else BuiltIn().get_variable_value("${API PROTOCOL}")
#         host = host if host else BuiltIn().get_variable_value("${API HOST}")
#         port = port if port else BuiltIn().get_variable_value("${API PORT}")
#         sap = sap if sap else BuiltIn().get_variable_value("${API SAP}")
#         version = version if version else BuiltIn().get_variable_value("${API VERSION}")
#         program_owner = program_owner if program_owner else BuiltIn().get_variable_value("${PROGRAM OWNER}")
#         project_type = project_type if project_type else BuiltIn().get_variable_value("${API PROJECT TYPE}")
#         program_code = program_code if program_code else BuiltIn().get_variable_value("${PROGRAM CODE}")
#
#         parameters_keys = list(parameters.keys())
#         parameters_values = list(parameters.values())
#
#         if parameters:
#             query = '?' + '&'.join(
#                 list(map(lambda X: X[0] + '=' + X[1], list(zip(parameters_keys, parameters_values)))))
#         else:
#             query = ''
#
#         if project_type == 'parameters':
#             if path:
#                 return f"{protocol}://{host}:{port}/{sap}/{version}/loyalty/{program_owner}/{project_type}/{path}{query}"
#             return f"{protocol}://{host}:{port}/{sap}/{version}/loyalty/{program_owner}/{project_type}{query}"
#
#         return f"{protocol}://{host}:{port}/{sap}/{version}/loyalty/{program_owner}/{project_type}/{program_code}/{path}{query}"
#
#     @keyword
#     def generate_request_headers(self,
#                                  sap=None,
#                                  user_id=None,
#                                  content_type=None,
#                                  if_match=None):
#         request_headers = {}
#
#         sap = sap if sap else BuiltIn().get_variable_value("${SAP}")
#         user_id = user_id if user_id else BuiltIn().get_variable_value("${USER ID}")
#         content_type = content_type if content_type else BuiltIn().get_variable_value("${CONTENT TYPE}")
#         lss_user = list(filter(lambda user: user['user_id'] == user_id, BuiltIn().get_variable_value("${LSS USERS}")))[0]
#
#         ama_internal_dcx = defaultdict(lambda: defaultdict(ama_internal_dcx.default_factory))
#
#         ama_internal_dcx['DCC']['@VERS'] = "1.0"
#
#         ama_internal_dcx['DCC']['MW']['UKEY']['@VAL'] = "123456789"
#         ama_internal_dcx['DCC']['MW']['UKEY']['@TRXNB'] = "1"
#
#         ama_internal_dcx['DCC']['MW']['SAP']['@NAME'] = '1ASIULOYINTD'
#         ama_internal_dcx['DCC']['MW']['SAP']['@FARM'] = 'EXT'
#
#         ama_internal_dcx['DCC']['MW']['DYNR']['PEAKTK']['@TYPE'] = "AIRIT"
#         ama_internal_dcx['DCC']['MW']['DYNR']['PEAKTK']['@VAL'] = lss_user['organization']
#
#         ama_internal_dcx['DCC']['MW']['AFY']['@APP'] = "LOYD"
#         ama_internal_dcx['DCC']['MW']['AFY']['@AS'] = "EDGE"
#
#         ama_internal_dcx['DCC']['SEC']['@VERS'] = "2.11"
#         ama_internal_dcx['DCC']['SEC']['@CONTENTS'] = "UNDEFINED"
#
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['OFFICEID']['@VALUE'] = lss_user['office_id']
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['SIGN']['@VALUE'] = lss_user['sign']
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['SIGN_OFFICE']['@VALUE'] = lss_user['office_id']
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['OOFF']['@VALUE'] = lss_user['office_id']
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['AREACODE']['@VALUE'] = "A"
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['USERID']['@VALUE'] = lss_user['user_id']
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['ORGANIZATION']['@VALUE'] = lss_user['organization']
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['COUNTRY']['@VALUE'] = "FR"
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['IATANUMBER']['@VALUE'] = "12345675"
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['ORIGINTYPECODE']['@VALUE'] = "A"
#         ama_internal_dcx['DCC']['SEC']['USERINFOS']['VND']['@VALUE'] = "AMAD"
#
#         ama_internal_dcx['DCC']['SEC']['USERSETTINGS']['DUTYCODE']['@VALUE'] = "GS"
#
#         ama_internal_dcx['DCC']['SEC']['PREFERENCES']['LANGUAGE']['@VALUE'] = "EN"
#         ama_internal_dcx['DCC']['SEC']['PREFERENCES']['CURRENCY']['@VALUE'] = "EUR"
#
#         ama_internal_dcx['DCC']['SEC']['SECURITYINDICATORS']['@VALUE'] = "YY7"
#
#         ama_internal_dcx['DCC']['SEC']['SIGNER']['@VAL'] = "W"
#
#         request_headers['Content-Type'] = content_type
#
#         request_headers['Ama-Internal-DCX'] = self._unparse_dict_to_xml(input_dict=ama_internal_dcx,
#                                                                         full_document=False,
#                                                                         short_empty_elements=True)
#
#         if if_match:
#             request_headers['If-Match'] = if_match
#
#         return json.loads(json.dumps(request_headers))
#
#     @keyword
#     def send_get_request(self, url: AnyStr, headers: AnyStr) -> Response:
#         response = requests.get(url=url, headers=headers, verify=False)
#         logger.info(f"Request URL: {url}")
#         logger.info(f"Request Headers: {headers}")
#         logger.info(f"Response Headers {response.headers}")
#         return response
#
#     @keyword
#     def send_post_request(self, url: AnyStr, data: Dict, headers: AnyStr) -> Response:
#         response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
#         logger.info(f"Request URL: {url}")
#         logger.info(f"Request Headers: {headers}")
#         logger.info(f"Request Data: {data}")
#         logger.info(f"Response Headers: {response.headers}")
#         logger.info(f"Response Data: {response.json()}")
#         return response
#
#     @keyword
#     def send_patch_request(self, url: AnyStr, data: Dict, headers: AnyStr) -> Response:
#         response = requests.patch(url=url, data=data, headers=headers, verify=False)
#         logger.info(f"Request URL: {url}")
#         logger.info(f"Request Data: {data}")
#         logger.info(f"Request Headers: {headers}")
#         logger.info(f"Response Data: {response.json()}")
#         logger.info(f"Response Headers: {response.headers}")
#         return response
#
#     @keyword
#     def send_put_request(self, url: AnyStr, data: Dict, headers: AnyStr) -> Response:
#         response = requests.put(url=url, data=data, headers=headers, verify=False)
#         logger.info(f"Request URL: {url}")
#         logger.info(f"Request Data: {data}")
#         logger.info(f"Request Headers: {headers}")
#         logger.info(f"Response Data: {response.json()}")
#         logger.info(f"Response Headers: {response.headers}")
#         return response
#
#     @keyword
#     def send_delete_request(self, url: AnyStr, headers: AnyStr) -> Response:
#         response = requests.delete(url=url, headers=headers, verify=False)
#         logger.info(f"Request URL: {url}")
#         logger.info(f"Request Headers: {headers}")
#         logger.info(f"Response Headers {response.headers}")
#         return response