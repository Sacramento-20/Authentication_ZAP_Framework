[
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "",
        "pluginId": "10020",
        "cweid": "1021",
        "confidence": "Medium",
        "wascid": "15",
        "description": "The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.",
        "messageId": "1",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-1021": "https://cwe.mitre.org/data/definitions/1021.html",
            "WSTG-v42-CLNT-09": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/09-Testing_for_Clickjacking",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options",
        "solution": "Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.\nIf you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's \"frame-ancestors\" directive.",
        "alert": "Missing Anti-clickjacking Header",
        "param": "x-frame-options",
        "attack": "",
        "name": "Missing Anti-clickjacking Header",
        "risk": "Medium",
        "id": "0",
        "alertRef": "10020-1",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "",
        "pluginId": "10038",
        "cweid": "693",
        "confidence": "High",
        "wascid": "15",
        "description": "Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.",
        "messageId": "1",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-693": "https://cwe.mitre.org/data/definitions/693.html",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy\nhttps://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html\nhttps://www.w3.org/TR/CSP/\nhttps://w3c.github.io/webappsec-csp/\nhttps://web.dev/articles/csp\nhttps://caniuse.com/#feat=contentsecuritypolicy\nhttps://content-security-policy.com/",
        "solution": "Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.",
        "alert": "Content Security Policy (CSP) Header Not Set",
        "param": "",
        "attack": "",
        "name": "Content Security Policy (CSP) Header Not Set",
        "risk": "Medium",
        "id": "1",
        "alertRef": "10038-1",
    },
    {
        "sourceid": "3",
        "other": 'No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token] was found in the following HTML form: [Form 1: "pw" "uid" ].',
        "method": "GET",
        "evidence": "<form method='get' action='/1142014131/login'>",
        "pluginId": "10202",
        "cweid": "352",
        "confidence": "Low",
        "wascid": "9",
        "description": "No Anti-CSRF tokens were found in a HTML submission form.\nA cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.\n\nCSRF attacks are effective in a number of situations, including:\n    * The victim has an active session on the target site.\n    * The victim is authenticated via HTTP auth on the target site.\n    * The victim is on the same local network as the target site.\n\nCSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.",
        "messageId": "1",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login",
        "tags": {
            "OWASP_2021_A01": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
            "WSTG-v42-SESS-05": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery",
            "OWASP_2017_A05": "https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html",
            "CWE-352": "https://cwe.mitre.org/data/definitions/352.html",
        },
        "reference": "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html\nhttps://cwe.mitre.org/data/definitions/352.html",
        "solution": "Phase: Architecture and Design\nUse a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.\nFor example, use anti-CSRF packages such as the OWASP CSRFGuard.\n\nPhase: Implementation\nEnsure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.\n\nPhase: Architecture and Design\nGenerate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).\nNote that this can be bypassed using XSS.\n\nIdentify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.\nNote that this can be bypassed using XSS.\n\nUse the ESAPI Session Management control.\nThis control includes a component for CSRF.\n\nDo not use the GET method for any request that triggers a state change.\n\nPhase: Implementation\nCheck the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.",
        "alert": "Absence of Anti-CSRF Tokens",
        "param": "",
        "attack": "",
        "name": "Absence of Anti-CSRF Tokens",
        "risk": "Medium",
        "id": "2",
        "alertRef": "10202",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "BaseHTTP/0.3 Python/2.6.5",
        "pluginId": "10036",
        "cweid": "200",
        "confidence": "High",
        "wascid": "13",
        "description": 'The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.',
        "messageId": "1",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
            "WSTG-v42-INFO-02": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server",
            "CWE-200": "https://cwe.mitre.org/data/definitions/200.html",
        },
        "reference": "https://httpd.apache.org/docs/current/mod/core.html#servertokens\nhttps://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10)\nhttps://www.troyhunt.com/shhh-dont-let-your-response-headers/",
        "solution": 'Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.',
        "alert": 'Server Leaks Version Information via "Server" HTTP Response Header Field',
        "param": "",
        "attack": "",
        "name": 'Server Leaks Version Information via "Server" HTTP Response Header Field',
        "risk": "Low",
        "id": "3",
        "alertRef": "10036",
    },
    {
        "sourceid": "3",
        "other": 'This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.\nAt "High" threshold this scan rule will not alert on client or server error responses.',
        "method": "GET",
        "evidence": "",
        "pluginId": "10021",
        "cweid": "693",
        "confidence": "Medium",
        "wascid": "15",
        "description": "The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.",
        "messageId": "1",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-693": "https://cwe.mitre.org/data/definitions/693.html",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85)\nhttps://owasp.org/www-community/Security_Headers",
        "solution": "Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.\nIf possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.",
        "alert": "X-Content-Type-Options Header Missing",
        "param": "x-content-type-options",
        "attack": "",
        "name": "X-Content-Type-Options Header Missing",
        "risk": "Low",
        "id": "4",
        "alertRef": "10021",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "",
        "pluginId": "10020",
        "cweid": "1021",
        "confidence": "Medium",
        "wascid": "15",
        "description": "The response does not include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options to protect against 'ClickJacking' attacks.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-1021": "https://cwe.mitre.org/data/definitions/1021.html",
            "WSTG-v42-CLNT-09": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/09-Testing_for_Clickjacking",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options",
        "solution": "Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.\nIf you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's \"frame-ancestors\" directive.",
        "alert": "Missing Anti-clickjacking Header",
        "param": "x-frame-options",
        "attack": "",
        "name": "Missing Anti-clickjacking Header",
        "risk": "Medium",
        "id": "5",
        "alertRef": "10020-1",
    },
    {
        "sourceid": "3",
        "other": "The following pattern was used: \\bUSER\\b and was detected in the element starting with: \" * Processes refresh response {'private_snippet':snippet, user:snippet, ...}\", see evidence field for the suspicious comment/snippet.",
        "method": "GET",
        "evidence": "user",
        "pluginId": "10027",
        "cweid": "200",
        "confidence": "Low",
        "wascid": "13",
        "description": "The response appears to contain suspicious comments which may help an attacker. Note: Matches made within script blocks or files are against the entire content not only comments.",
        "messageId": "7",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/lib.js",
        "tags": {
            "OWASP_2021_A01": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
            "WSTG-v42-INFO-05": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Webpage_Content_for_Information_Leakage",
            "OWASP_2017_A03": "https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure.html",
            "CWE-200": "https://cwe.mitre.org/data/definitions/200.html",
        },
        "reference": "",
        "solution": "Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.",
        "alert": "Information Disclosure - Suspicious Comments",
        "param": "",
        "attack": "",
        "name": "Information Disclosure - Suspicious Comments",
        "risk": "Informational",
        "id": "6",
        "alertRef": "10027",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "BaseHTTP/0.3 Python/2.6.5",
        "pluginId": "10036",
        "cweid": "200",
        "confidence": "High",
        "wascid": "13",
        "description": 'The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.',
        "messageId": "7",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/lib.js",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
            "WSTG-v42-INFO-02": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server",
            "CWE-200": "https://cwe.mitre.org/data/definitions/200.html",
        },
        "reference": "https://httpd.apache.org/docs/current/mod/core.html#servertokens\nhttps://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10)\nhttps://www.troyhunt.com/shhh-dont-let-your-response-headers/",
        "solution": 'Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.',
        "alert": 'Server Leaks Version Information via "Server" HTTP Response Header Field',
        "param": "",
        "attack": "",
        "name": 'Server Leaks Version Information via "Server" HTTP Response Header Field',
        "risk": "Low",
        "id": "7",
        "alertRef": "10036",
    },
    {
        "sourceid": "3",
        "other": 'This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.\nAt "High" threshold this scan rule will not alert on client or server error responses.',
        "method": "GET",
        "evidence": "",
        "pluginId": "10021",
        "cweid": "693",
        "confidence": "Medium",
        "wascid": "15",
        "description": "The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.",
        "messageId": "7",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/lib.js",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-693": "https://cwe.mitre.org/data/definitions/693.html",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85)\nhttps://owasp.org/www-community/Security_Headers",
        "solution": "Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.\nIf possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.",
        "alert": "X-Content-Type-Options Header Missing",
        "param": "x-content-type-options",
        "attack": "",
        "name": "X-Content-Type-Options Header Missing",
        "risk": "Low",
        "id": "8",
        "alertRef": "10021",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "",
        "pluginId": "10038",
        "cweid": "693",
        "confidence": "High",
        "wascid": "15",
        "description": "Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-693": "https://cwe.mitre.org/data/definitions/693.html",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy\nhttps://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html\nhttps://www.w3.org/TR/CSP/\nhttps://w3c.github.io/webappsec-csp/\nhttps://web.dev/articles/csp\nhttps://caniuse.com/#feat=contentsecuritypolicy\nhttps://content-security-policy.com/",
        "solution": "Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.",
        "alert": "Content Security Policy (CSP) Header Not Set",
        "param": "",
        "attack": "",
        "name": "Content Security Policy (CSP) Header Not Set",
        "risk": "Medium",
        "id": "9",
        "alertRef": "10038-1",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "Set-Cookie: GRUYERE",
        "pluginId": "10010",
        "cweid": "1004",
        "confidence": "Medium",
        "wascid": "13",
        "description": "A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "CWE-1004": "https://cwe.mitre.org/data/definitions/1004.html",
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "WSTG-v42-SESS-02": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://owasp.org/www-community/HttpOnly",
        "solution": "Ensure that the HttpOnly flag is set for all cookies.",
        "alert": "Cookie No HttpOnly Flag",
        "param": "GRUYERE",
        "attack": "",
        "name": "Cookie No HttpOnly Flag",
        "risk": "Low",
        "id": "10",
        "alertRef": "10010",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "Set-Cookie: GRUYERE",
        "pluginId": "10054",
        "cweid": "1275",
        "confidence": "Medium",
        "wascid": "13",
        "description": "A cookie has been set without the SameSite attribute, which means that the cookie can be sent as a result of a 'cross-site' request. The SameSite attribute is an effective counter measure to cross-site request forgery, cross-site script inclusion, and timing attacks.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "OWASP_2021_A01": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
            "WSTG-v42-SESS-02": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/02-Testing_for_Cookies_Attributes",
            "CWE-1275": "https://cwe.mitre.org/data/definitions/1275.html",
            "OWASP_2017_A05": "https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html",
        },
        "reference": "https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site",
        "solution": "Ensure that the SameSite attribute is set to either 'lax' or ideally 'strict' for all cookies.",
        "alert": "Cookie without SameSite Attribute",
        "param": "GRUYERE",
        "attack": "",
        "name": "Cookie without SameSite Attribute",
        "risk": "Low",
        "id": "11",
        "alertRef": "10054-1",
    },
    {
        "sourceid": "3",
        "other": "Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.",
        "method": "GET",
        "evidence": "<a class='button' onclick='_refreshHome(\"1142014131\")' href='#'>Refresh</a>",
        "pluginId": "10109",
        "cweid": "-1",
        "confidence": "Medium",
        "wascid": "-1",
        "description": "The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {},
        "reference": "",
        "solution": "This is an informational alert and so no changes are required.",
        "alert": "Modern Web Application",
        "param": "",
        "attack": "",
        "name": "Modern Web Application",
        "risk": "Informational",
        "id": "12",
        "alertRef": "10109",
    },
    {
        "sourceid": "3",
        "other": "",
        "method": "GET",
        "evidence": "BaseHTTP/0.3 Python/2.6.5",
        "pluginId": "10036",
        "cweid": "200",
        "confidence": "High",
        "wascid": "13",
        "description": 'The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.',
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
            "WSTG-v42-INFO-02": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server",
            "CWE-200": "https://cwe.mitre.org/data/definitions/200.html",
        },
        "reference": "https://httpd.apache.org/docs/current/mod/core.html#servertokens\nhttps://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10)\nhttps://www.troyhunt.com/shhh-dont-let-your-response-headers/",
        "solution": 'Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.',
        "alert": 'Server Leaks Version Information via "Server" HTTP Response Header Field',
        "param": "",
        "attack": "",
        "name": 'Server Leaks Version Information via "Server" HTTP Response Header Field',
        "risk": "Low",
        "id": "13",
        "alertRef": "10036",
    },
    {
        "sourceid": "3",
        "other": "An attacker may be able to poison cookie values through URL parameters. Try injecting a semicolon to see if you can add cookie values (e.g. name=controlledValue;name=anotherValue;).\n\nThis was identified at:\n\nhttp://192.168.15.95/1142014131/login?uid=admin&pw=admin\n\nUser-input was found in the following cookie:\nGRUYERE=98793808|admin||author; path=/\n\nThe user input was:\npw=admin",
        "method": "GET",
        "evidence": "",
        "pluginId": "10029",
        "cweid": "565",
        "confidence": "Low",
        "wascid": "20",
        "description": "This check looks at user-supplied input in query string parameters and POST data to identify where cookie parameters might be controlled. This is called a cookie poisoning attack, and becomes exploitable when an attacker can manipulate the cookie in various ways. In some cases this will not be exploitable, however, allowing URL parameters to set cookie values is generally considered a bug.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "CWE-565": "https://cwe.mitre.org/data/definitions/565.html",
            "OWASP_2021_A03": "https://owasp.org/Top10/A03_2021-Injection/",
            "OWASP_2017_A01": "https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html",
        },
        "reference": "https://en.wikipedia.org/wiki/HTTP_cookie\nhttps://cwe.mitre.org/data/definitions/565.html",
        "solution": "Do not allow user input to control cookie names and values. If some query string parameters must be set in cookie values, be sure to filter out semicolon's that can serve as name/value pair delimiters.",
        "alert": "Cookie Poisoning",
        "param": "pw",
        "attack": "",
        "name": "Cookie Poisoning",
        "risk": "Informational",
        "id": "14",
        "alertRef": "10029",
    },
    {
        "sourceid": "3",
        "other": "An attacker may be able to poison cookie values through URL parameters. Try injecting a semicolon to see if you can add cookie values (e.g. name=controlledValue;name=anotherValue;).\n\nThis was identified at:\n\nhttp://192.168.15.95/1142014131/login?uid=admin&pw=admin\n\nUser-input was found in the following cookie:\nGRUYERE=98793808|admin||author; path=/\n\nThe user input was:\nuid=admin",
        "method": "GET",
        "evidence": "",
        "pluginId": "10029",
        "cweid": "565",
        "confidence": "Low",
        "wascid": "20",
        "description": "This check looks at user-supplied input in query string parameters and POST data to identify where cookie parameters might be controlled. This is called a cookie poisoning attack, and becomes exploitable when an attacker can manipulate the cookie in various ways. In some cases this will not be exploitable, however, allowing URL parameters to set cookie values is generally considered a bug.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "CWE-565": "https://cwe.mitre.org/data/definitions/565.html",
            "OWASP_2021_A03": "https://owasp.org/Top10/A03_2021-Injection/",
            "OWASP_2017_A01": "https://owasp.org/www-project-top-ten/2017/A1_2017-Injection.html",
        },
        "reference": "https://en.wikipedia.org/wiki/HTTP_cookie\nhttps://cwe.mitre.org/data/definitions/565.html",
        "solution": "Do not allow user input to control cookie names and values. If some query string parameters must be set in cookie values, be sure to filter out semicolon's that can serve as name/value pair delimiters.",
        "alert": "Cookie Poisoning",
        "param": "uid",
        "attack": "",
        "name": "Cookie Poisoning",
        "risk": "Informational",
        "id": "15",
        "alertRef": "10029",
    },
    {
        "sourceid": "3",
        "other": 'This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.\nAt "High" threshold this scan rule will not alert on client or server error responses.',
        "method": "GET",
        "evidence": "",
        "pluginId": "10021",
        "cweid": "693",
        "confidence": "Medium",
        "wascid": "15",
        "description": "The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "CWE-693": "https://cwe.mitre.org/data/definitions/693.html",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
        },
        "reference": "https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85)\nhttps://owasp.org/www-community/Security_Headers",
        "solution": "Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.\nIf possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.",
        "alert": "X-Content-Type-Options Header Missing",
        "param": "x-content-type-options",
        "attack": "",
        "name": "X-Content-Type-Options Header Missing",
        "risk": "Low",
        "id": "16",
        "alertRef": "10021",
    },
    {
        "sourceid": "3",
        "other": "\ncookie:GRUYERE",
        "method": "GET",
        "evidence": "98793808|admin||author",
        "pluginId": "10112",
        "cweid": "-1",
        "confidence": "Medium",
        "wascid": "-1",
        "description": "The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to \"Auto-Detect\" then this rule will change the session management to use the tokens identified.",
        "messageId": "6",
        "inputVector": "",
        "url": "http://192.168.15.95/1142014131/login?uid=admin&pw=admin",
        "tags": {},
        "reference": "https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id",
        "solution": "This is an informational alert rather than a vulnerability and so there is nothing to fix.",
        "alert": "Session Management Response Identified",
        "param": "GRUYERE",
        "attack": "",
        "name": "Session Management Response Identified",
        "risk": "Informational",
        "id": "17",
        "alertRef": "10112",
    },
]
