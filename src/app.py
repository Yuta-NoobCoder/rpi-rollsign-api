from flask import Flask, Response

from RollsignController import Controller

rollsign = Controller()
rollsign.set_images_dir("../display_images")

app = Flask(__name__)

@app.route('/init')
def root():
    rollsign.draw_matrix(0)
    return Response(status=200)

@app.route('/next')
def next():
    rollsign.show_next_image()
    return Response(status=200)

@app.route('/prev')
def prev():
    rollsign.show_prev_image()
    return Response(status=200)

app.run(host='0.0.0.0')