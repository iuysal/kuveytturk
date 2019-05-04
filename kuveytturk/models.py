from kuveytturk.error import KTError


def _parse_error(results):
    errors = []
    if results:
        for result in results:
            message = result.get('errorMessage', None)
            code = result.get('errorCode', None)
            errors.append(ErrorModel(message, code))
    return errors


class ResultModel(object):
    """
    This models represents the "Response Structure" of the API responses described at
    https://developer.kuveytturk.com.tr/#/documentation/general/Getting%20Started
    """
    def __init__(self, response):
        if 'success' not in response or 'results' not in response:
            raise KTError('Invalid response!')
        self.response = response
        self.value = response['value'] if 'value' in response else None
        self.results = _parse_error(response['results'])
        self.success = response['success']
        self.isMockResponse = False
        if 'isMockResponse' in response:
            self.isMockResponse = response['isMockResponse']

    def __repr__(self):
        return str(self.response)


class ErrorModel(object):
    """
    Error object, having "message" and "code" properties.
    """
    def __init__(self, error_message, error_code):
        self.message = error_message
        self.code = error_code

    def __repr__(self):
        return self.message
