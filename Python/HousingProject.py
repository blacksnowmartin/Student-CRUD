import math
import random
from typing import Dict, List, Tuple


class HousingProject:
    """Represents an affordable housing development project."""

    def __init__(self, name: str, zone: str, total_land_cost: float, estimated_construction_cost: float):
        self.name = name
        self.zone = zone
        self.total_land_cost = total_land_cost
        self.estimated_construction_cost = estimated_construction_cost
        self.total_project_cost = total_land_cost + estimated_construction_cost

        # Crowdsourced metrics
        self.funded_capital = 0.0
        self.investors: Dict[str, float] = {}  # User: Contributed Amount
        self.material_contributions: Dict[str, List[Tuple[str, int]]] = {}  # User: [(Material, Qty)]

    def add_funding(self, user_id: str, amount: float) -> float:
        """Allows citizens to buy fractional ownership shares of the project."""
        self.funded_capital += amount
        self.investors[user_id] = self.investors.get(user_id, 0.0) + amount
        return (self.investors[user_id] / self.total_project_cost) * 100

    def add_materials(self, user_id: str, material_type: str, quantity: int, market_value_per_unit: float):
        """Allows local hardware stores, youth groups, or members to contribute physical materials

        (e.g., cement, ballast, timber, roofing) to offset building costs.
        """
        offset_value = quantity * market_value_per_unit
        # 15% discount bonus for community-sourced bulk materials to incentivize local manufacturing
        adjusted_offset = offset_value * 1.15

        self.funded_capital += adjusted_offset
        if user_id not in self.material_contributions:
            self.material_contributions[user_id] = []
        self.material_contributions[user_id].append((material_type, quantity))

        # Convert material worth into an equity stake
        self.investors[user_id] = self.investors.get(user_id, 0.0) + adjusted_offset

    @property
    def funding_status(self) -> float:
        return min((self.funded_capital / self.total_project_cost) * 100, 100.0)


class BomaCooperativeEngine:
    """Manages multiple housing pools, matches low-income Kenyans to viable projects,

    and optimizes construction resource allocation.
    """

    def __init__(self):
        self.projects: List[HousingProject] = []

    def register_project(self, project: HousingProject):
        self.projects.append(project)

    def match_citizen_to_equity(self, user_budget: float, location_preference: str) -> List[dict]:
        """Finds projects where a citizen's micro-savings can secure them an actual equity percentage

        instead of taking out predatory high-interest bank loans.
        """
        matches = []
        for project in self.projects:
            if project.zone.lower() == location_preference.lower():
                potential_share = (user_budget / project.total_project_cost) * 100
                matches.append({
                    "project_name": project.name,
                    "total_cost_kes": project.total_project_cost,
                    "your_potential_share": round(potential_share, 4),
                    "current_pool_completion": round(project.funding_status, 2)
                })
        return matches

    def generate_coop_report(self):
        """Generates an equity and execution transparency report for the community."""
        print("\n" + "=" * 65)
        print("   BOMA COOPERATIVE SYSTEM: HOUSING POOL STATE & EQUITY LEDGER   ")
        print("=" * 65)
        for proj in self.projects:
            print(f"\nProject: {proj.name} ({proj.zone})")
            print(f" -> Target Goal: KES {proj.total_project_cost:,.2f}")
            print(f" -> Funded/Offset Capital: KES {proj.funded_capital:,.2f} ({proj.funding_status:.2f}% Funded)")

            if proj.funding_status >= 100.0:
                print(" -> Status: 🎉 READY FOR GROUNDBREAKING! Materials & Land secured.")
            else:
                remaining = proj.total_project_cost - proj.funded_capital
                print(f" -> Status: 🏗️ Crowdsourcing. Needs KES {remaining:,.2f} more to break ground.")

            print(" -> Top Community Stakeholders (Fractional Owners):")
            for user, equity in proj.investors.items():
                share_pct = (equity / proj.total_project_cost) * 100
                print(f"    * Citizen {user}: Stake Value KES {equity:,.2f} ({share_pct:.2f}% ownership)")


# ==========================================
# SIMULATION OF THE UNIQUE ECOSYSTEM IN KENYA
# ==========================================
if __name__ == "__main__":
    # Create the engine
    boma_system = BomaCooperativeEngine()

    # Register two unique community projects (e.g., High-rise social housing projects)
    ruai_project = HousingProject(
        name="Ruai Eco-Block A",
        zone="Nairobi East",
        total_land_cost=4_000_000,  # 4 Million KES
        estimated_construction_cost=8_000_000  # 8 Million KES
    )

    kitengela_project = HousingProject(
        name="Kitengela Sustainable Terraces",
        zone="Kajiado/Nairobi Outskirts",
        total_land_cost=3_500_000,
        estimated_construction_cost=7_500_000
    )

    boma_system.register_project(ruai_project)
    boma_system.register_project(kitengela_project)

    # Scenario 1: Low-to-middle income citizens pool their money together incrementally
    print("--- Citizen Micro-Investing Simulation ---")
    ruai_project.add_funding(user_id="KE_USER_001", amount=150_000)  # Micro-savings contribution
    ruai_project.add_funding(user_id="KE_USER_002", amount=1_200_000)  # Chukuua chama payout pooled here
    kitengela_project.add_funding(user_id="KE_USER_003", amount=500_000)

    # Scenario 2: Local suppliers/Chamas contribute physical building materials instead of cash
    # Giving 500 bags of locally manufactured Bamburi/Savannah Cement
    ruai_project.add_materials(
        user_id="KE_LOCAL_HARDWARE_JUMA",
        material_type="Cement Bags",
        quantity=500,
        market_value_per_unit=850
    )

    # Giving Eco-friendly interlocking stabilized soil blocks (ISSBs) which reduce construction costs
    ruai_project.add_materials(
        user_id="MUMIAS_YOUTH_GROUP",
        material_type="Interlocking Soil Blocks",
        quantity=25_000,
        market_value_per_unit=35
    )

    # Large investor or diaspora citizen funds the remaining deficit to unlock the project
    ruai_project.add_funding(user_id="DIASPORA_REMITTANCE_POOL", amount=8_500_000)

    # Scenario 3: A user wants to see what their micro-budget can buy them
    my_budget = 250_000
    my_zone = "Nairobi East"
    print(f"\nMatching available options for citizen with KES {my_budget:,} in '{my_zone}':")
    matches = boma_system.match_citizen_to_equity(user_budget=my_budget, location_preference=my_zone)
    for match in matches:
        print(
            f" - Connect with '{match['project_name']}': Your budget secures {match['your_potential_share']}% of the overall estate asset."
        )

    # Output system report
    boma_system.generate_coop_report()
