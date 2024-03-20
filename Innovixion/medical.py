class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, patient_name, appointment_time):
        if appointment_time in self.appointments:
            print("Sorry, the selected time slot is already booked. Please choose another time.")
        else:
            self.appointments[appointment_time] = patient_name
            print("Appointment scheduled successfully for {} at {}.".format(patient_name, appointment_time))

    def cancel_appointment(self, appointment_time):
        if appointment_time in self.appointments:
            patient_name = self.appointments.pop(appointment_time)
            print("Appointment for {} at {} has been cancelled.".format(patient_name, appointment_time))
        else:
            print("No appointment found at the given time.")

    def display_appointments(self):
        if self.appointments:
            print("Scheduled Appointments:")
            for time, name in self.appointments.items():
                print("Time: {}, Patient: {}".format(time, name))
        else:
            print("No appointments scheduled.")

def main():
    scheduler = AppointmentScheduler()
    while True:
        print("\n1. Schedule Appointment")
        print("2. Cancel Appointment")
        print("3. Display Appointments")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter patient name: ")
            appointment_time = input("Enter appointment time (e.g., 9:00 AM): ")
            scheduler.schedule_appointment(patient_name, appointment_time)
        elif choice == '2':
            appointment_time = input("Enter appointment time to cancel: ")
            scheduler.cancel_appointment(appointment_time)
        elif choice == '3':
            scheduler.display_appointments()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
