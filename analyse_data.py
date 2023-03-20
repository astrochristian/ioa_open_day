import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scienceplots

def gaussian(x, mu, sigma, amp):
    return amp/np.sqrt(2 * np.pi) / sigma * np.exp(-1/2 * (x - mu)**2/sigma**2)

plt.style.use("science")

# Read data
df = pd.read_csv("scoreboard.csv")

# Load columns
scores = df["score_tot"].to_numpy()[1:]
times = df["t_tot"].to_numpy()[1:]

r1 = df["score1"].to_numpy()[1:]
t1 = df["t1"].to_numpy()[1:]
res1 = df["result1"].to_numpy()[1:]

r2 = df["score2"].to_numpy()[1:]
t2 = df["t2"].to_numpy()[1:]
res2 = df["result2"].to_numpy()[1:]

r3 = df["score3"].to_numpy()[1:]
t3 = df["t3"].to_numpy()[1:]
res3 = df["result3"].to_numpy()[1:]

r_arr = (r1, r2, r3)
t_arr = (t1, t2, t3)
res_arr = (res1, res2, res3)

# Plot histogram of scores
plt.figure(dpi=200, figsize=(4,4))

plt.hist(scores, bins=30, color="k", density=True, zorder=1)

# Plot gaussians
smooth_x = np.linspace(min(scores), max(scores), 1000)

plt.plot(smooth_x, gaussian(smooth_x, 66.7, 0.9, 0.3), "r-", linewidth=2, zorder=2, label="Planck")
plt.plot(smooth_x, gaussian(smooth_x, 71, 1.9, 1.2), "b-", linewidth=2, zorder=2, label="SH0ES")

plt.xlabel("Scores (km s$^{-1}$ Mpc$^{-1}$)")

plt.legend(loc="upper left")

plt.tight_layout()
plt.savefig("plots/score_histogram.png")


# Produce corner plot of round scores
fig, axd = plt.subplot_mosaic([
        ['11', 'remove', 'remove'],
        ['12', '22', 'remove2'],
        ['13', '23', '33']
], figsize=(6, 6.5), dpi=200)

axis_lims = [
    (18.55, 26.653),
    (20.773, 25.186),
    (18.189, 26.125)
]

for k in axd:
    if 'remove' in k:
        axd[k].axis('off')

    else:
        data1 = int(k[0])
        data2 = int(k[1])

        if data2 == 3:
            axd[k].set_xlabel("Round %i" % data1)
        else:
            axd[k].set_xticklabels([])

        if data1 == 1:
            axd[k].set_ylabel("Round %i" % data2)
        else:
            axd[k].set_yticklabels([])

        if data1 == data2:
            axd[k].hist(r_arr[data1 - 1], density=True, color="k")

            mean = np.average(r_arr[data1 - 1])
            std  = np.std(r_arr[data1 - 1])

            axd[k].set_title("Score %i = $%.2f \pm %.2f$" % (data1, mean, std))

            axd[k].axvline(x = mean, linestyle="-", color="r")
            axd[k].axvline(x = mean + std, linestyle="--", color="r")
            axd[k].axvline(x = mean - std, linestyle="--", color="r")

            axd[k].set_yticklabels([])

            axd[k].set_ylabel("")

        else:    
            axd[k].hist2d(r_arr[data1 - 1], r_arr[data2 - 1], cmap="plasma")
            axd[k].set_ylim(axis_lims[data2 - 1])

        

        axd[k].set_xlim(axis_lims[data1 - 1])
        
fig.suptitle("Cosmic Distance Ladder Scorner Plot")
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig("plots/scorner_plot.png")