from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str
    fname: str
    bugs: object
    melon: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return  self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def bugs(self) -> object: return  self._bugs

    @train.setter
    def bugs(self, bugs): self._bugs = bugs

    @property
    def melon(self) -> object: return  self._melon

    @test.setter
    def melon(self, melon): self._melon = melon