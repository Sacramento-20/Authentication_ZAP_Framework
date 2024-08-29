from ruamel.yaml.comments import CommentedMap
from keywords import keywords


def replace_words(
    text,
    login,
    password,
    credential_login="{%username%}",
    credential_password="{%password%}",
):
    if login == password:
        new_request = text.replace(login, credential_login, 1).replace(
            password, credential_password, 1
        )
    else:
        if "%40" in text:
            login = login.replace("@", "%40")
        new_request = text.replace(login, credential_login, 1).replace(
            password, credential_password, 1
        )
    return new_request


def build_yaml(
    context,
    alert_count,
    request_body,
    credential_login,
    credential_password,
    context_name,
    base_url,
    base_url_login,
):

    if alert_count > 0:
        # marcar contexto como auto detect.
        context["env"]["contexts"][0]["sessionManagement"]["method"] = "autodetect"
        print("Gerenciamento de sessão definido como auto detecção")

    request_text = replace_words(request_body, credential_login, credential_password)

    context["env"]["contexts"][0]["authentication"]["parameters"][
        "loginRequestBody"
    ] = request_text

    # Validação de autenticação
    context["env"]["contexts"][0]["authentication"]["verification"][
        "method"
    ] = "autodetect"

    # Usuario
    context["env"]["contexts"][0]["users"][0]["name"] = credential_login
    context["env"]["contexts"][0]["users"][0]["credentials"][
        "password"
    ] = credential_password
    context["env"]["contexts"][0]["users"][0]["credentials"][
        "username"
    ] = credential_login

    context["env"]["contexts"][0]["name"] = context_name
    context["env"]["contexts"][0]["urls"] = base_url
    context["env"]["contexts"][0]["includePaths"] = []
    # autenticação
    context["env"]["contexts"][0]["authentication"]["parameters"][
        "loginPageUrl"
    ] = base_url_login
    context["env"]["contexts"][0]["authentication"]["parameters"][
        "loginRequestUrl"
    ] = base_url_login

    # Criar novas entradas para a verificação logo abaixo de 'method'
    verification_context = context["env"]["contexts"][0]["authentication"][
        "verification"
    ]
    new_verification_entries = CommentedMap()
    new_verification_entries["method"] = "autodetect"

    if keywords.parameter_types_found["form"]:
        context["env"]["contexts"][0]["authentication"]["method"] = "form"

    if keywords.parameter_types_found["json"]:

        new_verification_entries["method"] = "json"

    # Atualizar os dados de verificação com a nova ordem
    context["env"]["contexts"][0]["authentication"][
        "verification"
    ] = new_verification_entries


def update_jobs(jobs, new_context, new_user, new_url):
    for job in jobs:
        if "parameters" in job:
            if "context" in job["parameters"]:
                job["parameters"]["context"] = new_context
            if "user" in job["parameters"]:
                job["parameters"]["user"] = new_user
            if "url" in job["parameters"]:
                job["parameters"]["url"] = new_url
