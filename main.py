@app.route("/")
def money():
    money = ["Орёл", "Решка"]

    return f'<p>{random.choice(money)}</p>'
