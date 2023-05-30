#TODO 1. 視窗大小 500 X 500 
# 分支功能 開啟視窗，自動調整為螢幕大小，增加可以匯入測試的文字檔
#TODO 2. 參考示範網站: https://typing-speed-test.aoeu.eu/?lang=en
# 視窗包含 欄位1: Your best: int  欄位2: Corrected CPM: int 欄位3: WPM:  int  欄位4:Time left:  int  按鈕1: Restar 欄位5: 顯示測試的文字 欄位6:輸入位置
#What are CPM and WPM? 名詞解釋
#They're short for Characters Per Minute, and Words Per Minute. The "raw CPM" is the actual number of characters you type per minute, including all the mistakes. "Corrected" scores count only correctly typed words. "WPM" is just the corrected CPM divided by 5. That's a de facto international standard.
#TODO 3. 顯示文字以空白鍵為計算鍵，輸入錯誤顯示文字則變色為紅色，輸入正確則顯示藍色，並即時計算顯示錯誤字數與目前輸入速度
#分支功能 Branch 增加可以調整速度的功能，例100字/分，則顯示顯示文字的視窗，文字變色速度依據設定的速度變色，下方有一個欄位顯示鍵入速度與現在速度的差異性與錯字數
#TODO 4. 顯示文字的視窗每次顯示的行數5行，依據鍵入的量向下轉動
#分支功能 Branch 增加可以調整每次顯示的行數
#TODO 5. 控制功能: 功能1.按enter可跳下一行 功能2.按Backspace可刪除並返回上一字(刪除已輸入的文字) 功能3.按ESC可跳出目前的測試，並顯示目前測試結果


#版本紀錄------------------------------------------------------------------------------------------------------------------------------------------
''''v1: 變更分數計算方法，原方法為分段次計算，變更為依據輸入字元數比較相對應字元數長度的文字，進行整段計算'''



#模組------------------------------------------------------------------------------------------------------------------------------------------sticky
from tkinter import *
from tkinter import font
import random as rd
import difflib as dl #比較字串差異的套件

#測試用文測試用文字------------------------------------------------------------------------------------------------------------------------------------------

example_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida tellus ut magna fermentum, sed hendrerit elit hendrerit. Sed interdum, mauris ac pharetra tempus, ex enim commodo neque, in euismod nisl nibh sit amet nibh. In faucibus eleifend nulla, ac pulvinar libero. Suspendisse eget convallis erat. Donec vehicula feugiat metus, eget convallis tortor malesuada a. Duis pharetra felis ac nibh mollis viverra. Aenean eget feugiat lorem. Praesent maximus ultricies lectus vel rhoncus. Vivamus in velit vel eros imperdiet ullamcorper sit amet at nulla. In vel massa eu orci sollicitudin sodales. Suspendisse potenti. Vestibulum malesuada tincidunt libero, vel interdum nisl ullamcorper nec. Proin quis neque eget urna rhoncus bibendum eget eu metus."
# 刪除空白項目
no_space_example_text_list = list(filter(lambda x: x.strip(), example_text.split('.'))) #用filter篩掉list中的空白項目後，再將無空白項目的物件list
#隨機挑選文字，並刪除挑出的文字前後空白
test_text = rd.choice(no_space_example_text_list).strip().split()
# position_in_text = int(0) 
# position_in_sentence = int(0) #一般設定
# total_correct_cpm = int(0)
total_correct_cpm =correct_char = position_in_text=position_in_sentence = int(0) #不同變數指向至同個物件
str2 =""

#分項指向不同物件設定

#初始時間設定
# original_time_left= 60
# time_left = 60
# #正確分數
# correct_char = int(0)
# #最佳分數
# best_score=int(0)

original_time_left = time_left = 60 #不同變數指向至同個物件




#產生視窗root------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.configure(bg="#e0e3dc")
root.title("Typing Speed Test")
root.geometry("1000x500") #調整視窗大小
# root.config(padx=500, pady=500) #這個不知道為什麼沒反應
# canvas=Canvas() #畫線用視窗

test_font = font.Font(font=('Arial', 24)) #設定測試文字中的字體大小

#產生分數欄位與重啟按鈕------------------------------------------------------------------------------------------------------------------------------------------
#第一排相關欄位與重啟按鈕
#顯示最佳成績
beast_score_label = Label(root, text='Your Best: ', font=('Arial', 12), relief=FLAT, bg="#e0e3dc") #relif解釋: https://www.tutorialspoint.com/python/tk_relief.htm
beast_score_label.grid(row=0, column=0,sticky="w", padx=5, pady=5,)
best_score_value = Label(text="00", font=('Arial',12), borderwidth=2, background='white', width=5, relief='sunken', anchor="center")
best_score_value.grid(row=0, column=1,sticky="w", padx=5, pady=5)

