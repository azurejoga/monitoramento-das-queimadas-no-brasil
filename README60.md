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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4da88bd-087c-3aec-afbf-685eacf4cc98 | -8.66139 | -68.7739 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d93f0a97-436a-33e9-9ebb-7a1a0b900296 | -8.75558 | -69.33746 | 2025-09-05 06:16:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91b5633e-bf17-376f-b7a4-ecfe973243ff | -8.66644 | -68.73875 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce93c89c-f235-36ed-8928-2414939f75cb | -8.52989 | -70.73201 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15631a5e-2c57-32e0-af43-1ad6e38034a9 | -8.69367 | -71.05148 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b914e30-bb55-37b6-96e4-22a3279f4053 | -6.77962 | -63.13739 | 2025-09-05 06:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b1ac7bb-17fc-3b0b-9329-f301c377ab19 | -5.50621 | -60.12191 | 2025-09-05 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 157f22e2-344e-313a-b8da-fbc2b9cb94f9 | -7.99528 | -71.004 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7198e952-ce1f-3a98-9860-d28c9d024458 | -8.53285 | -70.73666 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0be8b84-a6dc-3395-b5c9-556612986727 | -8.66191 | -68.74171 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35ce806-bff5-39ac-89a3-40290fc01f6e | -5.50538 | -60.12793 | 2025-09-05 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5cd4e01-a81b-3151-acbf-c8483a1baa17 | -8.37513 | -70.84628 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 484302d2-0a39-3e25-8cc3-8b046d0fb7f4 | -8.75548 | -69.33581 | 2025-09-05 06:16:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4014957b-ef63-3031-9ca3-46da006031af | -8.69014 | -71.05093 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4fb511c-b589-3e0e-a577-1e99a2086944 | -5.49859 | -60.12698 | 2025-09-05 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d4108be-4db9-31dc-a469-a7bec721c281 | -7.80776 | -72.99596 | 2025-09-05 06:16:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1bf5809c-3169-3555-aa31-9f0638500133 | -8.65788 | -68.7411 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6f0940a-aca5-3b46-8dae-c63865fe6420 | -8.75936 | -69.3364 | 2025-09-05 06:16:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deb16cdb-83ec-35a3-901e-147e8ac7d41c | -7.92106 | -72.96372 | 2025-09-05 06:16:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9261753-b380-383d-95cf-dcb8e336e01c | -5.49179 | -60.12603 | 2025-09-05 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb8ed6c6-803a-3b00-817c-f0a4b9a33673 | -8.6619 | -68.77038 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05e23097-525c-3817-9285-d10e4c96cc1a | -9.08396 | -71.96124 | 2025-09-05 06:16:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 623600cb-3fea-342e-885c-0477d8594f8a | -8.52927 | -70.7361 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fcf8f6b8-9aa1-39ca-9107-aa914cd481e1 | -12.35051 | -63.64331 | 2025-09-05 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfad51f9-744b-3a56-9a87-31f0ed222396 | -12.35596 | -63.64842 | 2025-09-05 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ca6d9d0-8954-3d13-924f-9f156db89727 | -12.34999 | -63.64772 | 2025-09-05 06:18:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebfaf3e4-12a1-31e5-8677-27e07070852e | -12.9859 | -54.7891 | 2025-09-05 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9a162d81-5638-357d-90d5-011325d62ce8 | -12.9665 | -54.8116 | 2025-09-05 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| dad25895-c0b3-3465-8713-bf00c89e427b | -12.9668 | -54.791 | 2025-09-05 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 161.5 |
| fc43b1fa-210b-311c-87ab-c32c9c037ab7 | -12.9477 | -54.793 | 2025-09-05 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| a73aed8b-78d2-3bc8-89b5-469ef58ee0da | -12.9856 | -54.8096 | 2025-09-05 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ebeb4843-551c-3fff-8081-5cfef4ac3dcf | -5.53272 | -57.24293 | 2025-09-05 06:29:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 60aee1dd-33d3-3f2f-be3b-522ddc0ff9e2 | -3.32587 | -54.90576 | 2025-09-05 06:29:00 | AQUA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 50bc3333-4987-3d82-b852-ac70560c7b5c | -4.99808 | -56.25539 | 2025-09-05 06:29:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ddd53d0-208d-3bd4-a918-b4b63bf214fd | -4.20659 | -50.44009 | 2025-09-05 06:29:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 15e6c255-9f74-3f7d-ac09-9fdc03413de0 | -12.9856 | -54.8096 | 2025-09-05 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6d8536f8-35e8-3514-a666-b645c68f6239 | -12.9665 | -54.8116 | 2025-09-05 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2ffe0529-4153-36b2-b8e7-c8e8dce58d28 | -12.967 | -54.7705 | 2025-09-05 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3cc9513d-9263-3ed2-9d3d-4d104b380be3 | -12.9477 | -54.793 | 2025-09-05 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| d62b0206-640a-3a25-b1c4-44d3624a9730 | -12.9668 | -54.791 | 2025-09-05 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 254.2 |
| 2e37378e-5ddd-369c-b4ef-0c19010e7b67 | -9.07963 | -46.98856 | 2025-09-05 06:31:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b8800c0f-2a54-3884-8263-a3ede0f14d27 | -11.60611 | -47.73636 | 2025-09-05 06:31:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 7af018b0-2d69-3aaf-bc0d-a1ea0759f344 | -9.0661 | -47.01774 | 2025-09-05 06:31:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 276eaf77-42aa-36d6-a453-a5055806d86e | -11.59534 | -52.17163 | 2025-09-05 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e0d4ffb6-2138-32cd-985d-b3cd3739185f | -9.71142 | -51.07941 | 2025-09-05 06:31:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b93a691f-33fa-38df-93ae-e691ab7b1b1b | -6.32963 | -58.1719 | 2025-09-05 06:31:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7adec188-043e-395d-b265-1e1aa6105a64 | -11.6126 | -47.73002 | 2025-09-05 06:31:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 54ad94d0-ec3a-30bb-87ee-2191b52961fe | -12.95274 | -54.78852 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 13bec843-2f3c-3e3e-83a6-9847563f67e9 | -12.96361 | -54.77948 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 7c4a1689-e9d1-337d-b93a-d1352f9caf17 | -11.64602 | -54.5288 | 2025-09-05 06:31:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b5270647-49b3-3091-8b14-4c41c666ca33 | -9.33273 | -55.20663 | 2025-09-05 06:31:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 293710a5-a030-3017-9b55-7a897f87e6a2 | -11.6251 | -52.21189 | 2025-09-05 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7204e799-7b5d-3a3d-aa67-dc40eb6d914b | -12.97011 | -54.80153 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d351ddef-0737-32ea-87d8-feaac1da2b3d | -12.97157 | -54.79118 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cf495744-d7fc-3900-bf75-63c13228231b | -12.99687 | -54.81589 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b3f411e8-c07b-3ca0-b1af-68d0403d2300 | -13.10442 | -57.11234 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ca9cefc-fe1a-301f-9519-b336a7dede00 | -10.06204 | -58.38435 | 2025-09-05 06:31:00 | AQUA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da392e0d-073c-3ff6-9ef4-fb4c402fdbe4 | -11.1987 | -55.00785 | 2025-09-05 06:31:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 90a8b9c4-a91f-35ac-a3da-24407c401803 | -12.98893 | -54.80423 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 769c9ec4-d1ad-372d-9cb5-2f15cd6da8fb | -14.78929 | -48.11608 | 2025-09-05 06:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 00324b97-0539-3a9b-9212-0ad3b578f9ee | -12.98746 | -54.81458 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 40acab65-04c6-37ed-8606-57b2bba5e3d7 | -9.07033 | -46.98423 | 2025-09-05 06:31:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3f01876f-8864-325c-a72b-c72208536e2a | -13.10577 | -57.10337 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7c51cfd-e1ef-318c-a6ab-82a313cde436 | -6.32015 | -58.17044 | 2025-09-05 06:31:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4409cd52-50cb-3c1e-a850-984ad47fb602 | -12.9607 | -54.80021 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 654d5994-832f-3ab0-b90f-cd51181750dc | -12.97952 | -54.80286 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d92dbee0-d7b5-362b-bc0b-100270afbdd4 | -12.97806 | -54.81318 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| ec890f55-113c-3280-8220-ef5e597dd8ee | -11.62453 | -52.20488 | 2025-09-05 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c8d8294b-9bd0-3ee1-b390-bbb4fa6fbad8 | -10.51676 | -57.77313 | 2025-09-05 06:31:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58beaeee-022e-3b10-bfb1-fbf89a6c0c93 | -14.7987 | -48.12168 | 2025-09-05 06:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 6ad1337d-ddc3-3bd1-a2ab-517afbc972ef | -11.64455 | -54.53908 | 2025-09-05 06:31:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e97d793-ddf2-3eb4-a4c6-e6292abe12a9 | -12.90792 | -48.01215 | 2025-09-05 06:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 25a0c8b8-1e33-3e9c-aaa2-594e942e13ac | -12.95419 | -54.77814 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9502b12f-7e35-32fc-84ec-96cf4a0efbe3 | -7.79884 | -52.13047 | 2025-09-05 06:31:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fb1eca30-2a2f-3905-8ec0-aa56b551a336 | -12.99539 | -54.8262 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 43.1 |
| ce918354-dbd6-319c-a7c2-76f4b5577cda | -12.96215 | -54.78988 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 048ee226-8144-39c7-8209-565a04b3cc34 | -12.9513 | -54.79881 | 2025-09-05 06:31:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 38d656cf-6990-3dea-86e7-dbecdc7a45e1 | -15.06281 | -50.06602 | 2025-09-05 06:33:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| d90d5a16-cda0-3f8e-956e-1afbade6061c | -16.61205 | -50.17596 | 2025-09-05 06:33:00 | AQUA_M-M | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 67b39c03-e5db-3810-a3c6-8ba96fc926ec | -15.14573 | -52.36975 | 2025-09-05 06:33:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1152b856-de72-35e2-9654-27ab34868c54 | -15.85197 | -52.29476 | 2025-09-05 06:33:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| af6cd15c-17a7-3441-a5ac-27eb593d2b2d | -20.23706 | -51.29825 | 2025-09-05 06:33:00 | AQUA_M-M | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| ca87b684-bcba-373d-b059-f6cdbf4d8d47 | -16.61614 | -50.18346 | 2025-09-05 06:33:00 | AQUA_M-M | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 02f44f35-a777-3f1f-8a57-3e1c9ec7f398 | -15.61678 | -52.89645 | 2025-09-05 06:33:00 | AQUA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5bd35c55-a3f3-3ff8-8f3c-cd007ccde0d7 | -15.31567 | -52.7411 | 2025-09-05 06:33:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d77b5aba-a40e-3a7c-a066-c1607a81bd48 | -16.32052 | -52.94753 | 2025-09-05 06:33:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 40b51b61-ada6-37e9-a37e-6324a22d4070 | -8.65771 | -68.77286 | 2025-09-05 06:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 799ba4af-b60b-3719-b386-f9e318e5dfd2 | -8.37359 | -70.8514 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b77e608-f846-3975-a75b-c2b05ca83dee | -8.52902 | -70.73653 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c352b54-50c7-3812-9862-a9da1d82d6b0 | -7.99346 | -71.00816 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34102918-e2c6-3fef-86f5-a7afe5237808 | -8.75363 | -69.33913 | 2025-09-05 06:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ab8eea2-68cb-3ec0-b80e-a22d28a030a2 | -8.65852 | -68.77093 | 2025-09-05 06:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bb0fff1-948b-3370-a574-8a9a3efb7cd0 | -8.5312 | -70.73754 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2c84a41-8638-3f7f-8887-f6c5d9254ee3 | -8.68846 | -71.05166 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d2bff0a-855c-3714-ad1a-8914547486eb | -7.57753 | -69.89701 | 2025-09-05 06:37:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d91816dc-f1e0-3023-87f3-c75b04349833 | -8.35673 | -70.31009 | 2025-09-05 06:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af53659e-9417-3b5a-b0d7-3cfd3ac71b29 | -8.37405 | -70.84801 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e398da8-9ab3-3a87-acd6-1ba31869c182 | -8.69375 | -71.05247 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d454a5-286e-34a0-a351-ffae51a199ef | -8.65788 | -68.77579 | 2025-09-05 06:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d09cfb38-1bfa-3226-8dad-3985266c42ca | -8.53165 | -70.73408 | 2025-09-05 06:37:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README61.md)
