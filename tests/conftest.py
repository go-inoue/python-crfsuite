# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest


@pytest.fixture()
def xseq():
    return [
        {'walk': 1, 'shop': 0.5},
        {'walk': 1},
        {'walk': 1, 'clean': 0.5},
        {u'shop': 0.5, u'clean': 0.5},
        {'walk': 0.5, 'clean': 1},
        {'clean': 1, u'shop': 0.1},
        {'walk': 1, 'shop': 0.5},
        {},
        {'clean': 1},
        {u'проверка': 1, 'clean': 1},
    ]

@pytest.fixture
def yseq():
    return ['sunny', 'sunny', u'sunny', 'rainy', 'rainy', 'rainy',
            'sunny', 'sunny', 'rainy', 'rainy']


@pytest.fixture
def model_filename(tmpdir, xseq, yseq):
    from pycrfsuite import Trainer
    trainer = Trainer('lbfgs')
    trainer.append_dicts(xseq, yseq)
    model_filename = str(tmpdir.join('model.crfsuite'))
    trainer.train(model_filename)
    return model_filename