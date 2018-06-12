def parameter_dmrg():
    para = dict()
    # Physical parameters
    para['spin'] = 'half'
    para['jxy'] = 1
    para['jz'] = 1
    para['hx'] = 0
    para['hz'] = 0
    para['bound_cond'] = 'periodic'
    # Calculation parameters
    para['l'] = 10  # Length of MPS
    para['chi'] = 8  # Virtual bond dimension cut-off
    para['d'] = 2  # Physical bond dimension
    para['sweep_time'] = 500  # sweep time
    # Fixed parameters
    para['if_print_detail'] = False
    para['tau'] = 1e-3  # a shift to ensure the GS energy is the lowest
    para['break_tol'] = 1e-8  # tolerance for breaking the loop
    para['is_real'] = True
    para['dt_ob'] = 5  # in how many sweeps, observe to check the convergence
    para['ob_position'] = (para['l'] / 2).__int__()  # to check the convergence, chose a position to observe
    para['data_path'] = '.\\data_dmrg\\'
    return para
