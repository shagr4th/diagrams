from flask import Flask, render_template, request
import os
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def builder():
    return render_template('app.html')

@app.route('/', methods=['POST'])
def image():
    diag_folder = "static/"
    # get now to append to the image file to force the browser to refresh the file
    # when we edt the code as the file have the same name.
    now = datetime.datetime.now()
    diagrams_data = request.data
    if diagrams_data:
        #diagrams_data = diagrams_data.replace('\t', '    ')
        # dir may not exist
        if not os.path.exists(diag_folder):
          os.makedirs(diag_folder)
        # clean the directory
        _, _, filenames = next(os.walk(diag_folder))
        for one_file in filenames:
          os.remove('%s%s' % (diag_folder, one_file))
        # write the diagrams_data in a file and execute
        try:
            exec(diagrams_data)
            # get the pic to display
            _, _, filenames = next(os.walk(diag_folder))
            pic_name = filenames[0]
            return '/static/%s?%s' % (pic_name, now)
        except Exception as err:
            error = str(err).strip().replace('\\n', '<br>').replace('\\r', '<br>')
            return error

    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')