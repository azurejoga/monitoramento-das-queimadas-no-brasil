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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d19bf19b-ce09-3cc3-8ae7-a27123eba591 | -6.32527 | -59.99312 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1681e68-00e5-3046-9e79-4027f38ee1a5 | -3.75861 | -51.1443 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbcec762-2205-3992-b426-ace23a1ac5eb | -6.33071 | -62.68144 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ede79e69-1870-3c34-a9f1-57b44ee84c6d | -2.89468 | -50.41513 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b61697f-f5f3-3fee-8e73-27dc602329de | -5.82164 | -52.10652 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3753e99-f64a-30ce-8fbd-4a7bdabec9bc | -4.80877 | -42.88456 | 2026-09-16 04:57:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d44f2f3c-a711-3448-844d-fc6722ffad43 | -4.34126 | -46.61445 | 2026-09-16 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| edeb1db8-6ab9-34c6-8100-9ba568ee19d5 | -5.13324 | -55.94038 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e418fc34-3957-300e-a0b7-9f38c6d95634 | -6.3433 | -62.69862 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b5e2cd7-7fec-3ff5-9024-c15a81c85d37 | -2.73254 | -54.98264 | 2026-09-16 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e288fe4-9923-35bd-943e-b8bc35d27e57 | -3.10422 | -51.18468 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 911261c9-2f3f-37ed-b5a9-0b0d997a22ea | -5.12699 | -55.93571 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f607f1e9-dca9-39ba-b8b3-746e9a49a561 | -5.12183 | -55.9462 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f283d30-0bda-3749-a61c-63b2fd0a721d | -8.64653 | -44.45305 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79461ee3-ce98-3209-9e62-e0092e7ff0f0 | -1.28757 | -55.71136 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b243296-b59c-3676-8944-ee2883800dfe | -6.33172 | -60.00607 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244e0ee3-ded4-396c-afaa-0fd298f92c5b | -3.36308 | -50.74594 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83cd42e0-a66c-3351-b5fa-a1f29636dc1d | -3.2316 | -50.58532 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| faa61f89-f230-30a1-963a-330448dfceb1 | -2.10296 | -52.04354 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a32c6ac-baf5-30a6-bbf5-69b1425ee136 | -6.43869 | -58.14365 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35b43572-00bc-38ab-aa35-bb1127879e75 | -6.33828 | -62.69776 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 784e29b5-2222-3dbd-8df5-781343e340f3 | -5.63687 | -51.67896 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39051ddb-ee85-3db7-846f-844c848ecfb4 | -6.61394 | -51.44003 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18340ef6-1bad-3f3b-b747-af663c7001e8 | -3.74178 | -57.16392 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b924ee3c-4e41-3910-9ca9-8df8ee69f5f5 | -5.60783 | -44.83929 | 2026-09-16 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5184c2c-d8e0-3d6f-8ff1-7124baafef81 | -4.38788 | -55.03751 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebd07a5a-e3d8-38e4-9f7d-4480aaa0c54f | -3.08092 | -50.57154 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9721c9a6-97ec-35f7-b934-46176fb39f8e | -2.77109 | -51.36987 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26da77e0-4985-30bb-ac27-ac46cdb498ed | -2.9818 | -54.15651 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728af432-173c-321e-84b1-3420db0ae27a | -2.95496 | -50.40739 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0c9a1b1-dceb-3be7-829d-697b1019a7bd | -6.14004 | -57.69244 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc5e3a4-f581-35c9-89ac-86178022bf78 | -7.083 | -43.56789 | 2026-09-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb5c0973-d047-397f-a91c-6199a01f9b7d | -9.5544 | -45.42374 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04176b0a-59ab-3f97-9e58-c88eefe044f3 | -7.60846 | -57.61272 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 756c40ef-c212-340a-ac14-670390ed90c6 | -6.33474 | -62.68814 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c15f56f1-6fdf-36b8-b02f-bf473d9fc300 | -6.32592 | -59.98922 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 046ee107-1e52-3d64-9497-21e35fe2f9de | -2.63953 | -54.69193 | 2026-09-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc5d5f62-03ad-363b-8f8c-33b9b37d9a5f | -3.14517 | -51.10367 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a00c0791-eb7c-327b-97df-1b0b7b1039bb | -2.94711 | -50.41042 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 534d9baa-13e1-3d5d-8cce-bead1c30fdfd | -5.10686 | -47.60529 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f8683ea0-b72b-3ed5-82f9-1d6404e61f70 | -3.84996 | -51.76812 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96ef4918-a26e-35e7-bad5-f817f30b8153 | -3.12192 | -61.25779 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41aa2778-e8d2-3495-89e1-fae3c2ee4cec | -6.33021 | -62.68436 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eaa09e14-f1ed-362e-b377-99fb9b2a8ee0 | -5.12242 | -55.94254 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45bb1e93-2367-3e54-9727-9fa8581de810 | -3.10466 | -51.82621 | 2026-09-16 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19b883f7-3fe8-3f6f-a6a3-b492b470f635 | -6.33501 | -62.68377 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8452b5b7-93fc-31bd-bff8-830189f0cfe0 | -6.11401 | -46.10345 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bafcd7bb-3ce2-3390-b1bc-e8666804591a | -6.01969 | -51.79875 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78ad9bae-c4a6-3689-892a-e87cfe1fb752 | -6.36928 | -55.82829 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445f784e-bfd6-3027-be2a-5f910ceab04f | -6.18914 | -44.03438 | 2026-09-16 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 780418bb-8393-3c12-92af-992fa1e7a5d6 | -6.18969 | -44.03046 | 2026-09-16 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0a8ffcf-9625-3fce-8b33-49c8326ec8bd | -2.91994 | -50.41901 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25ba0bb9-3756-3a1e-b48e-bd955b49b89f | -8.79545 | -46.90351 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e38ddf7f-7e02-3c7f-9c78-65df9e41c9ba | -2.64008 | -54.6884 | 2026-09-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46cea4f1-c93c-3b9c-bd3c-f145d08a6762 | -3.43082 | -58.23034 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b070ab2-2d3a-3fa1-a227-6bbb131c93ae | -6.33877 | -62.69485 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e232dbcf-7416-371e-a03a-331fd6563d49 | -3.84782 | -49.05887 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a11f03f3-8be5-3c75-b2ab-2c0711548aa4 | -7.87275 | -54.72791 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ee41a9e-b8e7-3fd0-8abb-9798e120796a | -9.11011 | -45.72832 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 20c00d2d-b3d7-3522-a044-cb90facb7382 | -8.85016 | -44.90627 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa5b8858-1eb1-3684-941b-b7d648d203b1 | -5.37211 | -56.04955 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9f14aab-9d95-3794-8e50-f8cdb5ee023c | -5.22405 | -49.30837 | 2026-09-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89157073-755b-3c65-90b9-ce771e769a70 | -6.10608 | -57.62627 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49d042f3-27c1-35f5-ac66-40d4cb1f01e8 | -6.77092 | -58.81473 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb631acc-bd93-32c6-b661-3191739527da | -2.91163 | -50.40072 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e63c723-65c0-3335-aaa9-c2bada4c0872 | -8.01786 | -54.84282 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9706b79-80e4-364f-8d6c-7b47848fbeb7 | -5.83714 | -52.09729 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d7232f8-d487-3ca8-907b-f369355381a9 | -3.8471 | -51.7639 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e44fa188-666b-3fcf-9bab-0b8201d8e96e | -3.42302 | -58.22912 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 177ffdd6-246b-382f-8d3d-3ed5e3d8e63c | -3.10481 | -51.18082 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c39afe6b-ddfb-33af-ac2c-eaf895df41a3 | -6.10538 | -57.63049 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aad27178-c461-36f2-b462-b45480fb7ad2 | -2.91507 | -50.42675 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c846dce-f0bd-30ff-9e54-70be8187c20f | -5.84117 | -51.95439 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 55b3acd4-b110-3f53-ae52-662d0212bb5f | -3.71409 | -60.61795 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11093d54-3e87-3e42-9353-dbc09790a0dc | -3.84148 | -59.33139 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb3ce5f3-c642-33d8-a914-b25f82060954 | -5.63512 | -51.69067 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4a83df06-b4e7-3f0d-86a0-b52c02e45535 | -6.82645 | -58.6482 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ddc9cd4-c1c4-3488-bb75-b89ca68d9f34 | -5.9881 | -46.63129 | 2026-09-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7eb3d60-1b0f-309c-87f5-64f17c1f4ddd | -5.84463 | -51.95493 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fa310eb-5461-3d5d-b470-529b4b7e6d80 | -5.97681 | -55.36066 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a41b2ed1-8ac1-3fdc-9026-661bf5ba4769 | -4.37562 | -55.02845 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aecbc124-9f55-359d-a84d-3d18ef6611ef | -6.33848 | -62.69337 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997caf6b-b756-3c0d-833b-63a191b79033 | -2.97186 | -54.15499 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11d783ab-5666-392c-a789-6dd663d8dcd7 | -4.51862 | -54.9425 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb4983c3-aad3-3783-b406-a6ad1d940680 | -6.02299 | -55.34973 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e244ea30-6921-3bb2-9f52-e0fb3a6300aa | -3.48486 | -54.67994 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedbc3b1-5f30-36fe-b4ff-3d138de9df23 | -7.26475 | -46.17761 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8800bdea-66bc-3831-aa57-fb01bd9c099f | -3.76709 | -59.39375 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce9936a-4fef-37e2-8918-b0578ecfeed5 | -7.71325 | -55.37453 | 2026-09-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e4ce43a-644e-315d-a28d-d728dbf33d83 | -5.24616 | -59.98061 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59df88f4-176b-3d1e-9ead-24adac4d3188 | -7.87714 | -54.7215 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2fe6715-9b4c-3a34-90cf-6ccabb6159c3 | -6.37007 | -55.13197 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87f2e366-702c-30e3-9816-952f20e62060 | -6.62671 | -58.37399 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4887d9ee-a8b3-320e-b003-0104648ec0f7 | -6.02661 | -57.76714 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23b1b163-234a-31a7-abb5-aec8a33c060c | -1.74458 | -55.25437 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d85a5044-cd48-3714-acc5-805c61083672 | -6.62848 | -55.13378 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceb6f9f5-2745-3296-a927-92618650099c | -5.1492 | -55.92779 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bce8c07a-8655-32cf-934d-7d89284e1fc0 | -8.80356 | -46.89387 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2ce97c6-5dfc-3cde-9258-e0417f12d0e8 | -6.28545 | -59.92371 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a67b82-5163-306a-9805-e592eb8ea67b | -6.34281 | -62.70155 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README43.md)
