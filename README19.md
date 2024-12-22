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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e5d1c6-dd01-334d-8ca0-032f15ba9ffe | -2.93233 | -41.17754 | 2024-12-22 12:06:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| bb6e9e22-786a-36f3-ba48-585b2df75669 | -8.89436 | -36.97105 | 2024-12-22 12:08:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 096cc5d8-5fe6-3cd8-9ff3-d80a8d9a2e46 | -8.01432 | -38.45183 | 2024-12-22 12:08:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 13.0 |
| acb5bcc8-46b9-3cc7-b822-e0a9f60107aa | -6.04411 | -38.10654 | 2024-12-22 12:08:00 | TERRA_M-T | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 34002b8e-9dd6-3b49-985c-d0e53220e811 | -6.03654 | -39.50469 | 2024-12-22 12:08:00 | TERRA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5cab2476-edca-31fe-ae45-7bda064c1427 | -7.71029 | -37.53745 | 2024-12-22 12:08:00 | TERRA_M-T | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 530843cf-41e7-3713-8524-fd693764ca89 | -6.13736 | -43.95651 | 2024-12-22 12:08:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| dd4b8579-1ed4-39e1-b7fd-2e48e696ef43 | -6.96512 | -37.78484 | 2024-12-22 12:08:00 | TERRA_M-T | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7302f54e-cc9c-381a-9598-adf15015c622 | -5.59639 | -42.83198 | 2024-12-22 12:08:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8455b314-7241-39e6-8f72-bd8c8ddd5fd2 | -7.67806 | -37.28889 | 2024-12-22 12:08:00 | TERRA_M-T | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| b3b4a2a2-f2de-3ef3-babb-25cae33328b7 | -7.68609 | -37.30025 | 2024-12-22 12:08:00 | TERRA_M-T | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 980fe96e-4f71-3114-bcda-3dad27d87c6e | -5.9095 | -38.27565 | 2024-12-22 12:08:00 | TERRA_M-T | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 0660320c-8bfd-33ec-af35-65dc123c36de | -7.36377 | -34.98439 | 2024-12-22 12:08:00 | TERRA_M-T | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 51bb43e3-7ead-3012-a849-a086f46f7623 | -7.36191 | -34.99852 | 2024-12-22 12:08:00 | TERRA_M-T | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 43.3 |
| abaa7576-ca4d-3178-a12a-bf689cbbdb2d | -5.37341 | -43.08365 | 2024-12-22 12:08:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fdd262d9-8727-3e01-a7c2-c8e20e209bcd | -7.21806 | -41.32695 | 2024-12-22 12:08:00 | TERRA_M-T | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3380f30b-7bf8-32e8-99d8-6091e25d4b42 | -7.7089 | -37.54731 | 2024-12-22 12:08:00 | TERRA_M-T | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7f50292f-ab77-3009-9de9-2668f3e57787 | -6.81184 | -35.5507 | 2024-12-22 12:08:00 | TERRA_M-T | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 98d558f6-291a-38ec-a8d4-4ea9d19ace1a | -10.12345 | -37.10948 | 2024-12-22 12:08:00 | TERRA_M-T | ITABI | SERGIPE | Brasil | 2803104 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 00ef2866-a08e-36e9-ac7f-d437fb1fc921 | -5.85718 | -44.13119 | 2024-12-22 12:08:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c25a60fe-08cb-3c80-92f2-73de25af7012 | -9.67749 | -36.70121 | 2024-12-22 12:08:00 | TERRA_M-T | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ff899904-2391-3795-8cc4-4b7636812768 | -6.9638 | -37.79431 | 2024-12-22 12:08:00 | TERRA_M-T | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e0f922d6-9d9f-3dcd-93fe-851de23277f2 | -6.01005 | -39.50095 | 2024-12-22 12:08:00 | TERRA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9cef467e-f81e-3f31-8e86-b21d2eace763 | -7.70099 | -37.53621 | 2024-12-22 12:08:00 | TERRA_M-T | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| a9693cde-95e4-3271-9385-e99fb541972b | -13.62471 | -39.177 | 2024-12-22 12:10:00 | TERRA_M-T | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| a1356982-2aaa-349e-8ae7-22f115fd574a | -17.93964 | -40.19873 | 2024-12-22 12:12:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7620f123-d48f-3ef8-aa71-ded36ff16715 | -17.93829 | -40.20858 | 2024-12-22 12:12:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d3e4943d-9ab7-3830-83f6-eafea0323a85 | -16.32469 | -39.55272 | 2024-12-22 12:12:00 | TERRA_M-T | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 68a243c4-3c7f-30fa-8518-5b13586ea065 | -2.8823 | -42.0243 | 2024-12-22 12:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a5aa5f1d-1080-3cd1-b2ef-65f6db7ac600 | -2.8449 | -42.0258 | 2024-12-22 12:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| aa334209-49e7-3766-a0c0-0d50b341c43a | -4.07 | -44.09 | 2024-12-22 13:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 414d969b-bd12-3293-a91e-84222d9cf799 | -4.1 | -44.09 | 2024-12-22 13:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca4fba3-8d00-3644-8975-dd7a142ede5d | -4.05 | -44.08 | 2024-12-22 13:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e1e8501-1b5d-396f-bba2-7fa4af068a45 | -4.05 | -44.13 | 2024-12-22 13:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 964603fd-128d-31aa-a1d5-b9dc7f9b6688 | -4.1 | -44.14 | 2024-12-22 13:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31d3ba55-b7ac-372d-84df-8d81d6fd67d1 | -4.07 | -44.04 | 2024-12-22 13:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb3f9778-4aa4-3e74-9bea-49aa3e29a616 | -2.8449 | -42.0258 | 2024-12-22 13:10:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6227b623-9065-33e4-8d25-b2d962df9cb6 | -2.8826 | -41.9529 | 2024-12-22 13:20:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 77.2 |
| dfede921-633c-3ff8-be22-14cce1995d1c | -4.3882 | -43.2663 | 2024-12-22 13:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0bb3c13f-88b3-3e5f-916a-2ec8b18ac952 | -2.8449 | -42.0258 | 2024-12-22 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 172f50a6-cfa7-363a-aad6-a60f2e2889a6 | -2.8826 | -41.9529 | 2024-12-22 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 195.6 |
| 57f9b95a-1f20-3c2b-ac9c-6017eee52350 | -1.3669 | -53.6953 | 2024-12-22 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| bb1ff327-323f-3af3-81f0-09cd5dc70436 | -2.8826 | -41.9529 | 2024-12-22 13:40:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 9facb4b7-a62c-3a9a-b9dd-a5c48140d589 | -1.7178 | -52.5757 | 2024-12-22 13:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d36e694e-74cd-38d2-95a4-5b98fde274f9 | -1.3669 | -53.6953 | 2024-12-22 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 196.2 |
| e62f3fb2-6065-3669-a126-87584463be93 | -4.05 | -44.13 | 2024-12-22 14:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22e89eb3-4ca7-3659-96d0-6c8571f4c7e6 | -4.05 | -44.08 | 2024-12-22 14:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7df46a3-2e2c-37de-8583-20c018b77c38 | -4.07 | -44.09 | 2024-12-22 14:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73b1cb3b-b8dc-3f85-a11d-cd04005c1943 | -4.08 | -44.13 | 2024-12-22 14:00:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |


