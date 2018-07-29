"""Simple example PipelineTask for testing purposes.
"""

import lsst.log
from lsst.pipe.base import (Struct, PipelineTask, PipelineTaskConfig,
                            InputDatasetField, OutputDatasetField)

_LOG = lsst.log.Log.getLogger(__name__)


class RawToCalexpTaskConfig(PipelineTaskConfig):
    input = InputDatasetField(name="raw",
                              units=["Camera", "Exposure", "Sensor"],
                              storageClass="DecoratedImageU",
                              doc="Input dataset type for this task")
    output = OutputDatasetField(name="calexp",
                                units=["Camera", "Visit", "Sensor"],
                                storageClass="ExposureF",
                                doc="Output dataset type for this task")

    def setDefaults(self):
        # set units of a quantum, this task uses per-visit-sensor quanta
        self.quantum.units = ["Camera", "Visit", "Sensor"]


class RawToCalexpTask(PipelineTask):
    """Simple example PipelineTask.
    """
    ConfigClass = RawToCalexpTaskConfig
    _DefaultName = 'RawToCalexpTask'

    def run(self, input, output):
        """Operate on in-memory data.

        With default implementation of `runQuantum()` keyword arguments
        correspond to field names in a config.

        Parameters
        ----------
        input : `list`
            List of input data objects
        output : `list`
            List of units for output, not used in this simple task.

        Returns
        -------
        `Struct` instance with produced result.
        """

        _LOG.info("executing %s: input=%s output=%s", self.getName(), input, output)

        data = input

        # attribute name of struct is the same as a config field name
        return Struct(output=data)

    def __str__(self):
        return "{}(name={})".format(self.__class__.__name__, self.getName())