#顯示目前的cpm，real time顯示
corrected_cpm_label =Label(root, text='Correct CPM: ', font=('Arial',12), relief=FLAT, bg="#e0e3dc")
corrected_cpm_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')
corrected_cpm_value = Label(text="00", font=('Arial',12), borderwidth=2,background='white', width=5, relief='sunken', anchor="center")
corrected_cpm_value.grid(row=0, column=3,sticky="w", padx=5, pady=5)

#顯示目前wpm
wpm_label=Label(root, text='WPM: ', font=('Arial', 12) , relief=FLAT, bg="#e0e3dc")
wpm_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
wpm_label_value = Label(text="00", font=('Arial',12), borderwidth=2,background='white', width=5, relief='sunken', anchor="center")
wpm_label_value.grid(row=0, column=5,sticky="w", padx=5, pady=5)

#重置鈕
from main import time_left_restart #function寫在後面
restart_button = Button(command=time_left_restart,background="#27522b", width=15, anchor="center", text="RESTART",fg='white', underline=-1) #加底線失效
restart_button.grid(row=0, column=6, padx=5, pady=5)

#平均分配在視窗中
root.grid_columnconfigure(0, weight= 0.5)
root.grid_columnconfigure(1, weight= 1)
root.grid_columnconfigure(2, weight= 0.5)
root.grid_columnconfigure(3, weight= 1)
root.grid_columnconfigure(4, weight= 0.5)
root.grid_columnconfigure(5, weight= 1)
root.grid_columnconfigure(6, weight= 1 )

# #分隔線(本來預計使用canvas畫上下框線，但調整後底色色塊難以調整)
# canvas.create_line()
# canvas.create_line(0,100,200, 100, width=10)
# canvas.grid(row=1, column=0)

# 建立文字區域物件，設定高度為 5 行，寬度為 40 個字元，以及可向下捲動
text_area = Text(root, padx=10, height=5, width=50, font=test_font, highlightbackground='black', highlightthickness=1,  spacing1=10, spacing2=10)
text_area.grid(row=2, columnspan=20, padx=10, pady=15)

# 在文字區域中插入文字
# text_area.insert(END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam gravida tellus ut magna fermentum, sed hendrerit elit hendrerit. Sed interdum, mauris ac pharetra tempus, ex enim commodo neque, in euismod nisl nibh sit amet nibh. In faucibus eleifend nulla, ac pulvinar libero. Suspendisse eget convallis erat. Donec vehicula feugiat metus, eget convallis tortor malesuada a. Duis pharetra felis ac nibh mollis viverra. Aenean eget feugiat lorem. Praesent maximus ultricies lectus vel rhoncus. Vivamus in velit vel eros imperdiet ullamcorper sit amet at nulla. In vel massa eu orci sollicitudin sodales. Suspendisse potenti. Vestibulum malesuada tincidunt libero, vel interdum nisl ullamcorper nec. Proin quis neque eget urna rhoncus bibendum eget eu metus.")
text_area.insert(END, test_text)

entry_box = Entry(root, width=50,  font=('Arial', 24),justify="center")
entry_box.grid(row=3, columnspan=10, )
# root.grid_anchor
 

#時間計算，預設計時1分鐘------------------------------------------------------------------------------------------------------------------------------------------
#timer計時經過時間

timer_label = Label(root, text="Time left : ", font=('Arial', 24), relief=FLAT, bg="#e0e3dc")
# timer_label.config(background="Transparent")
timer_label.grid(row=1, columnspan=4, pady=20)
timer_value = Label(root, text= "00" , font=('Arial', 24), width=10 ,background='white', relief='sunken', anchor="center")
timer_value.grid(row=1, columnspan=8, pady=20, padx=10)

#倒數function
def update_timer():
    global time_left
    # print(time_left) #顯示時間執行狀況
    if time_left > time_left:
        return
    elif time_left > 0:
        # 如果計時器的值大於 0，則將計時器的值減 1
        time_left -= 1
        # 更新 Label 元件的值
        timer_value.config(text=time_left)
        # 每隔 1 秒執行一次更新計時器的函數
        root.after(1000, update_timer)
    else:
        # 如果計時器的值已經為 0，則顯示提示訊息
        timer_value.config(text="Time's up!")
        return
        

# 執行更新計時器的函數
update_timer()

#按下restart時間重新計算

