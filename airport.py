
class Flight:
    def __init__(self, flight_no, destination, departure_time, delay):
        self.flight_no = flight_no
        self.destination = destination
        self.departure_time = departure_time
        self.delay = delay


flights = [
    Flight("AI101", "Chennai", "09:30", 45),
    Flight("AI202", "Delhi", "08:15", 90),
    Flight("AI303", "Mumbai", "12:00", 30),
    Flight("AI404", "Bangalore", "10:45", 120),
    Flight("AI505", "Hyderabad", "11:30", 75)
]

# 1. Display delayed flights
print("Delayed Flights:")
for f in flights:
    if f.delay > 0:
        print(f.flight_no, f.destination, f.delay, "minutes")

# 2. Find the longest delay
longest = max(flights, key=lambda f: f.delay)
print("\nFlight with Longest Delay:")
print(longest.flight_no, longest.destination, longest.delay, "minutes")

# 3. Calculate average delay
total_delay = sum(f.delay for f in flights)
average = total_delay / len(flights)
print("\nAverage Delay:", average, "minutes")

# 4. Sort flights by departure time
flights.sort(key=lambda f: f.departure_time)
print("\nFlights Sorted by Departure Time:")
for f in flights:
    print(f.flight_no, f.destination, f.departure_time, f.delay)

# 5. Display flights delayed more than 60 minutes
print("\nFlights Delayed More Than 60 Minutes:")
for f in flights:
    if f.delay > 60:
        print(f.flight_no, f.destination, f.delay, "minutes")
