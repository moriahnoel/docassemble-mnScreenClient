from docassemble.base.util import Individual, DAObject, DAList, Value

class LAAIndividual(Individual):
  def init(self, *pargs, **kwargs):
    self.initializeAttribute('annualIncome', Value)
    self.initializeAttribute('monthlyIncome', Value)
    self.initializeAttribute('assets', Value)
    super(LAAIndividual, self).init(*pargs, **kwargs)