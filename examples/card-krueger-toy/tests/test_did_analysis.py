from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest


from did_analysis import (
    DEFAULT_DATA_PATH,
    estimate_difference_in_differences,
    load_fast_food_data,
    make_group_means,
    render_replication_note,
    validate_balanced_panel,
)


def test_load_fast_food_data_adds_teaching_indicators() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)

    assert len(data) == 24
    assert {"post", "treated"}.issubset(data.columns)
    assert set(data["state"]) == {"NJ", "PA"}
    assert set(data["wave"]) == {"before", "after"}


def test_validate_balanced_panel_rejects_missing_wave() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)
    incomplete = data.loc[~((data["store_id"] == "NJ01") & (data["wave"] == "after"))]

    with pytest.raises(ValueError, match="before/after pair"):
        validate_balanced_panel(incomplete)


def test_make_group_means_reports_expected_cells() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)
    means = make_group_means(data)

    assert len(means) == 4
    nj_before = means.loc[
        (means["state"] == "NJ") & (means["wave"] == "before"), "mean_fte_employment"
    ].iloc[0]
    pa_after = means.loc[
        (means["state"] == "PA") & (means["wave"] == "after"), "mean_fte_employment"
    ].iloc[0]

    assert nj_before == pytest.approx(23.3333333333)
    assert pa_after == pytest.approx(23.0)


def test_estimate_difference_in_differences_returns_known_toy_result() -> None:
    data = load_fast_food_data(DEFAULT_DATA_PATH)
    result = estimate_difference_in_differences(data)

    assert result.observations == 24
    assert result.treated_stores == 6
    assert result.comparison_stores == 6
    assert result.nj_change == pytest.approx(2.0)
    assert result.pa_change == pytest.approx(-1.0)
    assert result.did == pytest.approx(3.0)


def test_render_replication_note_keeps_research_caveat_visible() -> None:
    result = estimate_difference_in_differences(load_fast_food_data(DEFAULT_DATA_PATH))
    note = render_replication_note(result)

    assert "synthetic teaching CSV" in note
    assert "full-time-equivalent workers" in note
    assert "does not certify a causal claim" in note


def test_loader_rejects_unexpected_state(tmp_path: Path) -> None:
    bad_data = pd.DataFrame(
        {
            "store_id": ["X01", "X01"],
            "state": ["XX", "XX"],
            "wave": ["before", "after"],
            "fte_employment": [10, 11],
        }
    )
    csv_path = tmp_path / "bad.csv"
    bad_data.to_csv(csv_path, index=False)

    with pytest.raises(ValueError, match="Unexpected states"):
        load_fast_food_data(csv_path)
