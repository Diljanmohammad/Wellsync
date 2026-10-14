"""Train the compact, interpretable models used by the WellSync web app."""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "dataset" / "clean" / "lifestyle_wellbeing_clean.csv"
MODEL_PATH = ROOT / "model" / "wellsync_models.pkl"

FEATURES = [
    "fruits_veggies", "places_visited", "core_circle", "supporting_others",
    "social_network", "achievement", "todo_completed", "flow", "daily_steps",
    "live_vision", "sleep_hours", "lost_vacation", "daily_shouting",
    "sufficient_income", "time_for_passion", "weekly_meditation",
]


def evaluate_models(x_train, x_test, y_train, y_test):
    candidates = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=10.0),
    }
    results = {}
    fitted = {}
    for name, model in candidates.items():
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        results[name] = {
            "r2": round(float(r2_score(y_test, pred)), 4),
            "mae": round(float(mean_absolute_error(y_test, pred)), 4),
        }
        fitted[name] = model
    selected = max(results, key=lambda name: results[name]["r2"])
    return fitted[selected], selected, results


def main():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["daily_stress", "work_life_balance_score"]).copy()
    x = df[FEATURES]
    x_train, x_test, train_idx, test_idx = train_test_split(
        x, df.index, test_size=0.2, random_state=42
    )

    stress_model, stress_name, stress_results = evaluate_models(
        x_train, x_test,
        df.loc[train_idx, "daily_stress"], df.loc[test_idx, "daily_stress"],
    )
    wellbeing_model, wellbeing_name, wellbeing_results = evaluate_models(
        x_train, x_test,
        df.loc[train_idx, "work_life_balance_score"],
        df.loc[test_idx, "work_life_balance_score"],
    )

    numeric = df.select_dtypes(include=np.number)
    correlations = numeric.corr()[["daily_stress", "work_life_balance_score"]].loc[FEATURES]
    summary = {
        "respondents": int(len(df)),
        "average_sleep": round(float(df["sleep_hours"].mean()), 1),
        "average_stress": round(float(df["daily_stress"].mean()), 2),
        "average_wellbeing": round(float(df["work_life_balance_score"].mean()), 1),
        "average_steps_score": round(float(df["daily_steps"].mean()), 1),
        "wellbeing_min": float(df["work_life_balance_score"].min()),
        "wellbeing_max": float(df["work_life_balance_score"].max()),
        "correlations": {
            feature: {
                "stress": round(float(correlations.loc[feature, "daily_stress"]), 3),
                "wellbeing": round(float(correlations.loc[feature, "work_life_balance_score"]), 3),
            } for feature in FEATURES
        },
    }

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump({
        "stress_model": stress_model,
        "wellbeing_model": wellbeing_model,
        "features": FEATURES,
        "stress_selected": stress_name,
        "wellbeing_selected": wellbeing_name,
        "stress_comparison": stress_results,
        "wellbeing_comparison": wellbeing_results,
        "summary": summary,
        "feature_defaults": {feature: float(df[feature].median()) for feature in FEATURES},
        "dataset_source": "Lifestyle and Wellbeing Data by Yash Dalvi (Kaggle)",
    }, MODEL_PATH, compress=3)
    print("Saved", MODEL_PATH)
    print("Stress:", stress_name, stress_results)
    print("Wellbeing:", wellbeing_name, wellbeing_results)


if __name__ == "__main__":
    main()

