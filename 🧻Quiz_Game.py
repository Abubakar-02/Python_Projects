print("╔══════════════════════════════════╗")
print("║       🎯 PYTHON QUIZ GAME 🎯      ║")
print("╚══════════════════════════════════╝")
print()

name=input("Enter your Name : ")
print()

print(f"🎮 Welcome {name} to Python 🐍 Quiz Game")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

start= input(" Do you want to Play It ? Yes/No ")
if start !="yes":
    quit()

print("okay ! Lets start it .... ")

score = 0

answer= input("📝 Q.1 :Python may List Bnaney k liya konsi bracket use hot hi ? ")
if answer=="[]":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 

answer= input("📝 Q.2 :Pakistan ka Capital kya hey ? ")
if answer.lower()=="islamabad":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answder") 

answer= input("📝 Q.3 :How many Bones are in the Human body ? ")
if answer.lower()=="206":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 
   
answer= input("📝 Q.4 : What is the Capital of Punjab ? ")
if answer.lower()=="lahore":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 
    
answer= input("📝 Q.5 :What is the National Flower of Pakistan ? ")
if answer.lower()=="jasmine":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 
    
answer= input("📝 Q.6 : What is the chemical formula of water ? ")
if answer.lower()=="h2o":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 
    
answer= input("📝 Q.7 :What is the chemical formula of Salt ? ")
if answer.lower()=="nacl":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 
    
answer= input("📝 Q.8 : Pakistan may kitney Province hein ? ")
if answer.lower()=="5":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 
   
answer= input("📝 Q.9 :CPU Stands for ? ")
if answer.lower()=="central processing unit":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer") 

answer= input("📝 Q.10 :RAM stands for ? ")
if answer.lower()=="random access memory":
    print("✅ Corectt Answer")
    score +=1
else:
    print("❌ Wrong Answer")    

print()
print("__________________________________________________")
print()
print(f"🏆 Quiz Completed 🏆")    
print(f" 🧑 Player Name : {name}") 
print(f"⭐ Score : {score}/10")
print("🌹Remarks🌹")

if score == 10:
    print("🥇 Perfect! Bohat zabardast!")
elif score >= 7:
    print("🥈 Bohat acha! Well done!")
elif score >= 5:
    print("🥉 Theek hai! Aur practice karo!")
else:
    print("😢 Mehnat karo! Tum kar sakte ho!")