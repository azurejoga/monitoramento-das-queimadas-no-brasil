# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00c06c3e-9719-37ea-b768-15b859e3556c | -22.15369 | -48.12421 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d3bd194-c819-30dc-90ae-e5bf37cec57a | -22.1533 | -48.12864 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 587675df-c6a4-382e-8ac2-d51fd5a0105b | -22.15096 | -48.0872 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1a54ec8-3a28-3bb9-87cc-40dbbbbee7e7 | -22.15055 | -48.09193 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5685306c-8ae2-3ea2-88d0-040f105367c7 | -22.14704 | -48.13211 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 258ada9e-dcdb-3144-9e32-130e53b5b24d | -22.14666 | -48.13651 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b07fde5c-0353-30e4-8f24-710c244223ec | -22.14231 | -48.11798 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f9630a9-c852-342f-922c-5e8969b78635 | -22.13641 | -48.11733 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5789842-9dcd-3006-9bfe-dc65d8bf6b8a | -22.13604 | -48.12157 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3de9fe1-625c-3e60-92d7-a1dbabb45988 | -22.13013 | -48.12104 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68f6cdbd-4e47-3ff1-9e0e-5825b8983cf2 | -22.12976 | -48.1253 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8299f893-f366-3823-93c2-f60369f13265 | -22.12422 | -48.12049 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3e98a75-f490-39b8-bfd5-1f9f94dfb1ec | -21.11664 | -47.23219 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7c47a8c-0f99-3478-8a79-376ee6907b5e | -21.11623 | -47.23238 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2f2d5ef-e6de-3d10-adb5-8f3e3fce39b8 | -21.11078 | -47.22813 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 711d92d5-e6b7-3e26-ba65-a40ca1eac7bc | -21.11036 | -47.23274 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62af047b-d489-3fca-be97-2177eda87671 | -21.11034 | -47.22836 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c88ecbfb-98d9-39a1-8880-cda03bf06b30 | -21.10999 | -47.23693 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcc930d1-915d-3631-8de5-7e04a21aff2d | -21.10996 | -47.23293 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c6556df-7ae7-3dad-949a-8c5dee85541a | -21.10962 | -47.2371 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08b6eb62-71b7-343b-97b0-8ddcf0a61ee0 | -21.1096 | -47.24126 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65c4cf69-5ff0-3de9-beb1-fe6d3dd6689f | -21.10926 | -47.24142 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b41f64-ac20-3201-8adb-3402f8f9162a | -21.10409 | -47.23337 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a27c213-2acb-3dfe-a552-3ac08cb34208 | -21.10375 | -47.23721 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0e98aec-abd6-3d88-9f90-6ab6f40b0135 | -21.1037 | -47.23347 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84880498-e734-35e7-ae37-80b8c6ccdcaf | -21.10339 | -47.24128 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0c1324b-5f4d-3c39-aed7-9f38e39fa85a | -21.10339 | -47.2373 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83d5a1e1-345d-3602-803f-fffd04e18ca9 | -21.10305 | -47.24138 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61cb4a82-9fd3-3df1-88ab-1709220cbc16 | -21.09829 | -47.22864 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdcb128a-7283-37ba-978b-d514272e3cf6 | -21.09758 | -47.23668 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66bff4f2-ee2c-3ca1-9b7e-799718dac0af | -21.08176 | -47.57052 | 2024-10-09 05:06:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 669d545e-dd07-3f82-8c44-2737a793411c | -21.08133 | -47.57559 | 2024-10-09 05:06:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02ab2ca1-2499-3750-85e8-23ed41ede2b9 | -21.07951 | -47.57472 | 2024-10-09 05:06:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51b24a0-f023-3406-9c74-2e67532eb483 | -21.07905 | -47.57972 | 2024-10-09 05:06:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0c440e2-4683-3382-82f6-e32827c1d151 | -21.05306 | -47.24841 | 2024-10-09 05:06:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5ffa386-04db-37c4-b749-2077d377303d | -21.05269 | -47.25272 | 2024-10-09 05:06:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8495547-e06e-36e6-a615-676b86e9271b | -21.6738 | -47.72522 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 401a9f6f-f480-3d44-8cea-e17d11b5d5e5 | -21.67339 | -47.7299 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c40b35b-59f8-38b0-bfaf-22fe8fbc2e1f | -21.66856 | -47.71563 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 374aa583-7d59-3b0f-a7af-483faf29ed74 | -21.66814 | -47.72044 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| af552873-336e-30d0-b857-28c682e37aec | -21.66734 | -47.72961 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 123.2 |
| ecee2242-dcba-3116-9f6e-ae1d8ce9f6d8 | -21.66692 | -47.7344 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 51c0ebae-d80b-35cc-b6ff-c171905ba4e9 | -21.66293 | -47.71062 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b44a8fa6-d78c-304f-badb-e25c6409d74f | -21.66251 | -47.7154 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 18d5774c-cc6b-391f-837d-d6a05894b953 | -21.66208 | -47.72024 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| f2227e70-db54-3b94-bcb3-7be33bb0bcda | -21.66169 | -47.72478 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a51228eb-bdca-344b-a297-86f7d00ef36f | -21.66129 | -47.7293 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 5e133379-6b48-34f3-aabf-035356ec7515 | -21.66088 | -47.734 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 7915fb4c-2a4d-3f4a-baf8-72bf4c1728e8 | -21.65688 | -47.71028 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 363e07c2-7fe2-3ed7-bf9e-2612e1c7a3ff | -21.65646 | -47.71507 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 80a1e897-4e19-3607-89f2-444a1e6f00b2 | -21.65604 | -47.71991 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2d16f474-1134-3cec-be2a-6d3261eea10b | -21.65563 | -47.72455 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 50df53b9-da24-30cd-a024-e9d94d17c7f4 | -21.65524 | -47.72911 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6aebef89-e260-3953-9ff9-233cb59fb3cb | -21.65125 | -47.70509 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad7f939b-0d48-35dc-bce7-bf5c7463135f | -21.65084 | -47.70983 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 120aed17-477b-3d4b-9e15-40ac1fe75ede | -21.65042 | -47.71464 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d7958ce5-8950-3cf2-8df2-d232dedbd8c6 | -21.64999 | -47.71953 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d770df3d-093c-381e-b33c-56f837d7e630 | -21.64958 | -47.72429 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 160c0073-6d57-39e2-a9c7-1b2bd66c4101 | -21.64396 | -47.71902 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98c95416-56df-3a66-916c-fa7c7054b486 | -21.63837 | -47.71343 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a79ddfb7-7cd6-32c6-bfa2-976f9f27bfdd | -21.63274 | -47.70824 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6133cd50-c9a8-3944-8e9a-edfe656cdb7b | -21.6271 | -47.70313 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e423f431-6e95-3884-8eae-3e99d786e7ac | -21.62671 | -47.70769 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8af444cc-7cd7-3ea6-82a1-01f2fb0945cc | -21.62526 | -47.70354 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd207d88-1775-3607-a96d-7a5e704cadd7 | -21.62484 | -47.70808 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0143c928-0696-3fef-a0e4-d6d7ab2fceca | -21.61801 | -47.71633 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e20b8534-d5fc-3ed5-a521-21b41ac9f3ad | -21.6172 | -47.72524 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6bada974-85e5-3247-9649-95e4f0a1d7ac | -21.61315 | -47.7243 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 79aa305e-741d-3512-9383-c58ffd82d058 | -21.61275 | -47.72901 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 49a8fc0a-6f3b-353c-91d5-0778fd9cdda0 | -21.6115 | -47.67166 | 2024-10-09 05:06:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 084d25b2-f908-3a9e-a223-46a34df80dc1 | -21.61117 | -47.72476 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6d38dcf-da97-3b41-a8d1-50968c98d348 | -21.61109 | -47.67645 | 2024-10-09 05:06:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2446e80b-17ae-3fab-8d35-568094259b65 | -21.61073 | -47.72952 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f23936a-1f1f-3c5f-bb6d-62a63850576d | -21.61068 | -47.68142 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da003c6f-83ef-379f-b52c-ac67043c6f11 | -21.60986 | -47.67217 | 2024-10-09 05:06:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c3989758-22ec-3ed6-ab3b-8ebd4cb81aab | -21.60942 | -47.67701 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| de6669b6-0521-336b-8401-4c494bd7b793 | -21.60897 | -47.682 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d058b96b-eaf1-3647-8b31-e4ab0ef827e9 | -21.60719 | -47.7016 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3df1eb6-d947-3462-8652-2bc2c055946b | -21.60546 | -47.67102 | 2024-10-09 05:06:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 053b5f6b-316d-3454-80d0-08517964d6f0 | -21.60505 | -47.67593 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 30eff1bc-7520-3131-8381-8adf858df9da | -21.60463 | -47.68092 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f68a82b8-fe45-3b03-b716-6bfb62b66bcd | -21.60299 | -47.70064 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f404b2c-de87-3acd-9f36-b4d60fd1e96a | -21.60159 | -47.69634 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e49e1f4-0db6-3055-af89-dc9750875f16 | -21.60073 | -47.7058 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee7e50f6-f649-3a8d-b11b-deb21ce49c7b | -21.60032 | -47.71043 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b714070-d811-3372-a268-cc377e8ae6da | -21.59738 | -47.69502 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fdde139-67fa-33f9-8329-10c7a6a81c30 | -21.59655 | -47.70493 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42e40140-bad6-30cc-b479-a4b0b9e3c8ca | -21.59614 | -47.70992 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c98a03e8-90d2-3698-b6c8-21f3f9d35b60 | -21.59558 | -47.69553 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b52a1cf4-f4a1-378d-94a4-b4915fcbe27c | -21.59468 | -47.70557 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1357d52b-c410-34ae-8a93-a6a1fe3b8327 | -21.59422 | -47.7107 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42c44a07-a4f9-3231-9742-700b8b3a333e | -21.58204 | -46.98193 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7e8c2c8-0108-38c7-9768-791a757f8a1c | -21.58185 | -47.8804 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 098f2cc3-9543-33de-9ca1-b55a2e4b100f | -21.58146 | -47.88503 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1bd961f-cfa4-357d-b2a1-262bba8bbbb6 | -21.58107 | -47.88965 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba66018b-81f2-3e23-8ac6-34847007782e | -21.57885 | -47.88061 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a14382ab-a325-3a99-9de3-972301bdcee7 | -21.57847 | -46.97961 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ebb6b3d-df1d-3331-a237-af1b2a4cfc80 | -21.57843 | -47.88523 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a937f33-4357-3a0c-90f0-5b79079a9a16 | -21.57806 | -46.98422 | 2024-10-09 05:06:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d237a46e-f2c0-3523-9530-4450d832f036 | -21.57801 | -47.88984 | 2024-10-09 05:06:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README190.md)
