from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request


ROOT = Path(__file__).resolve().parent
bundle = joblib.load(ROOT / "model" / "wellsync_models.pkl")
FEATURES = bundle["features"]

app = Flask(__name__)

RANGES = {
    "fruits_veggies": (0, 5), "places_visited": (0, 10), "core_circle": (0, 10),
    "supporting_others": (0, 10), "social_network": (0, 10), "achievement": (0, 10),
    "todo_completed": (0, 10), "flow": (0, 10), "daily_steps": (1, 10),
    "live_vision": (0, 10), "sleep_hours": (1, 10), "lost_vacation": (0, 10),
    "daily_shouting": (0, 10), "sufficient_income": (1, 2),
    "time_for_passion": (0, 10), "weekly_meditation": (0, 10),
}


def parse_payload(payload):
    values, errors = [], {}
    for feature in FEATURES:
        try:
            value = float(payload.get(feature, bundle["feature_defaults"][feature]))
            low, high = RANGES[feature]
            if not low <= value <= high:
                errors[feature] = f"Value must be between {low} and {high}."
            values.append(value)
        except (TypeError, ValueError):
            errors[feature] = "Enter a valid number."
            values.append(bundle["feature_defaults"][feature])
    return values, errors


def stress_band(score):
    if score < 1.8:
        return "Low", "calm"
    if score < 3.4:
        return "Moderate", "balanced"
    return "High", "attention"


def suggestions(data):
    checks = [
        (data["sleep_hours"] < 7, "Sleep", "Aim for a consistent seven to eight hour sleep window."),
        (data["weekly_meditation"] < 4, "Mindfulness", "Add short mindfulness sessions on four days each week."),
        (data["daily_steps"] < 6, "Movement", "Increase daily movement gradually through walks or active breaks."),
        (data["social_network"] < 5, "Connection", "Schedule regular time with supportive friends or family."),
        (data["time_for_passion"] < 4, "Personal time", "Reserve weekly time for an activity you genuinely enjoy."),
        (data["lost_vacation"] > 5, "Recovery", "Plan protected time away from work or study commitments."),
        (data["daily_shouting"] > 4, "Stress response", "Use a pause routine before reacting during stressful moments."),
        (data["fruits_veggies"] < 3, "Nutrition", "Add another serving of fruit or vegetables to your routine."),
    ]
    result = [{"area": area, "action": action} for failed, area, action in checks if failed]
    return result[:4] or [{"area": "Maintenance", "action": "Your inputs show balanced habits; focus on consistency."}]


@app.get("/")
def home():
    return render_template("index.html", summary=bundle["summary"])


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "product": "WellSync Analytics"})


@app.get("/api/insights")
def insights():
    return jsonify(bundle["summary"])


@app.post("/api/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    values, errors = parse_payload(payload)
    if errors:
        return jsonify({"errors": errors}), 400

    row = pd.DataFrame([values], columns=FEATURES)
    stress = float(np.clip(bundle["stress_model"].predict(row)[0], 0, 5))
    wellbeing = float(np.clip(bundle["wellbeing_model"].predict(row)[0], 480, 820.2))
    band, tone = stress_band(stress)
    data = dict(zip(FEATURES, values))
    percentile = round(100 * (wellbeing - 480) / (820.2 - 480))

    return jsonify({
        "stress_score": round(stress, 2),
        "stress_band": band,
        "tone": tone,
        "wellbeing_score": round(wellbeing, 1),
        "wellbeing_percentile": int(np.clip(percentile, 0, 100)),
        "recommendations": suggestions(data),
        "disclaimer": "Educational estimate from self-reported survey patterns; not a medical diagnosis.",
    })


if __name__ == "__main__":
    app.run(debug=True)
