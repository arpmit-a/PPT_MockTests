from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    mean1 = sum(sample1) / len(sample1)
    mean2 = sum(sample2) / len(sample2)
    std1 = stats.tstd(sample1)
    std2 = stats.tstd(sample2)
    n1 = len(sample1)
    n2 = len(sample2)
    
    t_statistic, p_value = stats.ttest_ind_from_stats(mean1, std1, n1, mean2, std2, n2)
    return p_value
