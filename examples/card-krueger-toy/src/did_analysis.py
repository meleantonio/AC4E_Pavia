"""Synthetic difference-in-differences example for the Pavia workshop."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "toy_fast_food.csv"
REQUIRED_COLUMNS = {"store_id", "state", "wave", "fte_employment"}
EXPECTED_STATES = {"NJ", "PA"}
EXPECTED_WAVES = {"before", "after"}


@dataclass(frozen=True)
class DidResult:
    """Compact difference-in-differences result for the toy example."""

    nj_change: float
    pa_change: float
    did: float
    observations: int
    treated_stores: int
    comparison_stores: int


def load_fast_food_data(csv_path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the synthetic fast-food panel and add teaching indicators."""

    data = pd.read_csv(csv_path)
    missing = REQUIRED_COLUMNS - set(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

    if data[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Dataset contains missing values in required columns")

    invalid_states = set(data["state"]) - EXPECTED_STATES
    if invalid_states:
        raise ValueError(f"Unexpected states: {sorted(invalid_states)}")

    invalid_waves = set(data["wave"]) - EXPECTED_WAVES
    if invalid_waves:
        raise ValueError(f"Unexpected waves: {sorted(invalid_waves)}")

    cleaned = data.copy()
    cleaned["post"] = (cleaned["wave"] == "after").astype(int)
    cleaned["treated"] = (cleaned["state"] == "NJ").astype(int)
    return cleaned.sort_values(["state", "store_id", "post"]).reset_index(drop=True)


def validate_balanced_panel(data: pd.DataFrame) -> None:
    """Check that each store has one before and one after observation."""

    duplicated_rows = data.duplicated(["store_id", "wave"])
    if duplicated_rows.any():
        duplicated = sorted(data.loc[duplicated_rows, "store_id"].unique())
        raise ValueError(f"Duplicate store-wave observations: {duplicated}")

    unbalanced = [
        store_id
        for store_id, waves in data.groupby("store_id")["wave"].agg(set).items()
        if waves != EXPECTED_WAVES
    ]
    if unbalanced:
        raise ValueError(f"Stores without a before/after pair: {sorted(unbalanced)}")

    changing_state = data.groupby("store_id")["state"].nunique()
    bad_state = sorted(changing_state[changing_state != 1].index)
    if bad_state:
        raise ValueError(f"Stores assigned to multiple states: {bad_state}")


def make_group_means(data: pd.DataFrame) -> pd.DataFrame:
    """Return mean full-time-equivalent employment by state and wave."""

    validate_balanced_panel(data)
    means = (
        data.groupby(["state", "wave"], as_index=False)["fte_employment"]
        .mean()
        .rename(columns={"fte_employment": "mean_fte_employment"})
    )
    means["wave_order"] = means["wave"].map({"before": 0, "after": 1})
    return means.sort_values(["state", "wave_order"]).drop(columns="wave_order")


def _mean_for(data: pd.DataFrame, state: str, wave: str) -> float:
    mask = (data["state"] == state) & (data["wave"] == wave)
    return float(data.loc[mask, "fte_employment"].mean())


def estimate_difference_in_differences(data: pd.DataFrame) -> DidResult:
    """Estimate the simple NJ-versus-PA before/after comparison."""

    validate_balanced_panel(data)

    nj_change = _mean_for(data, "NJ", "after") - _mean_for(data, "NJ", "before")
    pa_change = _mean_for(data, "PA", "after") - _mean_for(data, "PA", "before")

    return DidResult(
        nj_change=nj_change,
        pa_change=pa_change,
        did=nj_change - pa_change,
        observations=len(data),
        treated_stores=int(data.loc[data["state"] == "NJ", "store_id"].nunique()),
        comparison_stores=int(data.loc[data["state"] == "PA", "store_id"].nunique()),
    )


def render_replication_note(result: DidResult) -> str:
    """Document source, transformations, units, restrictions, and caveats."""

    return "\n".join(
        [
            "# Card-Krueger Toy Example",
            "",
            "Data source: synthetic teaching CSV in examples/card-krueger-toy/data/toy_fast_food.csv.",
            "Unit: store-wave observation; employment is full-time-equivalent workers.",
            "Sample restriction: stores with one before and one after observation in NJ or PA.",
            "Transformation: created treated and post indicators and compared mean changes.",
            f"NJ change: {result.nj_change:.1f} FTE workers.",
            f"PA change: {result.pa_change:.1f} FTE workers.",
            f"Toy DID estimate: {result.did:.1f} FTE workers.",
            "Research caveat: this is not Card and Krueger's raw data and does not certify a causal claim.",
        ]
    )


def main() -> None:
    """Run the toy analysis and print a compact replication note."""

    data = load_fast_food_data()
    means = make_group_means(data)
    result = estimate_difference_in_differences(data)

    print("Group means")
    print("===========")
    print(means.to_string(index=False))
    print()
    print(render_replication_note(result))


if __name__ == "__main__":
    main()
