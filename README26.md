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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35b70754-0476-3e13-991d-215eee5883ee | -8.30045 | -71.13423 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d61e6059-baab-3f5c-8241-173c16c99b66 | -8.95385 | -69.11012 | 2025-09-23 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1550ad43-8a26-3369-a650-d120fdc28d4b | -9.47378 | -68.52718 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db4c7bb7-7115-32ef-b1fb-b4e143edc9ec | -9.27829 | -71.94704 | 2025-09-23 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28253184-c6ec-3c6f-9d76-070656fc366a | -8.30547 | -70.5666 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c5f280-c020-3730-b5a1-762a08052700 | -8.30346 | -70.83743 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ed74759-255c-3641-9c76-4051e781069c | -9.17231 | -67.67667 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc498d0d-5f43-3858-ad82-3a48c0bf2f6e | -8.88384 | -69.22878 | 2025-09-23 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 453bf2f5-ed18-3945-b3e4-9d8532178205 | -10.20166 | -68.59433 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 164702c0-ac5c-3bb4-b35f-eddc46f114da | -9.73365 | -68.88961 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7441f09c-db0f-39ba-a2e8-786aae50fb82 | -10.24663 | -68.75732 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2925e6ad-8d5d-3511-8e5f-83d1e60d0ec5 | -9.25314 | -68.24615 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ffbb979-4fd2-339b-9d03-569bc117f2f4 | -8.89356 | -71.33435 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c295f750-8d25-32d3-9d83-79cfbb440c11 | -10.88783 | -69.42038 | 2025-09-23 06:01:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80873c1a-b017-3e51-bf19-b6a756f51550 | -8.2554 | -70.90444 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce227e87-4153-30ec-b57d-5e086de0db86 | -8.43197 | -70.19537 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73a617e-3e3d-36cb-8b0e-ecdef3db27ee | -8.86807 | -71.81456 | 2025-09-23 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78608d3a-9441-350d-8720-45a700c002f5 | -9.14083 | -67.81334 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3df8d51-fdf1-3cdb-83c8-9eeccfb737fb | -8.81522 | -70.78021 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3b0e31be-1252-3640-9e4c-baab0429dc51 | -15.9654 | -59.48491 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d50db9fb-ca88-3b1c-bab3-b78247f4b117 | -9.46711 | -67.12906 | 2025-09-23 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1bfd170-5324-3a3a-b37f-434d5d71fca4 | -10.05912 | -68.45557 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09ed7813-aa61-33cb-8b17-eedcfbf3bd0c | -9.88815 | -68.86315 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 166a4308-4a34-37c6-851a-c51d3051702d | -8.37025 | -70.75891 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b5ee57b-8623-3340-ad0a-341047e1ddac | -9.37712 | -68.81701 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2ac39d3-ee49-3f0f-a93b-d0659f5102e3 | -10.62071 | -68.85577 | 2025-09-23 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7a84271-f388-3788-9d5f-e3e3ff137c67 | -8.94966 | -71.26052 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8f90929-8ee5-3c99-acfb-324211875c66 | -8.38021 | -70.84613 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c0bf36d-aca0-3833-a52b-da875b477f20 | -8.89688 | -71.33488 | 2025-09-23 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9c0b599-26e2-3e64-90d6-891455ea1763 | -15.91658 | -59.36891 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfa61049-beeb-3214-bfdb-644c24163522 | -15.91194 | -59.37263 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae81eb4c-2c0e-3dff-b736-4f5dc1d3b546 | -7.89636 | -71.7504 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 220fa6ef-62b3-32cd-9efa-cb260b581994 | -8.23828 | -70.81953 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0d75ef6-a76c-3b0c-a69b-41ccb0d454cc | -9.88472 | -68.86261 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc28e52f-0ea7-3016-8721-e0fa23a36bf3 | -9.55642 | -68.55835 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 207a4b0b-3962-3d8f-949d-7326eab77a4c | -10.05505 | -68.45894 | 2025-09-23 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e23be3b3-18ca-35bc-94c5-d6bf480d7a73 | -8.33768 | -70.72874 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68bdc482-719c-332f-91e4-bf6c6c443c3c | -9.3782 | -68.78665 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ccc76a-c9e8-3819-8ada-8fc10634690a | -8.07536 | -71.28947 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3739eb40-8251-3ba7-89c2-24dbb5ac7234 | -8.31612 | -70.92879 | 2025-09-23 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e8130cf-0ea7-3d18-9821-4b77a7794c5b | -9.11237 | -68.32046 | 2025-09-23 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ba2b39-9d62-3ad1-9ad7-e7bdc9f3f98e | -9.65149 | -68.71587 | 2025-09-23 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d294db6-4e75-3be9-b0c7-b5668ee1a9f0 | -15.96493 | -59.48965 | 2025-09-23 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90cb50e2-c01c-3f28-90d6-6533bd9bede7 | -3.63235 | -51.90315 | 2025-09-23 06:40:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 37bf3c31-8085-34df-b8c3-8361ff3698cb | -9.27615 | -57.1629 | 2025-09-23 06:40:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| edb3fd1a-d9a8-3e8d-96d8-598312cff1ce | -6.33583 | -56.19458 | 2025-09-23 06:40:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6ef38387-ca1e-3483-92ae-77fdd567d753 | -3.63189 | -51.9084 | 2025-09-23 06:40:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7f7f182a-7795-3fa3-9928-dab6abb66de9 | -6.34478 | -56.1959 | 2025-09-23 06:40:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5d869897-c0f9-32a6-939b-166efc052756 | -15.83247 | -59.59256 | 2025-09-23 06:42:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a26aa328-5cff-3bc3-888e-2543d8e0d934 | -15.35911 | -59.17421 | 2025-09-23 06:42:00 | AQUA_M-M | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 612fe87b-5b26-365c-8baf-82a38bc2b13d | -15.94911 | -59.48737 | 2025-09-23 06:42:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4f142e61-c071-3d40-97f5-063152da726d | -15.83384 | -59.58347 | 2025-09-23 06:42:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ab13e89d-1a70-392f-879e-45db972cfa22 | -15.3476 | -59.19097 | 2025-09-23 06:42:00 | AQUA_M-M | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 456a27df-24cf-3ba0-9dba-348d36dc3c9b | -15.35776 | -59.18327 | 2025-09-23 06:42:00 | AQUA_M-M | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e05c6cb7-0f76-312e-ab97-10cb4aa2c83a | -15.82366 | -59.59117 | 2025-09-23 06:42:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00f3d2df-1480-346d-8961-f7024c812080 | -15.95927 | -59.47967 | 2025-09-23 06:42:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5be4915f-2731-3075-b898-6bf791581660 | -7.9885 | -70.90996 | 2025-09-23 06:52:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5641bd3-5458-3a94-b88b-f761b138b470 | -7.98919 | -70.90445 | 2025-09-23 06:52:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e46932e-1938-305d-ac02-c59060aed20b | -7.98881 | -70.91035 | 2025-09-23 06:52:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3731ae30-e3c1-3ea4-bc8e-d44de8e6176e | -7.98953 | -70.90485 | 2025-09-23 06:52:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2020a11-6b28-36db-a457-a9e704e68bc5 | -12.7375 | -57.8831 | 2025-09-23 07:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 569c25e7-1077-354b-990a-be7a9ea4cae9 | -12.7185 | -57.8847 | 2025-09-23 07:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e17bd93f-e011-30ea-937b-10749fd3be94 | -13.4294 | -47.5477 | 2025-09-23 07:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 70583bc7-1b42-3a0e-8f70-bda42039d299 | -13.4294 | -47.5477 | 2025-09-23 07:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4be596fb-86c1-3f16-bf76-b48ecb715bd4 | -15.9578 | -59.4888 | 2025-09-23 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 499b9bef-4d55-3a0d-b6a3-1c93a2acaa00 | -15.9578 | -59.4888 | 2025-09-23 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| a7a2ccac-6334-3fd1-adbd-ba763013a5b3 | -15.9384 | -59.4907 | 2025-09-23 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6e961bce-3ffe-3150-b784-218bd3532e31 | -15.9772 | -59.487 | 2025-09-23 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4682bcc1-709b-3ec1-a6a4-531baa8bb6e9 | -15.9576 | -59.5089 | 2025-09-23 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2cfd73de-3c30-31ec-a748-73eb82bc4a54 | -15.9578 | -59.4888 | 2025-09-23 08:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d0370349-2daa-3e38-b843-ac64fa344b78 | -15.9576 | -59.5089 | 2025-09-23 08:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 06534081-b260-305d-8b1a-281427867bd9 | -15.9576 | -59.5089 | 2025-09-23 08:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 7a124504-19ea-34ea-a801-6759ea80ed32 | -15.9578 | -59.4888 | 2025-09-23 08:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 895cbbc1-4dec-36ab-b8fa-68efe27851bc | -15.9576 | -59.5089 | 2025-09-23 08:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bbca0785-c9ae-31d3-a638-0d2b17b24fd0 | -15.9578 | -59.4888 | 2025-09-23 08:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 683e7653-2d68-31e7-9baa-67f6274cc197 | -15.9576 | -59.5089 | 2025-09-23 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c1422d69-4971-356a-b181-6abb01a43fcd | -15.9578 | -59.4888 | 2025-09-23 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3e2b247b-8937-3601-afe9-867eaf5ddb44 | -15.977 | -59.507 | 2025-09-23 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 23c143fd-15a7-34ae-bac1-8240142aee39 | -15.9576 | -59.5089 | 2025-09-23 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| d287f225-b914-3fd1-b222-d8c863a8428d | -15.9772 | -59.487 | 2025-09-23 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 922fa686-9b4e-3bac-b8db-9cc0712341b5 | -15.9578 | -59.4888 | 2025-09-23 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 6cf7a75f-111e-3bc0-8ec3-ce091998547c | -15.9578 | -59.4888 | 2025-09-23 09:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| fa308cea-5ed3-3c12-ae55-a6bfd6b21024 | -15.9576 | -59.5089 | 2025-09-23 09:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6c8f5bd4-0bbb-39f1-b934-e1daa6cbf3f8 | -15.9578 | -59.4888 | 2025-09-23 09:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3762af35-7eab-3b5a-8a5f-492bbbba97ce | -8.2803 | -44.3801 | 2025-09-23 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0c5177c7-e764-32e3-953b-455bb200d924 | -8.2803 | -44.3801 | 2025-09-23 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 484e3413-f001-30d0-a1eb-9abe305b949c | -8.2507 | -39.52275 | 2025-09-23 11:36:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2337b680-8a6f-3e44-aaf4-06889f225119 | -7.85632 | -37.63487 | 2025-09-23 11:36:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0b136b03-0c5f-3e5c-8aee-1b8f7a6dd45c | -7.35346 | -38.86488 | 2025-09-23 11:36:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 1425bc8a-5cb6-37d2-b907-71ec7b348868 | -7.34567 | -38.85387 | 2025-09-23 11:36:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 969bb523-616a-39d4-96a1-19f46e491d5d | -8.29662 | -40.15467 | 2025-09-23 11:36:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 21.8 |
| ab77ca72-e248-3fe6-ba65-15eb5398f81e | -8.35064 | -39.47126 | 2025-09-23 11:36:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2d8271a2-27d5-377c-9c42-bffe9d4537b4 | -7.68414 | -35.03199 | 2025-09-23 11:36:00 | TERRA_M-M | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2e1c6382-c2be-301f-bee2-09bb7294d2b6 | -7.44627 | -39.95813 | 2025-09-23 11:36:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 6d07bedc-176e-37d7-93fc-9bb1d5417af4 | -7.34422 | -38.86358 | 2025-09-23 11:36:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 367e0781-0507-39bf-8ee2-86355841197b | -7.29637 | -38.56554 | 2025-09-23 11:36:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 891cd7e3-959e-3697-a860-3174c64b70b7 | -8.34732 | -36.59595 | 2025-09-23 11:36:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 22.5 |
| cb1829a2-7af6-3e3a-8ad3-95f252338028 | -4.93906 | -37.71832 | 2025-09-23 11:36:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| aeb3f8f8-3093-3887-8c5d-9bff5c8581b8 | -7.1548 | -37.89519 | 2025-09-23 11:36:00 | TERRA_M-M | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1788c869-075c-3617-9340-ad3d41c2ef74 | -8.15911 | -38.15384 | 2025-09-23 11:36:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |


[Clique aqui para ver as próximas entradas](README27.md)
