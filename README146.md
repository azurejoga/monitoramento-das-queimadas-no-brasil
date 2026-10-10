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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fc249dd-6095-3891-b4c4-551acfb245fe | -7.48342 | -63.451 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7084b9d5-2fe6-3332-a947-84d6b460339d | -6.48698 | -55.96714 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3e5b825f-f0ce-38ef-9486-dadf4adb1552 | -10.59792 | -60.48364 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5c91a07e-fba6-341f-a71d-d5937d7dac36 | -6.9526 | -59.36481 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e1148b8-580f-3979-9ad9-20ed20b3dc82 | -10.55782 | -69.18391 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7de4a98a-2405-32f0-a328-fcffb0d0497e | -7.91068 | -54.72421 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5efa675c-02b7-3936-ba29-6dd052f92db7 | -6.70468 | -58.71231 | 2026-10-10 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b23fd63e-1002-334e-b14a-cf723c6e0d37 | -6.46291 | -55.48372 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7229fea-720f-3603-9b48-1c7dab9840a7 | -7.69924 | -73.10436 | 2026-10-10 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb745c31-be2a-358b-9f04-c2acd40678a2 | -7.90545 | -54.71178 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbbb388d-06ce-39cd-bd24-7dd064e1ec77 | -6.94669 | -59.11352 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dea097e2-d438-3bd8-936a-2568983f84f2 | -7.92259 | -54.73735 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb9293f4-ca41-36b3-bbef-95683bf89166 | -6.22664 | -60.03865 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a5e97b7-ad17-3dec-b37f-889b7ddb77ac | -7.45551 | -63.63926 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13350233-aeb5-37d2-9e48-b16fcd23c71b | -10.62354 | -67.92671 | 2026-10-10 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3f94847-3051-36b7-a7ad-961d38ebbbd4 | -7.20906 | -55.08687 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8745666-c525-3abf-93ba-b5b34233a805 | -7.09503 | -55.73055 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d3a84d-11eb-3099-81f4-92d027dc61d2 | -6.61861 | -59.94543 | 2026-10-10 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c81efd5-e742-3537-b31d-289be9ad3301 | -8.53667 | -66.97475 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d36dca5-e839-3a54-b484-277e8c515c2b | -6.2234 | -60.02835 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd84bee6-788d-3291-a9b0-103a72612e29 | -6.45469 | -55.49802 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 553f3c05-c603-3929-ae82-e3a47def5c3b | -7.4985 | -54.99522 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d83bed00-6e98-3a4f-bdbf-86eb55587321 | -6.9425 | -59.10702 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bdae8f19-3d2c-347a-8085-ca892385aa67 | -7.08772 | -59.76854 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a35a0dc-0a5a-387b-a627-072cd254702e | -6.22271 | -60.03317 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967acb89-734c-3c6e-b6b1-e5d087c8c13a | -6.94258 | -59.09932 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c38e9f0-398e-34fc-aa19-8c67ff20f134 | -8.18804 | -54.71384 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 409908e6-ad74-3f40-82f0-9f275288679c | -7.44507 | -63.55579 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d565de6c-1c3d-34da-9e02-807fd9f92778 | -7.57166 | -61.54005 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ac1b2a7-38fb-3fb1-9211-8bbd395a1676 | -7.45419 | -63.64812 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b17dbd80-b0e3-30bd-8ad7-f35221e41215 | -7.50607 | -54.99372 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 24e3b9a9-682f-3c05-a574-6c5195978ccb | -7.00442 | -59.09882 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55eb77ce-8af4-377f-9bed-58ed9e737ba8 | -6.62054 | -59.94445 | 2026-10-10 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ef0aa0ee-6afa-3e0e-932e-d918d6155d9e | -8.5909 | -67.04033 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad395598-4f46-307a-b224-13e3484f6056 | -7.50534 | -54.99923 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2249b367-5941-31de-b1c1-1ee6e23e1f38 | -6.8881 | -62.998 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64f441e2-80ea-3f6b-a982-69438f670e43 | -6.94591 | -59.11152 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abe0a942-4f9d-38bc-8d25-c35f92ce7722 | -10.16443 | -69.0687 | 2026-10-10 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77893611-89d0-30a9-a15a-93447557bbe3 | -8.50399 | -54.60818 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a6b7149f-073b-315a-a60c-6efe0765e40b | -12.29716 | -63.3742 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c412386-cdbd-34be-9556-0de843300dad | -8.18728 | -54.71995 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ed792f9-76fc-34e8-b5bd-402801c9ed9e | -6.04826 | -59.91032 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a668b034-2709-3773-9926-8af474bf2197 | -8.22767 | -61.1764 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8afb1c08-d399-34ea-84fc-29a6f6120342 | -9.39468 | -68.98381 | 2026-10-10 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 420d28e2-7380-3a3b-aa24-e96651c7aec5 | -6.49064 | -55.31839 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1c672a6-48b7-377b-9c5c-674fa45756aa | -9.08899 | -61.05503 | 2026-10-10 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a97a7fb3-a905-35e3-8422-420a58ea8da2 | -7.95937 | -63.05621 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1be48af-23c7-3cc5-87a7-570c0227ae49 | -7.00502 | -59.0945 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5caa1840-9724-3a6c-b9ac-28a1ddf583c7 | -8.51814 | -67.02897 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44ae031f-7889-3451-8fcf-2bed2e766e26 | -8.52091 | -67.03297 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e213ae40-f028-3daa-aa22-1d91d031797f | -6.46158 | -55.49401 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3e324116-43a4-396d-bacc-27eac823fc4a | -10.61359 | -60.47538 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ddb4794-dae7-32f3-8871-6cc7fc70a500 | -7.9181 | -54.71925 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03d6ef6b-a7b1-348e-99c0-612dbe544f57 | -6.70427 | -58.71532 | 2026-10-10 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4fbbbea-28d1-38ce-a5de-4b92abec32ac | -7.6999 | -73.10045 | 2026-10-10 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b050086-85c9-3af4-84d5-254f8453c0d3 | -6.62447 | -59.95015 | 2026-10-10 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0cc379c-ae90-3adf-b09a-2fa71329c37f | -9.25667 | -62.3088 | 2026-10-10 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac9b6e6-d57e-35be-b2b7-e138205aa3fb | -8.62431 | -66.78062 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51117cbe-9033-336b-abec-449252230d6e | -9.95649 | -55.33261 | 2026-10-10 05:50:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7181efb2-301a-39db-a1c9-ec24cc093d20 | -9.2572 | -62.30503 | 2026-10-10 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf855c6b-ee02-3083-a018-38484e42352a | -8.93102 | -62.40636 | 2026-10-10 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b880c87-fd8e-30ff-8b26-0ae9516498ad | -9.67931 | -68.67361 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd8f041a-b45c-3569-abcd-ff0411a3414b | -7.70151 | -61.36079 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf1ad3c5-ed6a-3c7b-9d4b-36416005d313 | -6.44284 | -60.03445 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3f10f33-d0e2-3364-af17-e7fe4225f231 | -7.89156 | -63.77781 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bac4bd4-e5fe-31c3-92f3-e92f6b5d0430 | -6.13913 | -59.92999 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09e4c3e5-ae7d-3498-9399-6ee961691e81 | -9.07018 | -61.29123 | 2026-10-10 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32e6d245-e565-39c4-b01f-6121f716e7f9 | -10.60407 | -60.47392 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c92e2ebc-11a4-300b-aec0-33e8c51aeeeb | -6.04434 | -59.90471 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf9d2851-79fb-33cd-a90b-2dc18df9cee5 | -8.52475 | -67.03001 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 140ed4d5-be4b-3bf2-813e-fc42b10389cf | -8.50051 | -62.69247 | 2026-10-10 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59061b66-dd2a-3d47-8c9f-a12a2fef5387 | -7.56406 | -62.33177 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dab7cb58-22ce-3a32-b5dc-e1d1d19e16a7 | -6.70976 | -58.71306 | 2026-10-10 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dcc0a0f-804c-3be0-9967-3915669728db | -7.22764 | -55.14666 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5e842e3-ac7d-393d-b5ee-48956c4f96a1 | -9.84691 | -68.86044 | 2026-10-10 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26d48b52-f295-3342-b43c-157018f67f70 | -10.61765 | -60.4813 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da23a22-848c-3731-8f9f-4d58f5626e4c | -6.42765 | -60.04184 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8f54544-7969-3163-9d33-edc08319a45d | -9.25614 | -62.31259 | 2026-10-10 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e735f50f-67fc-3586-8c26-d924895f7057 | -6.89573 | -62.99914 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0a9793-eace-3065-94a4-3ac86f2a394a | -10.41176 | -69.14135 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a7d4586-e2cd-3aab-85bb-1cd8e70709e2 | -7.56004 | -62.33118 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eabf80b-ef3d-35f1-ba2b-34c4a5ef8266 | -6.47151 | -55.51576 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f0e8fc3-3a31-3024-9e67-954c15ae6371 | -7.93002 | -54.73242 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 10ead94b-2006-36f3-81c1-0d05e19eec0f | -6.62326 | -59.94619 | 2026-10-10 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fbad38ee-36fc-3acd-b377-a79a4854b4b2 | -7.93439 | -54.72595 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7a52add6-419e-3ea4-bc08-807560ad0773 | -7.90325 | -54.72916 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5467618a-7b06-3eb1-8f12-3db05bac4d33 | -8.53336 | -66.97424 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94dba351-0a94-322f-8dae-2f4fac5b4103 | -10.56624 | -68.46873 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3f5aa7c-37f4-3f9e-b785-2665e94a623c | -6.04896 | -59.90547 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52223c3a-d275-34b2-a6f6-4e181adfb0c9 | -6.94746 | -59.10775 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7146a600-692f-3a12-92c1-08883b1fb2fe | -7.2184 | -55.06569 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 86b46fcc-325e-3e36-832c-d66340ade955 | -9.0884 | -61.28949 | 2026-10-10 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89fa429d-3123-37e2-b48e-a1cb86be4b06 | -8.23085 | -61.18559 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31e0c39f-82bc-35dc-8ea5-203dbc594276 | -7.09354 | -55.73272 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09ec7065-401a-3758-a0c1-92f8c5e2a1e3 | -10.63417 | -69.30657 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e609c7bc-e1ec-36f7-9ff1-8825f74cc62f | -8.63095 | -66.78165 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78bc0fef-bd43-3af3-a8e7-25660e1802e2 | -9.46487 | -68.54498 | 2026-10-10 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2ecd7d7-fb8e-39d5-9369-bdbae42a45b8 | -7.09292 | -55.73755 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f2dfd6-96f5-33d8-81ca-73f3a8766da1 | -7.95551 | -63.05562 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bf73b44-9317-3d8e-b329-c592f2b736c7 | -9.21093 | -57.72696 | 2026-10-10 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README147.md)
