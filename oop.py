import sys
from boy import Boy
from girls import Girl
from women import Woman
from father import Father


def get_activity(member, hour: int) -> str:
	"""Return an activity string for the given member at the specified hour (0-23)."""
	# Night / sleeping
	if 0 <= hour < 7:
		return member.sleeping()

	# Morning routine
	if hour == 7:
		return member.eating_food()

	# School / work time
	if 8 <= hour <= 12:
		if hasattr(member, "going_school"):
			return member.going_school()
		if hasattr(member, "working"):
			return member.working()
		# fallback
		return member.eating_food()

	# Lunch hour
	if hour == 13:
		return member.eating_food()

	# Afternoon (study / play / work)
	if 14 <= hour <= 16:
		if hasattr(member, "reading_books"):
			return member.reading_books()
		if hasattr(member, "playing_football"):
			return member.playing_football()
		if hasattr(member, "working"):
			return member.working()
		return member.eating_food()

	# Early evening (hobbies)
	if 17 <= hour <= 18:
		if hasattr(member, "drawing_pictures"):
			return member.drawing_pictures()
		if hasattr(member, "playing_football"):
			return member.playing_football()
		return member.eating_food()

	# Dinner
	if hour == 19:
		return member.eating_food()

	# Night activities
	if hour == 20:
		# prefer coding for Boy, makeup for Woman, chatting for Girl
		if hasattr(member, "coding_javaScript"):
			return member.coding_javaScript()
		if hasattr(member, "put_makeup"):
			return member.put_makeup()
		if hasattr(member, "chatting_friends"):
			return member.chatting_friends()
		return member.eating_food()

	if hour == 21:
		if hasattr(member, "shopping_clothes"):
			return member.shopping_clothes()
		if hasattr(member, "grumble"):
			return member.grumble()
		return member.eating_food()

	if hour == 22:
		if hasattr(member, "act_coy"):
			return member.act_coy()
		return member.sleeping()

	# Default
	return member.sleeping()


def simulate_day(member, label: str = None):
	"""Print a simple 24-hour timeline for the member."""
	name = label or getattr(member, "name", "Member")
	print(f"--- 24-hour schedule for {name} ---")
	for hour in range(24):
		activity = get_activity(member, hour)
		print(f"{hour:02d}:00 - {activity}")
	print("--- end of day ---\n")


def ask_assignee(task_name: str) -> str:
	"""Prompt the user to choose who will perform task_name.
	Returns one of: 'boy', 'girl', 'woman', 'father' (default 'father').
	"""
	options = {"1": "boy", "2": "girl", "3": "woman", "4": "father"}
	prompt = (
		f"Who should perform '{task_name}'?\n"
		"1) boy  2) girl  3) woman  4) father  (default 4) > "
	)
	choice = input(prompt).strip()
	return options.get(choice, "father")


# -----------------------
# DYNAMIC HOUR EVENTS
# Keep this mapping small and editable: for each hour (0..23) you may list
# per-member messages. Keys for members: "boy", "girl", "woman", "father".
# Values can be strings or callables that accept the member instance and return a string.
#
# Example: at hour 18 father returns home, boy returns from school, etc.
hour_events = {
	18: {
		"father": "The father comes back at home",
		"boy": "Aref comes back from school",
		"girl": "Sara comes back from school",
		"woman": "Mother is preparing dinner"
	},
	7: {
		"boy": "Aref is having breakfast",
		"girl": "Sara is having breakfast",
		"father": "The father is leaving for work",
		"woman": "Mother is getting ready"
	},
	20: {
		"boy": lambda m: m.coding_javaScript() if hasattr(m, "coding_javaScript") else "Boy is doing his hobby",
		"girl": "Girl is chatting with friends",
		"woman": "Woman is applying makeup",
		"father": "Father is reading the newspaper"
	},
	17: {
		"boy": "Boy is playing outside",
		"girl": "Girl is reading books",
		"father": "Father is returning from work",
		"woman": "Mother is shopping for groceries"
	},
	# you can extend other hours as needed
}


def get_hour_event_for_member(member_key: str, hour: int, members: dict):
	"""
	Return the dynamic event string for given member (key) at hour.
	If no custom event is set, fall back to the generic get_activity() call.
	"""
	# prefer specific mapping if exists
	try:
		member = members[member_key]
		events_for_hour = hour_events.get(hour, {})
		event = events_for_hour.get(member_key)
		if event is None:
			# no custom message: use get_activity
			return get_activity(member, hour)
		# if event is callable, call with instance
		if callable(event):
			try:
				return event(member)
			except Exception:
				# fallback robustly to activity
				return get_activity(member, hour)
		# otherwise it's a string: return it
		return event
	except KeyError:
		# unknown member key -> just return generic activity
		return "No data"


