def generate_itinerary(places_df, days):

    places_list = places_df["place"].tolist()

    itinerary = {}

    total_places = len(places_list)
    per_day = max(1, total_places // days)

    index = 0

    for day in range(1, days + 1):
        itinerary[f"Day {day}"] = places_list[index:index + per_day]
        index += per_day

    return itinerary