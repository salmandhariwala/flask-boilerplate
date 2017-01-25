from flask import Flask, request, redirect, url_for, send_from_directory,Response,jsonify,json
import DemoModule

# Setup Flask app.
app = Flask(__name__)
app.debug = True


# this is for index.html file
@app.route('/')
def root():
  return app.send_static_file('index.html')

# this is for handling static contents
@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# this is sample post method
@app.route('/test/post', methods=['POST'])
def sample_post():

	# access request post body
	print(request.data)

	# access request post headers
	print(request.headers)

	# access post data as dict
	mydict = request.get_json()

	# set reponse code
	res = Response(status=200)

	# set application type
	res.headers['Content-Type'] = "application/json"

	# prepare data
	my_data = DemoModule.get_demo_data();

	res.set_data(json.dumps(my_data))

	# return response
	return res 

@app.route('/test/get', methods=['GET'])
def sample_get():

	# access request  headers
	print(request.headers)

	# set reponse code
	res = Response(status=200)

	# set application type
	res.headers['Content-Type'] = "application/json"

	# prepare data
	my_data = DemoModule.get_demo_data();

	res.set_data(json.dumps(my_data))

	# return response
	return res 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)