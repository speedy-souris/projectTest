import requests
import pytest
from ..src.conversation import Conversation
from ..src.redis_utilities import erasing_data
from ..src import google_api
from ..src.mock_api import get_place_id_googleMap_api_mockreturn
from ..src import display_behaviour
from ..src.mock_api import get_mockreturn
from ..main import main
from ..src.mock_api import get_address_googleMap_api_mockreturn
from ..src.redis_utilities import read_access_conversation_data
from ..src.counting_behaviour import user_incivility_count
