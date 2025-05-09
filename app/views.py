from django.shortcuts import render
import logging
from django.http import HttpResponse
import datetime

logger = logging.getLogger(__name__)

def welcome_page(request):
    logger.warning(f'Homepage was accessed at {str(datetime.datetime.now())} hours!')
    return HttpResponse("<h1>Welcome web application development course 2023 (URFI/RTF) :)</h1>")

