import re
import long_response as long


def message_probability(user_message,recognised_words,single_response=False,reqiried_words=[]):
    message_certainty=0
    has_requered_words=True

#counts how many words are present in each predefished massage 
for word in user_message:
    if word in recognised_words:
        message_certainty += 1

#calcutes the percent of recognised word in a user message
        percentage =float(message_certainty)/float(len(recongnised_words))

#checks that the requried words are in the string
for word in requried_words:
    if word not in user_message:
        has_requried_words=False
        break

    if has_requried_words or single_response:
     int(percentage*100)
     
else:  
    


 def check_all_message(message):
    highest_prob_List = {}

    def response(bot_response,List_of_word,single_response =False,required_word =[]):
        nonlocal highest_prob_List
        higest_prob_List[bot_response]=message_probability(message,List_of_words,single_response,required)

    #response---------------------------------------------------------
    response('Hello',['hello','hii','sup','hey','heyo'],single_response=true) 
    response('I\'m doing fine,and you?',['how','are','you','doing'],required_word=['how'])   
    response('thanks you!',['i','love','code','palace'],required_word=['how'])

    best_match=max(highest_prob_List, key=highest_prob_List.get)
    #print(highest_prob_List)

    return long.unknown() if highest_prob_List[best_match]  <1 else best_match


def get_response(user_input):
    split_message =re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response =check_all_message(sprit_message)
    return response
    
    _

#testing the response system
while true:
     print ('Bot: ' + get_response(input('you: ')))
