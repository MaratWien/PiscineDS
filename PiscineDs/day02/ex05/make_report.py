from config import *
from analytics import Research


if __name__ == '__main__':
	research = Research(f_path)
	data = research.file_reader()
	counts = research.calculations.counts()
	fractions = research.calculations.fractions(counts[0], counts[1])
	predict_random = research.analytics.predict_random(num_of_step)
	random_tail = sum([elem[0] for elem in predict_random])
	random_head = sum([elem[1] for elem in predict_random])
	predict_last = research.analytics.predict_last()
	text_report = report.format(len(data), counts[0], counts[1], fractions[0], fractions[1], num_of_step, random_head, random_tail)
	research.analytics.save_file(text_report, save_file)