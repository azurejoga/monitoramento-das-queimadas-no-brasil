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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f303815b-6882-3317-a95d-9082b38781ff | -15.739 | -51.17813 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a73d45d5-00cf-33ee-ab40-85df4e20aa1f | -20.68592 | -50.48326 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 1700fdcb-5069-35e2-af4a-101b102136f6 | -15.728 | -51.18032 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 76edd729-ef0b-30c4-bfe6-d0534afd3d65 | -14.9452 | -49.04039 | 2026-08-28 17:43:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a7769fc4-ab23-34a2-88d7-ff5595e5f6f6 | -18.35387 | -54.9915 | 2026-08-28 17:43:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 766a04e0-b7bc-3d4b-ae16-b86e199f4249 | -17.59525 | -51.64029 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 5da685ce-b8bd-3505-b116-5cc4e7d65612 | -14.49153 | -53.40028 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 028e0093-95ce-3c34-a07c-13aeb5e4a50f | -10.1651 | -68.61843 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 81168c85-b3ce-30cf-ae08-02ea57fb7431 | -13.31788 | -48.20141 | 2026-08-28 17:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 45afe62b-6266-3efd-906a-f6dfc9a16939 | -14.88497 | -52.62528 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e8993f78-9215-35dc-a304-4c8d1501a675 | -10.76385 | -53.98051 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bf941997-09cb-3ad1-9ba0-b336fe4dece8 | -9.1347 | -60.91658 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ac8cb05-bbbe-38c1-bf8a-a6073070ada8 | -11.23416 | -53.98511 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 0ae57c8c-7dba-3d71-8bc2-4b8901ae7ddc | -10.57292 | -69.69102 | 2026-08-28 17:45:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 421e366c-b287-3834-aff1-fec67e770b92 | -10.57105 | -57.48584 | 2026-08-28 17:45:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 97f966fd-21c7-3a11-bc08-ac79ec5d89d3 | -10.85079 | -50.2146 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 593a690d-219b-3039-953f-d809027ff796 | -14.16145 | -52.83749 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 724cbeda-cefc-31ec-9d51-7f28dbcb8246 | -10.55106 | -69.83392 | 2026-08-28 17:45:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d9918222-1809-39cc-9a71-3ec1f5a3ca88 | -8.5907 | -54.79033 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4b6d6c22-9d3f-3b81-82ae-59a9e34aad9e | -9.46457 | -60.56244 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| cbf2dfcd-5d27-323a-a897-963b1dbdb9b4 | -9.23079 | -59.77251 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e616cbf8-a936-362a-a763-b70bbeaf4aad | -10.44243 | -59.6093 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec99628f-1aa9-33be-94a5-a63300c6f880 | -11.71455 | -54.53786 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 231a3c5e-4eb0-3823-b0c3-85edcf0070fd | -8.58688 | -54.82663 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 616b3106-eab6-3fbc-9bd3-60a46fa50a40 | -8.56007 | -54.90448 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c3a69e95-bc90-3d0d-8220-913e671a6820 | -9.25335 | -57.08227 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eaa473b6-b417-3e32-a24f-f5dc2a67f98f | -14.43248 | -53.38289 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 1b7e7fb3-4787-37f1-93bc-fb9e765042a2 | -10.51632 | -59.61873 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 777ee394-28af-3514-925a-bf9e6697dbae | -8.5918 | -54.82575 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 856e2cb2-03ff-32f7-93a4-08d33613a4f0 | -10.51319 | -59.61846 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 984ad49e-c929-3c28-9d3c-25215186c8cb | -14.89124 | -52.6303 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 803f6792-6ead-3b0f-ab41-5f68899e82cf | -9.86449 | -60.26528 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bea7f434-2c44-3011-b8ac-02cacf077304 | -10.5145 | -59.62662 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| cdc42b61-a752-3c9a-8146-efca38ec4926 | -9.92762 | -60.43659 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 514.2 |
| 4b694b93-379e-39d5-9399-876852bb4fe0 | -14.43306 | -52.58788 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b72a0e46-ad19-316e-9656-5103242c9d2d | -11.71549 | -54.54309 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5317c15b-9c62-3aa7-81f5-bd24d528214b | -10.5367 | -50.77365 | 2026-08-28 17:45:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aeb1575f-5615-341b-9eb0-5618ebdc77e4 | -9.1393 | -57.56141 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f89ded5d-ca79-3082-91e8-007f7a295b28 | -9.85056 | -65.01205 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| aa93bd43-f387-3c1f-8ca1-e51e4f6b55d0 | -9.15894 | -49.97071 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ae2ba532-5bf3-3cb6-8a6b-128851def38a | -9.13529 | -60.9203 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7441a858-3bb8-38cc-8db6-c8b6403ddaac | -9.76488 | -64.97276 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 143e7038-e1ea-3613-a9c0-e2c3ba55ddc5 | -12.98522 | -60.08887 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c82ac2a-443d-362b-b185-a7e321540551 | -10.77051 | -69.51304 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 76001cf8-1b71-36ae-9c20-cd71e7e393c2 | -14.186 | -52.85538 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b15b8cdc-005a-3dad-b929-7f2da58fb18e | -9.97357 | -53.93455 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 6cabcdfc-0070-363f-99cb-d34efba2f772 | -14.92109 | -56.31457 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b2bfe1e6-6817-345c-99c9-743e29b521f2 | -9.02365 | -57.54486 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 6ab4f75a-603e-34a5-8fc3-a6a4f48f17c3 | -11.35349 | -48.39261 | 2026-08-28 17:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1be54439-8a11-3c98-9b17-8097eb34fa4f | -9.96039 | -66.81998 | 2026-08-28 17:45:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e5be9311-cab7-39e5-8382-059b11ae420e | -10.07917 | -68.55373 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0cbeb2d-af85-35c6-b9fe-b2debbb9609f | -11.93888 | -62.4052 | 2026-08-28 17:45:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca444a38-54a7-3bee-a9bd-46f1ef3efbfb | -9.42028 | -50.44859 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fba9166f-03c6-3a28-8c75-eb79675c0cb6 | -9.9763 | -53.93434 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b3630a6c-d3f0-3581-9a90-625701d5602e | -11.60741 | -50.20057 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46c17463-2f6e-3c8c-9f6d-de7188395736 | -10.33283 | -69.17075 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 43890ffc-d39d-34b5-8bce-29d268aa8bdb | -10.50017 | -64.50108 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ded5d065-ad29-3934-bf37-6bb1c74b883a | -10.5116 | -59.63128 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1038e0ba-1019-39de-bd66-9c1ab851ba4c | -14.52025 | -56.50959 | 2026-08-28 17:45:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ac5fb81-829d-387c-a834-0ab82e74a03e | -14.87525 | -52.60251 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fc57ae3b-7e7f-394d-a301-4a3b4942d5b2 | -10.20276 | -69.35815 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 32.3 |
| eddd0cf0-6ff1-3288-9993-f61f0e8eec10 | -9.11672 | -61.60096 | 2026-08-28 17:45:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 719dea5d-e5b7-3306-899a-8f059d46c6bc | -9.19738 | -61.09267 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7ed4d8cb-ed42-3b87-97f3-ae386879237f | -9.9264 | -60.42898 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7ca780f0-6d65-35c8-a282-dd720b0e2081 | -14.18577 | -52.82659 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dceeb099-9e3a-3545-85e2-f7115b7fd564 | -13.46866 | -57.04108 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 624a0241-f289-3d2a-901d-dfe49913a97d | -9.4337 | -51.69466 | 2026-08-28 17:45:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f3bec5ff-f8e5-39e9-8580-24a109f1d175 | -10.25899 | -64.5022 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40764a9c-8ac4-3b91-b37d-2395510f738b | -13.42819 | -51.76843 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 85fb26b5-ed32-396f-9787-649812fe0642 | -9.93046 | -60.43222 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 336.0 |
| a685bb4b-ea12-31c6-bda0-71d160313771 | -10.60314 | -69.41589 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 877fa5e1-1046-30ef-ac0b-fed6f09d95d3 | -8.23139 | -54.96656 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| acca77db-f699-3776-b074-81e176ad52ca | -9.97301 | -53.93143 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| e90d0093-183e-3249-b441-0ed4ac844b22 | -14.17613 | -52.83144 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69281fa2-e149-39b7-97e9-b48d9316ebf1 | -8.80488 | -50.49379 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a476ada6-4abb-37ed-960f-ae3c3ce409cc | -14.51383 | -53.24929 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| cee6dcf2-3dc4-3228-9007-c9f6b6c5f4ba | -14.64357 | -57.00491 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1870a2b6-67f5-3a68-982b-457ae36c5f88 | -14.17403 | -48.7747 | 2026-08-28 17:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1be71a56-507e-34b0-92a1-eacd8327df8b | -14.59787 | -53.14714 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3c7a7fda-f9f6-3203-bcbf-e5907d87e274 | -11.24019 | -53.98993 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c6bf7a76-bb8d-3c2d-b1a7-704cceb509b0 | -11.23734 | -54.0024 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 992b54cf-6df7-3079-bcc1-a71a76255ad0 | -9.12736 | -57.58953 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b051ca1c-6818-3874-9505-97f04af6cb01 | -10.3413 | -50.39006 | 2026-08-28 17:45:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 709e4131-6ff6-3342-aa77-1407bed8d028 | -13.87509 | -54.11181 | 2026-08-28 17:45:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 072d2085-d8e6-396a-9818-df4eceb17462 | -9.17359 | -59.39018 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 41ecb3e6-cf1c-3625-9880-2a56a6c20207 | -9.15115 | -49.96609 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3ae23567-bec8-38ef-93b0-bcef5dc6f3b3 | -12.38799 | -48.20315 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| effec577-fb0f-3d63-92c2-abee09156f05 | -14.89066 | -52.62732 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4dd4af60-861a-3511-b00b-33374eeabc66 | -9.85 | -65.00817 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f67da865-d4f5-3df3-841e-0cbe198b5d28 | -14.42591 | -52.60598 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ab8eeac-e704-30e4-9270-5aa04d6d6ae7 | -9.41726 | -50.43615 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| a932d97d-697b-330c-9cb7-47c8dc79f660 | -9.87302 | -60.25193 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 09c71ad7-ffe4-31bf-b087-9ef7e58bc1ef | -8.67549 | -49.54412 | 2026-08-28 17:45:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 9a194dba-dd50-383a-8a04-c83822a6bbab | -14.3881 | -53.28608 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 800b61c5-1b1f-37e3-a2a0-fc67a11f527b | -11.28094 | -54.04 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 93e90ec9-3ce1-38f2-9986-af4fa10e73e4 | -9.23013 | -59.76838 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ef83f393-882d-331a-a0b1-85bd28363614 | -9.92986 | -60.42841 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 70b0f0e6-ebcf-3411-90c5-6ac859980437 | -10.5753 | -69.69324 | 2026-08-28 17:45:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 671b98da-10e5-3370-a71d-41229f828220 | -14.60176 | -53.14056 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dc4cb809-ec4d-32d2-b284-c073a9b8b470 | -10.08458 | -68.56135 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 41.9 |


[Clique aqui para ver as próximas entradas](README138.md)
