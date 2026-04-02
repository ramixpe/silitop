import unittest

from silitop.parsers import parse_cpu_metrics


class ParseCpuMetricsTests(unittest.TestCase):
    def test_cluster_activity_uses_core_average_when_cluster_idle_ratio_is_wrong(self):
        metrics = parse_cpu_metrics(
            {
                "processor": {
                    "clusters": [
                        {
                            "name": "E-Cluster",
                            "freq_hz": 1_200_000_000,
                            "idle_ratio": 0.0,
                            "down_ratio": 0.0,
                            "cpus": [
                                {"cpu": 0, "freq_hz": 1_200_000_000, "idle_ratio": 0.75, "down_ratio": 0.0},
                                {"cpu": 1, "freq_hz": 1_200_000_000, "idle_ratio": 0.25, "down_ratio": 0.0},
                            ],
                        },
                        {
                            "name": "P-Cluster",
                            "freq_hz": 3_200_000_000,
                            "idle_ratio": 0.0,
                            "down_ratio": 0.0,
                            "cpus": [
                                {"cpu": 2, "freq_hz": 3_200_000_000, "idle_ratio": 0.50, "down_ratio": 0.0},
                                {"cpu": 3, "freq_hz": 3_200_000_000, "idle_ratio": 0.50, "down_ratio": 0.0},
                            ],
                        },
                    ],
                    "ane_energy": 0,
                    "cpu_energy": 0,
                    "gpu_energy": 0,
                    "combined_power": 0,
                }
            }
        )

        self.assertEqual(metrics["E-Cluster_active"], 50)
        self.assertEqual(metrics["P-Cluster_active"], 50)
        self.assertEqual(metrics["E-Cluster0_active"], 25)
        self.assertEqual(metrics["E-Cluster1_active"], 75)

    def test_cluster_activity_accounts_for_cluster_and_core_down_ratio(self):
        metrics = parse_cpu_metrics(
            {
                "processor": {
                    "clusters": [
                        {
                            "name": "E-Cluster",
                            "freq_hz": 1_000_000_000,
                            "idle_ratio": 0.0,
                            "down_ratio": 0.25,
                            "cpus": [
                                {"cpu": 0, "freq_hz": 1_000_000_000, "idle_ratio": 0.0, "down_ratio": 0.0},
                                {"cpu": 1, "freq_hz": 1_000_000_000, "idle_ratio": 0.0, "down_ratio": 0.50},
                            ],
                        },
                        {
                            "name": "P-Cluster",
                            "freq_hz": 3_000_000_000,
                            "idle_ratio": 0.0,
                            "down_ratio": 0.0,
                            "cpus": [
                                {"cpu": 2, "freq_hz": 3_000_000_000, "idle_ratio": 1.0, "down_ratio": 0.0},
                                {"cpu": 3, "freq_hz": 3_000_000_000, "idle_ratio": 1.0, "down_ratio": 0.0},
                            ],
                        },
                    ],
                    "ane_energy": 0,
                    "cpu_energy": 0,
                    "gpu_energy": 0,
                    "combined_power": 0,
                }
            }
        )

        self.assertEqual(metrics["E-Cluster_active"], 56)
        self.assertEqual(metrics["P-Cluster_active"], 0)


if __name__ == "__main__":
    unittest.main()
