from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import re
from keywords import keywords

DEFAULT_TIME = 3
password_regex = r'\b[\w.-]*password[\w.-]*\b'

def find_password(element):
    return any(re.search(password_regex, str(value), re.IGNORECASE) for _, value in element.items())


def filtered_dict(driver, evidence, struct_login):
    # driver = webdriver.Firefox(service=s, options=firefox_options)
    driver.get(evidence)
    # pegar os elementos
    time.sleep(DEFAULT_TIME)
    elements = driver.find_elements(By.XPATH, "//*")

    # leve macro para burlar aplicações com uma janela de pop-up
    if not elements:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        elements = driver.find_elements(By.XPATH, "//*")

    array_elements = []

    for element in elements:
        element_info = {}
        try:
            attributes_to_gather = [
                ("name", element.get_attribute("name")),
                ("type", element.get_attribute("type")),
                ("placeholder", element.get_attribute("placeholder")),
                ("id", element.get_attribute("id")),
            ]
            element_info = {key: value for key, value in attributes_to_gather if value}
        except NoSuchAttributeException:
            pass

        if element_info:
            array_elements.append(element_info)

    print(array_elements)
    print("\n")
    # regex match
    # Filtrando os dicionários
    filtered_dictionaries = []
    for d in array_elements:
        for _, value in d.items():
            # Verifica se o valor corresponde à regex
            for regex in keywords.valid_values_elements:
                if re.search(regex, value):
                    # se a correspondencia do elemento não estiver no dicionário, adicionar
                    if d not in filtered_dictionaries:
                        filtered_dictionaries.append(d)
                    break

    print(filtered_dictionaries)

    # Se após a filtragem o dicionario possuir elementos, criar as tuplas para usar na autenticação.
    if filtered_dictionaries != []:
        
        if len(filtered_dictionaries) > 2:
            login = []
            for index, element in enumerate(filtered_dictionaries):
                if find_password(element):
                    if (filtered_dictionaries[index-1] in login):
                        pass
                    else:
                        login.append(filtered_dictionaries[index-1])
                    if (element in login):
                        pass
                    else:
                        login.append(element)
            filtered_dictionaries = login

        authentication_data = {
            # palavras reservadas em italico
            "name": tuple(element.get("name", "") for element in filtered_dictionaries),
            "type": tuple(element.get("type", "") for element in filtered_dictionaries),
            "placeholder": tuple(
                element.get("placeholder", "") for element in filtered_dictionaries
            ),
        }

        dicionario_autenticado = {evidence: authentication_data}
        struct_login.append(dicionario_autenticado)

    driver.quit()
