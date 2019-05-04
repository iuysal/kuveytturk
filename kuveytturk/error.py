import six


class KTError(Exception):
    """Kuveytturk exception"""

    def __init__(self, reason, response=None, api_code=None):
        self.reason = six.text_type(reason)
        self.response = response
        self.api_code = api_code
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason