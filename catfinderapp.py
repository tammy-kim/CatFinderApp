from tkinter import *
from PIL import ImageTk, Image
from functools import partial

# create the main window where the user answers questions
root = Tk()
root.title("CatFinder")
root.iconbitmap("images/icon.ico")
root.geometry("800x540")
background_img = ImageTk.PhotoImage(Image.open("images/background.jpg"))
Label(root, image=background_img).place(x=0, y=0)

"""
create a Cat class, which is characterized by its breed name (name), type of coat (coat), levels of activity (activity), 
grooming requirements (grooming), levels of independence (independence), general health (health), whether it is hypoallergenic or not (hypoallergenic), 
its image file (image), and brief behavioral / morphological description (intro).
"""
class Cat:
    def __init__(self, name, coat, activity, grooming, friendliness, independence, health, hypoallergenic, image, intro):
        self.name = name
        self.coat = coat
        self.activity = activity
        self.grooming = grooming
        self.friendliness = friendliness
        self.independence = independence
        self.health = health
        self.hypoallergenic = hypoallergenic
        self.image = ImageTk.PhotoImage(Image.open("images/" + image))
        self.intro = intro

cat_list = []   # cat_list stores all the cat breeds
cat_list.append(Cat("Abyssinian", "shorthair", "high", "low", "moderate", "moderate", "low", "yes", "abyssinian.jpg",
                    "Very active, and friendly to people and animals. They are affectionate and social cats."))
cat_list.append(Cat("American Bobtail", "shorthair and longhair", "high", "moderate", "high", "moderate", "high", "no", "american_bobtail.jpg",
                    "Unique for their natural bobbed tail, American Bobtail is athletic and playful. They are affectionate and need lots of attention."))
cat_list.append(Cat("American Curl", "shorthair and longhair", "high", "moderate", "high", "moderate", "high", "no", "american_curl.jpg",
                    "They have uniquely curled-back ears. Muscled and slender in build. They're generally very healthy breed."))
cat_list.append(Cat("American Wirehair", "shorthair", "moderate", "low", "moderate", "moderate", "moderate", "no", "american_wirehair.jpg",
                    "American Wirehairs have dense, coarse coat. They enjoy attention and are affectionate, loyal, and agile cats."))
cat_list.append(Cat("American Shorthair", "shorthair", "low", "low", "high", "high", "high", "no", "american_shorthair.jpg",
                    "Well-balanced, strongly built cat. They are calm and make a good family companion."))
cat_list.append(Cat("Balinese", "longhair", "high", "low", "moderate", "low", "low", "yes", "balinese.jpg",
                    "Known for their svelte build, the Balinese is curious and outgoing cats. They are vocal and need lots of attention"))
cat_list.append(Cat("Bengal", "shorthair", "high", "low", "low", "low", "moderate", "yes", "bengal.jpg",
                    "Bengals have a wildcat-like look, but they are people-oriented and loyal. They are athletic and agile, and learn very quickly."))
cat_list.append(Cat("Birman", "longhair", "low", "high", "high", "low", "moderate", "no", "birman.jpg",
                    "Birman is a colorpointed cat with four pure white feet. They are affectionate, gentle, and intelligent"))
cat_list.append(Cat("Bombay", "shorthair", "moderate", "low", "high", "low", "moderate", "no", "bombay.jpg",
                    "Bombays are playful, agreeable, and demand a lot of attention. They are attached to their owners and like to follow them."))
cat_list.append(Cat("British Shorthair", "shorthair", "low", "low", "high", "high", "moderate", "no", "british_shorthair.jpg",
                    "They are affectionate but not clingy, playful but not overactive. They are generally quiet and undemanding."))
cat_list.append(Cat("Burmese", "shorthair", "high", "low", "moderate", "low", "moderate", "yes", "burmese.jpg",
                    "They are very playful and intelligent cats. They have a unique rasp to their voices, so they may sound husky compared to other cats."))
