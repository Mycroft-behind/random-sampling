import random, sys, os, argparse
from collections import defaultdict
def dealFastaFile(fastaFile, percentage, repeat):
	"""
	:param fastaFile: Target file
	:param percentage: Percentage of eatracting sequence from target file. Such as 5%, 10%...
	:param repeat:    Repetitions of sampling
	"""
	for each_line in fastaFile:
		fastaTitle = each_line.strip()
		fastaSeq = next(fastaFile)
		# Generating random seeds of a specific length
		if randomSeesList == []:
			for i in range(repeat):
				randomSeesList.append(random.sample(range(1,round(len(fastaSeq.strip())/lengthSeed)+1),round(round(len(fastaSeq.strip())/lengthSeed)*percentage)))
		else:
			pass
	#==========
		# 20-27 Spliting and splicing target sequence based on the random seed which generated above 
		for eachRandomSeed in randomSeesList:
			targetSeq = ""
			for eachSeed in sorted(eachRandomSeed):
				if eachSeed * lengthSeed <= len(fastaSeq):
					targetSeq += fastaSeq[(eachSeed - 1) * lengthSeed :eachSeed * lengthSeed ]
				else:
					targetSeq += fastaSeq[(eachSeed - 1) * lengthSeed:len(fastaSeq)]
			resultSequence[fastaTitle].append(targetSeq)
	#============
	for i in range(repeat):
		os.system("mkdir -p {pwd}/result/{percent}%/".format(pwd=os.getcwd(), percent=str(int(percentage*100))))
		outFile = open("{pwd}/result/{percent}%/result-{i}".format(pwd=os.getcwd(), percent=str(int(percentage*100)),i=str(i)), "w")
		for each_sample in resultSequence.keys():
			outFile.write(each_sample + "\n" + resultSequence[each_sample][i] + "\n")
		outFile.close()
if __name__ == "__main__":
	parse = argparse.ArgumentParser()
	parse.add_argument("--input", "-i", help="Fasta file", required=True, metavar="")
	parse.add_argument("--lengthSeed", "-l", help="Length Seed", required=True, type=int, default=100, metavar="")
	parse.add_argument("--percentage", "-p", type=float, default=0.05, metavar="")
	parse.add_argument("--repeat", "--rep", type=int, default=1, metavar="", help="Repetitions")
	args = parse.parse_args()
	fastaInfo = {}
	lengthSeed = args.lengthSeed
	percent = args.percentage
	rep = args.repeat
	fastaFile = open(args.input, "r")
	resultSequence = defaultdict(list)
	randomSeesList = []
	dealFastaFile(fastaFile, percent, rep)

