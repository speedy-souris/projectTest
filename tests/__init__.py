import requests
import pytest
from ..src.redis_utilities import erasing_data
from ..src.conversation import Conversation
from ..src import google_api
from ..src.mock_api import get_place_id_googleMap_api_mockreturn
from ..src.mock_api import get_address_googleMap_api_mockreturn
from ..src.mock_api import get_mockreturn
from ..main import main
from ..main import get_user_presentation_management
