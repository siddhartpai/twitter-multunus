import urllib2
import json
from pprint import pprint
def getId(screenName):
	url="https://api.twitter.com/1/users/lookup.json?screen_name="+screenName
	data=urllib2.urlopen(url)
	data=json.load(data)
	#print(data)
	#data=json.dumps(data,indent=2)
	print data[0]["id"]

def getTweets(screenName,numberOfTweets):
	url="https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=false&screen_name="+screenName+"&count="+str(numberOfTweets)
	data=urllib2.urlopen(url)
	data=json.load(data)
	followers=[]
	rtData=[]
	newData=[]
	max=0;
	for i in range(0,len(data)):
		if(data[i]["retweet_count"]!=0):
			print data[i]["text"] + "RT : " + str(data[i]["retweet_count"])
			url="https://api.twitter.com/1/statuses/"+str(data[i]["id"])+"/retweeted_by.json"
			data2=urllib2.urlopen(url)
			data2=json.load(data2)
			for j in range(0,len(data2)):
				#print data2[j]["followers_count"]
				followers.append(data2[j]["followers_count"])
			rtData.append(data2)
	
	followers=list(set(followers))
	followers.sort(reverse=True)
	for i in range(0,10):
	  for data2 in rtData:
	    for j in range(0,len(data2)):
	      if(data2[j]["followers_count"]==followers[i]):
		print data2[j]["screen_name"] + str(data2[j]["followers_count"])
def main():
	screenName=raw_input("Enter twitter screen Name : @")
	twitId=getId(screenName)
	getTweets(screenName,20)

if __name__=="__main__":
	main()
	
