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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aed51677-d192-394b-a0b1-549483169e84 | -12.5369 | -57.216999 | 2026-07-08 00:27:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27fb183a-225d-3455-92b4-de2f9da415d5 | -13.282 | -45.1633 | 2026-07-08 00:27:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 363843eb-79d5-3ff3-acc6-93ab39dab4f4 | -21.810101 | -52.711899 | 2026-07-08 00:27:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1e4bc1ba-658d-36c1-9a18-c7d413f23992 | -8.2023 | -49.474098 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04b9a261-a44c-3259-ba46-47973bf6988f | -21.3687 | -49.162701 | 2026-07-08 00:27:00 | METOP-B | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ba06068-000e-3bd7-91e5-7a177c9d3c3e | -13.2723 | -45.165798 | 2026-07-08 00:27:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce524557-638b-3b55-878d-4a576c587c72 | -12.7373 | -44.4521 | 2026-07-08 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0f4ee1ec-e7b0-3e33-ad45-f6840ae8ad81 | -12.7562 | -44.4724 | 2026-07-08 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 11ff36ce-aaba-3c03-bca1-8f3aacfb9aad | -21.8033 | -56.2729 | 2026-07-08 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f44e43f6-d562-3686-b601-727f4ea615fe | -9.207 | -48.5801 | 2026-07-08 00:30:00 | GOES-19 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b76ccd61-34f0-3d40-a9f3-c2cbf8d51864 | -12.3561 | -47.413 | 2026-07-08 00:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 1f2bbcaf-c39c-32a1-9145-cc7700b14d8e | -21.0705 | -47.2568 | 2026-07-08 00:30:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 19ed54cd-cfc9-305b-958e-c0afd8f4270d | -13.9589 | -45.2251 | 2026-07-08 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| eeeb6f82-b306-35c6-a25f-bfb7476593fe | -9.2258 | -48.5782 | 2026-07-08 00:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| a12415fd-e401-325f-b1ca-a7a27c4231ae | -5.6701 | -44.3147 | 2026-07-08 00:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5f8715d5-fbfb-3466-85f9-b7ce3bd5734f | -21.8037 | -56.2514 | 2026-07-08 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 51.1 |
| dc1fbdf6-3984-335f-b3c7-f87377d5a90f | -12.7566 | -44.449 | 2026-07-08 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 713ea358-2c14-3f70-85a6-ed20417ea77e | -21.7827 | -56.2762 | 2026-07-08 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| bb5862df-dbc9-3c78-ac97-284066e27d46 | -19.65908 | -50.86932 | 2026-07-08 00:37:00 | TERRA_M-M | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2b168eaf-1386-39e9-bc39-4f8a02d0b39c | -21.37373 | -49.1804 | 2026-07-08 00:37:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 2546be84-3b61-3d6f-9b45-45fa1e04e477 | -21.79417 | -56.26395 | 2026-07-08 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 897ef515-18c7-3f23-88dd-cc503ddbd4d4 | -23.15339 | -51.68927 | 2026-07-08 00:37:00 | TERRA_M-M | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c2f8fff8-81dd-32a3-8140-723a1447c254 | -21.81241 | -52.71099 | 2026-07-08 00:37:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9cfb78a4-9586-3a3d-9ea1-e1aa0ed6e17f | -21.81391 | -52.72111 | 2026-07-08 00:37:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bd770c27-e205-383d-9734-5ad376d90c7d | -21.80343 | -56.26266 | 2026-07-08 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 28.7 |
| cdbba3ca-b0d2-3242-ba2e-bbf28cc420d5 | -21.06132 | -47.2461 | 2026-07-08 00:37:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 48067b4c-a73d-3563-a37b-c64cf2c85718 | -18.08578 | -54.01955 | 2026-07-08 00:37:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 45da158d-6f25-369f-a0b9-c899287a67a3 | -21.06145 | -47.26141 | 2026-07-08 00:37:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 220a75ca-6469-3d21-9efa-9ef37172d2de | -17.53141 | -54.00879 | 2026-07-08 00:37:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4580d2b5-7b76-3c09-a437-a05745880e1d | -18.07817 | -54.03054 | 2026-07-08 00:37:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a2039a96-ec88-3fdc-9946-d3af519a608d | -17.54042 | -54.00735 | 2026-07-08 00:37:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8e5dfeb3-b2c9-30f4-81a6-f4e6d21fe48d | -21.371 | -49.16425 | 2026-07-08 00:37:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| c001b01a-75de-3f74-b228-5845e30cc868 | -17.27851 | -50.01804 | 2026-07-08 00:37:00 | TERRA_M-M | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e730c8e0-e021-36d9-9b54-a3e2efab03cc | -17.54179 | -54.01689 | 2026-07-08 00:37:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f574cce-68e5-37cf-9b11-44852fd8b47a | -21.05754 | -47.24053 | 2026-07-08 00:37:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ce4cbcef-deda-3862-8c34-4efb4f6207b8 | -17.28119 | -50.03446 | 2026-07-08 00:37:00 | TERRA_M-M | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 9ef6ee05-fc8a-3ae9-97bc-becdbec38215 | -21.77964 | -56.29797 | 2026-07-08 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 443f49da-d17f-3204-a52a-0d48a02682db | -21.80477 | -56.27309 | 2026-07-08 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 4ec3013f-d821-3c8d-bbd0-310fe763fe69 | -18.24148 | -54.59632 | 2026-07-08 00:37:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 86c62f81-8b6d-3585-a05c-9137ffdd59b6 | -22.28592 | -46.86752 | 2026-07-08 00:37:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2a4973f7-6ad9-3128-a1df-52f239b987c6 | -21.77831 | -56.28751 | 2026-07-08 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d042677e-28cc-36bc-bfcf-9a9c699860b3 | -20.10722 | -53.33846 | 2026-07-08 00:37:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a475408-1b82-3ab2-b5ce-0399ef092717 | -18.24279 | -54.60566 | 2026-07-08 00:37:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d461fe9e-d5c1-32cc-ae97-3fd70b8abb5e | -21.06507 | -47.26698 | 2026-07-08 00:37:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 60f02f88-8d3f-3270-84fd-4a968582be6e | -18.08715 | -54.0291 | 2026-07-08 00:37:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4889c418-5a0e-3c39-8f25-680ce586840c | -21.79551 | -56.27439 | 2026-07-08 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f483c6ec-da3a-3345-b1ba-fdf3cbfccfd5 | -20.10864 | -53.3483 | 2026-07-08 00:37:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fea29026-9536-381a-a639-bd2636c920e3 | -23.15175 | -51.67856 | 2026-07-08 00:37:00 | TERRA_M-M | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| e04e5b91-9b79-3e3d-a66a-b7dd1d4629e7 | -15.08205 | -49.46456 | 2026-07-08 00:39:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 836789b0-743d-3875-9ebd-50a6a3c7d9ae | -8.60202 | -48.02444 | 2026-07-08 00:39:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1fc5efd6-e647-379a-9831-8a1929b2059c | -13.33619 | -54.3768 | 2026-07-08 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 51ce2228-ee38-38c3-b8a4-57a7ce6ac120 | -13.29305 | -54.4036 | 2026-07-08 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c91280b8-4a3b-3d1f-979c-945bd4e2290d | -13.28385 | -54.40502 | 2026-07-08 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2664055b-ff55-3ab9-a5bb-74101838bb82 | -6.84963 | -50.65555 | 2026-07-08 00:39:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 11c17efe-bb0d-3dd6-91e6-063c5b28e6bf | -9.19003 | -58.06604 | 2026-07-08 00:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a953e4de-b0b3-320b-a3fb-2fd17fa85cf7 | -9.31033 | -51.92906 | 2026-07-08 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9f12c750-7d0e-34fb-9ad9-cf418a0b90fe | -14.14064 | -52.88215 | 2026-07-08 00:39:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d889658d-8467-3531-a66d-a34ecb19b9d0 | -13.29448 | -54.41338 | 2026-07-08 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 07e1437e-5d2e-3216-9b92-212e609b4ad3 | -12.13818 | -48.26562 | 2026-07-08 00:39:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 8b610ece-1c6b-3de6-b49e-167bf6194c34 | -8.73329 | -54.54229 | 2026-07-08 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54c68da0-9d98-352f-9971-331ff316c131 | -12.36512 | -47.44856 | 2026-07-08 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a580c17f-2ac4-3806-89bc-ac579d200c17 | -9.22424 | -48.57499 | 2026-07-08 00:39:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 16d1029c-d25e-30b9-ab3a-31f216d8ae45 | -12.3643 | -47.42193 | 2026-07-08 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| c1e8706e-3c7b-3f5d-905a-d0aee883dcc2 | -12.34427 | -47.42064 | 2026-07-08 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 543b2ba1-b580-36e0-bf3f-c74bd2b9b396 | -12.139 | -48.26013 | 2026-07-08 00:39:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 6f1e6470-be15-30fe-a019-4a4a1148938e | -7.63475 | -50.03086 | 2026-07-08 00:39:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| e9c7d1a6-2daa-381a-aa91-ac013b8becc5 | -15.71073 | -53.10085 | 2026-07-08 00:39:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e5777ee6-6006-3c4b-8cd6-2a860c194a95 | -8.73484 | -54.55296 | 2026-07-08 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f8c7d3a7-d24e-3c4c-a553-69ff4450c092 | -14.14236 | -52.89369 | 2026-07-08 00:39:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| ff4b8715-e3bc-3316-bc28-67491c274e51 | -13.95716 | -45.21496 | 2026-07-08 00:39:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d99d9cbe-b8da-3d86-b02d-94f85100bea6 | -14.15224 | -52.89215 | 2026-07-08 00:39:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 81720f9a-e4c7-3401-948a-3d8a86081a82 | -13.53615 | -52.94578 | 2026-07-08 00:39:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 944b4b7d-3b15-3ad0-9136-b5f85b3c0230 | -11.32311 | -54.47548 | 2026-07-08 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2f1921b5-049c-305d-a863-0ce722c3310d | -9.74555 | -49.03749 | 2026-07-08 00:39:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 4e501a97-c395-359b-89e6-cdaf180bd5b2 | -11.91339 | -55.91105 | 2026-07-08 00:39:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4aa1615c-ddb7-3226-a146-94aa5aca9b71 | -9.30786 | -51.91338 | 2026-07-08 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 18bcbf08-b600-3cdc-a2b7-f0f0560ade80 | -10.48376 | -54.80133 | 2026-07-08 00:39:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 827b2d92-33cf-3339-843f-d3fcf134384c | -9.22693 | -48.59861 | 2026-07-08 00:39:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 62699850-3899-3a73-bd82-035a44544965 | -9.31092 | -51.91949 | 2026-07-08 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| bbe7cd5f-7e2d-3e30-b2c9-59681644e6b3 | -14.15052 | -52.88055 | 2026-07-08 00:39:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cd7b5260-dcd4-3244-bd4e-447cd9041d55 | -9.74313 | -49.04448 | 2026-07-08 00:39:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| f1d854b8-5897-3326-afa4-f66000020838 | -9.22884 | -48.60348 | 2026-07-08 00:39:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a6916684-c56b-3c19-b2a9-1b54e9b24d9d | -8.59681 | -47.99206 | 2026-07-08 00:39:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 1b4ac79a-b2ca-3af1-9098-a6e575bdafb8 | -9.22208 | -48.56995 | 2026-07-08 00:39:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 5e251aba-bda7-326c-a92f-6de028841f95 | -7.6404 | -50.02428 | 2026-07-08 00:39:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 3464ebb2-025e-3e38-ae81-c241b150a8d8 | -12.3489 | -47.42496 | 2026-07-08 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 3999a16a-cc47-3e44-9f59-900c1d742d16 | -12.54452 | -57.15185 | 2026-07-08 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b8c8bce1-c132-3b60-88e8-7823263447e3 | -12.53661 | -57.22768 | 2026-07-08 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 025bd99b-6844-3491-b5ce-6f12efba40df | -12.35967 | -47.41764 | 2026-07-08 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 48e75ed5-7eb2-396c-8b85-3f3b0ed0b058 | -8.59516 | -48.02045 | 2026-07-08 00:39:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 18ee6f62-ef7f-3e38-9541-247997fef74c | -5.6701 | -44.3147 | 2026-07-08 00:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 93ff568c-a686-3e04-967c-9e8abd13ed05 | -21.3642 | -49.1664 | 2026-07-08 00:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| f7923ab1-a655-30d2-ad70-5e5c39d32416 | -13.9589 | -45.2251 | 2026-07-08 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| ded9f9c4-b1d3-348b-a092-99625d689c97 | -9.2258 | -48.5782 | 2026-07-08 00:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 1ec649a9-870a-3c70-88cd-70d802b12fd4 | -12.7566 | -44.449 | 2026-07-08 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 219.4 |
| 9e579296-c32e-3828-95ea-59b4348cfc71 | -12.3561 | -47.413 | 2026-07-08 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 672a2081-2087-3d49-a9d7-039f0861cbbc | -21.8037 | -56.2514 | 2026-07-08 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 8196cf7b-ce47-3b1d-9e9f-aa71b44eca44 | -12.7562 | -44.4724 | 2026-07-08 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 1330a8aa-3516-31d7-aa4d-e68a56e9b30d | -8.5933 | -48.0069 | 2026-07-08 00:40:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 553a8661-786d-3e5e-b100-5f6d64ac1694 | -21.8033 | -56.2729 | 2026-07-08 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 106.9 |


[Clique aqui para ver as próximas entradas](README4.md)
