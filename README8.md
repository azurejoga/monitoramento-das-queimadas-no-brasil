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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00d1b5a0-80cd-3643-852f-890ff731ed2f | -13.23084 | -47.36164 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| dc0f1644-3fe1-3fdc-bffc-45fddea622a0 | -13.76779 | -48.05971 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 01f5f132-264f-325a-9506-35ce6a16ccc2 | -12.82642 | -46.91378 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d9e2dccd-b2d8-35dd-b3c2-ca9f74135eec | -8.63123 | -54.98357 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fc5d1f6d-ce93-34c0-9b1a-efc0a2852142 | -8.61974 | -54.96629 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| da9f2a2a-53e2-3d49-8773-fd4877101176 | -8.24109 | -47.02744 | 2025-10-03 00:52:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1e1729c5-7882-31e5-b64e-86d2d8e18fe8 | -13.20835 | -50.87283 | 2025-10-03 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18f8262d-023b-3fbf-8e9c-0ef6cc648c91 | -10.94197 | -51.08142 | 2025-10-03 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 46735f17-6d13-3e72-98f6-220843bd4612 | -7.90072 | -43.50621 | 2025-10-03 00:52:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 69ec299c-d21b-3d6d-9049-b83cc08b51e6 | -9.4478 | -50.88976 | 2025-10-03 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 748e2eea-61f3-36c8-a4ce-5ff0992a1b25 | -12.60157 | -49.89822 | 2025-10-03 00:52:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0518a61f-cd55-301d-9736-4f88aba1165f | -9.06435 | -46.662 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 757ae7ef-3fb1-374c-bd4d-382e7559de59 | -13.5439 | -47.29096 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b21e726c-2825-3cf4-9045-30753c722205 | -13.76096 | -48.0699 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| ed2354ea-a712-38e5-8d7c-3cabbf9d40f8 | -11.1607 | -51.89178 | 2025-10-03 00:52:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| df4bc789-f8a2-35c3-bec2-2e8a2d56e20b | -11.14063 | -43.41032 | 2025-10-03 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 234.6 |
| 3700de0f-e288-3cc9-8576-a9b595fd260f | -10.76434 | -45.34376 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1e062fef-d9ce-337a-8c3a-9d0c5e24d0cd | -11.16204 | -51.90112 | 2025-10-03 00:52:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d56e80de-ea0a-326a-b573-b16c17fc154a | -13.34203 | -48.12628 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d6ee788b-bae5-370e-9fd3-dc0795365a22 | -12.80536 | -46.86045 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c02e12b0-b91a-319f-af5b-2e5a5358d439 | -12.29614 | -45.35805 | 2025-10-03 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7c94dcba-faaa-3d3b-8868-32fa5acddde5 | -7.24658 | -49.41432 | 2025-10-03 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| e058b267-fdea-3849-8aab-1cb77908cbaa | -13.77179 | -48.06779 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 660e0451-514c-3802-8085-eb18e2806de3 | -7.88548 | -47.34679 | 2025-10-03 00:52:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6bea003f-7a67-3622-9a67-8ec31043c9e1 | -7.90728 | -43.54688 | 2025-10-03 00:52:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 2ecadf50-5fce-3e84-990b-7a813504c808 | -13.49475 | -48.57666 | 2025-10-03 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bdec1040-c650-3039-b271-1cf37bd3724a | -11.6264 | -47.9954 | 2025-10-03 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| f3519131-419e-32c3-bd15-52337e1403ae | -12.93068 | -48.44357 | 2025-10-03 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cb302d85-44b6-3eac-9a67-85886b76ba72 | -9.88151 | -47.82515 | 2025-10-03 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7a753bfa-5841-396a-99d8-6180c6fb5434 | -11.01885 | -46.55213 | 2025-10-03 00:52:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 1ba967a3-7764-3b9f-82ce-ebcacde07a28 | -10.96353 | -51.09868 | 2025-10-03 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75680652-590e-3e2d-8b47-36cd50b419a8 | -10.86365 | -47.05509 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 42743c4f-ff02-3047-9c28-b46ab2348ba2 | -9.44936 | -50.90042 | 2025-10-03 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05af0bed-2ad0-331f-a1c0-993b5fb19f27 | -13.97259 | -48.16739 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 04df4ee6-b6d7-3a13-b937-f75af0dbf906 | -11.13863 | -47.20022 | 2025-10-03 00:52:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 38be5777-b7d4-357d-8cab-59ce2378711d | -9.48478 | -47.87935 | 2025-10-03 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 577725f8-400f-31a7-8ae6-cf6ca51cfea3 | -12.71913 | -48.58024 | 2025-10-03 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ad3ce429-42e3-3c80-bd24-887e277b93bf | -11.14655 | -43.40401 | 2025-10-03 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 242.7 |
| 36882c4f-40fa-368d-ac0c-95032f476631 | -14.46829 | -48.41793 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 60573c74-3ced-33ba-bf3b-8b37e80839eb | -13.76537 | -47.53169 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3692d931-4512-359c-8f41-c89a1ffa3af4 | -13.77605 | -47.52064 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 02377523-468a-3510-8b36-49ba67c7ecd6 | -13.78685 | -50.78584 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 728b8b39-479d-3cfa-b98d-8ec3508cdaa0 | -8.52339 | -50.03357 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 39c65b97-8379-3b59-9b08-ad2e90c1b260 | -11.90905 | -46.28998 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 34a3c481-7cab-3335-8643-3173d67d61c1 | -8.61199 | -54.97678 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 081adc79-5efe-3d5d-8e41-b477ac5f8fa8 | -13.27142 | -47.26554 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 97a2d0d3-f9c0-3a09-acca-8f353fdd040e | -9.91452 | -50.50378 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 0198d34d-8bf3-3b7d-ae53-af2bb982a457 | -13.76776 | -47.54617 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3f2a7552-527b-373b-a8f9-a6a02ba68fe4 | -13.75909 | -48.07572 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 001e3dc8-a4f0-3c0f-bb3f-416e5dae224a | -7.71853 | -46.20102 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 41b0d2c5-de8a-3949-b239-7fb2f5db7980 | -8.62099 | -54.97554 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8535a204-c2fd-3701-99a8-93d57dfd750d | -10.34187 | -48.18149 | 2025-10-03 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4dc457b9-f5cc-364d-8fa4-895ad1e28a88 | -11.60479 | -47.64801 | 2025-10-03 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 985aa609-0cc4-39f6-a869-be9b9a047fb1 | -9.90156 | -43.71906 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 9d9a69c0-77c3-37e7-a573-3d46dd4c38a8 | -14.66847 | -48.27171 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f7f3c1a8-cbe2-3138-8879-2ef3c259ae01 | -14.04377 | -53.88303 | 2025-10-03 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a223aede-ec11-330a-9a32-dc563859660e | -10.89382 | -53.74532 | 2025-10-03 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97436d0a-6661-3459-80d4-615fd4886d0d | -14.19637 | -46.11069 | 2025-10-03 00:52:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 969043d5-9b18-35d9-867a-c46e0c0c2454 | -10.27304 | -50.36665 | 2025-10-03 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ecc3c883-e212-3ef1-a4ca-e8d190ef7a27 | -11.06271 | -47.79299 | 2025-10-03 00:52:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7090d8f3-f7c0-3be9-a012-d038f7a9e252 | -14.77298 | -50.09137 | 2025-10-03 00:52:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c0bb8a29-82b6-3d04-a508-fa4cf1069206 | -12.37072 | -46.53338 | 2025-10-03 00:52:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 825a7d77-3da2-3ab0-8736-7abcbcca6e36 | -13.26191 | -47.25652 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e8d6488b-d4b0-3dde-a14d-2c6ecfd019cd | -13.64557 | -50.28084 | 2025-10-03 00:52:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e86e5f4-1a88-3608-a364-8181c765a2a2 | -13.77012 | -47.56052 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 013f0d19-c5e7-3101-aaa5-f7d6dd87e76e | -9.92374 | -43.7925 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| c3c6137a-cdb8-3b0e-8b09-e8f0b966f1aa | -13.30477 | -47.82156 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 46c3a836-4a1b-37b9-ba39-375a1e79721a | -10.16419 | -45.51397 | 2025-10-03 00:52:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 4cd1c174-bc2c-35b8-b4e9-465ac7788296 | -8.76301 | -49.9275 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9457323e-1682-3603-8c5b-0bb309d6aefe | -9.92427 | -50.50222 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5e9b0004-cf14-3d25-a586-c2577d0eeb13 | -8.62348 | -54.99406 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4369729e-3169-3466-b028-032dc88cb27b | -9.1643 | -50.84242 | 2025-10-03 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b335e6d5-fba5-3597-b4be-8aa63576839c | -14.57509 | -48.33398 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3cd772de-943e-39e7-ab10-69508c2e7611 | -9.08435 | -48.02713 | 2025-10-03 00:52:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| d3be3011-2573-3873-b527-fb53aaa54dcc | -7.70437 | -46.20327 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ef8e9b8c-20e6-3c64-8eec-a160d432d8d5 | -7.93669 | -55.02613 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da56341a-69b7-3c16-b55a-b108621e5216 | -12.63667 | -46.95777 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2162e115-c9f5-3026-a627-37ad6afb2d31 | -13.53222 | -47.29248 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e36896e3-384d-3d1e-a63f-0188bebdc248 | -13.96121 | -48.09678 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1c778d1e-c436-3db0-abad-d28668af73ff | -12.75872 | -50.56273 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 960dfeb5-a15a-3110-9afd-ad3fa6fbff9c | -12.22797 | -56.94298 | 2025-10-03 00:52:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| acce78a7-13a1-3f25-a3bd-a839aa64bd1e | -13.2737 | -47.25509 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 940fbaf6-c1b9-39e0-b0fe-86e41f372dc3 | -13.79514 | -47.57139 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7364d9bd-1308-3d30-8698-63e0ec1e2bfb | -8.24432 | -47.03247 | 2025-10-03 00:52:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ccfbe170-35b9-3420-b1a8-3de5f5b80b00 | -13.32717 | -47.59676 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 2552bb42-825d-3105-b495-d8c257338825 | -8.02762 | -55.42497 | 2025-10-03 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e6d434e-b0dd-39e3-9e25-3660da39acbd | -11.13029 | -43.40773 | 2025-10-03 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 44e8b3f7-14ce-361d-a1a2-00cd9d57c440 | -11.90163 | -46.31945 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ad6b0c03-bc5d-39e9-9f66-fdbea44cdd5a | -13.77165 | -47.56661 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| cb565db9-4120-3112-a430-e553fc9e1922 | -13.12681 | -47.86283 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0372e47b-6588-360e-a17c-47a8e58f45e5 | -15.25692 | -56.76952 | 2025-10-03 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c7a28832-e8a0-330f-9e58-b29481b13fab | -14.62596 | -48.24377 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 34cd32d1-32c4-3c5b-a277-1bc76fc9ac91 | -11.85044 | -44.96162 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| ef372e4a-9750-3c96-bff0-ac402b7e5124 | -10.83162 | -49.39103 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 0fe928cf-e980-3522-9c89-b010d3cb6b6e | -9.95058 | -43.75178 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| f8ba688b-c542-3019-b2e8-8b51effaece9 | -13.33407 | -47.20676 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1c2ebb13-eec6-36a3-92d4-feee31d14484 | -9.48203 | -47.8623 | 2025-10-03 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| fb77cb69-2329-361b-8f32-f00f4d9b9cf8 | -11.89831 | -46.29894 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 17aeb10d-c0ed-3758-915b-a7af0d1bcecf | -14.19682 | -46.10525 | 2025-10-03 00:52:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a14ce311-91ac-33d8-acef-827cb0e99bad | -7.75489 | -46.24805 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |


[Clique aqui para ver as próximas entradas](README9.md)
