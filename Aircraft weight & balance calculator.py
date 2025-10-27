# ⚖️ Aircraft Weight & Balance Calculator
# Author: Gavashkar Palanisamy
# Description: Calculates total aircraft weight and center of gravity (CG) position.

print("------ AIRCRAFT WEIGHT & BALANCE CALCULATOR ------")

# Input Section
empty_weight = float(input("Enter Basic Empty Weight (kg): "))
empty_cg = float(input("Enter Empty CG (m): "))

crew_weight = float(input("Enter total crew weight (kg): "))
crew_arm = float(input("Enter crew arm (m): "))

pax_weight = float(input("Enter total passenger weight (kg): "))
pax_arm = float(input("Enter passenger arm (m): "))

cargo_weight = float(input("Enter total cargo weight (kg): "))
cargo_arm = float(input("Enter cargo arm (m): "))

fuel_weight = float(input("Enter fuel weight (kg): "))
fuel_arm = float(input("Enter fuel arm (m): "))

# Moment Calculations
moment_empty = empty_weight * empty_cg
moment_crew = crew_weight * crew_arm
moment_pax = pax_weight * pax_arm
moment_cargo = cargo_weight * cargo_arm
moment_fuel = fuel_weight * fuel_arm

total_weight = empty_weight + crew_weight + pax_weight + cargo_weight + fuel_weight
total_moment = moment_empty + moment_crew + moment_pax + moment_cargo + moment_fuel

cg_position = total_moment / total_weight

# Check CG Limits (example range)
cg_min = 2.5
cg_max = 3.6

print("\n------ WEIGHT & BALANCE SUMMARY ------")
print(f"Total Weight     : {total_weight:.2f} kg")
print(f"Total Moment     : {total_moment:.2f} kg·m")
print(f"CG Position      : {cg_position:.2f} m")

if cg_min <= cg_position <= cg_max:
    print("✅ CG within limits.")
else:
    print("⚠️ CG OUT OF LIMITS! Check loading configuration.")
print("---------------------------------------------")
