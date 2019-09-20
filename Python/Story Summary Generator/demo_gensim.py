# Summary Creator with gensim libray
# Created By Khondokar Hashibul

from gensim.summarization import summarize
import sys

fname = sys.argv[1]
 
with open(fname, 'r') as f:
    content = f.read()
    summary = summarize(content, split=True)
    summaryFileName = fname.split('.txt')[0] + '.summary.txt'
    with open(summaryFileName, 'w+') as summaryFile:
        print('Writing summary to %s' %summaryFileName)
        for i, sentence in enumerate(summary):
            summaryFile.write('%d) %s\n' %((i+1), sentence))
        print('Done!')