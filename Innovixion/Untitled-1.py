class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, patient_name, appointment_time):
        if appointment_time in self.appointments:
            print("Appointment time already taken. Please choose another time.")
        else:
            self.appointments[appointment_time] = patient_name
            print("Appointment scheduled for {} at {}".format(patient_name, appointment_time))

    def cancel_appointment(self, appointment_time):
        if appointment_time in self.appointments:
            patient_name = self.appointments.pop(appointment_time)
            print("Appointment for {} at {} has been canceled.".format(patient_name, appointment_time))
        else:
            print("No appointment found at {}".format(appointment_time))

    def view_appointments(self):
        if self.appointments:
            print("Scheduled Appointments:")
            for time, patient in self.appointments.items():
                print("Time: {}, Patient: {}".format(time, patient))
        else:
            print("No appointments scheduled.")

# Example usage
scheduler = AppointmentScheduler()

scheduler.schedule_appointment("John", "2024-03-14 09:00")
scheduler.schedule_appointment("Alice", "2024-03-14 10:00")
scheduler.schedule_appointment("Bob", "2024-03-14 11:00")

scheduler.view_appointments()

scheduler.cancel_appointment("2024-03-14 10:00")

scheduler.view_appointments()
