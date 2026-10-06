import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).parent.parent / "plt_temp.py"

spec = importlib.util.spec_from_file_location("plt_temp", MODULE_PATH)
plt_temp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plt_temp)


def test_make_dataframe():
    hours = [
        "2026-01-03T03:00",
        "2026-01-03T01:00",
        "2026-01-03T02:00",
    ]

    temps = [3.0, 1.0, 2.0]

    df = plt_temp.make_dataframe(hours, temps)

    assert list(df.columns) == ["time", "temperature_c"]
    assert len(df) == 3
    assert df["time"].is_monotonic_increasing
    assert df["temperature_c"].tolist() == [1.0, 2.0, 3.0]