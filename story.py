from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from utility import Utility
from creepy_guy import CreepyGuy

input()
codecool_bp = CodecoolClass.generate_local()

# init mentors, students, creepy guy, coffee machine
miki = codecool_bp.mentors[0]
miki.set_school(codecool_bp)

dani = codecool_bp.mentors[1]
dani.set_school(codecool_bp)

tomi = codecool_bp.mentors[2]
tomi.set_school(codecool_bp)

dori = codecool_bp.students[0]
dori.set_school(codecool_bp)

cg = CreepyGuy(False, "Creepy Guy", "CG", 1980, "male")
cg.set_school(codecool_bp)

coffe_machine = Utility("coffee machine")
coffe_machine.set_school(codecool_bp)

# morning session
input()
print("{} suggests to drink coffee.".format(tomi.nickname))
miki.drink_coffee()
miki.gong()
tomi.check_attendance()
dani.share_knowledge()
tomi.share_knowledge()
miki.share_knowledge()
tomi.check_knowledge()
dori.dojo()
print("After the dojo the energy level is lower.")
cg.arrives()

# lunch
input()
dani.lunch_break()

# afternoon session
input()
tomi.gong()
coffe_machine.beeping()
miki.maintain_utility(coffe_machine)
tomi.check_knowledge()
cg.creeping_around()
tomi.feedback()
cg.feedback()

# after work
input()
miki.do_hobby()
tomi.do_hobby()
dani.do_hobby()
