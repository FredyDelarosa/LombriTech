from abc import ABC, abstractmethod
import pandas as pd

class DatosSensorPort(ABC):
    @abstractmethod
    def obtener_datos_dataframe(self) -> pd.DataFrame:
        pass
