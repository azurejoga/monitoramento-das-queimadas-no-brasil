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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 387316de-3e05-3528-80a3-82ddd7858abb | -9.72822 | -65.08366 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c46f6b0a-5ed6-3e00-a3be-90d9d29681a9 | -9.07572 | -65.38917 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0235dff6-65a8-3594-b3fd-2248f45cc4ff | -12.88596 | -62.18445 | 2026-10-06 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca32c9ce-089d-3785-b9f1-8df4a721b6c4 | -6.59088 | -55.28063 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 012b0e35-3fe9-3550-a956-9f8bf7824db9 | -9.16153 | -67.84808 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d81b699b-b575-3711-a4c5-ba93b3d40658 | -8.3982 | -70.10863 | 2026-10-06 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffa77c9a-0b0b-3ac1-8512-cfbd960a8969 | -3.54066 | -60.52083 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bc373e5-cfbb-34d0-a273-6ef46eb2b0f5 | -9.07649 | -65.38455 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1be98d93-93e8-3152-bb5b-1e9d99ec3458 | -4.45384 | -54.96219 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c95169ff-b464-31ce-97a5-8c39a87f98e7 | -3.75248 | -59.42329 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89de9d8e-101a-3290-925e-34bac59709b0 | -5.81376 | -53.83778 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dde8e32d-4f33-3b52-8016-4678cb3bf334 | -4.81367 | -54.73102 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 847eee1a-94b1-398d-9f06-c94eab71af30 | -9.14211 | -65.29173 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76e38da-2381-3a19-9149-3af58668f534 | -9.02167 | -65.71014 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e0f56bc-a869-3afa-abe0-7eaeacbe3e7f | -9.16344 | -68.2556 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45932a69-d8c1-3691-a85b-24bd2a5916ac | -9.1352 | -67.81828 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74deb575-8ae7-3412-a9f4-e2b896d3b9ab | -9.10446 | -65.35609 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 823eb92d-0204-3cca-9f36-d5c5e36ca4dd | -9.34186 | -64.71461 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20217be7-cee5-3581-aa02-fb0cb585a52e | -5.67352 | -53.5018 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f53c8caa-7818-38c6-b4f2-ca6b99dae16c | -9.17337 | -67.67464 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071b6643-f349-30a3-8122-e3b39a4ea914 | -8.85038 | -66.79041 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9029d86-3b68-343c-a423-db0001135c03 | -4.44804 | -54.97276 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97f0535d-ed61-3e98-ad76-3c2b8f6c2c03 | -9.62318 | -65.73911 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5bfdf1b-107b-33f6-a7d9-cd916382d3c4 | -8.62973 | -69.5022 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7298cd22-07c0-3bab-a1db-14ad59d62582 | -8.77896 | -69.53646 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e3090de-4161-3ae9-992b-cc2c5769a3c1 | -9.15228 | -68.23938 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec118c0f-5362-3b69-a7f7-7be7fcd3df73 | -6.21805 | -57.77309 | 2026-10-06 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f85849cd-ebf4-3dbd-a4e7-f630ffeef2a3 | -9.48108 | -67.09374 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fadf6f24-e4a5-31fc-a88f-796e916fb2f2 | -9.02085 | -65.71499 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ced97c2-213e-360c-afbe-0b6b7a3cc837 | -9.04148 | -65.43107 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6d27c5a-9293-37eb-9eb5-850388e0bbfd | -9.2311 | -67.89169 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| febdfa06-9690-3510-a68b-3d4177d689f7 | -4.56668 | -54.95218 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 196f5a27-9977-30b2-95a6-3178cf362bcb | -13.49951 | -61.13502 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 119c854f-d57a-3015-be64-a06a0d1dbb12 | -4.46102 | -54.96338 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0af2d14-8d52-3259-86d5-a2c30201a34c | -9.02551 | -65.71082 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebb128e8-b9f0-35a8-a05a-1e8f77b5b899 | -4.45281 | -54.96209 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8009928-9531-3d53-be0d-0fa647a7a9e1 | -8.4346 | -70.11506 | 2026-10-06 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c0ff2e-11ab-3e05-8091-cffb9c75c336 | -9.48897 | -63.95271 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c8bf33e-14e8-3e47-aebc-107e887885e3 | -10.87795 | -61.40503 | 2026-10-06 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 197c0c06-433a-381d-87e9-f3489c2b529e | -9.48832 | -63.95662 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7b7488-4340-3244-b841-1aafa1fa8ea2 | -13.52012 | -61.11223 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba2be507-bf67-32f5-b543-0fad1c1cc894 | -12.87879 | -62.14364 | 2026-10-06 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 750eac97-2607-38af-8247-a8b7ef79c5d8 | -4.28026 | -55.76152 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edc46006-e7f3-33ae-b4c1-cbf1cae05257 | -10.64244 | -68.60036 | 2026-10-06 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20c9f6d6-032f-304c-bd7c-8983b68729e5 | -8.86935 | -68.50583 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62666a95-0ead-3add-a079-1960038b8777 | -9.67286 | -66.82533 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2e8e5d1-4722-32dd-aa82-ad016b8f743c | -6.01008 | -53.50804 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1db2768-4615-3143-b239-091861ea91af | -8.62375 | -69.50704 | 2026-10-06 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13f0171a-6eee-3b81-9de3-4fadad099a72 | -9.33761 | -68.79111 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf04527a-500f-364e-b60e-bca0a4a6b947 | -10.03223 | -65.2603 | 2026-10-06 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d77b1d-1d0e-31e7-87ac-d61e7fa25992 | -9.7275 | -65.08805 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0dbb095b-85d0-3782-8de3-5db7cd9785a6 | -9.48225 | -67.66933 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d4459f2-5878-3a02-af9f-e943bba938a6 | -11.99299 | -60.47346 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed424533-3357-318e-a506-e0f388c87871 | -9.46283 | -64.32881 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e266170-c04f-300d-9404-889a12d77745 | -4.46567 | -54.96026 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1310fae-921d-3805-a837-22228a333181 | -5.68343 | -53.49852 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0b8f766-42a4-3380-a2f9-9bf999638829 | -9.35617 | -67.4389 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e006de-0c91-38a6-8274-4f230234ec7e | -9.15891 | -65.56489 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efd83d6d-b208-3460-9988-9c062c57640c | -10.6965 | -69.63203 | 2026-10-06 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35303bde-9eec-3932-8f70-350e20615d67 | -5.81826 | -53.83864 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 235b9e00-2a27-3ddf-b76a-f066662f916d | -5.81619 | -53.84147 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2913983c-e915-394a-be61-e8a1fa1fc158 | -9.19493 | -65.32747 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bce4c941-332b-3ed9-bc0c-90f3ab50fec9 | -12.1363 | -63.15765 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27909c02-3260-3204-b022-c7f9c5c474a2 | -10.44497 | -67.89875 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 808e6a0d-64a4-307e-9f27-263dd6af1081 | -9.16902 | -67.67387 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c3a9c3c-bb50-34b1-9673-da1e727f53d9 | -5.67953 | -53.49273 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25560915-e0a2-3bd7-b001-8487d3ecf4ab | -8.79964 | -68.70823 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b35b7fbc-110d-350c-886a-2057e8dcc087 | -11.3708 | -60.71872 | 2026-10-06 05:25:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b526805-4b6b-3e86-807e-f12e24b575a1 | -9.67758 | -66.8224 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b8f1d66-052b-36ff-bafb-15ba8af6e42b | -4.38195 | -55.16255 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a92f2473-f2e4-3a28-ab77-4d1c4c0541fb | -12.60989 | -60.90369 | 2026-10-06 05:25:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbfcda54-e082-3059-a888-0cbf05955295 | -4.37166 | -55.42187 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a1e624-d87a-3ddd-a189-c6464b0a0041 | -9.13324 | -67.75113 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6404fef-ac90-37e6-80bf-4453300c3840 | -3.89455 | -58.74363 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7508495a-550f-39de-b564-65f49a1ad727 | -9.36853 | -65.80137 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c044c772-815a-3d85-9b3c-74e68a1c2f02 | -10.44378 | -67.89539 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49441922-4048-37c3-a457-8d963806ef16 | -9.4931 | -63.94938 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba3a21a6-440e-311f-9cd8-e50034348489 | -9.6237 | -65.74167 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a98c8f11-7bb6-3bf6-8584-88d9b2cbef7d | -9.43741 | -67.09814 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f87769e1-a4e1-31c4-a4e9-53f0b158a204 | -10.87741 | -61.40853 | 2026-10-06 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db9b1a17-35dc-3d8b-9fde-168f56a537cc | -3.97625 | -59.34084 | 2026-10-06 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b884ec3e-9d26-3192-9b72-94419557d38d | -4.38413 | -55.60242 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84d99a17-19b2-3cc2-94c0-2ccc14d6539b | -10.27554 | -60.54472 | 2026-10-06 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1be4eba-631c-3759-ad08-a542208e0a8b | -9.95491 | -68.77738 | 2026-10-06 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 416d3c4d-45db-3170-9ee7-ba2915ca6111 | -3.65178 | -59.72242 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c1041b-6291-338f-b287-c1bd2dc72b9b | -9.72237 | -65.09628 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8397f6a4-d6de-326a-9ff6-a5c52aa2a47f | -3.72427 | -59.4083 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f07bd51-78e9-3ba2-8bfe-5e466db8d998 | -7.82095 | -72.83504 | 2026-10-06 05:25:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1bd9e2a9-30c4-3190-b0db-fad8ee9a6971 | -8.924 | -66.84628 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 352cf95d-1f6c-31b3-bd63-56c571b86d0d | -9.14635 | -65.40908 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5effc74-6419-34cb-9821-f400498eec0c | -9.13249 | -67.75545 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a089c9f2-daaa-378a-8cee-175af4a50b05 | -3.76897 | -59.40453 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f8f9a64-bd8c-3abe-b3e4-58fc5b3d5c69 | -4.81062 | -54.72997 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d06755e1-a1cb-3dcb-ae9e-abf0ee9e375b | -9.48656 | -68.94538 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4695951d-8981-3ca4-824a-1632136152af | -9.82336 | -65.05305 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4b586be2-852a-3ac2-86b8-6280ed4ecd32 | -12.13572 | -63.16123 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eea947a0-b2df-3547-a05e-453f9ee364af | -9.80419 | -64.98741 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90ecf9c4-50d8-3453-8780-bfd5739b97c2 | -9.36045 | -67.43962 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce742d1-d40f-340a-be48-6619e50530b0 | -8.75721 | -68.97134 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80596c0d-25d5-35ee-a241-6657a1e0b73f | -12.87824 | -62.14716 | 2026-10-06 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README65.md)
