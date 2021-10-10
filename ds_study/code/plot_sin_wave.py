import matplotlib.pyplot as plt
import numpy as np


def plot_sine_wave(**kwargs):
    """
    plot sine wave
    y = a sin(2 pi f t + t_0) + b
    """
    
    end_time = kwargs.get("end_time", 1)
    sample_time = kwargs.get("sample_time", 0.01)
    amp = kwargs.get("amp", 1)
    freq = kwargs.get("freq", 1)
    start_time = kwargs.get("start_time", 0)
    bias = kwargs.get("bias", 0)
    figsize = kwargs.get("figsize", (12, 6))
    
    time = np.arange(start_time, end_time, sample_time)
    result = amp * np.sin(2* np.pi * freq * time + start_time) + bias
    
    plt.figure(figsize=(12, 6))
    plt.plot(time, result)
    plt.grid(True)
    plt.xlabel("time")
    plt.ylabel("sin")
    plt.title(str(amp) + "*sin(2*pi)" + str(freq) + "*t+" + str(start_time) + ")+" + str(bias))
    plt.show()
    
if __name__ == "__main__":
    plot_sine_wave()