def time_left_restart():
    global time_left, test_text, correct_char, realtime_cpm_value
    # print("timer_value.cget(\"text\") == \"Time's up!\":", timer_value.cget("text") == "Time's up!") #確認若顯示文字相同，則重新
    if timer_value.cget("text") == "Time's up!":
        # print(timer_value.cget("text")) #確認獲得的文字
        time_left= original_time_left #多1秒顯示
        timer_value.config(bg= "blue", fg="white", text=time_left)
        timer_value.after(500, lambda: timer_value.config(bg='white', fg="black"))
        test_text = rd.choice(no_space_example_text_list).strip()
        # print(test_text)#確認是否更新文字
        entry_box.delete(0, "end") #輸入欄清空
        text_area.delete('1.0', END ) #清空text 中的內容
        text_area.insert(END, test_text)
        update_timer()
        correct_char = int(0)
        corrected_cpm_value.config(text="00")
    else:
        time_left = original_time_left
        timer_value.config(bg= "blue", fg="white", text=time_left)
        timer_value.after(500, lambda: timer_value.config(bg='white', fg="black"))
        test_text = rd.choice(no_space_example_text_list).strip()
        entry_box.delete(0, "end")
        text_area.delete('1.0', END )
        text_area.insert(END, test_text)
        correct_char = int(0)
        corrected_cpm_value.config(text=realtime_cpm_value)
        corrected_cpm_value.config(text="00")


#錯誤數計算------------------------------------------------------------------------------------------------------------------------------------------

# 1. 隨機選擇text，並將文字依空格變更為list
# print(test_text)

# 2. entry輸入後按下空白鍵，清空entry欄位，並跳至list下個項目
def clear_entry_and_text_position(event):
    global position_in_text, position_in_sentence, correct_char
    # print(entry_box.get(), len(entry_box.get().strip())) #檢查加入strip()後是否可去除前後空白
    if entry_box.get().strip(): #檢查是否有輸入東西，使用strip()刪除輸入中的空白
        entry_box.delete(0, "end")
        position_in_sentence += 1
        position_in_text = 0
        total_correct_cpm += correct_char
        # print("position_in_sentence: %d, position_in_text: %d" %(position_in_sentence, position_in_text)) #檢查檢查
        if position_in_sentence >= len(test_text)-1:
            score_caculate_count_chars #若輸入字元數已經為最後一個字元，則直接計算分數
            print("caculate")
            
        
    else:
        print("no entry", position_in_sentence , position_in_text)
        
# 3. 按Backspace次數大於該項目字元數，則跳至上個項目
def backspace(event):
    '''如果按下backspace後若超過text的字元數，
    則跳到上個字元，若是此字句的第1個字元，
    則position持續為0'''
    global position_in_text, position_in_sentence
    print("backspace and position_in_text: %d" %(position_in_text))
    #TODO 這裡應該加入try 回復如果沒有text的話
    if position_in_text > 0: #設定字元位置的動作
        position_in_text-=1
        print("backspace", position_in_text)
    
    elif position_in_text <= 0 and position_in_sentence > 0:
        print("position_in_sentence: {}, position_in_text: {}".format(position_in_sentence, position_in_text))
        position_in_sentence-=1
        print(test_text)
        print(test_text[position_in_sentence])
        position_in_text = len(test_text[position_in_sentence])-1 #???不會動?
        print("position_in_sentence: %d, position_in_text: %d" %(position_in_sentence, position_in_text))
        
    # elif position_in_sentence > 0:
    #     position_in_sentence-=1
    #     position_in_text = len(test_text[position_in_sentence])-1
    #     print("position_in_sentence: %d, position_in_text: %d" %(position_in_sentence, position_in_text))
        
    else:
        position_in_sentence, position_in_text= int(0),int(0)
        print("position_in_sentence: %d, position_in_text: %d" %(position_in_sentence, position_in_text))

