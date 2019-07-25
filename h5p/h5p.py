from IPython.core.magic import register_line_magic
from IPython.display import IFrame

@register_line_magic
def h5p(parameters):
    """
    %h5p / h5p
    This magic line / function displays an H5P (h5p.org) object in
    an IFRAME.
    Magic line parameters are ',' separated.
    1st parameter: H5P object ID  (if not provided a sample MCQ object is used)
    2nd: IFRAME width             (optional)
    3rd: IFRAME height            (optional)
    """
    values = parameters.split(',') if parameters != '' else []
    if len(values) < 1: values.append('558819')
    if len(values) < 2: values.append(800)
    if len(values) < 3: values.append(360)
    h5p_id, width, height = values
    frame = IFrame('https://h5p.org/h5p/embed/{}'.format(h5p_id), width, height)
    display(frame)
    return None

# EOF