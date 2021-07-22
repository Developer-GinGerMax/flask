from dataclasses import dataclass


@dataclass

class Dataset(object):
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str
