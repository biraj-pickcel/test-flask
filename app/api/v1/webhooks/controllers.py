from app.helpers.apify import digest_apify_dataset


def apify():
    try:
        digest_apify_dataset("some_id")
        return {"success": True, "message": "apify webhook received"}
    except Exception as e:
        print(e)
        return {"success": False, "message": "internal server error"}, 500
