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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20e107d2-2699-3e69-913a-ab8698f7c068 | -9.01705 | -52.10246 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daa5a39f-7efe-31bd-97dc-5ee5c6f7db8f | -9.0165 | -52.13041 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecac6fd9-e00b-340a-a802-3becaf14d70b | -9.01299 | -52.12989 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cc541ec-2d42-33f6-8b9b-53ed64ab652c | -9.0118 | -52.08929 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f870ed11-eb39-3e59-b243-d6c22f6c3a2f | -9.00828 | -52.08885 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bb2a8d5-8599-36d2-b418-eb15bb8337b4 | -9.00755 | -52.08942 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c71fe599-ca12-3828-b03a-265ae7c00d45 | -9.00416 | -52.09241 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa5aecd6-5b65-31f8-afd8-75eabefc5167 | -9.00341 | -52.09297 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78740ce8-f957-31d4-ba7b-40e7f4cf6b4d | -8.95123 | -52.1293 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44f6183d-caf0-3156-9fb3-72adbcb2c933 | -8.9483 | -52.12492 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5773057-fdd4-33b6-a9a9-19f9e8e2243a | -8.2257 | -51.73869 | 2024-10-04 04:55:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46b13325-f0f4-3f06-b937-82192cf89819 | -9.84553 | -52.06921 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db2323c9-2aa0-3ad5-a47f-1e8e713cb763 | -9.84493 | -52.07323 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c651ef2-51b2-3d5d-ba84-d187698e3c9e | -9.84434 | -52.07722 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f231c5f-3b6a-30a2-9edb-708c0d53ad5b | -9.84312 | -52.08532 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5b692f1-f3da-31c1-8df5-1f1d2e59b09b | -9.84199 | -52.06863 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a49ad06-36ce-3fa8-94c2-a5f48ca11087 | -9.84138 | -52.0727 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ec83b50-f826-3a97-8404-0bf2efd37f86 | -9.83907 | -52.06391 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c869a938-fd25-35ae-a379-6fcbbb55f4dd | -9.83897 | -52.08882 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f3d29b2-3845-38d8-8420-a0e6abec6dbe | -9.83845 | -52.06805 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48adea1a-cbf7-383c-893e-ce85d8b906ca | -9.83544 | -52.08823 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a415232-7705-32fb-9074-caf8c851dcaa | -9.83485 | -52.09219 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09c9583a-8543-373d-852a-0a608af25ec2 | -9.81126 | -52.05566 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c0ccce8-ce4b-3c4f-9cc4-3060716ffec9 | -9.80772 | -52.05506 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e26b8625-7c91-3bb6-8ad8-6910443ed647 | -9.58337 | -53.26744 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36ea112c-2962-36c3-93a8-c6d296c0ec45 | -9.76387 | -53.16642 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38d3fac7-77d5-3321-a1b7-ed3b829cb75d | -9.76047 | -53.16589 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24019439-8c24-3fc2-adcf-989a1995d84e | -9.75707 | -53.16537 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25455b91-55e9-3a06-8459-aef7a0381bdc | -9.75367 | -53.16485 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab0cf834-7077-3328-9c74-a4f56425d231 | -9.69047 | -53.18602 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44bb29a2-37f7-3bcb-bc56-4970c203a3c6 | -9.68934 | -53.17075 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce5824d7-4383-34f5-ad4a-b4cd89b3c193 | -9.68877 | -53.17443 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11b331dc-8d9a-36ee-8caa-7ebe7784bbf4 | -9.68765 | -53.18181 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8d8e6c8-23cf-3c6b-8bf0-0f129825e5c6 | -9.68708 | -53.18549 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2a64acf-5d6d-3f32-9c27-b091f7d4fd5a | -9.68595 | -53.17022 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec86e1b-97e7-39e2-9eb6-5ffa07d0e98a | -9.68538 | -53.17391 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ecae14e-67f8-3865-9cf0-75864838dd3e | -9.68482 | -53.1776 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13a97a91-558d-3d6b-aa10-24a42ffd7a75 | -9.68425 | -53.18129 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42a337f3-c628-3040-ac33-3bdb574a6d59 | -9.68312 | -53.16601 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10aabf1b-44e0-3f30-a5f8-370e2634e1fa | -9.67972 | -53.16549 | 2024-10-04 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f527feb-b081-3e6c-890a-b33398df11e2 | -9.61534 | -53.20071 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb3a0355-3622-3187-b351-ddd4e189d466 | -9.61195 | -53.2002 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc7efc9-bd1c-3347-b828-e6d2310cdf12 | -9.61139 | -53.20387 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c164d16-960e-3be2-b869-39587fd1a8ce | -9.59127 | -53.26825 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 64d30f81-f713-345d-af6e-bd59078dc663 | -9.57943 | -53.27057 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d3a7f9ad-6beb-39a7-9510-26f3a7852903 | -9.57604 | -53.27005 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 587290dc-556e-33f5-8c9b-6a08c147a4b7 | -9.39538 | -53.19724 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28a19bcd-7e26-3911-88fc-51925299e50d | -9.39255 | -53.19304 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5973177a-0c0a-32a5-9638-90998d9853a6 | 3.23494 | -51.21098 | 2024-10-04 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff73414e-1be7-30c2-95d5-2c16f7bfcf36 | 3.2344 | -51.2075 | 2024-10-04 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9f83149b-9743-3f66-81cb-cff6a33c51e6 | 3.23385 | -51.20403 | 2024-10-04 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 57c5a0f9-feee-302a-bbb1-046d4162fb09 | 3.23108 | -51.20802 | 2024-10-04 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bd3fcfb-710f-3a77-971f-bf53044541a7 | 3.22776 | -51.20854 | 2024-10-04 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b9bb1bb-ed9b-3c82-b5e0-44d77fdaaaf1 | 2.40073 | -51.67509 | 2024-10-04 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff9ffe28-4ebf-36f1-a679-f9fe5e781003 | -2.8524 | -53.31615 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce66db4e-fcbd-3ab0-90f4-41562b3ac1c2 | -3.12698 | -52.92953 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00b39a6d-c585-352a-8b67-dfdc3344f994 | -2.9558 | -52.7859 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d6b6f6e-6479-39c7-92e9-82f3abeaa1ab | -2.95303 | -52.78193 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5888478-908e-36bd-a014-8ba58deedb1e | -2.95249 | -52.7854 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 022d6d56-e4df-3e27-9ee7-d17c0d28073a | -2.95195 | -52.78886 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 387688be-f8ac-3c12-967c-dbc535dccb4f | -2.95026 | -52.77795 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebec4866-6708-31b9-895f-07d75e8af2c0 | -2.94972 | -52.78142 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23b378d3-1e23-343a-b1ce-9f72ae8bc822 | -2.94918 | -52.78489 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44ce4a7e-2db5-3dba-b826-2c4de70834d5 | -2.94907 | -52.91565 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb524670-2f2c-331c-ae43-2a94cf423f9c | -2.94864 | -52.78835 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1d97413-59c9-35f3-b8b9-ebf73cd1c508 | -2.9463 | -52.91169 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6e29c1-a666-36f1-a73b-0072de9310fe | -2.94586 | -52.78437 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7d960b6-ceef-3439-9edb-9c6d6e102eb6 | -2.94576 | -52.91513 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f47a3704-ba39-3cad-83c0-19f3026ed917 | -2.94532 | -52.78784 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1e3b3fc-31b5-3dcf-a9e8-926420028622 | -2.94245 | -52.91462 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 624f7102-a44b-311f-9982-264684e18840 | -2.94191 | -52.91807 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04af8c8f-5b2e-31d9-8396-c5f179918436 | -2.94137 | -52.92152 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f07c4e6-0888-3e8d-9375-8f9a7a7151ed | -2.93914 | -52.9141 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 395ddfc8-63ec-36fc-aae0-89dfcb3582c6 | -2.9386 | -52.91756 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf368b71-3eae-36c7-8fb9-abdf004cde24 | -2.93637 | -52.91014 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ec52528-be70-3fa2-88bd-a3ecbbde327e | -2.93583 | -52.91359 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f315454-016f-3710-88e2-cb830f43e60f | -2.93529 | -52.91705 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40606725-7b5f-3bf8-971e-5e99acea7265 | -2.93484 | -52.78975 | 2024-10-04 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c8f9a06-10b5-3ea1-913d-eed125ab5481 | -3.82631 | -52.34542 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46cecba9-6cd0-3072-8138-457af07f2fe2 | -3.82296 | -52.34489 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e445b82-f98f-3812-9529-550c280630da | -3.76271 | -52.33547 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56cd5f1a-7a1f-3b76-a234-cdca1a93dc51 | -3.75936 | -52.33495 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e87ad986-499f-31e2-9f9b-6b629a35c27f | -3.75803 | -52.26204 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc5d89a0-dc7f-3cb5-b431-d3fb48395148 | -3.75584 | -52.29793 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6cd1aed-fded-3b6d-b61c-2189ba89fe50 | -3.75529 | -52.30147 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9c681de-41f5-30ba-8fad-b230ec2fe7fe | -3.75249 | -52.29741 | 2024-10-04 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af662fbf-2157-3e7d-9ab4-cb15b49b5cea | -8.70936 | -54.8247 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b2362b-090c-390a-85f5-5021e3fd350c | -8.70881 | -54.82817 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbef82da-8f41-3502-9226-96920d19ddbf | -8.56191 | -53.32996 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdb46b8c-06b8-349f-9e55-d2bbbf0b81a7 | -8.56136 | -53.33353 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3674add7-ee21-3e40-8684-8a94dff76282 | -8.56081 | -53.3371 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50aed1ac-b027-3f2e-a667-849399ff3667 | -2.13696 | -53.65179 | 2024-10-04 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8149e7df-faa7-3fc4-8529-8ab2e1c14726 | -2.13641 | -53.65524 | 2024-10-04 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99aff099-169d-30c3-9ce6-da33789c38e7 | -2.05111 | -54.36684 | 2024-10-04 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99890bff-f79f-3d91-82e1-7877071694a8 | -3.50456 | -54.02906 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 585b4cdc-720b-31d6-82b5-10927c44aad5 | -3.50402 | -54.03252 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74da8996-d8a9-3304-b71b-b662181c05f5 | -3.3759 | -54.11145 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee53d2e7-7ea7-31a0-bd64-db7527958a50 | -3.37535 | -54.1149 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b895f9ac-3341-3e9d-af6b-08b1c8e3a948 | -3.32891 | -53.76435 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a2f44cc-6858-3bf0-a8cf-b6d61867b260 | -3.32561 | -53.76384 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README149.md)
