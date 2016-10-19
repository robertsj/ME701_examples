def init_nice_plots() :
    from matplotlib import rcParams
    rcParams['font.family']     = 'serif'
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    rcParams['xtick.labelsize'] = 18
    rcParams['ytick.labelsize'] = 18
    rcParams['lines.linewidth'] = 1
    rcParams['axes.labelsize']  = 20
    rcParams['legend.fontsize'] = 16
    rcParams.update({'figure.autolayout': True}) 