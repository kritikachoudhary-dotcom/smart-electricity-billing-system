
from flask import Flask, render_template, request
import subprocess
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
print("Current folder:", os.getcwd())
print("Static folder:", app.static_folder)
print("CSS exists:", os.path.exists(
    os.path.join(app.static_folder, "style.css")
))
print("PROJECT LOCATION:", os.getcwd())
print("CSS FILE EXISTS:", os.path.exists("static/style.css"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    name = request.form.get("name", "").strip()
    consumer_id = request.form.get("consumer_id", "").strip()

    if not name or not consumer_id:
        return render_template(
            "index.html",
            error="Please enter consumer details."
        )

    units = []

    # Collect unit values
    for i in range(1, 6):

        value = request.form.get(f"unit{i}", "").strip()

        if value == "":
            continue

        try:
            number = float(value)

            if number < 0 or number > 1000000:
                raise ValueError

            units.append(number)

        except ValueError:
            return render_template(
                "index.html",
                error="Please enter valid unit values."
            )

    if not units:
        return render_template(
            "index.html",
            error="Enter at least one unit value."
        )

    # Prepare input for C program
    input_data = str(len(units)) + "\n"
    input_data += "\n".join(map(str, units)) + "\n"

    # Select executable according to operating system
    program = "billcalc.exe" if os.name == "nt" else "./billcalc"

    try:

        result = subprocess.run(
            [program],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )

        values = result.stdout.strip().splitlines()

        if len(values) != 5:
            raise ValueError("Invalid C output")

        total_units, energy, fixed, tax, total = map(
            float, values
        )

        bill = {
            "name": name,
            "consumer_id": consumer_id,
            "units": total_units,
            "energy": energy,
            "fixed": fixed,
            "tax": tax,
            "total": total
        }

        return render_template(
            "index.html",
            bill=bill
        )

    except (subprocess.SubprocessError, ValueError, OSError) as e:
     print("Calculation Error:", repr(e))

    return render_template(
        "index.html",
        error="Unable to calculate bill. Please try again."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)

