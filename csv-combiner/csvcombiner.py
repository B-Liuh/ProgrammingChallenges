#!/usr/bin/env python3

import sys
import pandas as pd
import unittest

class TestCsvCombiner(unittest.TestCase):

    def test_combinecontent(self):
        expected = pd.read_csv('./fixtures/combinecontent3.csv', sep=',').to_csv(index=False)
        actual = combine(['./fixtures/combinecontent1.csv', './fixtures/combinecontent2.csv'])
        self.assertEqual(actual, expected)

    def test_checkcol(self):
        expected = pd.read_csv('./fixtures/checkcol4.csv', sep=',').to_csv(index=False)
        actual = combine(['./fixtures/checkcol1.csv', './fixtures/checkcol2.csv', './fixtures/checkcol3.csv'])
        self.assertEqual(actual, expected)

def combine(csvfiles):
    all_df = []
    for curfile in csvfiles:
        df = pd.read_csv(curfile, sep=',')
        df['filename'] = curfile[curfile.replace('/', '\\').rindex('\\') + 1:]
        all_df.append(df)
    df = all_df[0]
    for temp in all_df[1:]:
        df = pd.merge(df, temp, how='outer')
    return df.to_csv(index=False)


if __name__ == '__main__':
    print(combine(sys.argv[1:]))
