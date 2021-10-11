# Climbing-Holds
Climbing Wall data acquisition 

Planned Structure:
        
        Local Host:
        -Rock holds with strain gauge plate set up utilizing an ESP 8266
        -ESP8266 mesh network for sending and recieveing packed data
        -Host ESP8266 hooked up to computer for local data cacheing and data holding.
        -Local computer logs in with API key to send data from ID'd wall to users server side account.

        Web:
        Web Gui Login interface ==> Checks against account database
        Success ==> brings user to home page

        Home Page: 
           Feature List:
           - Overall Stats
           - Wall Ratings
           - PR times for wall difficulty levels
           -
           Tabs:
           - Overview
           - Data Analytics
           - Tips Suggestions
           


        Wall History:

            Options:
            -Previous attemps
              -Load previous data to analyze
            -New attempt
              ==>Creates New data dictionary for tracking and serializes data when run is complete
