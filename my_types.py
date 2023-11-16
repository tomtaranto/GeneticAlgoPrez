from typing import Annotated, Literal, TypeVar
import numpy as np
import numpy.typing as npt


DType = TypeVar("DType", bound=np.generic)

# Notation
# N: population size
# M: number of cities

ArrayNx1 = Annotated[npt.NDArray[DType], Literal["N", 1]]
ArrayNx2 = Annotated[npt.NDArray[DType], Literal["N", 2]]
ArrayMx2 = Annotated[npt.NDArray[DType], Literal["M", 2]]
ArrayNxM = Annotated[npt.NDArray[DType], Literal["N", "M"]]
ArrayKx2xM = Annotated[npt.NDArray[DType], Literal["K", 2, "M"]]  # with K = N/2