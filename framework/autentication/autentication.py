from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def find_element_by_attribute(driver, attribute, value):
    """
    Encontra um elemento no site com base no atributo especificado.
    """
    try:
        if attribute == "name":
            element = driver.find_element(By.NAME, value)
        elif attribute == "type":
            element = driver.find_element(By.CSS_SELECTOR, f"input[type='{value}']")
        elif attribute == "placeholder":
            element = driver.find_element(
                By.CSS_SELECTOR, f"input[placeholder='{value}']"
            )
        else:
            raise ValueError(f"Atributo inválido: {attribute}")
        print(f"Elemento encontrado com sucesso.")
        return element
    except NoSuchElementException:
        print(f"Elemento não encontrado com base no atributo '{attribute}'.")
        return None


# Função para validar se o elemento está visível
def validate_by_attribute(driver, attribute, value):
    try:
        if attribute == "name":
            if driver.find_element(By.NAME, value).is_displayed():
                pass
        elif attribute == "type":
            if driver.find_element(
                By.CSS_SELECTOR, f"input[type='{value}']"
            ).is_displayed():
                pass
        elif attribute == "placeholder":
            if driver.find_element(
                By.CSS_SELECTOR, f"input[placeholder='{value}']"
            ).is_displayed():
                pass
        print("failed to log in !")
        driver.refresh()
        return
    except:
        print("login done !")


def check_credentials(request, credencial_login, credencial_passsword):

    # Verifica os casos em que o login e senha são iguais (admin, admin)
    if credencial_login == credencial_passsword:
        # Conta o número de ocorrências da palavra no texto
        return request.count(credencial_login) >= 2
    else:
        # Verifica se ambas as palavras estão presentes no texto
        return credencial_login in request and credencial_passsword in request