cat_list.append(Cat("Burmilla", "shorthair and longhair", "moderate", "low", "high", "high", "moderate", "no", "burmilla.jpg",
                    "They are very people-oriented cats. They are intelligent, affectionate, and not too vocal."))
cat_list.append(Cat("Chartreux", "shorthair", "moderate", "low", "high", "moderate", "high", "no", "chartreux.jpg",
                    "Loving, amiable, and adapatable. They are generally quiet and very intelligent."))
cat_list.append(Cat("Colorpoint Shorthair", "shorthair", "high", "low", "high", "low", "low", "yes", "colorpoint_shorthair.jpg",
                    "They are very outgoing, affectionate, playful, and people-friendly cats. However, they are also sensitive and very vocal. They demand a lot of attention."))
cat_list.append(Cat("Cornish Rex", "shorthair", "high", "low", "low", "low", "low", "yes", "cornish_rex.jpg",
                    "They are extremely playful, so they are good for people who are into very active cats. They are social and agile cats"))
cat_list.append(Cat("Devon Rex", "shorthair", "high", "low", "moderate", "low", "moderate", "yes", "devon_rex.jpg",
                    "They shed less than many other breeds, and they are affectionate, playful, and curious cats."))
cat_list.append(Cat("Egyptian Mau", "shorthair", "high", "low", "moderate", "moderate", "moderate", "no", "egyptian_mau.jpg",
                    "They are quiet and loyal cats. They like to hunt and provide small gifts to their human companions, and they want a lot of praise and pettings."))
cat_list.append(Cat("Exotic", "shorthair and longhair", "low", "low", "high", "low", "low", "no", "exotic.jpg",
                    "Laid-back, affectionate, and loyal. They're also playful and enjoy cuddles."))
cat_list.append(Cat("Havana Brown", "shorthair", "moderate", "low", "moderate", "low", "moderate", "no", "havana_brown.jpg",
                    "One of the rare cat breeds, Havana Brown is very adaptable and agreeable cats. They love to fetch and demand a lot of attention."))
cat_list.append(Cat("Japanese Bobtail", "shorthair and longhair", "high", "low", "high", "low", "moderate", "no", "japanese_bobtail.jpg",
                    "Japanese Bobtails are bold, intelligent, and energetic. They are also adaptable and highly intelligent."))
cat_list.append(Cat("Khao Manee", "shorthair", "high", "low", "high", "low", "moderate", "no", "khao_manee.png",
                    "They are devoted to their owners and they are curious and intelligent cats. They may have odd-eyes (one of them blue, the other gold)."))
cat_list.append(Cat("Korat", "shorthair", "high", "low", "moderate", "low", "low", "no", "korat.png",
                    "Korats like to fetch and they are playful and affectionate. They need a lot of affection from their owners."))
cat_list.append(Cat("LaPerm", "shorthair and longhair", "high", "low", "high", "moderate", "high", "no", "laperm.jpg",
                    "Known for their curly coats, LaPerms are gentle and people-oriented cats. They are active, agile, and quiet."))
cat_list.append(Cat("Lykoi", "shorthair", "high", "low", "high", "high", "moderate", "no", "lykoi.jpg",
                    "Lykoi cats are easygoing, affectionate, and playful. They are unique for their half-hairless appearance."))
cat_list.append(Cat("Maine Coon", "longhair", "moderate", "high", "high", "high", "high", "no", "maine_coon.jpg",
                    "Maine Coons are very large cats, weighing up to 8 kg. They are intelligent, loyal, and playful."))
cat_list.append(Cat("Manx", "shorthair and longhair", "moderate", "moderate", "high", "moderate", "low", "no", "manx.jpg",
                    "They have round build, with short front legs and short back. They are loyal, gentle, and are great jumpers."))
cat_list.append(Cat("Norwegian Forest Cat", "longhair", "high", "moderate", "high", "moderate", "high", "no", "norwegian_forest_cat.jpg",
                    "They are slowly maturing breed, and large in size. They are athletic, playful, friendly, and family-oriented."))
