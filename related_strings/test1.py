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
        {name: 'Bob J', age: '31', relatives: ['Mary Jones'], locations: ['Akron, OH', 'Dover, OH']},
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

class Test(object):

    def setup(self):
        pass

    def teardown(self):
        pass
