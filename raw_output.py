import re
myString = """r 0 https://farm6.staticflickr.com/5615/15163303444_25cd6a94e3_z.jpg
abstract paris film analog eiffeltower retro neamoscou
eiffeltower 1 https://farm6.staticflickr.com/5612/15604970017_13c2273b52_z.jpg
bridge bw paris france monochrome statue seine bronze denmark eiffeltower equestrian fra pontdebirhakeim
eiffeltower 2 https://farm8.staticflickr.com/7465/15790051635_08c0993901_z.jpg
bridge winter paris statue bronze denmark eiffeltower equestrian fra pontdebirhakeim
eiffeltower 3 https://farm9.staticflickr.com/8575/15604561738_bd0eb3f40a_z.jpg
paris eiffeltower reflet toureiffel
eiffeltower 4 https://farm6.staticflickr.com/5615/15766136296_09f08fc50d_z.jpg
november paris eiffeltower
 """
urlList = re.findall(r'(https?://[^\s]+)', myString)
print urlList