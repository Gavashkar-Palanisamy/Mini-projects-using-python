# Fuel Burn Calculator

# Input values
distance = float(input("Enter distance (NM): "))
fuel_burn_rate = float(input("Enter fuel burn rate (kg/hr): "))
ground_speed = float(input("Enter average ground speed (knots): "))
reserve_time = float(input("Enter reserve time (minutes): "))

# Calculations
flight_time_hr = distance / ground_speed
trip_fuel = flight_time_hr * fuel_burn_rate
reserve_fuel = (reserve_time / 60) * fuel_burn_rate
total_fuel = trip_fuel + reserve_fuel

# Output
print("\n--- Fuel Calculation Summary ---")
print(f"Flight Time      : {flight_time_hr:.2f} hr")
print(f"Trip Fuel        : {trip_fuel:.2f} kg")
print(f"Reserve Fuel     : {reserve_fuel:.2f} kg")
print(f"Total Required   : {total_fuel:.2f} kg")
