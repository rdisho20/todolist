self.assertRaises(NoExperienceError):
    employee.hire(Candidate("John Smith", "no experience"))