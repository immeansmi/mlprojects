import sys
from src.Data_Science_Projects.logger import logging


class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):

