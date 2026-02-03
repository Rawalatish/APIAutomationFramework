import pytest
import allure


from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import payload_create_booking
from src.helpers.payload_manager import *
from src.utils.utils import Util

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_json_key_for_not_null, \
    verify_http_status_code
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null "
        "and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        post_response_op = post_request(url=APIConstants.url_create_booking(),
                     headers=Util().common_headers_json(),
                     auth=None,
                     payload=payload_create_booking(),
                     in_json=False                        # here we want full response so we passed Fasle
                     )

        booking_id = post_response_op.json()["bookingid"]

        actual_status_code = post_response_op.status_code
        verify_http_status_code(response_data=post_response_op, expect_data=200)
        verify_json_key_for_not_null(booking_id)

    def test_create_booking_negative(self):         # empty payload passed
        # URL, Headers, Payload,
        post_response_op = post_request(url=APIConstants.url_create_booking(), auth=None, headers=Util().common_headers_json(),
                                payload={}, in_json=False)
        # ER == AR
        # 500 == 500
        # verify_http_status_code(response_data=post_response_op, expect_data=500)
        verify_http_status_code(post_response_op, 500)





