import calendar
import random


picture1="x-------x";
picture2="""x-------x\n|\n|\n|\n|\n|""";

picture3="""x-------x\n|       |\n|       0\n|\n|\n|""";

picture4="""x-------x
|       |
|       0
|       |
|
|""";
picture5="""x-------x\n|       |\n|       0\n|      /|\ \n|\n|""";

picture6="""x-------x\n|       |\n|       0\n|      /|\ \n|     /\n|""";

picture7="""x-------x\n|       |\n|       0\n|      /|\ \n|      / \ \n|\n"""; 
HANGMAN_ASCII_ART="""welcome to the game Hangman\n  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ \n""";
MAX_TRIES=6;
#print(HANGMAN_ASCII_ART,MAX_TRIES,"MAX_TRIES");
#str="\"Shuffle, Shuffle, Shuffle\", say it together!\nChange colors and directions,\nDon't back down and stop the player!\n\t\tDo you want to play Taki?\n\t\tPress y\\n";
#print(str);
#Guessed_letter=input("Guess a letter\n");
#print(Guessed_letter.lower());
#word = input("Please enter a word: ");
#print(' _ ' * len(word));
#word_is_polindrom = input("Enter a word: ").lower().replace(' ', '');
#if(word_is_polindrom[::-1]==word_is_polindrom):
 #   print("OK");
#else:
#    print("NOT");
#num_degree = input("Insert the temperature you would like to convert: ").lower();
#num = float(num_degree[:-1]);
#if('f' in num_degree):
 #   print((5 * num - 160) / 9, 'C');
#if('c' in num_degree):
#    print((9 * num + 32 * 5) / 5, 'F');
date=str(input("enter the date: "))

x = calendar.weekday(int(date [6:]), int(date [3:5]), int(date[0:2]))

day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

print(day[x])