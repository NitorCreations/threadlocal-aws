import sys
from threadlocal_aws import _get_local, session, PY37
from threadlocal_aws.pep562 import Pep562

def __getattr__(name):
    return lambda resource_region=None: _get_local(name, session().resource, session_region=resource_region)

if not PY37:
    Pep562(__name__)