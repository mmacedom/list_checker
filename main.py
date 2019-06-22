import csv

#read and store old emails from csv file
old_emails = []
with open('old_sheet.csv', 'r') as csvFile:
    readerOld = csv.reader(csvFile)
    for row in readerOld:
      for email in row: 
        old_emails += [email]


#read and store new emails from csv file
new_emails = []
with open('new_sheet.csv', 'r') as csvFile:
    readerNew = csv.reader(csvFile)
    for row in readerNew:
      for email in row: 
        new_emails += [email]


#check if new emails are in old list
def email_list_repeater(listOld, listNew):

  new = []
  for email in listNew:
      if '@' in email:
        if not email in listOld:
          new += [email]


  #where you want the file to be downloaded to 
  download_dir = "new_emails.csv" 

  csv = open(download_dir, "w") 
  #"w" indicates that you're writing strings to the file

  columnTitleRow = "new_emails"
  csv.write(columnTitleRow)

  for new_email in new:
    email = new_email
    row = email + ',' + "\n"
    csv.write(row)

  return new


listOld = old_emails
listNew = new_emails
print(email_list_repeater(listOld, listNew))


