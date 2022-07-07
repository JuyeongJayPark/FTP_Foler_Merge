import os 
current_path = os.getcwd()
Folders = os.listdir(current_path)
count = 1
for Folder in Folders:
	target_path = os.path.join(current_path, Folder, "Rawdata")
	
	old_pdf_file = "Analysis_report_TBD220070.pdf"
	new_pdf_file = "Analysis_report_TBD220070_" + str(count) + ".pdf"
	
	old_excel_file = "Sequencing_Statistics_Result.xlsx"
	new_excel_file = "Sequencing_Statistics_Result_" + str(count) + ".xlsx"

	old_txt_file = "md5sum.diff.txt"
	new_txt_file = "md5sum.diff." + str(count) + ".txt"

	old_pdf_path = os.path.join(target_path, old_pdf_file)
	new_pdf_path =  os.path.join(target_path, new_pdf_file)

	old_excel_path = os.path.join(target_path, old_excel_file)
	new_excel_path =  os.path.join(target_path, new_excel_file)

	old_txt_path = os.path.join(target_path, old_txt_file)
	new_txt_path =  os.path.join(target_path, new_txt_file)

	os.rename(old_pdf_path, new_pdf_path)
	os.rename(old_excel_path, new_excel_path)
	os.rename(old_txt_path, new_txt_path)