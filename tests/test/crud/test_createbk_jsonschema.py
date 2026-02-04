#createbk > create booking json schema

# Get Response
# Create the JSON schema - https://www.jsonschema.net/
# Save that schema into the name.json file
# If you want to validate the json schema - https://www.jsonschemavalidator.net/
import json
import os

import allure
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
# from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBookingJSONSchema(object):
    """
            1. def load_schema(self, filename):
               - 'def': Keyword to define the method.
               - 'load_schema': Name of the function.
               - 'self': Refers to the class instance.
               - 'filename': Path to the JSON schema file.

            2. with open(filename, 'r') as file:
               - 'open(..., "r")': Opens the file in Read Mode.
               - 'with': Context manager that auto-closes the file to prevent memory leaks.
               - 'as file': Assigns the opened file to a variable.

            3. return json.load(file)
               - 'json.load()': Converts JSON file content into a Python Dictionary.
               - 'return': Passes the dictionary back to the caller.
            """
    def load_schema(self, file_name):
        with open(file_name, 'r') as file:     # 'r' means read mode only
            return json.load(file)

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_schema(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # json schema verification
        # response with schema.json stored

        # print("json shema file path: ", os.getcwd())

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "create_booking_schema.json ")
        # file_path = os.path.join(current_dir, "create_booking_wrong_schema.json ")  # form required key we removed "firstname", and data type changed

        # file_path = os.getcwd() + "/create_schema.json"   # or paste full file path  C:\Users\HP\PycharmProjects....crud\create_booking_schema.json
        # Better way to write it:
        # file_path = os.path.join(os.getcwd(), "create_schema.json")


        schema_file = self.load_schema(file_name=file_path)



        try:
            validate(instance=response.json(), schema=schema_file)
        except ValidationError as err:
            print(err.message)
            pytest.fail("failed : Json Schema Error")

            """
            1. except ValidationError as err:
               - Catches specifically the errors where JSON data doesn't match the schema.
               - Stores the error details in the 'err' variable.

            2. print(err.message):
               - Prints a human-readable explanation of why the validation failed 
                 (e.g., "Missing field" or "Wrong data type").

            3. pytest.fail(...):
               - Forcefully marks the test as FAILED in the PyTest report.
               - Stops the execution of the current test case immediately.
            """






