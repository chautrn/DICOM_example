import pydicom

slice_data = pydicom.filereader.dcmread('./dicom_files/1-01.dcm')

print(slice_data)
print(slice_data.PatientName)
print(slice_data[0x281050])
