# Trip-Planner

# Smart Trip Planner

A Python command-line tool that plans a trip based on your source city,
destination, number of days, and budget.

## Features
- Suggests tourist places for the chosen destination
- Picks the cheapest available hotel and calculates the stay cost
- Picks the cheapest transport option between source and destination
- Checks whether the total cost (hotel + transport + activities) fits the budget
- Generates a day-wise itinerary
- Exports the final plan to a Word (.docx) file

## Project Structure
├── main.py        # CLI entry point
├── agents.py      # Places, hotel, transport, and budget agents
├── itinerary.py   # Day-wise itinerary generator
├── export.py      # Exports itinerary to .docx
└── data/
    ├── places.xlsx
    ├── hotels.xlsx
    └── transport.xlsx

## Tech Stack
Python, pandas, openpyxl, python-docx

## Installation
pip install pandas openpyxl python-docx

## Usage
python main.py

Enter source city, destination, number of days, and budget when prompted.
The plan is printed in the terminal and saved as trip_plan.docx.

## Future Improvements
- Handle missing routes/hotels gracefully
- Distribute all places evenly across days
- Include hotel, transport, and cost summary in the exported document
- Suggest budget-friendly alternatives when over budget
- Add round-trip transport and multiple travelers
- Integrate an LLM for smarter, personalized recommendations
