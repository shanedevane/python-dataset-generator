# -*- coding: utf-8 -*-

import os
import random
import csv
from collections import namedtuple

DEFAULT_OUTPUT_FILENAME = 'dataset_output.csv'
DEFAULT_ROWS = 10000
DEFAULT_DELIMITER = ','


class PythonDataSetGenerator:

    def __init__(self, rows=10000, delimiter=',', filename='dataset_output.csv'):
        self._rows = rows
        self._delimiter = delimiter
        self._filename = filename
        self._factors = list()
        self._last_factor = 0
        self._generated_rows = 0
        self._positive_ratio = 50
        self.enable_incremental_id = True
        self.enable_mixed_data = False

    def add_factor(self, name, good_range, bad_range, mixed=False):
        factor = namedtuple('Factor', 'name good_range bad_range mixed')

        factor.name = name
        factor.mixed = mixed
        factor.good_range = good_range
        factor.bad_range = bad_range
        self._factors.append(factor)

    def _go_to_next_factor(self):
        self._last_factor += 1
        if self._last_factor > len(self._factors)-1:
            self._last_factor = 0

    def _create_positive_factor_row(self):
        row = list()
        for factor in self._factors:
            positive_range_min = factor.good_range[0]
            if len(factor.good_range) > 1:
                positive_range_max = factor.good_range[1]
                val = random.randint(positive_range_min, positive_range_max)
            else:
                val = positive_range_min

            row.append(val)
        return row

    def _create_negative_factor_row(self):
        row = list()
        for factor in self._factors:
            negative_range_min = factor.bad_range[0]
            if len(factor.bad_range) > 1:
                negative_range_max = factor.bad_range[1]
                val = random.randint(negative_range_min, negative_range_max)
            else:
                val = negative_range_min

            row.append(val)
        return row

    def _create_mixed_factor_row(self):
        row = list()
        for factor in self._factors:
            positive_range_min = factor.good_range[0]
            negative_range_min = factor.bad_range[0]
            if len(factor.bad_range) > 1:
                positive_range_max = factor.good_range[1]
                val = random.randint(negative_range_min, positive_range_max)
            else:
                if random.choice([True, False]):
                    val = negative_range_min
                else:
                    val = positive_range_min

            row.append(val)
        return row

    def _get_factor_names(self):
        names = list()
        for factor in self._factors:
            names.append(factor.name)
        return names

    def _generate(self):
        if not self._factors:
            return

        with open(self._filename, 'w', newline='\n') as file:
            writer = csv.writer(file,
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(self._get_factor_names())

            weighted_random = [True] * self._positive_ratio + [False] * (100-self._positive_ratio)

            for num, row in enumerate(range(self._rows)):

                if self.enable_mixed_data:
                    output_row = self._create_mixed_factor_row()
                else:
                    data_choice = random.choice(weighted_random)

                    if data_choice:
                        output_row = self._create_positive_factor_row()
                    else:
                        output_row = self._create_negative_factor_row()

                if self.enable_incremental_id:
                    output_row.insert(0, num+1)

                writer.writerow(output_row)

    def save(self):
        self._generate()

if __name__ == "__main__":
    generator = PythonDataSetGenerator()
    generator.add_factor('photo_width', [2000, 5000], [1, 1000])
    generator.add_factor('photo_colours', [12000, 55886], [1, 9000])
    generator.save()


"""s
    TO DO
   - the mixed data can be from the lower and upper boundaries of the good/bad
   - accommodate floating vs int
   - accountmodate the good being -numbers
   - accommodate when the bad values are above the good values when doing the mixed thing
   - allow for a default file?
   - pep 8 convention
   - more unit tests
   - property testing test?
   - conditional data ranges
    -: first_time_user and usage_amount. if someone is first time user, then usage_amount == 0 etc.
"""