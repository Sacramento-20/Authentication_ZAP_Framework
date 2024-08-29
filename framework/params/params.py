import re
from keywords import keywords


def Define_type_authentication(
    zap, parameter_types_found, BASE_URL_LOGIN, request_body
):
    session_parameters = zap.params.params(BASE_URL_LOGIN)
    session_parameters = session_parameters[0]["Parameter"]

    for params in session_parameters:
        name = params.get("name")
        param_type = params.get("type")

        if (
            name in keywords.password_field_identifiers
            and param_type in keywords.parameters_types
        ):
            parameter_types_found[param_type] = 1
            break

    all_zero = all(value == 0 for value in parameter_types_found.values())

    if all_zero:
        r = r"{\s*[^{}]*\s*}"
        if re.search(r, request_body):
            parameter_types_found["json"] = 1

    else:
        pass
