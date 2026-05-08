#!/usr/bin/env python3
# Run this script to refresh paradas.json:
# python scripts/fetch_paradas.py

import json
import httpx


def main():
    url = "https://metroapi.alexbadi.es/metrodata/paradas"
    headers = {"User-Agent": "metrovalencia-py/0.1.0 (Python; contact=dev@alexbadi.es)"}

    response = httpx.get(url, headers=headers, timeout=30.0)
    response.raise_for_status()

    data = response.json()
    paradas = data.get("paradas", [])

    output_path = "metrovalencia/data/paradas.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(paradas, f, ensure_ascii=False, indent=2)

    print(f"Fetched {len(paradas)} paradas -> {output_path}")


if __name__ == "__main__":
    main()