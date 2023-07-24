from flask import Flask, request, jsonify

from src.service.entity_service import EntityService

app = Flask(__name__)


@app.route("/entity/historical-rates", methods=["GET"])
def histotical_rates():
    entity_id = request.args.get("entity_id")
    check_in = request.args.get("check_in")

    if not entity_id or not check_in:
        return jsonify({"error": "Debes proporcionar entity_id y check_in"}), 400

    return EntityService().get_historical_rates(entity_id=entity_id, check_in=check_in)


@app.route("/entities/average-rates", methods=["GET"])
def obtener_historico_tarifas():
    pass


if __name__ == "__main__":
    app.run(debug=True)
