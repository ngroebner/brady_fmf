import obspy

POROTOMO_CONTINUOUS_NODAL_WAVEFORM_PATH = "https://nrel-pds-porotomo.s3.amazonaws.com/Nodal"

def fetch_waveform(remote_filename, remote_path):
    url = remote_filename + remote_path
    return obspy.read(url)[0]
