import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple', 'orange', 'banana', 'peach']
	# using template views/hello_world.tpl
	return bottle.template('hello_world', username="Tin", things=mythings)

	
bottle.debug(True)
bottle.run(host='localhost', port=8080, reloader=True)
