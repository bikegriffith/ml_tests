# vim:filetype=python:fileencoding=utf-8
"""
Given an initial subject profile:
    profile = {
        names: ['Bob Jones', 'Bobby Jones'],
        birthday: '1983-01-01',
        relatives: ['Sue Smith', 'Billy Jones'],
        locations: ['Akron, OH', 'Cleveland, OH'],
    }

And some sample datasets that might belong to the subject:
    datasets = [
        {name: 'Bob J', age: '32', relatives: ['Mary Jones'], locations: ['Akron, OH', 'Dover, OH']},
        {name: 'Bob Jones', age: '33', relatives: [], locations: ['Dover, OH']},
        {name: 'Bob James', age: 21, relatives: ['Paul Foo'], locations: ['Atlanda, GA']}
    ]

Can we figure out that our original subject might also have some new
information?
    discoveries = [
        {locations: ['Dover, OH'], via_dataset_idx: [0, 1]},
        {relatives: ['Mary Jones'], via_dataset_idx: [0]},
        {name: 'Bob J', via_dataset_idx: [0]}
    ]

"""

import apriori

class TestAprioriAlgorithm(object):

    def setup(self):
        self.dataset = [
            # Columns:
            # 1: Count of total matches      2-N: additional bits of data prefixed
            #    from original profile            with the type of data
            #    allowing for some slop
            (3, 'name:Bob J', 'relative:Mary Jones', 'location:Dover, OH'),
            (2, 'name:Bob J', 'relative:Mary Jones', 'location:Dover, OH'),
            (0, 'name:Bob James', 'age:21', 'relative:Paul Foo', 'location:Atlanta, GA'),
        ]

    def test_generate_associations(self):
        L, supp_data = apriori.apriori(self.dataset, min_support=0.5)
        print 'L:', L
        print '-'*20
        print 'supp_data: ', supp_data
        print '-'*20
        rules = apriori.generateRules(L, supp_data, min_confidence=0.95)
        print '-'*20
        print 'rules: ', rules
        print '-'*20
        assert False

