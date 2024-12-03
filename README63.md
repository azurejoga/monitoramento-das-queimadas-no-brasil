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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4eb2bb0-2931-382c-9974-f7931052fccf | -3.1213 | -53.98314 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6820ab0f-99d6-3c06-85d2-819b3f7fa4bd | -3.26531 | -53.61983 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f43412fc-c406-3930-aeea-e2b0f08f0be8 | -3.03299 | -53.4249 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6805adac-9f75-37d3-bd14-8d9c278381c5 | -13.11085 | -58.05094 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09fd4596-6a72-3ce2-b9de-e4dd1b38cf97 | -3.31038 | -53.70809 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6eb6c90-533f-38e8-b857-9cd83d7844c0 | -3.10189 | -54.0554 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34eec5f5-3830-34a5-919c-44de358b8179 | -2.7974 | -53.05503 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1f421d3-7387-3a8d-b9ee-72b06c8b2ca0 | -2.63836 | -54.20816 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38dc62d4-cc8e-35a9-babf-0e56f8ee51d4 | -12.70257 | -58.21358 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5160ab1-8696-322f-a3d9-6e3d2f0cc7c2 | -2.4397 | -54.00707 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 301f6971-5d1d-343b-bebf-48a4657067d0 | -9.6372 | -62.83521 | 2024-12-03 05:25:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c13a4b5-1f20-3c67-bb46-1e5a87dc386a | -4.17203 | -48.19103 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc2810c9-16bf-3887-9474-1619d69b31da | -1.9486 | -53.32947 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f310b7e1-4cb3-332e-8732-6f39e9228f70 | -3.08345 | -53.37938 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 635077ba-545d-3309-8eeb-93db781a0e6b | -2.80799 | -53.0471 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9a93757-8859-361a-95cd-c9e88425808d | -3.09498 | -53.25894 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ec0b431-3472-3216-9308-1171448df1bb | -1.7003 | -52.60715 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a9c8fc7-8d22-3658-8e8f-4335c24b78c8 | -2.89654 | -51.7941 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f6f7e82-7c4d-3b21-b3a4-5ef63f99922a | -3.05822 | -54.49807 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8bebf17-e21d-3567-a0f5-a43c33d518cd | -12.43075 | -57.80722 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b3b9202-3105-3b45-bb42-277461c041e8 | -2.76234 | -54.13046 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0eff508-f1e5-3171-9b41-3863048fb07f | -3.25357 | -53.66702 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a0ec347-7530-33c6-acff-c4e7d1f333e4 | -3.33498 | -53.32476 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4559b176-374f-33e5-a9b1-6d31b205f5de | -3.25354 | -53.66433 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a15ac412-d855-3f8e-8fdd-b8f8c1bd6b40 | -7.00867 | -59.41252 | 2024-12-03 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 022d82c1-17f2-34ce-a061-68e9b413863d | -2.46309 | -53.71036 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c855831d-5fbd-3985-a2a3-8289152c274b | -3.02716 | -54.18429 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f35d689a-6ea8-321b-99f9-d20590d3adf7 | -3.34128 | -51.20419 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b16f9a53-5991-3d0e-be99-2be9e6da1e28 | -1.69283 | -52.63322 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c05204dc-afa9-3169-aeee-016431f19185 | -3.41921 | -54.02831 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24cce94a-d824-3cbd-b336-fec9e5f218ff | -2.81163 | -53.05407 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d5c4023-a69a-3ff3-9604-9627acc59eb5 | -2.56749 | -53.40403 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0942ac61-c285-38ee-834a-7a3446401ba9 | -2.81095 | -53.05877 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f8c04dd-544c-365c-a3ef-189ca6cd8d19 | -12.707 | -58.20944 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95bf13d3-c55e-3b7b-ba17-e61a9615ce48 | -10.05433 | -59.12539 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a60ce0c3-1e0e-3c21-8d54-14f20945a30d | -2.89667 | -51.79411 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d9bb6b-7db7-3fb8-aebf-2787281c9012 | -3.11288 | -54.04046 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0d7cdda-236e-3f60-8f63-4405190c0b7e | -3.18569 | -51.16671 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 10eaa0fa-6b0f-3b67-9e1a-12ae158f5467 | -1.71168 | -52.4509 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc381389-5160-3454-bb32-8665ecb8c2c9 | -1.75735 | -52.79219 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1cfe0db-95bb-33be-a3e4-e680cefd1a13 | -3.1953 | -51.17543 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbaedfd8-f5a8-34f0-9c73-02d1ffec2140 | -10.05198 | -59.11702 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fb77d2c-ba30-3cd1-91cb-5491d40a1d4c | -2.54197 | -55.21569 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4a09d78-d6b9-3ba6-a03a-c9ce7d7cc283 | -2.9799 | -53.8968 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81828916-6cc5-3298-90de-29bab60bc6f3 | -3.01883 | -54.03508 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13539e82-3650-36f6-bf43-261e586f6162 | -3.20933 | -53.12537 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 368eb785-6a4e-3176-8459-a6a232d3aec3 | -2.55019 | -53.4074 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d051ab64-e5af-3e23-9850-014a4a124359 | -1.13961 | -53.22911 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ca45c78-ef66-3117-8afe-ce3a3b7055e2 | -3.75821 | -48.15682 | 2024-12-03 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b62f81d-f166-34dc-aa0a-05bb11c5dafe | -12.57364 | -57.81109 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3b8f3b4-3643-384e-b46f-205ad4142633 | -3.03112 | -54.04111 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 668c2bfb-cbbb-3822-969c-9e66abe27435 | -2.37093 | -53.85202 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b91341f-e28d-32aa-819f-96552d734990 | -2.6048 | -54.22912 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9905aca0-c352-3cb1-b9a1-831a75ec458c | -3.25953 | -53.62793 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e80f73ba-5326-336e-9c2b-6b1621b190e4 | -8.80926 | -64.27202 | 2024-12-03 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94086a4a-d4bd-3293-b7b1-06dd4a6e2b84 | -2.78972 | -55.35562 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c5566e6-c715-371c-8154-f94125b51a9d | -3.08281 | -53.38381 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8171f7b2-71f2-35ce-9bb6-4ed93e918ca1 | -12.7152 | -58.20581 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee7425f1-a991-3bde-9d5e-91e0915c5b2d | -1.39814 | -60.11264 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62513bde-f3ed-3904-8743-bc56132bb0f0 | -1.43828 | -53.39691 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f03622c7-b28f-3468-b580-37fc07043dbd | -2.00148 | -52.09587 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96cc93fc-4b60-3d92-84b0-9c9cc351f8f0 | -2.80637 | -53.05804 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f8e53be-ea0a-3934-879c-a69dd481fe50 | -12.7083 | -58.2001 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2839f598-0277-3359-9d25-9b10ecd35883 | -2.44539 | -53.88432 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 582f0fe9-4dff-31e5-a751-3049d751430f | -4.22994 | -47.57636 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b27d7267-1d28-373e-b390-1e34f322f6b2 | -2.76835 | -54.11917 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a533079-e395-3a7f-af5e-ac63f2a815bd | -3.19004 | -51.17471 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be5c0007-2b11-31e7-8a7c-c00e5a36fafb | -1.10917 | -54.12196 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1a21138-2ce2-3cd6-8307-a12374879c6d | -1.70952 | -52.44776 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f9719b8d-6a2c-35ac-9a10-9cae1fedc4a3 | -3.17493 | -54.32477 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d956410-c2ef-31ad-9813-3ea61cb2a20a | -3.27253 | -53.62706 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec2ccf70-fe6c-37e8-805f-29de83073d2b | -1.76017 | -52.80383 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9d324f4-fc21-3fc8-8285-dd525ed07d2f | -2.81232 | -53.04936 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1545e896-7851-3ef5-80b9-a3b767404a83 | -1.73846 | -52.6379 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bbc76a6-f386-3b2e-93ee-44637fe2c932 | -2.75274 | -55.3348 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cfb14ed-78c9-37ec-9e86-3d52815b7d44 | -3.29151 | -54.1468 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8383e7f-1eff-32b8-9d80-1ad7c72a9c22 | -3.28804 | -50.79576 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e66930b5-efb8-313b-9e5a-b5af401f514a | -3.18107 | -54.34174 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2252ff7-c957-3166-b223-7b8a7605c5d4 | -2.80705 | -53.05334 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea7ad7e8-cbe7-35c5-b23d-fee276752f39 | -3.02895 | -53.87667 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 69f0354f-de59-34c2-98b2-1dcab603825d | -2.83004 | -52.58604 | 2024-12-03 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc9b2911-58fc-395f-bfbb-b33cc07ff0e0 | -3.10298 | -54.01788 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a30875be-18ac-39a7-bbc1-81bd07355331 | -2.3349 | -53.92697 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f94d17ee-9b75-334d-96b3-9bc501556b14 | -13.11244 | -58.04852 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b12ba6b-f583-39dc-a14f-1d8e2ce2f85e | -1.75349 | -52.78677 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8648241d-98de-34f4-97d9-34752312abb9 | -2.44761 | -54.01243 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82867b52-b339-3800-b1ec-5e687305237d | -3.55105 | -51.4572 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ef0edab-3e5f-3c6a-9725-b74cbed60c97 | -3.09569 | -53.2543 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d0e0ed-94df-3041-9665-15d7ea4cd1bb | -3.03081 | -54.1889 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 279a87b3-9a90-3fc1-9235-8d635ff9ae1a | -3.26396 | -53.62864 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6c5f885-7bfd-3d1e-b330-c9853a3c0d2d | -3.70634 | -51.82714 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23168c2-f12c-378d-8b59-097fd701ddb8 | -2.19122 | -54.0165 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0553af5a-c1c3-31a4-afa7-908bec41a7a3 | -3.43147 | -53.88949 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1a66448-effe-3a1f-aaef-4157345dd854 | -2.983 | -53.90558 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3980f92-7e58-3d05-b204-3e80526a03c4 | -3.48565 | -50.24813 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1be83172-4f57-3700-aae5-fccbb2389d40 | -2.65168 | -51.89539 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 760882ed-aa6e-3e3a-8cab-9365a3cb4a6c | -3.37417 | -50.6997 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c296038a-6443-33eb-9b25-9dff12c49eba | -3.25003 | -53.63077 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c90c201b-48bf-300f-a3b8-dbec0a65c11f | -2.23062 | -53.69928 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f085f306-c25d-3bfb-b938-52fe0afae383 | -3.26088 | -53.6191 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README64.md)
