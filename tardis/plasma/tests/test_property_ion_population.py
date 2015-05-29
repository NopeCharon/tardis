import numpy as np

def test_phi_saha_lte(beta_rad, g_electron, ionization_data,
        phi_saha_lte):
    assert(phi_saha_lte.shape == (2,20))
    assert np.all(np.isclose(g_electron * 4 * np.exp(
        -ionization_data.ionization_energy.ix[2].ix[1] * beta_rad),
        phi_saha_lte.ix[2].ix[1]))

def test_ion_number_density(phi_saha_lte, ion_number_density_lte):
    ion_numbers = ion_number_density_lte.index.get_level_values(1).values
    ion_numbers = ion_numbers.reshape((ion_numbers.shape[0], 1))
    n_electron_from_ions = (ion_number_density_lte.values * ion_numbers).sum(
        axis=0)
    n_electron_from_saha = (ion_number_density_lte.ix[2].ix[0]/
        ion_number_density_lte.ix[2].ix[1]) * phi_saha_lte.ix[2].ix[1]
    tolerance = 0.01 * n_electron_from_ions
    assert np.allclose(n_electron_from_ions, n_electron_from_saha,
        atol=tolerance)