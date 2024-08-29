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


def main():
    file_name = os.getenv("FILE")
    shared_data_dir = Path("/shared_data")
    # file_name = "orangehrm.json"
    # print(file_name)
    file_path = shared_data_dir/file_name
    # file_path = Path(f"input_data/{file_name}")
    json_data = file_path.read_text()

    # Validando os dados JSON usando model_validate_json
    user = User.model_validate_json(json_data)

    print(user)
    print('\n')

    # --------------------------------------------------- BROWSER CONFIG ---------------------------------------------------
    FIREFOX = os.getenv("FIREFOX")
    ZAP_API_KEY = os.getenv("ZAP_API_KEY")
    ZAP_PROXY_ADDRESS = os.getenv("ZAP_PROXY_ADDRESS")
    ZAP_PROXY_PORT = 8080

    zap = ZAPv2(
        apikey=ZAP_API_KEY,
        proxies={
            "http": f"http://{ZAP_PROXY_ADDRESS}:{ZAP_PROXY_PORT}",
            "https": f"http://{ZAP_PROXY_ADDRESS}:{ZAP_PROXY_PORT}",
        },
    )
    proxyServerUrl = f"{ZAP_PROXY_ADDRESS}:{ZAP_PROXY_PORT}"
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--ignore-certificate-errors")
    firefox_options.add_argument(f"--proxy-server={proxyServerUrl}")
    firefox_options.add_argument("--headless")

    s = Service(FIREFOX)
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("network.proxy.type", 1)
    firefox_profile.set_preference("network.proxy.http", ZAP_PROXY_ADDRESS)
    firefox_profile.set_preference("network.proxy.http_port", ZAP_PROXY_PORT)
    firefox_profile.set_preference("network.proxy.ssl", ZAP_PROXY_ADDRESS)
    firefox_profile.set_preference("network.proxy.ssl_port", ZAP_PROXY_PORT)
    firefox_profile.update_preferences()

    firefox_options.profile = firefox_profile

    # ---------------------- BROWSER CONFIG ----------------------

    """
    Criar uma flag que executa determinado trecho de codigo
    se foi passado a url de login e caso contrário, executa
    outro trecho de codigo.
    """

    """
    0 - url de login não foi passada
    1 - url de login foi passada

    Valor será setado ao verificar se a estrutura 
    em user_data é vazia ou não.
    """
    if user.url_login == "":
        FLAG_LOGIN = 0
        print("url de login não foi setada")
    else:
        FLAG_LOGIN = 1
        print("url de login setada")

    DEFAULT_TIME = 3

    zap.core.new_session(overwrite=True)

    struct_login = []


    driver = webdriver.Firefox(service=s, options=firefox_options)
    if FLAG_LOGIN:
        filtered_dict(driver, user.url_login, struct_login)

        time.sleep(DEFAULT_TIME)

    print(struct_login)
    if FLAG_LOGIN == 0:
        # Primeira url será utilizada para realizar o crawler na página com o spider
        driver.get(user.url[0])

        time.sleep(DEFAULT_TIME)
        scanid = zap.spider.scan(user.url[0])

        time.sleep(DEFAULT_TIME)
        while int(zap.spider.status(scanid)) < 100:
            # Loop until the spider has finished
            print("Spider progress %: {}".format(zap.spider.status(scanid)))
            time.sleep(DEFAULT_TIME)

        print("Spider completed")

        driver.quit()

        urls_found = zap.core.urls()

        print(urls_found)
        general_results = urls_login.find_urls_login(urls_found, keywords.url_words)
        print(general_results)
        evidences_urls_login = []
        for url in general_results:
            if not any(
                re.search(pattern, url) for pattern in keywords.invalid_values_urls
            ):  # match das palavras do array (regex group)
                evidences_urls_login.append(url)

        print(evidences_urls_login)
        for evidence in evidences_urls_login:
            driver = webdriver.Firefox(service=s, options=firefox_options)
            filtered_dict(driver, evidence, struct_login)

        print(struct_login)

    print(len(struct_login))

    # Autenticação
    "-----------------------------------------------------------------------------------------------------------------------------------"

    zap.core.new_session(overwrite=True)

    # Inicializar o driver do Selenium
    # Criar função
    # conteudo da struct login
    driver = webdriver.Firefox(service=s, options=firefox_options)
    if len(struct_login) == 1:
        url_authentication = list(struct_login[0].keys())[0]
        driver.get(url_authentication)
    elif len(struct_login) > 1:
        pass
    else:
        # lançar assert
        pass

    time.sleep(DEFAULT_TIME)

    for authentication_dictionary in struct_login:
        for _, elements in authentication_dictionary.items():
            for type, field in elements.items():
                login_element, password_element = field
                print(login_element, password_element)
                # Encontrar os campos de login e senha (mudar)
                username_field = autentication.find_element_by_attribute(
                    driver, type, login_element
                )
                if username_field is None:
                    continue  # Se não encontrou o campo de username, pula para o próximo elemento
                password_field = autentication.find_element_by_attribute(
                    driver, type, password_element
                )
                if password_field is None:
                    continue  # Se não encontrou o campo de password, pula para o próximo elemento

                username_field.send_keys(user.login)
                password_field.send_keys(user.password)

                time.sleep(DEFAULT_TIME)

                # Tentar enviar o formulário
                try:
                    password_field.send_keys(Keys.RETURN)

                    time.sleep(1)
                    autentication.validate_by_attribute(driver, type, login_element)
                except Exception:
                    pass

                time.sleep(DEFAULT_TIME)
                break

    time.sleep(DEFAULT_TIME)
    # Finalizar o driver
    driver.quit()

    # "-----------------------------------------------------------------------------------------------------------------------------------"

    # Pegar todos os alertas da aplicação
    alerts = zap.alert.alerts()
    print(f'Alerts: {len(alerts)}')
    print(alerts) #se não retornar alerta, lançar assert informando a possibilidade do scan passivo ter parado de funcionar
    # Alertas no momento que o post foi passado, isso inclui as aplicações que foram passadas de forma errada
    # Lembrar que pegar o ultimo ainda é o mais sensato (evitar casos que manda a credencial que queremos, mas de uma forma errada) tem que testar.
    alert_autentication = []
    #  Depurar para encontrar outras formas de identificação de autenticação pelo proxy (rodar pelo UI - getboo, gruyere)
    for alert in alerts:
        if alert["name"] == "Authentication Request Identified":
            # alerta de autenticação
            alert_autentication.append(alert)


    # Pegar os ids de todas as mensagens de autenticação, ou de possiveis autenticação
    messageId = []
    for alert in alert_autentication:
        messageId.append(alert["messageId"])

    # verifica todos os alertas candidatos e filtra o que foi passado as credenciais de forma correta.
    for id in messageId:
        request_autenticated = zap.core.message(id)
        # print(request_autenticated)
        if autentication.check_credentials(
            request_autenticated["requestBody"],
            user.login,
            user.password,
        ):
            print(
                f'O response da aplicação no momento do login é:\n{request_autenticated["requestBody"]}'
            )
            break

    request_body = request_autenticated["requestBody"]

    # Verifica que o zap encontrou o gerenciamento de sessão
    alert_count = len(
        [
            alert
            for alert in alerts
            if alert["name"] == "Session Management Response Identified"
        ]
    )

    BASE_CONTEXT = "base_context/context_base.yaml"

    params.Define_type_authentication(
        zap, keywords.parameter_types_found, url_authentication, request_body
    )

    yaml = YAML()

    with open(BASE_CONTEXT, "r") as file:
        context = yaml.load(file)

    build_yaml(
        context,
        alert_count,
        request_body,
        user.login,
        user.password,
        user.context,
        user.url,
        url_authentication,
    )

    new_context = user.context
    new_user = user.login
    new_url = url_authentication

    # Chama a função para atualizar os valores
    update_jobs(context["jobs"], new_context, new_user, new_url)

    OUTPUT = f"context_{file_name}"

    # Salvar em um novo arquivo YAML
    with open(f"../shared_data/{OUTPUT}.yaml", "w") as file:
        yaml.dump(context, file)

    print("Arquivo YAML modificado e salvo com sucesso !")

    time.sleep(DEFAULT_TIME)

    # mudar para o path da raiz
    output_yaml = f"../shared_data/{OUTPUT}.yaml"
    print(output_yaml)

    scanid = zap.automation.run_plan(output_yaml, ZAP_API_KEY)

    print(f"scanid plano = {scanid}")

    while zap.automation.plan_progress(scanid)["finished"] == "":
        time.sleep(1)

    print(zap.automation.plan_progress(scanid)["finished"])

    # rodar o spider autenticado
    id_context = zap.context.context(user.context)["id"]
    print(f"nome contexto = {user.context} id_context = {id_context}")

    id_user = zap.users.users_list(id_context)[0]["id"]
    print(f"id_user = {id_user}")

    scanid = zap.spider.scan_as_user(id_context, id_user, apikey=ZAP_API_KEY)
    print(f"scanid spider = {scanid}")

    while int(zap.spider.status(scanid)) < 100:
        # Loop until the spider has finished
        print("Spider progress %: {}".format(zap.spider.status(scanid)))
        time.sleep(DEFAULT_TIME)

    time.sleep(1)
    FILE_CONTEXT = f"{user.context}.context"

    # mudar para o path da raiz
    print(
        zap.context.export_context(
            user.context, f"/shared_data/{FILE_CONTEXT}", apikey=ZAP_API_KEY
        )
    )


if __name__ == "__main__":
    main()
