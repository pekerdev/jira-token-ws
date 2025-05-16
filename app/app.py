import os
from flask import Flask, request, abort

app = Flask(__name__)

EXPECTED_BEARER_TOKEN = os.environ.get("EXPECTED_BEARER_TOKEN", "")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

@app.route("/api/jira-token", methods=["GET"])
def get_jira_token():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        abort(401, description="Token no provisto.")

    token_recibido = auth_header.replace("Bearer ", "").strip()
    if token_recibido != EXPECTED_BEARER_TOKEN:
        abort(403, description="Token inválido.")

    if not JIRA_API_TOKEN:
        abort(500, description="Token de Jira no configurado.")

    return JIRA_API_TOKEN, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
