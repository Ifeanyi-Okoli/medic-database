import psycopg2

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="quickmedic",
    user="postgres",
    password="admin"
)
cursor = conn.cursor()

# Create the Patients table
cursor.execute('''
    CREATE TABLE Patients (
        PatientID SERIAL PRIMARY KEY,
        Name TEXT,
        Address TEXT,
        GeographicalLocation TEXT,
        Balance NUMERIC
    )
''')

# Create the Consultations table
cursor.execute('''
    CREATE TABLE Consultations (
        ConsultationID SERIAL PRIMARY KEY,
        PatientID INTEGER,
        DoctorID INTEGER,
        ConsultationType TEXT,
        StartDateTime TIMESTAMP,
        EndDateTime TIMESTAMP,
        Status TEXT,
        FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
        FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
    )
''')

# Create the Doctors table
cursor.execute('''
    CREATE TABLE Doctors (
        DoctorID SERIAL PRIMARY KEY,
        Name TEXT,
        Specialization TEXT,
        Address TEXT,
        GeographicalLocation TEXT
    )
''')

# Create the Pharmacies table
cursor.execute('''
    CREATE TABLE Pharmacies (
        PharmacyID SERIAL PRIMARY KEY,
        Name TEXT,
        Address TEXT,
        GeographicalLocation TEXT
    )
''')

# Create the Medical Laboratories table
cursor.execute('''
    CREATE TABLE MedicalLaboratories (
        LabID SERIAL PRIMARY KEY,
        Name TEXT,
        Address TEXT,
        GeographicalLocation TEXT
    )
''')

# Create the Medical Records table
cursor.execute('''
    CREATE TABLE MedicalRecords (
        RecordID SERIAL PRIMARY KEY,
        PatientID INTEGER,
        DoctorID INTEGER,
        Date DATE,
        Diagnosis TEXT,
        Prescription TEXT,
        Notes TEXT,
        FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
        FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
    )
''')

# Create the Funds table
cursor.execute('''
    CREATE TABLE Funds (
        TransactionID SERIAL PRIMARY KEY,
        PatientID INTEGER,
        Amount NUMERIC,
        TransactionDateTime TIMESTAMP,
        FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