def ask_hour_and_explain():
	"""Prompt for an hour (0-23), then print the tasks at that hour and explanation."""
	try:
		hour_str = input("Please enter the hour (0-23): ").strip()
		hour = int(hour_str)
		if not (0 <= hour <= 23):
			raise ValueError()
	except ValueError:
		print("Invalid input. Please enter a number between 0 and 23.")
		return

	# create family members objects
	boy_p = Boy()
	girl_p = Girl()
	woman_p = Woman()
	father_p = Father()

	# put them in a dict keyed by the strings used in hour_events
	members = {
		"boy": boy_p,
		"girl": girl_p,
		"woman": woman_p,
		"father": father_p,
	}

	print(f"\nAt {hour:02d}:00 the family does the following:")
	# Print dynamic message per member (uses hour_events if defined, else get_activity)
	for key, member in members.items():
		msg = get_hour_event_for_member(key, hour, members)
		# include member's name where possible for clarity
		member_name = getattr(member, "name", key.capitalize())
		print(f" - {member_name}: {msg}")

	# Additionally, keep your original three fixed example actions (optional)
	# (I keep them but now they will always also be printed after the per-member lines)
	print("\nAdditional actions (examples):")
	# 1) Father takes out the trash
	print(f" - {father_p.take_out_trash()}")
	# 2) Son and daughter go to school
	print(f" - {boy_p.going_school()}")
	print(f" - {girl_p.going_school()}")
	# 3) Mother puts on makeup / makes herself beautiful
	if hasattr(woman_p, "put_makeup"):
		print(f" - {woman_p.put_makeup()}")
	else:
		print(f" - {woman_p.name} is preparing herself.")
	# 4) Afterwards father goes to work
	if hasattr(father_p, "work"):
		print(f" - {father_p.work()}")
	else:
		print(f" - {father_p.name} goes to work.")

	# (explanation lines commented out to preserve your original file's spirit)
	# print("\nExplanation: In this program the features and behaviors ...")


if __name__ == "__main__":
	# Optional command-line argument: 'boy', 'girl', 'woman', 'assign'
	choice = sys.argv[1].lower() if len(sys.argv) > 1 else "boy"

	if choice in ("boy", "girl", "woman", "father"):
		if choice == "boy":
			p = Boy()
		elif choice == "girl":
			p = Girl()
		elif choice == "woman":
			p = Woman()
		else:
			p = Father()
		simulate_day(p, p.name)

	elif choice == "assign":
		# Interactive assignment mode: let user map tasks to family members.
		print("Assignment mode: choose who performs each task.")
		assignments = {}
		assignments["shopping_clothes"] = ask_assignee("shopping_clothes")
		assignments["put_makeup"] = ask_assignee("put_makeup")
		assignments["take_out_trash"] = ask_assignee("take_out_trash")

		# create instances dictionary
		members = {
			"boy": Boy(),
			"girl": Girl(),
			"woman": Woman(),
			"father": Father(),
		}

		print("\nAssignments:")
		for task, who in assignments.items():
			print(f" - {task} -> {who}")

		# Run a simple schedule where the assigned tasks happen at certain hours
		print("\n--- Running assigned tasks during the day ---")
		# schedule: shopping at 17, makeup at 20, trash at 18
		schedule_map = {17: "shopping_clothes", 18: "take_out_trash", 20: "put_makeup"}
		for hour in range(24):
			if hour in schedule_map:
				task = schedule_map[hour]
				who = assignments.get(task)
				member = members.get(who)
				if member is None:
					print(f"{hour:02d}:00 - No member assigned for {task}")
					continue
				if hasattr(member, task):
					method = getattr(member, task)
					print(f"{hour:02d}:00 - {method()}")
				else:
					# fallback to a similar method if available
					if hasattr(member, "shopping_clothes") and task == "shopping_clothes":
						print(f"{hour:02d}:00 - {member.shopping_clothes()}")
					elif hasattr(member, "put_makeup") and task == "put_makeup":
						print(f"{hour:02d}:00 - {member.put_makeup()}")
					elif hasattr(member, "take_out_trash") and task == "take_out_trash":
						print(f"{hour:02d}:00 - {member.take_out_trash()}")
					else:
						# general fallback
						if hasattr(member, "eating_food"):
							print(f"{hour:02d}:00 - {member.eating_food()}")
						else:
							print(f"{hour:02d}:00 - {member.name} is idle.")
			# else: skip printing every hour for assignment mode
		print("--- end of assigned tasks ---")

	else:
			print("Unknown choice. Use: python oop.py [boy|girl|woman|father|assign]")


	# call the hour prompt and explanation at the very end of the program run
	ask_hour_and_explain()
