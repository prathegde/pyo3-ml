use pyo3::prelude::*;
use pyo3::types::PyList;
fn main() -> PyResult<()> {
    Python::with_gil(|py|{
        let syspath: &PyList = py.import("sys")?
                                 .getattr("path")?
                                 .try_into()?;
                            
        syspath.insert(0, ".")?;

        let sample_script_module = py.import("py.ml_script")?;

        sample_script_module.getattr("train_model")?
                            .call0()?;
        
        Ok(())
    })
}
