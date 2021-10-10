
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


path = "C:/Windows/Fonts/malgun.ttf"

if platform.system() == "Darwin":
    print("Set Hangul of Darwin")
    rc("font", family="Arial Unicode MS")
elif platform.system() == "Windows":
    print("Set Hangul of Windows")
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc("font", family=font_name)
else:
    print("Unknown system. Error Hangul")
    
plt.rcParams["axes.unicode_minus"] = False
