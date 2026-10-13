from flask import Flask, jsonify, request

app = Flask(__name__)

members = {}
next_member_id = 1


@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "status": "running",
        "version": "1.0"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(list(members.values())), 200


@app.route("/members", methods=["POST"])
def add_member():
    global next_member_id

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "JSON request body required"}), 400

    name = data.get("name")
    plan = data.get("plan")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "A valid name is required"}), 400

    if not isinstance(plan, str) or not plan.strip():
        return jsonify({"error": "A valid plan is required"}), 400

    member = {
        "id": next_member_id,
        "name": name.strip(),
        "plan": plan.strip()
    }

    members[next_member_id] = member
    next_member_id += 1

    return jsonify(member), 201


@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = members.get(member_id)

    if member is None:
        return jsonify({"error": "Member not found"}), 404

    return jsonify(member), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
