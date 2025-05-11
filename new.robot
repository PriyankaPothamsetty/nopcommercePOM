*** Settings ***
Suite Setup    Login browser connection     ${URL}
Library   SeleniumLibrary


*** Variables ***
&{dict}   key1=1   key2=2
@{list}   key1    key2
${URL}   https://www.amazon.in/s?k=flipkart&adgrpid=1326012633048780&hvadid=82876055231412&hvbmt=be&hvdev=c&hvlocphy=149009&hvnetw=o&hvqmt=e&hvtargid=kwd-82876681051014%3Aloc-90&hydadcr=15412_2338239&msclkid=3ba3be9d62391d4a80add9ae08483cd0&tag=msndeskstdin-21&ref=pd_sl_8mpp1ql5l2_e

*** Test Cases ***
first testcase
   [Documentation]   my first testcase
   FOR   ${i}  IN   @{list}
        ${value}   set variable   ${dict["${i}"]}
        log to console    ${value}
   END
   ${variable}   Set Variable    ${dict["key1"]}
   log to console     ${variable}
   ${value}  Evaluate   0+5
   log to console    ${value}
   Switch Window    Title=${URL}
   #Login browser connection     ${URL}
   Wait Until Element is Enabled      //a[text()="Customer Service"]
   Wait Until Element Is Visible     //a[text()="Customer Service"]
   ${status}   Run Keyword and Return Status   page should contain element     //a[text()="Customer Service"]
   Run Keyword and Ignore error     mmm
   log to console    ${status}
   close browser

*** Keywords ***
Login browser connection
   [Arguments]   ${url}
   Open Browser   ${url}   chrome
   maximize browser window
   #Wait Until Element is Visible



