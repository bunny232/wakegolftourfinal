from setuptools import setup, find_packages

setup (name='elwgtsite',
       version='1.3',
       author='me',
	 author_email='me@waketech.edu',
	 url='https://waketech.edu',	
	 description="WakeGolfTour Project",
          long_description="Wake Golf Tour project - CSC122 Python Applications",
          long_description_content_type="text/plain",
 	 packages = find_packages(),
	 package_data = { 
               '': ['WakeGolfTour.db',  'templates/*', 
	          'golf_course/templates/golf_course/*', 
                    'golf_course/static/golf_course/*' ,
	          'golfer/templates/golfer/*', 
                    'golfer/static/golfer/*' ,
	          'golfer_polls/templates/golfer_polls/*', 
                    'golfer_polls/static/golfer_polls/*' ,
	          'tournament/templates/tournament/*', 
                    'tournament/static/tournament/*'],  
         },	 
         scripts = ['runWGT.py'],		 
  )
