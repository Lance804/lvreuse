"""Effect of stage mass ratio on payload capacity."""

import numpy as np
from matplotlib import pyplot as plt
from itertools import cycle

import payload
import launch_vehicles

g_0 = 9.81

def get_dv_mission(mission):
    """Mission delta-v [units: meter second**-1]"""
    if mission == 'GTO':
        return 12e3    # GTO
    elif mission == 'LEO':
        return 9.5e3    # LEO
    else:
        raise ValueError()


def main():
    mission = 'GTO'

    # Launch vehicles to examine
    lvs = (launch_vehicles.delta_iv_m, launch_vehicles.atlas_v_401, launch_vehicles.f9_b3_e)
    
    fig, axes = plt.subplots(ncols=len(lvs), sharey=True)
    fig.set_size_inches(12, 6)

    for i in range(len(lvs)):
        plt.sca(axes[i])
        plot_lv(lvs[i], mission, full_legend=(i==2))
        if i > 0:
            plt.ylabel('')

    plt.suptitle("Effect of $\\epsilon_1'$ on optimal stage mass ratio"
        + ' for {:s} ($\Delta v_*$ = {:.1f} km/s)'.format(
            mission, get_dv_mission(mission) * 1e-3))

    plt.tight_layout()
    plt.subplots_adjust(wspace=0, top=0.85)
    plt.show()


def plot_lv(lv, mission, full_legend=True):
    """Plot the payload capacity vs. stage mass ratio for a launch vehicle."""
    # Stage exahust velocities [units: meter second**-1].
    # O2/kerosene
    c_1 = lv.c_1
    c_2 = lv.c_2

    # Stage inert mass fractions
    e_1_actual = lv.stage_inert_mass_fraction(1)
    e_1_steps = np.concatenate(([e_1_actual], np.linspace(0.10, 0.25, 4)))
    e_2 = lv.stage_inert_mass_fraction(2)

    # Stage mass ratio [units: dimensionless].
    y = np.linspace(0.05, 0.50)

    # Mission delta-v [units: meter second**-1]
    dv_mission = get_dv_mission(mission)

    #colors
    color_cycle = cycle(['C' + str(i) for i in range(len(e_1_steps))])

    for e_1 in  e_1_steps:
        pi_star = np.zeros(y.shape)
        for i in range(len(y)):
            pi_star[i] = payload.payload_fixed_stages(
                c_1, c_2, e_1, e_2, y[i], dv_mission)
        if e_1 == e_1_actual:
            color='black'
            label="$\\epsilon_1'=${:.2f} (actual)".format(e_1)
        elif full_legend:
            color = next(color_cycle)
            label="$\\epsilon_1'=${:.2f}".format(e_1)
        else:
            color = next(color_cycle)
            label = None

        plt.plot(y, pi_star, label=label, color=color)

        # Mark the maxium, if there is one
        i_max = np.nanargmax(pi_star)
        if (i_max != 0) and (i_max != len(y) - 1):
            plt.scatter(y[i_max], pi_star[i_max], color=color)

    # Mark actual values
    pi_star_actual = lv.payload_actual(mission)
    y_actual = lv.stage_mass_ratio()
    plt.axhline(y=pi_star_actual, color='black')
    plt.axvline(x=y_actual, color='black')
    plt.text(y_actual*1.02, pi_star_actual*1.02, lv.name)

    plt.legend()
    plt.xlabel("2nd/1st stage mass ratio $y$ [-]")
    plt.ylabel('Payload mass fraction $\\pi_*$ [-]')
    plt.title('$c_1/g_0$={:.0f} s, $c_2/g_0$={:.0f} s\n'.format(c_1 / g_0, c_2 / g_0)
        + '$\\epsilon_2$={:.2f}'.format(e_2))

    # Start plot at 0,0
    ax = plt.gca()
    ax.set_xlim([0, 0.49])
    ax.set_ylim(ymin=0)

    # Consistent pi_star max across all subplots
    if mission == 'GTO':
        ax.set_ylim(ymax=0.02)
    elif mission == 'LEO':
        ax.set_ylim(ymax=0.04)


if __name__ == '__main__':
    main()
