from twocaptcha import TwoCaptcha

def solveCaptcha(api_key, site_key, url):
    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey=site_key,
            url=url
        )
    except Exception as e:
        print(e)
    else:
        return result["code"]
