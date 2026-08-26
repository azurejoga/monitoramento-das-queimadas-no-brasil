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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fe752d2-ec3d-3617-b8d2-52f37e0cc138 | -13.1711 | -51.3404 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 00e5acc6-f862-3118-8116-c0e287e4f5b1 | -13.2476 | -51.3521 | 2026-08-26 06:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 293.1 |
| 82d5eb67-7ecd-3652-bd4b-e42af7627876 | -13.1711 | -51.3404 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8f27694e-6057-31b3-bc7c-5f910e1f35ed | -13.2472 | -51.3735 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| b4fecaf4-e373-32f6-93f6-18b1a514e25f | -13.3038 | -51.4304 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 6001a35b-a969-31b4-abd0-a8193f716f90 | -13.2668 | -51.3497 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 0598e8f5-95ae-3688-a5c6-69d687d54817 | -6.641 | -58.4987 | 2026-08-26 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fabae11e-f768-3917-8ac5-8d867913a348 | -13.2476 | -51.3521 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 80fa5b60-527c-350c-b97c-af7b27b640cb | -13.2664 | -51.3711 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 176.1 |
| f8e20ffe-8abc-30ab-a9d6-cf1c92830525 | -13.2284 | -51.3545 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 185.2 |
| ce76856b-03e7-351c-9bac-5b252773414f | -13.228 | -51.3759 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3a34c5eb-377d-3133-83f2-62e319d41111 | -10.7596 | -54.0384 | 2026-08-26 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fa639dd4-5fc9-3c6a-8c7d-cc0f17f23e57 | -13.3034 | -51.4517 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 252.6 |
| 93171a7f-edfb-3826-b410-edd3fce3789d | -13.3226 | -51.4493 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ec70fbbd-ec1d-3822-ad3f-c72281b9a654 | -13.1903 | -51.338 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| aa5c52be-883b-38be-9f2d-7fc96c005d58 | -9.6024 | -55.1078 | 2026-08-26 06:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| baf95420-54d0-3b73-872f-4846f42ae380 | -13.1906 | -51.3166 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 7c6c7653-f58c-35e2-bf52-7a0e3b1579fc | -6.2676 | -53.3768 | 2026-08-26 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| bb1ed07b-db34-3797-8e82-3fe3ffaaa896 | -13.2842 | -51.4541 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a7885005-7365-3897-88ab-c1ea98c74f49 | -7.5289 | -61.3825 | 2026-08-26 06:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 8cf99061-5252-3678-9ea6-c8856247b5df | -10.7784 | -54.0368 | 2026-08-26 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c27a4ba2-6698-3a28-8c62-51f9b7e25a04 | -13.1715 | -51.319 | 2026-08-26 06:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 51f6fa63-564c-3b92-8982-e01ad114d6ee | -7.5104 | -61.3832 | 2026-08-26 06:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3023a1cf-6704-332c-bea5-cc93ac764988 | -7.60393 | -67.42406 | 2026-08-26 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f9dd944-ec38-30b6-9b6f-bd9396018fb8 | -7.60454 | -67.41953 | 2026-08-26 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdc91143-a1d7-379f-8435-15271ba17d08 | -10.7598 | -54.0179 | 2026-08-26 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b20b813e-c7d8-3e34-b979-797d017ad2a6 | -13.3038 | -51.4304 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f6116fa5-d856-3e2c-bead-bb9a5d0b466b | -6.641 | -58.4987 | 2026-08-26 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bf825afa-af7d-3252-a0a6-26d0dc3fd16a | -13.2476 | -51.3521 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 398f94fe-ede7-3e3a-91b8-7932c4381cdc | -13.2284 | -51.3545 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 695034a4-6aaa-3cd5-b795-d36560fbacba | -7.5289 | -61.3825 | 2026-08-26 06:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a827d7cf-d38c-31c8-8c04-3b179ba26329 | -13.1903 | -51.338 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 3f2e3e6a-42fb-360f-a0a5-2558e2a8eb27 | -13.2664 | -51.3711 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 4d05ad17-1a97-381f-82f8-0c34fb6e990b | -13.2472 | -51.3735 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| cc2c7f3d-ec36-3c9f-ad33-636b6c5331df | -13.2668 | -51.3497 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 199.1 |
| fd5bf23c-1a3f-3867-b22e-15d841edb7dd | -10.7596 | -54.0384 | 2026-08-26 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 825aca74-85d0-397f-aa04-693d81ce6a3e | -9.6024 | -55.1078 | 2026-08-26 06:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 81e91b9d-1a82-3859-95f5-b19b501aac65 | -7.5104 | -61.3832 | 2026-08-26 06:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 33e8b058-f16a-34f5-ba56-e6d24a35d066 | -13.3034 | -51.4517 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.5 |
| a245865a-f8d2-3689-9f2b-d660e088aac0 | -13.1906 | -51.3166 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 05239ca6-5db7-3e67-8a3a-c8fd9cce585c | -13.2842 | -51.4541 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a9f2b8b1-b6c4-3787-b6d5-881423a92f25 | -13.1711 | -51.3404 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 79bc1bde-b158-3d95-9e0d-d355aec0a906 | -13.228 | -51.3759 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| bfa6aab3-781c-3f2c-856d-cb385d8469a6 | -13.1715 | -51.319 | 2026-08-26 06:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| bec63474-ceec-3c8c-ac30-37fefb19bb96 | -12.0358 | -46.0146 | 2026-08-26 06:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8d33ab09-0373-3635-8d44-0241cc0cfca9 | -7.5289 | -61.3825 | 2026-08-26 06:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6315b7f7-3606-3d61-82cd-8f85c21e5f80 | -10.7598 | -54.0179 | 2026-08-26 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f9135c1b-c28e-3929-8578-cadfb04323a9 | -13.3038 | -51.4304 | 2026-08-26 06:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| cba52a37-5654-304b-a397-248b9d85799c | -13.2842 | -51.4541 | 2026-08-26 06:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 315d607a-8c66-3eba-848a-151667d1d741 | -13.3034 | -51.4517 | 2026-08-26 06:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 580ad66d-219d-378f-a8b2-760132554bbe | -10.7784 | -54.0368 | 2026-08-26 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 0efbedb1-4162-3233-ae32-5846fadbd930 | -10.7596 | -54.0384 | 2026-08-26 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 11889f22-3768-3b4c-a65e-5430870d6a1b | -6.641 | -58.4987 | 2026-08-26 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 176baf2a-dd98-30c9-8041-2118535654bc | -9.6024 | -55.1078 | 2026-08-26 06:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 6d4fed8f-33fc-3760-bf31-d2426549cc14 | -7.5104 | -61.3832 | 2026-08-26 06:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f1018a86-d797-3128-b910-9ae98e22f79d | -2.49728 | -48.13557 | 2026-08-26 06:54:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ce014304-bb2c-32c2-90f8-da0a6014ff27 | -2.79063 | -49.57579 | 2026-08-26 06:54:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 494ff50a-ab98-30c5-9738-e3b884bfc704 | -2.79939 | -49.57708 | 2026-08-26 06:54:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bac5eac3-a72f-3d7a-b542-ca823ad022e9 | -3.53481 | -48.1803 | 2026-08-26 06:54:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3825e05b-b9ce-3b5e-852d-2df13d732c08 | -9.60032 | -55.1175 | 2026-08-26 06:57:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| ca24adfa-960f-3397-add3-3f659df24c00 | -8.17845 | -54.95303 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0beaeff2-ffa2-3fad-9679-72d125872d6e | -6.64783 | -58.50266 | 2026-08-26 06:57:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b99d2eeb-21bd-3b76-a89d-a6eee0da4bd0 | -8.16817 | -54.95085 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a8d56324-c2ca-37df-8a61-595c9aa17234 | -6.25912 | -53.3788 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7270c00a-8243-382a-8e2b-11b1cc3dd8ea | -10.75992 | -53.98331 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 839bc22c-c600-3f94-b07c-67636a0eeeb1 | -6.27034 | -53.36967 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f5145755-b97b-3d61-85c7-c5c1d3a31bb6 | -10.75505 | -54.014 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1e9dd589-2fa0-316a-b9bd-8969e10cfea2 | -7.06447 | -59.22219 | 2026-08-26 06:57:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 478859ee-1a9d-3d4c-bfa7-0ccb54cec8a3 | -6.12072 | -57.83475 | 2026-08-26 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 48c37d3f-4874-3cbe-8d9f-5dc8206344d2 | -6.27421 | -53.37603 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e62ecab2-46c5-35a9-b333-fa10e4dfd887 | -10.76444 | -54.01545 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 77ce29af-5c8d-3d17-a021-3aedd3a3f445 | -7.06677 | -59.21509 | 2026-08-26 06:57:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 54fd2d7a-548c-343d-8664-b87c2a2609bd | -12.03214 | -46.00674 | 2026-08-26 06:57:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7d2329cc-5e6a-36e1-a006-d02e528cc9f5 | -6.12455 | -57.81193 | 2026-08-26 06:57:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b1f5f8f9-4b4e-3b9b-9e34-bf7aa89bd102 | -6.61945 | -58.49805 | 2026-08-26 06:57:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 0df60932-f737-3e26-a173-d4d290f948c9 | -9.60617 | -55.09896 | 2026-08-26 06:57:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 83600ea6-9691-31a4-acca-feeef60a4a53 | -6.32624 | -54.73731 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6a37e5fe-8c25-3acf-a6d5-2aa8a5bb02f0 | -6.26076 | -53.36819 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b421789b-2fe2-3e58-af09-69912c695bcc | -11.15634 | -53.99889 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d853cf9-cb15-32f3-bef4-4e5a902cf50a | -10.76119 | -54.03598 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 58907a0d-6a3d-3143-afcf-a69cea9b55d9 | -6.2759 | -53.36543 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 77e6bf4e-bf0d-3f55-8266-da9b6ea49d6e | -6.27198 | -53.35901 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b4bbab92-9691-32a6-ad1d-f2af238f4fe5 | -7.37997 | -55.15516 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fd97747a-265c-304f-9d42-465295d87bc9 | -12.02975 | -46.02481 | 2026-08-26 06:57:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 5bb61a38-4555-3565-96f1-8621086646d3 | -6.26871 | -53.38026 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e03fcedf-711f-3aa7-a2b8-9c1c8f16dbf1 | -12.03321 | -46.03221 | 2026-08-26 06:57:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| dce1c1f1-0a87-3de9-9754-4756c9c1a7b9 | -6.63365 | -58.50027 | 2026-08-26 06:57:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b63af26f-ddcc-3cad-bad9-9d1894eed83b | -6.25117 | -53.36669 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1e3f1a4e-ee5b-36ba-8963-3b2440c4769d | -6.30326 | -53.56762 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b8355999-32c0-3023-bade-c1051ffd1998 | -6.22168 | -55.6183 | 2026-08-26 06:57:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f235eb51-2e35-3bfa-8b43-f586bf978cec | -7.50886 | -61.37854 | 2026-08-26 06:57:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 38ea6a79-2b90-38e5-a1e7-140678d7de69 | -7.52326 | -61.37672 | 2026-08-26 06:57:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 45c8b75f-52b4-3a0f-8a62-1c01ba70207a | -10.76282 | -54.02573 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fafcc616-8ad1-33c6-80d1-091b31a63a7c | -6.27759 | -53.3548 | 2026-08-26 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a745235f-60d0-395e-9d52-fcfac3331481 | -9.60422 | -55.11129 | 2026-08-26 06:57:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| aa6f6297-9f01-385b-ab24-e33d3364d7cf | -10.64512 | -57.24145 | 2026-08-26 06:57:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 79be4523-3602-3bcf-8cc8-a246e1aacada | -11.28255 | -47.06934 | 2026-08-26 06:57:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8c18d17b-835a-3383-a306-575a329a8a1e | -9.60237 | -55.10514 | 2026-08-26 06:57:00 | AQUA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| dd16dfd0-e201-3db8-9074-0cefd0b5ce2d | -7.75076 | -44.74496 | 2026-08-26 06:57:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 49d6be8d-2d87-38de-9c22-c1df2b6e26df | -11.15793 | -53.98877 | 2026-08-26 06:57:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README75.md)