cat_list.append(Cat("Ocicat", "shorthair", "high", "low", "high", "low", "moderate", "yes", "ocicat.jpg",
                    "Noted for their wild appearance, they are adaptable, playful, vocal, and social cats. They need a lot of space and toys because they are very active."))
cat_list.append(Cat("Oriental", "shorthair and longhair", "high", "low", "moderate", "low", "low", "yes", "oriental.jpg",
                    "They are very curious and active, so they require a lot of attention. They are social and loyal cats."))
cat_list.append(Cat("Persian", "longhair", "low", "high", "high", "low", "low", "no", "persian.jpeg",
                    "Well known for sweet expressions and round appearance, Persians are calm, not as active. They require daily grooming."))
cat_list.append(Cat("RagaMuffin", "longhair", "low", "high", "high", "low", "moderate", "no", "ragamuffin.jpg",
                    "RagaMuffins are people-oriented, affectionate, and not very vocal cats. They are also generally very healthy and adaptable."))
cat_list.append(Cat("Ragdoll", "longhair", "low", "high", "high", "low", "moderate", "no", "ragdoll.jpg",
                    "Docile and mild-mannered, Ragdolls are excellent indoor companions. They are laid-back, affectionate, and gentle."))
cat_list.append(Cat("Scottish Fold", "shorthair and longhair", "low", "moderate", "moderate", "high", "low", "no", "scottish_fold.jpg",
                    "Scottish Folds have folded ears and very round build, due to mutation. They are soft-spoken and adaptable. Some, however, develop ear infections and deafness."))
cat_list.append(Cat("Selkirk Rex", "shorthair and longhair", "low", "high", "high", "moderate", "high", "no", "selkirk_rex.jpg",
                    "Selkirks are very friendly, playful, and loyal. They are known for their curly hair."))
cat_list.append(Cat("Siamese", "shorthair", "high", "low", "low", "low", "low", "yes", "siamese.jpg",
                    "With svelte build, Siamese are intelligent and playful, but very vocal. They crave social interaction and need a lot of daily activities."))
cat_list.append(Cat("Siberian", "longhair", "moderate", "low", "high", "moderate", "high", "yes", "siberian.png",
                    "Unlike most cats, Siberians like to play in water. They are affectionate, playful, extremely agile, and generally very healthy."))
cat_list.append(Cat("Singapura", "shorthair", "high", "low", "moderate", "moderate", "low", "no", "singapura.jpg",
                    "One of the smaller cat breeds, Singapuras are active, curious, quiet, and highly intelligent. They like to be the center of attention."))
cat_list.append(Cat("Somali", "longhair", "high", "moderate", "low", "moderate", "low", "no", "somali.jpg",
                    "Somalis are very active and intelligent, but also quite michievous. They are friendly with people but are not lap cats."))
cat_list.append(Cat("Sphynx", "shorthair", "high", "high", "high", "low", "moderate", "yes", "sphynx.jpg",
                    "Noted for their hairlessness, Sphynxes are very loyal and demand lots of attention. They need frequent bathing and are high maintenance."))
cat_list.append(Cat("Tonkinese", "shorthair", "high", "low", "high", "low", "moderate", "no", "tonkinese.jpg",
                    "Tonkinese demand a lot of attention, but they are affectionate and adaptable. They do well with pets that have similar activity level as them."))
cat_list.append(Cat("Toybob", "shorthair and longhair", "moderate", "low", "high", "moderate", "high", "no", "toybob.jpg",
                    "One of the smallest cat breeds, Toybobs are social, active, and playful. They are agile climbers and good lap cats."))
cat_list.append(Cat("Turkish Angora", "longhair", "high", "moderate", "moderate", "low", "moderate", "no", "turkish_angora.jpg",
                    "Turkish Angoras are good-natured, determined, and playful. They are good at swimming and they like to be in control of their surroundings."))