# 4. 每次輸入字數比對該字相對字元是否相符，超過字元數，在按空白鍵前計算至最後一個字元錯誤
def score_caculate_count_chars(event):
    '''計算輸入的字元數，即時反饋字元位置'''
    global position_in_sentence, position_in_text, correct_char, str2, realtime_cpm_value, best_score
    
    
    #方案3. string函數比較法: 使用python自有比對字串模組difflib執行
    print(str2)
    
    str2 +=entry_box.get()
    str1 = test_text[position_in_sentence]
    char_count = len(str2)
    # 創建SequenceMatcher對象
    matcher = dl.SequenceMatcher(None, str1, str2)

    # 獲取Delta物件
    delta = matcher.get_opcodes()
    correct_char = char_count
    # 輸出差異
    for tag, i1, i2, j1, j2 in delta:
        if tag == 'replace':
            correct_char-=1
            print(f"Replace '{str1[i1:i2]}' with '{str2[j1:j2]}', correct char. in this sentence '{char_count}'")
        elif tag == 'delete':
            correct_char-=1
            print(f"Delete '{str1[i1:i2]}', correct char. in this sentence '{char_count}'")
        elif tag == 'insert':
            correct_char-=1
            print(f"Insert '{str2[j1:j2]}', correct char. in this sentence '{char_count}'")
    # temp_correct_char = char_count
    # correct_char += char_count
    print("char_count: {}, correct_char: {}".format(char_count, correct_char))
    # typeing_speed_caculate(correct_char, original_time_left=original_time_left, time_left=time_left)
    # realtime_cpm_value = int(correct_char/((original_time_left - time_left)/60))
    # realtime_wpm_value = int(realtime_cpm_value/5)
    # corrected_cpm_value.config(text=realtime_cpm_value)
    # wpm_label_value.config(text=realtime_wpm_value)
    
    # if realtime_cpm_value > best_score:
    #     best_score = realtime_cpm_value
    #     best_score_value.config(text=best_score)
    
def typeing_speed_caculate(correct_char, original_time_left, time_left, best_score):

    #cpm計算
    realtime_cpm_value = int(correct_char/((original_time_left - time_left)/60))
    realtime_wpm_value = int(realtime_cpm_value/5)
    corrected_cpm_value.config(text=realtime_cpm_value)
    wpm_label_value.config(text=realtime_wpm_value)
    
    if realtime_cpm_value > best_score:
        best_score = realtime_cpm_value
        best_score_value.config(text=best_score)
    
    
    
    #方案2. list交集法: 比較2個序列間的差異值 
    #但ChatGPT提供的code會刪掉重複的
    # list1 = [1, 2, 3, 4, 5]
    # list2 = [3, 4, 5, 6, 7]

    # set1 = set(list1)
    # set2 = set(list2)

    # print(set1.difference(set2))
    # print(set2.difference(set1))
    # >>> 產生
    # {1, 2}
    # {6, 7}
    # set集合會造成重複字體非重複文字無法確認是否輸入正確，但如果不用set會出現錯誤 AttributeError: 'list' object has no attribute 'difference'

    
    #方案1. 直述式: 直接用if比對差異數
    # entring_text = entry_box.get()
    # char_count = len(entring_text)
    # position_in_text = char_count-1
    # print(f"Number of characters entered: {char_count}")
    # if test_text[position_in_sentence][position_in_text] == entring_text[-1]:
    #     print(correct_char)
    #     correct_char += 1
    #     realtime_cpm_value = correct_char/((original_time_left - time_left)/60)
    #     print("correct: ", correct_char)
    #     corrected_cpm_value.config(text=realtime_cpm_value)
    
    # else:
    #     correct_char-=1
    #     print(correct_char)
        
    #測試用try去除IndexError    
    # try except else finally
    
     # try: 
    # except IndexError:
    # IndexError: string index out of range
    #     Message("超過index")   
             
    
    

# 5. 預設起始秒數減掉time_left等於經過時間，計算cpm = 正確字數

root.bind("<space>", clear_entry_and_text_position)
root.bind("<Return>", clear_entry_and_text_position)
root.bind("<BackSpace>", backspace)
root.bind("<KeyRelease>", score_caculate_count_chars)


#正確與錯誤顯示------------------------------------------------------------------------------------------------------------------------------------------
#顯示視窗往下捲動速度------------------------------------------------------------------------------------------------------------------------------------------
#功能設定------------------------------------------------------------------------------------------------------------------------------------------


#視窗持續開啟------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()



#測試待解決------------------------------------------------------------------------------------------------------------------------------------------

#1. 嘗試從其他py匯入function
# from timer_function import update_timer

# time_left = 60

# def update_timer(root, label):
#     global time_left
#     if time_left>0:
#         time_left-=1
#         label.config(text=time_left)
#         root.after(1000, update_timer(root=root, label=label))
#     else:
#         label.config(text="Time's Up!!!")


# update_timer(root=root, label=timer_value)

#2. 嘗試將label背景顏色變更用function執行
# def bg_color_change(label):
#     label.config(bg= "blue", )
#     label.after(50, lambda: label.config(bg='white'))
 # 復歸function加入 # bg_color_change(timer_value)
# def time_left_restart():
#     global time_left
#     time_left =61
#     # bg_color_change(timer_value)
#     timer_value.config(bg= "blue", fg="white")
#     timer_value.after(500, lambda: timer_value.config(bg='white', fg="black"))
        