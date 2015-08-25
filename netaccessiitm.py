from mechanize import Browser
import urllib2

br = Browser()

# Going to the login page
page = br.open( 'https://netaccess.iitm.ac.in/account/login' )
br.select_form( nr = 0 )

# Replace with your LDAP username and password
br.form[ "userLogin" ] = "PUT_USERNAME_HERE"
br.form[ "userPassword" ] = "PUT_PASSWORD_HERE"
br.submit()
resp = br.open( 'https://netaccess.iitm.ac.in/account/approve' )

response = '''
<form class="form-horizontal" method="post" action="/account/approve">
<fieldset>
<!-- Form Name -->
<legend>Authorization</legend>
<!-- Multiple Radios -->
<div class="form-group">
  <label class="col-md-4 control-label" for="radios">Duration</label>
  <div class="col-md-4">
  <div class="radio">
    <label for="radios-0">
      <input type="radio" name="duration" id="radios-0" value="1" checked="checked">
      60 minutes (recommended for public machines)
    </label>
  </div>
  <div class="radio">
    <label for="radios-1">
      <input type="radio" name="duration" id="radios-1" value="2">
      1 day (hostel zone)
    </label>
  </div>
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="approveBtn"></label>
  <div class="col-md-4">
    <button id="approveBtn" name="approveBtn" class="btn btn-primary">Authorize</button>
  </div>
</div>
</fieldset>
</form> 
'''

resp.set_data( response )
br.set_response( resp )

# Filling the form using the response
br.select_form( nr = 0 )

# Set 1 for one hour and 2 for one day
br.form[ 'duration' ] = [ '2' ]
response = br.submit()
print "I put your Netaccess"
