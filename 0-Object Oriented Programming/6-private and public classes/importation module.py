import mod
from mod import NotPrivate


test = NotPrivate("Tim")
test.display()

test._display()
