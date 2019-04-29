import sys
import subprocess
import re

def get_lpcred(lp_path, token_type='xoxb'):
    try:
        bytes_res = subprocess.check_output(
            ["lpass", "show", "--notes", lp_path])
        string_res = str(bytes_res, 'utf-8')

        p = re.compile('({}-[A-Za-z0-9-]+)'.format(token_type))
        m = p.search(string_res)
        if m:
            return m.group(1)
        else:
            raise Exception(
                'Was able to read note "{}", but could not find an xoxb- token in it.'.format(lp_path))
    except subprocess.CalledProcessError:  # as e:
        #print( repr(e) )
        print('Unable to read the "{}" token from "{}"'.format(token_type, lp_path))
        sys.exit(0)
