from prac_09.silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
print(silver_service_taxi)
silver_service_taxi.drive(18)
print(f"{silver_service_taxi.get_fare():.2f}")
