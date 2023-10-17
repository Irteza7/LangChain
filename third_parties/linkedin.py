import requests
from config import settings


def scrape_linkedin_profile(linkdin_url):
    """Scrape information from LinkedIn profiles,
    Manually scrape information from LinkedIn profile"""

    api_key = settings.proxycurl_api
    headers = {"Authorization": "Bearer " + api_key}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    params = {"linkedin_profile_url": linkdin_url, "use_cache": "if-recent"}

    response = requests.get(api_endpoint, params=params, headers=headers)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", "null", "None", None)
        and k
        not in [
            "people_also_viewed",
            "certifications",
            "similarly_named_profiles",
            "profile_pic_url",
        ]
    }

    # Removing fields with values of 'None' and URL fields from each dictionary
    if "experiences" in data:
        for experience in data["experiences"]:
            # Removing keys with 'None' values
            keys_to_remove = [
                key for key, value in experience.items() if value == "None"
            ]
            for key in keys_to_remove:
                experience.pop(key, None)

            # Removing URL fields
            experience.pop("logo_url", None)
            experience.pop("company_linkedin_profile_url", None)

    if "education" in data:
        for edu in data["education"]:
            # Removing keys with 'None' values
            keys_to_remove = [key for key, value in edu.items() if value == "None"]
            for key in keys_to_remove:
                edu.pop(key, None)

            # Removing URL fields
            edu.pop("school_linkedin_profile_url", None)
            edu.pop("logo_url", None)

    if "accomplishment_projects" in data:
        for projects in data["accomplishment_projects"]:
            # Removing keys with 'None' values
            keys_to_remove = [key for key, value in projects.items() if value == "None"]
            for key in keys_to_remove:
                projects.pop(key, None)

            # Removing URL fields
            projects.pop("url", None)

    if data.get("groups"):
        for groups_dict in data.get("groups"):
            groups_dict.pop("profile_pic_url", None)

    return data


def scrape_linkedin_profile_gist(gist_url):
    """Scrape information from LinkedIn profiles,
    Manually scrape information from LinkedIn profile"""

    response = requests.get(gist_url)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None, "null", "None")
        and k
        not in [
            "people_also_viewed",
            "certifications",
            "similarly_named_profiles",
            "profile_pic_url",
        ]
    }

    # Removing fields with values of 'None' and URL fields from each dictionary
    if "experiences" in data:
        for experience in data["experiences"]:
            # Removing keys with 'None' values
            keys_to_remove = [
                key for key, value in experience.items() if value == "None"
            ]
            for key in keys_to_remove:
                experience.pop(key, None)

            # Removing URL fields
            experience.pop("logo_url", None)
            experience.pop("company_linkedin_profile_url", None)

    if "education" in data:
        for edu in data["education"]:
            # Removing keys with 'None' values
            keys_to_remove = [key for key, value in edu.items() if value == "None"]
            for key in keys_to_remove:
                edu.pop(key, None)

            # Removing URL fields
            edu.pop("school_linkedin_profile_url", None)
            edu.pop("logo_url", None)

    if "accomplishment_projects" in data:
        for projects in data["accomplishment_projects"]:
            # Removing keys with 'None' values
            keys_to_remove = [key for key, value in projects.items() if value == "None"]
            for key in keys_to_remove:
                projects.pop(key, None)

            # Removing URL fields
            projects.pop("url", None)

    if data.get("groups"):
        for groups_dict in data.get("groups"):
            groups_dict.pop("profile_pic_url", None)

    return data
