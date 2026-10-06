
import requests


def get_country_info(country_code, cache, api_key):
    """
    Fetch region, currency, and population for a given country code
    from the REST Countries API. Results are cached to avoid making
    duplicate API calls for the same country.
    """
  
    if country_code in cache:
        return cache[country_code]


    default = {"region": "Unknown", "currency": "Unknown", "population": None}

    url = f"https://api.restcountries.com/countries/v5/codes.alpha_2/{country_code}"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            print(f"[{country_code}] Bad response: {response.status_code}")
            cache[country_code] = default
            return default

        payload = response.json()
        objects = payload.get("data", {}).get("objects", [])

  
        if not objects:
            print(f"[{country_code}] No country data returned.")
            cache[country_code] = default
            return default

        country = objects[0]

  
        currencies = country.get("currencies", [])
        currency_code = currencies[0]["code"] if currencies else "Unknown"

        info = {
            "region": country.get("region", "Unknown"),
            "currency": currency_code,
            "population": country.get("population"),
        }
        cache[country_code] = info
        return info

    except requests.exceptions.Timeout:
        print(f"[{country_code}] Request timed out.")
    except requests.exceptions.ConnectionError:
        print(f"[{country_code}] Could not connect to API.")
    except requests.exceptions.RequestException as e:
        print(f"[{country_code}] Request failed: {e}")

    # Any exception falls through to here — cache the default so we don't retry
    cache[country_code] = default
    return default
