"""pydicom package -- easily handle DICOM files.
   See Quick Start below.

Copyright (c) 2008-2014 Darcy Mason
This file is part of pydicom, released under a modified MIT license.
   See the file LICENSE included with this distribution, also
   available at https://github.com/pydicom/pydicom

-----------
Quick Start
-----------

1. A simple program to read a dicom file, modify a value, and write to a new
   file::

    from pydicom.filereader import dcmread
    dataset = dcmread("file1.dcm")
    dataset.PatientName = 'anonymous'
    dataset.save_as("file2.dcm")

2. See the files in the examples directory that came with this package for more
   examples, including some interactive sessions.

3. Learn the methods of the Dataset class; that is the one you will work with
   most directly.

4. Questions and comments can be directed to the pydicom google group:
   http://groups.google.com/group/pydicom

5. Bugs and other issues can be reported in the issue tracker:
   https://www.github.com/pydicom/pydicom

"""

from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset, FileDataset
from pydicom.filereader import dcmread, read_file
from pydicom.filewriter import dcmwrite, write_file
from pydicom.sequence import Sequence

from ._version import __version__
from ._version import __version_info__

__all__ = ['DataElement',
           'Dataset',
           'FileDataset',
           'Sequence',
           'dcmread',
           'dcmwrite',
           'read_file',
           'write_file',
           '__version__',
           '__version_info__']
