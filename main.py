from flask import Flask

app = Flask(__name__)


@app.route("/")
def start():
    return "To invert the color value, please enter the RGB value as nine digits" \
           " with no space following the '/' in the url."


@app.route("/<string:value>", methods=["GET", "POST"])
def rgb_invert(value):
    rgb = [digit for digit in value]
    r = "".join(rgb[:3])
    g = "".join(rgb[3:6])
    b = "".join(rgb[6:])
    print(r, g, b)

    if len(rgb) < 9 or len(rgb) > 9:
        return {
            "error": "RGB value does not meet necessary length [9]."
        }
    elif int(r) > 255 or int(g) > 255 or int(b) > 255:
        return {
            "error": "One or more of your numbers exceeds 255."
        }
    else:
        new_r = 255 - int(r)
        new_g = 255 - int(g)
        new_b = 255 - int(b)
        return {
            "r": new_r,
            "g": new_g,
            "b": new_b
        }


if __name__ == "__main__":
    app.run(debug=True)
