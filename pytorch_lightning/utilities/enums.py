# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Enumerated utilities"""
from enum import Enum
from typing import Union


class LightningEnum(str, Enum):
    """ Type of any enumerator with allowed comparison to string invariant to cases. """

    @classmethod
    def from_str(cls, value: str) -> 'LightningEnum':
        statuses = [status for status in dir(cls) if not status.startswith('_')]
        for st in statuses:
            if st.lower() == value.lower():
                return getattr(cls, st)
        return None

    def __eq__(self, other: Union[str, Enum]) -> bool:
        other = other.value if isinstance(other, Enum) else str(other)
        return self.value.lower() == other.lower()


class AMPType(LightningEnum):
    """Type of Automatic Mixed Precission used for training.

    >>> # you can math the type with string
    >>> AMPType.APEX == 'apex'
    True
    """
    APEX = 'apex'
    NATIVE = 'native'


class DistributedType(LightningEnum):
    """ Define type of ditributed computing.

    >>> # you can math the type with string
    >>> DistributedType.DDP == 'ddp'
    True
    >>> # which is case invariant
    >>> DistributedType.DDP2 == 'DDP2'
    True
    """
    DP = 'dp'
    DDP = 'ddp'
    DDP2 = 'ddp2'
    DDP_SPAWN = 'ddp_spawn'
    HOROVOD = 'horovod'


class DeviceType(LightningEnum):
    """ Define Device type byt its nature - acceleatrors.

    >>> DeviceType.CPU == DeviceType.from_str('cpu')
    True
    >>> # you can math the type with string
    >>> DeviceType.GPU == 'GPU'
    True
    >>> # which is case invariant
    >>> DeviceType.TPU == 'tpu'
    True
    """
    CPU = 'CPU'
    GPU = 'GPU'
    TPU = 'TPU'