cat_list.append(Cat("Turkish Van", "longhair", "high", "moderate", "high", "moderate", "high", "no", "turkish_van.jpg",
                    "Turkish Vans are talkative and demand a lot of attention. They're energetic, agile, and very healthy."))

# dictionaries of the user's answer to each question. The user's answer matches with the cat's characteristics so that the user can receive the correct result.
hairtypes = {"yes": ["shorthair", "shorthair and longhair"], "no": ["longhair", "shorthair and longhair"], "dm": ["shorthair", "longhair", "shorthair and longhair"]}
activitytypes = {"yes" : ["high", "moderate"], "no" : ["low", "moderate"], "dm": ["high", "moderate", "low"]}
groomingtypes = {"yes" : ["low", "moderate"], "no": ["low", "moderate", "high"]}
friendlytypes = {"yes": ["high", "moderate"], "no": ["low", "moderate"], "dm": ["high", "moderate", "low"]}
independencetypes = {"yes": ["high", "moderate"], "no": ["low", "moderate"], "dm": ["high", "moderate", "low"]}
healthtypes = {"yes": ["high", "moderate"], "dm": ["high", "moderate", "low"]}
allergytypes = {"yes": ["yes"], "no": ["yes", "no"]}

Label(root, text = "Welcome to CatFinder! Answer only 7 questions, and find out all kinds of lovely cats that will be perfect for you!", 
      font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
Label(root, text = "When you are done, click 'Submit' button below.", font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
Label(root, text = "1) Would you like your cat to be shorthair? Enter 'yes', 'no', or 'dm' (doesn't matter).", font=("Helvetica", 10), 
      bg = "#FCF8EC").pack(anchor=W)
e1 = Entry(root, width=40, font=("Helvetica", 10))
e1.pack(anchor=W)

Label(root, text = "2) Do you want the cat to be active (high-energy, playful)? Enter 'yes', 'no', or 'dm' (doesn't matter).", 
      font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
e2 = Entry(root, width=40, font=("Helvetica", 10))
e2.pack(anchor=W)

Label(root, text = "3) Would you mind if the cat requires a lot of grooming? Enter 'yes' if you don't want the cat to require lots of grooming, enter 'no' otherwise.", 
      font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
e3 = Entry(root, width=40, font=("Helvetica", 10))
e3.pack(anchor=W)

Label(root, text = "4) Do you want your cat to be friendly to strangers, including children? Enter 'yes', 'no' or 'dm' (doesn't matter).", 
      font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
e4 = Entry(root, width=40, font=("Helvetica", 10))
e4.pack(anchor=W)

Label(root, text = "5) Would you like your cat to be independent (likes to be alone)? Enter 'yes', 'no', or 'dm' (doesn't matter).",
      font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
e5 = Entry(root, width=40, font=("Helvetica", 10))
e5.pack(anchor=W)

Label(root, text = "6) Should the cat be very healthy (little to no genetic health problems) in general? Enter 'yes' or 'dm' (doesn't matter).",
      font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
e6 = Entry(root, width=40, font=("Helvetica", 10))
e6.pack(anchor=W)

Label(root, text = "7) Are you allergic to cats? Enter 'yes' or 'no'.", font=("Helvetica", 10), bg = "#FCF8EC").pack(anchor=W)
e7 = Entry(root, width=40, font=("Helvetica", 10))
e7.pack(anchor=W)

result = []     # stores all cat breeds that fit with what the user wants for their cat's qualities

# when the user presses the button "Ok" in errorWindow, the window will automatically close.
def goback():
    errorWindow.destroy()

# display showWindow, which shows the corresponding cat's brief description and image.     
def show(curr_name):
    global showWindow
    showWindow = Toplevel(root)
    showWindow.title("CatFinder")
    showWindow.iconbitmap("images/icon.ico")
    Label(showWindow, text = curr_name, font=("Helvetica", 10, "bold")).pack()
    for cat in cat_list:
        if cat.name == curr_name:
            print(cat.name)
            Label(showWindow, text = cat.intro, font=("Helvetica", 10)).pack()
            Label(showWindow, image=cat.image).pack()
            
"""
Processes the user's inputs, evaluates whether their answers are valid, and if so, provide a list of recommended cats.
Otherwise, informs the user that their answers are not valid.
"""
def submit():
    ans1 = e1.get().lower()
    ans2 = e2.get().lower()
    ans3 = e3.get().lower()
    ans4 = e4.get().lower()
    ans5 = e5.get().lower()
    ans6 = e6.get().lower()
    ans7 = e7.get().lower()
    
    # bad_condition is when the user inputs wrong answer to any of the questions
    bad_condition = (ans1 not in hairtypes) or (ans2 not in activitytypes) or (ans3 not in groomingtypes) or (ans4 not in friendlytypes) \
        or (ans5 not in independencetypes) or (ans6 not in healthtypes) or (ans7 not in allergytypes)
    
    if bad_condition: 
        global errorWindow
        errorWindow = Toplevel(root)
        errorWindow.title("CatFinder")
        errorWindow.iconbitmap("images/icon.ico")
        Label(errorWindow, text = "Error: Please make sure that you answered appropriately for all questions.", font=("Helvetica", 10)).pack()
        Button(errorWindow, text = "Ok", font=("Helvetica", 10), command=goback).pack()
    else: 
        for cat in cat_list:
            coat = cat.coat in hairtypes[ans1]
            activity = cat.activity in activitytypes[ans2]
            grooming = cat.grooming in groomingtypes[ans3]
            friendliness = cat.friendliness in friendlytypes[ans4]
            independence = cat.independence in independencetypes[ans5]
            health = cat.health in healthtypes[ans6]
            hypoallergenic = cat.hypoallergenic in allergytypes[ans7]
            satisfy = coat and activity and grooming and friendliness and independence and health and hypoallergenic
            if satisfy:
                result.append(cat)
        resultWindow = Toplevel(root)       # display resultWindow, which lists all the cats stored in result (in buttons).
        resultWindow.title("CatFinder")
        resultWindow.iconbitmap("images/icon.ico")
        resultWindow.configure(background = "#CBF3F1")
        resultWindow.geometry("630x600")
        if not result:  # if list is empty, display a window that tells the user that there are no cats that meet their requirements
            Label(resultWindow, text = "Oh no! It looks like there are no suitable cat breeds that meet your requirements.\n", 
                  font=("Helvetica", 10), bg = "#CBF3F1").pack(anchor=W)
        else:   # otherwise, display a window that gives a list of the recommended cat breeds for the user
            Label(resultWindow, text = "Here are the results!", font=("Helvetica", 10), bg = "#CBF3F1").grid(row=0, column=1)
            Label(resultWindow, text = "To view the cat's image and brief description, click the button.", font=("Helvetica", 10), 
                  bg = "#CBF3F1").grid(row=1, column=1)
            Label(resultWindow, text = "", bg = "#CBF3F1").grid(row=2, column=0, columnspan = 30)
            count = 0
            row_num = 3
            for cat in result:
                cat_name = cat.name
                if count < 15:
                    Button(resultWindow, text = cat_name, font=("Helvetica", 10), bg = "#E1FEFC", command=partial(show, cat_name)).grid(row = row_num, column = 0)
                elif count < 30:
                    Button(resultWindow, text = cat_name, font=("Helvetica", 10), bg = "#E1FEFC", command=partial(show, cat_name)).grid(row = (row_num % 15) + 3, column = 1)
                else:
                    Button(resultWindow, text = cat_name, font=("Helvetica", 10), bg = "#E1FEFC", command=partial(show, cat_name)).grid(row = (row_num % 15) + 3, column = 2)
                count += 1
                row_num += 1
    result.clear()
    
submitButton = Button(root, text="Submit", bg = "#E1FEFC", font=("Helvetica", 10), command=submit)
submitButton.pack()

root.mainloop()
