def silence(request):
  """Don't do anything!"""
  pass

def wild_goose_chase(request):
  """Send them somewhere else."""
  return HttpResponseRedirect('http://google.com')

confuse=silence
