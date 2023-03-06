import calcapp.globals as gl

# Initialization of global variables
gl.init()


from calcapp.main import root
# Start of application window
def build_app():
    root.mainloop()