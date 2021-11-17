# Day 31 - Flash Card App Capstone Project

[Wiktionary:Frequency lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#Japanese)

[github](https://github.com/hermitdave/FrequencyWords)

[字幕](https://www.opensubtitles.org/en/search/subs)

[Google Translates Sheet](https://support.google.com/docs/answer/3093331?hl=en-GB)

[Google Translates API](https://cloud.google.com/translate/docs/languages?hl=en)


```
my_image = PhotoImage(file="path/to/image_file.png")
button = Button(image=my_image, highlightthickness=0)
```

## Step 3:

1. To change the canvas image, you'll need a reference to the image, like what you have with the text created in the canvas.
 
Then you can set the image attribute using itemconfig(). e.g.

```
new_image = PhotoImage(file="new_image.png")
old_image = PhotoImage(file="old_image.png")
canvas_image = canvas.create_image(300, 300, image=old_image)
#To change the image:
canvas.itemconfig(canvas_image, image=new_image)
```

IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.

2. To change the color of the text in a canvas element, use the fill parameter. 

e.g. https://stackoverflow.com/questions/41030973/how-can-i-change-the-color-of-text-in-tkinter

3. Remember in the mainloop() you should not create additional delayed loops 

e.g. with time.sleep() but instead, use window.after() 

e.g. [Tkinter Reference Manual: .after() method](https://tcl.tk/man/tcl8.6/TclCmd/after.htm)

4. You can cancel a window.after() loop using window.after_cancel() 

e.g. Tkinter Reference Manual: .after_cancel() method

## Step 4 - Save Your Progress

1. The remove() method can remove elements from a list. 

e.g. https://www.w3schools.com/python/ref_list_remove.asp

2. You can create a new csv file from a dictionary using DataFrame.to_csv() 

e.g. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

3. If you don't want to create an index for the new csv, you can set the index parameter to False. 

e.g. data.to_csv("filename.csv", index=False)