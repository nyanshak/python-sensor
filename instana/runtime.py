import opentracing as ot
from instana import tracer, options
import os


def hook(module):
    """ Hook method to install the Instana middleware into Flask """
    if os.environ["AUTOWRAPT_BOOTSTRAP"] == "runtime":
        if "INSTANA_DEV" in os.environ:
            print("==========================================================")
            print("Instana: Running runtime hook")
            print("==========================================================")

        opts = options.Options()
        ot.tracer = tracer.InstanaTracer(opts)
