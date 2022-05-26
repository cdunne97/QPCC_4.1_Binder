import gspread
from string import ascii_uppercase, ascii_lowercase

def grading(student_id, question, answer):
    gc = gspread.service_account(filename='qpccnew-2fcf5aebef09.json')
    sh = gc.open_by_key('1UcN2Ru06sTUT3cT3-RsvJKOioQySvpNuWa6XFK1L0Ww')
    wk = sh.sheet1
    
    right = 0
    for x in range(len(question)):
        wk.update_cell(wk.find(student_id).row, wk.find(question[x]).col, answer[x])
        
        if wk.acell(ascii_uppercase[1+x]+'2').value == answer[x].capitalize():
            right+=1
            print('P'+str(x+1)+': Right 😎')
        else:
            print('P'+str(x+1)+': Wrong 😭')
      
    print('Loading...')
    print('Submitted 🎉 👨🏻‍💻')
    print('Grade:' +str(right) + '/' + str(len(question)))