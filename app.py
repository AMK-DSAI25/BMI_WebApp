from flask import Flask, render_template, request

app = Flask(_name_)

# Function to calculate BMI
def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Function to get BMI category and color
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "#FFD54F"  # Yellow
    elif 18.5 <= bmi < 25:
        return "Normal weight", "#81C784"  # Green
    elif 25 <= bmi < 30:
        return "Overweight", "#FFB74D"  # Orange
    else:
        return "Obese", "#E57373"  # Red

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    color = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = calculate_bmi(weight, height)
            category, color = get_bmi_category(bmi)
        except:
            bmi = None
            category = "Invalid input"
            color = "#f44336"  # Red for error

    return render_template("index.html", bmi=bmi, category=category, color=color)

if _name_ == "_main_":
    app.run(debug=True)