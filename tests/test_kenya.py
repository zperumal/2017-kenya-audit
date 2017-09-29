import kenya
def test_kenya_default():
	
    audit_file = 'audit.csv'
    sites_file = 'sites.csv'
    n_trials = 1000
    expected_counts = [400, 300]
    counts = kenya.read_files(sites_file, audit_file)
    assert(counts==expected_counts)
    expected_audit_win_counts = {'Gnu': 613, None: 387}  
    audit_win_counts = kenya.audit(n_trials)
    assert(expected_audit_win_counts == audit_win_counts)
    