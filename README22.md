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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cabc0c53-e689-3d69-868a-5266322de4e5 | -9.90558 | -42.10243 | 2024-10-21 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 32dc2aa4-ed40-31c9-9144-15c463152659 | -9.90169 | -42.10176 | 2024-10-21 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 00ecf93f-7d57-3147-9bab-d10e03de5a7c | -9.2878 | -35.63658 | 2024-10-21 03:49:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e60289b5-173a-3d41-8b0f-5a2ddfe12f5c | -8.77356 | -40.57962 | 2024-10-21 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3ec899b2-7068-371d-b56d-4622ec92a624 | -8.53819 | -44.73663 | 2024-10-21 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af36fb5a-2978-3de0-9cde-b04a07f9bb5f | -8.07311 | -34.97725 | 2024-10-21 03:49:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 322ae505-7007-3cc0-bd30-a2560402129a | -7.91077 | -38.39653 | 2024-10-21 03:49:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c6e84004-b017-3e61-859d-5abe6ba7f604 | -6.27623 | -37.82094 | 2024-10-21 03:49:00 | NOAA-21 | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1751f1e0-497f-32d6-95b3-f81325a9a8c3 | -5.87535 | -40.16549 | 2024-10-21 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ce12e14-4b39-3676-a2d1-8c2b948be7f4 | -5.87465 | -40.16985 | 2024-10-21 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9154958-d08f-347f-b210-92d543ad5775 | -12.78168 | -38.49951 | 2024-10-21 03:49:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5afffac2-859a-3e0c-9f1e-7dfb942a9a38 | -12.42932 | -42.49023 | 2024-10-21 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9dc9459-35b8-3956-99f9-52aaad962dfe | -10.90271 | -40.53611 | 2024-10-21 03:49:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 22869026-269c-3dd6-bc30-d4b6940ca75c | -10.61073 | -40.52213 | 2024-10-21 03:49:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 14b7e697-3f4d-36ed-a4dd-ed722a31d011 | -10.28638 | -36.30759 | 2024-10-21 03:49:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a38f6ec4-8942-379d-a24c-8190a65edc01 | -10.07958 | -36.34909 | 2024-10-21 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 65bc5417-cd89-3482-b526-a24ef1036862 | -10.07903 | -36.35267 | 2024-10-21 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 41b03b1d-6fdb-3113-b21f-3919b58b6bb1 | -10.07623 | -36.34857 | 2024-10-21 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 14.3 |
| e73ef836-7b0e-346e-bbe4-37a6b6417c23 | -10.07568 | -36.35215 | 2024-10-21 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 14.3 |
| f0594f1a-4596-3665-8a7a-d6adf11eff52 | -7.18137 | -44.9682 | 2024-10-21 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a3bc5f8-390e-365c-a91e-c0ed2d13b116 | -6.83035 | -49.13699 | 2024-10-21 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 537597d6-aa59-3360-8ed1-7c46e50b3779 | -6.83004 | -49.13739 | 2024-10-21 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b9a0007-6c89-3079-9c17-c27d727fbd7d | -6.00874 | -44.52552 | 2024-10-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 094c0d00-6249-3584-85c6-7f897e738b43 | -6.00739 | -44.52274 | 2024-10-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d15afff2-6316-397e-aa22-e8e59203a7f6 | -5.69383 | -46.43197 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 888d3f82-5002-3c56-8fc7-0f3a21c97aa8 | -5.69006 | -46.42599 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a58a08aa-4ed9-3196-af6c-bdc13d7dafa6 | -5.68958 | -46.42373 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7bcdf542-e3d9-35ce-b016-6b593efafa67 | -5.68945 | -46.42956 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 25986c2d-70e6-3b0f-8b1a-e46b790c53fb | -5.68895 | -46.42725 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 73b1eb73-3bc4-35de-9d2b-a84aab80f7d0 | -5.6888 | -46.43335 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| e7cad909-698c-39b8-83e9-c26012c856fc | -5.6883 | -46.43087 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f52c99c5-ebc3-3578-b611-3427be96fc49 | -5.68762 | -46.43464 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0ef2eabc-feff-3ec7-b5d1-5ef32e32ed35 | -5.6845 | -46.42506 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e6a91fd1-c074-31e1-8bc0-a7b098d8cd78 | -5.68258 | -46.43619 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 94aeeaa1-b5c8-33e9-9c8f-0c99c2b474d6 | -5.68136 | -46.43758 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2e522a7-234d-3134-8870-9dde7de2feee | -5.66265 | -47.00288 | 2024-10-21 03:49:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 907f60d1-4f24-3ca0-b4a0-b5d4c1c45221 | -5.4358 | -46.35281 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96d6c840-8c38-3bd9-9836-784873cf2974 | -5.43517 | -46.35641 | 2024-10-21 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 437d8628-829c-341e-9c60-2788cec78dd3 | -5.2827 | -49.29926 | 2024-10-21 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c85a36b9-f83a-3a91-830e-e5487c56d4c8 | -5.27889 | -49.30051 | 2024-10-21 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea773eb9-ae6e-3713-a14c-d1e0527b5376 | -5.27598 | -49.29827 | 2024-10-21 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52d9fc8e-06be-3a6a-bdf7-f20d7cdd0745 | -5.00433 | -47.65568 | 2024-10-21 03:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 019e5955-a5cc-30aa-8666-1c5042646360 | -4.92025 | -45.88438 | 2024-10-21 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7982380c-d06e-3985-9470-37f27011d1db | -4.9197 | -45.88763 | 2024-10-21 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c09b8a0-865a-3f68-8034-3d14ce30c757 | -4.84016 | -46.88578 | 2024-10-21 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47b28450-0b22-382a-8176-cd7a5387a303 | -4.83938 | -46.89035 | 2024-10-21 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec8d7aef-ab01-35ba-909d-41142a1c0466 | -4.41701 | -49.80277 | 2024-10-21 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d40fbebf-d6d8-383d-85a3-f0247ffd28c1 | -27.23544 | -52.57591 | 2024-10-21 03:55:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d163525c-577f-3e60-ab3b-43bfab0a292c | -1.2018 | -53.6366 | 2024-10-21 03:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e5e9c33c-ba1b-316c-bc97-a51a7604a41f | -1.1834 | -53.6368 | 2024-10-21 03:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 170c478d-fedd-3e59-89bf-dc6a512428cc | -2.4824 | -49.102 | 2024-10-21 03:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cfaf8e39-15ca-3d4b-80a2-23e5f64cc489 | -2.4824 | -49.1233 | 2024-10-21 03:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 983b34e9-f4ce-32e1-9b8f-a42d0f862fd8 | -2.905 | -45.2143 | 2024-10-21 03:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8d728a8b-f41d-3bfe-8175-09432b570417 | -2.8372 | -53.3261 | 2024-10-21 03:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1f42f50d-0584-3304-beb5-5382924fd938 | -2.8069 | -51.3613 | 2024-10-21 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 126931ae-1833-389b-9965-0b066daf66f0 | -2.7773 | -49.3067 | 2024-10-21 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a522d34a-f8d6-31e4-8a74-1d94b3bbeb58 | -3.2146 | -50.8093 | 2024-10-21 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 31236111-8ad0-35fe-a18a-642650086ed5 | -3.1138 | -53.1163 | 2024-10-21 03:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0ad0ab73-289c-3965-9141-b8ee4c4d5d00 | -3.1137 | -53.1366 | 2024-10-21 03:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 0f511ad6-98f8-36e1-a422-72d7191fd5e4 | -4.2544 | -43.7149 | 2024-10-21 03:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 2440073d-79ba-36b5-86fd-372e455ee5d4 | -4.2542 | -43.7381 | 2024-10-21 03:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c59db69e-d9ab-38fc-826e-c29856f6379b | -4.2357 | -43.716 | 2024-10-21 03:55:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c7631f6a-9cbd-3be8-85ec-f3f399eb7d49 | -4.2356 | -43.7391 | 2024-10-21 03:55:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5be51e2e-e515-3288-820d-f5a46fd9bf1c | -5.6894 | -46.435 | 2024-10-21 03:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 136f4b99-875d-3df3-9e37-6e89566a3ecd | -12.5336 | -63.3003 | 2024-10-21 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 721cf1b1-f508-3b7f-bd3c-29ce36cdbc1a | -12.5147 | -63.3014 | 2024-10-21 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7711971a-3dd7-3964-bc7b-b280c80af1fd | -18.2828 | -56.0994 | 2024-10-21 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| eff5f099-c9dc-3e05-a878-272600b6b95e | -1.1834 | -53.6368 | 2024-10-21 04:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 24e6feac-5ec6-3aab-bd33-4e5af1f86fd2 | -1.2018 | -53.6366 | 2024-10-21 04:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 6d0e9c68-e776-3fe6-9a05-62e49497835a | -2.4824 | -49.1233 | 2024-10-21 04:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9196e9b9-af58-3dbd-9094-03ba1ed3cc63 | -2.4824 | -49.102 | 2024-10-21 04:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bd73cc91-cea9-36dc-8006-99f9655fd680 | -2.7773 | -49.3067 | 2024-10-21 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d25aa40a-eb76-3fdd-86e4-f584393db64a | -2.8069 | -51.3613 | 2024-10-21 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1faa4042-d34f-386a-952b-2b4727b40624 | -2.905 | -45.2143 | 2024-10-21 04:05:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 3f3aa72b-ef57-3695-9f3f-f8d54d77cba1 | -3.0037 | -53.038 | 2024-10-21 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 9ac97d72-d59a-36bd-afc4-610afa5df7e1 | -3.0581 | -53.2395 | 2024-10-21 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| d03120fd-4cd0-3df9-a25c-b5d4284c1a6e | -3.1138 | -53.1163 | 2024-10-21 04:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| b957372e-bf5e-3c5b-9e61-81654d09e740 | -3.2146 | -50.8093 | 2024-10-21 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e86e5463-38cc-31dc-8611-727dbbd5866a | -4.2356 | -43.7391 | 2024-10-21 04:05:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b6667e5c-b9cc-3ab6-8ea5-6318e15f011a | -4.2357 | -43.716 | 2024-10-21 04:05:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7d21155d-0b0b-3b54-91a5-76c31ed81553 | -4.2542 | -43.7381 | 2024-10-21 04:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| e67e5709-dd52-3910-828d-4366546de4e8 | -4.2544 | -43.7149 | 2024-10-21 04:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d0b1016b-287b-3b3b-8bbc-5f9bf7d31d48 | -5.6894 | -46.435 | 2024-10-21 04:05:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b471563c-6103-334d-80a6-fc8febd972a5 | -12.4778 | -63.1885 | 2024-10-21 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 8e0469c1-db76-3665-8d21-293aba939907 | -12.5336 | -63.3003 | 2024-10-21 04:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| ea2af481-75d9-3e93-8e26-842a2e30a6d8 | -12.5357 | -63.0319 | 2024-10-21 04:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| bd41c746-33b9-3847-802f-802d13051c12 | -18.2828 | -56.0994 | 2024-10-21 04:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| a45dfc01-e41f-3638-bdfa-b3156216e51d | 2.91689 | -51.00104 | 2024-10-21 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc89bc54-c8e1-3067-9785-3c211ee34fef | 1.83302 | -50.49594 | 2024-10-21 04:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f8b18577-312a-3594-9715-6c1f3fba6ab9 | 1.83248 | -50.49244 | 2024-10-21 04:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5d1b51ea-558e-3039-ae78-22eb2f4f70cd | 1.83194 | -50.48894 | 2024-10-21 04:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60cdcf38-bc19-3f65-a90b-46c6c356e45f | 1.82757 | -50.49681 | 2024-10-21 04:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b07bcbf-965b-3328-ae5b-0751497762d2 | 1.82703 | -50.49331 | 2024-10-21 04:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fc51cc2-04ff-3637-9450-228a9226cf91 | 1.01595 | -51.14677 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc2b7dd3-926b-3e20-9506-75cec4b585ca | 1.0136 | -51.14952 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34692407-f0ae-3d54-9600-0b6ce97d3f8e | 1.01301 | -51.14581 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac611a8-8cae-3769-9e47-ac492f66653f | 1.01145 | -51.15506 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9027d436-b539-356e-b796-e95974923ffc | 1.01088 | -51.15133 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a682032-cec9-3f7a-a7f8-6d7d465bfaa6 | 1.01032 | -51.14761 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5964242e-35b4-3aef-a7ce-98320f6a5af3 | 1.00915 | -51.15782 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
