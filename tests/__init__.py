import requests
import pytest
from src.redis_utilities import RedisDataManagement
from src.session.conversation import Conversation
from src.APIs import google_api
from src.APIs.mock_api import get_place_id_googleMap_api_mockreturn
from src.APIs.mock_api import get_address_googleMap_api_mockreturn
from src.APIs.mock_api import get_mockreturn

