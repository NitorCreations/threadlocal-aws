import sys
from threadlocal_aws import _get_local, session, PY37
from threadlocal_aws.pep562 import Pep562

def __getattr__(name):
    return lambda region=None: _get_local(name, session().client, session_region=region)

if not PY37:
    Pep562(__name__)