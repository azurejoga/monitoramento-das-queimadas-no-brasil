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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb4661af-57ec-3acb-9add-f48f2cf033f8 | -2.62201 | -49.10818 | 2025-12-11 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e5585d4-ca30-39ec-b768-55820c0a20c9 | -2.896 | -50.23554 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 061c87a6-61d6-301b-a917-0ed25a733ad3 | -2.77513 | -54.5274 | 2025-12-11 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28a897e8-ad0b-3e47-a867-8420d35de414 | -4.20573 | -44.47322 | 2025-12-11 04:38:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffc4cad5-9de1-3c03-a546-7730f8c04853 | -3.04175 | -50.49121 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b70a1dd-3f66-3331-8937-20dc24e86e28 | -3.62918 | -44.64915 | 2025-12-11 04:38:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c2bca57-2242-3c92-942b-635d9f1122a0 | -4.3519 | -45.92758 | 2025-12-11 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa6ba3d3-acac-38a7-93a6-a96d46c14910 | -2.40923 | -56.02153 | 2025-12-11 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a82dd427-9dc6-3926-b2a8-6ee766a71386 | 0.2293 | -50.07195 | 2025-12-11 04:38:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 910c8b8a-0565-32bd-a66e-729d206dbce7 | 0.00878 | -49.96125 | 2025-12-11 04:38:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a5036b9-eff1-3a00-b02e-a9b0fef7b018 | -3.50696 | -52.87741 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9afad54-277b-3d64-99cc-1f6173baa891 | -3.54982 | -45.44907 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f406fa68-b753-3d18-b934-880a815211a6 | -2.03178 | -47.14161 | 2025-12-11 04:38:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3251febb-997f-3bb5-ba60-05335be3a814 | -3.84313 | -47.82425 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90f6f5b2-5f24-356b-8aa9-fb696e8f4380 | -1.47626 | -54.20385 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67842ad6-93e8-3392-81a1-d37a1bd0acad | -2.21522 | -45.66704 | 2025-12-11 04:38:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eedff1d8-15dc-39f1-a651-6074fbb033b1 | -1.75221 | -45.60152 | 2025-12-11 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fadd634b-5f03-3122-b38a-ba7d7dc99c9c | 0.45971 | -60.43293 | 2025-12-11 04:38:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 554c7bde-b0cd-3a78-b004-c1f886792288 | -2.28449 | -45.59842 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3f523b69-485e-3057-994f-d94ef444b533 | -5.01108 | -41.29304 | 2025-12-11 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37dee45f-384e-3cb8-b0f3-d9c8ffe355b5 | -3.57883 | -52.11106 | 2025-12-11 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f15d6f37-6d36-3ad8-8f57-64c1e8b519ce | 0.22947 | -50.07077 | 2025-12-11 04:38:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d17a0bf-d555-3128-82d8-05d8049ac608 | -3.46464 | -48.98 | 2025-12-11 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebbf5aeb-4e7c-3eb2-8dfb-2a3b2787ae9e | -1.01502 | -53.72303 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0f51ab6-031e-3208-b2d5-5c28c3be1b94 | -2.2891 | -53.70142 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f30ccc08-4936-3117-b50f-15046886109a | -1.29105 | -53.16461 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce334fd-8357-3d67-a696-a9c6ae446883 | -4.29715 | -44.63533 | 2025-12-11 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 681d7af5-4d01-398f-a981-1f46affa60ed | -1.43066 | -45.6657 | 2025-12-11 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ddfe09d-562e-3a14-8963-00da019b81d6 | -1.59169 | -53.75954 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14ad77db-c428-3ea5-af1a-dd6247532faa | -1.43196 | -53.43336 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bab52af6-b9eb-351f-9ffa-9f089875b4e8 | -2.38138 | -47.42121 | 2025-12-11 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a22db56-f7f0-339c-bfb0-6b07fd102175 | -2.43883 | -50.26795 | 2025-12-11 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1be624d0-a7f3-393f-a281-477207e53a38 | -3.84211 | -50.97023 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3907760e-976a-3a5b-8628-16c18ac601d2 | -2.47377 | -56.05056 | 2025-12-11 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e81b8b-7bbe-3b8d-b399-f26a460bb226 | -2.69515 | -51.6444 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0ce5ba7-63f0-3800-b80b-94a7da8d0fb1 | -2.38194 | -47.41766 | 2025-12-11 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85b06082-9a16-322d-bd0c-56e82603d312 | -2.36401 | -47.68515 | 2025-12-11 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1db1383-d91e-303e-ad7e-5a0a93ec4945 | -1.68544 | -45.79564 | 2025-12-11 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 63c51995-1ea0-37c5-9aad-0f7f7192ddef | -2.84952 | -45.7993 | 2025-12-11 04:38:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1401ca1-de8a-3190-9771-f95752664cc8 | -2.02055 | -50.56351 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d94be14e-dfa3-3747-a914-967390c8f407 | -3.67123 | -45.77784 | 2025-12-11 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5615c57-8621-36bd-b25b-61a72a62a85f | -2.65613 | -51.64313 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aeded125-fa04-3ae8-b835-9ef898ac23c6 | -0.9285 | -46.89503 | 2025-12-11 04:38:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b34c40b0-f4cf-3a71-a7ce-99777056a1b7 | -3.1923 | -51.14814 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713dcc3c-7919-3133-9ee3-206745f5b78c | -1.42794 | -53.4327 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6cdbbf5-7f0c-3a98-889e-478f04b737ef | -1.58353 | -53.75801 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab81f5ff-0a09-3725-98d1-1b3dcf60f1ed | -2.36456 | -47.68166 | 2025-12-11 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda4c850-c8c0-394f-b200-f6c1dfbaf452 | -1.11169 | -53.69012 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b29076-97a1-3ac1-ac04-31cc1f1d4a0e | -4.65602 | -44.49268 | 2025-12-11 04:38:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50480ba7-0197-3031-a109-96e432580a3c | -2.81292 | -52.39848 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af08712c-07bb-37db-aa56-5e4474f18e22 | -2.21638 | -45.41175 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ff95177-49e6-36c8-80ec-e59a6bb275a6 | -2.21211 | -45.41537 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acb1ae0-e7c5-3b5a-ae73-89ff2ea29347 | -2.10276 | -52.76331 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09f0b15f-46c5-3021-8392-b792eb7178a9 | -1.11111 | -53.69376 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53255ab5-2067-31b4-81c8-fcf7f9cbf73c | -4.12419 | -42.91723 | 2025-12-11 04:38:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ef368cf-3212-3472-8d16-63c8f0b9a882 | -3.67907 | -52.53204 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7774b3ee-e0d4-33cd-be84-0a4b2555c695 | -3.17487 | -45.21252 | 2025-12-11 04:38:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 871facbe-3e40-3811-a64f-2921d4a4165d | -1.18605 | -53.90366 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25298a4c-f9d3-3219-bb32-13cf60d45b81 | -3.23567 | -47.47297 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3a9666a6-e139-39c9-836a-6f7228932076 | -0.92962 | -46.88787 | 2025-12-11 04:38:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85701ae3-59a4-3781-a99c-f7fb44348d79 | -2.55234 | -45.32148 | 2025-12-11 04:38:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49292781-ee23-30a1-b6b4-0c3d99a88f7c | -3.33215 | -48.84963 | 2025-12-11 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20f4ea84-6d3b-3b12-ba46-d3addf507c70 | -2.08552 | -52.05402 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26adbea1-7803-3c34-9e3b-01bdd4551b15 | -2.08185 | -52.05344 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18ad4600-dcd5-3fba-86be-fe825c387721 | -3.70085 | -47.15906 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72cd8e77-2839-37cd-b759-f3e332083fd2 | -1.6471 | -52.1018 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd58a506-e181-382a-b78e-0fd31d1c8412 | -3.75662 | -45.49004 | 2025-12-11 04:38:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 011584af-fa8d-3dae-8e2a-353364006da2 | -1.05529 | -53.67381 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf638bb-fc05-30c9-8654-12b3977d0312 | -3.36097 | -45.33947 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a57a776-43e7-332a-8604-b71f428f094f | -3.09256 | -44.89148 | 2025-12-11 04:38:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 487cca6d-7dba-3f7f-b088-65324e6ee653 | -3.08788 | -44.89258 | 2025-12-11 04:38:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfa823f1-cb28-3800-83de-ef64bdd80e3e | -4.41346 | -44.80017 | 2025-12-11 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 05b67dab-4417-3269-9ba1-7555d8610668 | -4.41731 | -44.80074 | 2025-12-11 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c5f6e8e8-3bc5-39b1-be8f-2826356ab5a4 | -1.16177 | -48.84636 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 892fd715-418e-3f02-9c6e-252047a1413e | -1.8064 | -54.06121 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2c8cd663-ec43-3479-85d2-45f8860e7692 | -2.08423 | -45.32479 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f922fc19-3c4c-39e5-904b-711914dd5581 | -2.26184 | -51.93603 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 364781f3-c5eb-30f9-a23f-b6cba24d35b7 | -2.2146 | -45.67109 | 2025-12-11 04:38:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c52db60-93dd-3e6e-8a8c-bd29e01c0537 | -2.24835 | -46.4545 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fdf2ad9-be6e-3e0f-901c-8c16572a0ef5 | -2.2582 | -51.93544 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d1a6027-3e0d-3dd8-9ec6-5cf6b7eb26a4 | -2.21276 | -45.4112 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4d5ae07-81cd-3ba9-9e8d-274b8cf140ec | -4.20964 | -44.47382 | 2025-12-11 04:38:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c193c42-04b0-3b9d-bf94-f70580234068 | -2.20849 | -45.41481 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0130501a-c4bd-3bbf-a42b-9e047a4890e6 | -1.66589 | -54.5787 | 2025-12-11 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d025e074-c181-35fe-8dc1-b0968e0e52a7 | -2.89657 | -50.23196 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59104864-fbd7-39fc-b40f-fa1de148cc5d | -1.16027 | -47.51995 | 2025-12-11 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6945837-2e80-3823-b292-ada73ba81d5a | -3.84593 | -47.82833 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3310c8-4aa3-3751-aea7-5cb1ecf4b975 | -1.52811 | -47.13003 | 2025-12-11 04:38:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f517275-6ca4-3506-8fd6-acced3a184de | -2.88111 | -52.7197 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 274c6076-7356-39f9-8b4d-0c7a68865429 | -2.07978 | -48.36779 | 2025-12-11 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d37908f-d105-344b-88f1-3d73bd48604c | -3.39314 | -45.42384 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ce3b46-17a2-30f6-970a-28933772ffca | -1.26595 | -54.11028 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d29d397-97c8-30e3-b7a5-b34322f71e6d | -2.20842 | -51.89725 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07b82e41-ac58-3a0d-94ba-d791f9a8ec3d | -2.3141 | -46.47952 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f6f9953-5b30-34c7-9b86-d8789ec2c1a2 | -3.94398 | -50.62068 | 2025-12-11 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c01d618a-42dc-35f1-aaa4-958c4623b72f | -5.15862 | -37.69777 | 2025-12-11 04:38:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fb70af73-08b6-3184-b4cd-46d0c7cb3a21 | -3.33002 | -52.82035 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 225d8a98-de0a-3dfb-a748-a79ed40248c5 | -3.23622 | -47.46938 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7ba6b662-03c8-3871-a1e3-01e219b9f20b | -3.66565 | -48.93393 | 2025-12-11 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e0fdb40-66d2-3985-853a-c2738a6330a6 | -1.78614 | -45.82232 | 2025-12-11 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
