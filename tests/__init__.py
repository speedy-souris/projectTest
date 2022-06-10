import requests
import pytest
from src.redis_utilities import erasing_data
from src.session.behavior_parameters import BehaviorParams
from src.APIs import google_api
from src.APIs.mock_api import get_place_id_googleMap_api_mockreturn
from src.APIs.mock_api import get_address_googleMap_api_mockreturn
from src.APIs.mock_api import get_mockreturn
import main
