from patterns.csv_utils import Ride


def create_content(rides, headers):
    builder = [_create_headers("Taxi Report"), _create_table_headers(headers)]
    for ride in rides:
        builder.append(_add_ride(ride))
    builder.append(_close_table_headers())

    return "".join(builder)


def create_file(content: str):
    with open("financial-report.html", "w") as file:
        file.write(content)


def _create_headers(title: str):
    return f"<h1>{title}</h1>"


def _close_table_headers():
    return "</table>"


def _create_table_headers(headers):
    headers_with_tag = ""
    for header in headers:
        headers_with_tag += ("<td>" + header + "</td>")
    return "".join([
        "<table>",
        "<tr>",
        headers_with_tag,
        "</tr>"
    ])


def _add_ride(ride):
    return "".join([
        "<tr>",
        f"<td>{ride.taxi_id}</td>",
        f"<td>{ride.pick_up_time.isoformat()}</td>",
        f"<td>{ride.drop_of_time.isoformat()}</td>",
        f"<td>{ride.passenger_count}</td>",
        f"<td>{ride.trip_distance}</td>",
        f"<td>{_format_amount(ride.tolls_amount)}</td>",
        "</tr>"
    ])


def _format_amount(amount):
    if amount < 0:
        return f"<span style='color:red'>{amount}</span>"
    return str(amount)
