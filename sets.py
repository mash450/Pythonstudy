days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

# set methods
# add
days.add('mon')
print(days)
# remove
days.remove('mon')
print(days)

# add more values
days.update([1,2,3,4])
print(days)

# clear
days.clear()
print(days)

# discard


s = {'foo', 'bar', 'baz', 'qux'}
del s['bar']
print(s)