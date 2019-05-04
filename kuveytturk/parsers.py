from kuveytturk.error import KTError
from kuveytturk.models import ResultModel
from kuveytturk.utils import import_simplejson


class Parser(object):

    def parse(self, method, payload):
        """
        Parse the response payload and return the result.
        Returns a tuple that contains the result data and the cursors
        (or None if not present).
        """
        raise NotImplementedError


class JSONParser(Parser):

    payload_format = 'json'

    def __init__(self):
        self.json_lib = import_simplejson()
        self.model = ResultModel

    def parse(self, payload):
        try:
            json = self.json_lib.loads(payload)
        except Exception as e:
            raise KTError('Failed to parse JSON payload: %s' % e)

        return self.model(json)
