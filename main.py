from agents import places_agent, hotel_agent, transport_agent, budget_agent
from itinerary import generate_itinerary
from export import export_itinerary


def main():

    source = input("Enter source city: ")
    destination = input("Enter destination: ")
    days = int(input("Enter number of days: "))
    budget = int(input("Enter budget: "))

    nights = days - 1

    places = places_agent(destination)

    hotel_name, hotel_cost = hotel_agent(destination, nights)

    transport_type, transport_cost = transport_agent(source, destination)

    activity_cost = places["cost"].sum()

    ok, total = budget_agent(budget, hotel_cost, transport_cost, activity_cost)

    itinerary = generate_itinerary(places, days)

    print("\nTrip Plan\n")

    print("Hotel:", hotel_name)
    print("Transport:", transport_type)

    print("\nItinerary:")

    for day, p in itinerary.items():
        print(day, ":", p)

    print("\nTotal Cost:", total)

    if ok:
        print("Within Budget")
    else:
        print("Over Budget")

    export_itinerary(itinerary, "trip_plan.docx")

    print("\nTrip plan exported to trip_plan.docx")


if __name__ == "__main__":
    main()