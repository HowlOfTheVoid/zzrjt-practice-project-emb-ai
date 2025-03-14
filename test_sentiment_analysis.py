from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

# python3.11 test_sentiment_analysis.py
class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer("I love working with Python")
        result_2 = sentiment_analyzer("I hate working with Python")
        result_3 = sentiment_analyzer("I am neutral on Python")

        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()