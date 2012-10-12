import collections

def evalute(hand):
	
	x = is_royal_flush(hand)
	if x: return (9,x)
	x = is_straight_flush(hand)
	if x: return (8,x)
	x = is_four_kind(hand)
	if x: return (7,x)
	x = is_full_house(hand)
	if x: return (6,x)
	x = is_flush(hand)
	if x: return (5,x)
	x = is_straight(hand)
	if x: return (4,x)
	x = is_three_kind(hand)
	if x: return (3,x)
	x = is_two_pair(hand)
	if x: return (2,x)
	x = is_pair(hand)
	if x: return (1,x)
	return (0,0)



def is_straight_flush(hand):
	if is_flush(hand) and is_straight(hand):
		return high_val(hand)
	return False

def is_royal_flush(hand):
	if is_straight_flush(hand):
		vals = values(hand)
		if 10 in vals and 14 in vals:
			return 14
	return False

def is_flush(hand):
	if len(set(suit(hand))) == 1:
		return high_val(hand)
	return False

allstraights = "14,1,2,3,4,5,6,7,8,9,10,11,12,13,14, ||| 1,2,3,4,5,14"
def is_straight(hand):
	vals = values(hand)
	vals.sort()
	strvals = ",".join([str(val) for val in vals])
	print strvals
	print allstraights
	if strvals in allstraights:
		if strvals == "2,3,4,5,14":
			return 5
		else:
			return high_val(hand)
	return False


def test_pairs(hand,testpairset):
	x = _num_2_uniques(hand)
	if x[0] == testpairset:
		return x[1][-1]

def is_pair(hand):
	return test_pairs(hand,pairset)

def is_two_pair(hand):
	return test_pairs(hand,twopairset)

def is_three_kind(hand):
	return test_pairs(hand,threekindset)

def is_full_house(hand):
	return test_pairs(hand,fullhouseset)

def is_four_kind(hand):
	return test_pairs(hand,fourkindset)

def _num_2_uniques(hand):
	vals = values(hand)
	counts = collections.Counter(vals)
	pairs = [i for i in counts.iteritems() if i[1] >= 2]
	if not pairs: return [[],[]]
	c,p = zip(*pairs)
	pairs = sorted(p)
	print pairs
	print c
	return (pairs,c) 

def suit(hand):
	return [card[1] for card in hand]

def values(hand):
	return [cardmap[card[0]] for card in hand]

def high_val(hand):
	return sorted(values(hand))[-1]

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

if __name__ == "__main__":
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

	testhand(["Ah","Kh","Qh","Jh","Th"], (9,14))
	testhand(["9h","8h","5h","7h","6h"], (8,9))
	testhand(["Qc","Qh","Qh","Qh","Jh"], (7,12))
	testhand(["Ah","Ah","Ah","9h","9c"], (6,14))
	testhand(["Ah","2h","Ah","Qh","Qh"], (5,14))
	testhand(["2h","5h","3h","4c","Ac"], (4,5))
	testhand(["Ah","Ah","Ac","3h","4c"], (3,14))
	testhand(["4h","4h","6h","6h","8c"], (2,6))
	testhand(["4h","4h","6h","7c","8h"], (1,4))
	testhand(["4h","Ac","6c","7h","8h"], (0,0))
