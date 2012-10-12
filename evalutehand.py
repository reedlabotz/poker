import collections

def evalute(hand):
	if is_royal_flush(hand): return 9
	if is_straight_flush(hand): return 8
	if is_four_kind(hand): return 7
	if is_full_house(hand): return 6
	if is_flush(hand): return 5
	if is_straight(hand): return 4
	if is_three_kind(hand): return 3
	if is_two_pair(hand): return 2
	if is_pair(hand): return 1
	return 0



def is_straight_flush(hand):
	return is_flush(hand) and is_straight(hand)

def is_royal_flush(hand):
	if is_straight_flush(hand):
		vals = values(hand)
		if 10 in vals and 14 in vals:
			return True
	return False

def is_flush(hand):
	return len(set(suit(hand))) == 1

allstraights = "14,1,2,3,4,5,6,7,8,9,10,11,12,13,14, ||| 1,2,3,4,5,14"
def is_straight(hand):
	vals = values(hand)
	vals.sort()
	strvals = ",".join([str(val) for val in vals])
	print strvals
	print allstraights
	return strvals in allstraights


def is_pair(hand):
	return len(set(values(hand))) <= 4

def is_two_pair(hand):
	return _num_2_uniques(hand) == twopairset

def is_three_kind(hand):
	return _num_2_uniques(hand) == threekindset

def is_full_house(hand):
	return _num_2_uniques(hand) == fullhouseset 

def is_four_kind(hand):
	return _num_2_uniques(hand) == fourkindset 

def _num_2_uniques(hand):
	vals = values(hand)
	counts = collections.Counter(vals)
	pairs = [i for i in counts.values() if i >= 2]
	pairs.sort()
	print pairs
	return pairs 

def suit(hand):
	return [card[1] for card in hand]

def values(hand):
	return [cardmap[card[0]] for card in hand]

pairset = [2]
twopairset = [2,2]
threekindset = [3]
fullhouseset = [2,3]
fourkindset = [4]

cardmap = {
		"1":1,
		"2":2,
		"3":3,
		"4":4,
		"5":5,
		"6":6,
		"7":7,
		"8":8,
		"9":9,
		"T":10,
		"J":11,
		"Q":12,
		"K":13,
		"A":14,
}

def test(hand):
	print "suit: "+str(suit(hand))
	print "values: "+str(values(hand))
	print "is_flush: "+str(is_flush(hand))
	print "is_pair: "+str(is_pair(hand))
	print "is_two_pair: "+str(is_two_pair(hand))
	print "is_three_kind: "+str(is_three_kind(hand))
	print "is_full_house: "+str(is_full_house(hand))
	print "is_four_kind: "+str(is_four_kind(hand))
	print "is_straight: "+str(is_straight(hand))
	print "is_straight_flush: "+str(is_straight_flush(hand))
	print "is_royal_flush: "+str(is_royal_flush(hand))

print "flush"
test(["Ah","Kh","Qh","Jh","Th"])
print "pair"
test(["Ah","Kh","Qh","Jh","Jh"])
print "twopair"
test(["Ac","Qh","Qh","Jh","Jh"])
print "threekind"
test(["Ah","Ah","Ah","9h","Th"])
print "fullhouse"
test(["Ah","Ah","Ah","Qh","Qh"])
print "fourkind"
test(["Ah","Ah","Ah","Ah","Qh"])
print "tough straight"
test(["Ah","1h","2h","3h","4h"])
print "straight"
test(["4h","5h","6h","7h","8h"])



print "-----"*10

def testhand(hand, expected):
	val = evalute(hand)
	if val != expected:
		print "ERROR!!!!!!!!!!!!!!!!! "
	print "hand: "+str(hand) + " answer: "+str(val)

testhand(["Ah","Kh","Qh","Jh","Th"], 9)
testhand(["9h","8h","5h","7h","6h"], 8)
testhand(["Qc","Qh","Qh","Qh","Jh"], 7)
testhand(["Ah","Ah","Ah","9h","9c"], 6)
testhand(["Ah","2h","Ah","Qh","Qh"], 5)
testhand(["2h","5h","3h","4c","Ac"], 4)
testhand(["Ah","Ah","Ac","3h","4c"], 3)
testhand(["4h","4h","6h","6h","8c"], 2)
testhand(["4h","4h","6h","7c","8h"], 1)
testhand(["4h","Ac","6c","7h","8h"], 0)
