from kuveytturk.binder import bind_api
from kuveytturk.parsers import JSONParser


def prepare_params(*args, **kwargs):
    """Converts both positional and named arguments into a dict."""
    if not kwargs:
        kwargs = {}

    for arg in args:
        # if the positional argument is a dictionary, then put its items
        # into kwargs dict. Otherwise, ignore the argument
        if isinstance(arg, dict):
            for k, v in arg.items():
                kwargs[k] = v

    # Finally, all the supplied arguments are in a unified dict.
    return kwargs


class API(object):
    """
    KuveytTurk API

    This class contains 4 different api endpoints to give you an
    idea of what type of url paths are supported. You can simply
    call the generic_request method with the desired endpoint
    parameter settings that are documented on the API Market.

    Please see the examples for getting started.
    """

    def __init__(self, auth_handler=None,
                 host='https://apitest.kuveytturk.com.tr/prep',
                 timeout=60, parser=None):
        """ API instance Constructor

        :param auth_handler:
        :param host: url of the server of the rest api, default: 'https://apitest.kuveytturk.com.tr/prep'
        :param timeout: delay before to consider the request as timed out in seconds, default:60
        :param parser: Parser instance to parse the responses, default:None
        """
        self.auth = auth_handler
        self.host = host
        self.timeout = timeout
        self.parser = parser or JSONParser()

    def _call_endpoint(self, endpoint_params, *args, **kwargs):
        """
        Initiatest the api request after modifying the parameters if necessary.
        :param endpoint_params:
        :param args:
        :param kwargs:
        :return:
        """
        if 'host' in kwargs:
            self.host = kwargs['host']

        return bind_api(
            api=self,
            endpoint_params=endpoint_params,
            post_data=prepare_params(*args, **kwargs)
        )

    def generic_request(self, endpoint_params, *args, **kwargs):
        """
        This method can be used to call the endpoints that are not wrapped in this class,
        by simply passing the endpoint_params dict with the following keys:
        'path', 'method', 'scope', and 'authorization_flow'

        :param endpoint_params:
        :param args: positional arguments
        :param kwargs: named arguments
        :return: A ResultModel instance
        """
        return self._call_endpoint(endpoint_params, *args, **kwargs)

    def test_customer_list(self, *args, **kwargs):
        """
        :reference: https://developer.kuveytturk.com.tr/#/documentation/general/Test%20Customer%20List
        """
        return self._call_endpoint(
            {
                'path': '/v1/data/testcustomers',
                'method': 'GET',
                'scope': 'public',
                'authorization_flow': 'client credentials'
            }, *args, **kwargs)

    def account_list(self, *args, **kwargs):
        """
        :reference: https://developer.kuveytturk.com.tr/#/documentation/Accounts/Account%20List
        """
        return self._call_endpoint(
            {
                'path': '/v1/accounts/{suffix?}',
                'method': 'GET',
                'scope': 'accounts',
                'authorization_flow': 'authorization code'
            }, *args, **kwargs)

    def bank_branch_list(self, *args, **kwargs):
        """
        :reference: https://developer.kuveytturk.com.tr/#/documentation/Information%20Services/Bank%20Branch%20List
        """
        return self._call_endpoint(
            {
                'path': '/v1/data/banks/{bankId}/branches?cityId={cityId}',
                'method': 'GET',
                'scope': 'public',
                'authorization_flow': 'client credentials'
            }, *args, **kwargs)

    def collection_list(self, *args, **kwargs):
        """
        :reference: https://developer.kuveytturk.com.tr/#/documentation/Loans%2FFinancing/Collection%20List
        """
        return self._call_endpoint(
            {
                'path': '/v1/collections',
                'method': 'POST',
                'scope': 'loans',
                'authorization_flow': 'client credentials'
            }, *args, **kwargs)

    # def fx_currency_rates(self, *args, **kwargs):
    #     """
    #     :reference: https://developer.kuveytturk.com.tr/#/documentation/Information%20Services/FX%20Currency%20Rates
    #     """
    #     return self._call_endpoint(
    #         {
    #             'path': '/v1/fx/rates',
    #             'method': 'GET',
    #             'scope': 'public',
    #             'authorization_flow': 'client credentials'
    #         }, *args, **kwargs)

    # def bank_list(self, *args, **kwargs):
    #     """
    #     :reference: https://developer.kuveytturk.com.tr/#/documentation/Information%20Services/Bank%20List
    #     """
    #     return self._call_endpoint(
    #         {
    #             'path': '/v1/data/banks',
    #             'method': 'GET',
    #             'scope': 'public',
    #             'authorization_flow': 'client credentials'
    #         }, *args, **kwargs)

    # def moneygram_send(self, *args, **kwargs):
    #     """
    #     :reference: https://developer.kuveytturk.com.tr/#/documentation/MoneyGram/MoneyGram%20Send
    #     """
    #     return self._call_endpoint(
    #         {
    #             'path': '/v1/moneygram/send',
    #             'method': 'POST',
    #             'scope': 'transfers',
    #             'authorization_flow': 'authorization code'
    #         }, *args, **kwargs)
    #
    # def money_transfer_to_iban(self, *args, **kwargs):
    #     """
    #     :reference: https://developer.kuveytturk.com.tr/#/documentation/Money%20Transfers/Money%20Transfer%20to%20IBAN
    #     """
    #     return self._call_endpoint(
    #         {
    #             'path': '/v1/transfers/toIBAN',
    #             'method': 'POST',
    #             'scope': 'transfers',
    #             'authorization_flow': 'authorization code'
    #         }, *args, **kwargs)
