
#%%
def runit (alist):

max = 0
min = 0
for i in alist:
    if (i > max):
        max = i
    if i < min:
        min = i
print (max, min)
print (alist)

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
#%%


