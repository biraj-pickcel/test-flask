from flask import request


def ask():
    try:
        data = request.get_json()
    except:
        return {"success": False, "message": "provide a valid json"}

    query = data.get("query")
    if not query:
        return {"success": False, "message": "provide a query"}, 400

    return {"success": True, "message": f"you asked: {query}"}
