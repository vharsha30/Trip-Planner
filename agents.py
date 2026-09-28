import pandas as pd

places = pd.read_excel("data/places.xlsx")
hotels = pd.read_excel("data/hotels.xlsx")
transport = pd.read_excel("data/transport.xlsx")


def places_agent(destination):
    result = places[places["location"] == destination]
    return result


def hotel_agent(destination, nights):
    result = hotels[hotels["location"] == destination]

    cheapest = result.sort_values("price").iloc[0]

    total_cost = cheapest["price"] * nights

    return cheapest["hotel"], total_cost


def transport_agent(source, destination):

    result = transport[
        (transport["from"] == source) &
        (transport["to"] == destination)
    ]

    option = result.sort_values("price").iloc[0]

    return option["type"], option["price"]


def budget_agent(budget, hotel_cost, transport_cost, activity_cost):

    total = hotel_cost + transport_cost + activity_cost

    return total <= budget, total