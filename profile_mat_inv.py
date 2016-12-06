import os
import  gauss_jordan as gj
import matrix

def main():
    import sys

    filemane_profile = 'cProfile.result'
    if 2 <= len(sys.argv)
        if 'run' == sys.argv[1]:
            profile(filemane_profile)
        elif 'read' == sys.argv[1]:
            if os.path.exists(filemane_profile):
                read_profile_result(filemane_profile)
            else:
                print ('Cannot find result file %s' % filemane_profile)
        else:
            print ('please choose "read or "run"')
    else:
        print ('pelase choose "read or "run"')


def profile(filename_profile):
    import cProfile
    cProfile.run('run_mat_inv()', filename_profile)
    read_profile_result(filename_profile)

def read_profile_result(filename_profile):
    import pstats
    p = pstats.Stats(filename_profile)

    p.strip_dirs()
    p.sort_stats('cumulative', 'time')
    p.print_stats(50)

def run_mat_inv():
    n = 10
    mat_a = matrix.get_random_mat(n, n)
    mat_a_adj = matrix.adjugate_matrix(mat_a)
    mat_a_gj = gj.gauss_jordan(mat_a)

if __name__ == '__main__':
    main()