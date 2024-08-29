from context.context import build_yaml, update_jobs
from user_data.user_data import User
from urls_login import urls_login
from elements.elements import filtered_dict
from keywords import keywords
from autentication import autentication
from params import params
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
from zapv2 import ZAPv2
from ruamel.yaml import YAML
from pathlib import Path
import re

FIREFOX = os.getenv("FIREFOX")
ZAP_API_KEY = os.getenv("ZAP_API_KEY")
ZAP_PROXY_ADDRESS = os.getenv("ZAP_PROXY_ADDRESS")
ZAP_PROXY_PORT = 8080

contexto = "Default Context"

zap = ZAPv2(
    apikey=ZAP_API_KEY,
    proxies={
        "http": f"http://{ZAP_PROXY_ADDRESS}:{ZAP_PROXY_PORT}",
        "https": f"http://{ZAP_PROXY_ADDRESS}:{ZAP_PROXY_PORT}",
    },
)
# print(zap.context.new_context(contexto))
print(zap.context.context_list)

print(
        zap.context.export_context(
            contexto, f"/shared_data/{contexto}.context", apikey=ZAP_API_KEY
        )
    )