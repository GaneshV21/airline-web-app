import os,requests,json
from flask import Flask, render_template
from collections import Counter
app = Flask(__name__)

@app.route('/')
def index():
    with open("flights.json") as f:
        flights_data = json.load(f)

    routes = []
    for item in flights_data.get('data'):
        departure = item.get('departure', {}).get('airport')
        arrival = item.get('arrival', {}).get('airport')
        if departure and arrival:
            routes.append(f"{departure} ➜ {arrival}")
    route_counter = Counter(routes)
    top_routes = route_counter.most_common(10)

    airlines = [
        item.get('airline', {}).get('name')
        for item in flights_data['data']
        if item.get('airline') and item['airline'].get('name')
    ]
    airline_counter = Counter(airlines)
    top_airlines = airline_counter.most_common(5)

    arrival_airports = [item['arrival']['airport'] for item in flights_data['data'] if item['arrival'].get('airport')]
    arrival_counter = Counter(arrival_airports)
    top_arrivals = arrival_counter.most_common(10)

    statuses = [
        item.get('flight_status')
        for item in flights_data['data']
        if item.get('flight_status')
    ]
    status_counter = Counter(statuses)

    return render_template(
        "index.html",
        top_routes=[{"route": route, "count": count} for route, count in top_routes],
        top_airlines=[{"airline": name, "count": count} for name, count in top_airlines],
        status_data=dict(status_counter),
        top_arrivals=[{"location": name, "count": count} for name, count in top_arrivals]
    )

if __name__ == '__main__':
    app.run(debug=True)
