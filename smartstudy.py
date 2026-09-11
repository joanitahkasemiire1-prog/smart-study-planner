def add_session(sessions):
      # Adds a new study session
      print("Add study session selected.")
def view_all_sessions(sessions):
      print("View all sessions selected")
def search_sessions(sessions):
       print("Search sessions selected")
def view_statistics(sessions):
       print("View statistics selected")
def save_data(sessions):
       print("saving data....")
def main():
    sessions =[]

    while True:
        print("====smart study planner====")
        print("1. Add study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View statistics")
        print("5. Save and exit")

        choice = input("Enter your choice (1-5):")

        if choice =="1":
               print("Add study sessions")
        elif choice =="2":
               print("View all sessions")
        elif choice =="3":
               print("Search sessions by subject")
        elif choice =="4":
              print("View statistics")
        elif choice =="5":
               print("Save and exit")
               print("your data has been saved.")
               print("Goodbye!")
               break

        else:
            print("Invalid choice. please enter a number from 1 to 5.")
    main()

    # part b
def add_session(sessions):
    print("---Add study session---")

    subject = input("Enter subject name:")
    topic = input("Enter topic covered:")
    date_day = input("Enter date or day:")

    while True:
       try:
                duration = int(input("Enter duration in minutes:"))
                if duration > 0:
                      break
                else:
                      print("Please enter a valid whole number.")
       except ValueError:
              print(" Please enter a valid whole number.")
       session = {
             "subject": subject,
             " topic": topic,
             "date_day": date_day,
             "duration": duration,
       }

       sessions.append(session)
       print("Session added successfully.")

def view_all_sessions(sessions):
      print("---ALL study sessions---")

      if len(session) == 0:
            print("No sessions have been added yet.")
      else:
            for session in sessions:
                print(session)

def search_sessions(sessions):
    print("Search sessions function will go here.")

def view_statistics(sessions):
    print("View statistics function will go here.")

def save_data(sessions):
    print("Save data function will go here.")

def add_sessions(sessions):
     print("Add sessions")

def main():
    # controls the menu and progam flow
    sessions = load_sessions()

    while True:
          print("====smart study planner====")
          print("1. Add a study session")
          print("2. View all sessions")
          print("3. Search sessions by subject")
          print("4. View statistics")
          print("5. Save and exit")

          choice = input("Enter your choice (1-5):")

          if choice == "1":
              add_session(sessions)
          elif choice =="2":
             print("View all session(sessions)")
          elif choice =="3":
             print("Search session(sessions) by subject")
          elif choice =="4":
             print("View statistics(sessions)")
          elif choice =="5":
             save_sessions(sessions)
             print("Your data has been saved")
             print("Goodbye!")
             break
          else:
               print("Invalid choice. Please enter a number from 1 to 5.")
main()

# part c: catergorize tasks by duration
def search_by_subject(subject'sessions):
     # searches sessions by subject
     """
     catergorize tasks into:
     -short: less than 30 minutes
     -medium: 30 to 60 minutes
     -long: over 90 minutes
     """
     short = []
     medium =[]
     long_tasks = []

     for tasks in self.tasks:
          if task.duration_minutes< 30:
               short.append(task)
          elif 30 <= task.duration_minutes <= 90:
                   medium.append(task)
          else: # over 90 minutes
                   long_tasks.append(task)

          print("===Tasks by duration===")

          print(" SHORT (less than 30 minutes:)")
          if short:
                   for task in short:
                        print(f"  .{task.subject} -{task.duration_minutes} min ({task.subject})")
          else:
                  print("   No short tasks")

                  print(" MEDIUM ( 30 to 90 minutes): ")
                  if medium:
                           for task in medium:
                                 print("   No medium tasks")
                  print(" LONG ( over 90 minutes):")
                  if task in long_tasks:
                   print(f"   .{task.name} -{ task.duration_minutes} min ({task.subject})")
                  else: 
                   print("   No long tasks")
                   return short, medium, long_tasks

# part d: 
def view_sessions():
     sessions =[]
     if not sessions:
          print("No study sessions recorded.")
          return
     print("\nStudy Sessions")
     print("-" * 70)
     print(f"{'Subject':<15}{'Topic':<20}{'Duration':<12}{'Classification':<15}")
     print("-" * 70)
     for session in sessions:
          classification = 
     classify_session(session["duration"])

     print(f"{session['subject']:<15}"
                f"{session['topic']:<20}"
                f"{session['duration']:<12}"
                f"{classification:<15}")
     print("-" * 70)
     
    
            # part e
def search_by_subject(subject):
#searches sessions by subject
     found_sessions = []
     total_time = 0
     for session in sessions:
          if session["subject"].lower() ==subject.lower():
               found_sessions.append(session)
               total_time += session["duration"]

          if len(found_sessions) ==0:
               print("No study found for that subject.")
          else:
               print("\nStudy Sessions for:", subject)
               print("-" * 50)
               print(f"{'Subject':<15}{'Topic':<20}{'Duration':<15}")
               print("-" * 50)

               for session in found_sessions:
                    print(f"{session['subject']:<15}"
                          f"{session['topic']:<20}"
                          f"{session['duration']:<15}")

                    print("-" * 50)
                    print("Total time spent:", total_time, "minutes")

                 # part f
def study_statistics():
     if len(sessions) == 0:
          print("No study sessions recorded.")
          return

     # calculate total study time
     total_minutes = 0

     for session in sessions:
          total_minutes +=session["duration"]
     total_hours = total_minutes / 60
     print("\nSTUDY STATISTICS")
     print("-" * 40)
     print(f"Total hours studied overall: {total_hours:2f} hours")

     #calculate total time for each subject
     subject_totals = {}
     for session in sessions:
          subject = session["subject"]
          duration = session["duration"]

          if subject in subject_totals:
             subject_totals[subject] += duration
          print("\nTotal hours studied per subject:")
          for subject, minutes in subject_totals.items():
               hours = minutes / 60
               print(f"{subject}: {hours: 2f} hours")

               #find the subject with the least study time
               weakest_subject =min(subject_totals, key=subject_totals.get)
               weakest_time = subject_totals[weakest_subject]

               print("\nSubject with the least study time:")
               print(f"{weakest_subject} - {weakest_time /60:.2f} hours")

               #calculate the longest study session
               longest_session = max(sessions, key=lambda session: session["duration"])

               print("\nLongest study session:")
               print(f"Subject:{longest_session['subject']}")
               print(f"Topic:{longest_session['topic']}")
               print(f"Duration:{"longest_session['duration]"} minutes")

               # part g
     def save_sessions(sessions):
     #saves sessions to the next file
          with open("study_log.txt", "w") as file:
               for session in sessions:
                    file.write(
                         f"{session['subject']}|"
                         f"{session['topic']}|"
                         f"{session['date_day']}|"
                         f"{session['duration']}|"
                    )

def load_sessions():
#loads previously saved sessions
     sessions = []

     try:
          with open("study_log.txt", "r") as file:
               for line in file:
                    line = line.strip()

                    if line:
                         parts = line.split("|")

                         if len(parts) == 4:
                              session ={
                                   "subject": parts[10],
                                   "topic": parts[1],
                                   "date_day": parts[2],
                                   "duration": int(parts[3])
                              }
                              sessions.append(session)

      except FileNotFoundError:
          sessions =[]

          return sessions
#program entry point
if__name__ =="__main__":
          
     


        