# CafeLogon
Bypass public wifi network splash screens.  
A python script that uses the selenium web driver to automatically complete 
the splash screen forms commonly found at cafes with public wireless networks.
(note: this script was specifically designed for Au Coquelet, a cafe 
frequented by the Code Self Study meetup group, though I'm sure it 
could be adapted for other cafes and networks)  

# pre-requistes  
 * python  
 * selenium (```pip install selenium``` within virtualenv if testing)   
 * phantomjs (do not apt-get, download from [here](http://phantomjs.org/download.html), and move to your PATH)  
 * ghostdriver (included as part of phantom js)  

if you want to see what's going on,  you can use these options:   
 * chrome (ver. 56 or later)  
 * chromedriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)  
or  
 * firefox (ver. 52 or later)  
 * geckodriver (https://github.com/mozilla/geckodriver/releases)  

# to use
 * clone this repository
 * create virtualenv with ```virtualenv env```
 * activate virtualenv with ```source env/bin/activate```  
 * ```pip install selenium```
 * copy the example bin to the virtualenv bin with ```cp -r env-sample/bin/* env/bin/```
 * goto AuCoquelet, order coffee or tea   
 * run ```python wifi.py```  
 * wait for ghostdriver to automatically accept the terms and conditions
 * deactivate virtualenv with ```deactivate```  
# improvements to be made  
auto run once your computer detects preset network  
add mac spoofer? or auto reset to anonymize your activity?
