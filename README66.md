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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23f8fc62-c730-3511-bfba-90eaae772c6e | -17.97354 | -57.42575 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f0a5ffc8-12a1-3742-85e6-c03a63443d4d | -17.93666 | -57.44908 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fee3a155-3ade-3867-a7ce-8ec9aa5e06ed | -17.9361 | -57.45573 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c09fe19b-1921-339d-9fad-f90ca2e943bf | -17.92338 | -57.44104 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8f5bf2bf-19d3-3d6f-a477-afc36b872834 | -17.90844 | -57.45169 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1e00b6d8-f6b8-3c93-82de-92943e0225af | -17.90785 | -57.45831 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0ff75544-6928-3806-92b7-7a0727c3b390 | -17.90152 | -57.45102 | 2024-10-17 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 686aec28-2bad-308e-b91a-b70c63f3198d | -17.90094 | -57.45764 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 423c014e-3fd8-3ba1-9e20-a417c4a29837 | -17.89403 | -57.45694 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a5369858-4745-3537-a7d5-1bc8c0f00f20 | -17.86532 | -57.46751 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0abdee1c-d872-369a-ab3f-e56d723b5350 | -17.86525 | -57.46747 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fa16af97-4f46-3270-8197-0aed57ff108d | -17.8647 | -57.47412 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 291ae9ab-bba9-31ae-83f0-0af79f973dbc | -17.86468 | -57.4741 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6acb5a90-c256-3a5c-b07c-6db2fdfa3737 | -17.85841 | -57.46686 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 763e7c3a-b47a-3d22-84f0-d51351a510c2 | -17.85835 | -57.4668 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d5ccbdae-5789-3887-bd2f-68fd153cbd8d | -17.8578 | -57.47349 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 41438365-8d86-3bcb-bd46-25f1982f1172 | -17.85777 | -57.47343 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3cdf7468-55c1-38d4-a4d0-0f73fd5f93b9 | -17.8509 | -57.47284 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 377779cf-d297-33c8-83c3-2d37d293e436 | -17.844 | -57.47219 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2a1ce012-95d0-35f5-ac5f-017aa0fc69e9 | -17.84398 | -57.47207 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4441ca4e-0ea0-3aa0-b89b-f0a401b96d64 | -17.8371 | -57.47151 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 39d9a83c-2949-3771-9998-fc5f651cbe03 | -17.83708 | -57.47137 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e924f92d-7ba3-3472-9631-1618f3bb0b51 | -17.8308 | -57.46427 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 303e5953-a9fa-3908-ac10-1c72e5697a26 | -17.8302 | -57.47085 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| eac5eb81-43fc-37e5-aa87-79d6e460ea90 | -17.8164 | -57.46953 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1e23e857-9c91-3f67-bd09-217e27ba28fb | -17.81638 | -57.46931 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| b41c7e2e-aaf6-3b63-b9cc-7c3ff2466d52 | -17.81581 | -57.47613 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 89354416-532a-3d47-91b1-8743239236dd | -17.81009 | -57.46228 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 03b26a6d-a0eb-3d66-af02-8ac11276e4c5 | -17.81002 | -57.46202 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 4521798d-2130-38f6-91f3-4e7e4e8e422a | -17.80951 | -57.46888 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| c8793326-3367-3381-bc2f-3ef77d79539f | -17.80947 | -57.46864 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 2ff45e00-e512-3fa5-901a-e08f3ca91b2c | -17.80732 | -57.41526 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| a251620f-1e9c-334b-a3f7-20fbbd519658 | -17.80673 | -57.42191 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 5c3b562a-9e28-36f1-ae19-95b57d269c44 | -17.80378 | -57.45502 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 609cfd12-d1e3-3d31-b7e4-bbd5215372c6 | -17.80319 | -57.46165 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 564d1721-58c7-3688-ba5e-ab0b45e04e31 | -17.79981 | -57.42124 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 45b77341-1158-386e-ad5a-7f95e4854263 | -17.79746 | -57.44775 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| c05db039-34da-3668-8447-e6ea6b3f1a93 | -17.79688 | -57.45435 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| f0f1a000-1deb-3ef3-9be8-0ab8fd8404b1 | -17.7929 | -57.42058 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 71623ad7-5c98-32b7-b4b9-b00794098541 | -17.79231 | -57.42721 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f8579931-0552-3d6e-b80d-20ad081dc020 | -17.79173 | -57.43383 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 58fb0f64-f4d3-3ae2-802a-8f208b816ece | -17.16896 | -56.81993 | 2024-10-17 05:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cb19ba1f-70c8-35ba-9070-764444df9a09 | -7.34392 | -59.79057 | 2024-10-17 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b328838-4e95-338c-827a-6216c065a496 | -7.34348 | -59.79379 | 2024-10-17 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bb28528-b7b6-3b75-95cd-ab23fa304387 | -7.33859 | -59.79041 | 2024-10-17 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55490ab5-3683-32c8-95dc-880f11a8ecc3 | -7.33816 | -59.79362 | 2024-10-17 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d2fbf72-b9d6-3028-87ef-cdc2a2c24f4d | -7.01371 | -59.35644 | 2024-10-17 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72e9bc08-06d5-33aa-8f9c-da5353483f31 | -7.00881 | -59.35231 | 2024-10-17 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 282a389d-dfc9-33a1-90ea-84619b3e10cc | -7.33292 | -72.50428 | 2024-10-17 05:55:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a79ba169-19ec-3a8a-975f-fcd6a3f81483 | -7.25224 | -72.48164 | 2024-10-17 05:55:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8af664d7-6a9e-33c1-bf3e-3cde97399ed9 | -7.24852 | -72.48095 | 2024-10-17 05:55:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e4af757-f62f-36ed-a6a7-23d3350824d0 | -6.92487 | -71.48473 | 2024-10-17 05:55:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a2aa7e-7752-3871-80c1-0af40fc4b34b | -9.68153 | -68.58904 | 2024-10-17 06:40:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa05e622-828a-3569-b4ee-30f706599148 | -9.67202 | -68.58755 | 2024-10-17 06:40:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6caaf8f-6e43-3468-9860-c16e74568258 | -9.6302 | -68.66662 | 2024-10-17 06:40:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c1c385dc-a0d0-3320-ad8b-a68cb30a65c5 | -9.57584 | -66.63868 | 2024-10-17 06:40:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19579bdb-3fca-3093-b924-ac6ca3f9c7cc | -9.46918 | -67.08928 | 2024-10-17 06:40:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9fac62ac-fbf1-33dc-8e7f-ab3c208e5d80 | -9.45185 | -67.1429 | 2024-10-17 06:40:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aa5996e9-b199-39f5-b887-54ea01296f46 | -9.39525 | -68.98069 | 2024-10-17 06:40:00 | AQUA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 28a307ac-10d7-322e-b778-775a079aaf03 | -8.45672 | -66.95092 | 2024-10-17 06:40:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 193a610f-43f6-33dd-91e9-4648b0e4a5b2 | -8.45532 | -66.96011 | 2024-10-17 06:40:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b1674f9b-06b7-3e97-ab82-33cc88483e29 | -11.87442 | -64.93285 | 2024-10-17 06:40:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c9e09b3c-7331-319f-b8c5-6cf65a0f82a2 | -11.87304 | -64.94255 | 2024-10-17 06:40:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| fb0ae37b-f066-3e52-866f-fe49e4a874b8 | -11.86524 | -64.93152 | 2024-10-17 06:40:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 19acf0e0-6119-36fa-a111-f6c7c82152f5 | -11.86385 | -64.94122 | 2024-10-17 06:40:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 0b299545-6591-3256-b54a-51c8c0272f67 | -11.73182 | -64.96886 | 2024-10-17 06:40:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 386a75a7-a8cc-38ea-b8cf-902f6da5cc54 | -11.48895 | -65.11621 | 2024-10-17 06:40:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 306e1465-111b-35b2-8f15-b58778e1d6a3 | -10.86005 | -68.26067 | 2024-10-17 06:40:00 | AQUA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0c3fa000-79ef-3cc9-8239-285355c52223 | -10.58498 | -67.76927 | 2024-10-17 06:40:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 0fa923b5-22de-34a9-90e2-7345f9521946 | -10.38806 | -67.89838 | 2024-10-17 06:40:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3ee01e3-838f-3f5b-ac32-1718ac3895e7 | -10.35786 | -67.98538 | 2024-10-17 06:40:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13f3d67e-8316-35f0-9c32-e0ccb4a00260 | -10.35461 | -67.94543 | 2024-10-17 06:40:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc439da5-d2d0-390e-8617-2e4e27ca8854 | -10.34868 | -67.98396 | 2024-10-17 06:40:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9730c09b-0ea5-3a01-8876-3174ea4b4477 | -9.76807 | -68.80538 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 803542a8-6fcf-3da2-8562-f00e22efcd6e | -9.76734 | -68.81157 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d44b750e-25a9-36bc-9bed-8fe3f9a9311a | -9.76656 | -68.80645 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cc77fad-8e76-3cb1-af56-c0d2c43fa715 | -9.7658 | -68.81262 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdfdb5cf-adc6-3c2b-a1e0-61d93dca6a65 | -9.68337 | -68.56918 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2127464-727b-34f4-a74f-218fefaa7b5d | -9.68109 | -68.58881 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e70dbb47-9a5d-32f0-b6db-cab895d5fb4d | -9.68037 | -68.59507 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ab67b83-ab55-399b-a99e-b8bab720b959 | -9.67646 | -68.56831 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c77630d-e924-3d94-b943-6493666c05fc | -9.66731 | -68.58676 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7bc51a43-8d87-3acf-aa7a-7ee772b0a1a6 | -9.65501 | -68.57176 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cc9010e-affb-3833-88e5-a5103a0a6ba0 | -9.65501 | -68.57071 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 152869c3-f538-3923-9b16-19072bfb46b5 | -9.6481 | -68.57088 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6a4a28a-8d1b-38de-a2f4-03efcb1c1bea | -9.64809 | -68.56989 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e62277e-4985-383d-8995-93745663cc9e | -9.637 | -68.66805 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e960ab87-327c-38f2-b087-61b42ad79f6e | -9.63637 | -68.66684 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e5ddbd7-3c5a-327e-aa5f-9618d9301075 | -9.63015 | -68.66699 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8885d69-f7af-37d9-a7bf-5301221d8c0a | -9.62943 | -68.67331 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fe04ef2f-a549-3f38-ab83-16e2af959d44 | -9.62876 | -68.67216 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0288340-8140-3d11-a122-b5cb0672cf0d | -9.5237 | -68.72839 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42ae301f-2d94-33b1-bbf4-b80d617cb486 | -9.47938 | -68.57025 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 813d86b3-f2bb-3547-9385-77cfc936c62e | -9.45945 | -68.56144 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16dd4536-1384-3a55-83fc-5ad6420429b3 | -9.45865 | -68.56791 | 2024-10-17 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ec5bcfb-5ba4-3d31-a809-21880200a32b | -9.40121 | -68.29375 | 2024-10-17 06:46:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71066eec-0229-3504-a11a-740aa7a75c48 | -9.39923 | -68.29824 | 2024-10-17 06:46:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f8c2248-899d-3057-a858-2ed9ca75f629 | -9.3934 | -68.29944 | 2024-10-17 06:46:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b74cea26-96b0-3ee9-bd7f-d2e1195bffc9 | -9.39146 | -68.30392 | 2024-10-17 06:46:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cff1fac5-50bf-38c0-a003-d3ba7b882e79 | -10.29 | -68.84764 | 2024-10-17 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README67.md)
