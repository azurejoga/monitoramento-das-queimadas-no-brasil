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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba0b24af-a095-36a5-95cc-b6758c0dd663 | -13.1359 | -51.19586 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 6af4e7d1-6219-3374-ba0c-063f402b7d03 | -13.13227 | -51.19521 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 187efca8-3e8b-380f-a5bc-3b090aeb89ea | -13.12865 | -51.19458 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6d1e550f-aadc-3eeb-aa2c-acce8f9a64c2 | -13.12502 | -51.19394 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bcad45d-a8a3-3b1d-a6a0-1c3e1042def8 | -13.10834 | -51.17842 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acf93715-0fab-3c8b-a00a-ae887ed90300 | -13.10761 | -51.18273 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c369f3f-21c2-38c2-b5ad-95444b787c26 | -13.10399 | -51.18209 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f22948f6-4dbc-312e-9f85-6b54880ca9b2 | -13.09602 | -51.16294 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 399eba86-8545-365f-b761-5090450daa05 | -13.09529 | -51.16725 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5eb5fbf4-0650-3686-9e8e-af72276fe67a | -13.09456 | -51.17156 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4c3a131-73bd-33a9-9671-8eb38726da1f | -13.09312 | -51.158 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 56c587d0-f53f-3f3f-bf9a-58072113c654 | -13.09239 | -51.1623 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 992d4d53-17c3-315c-b476-bee2f6420fc2 | -13.09167 | -51.16661 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 67032ce4-0248-36e0-a989-a6318a828a85 | -13.09094 | -51.17092 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a3d8de20-57ac-36ae-9bc9-1f1556bcd935 | -13.09021 | -51.17522 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2e3d1f5-2d78-3e74-8776-b6ba947d6756 | -13.08877 | -51.16167 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 4789cdb4-9d43-3471-bfce-2baa297ac97b | -13.08804 | -51.16597 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bef31302-3541-3303-817a-cf90bbcedcc9 | -13.08731 | -51.17028 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8d9345dd-b466-3942-9ca0-e585cd352aaa | -13.08442 | -51.16534 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 05b86778-959c-33ac-9823-84311cdbbba0 | -13.08152 | -51.1604 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 27465333-4f0c-3df2-bb3d-f6644edd4803 | -13.0779 | -51.15976 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 70d97225-daf9-3ee3-9898-af1876c5074e | -13.07717 | -51.16407 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e5b6b7b-f71d-37d4-8b99-b48acb71789e | -13.07354 | -51.16344 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14db9ab5-6797-3853-9067-128c83b12c6a | -13.06629 | -51.16216 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54aaf629-dc71-36ea-980a-8db996d6eb9c | -13.05978 | -51.15658 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| be523fab-b3ed-3163-9bd3-0f947cd04097 | -13.05689 | -51.15165 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cffa8ce4-f5a1-3dbf-85d9-6397d2c8db10 | -13.05616 | -51.15595 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 99cd3269-bd6a-32ab-9a80-9705b7848857 | -13.05253 | -51.15532 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0b1f102-4ad4-3d66-a0a0-7f64c0a1c04b | -13.05038 | -51.14608 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d5882a6-d645-3900-a095-5bf85e7d0cd9 | -13.0475 | -51.14115 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d4873baf-3012-3a0a-a0ab-2cf1e844fd45 | -13.04676 | -51.14545 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3b6ee424-2797-3f1f-8363-686798b5cbbe | -13.04602 | -51.14975 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aadf7fc7-18ea-388e-a148-30feaf75e480 | -13.04387 | -51.14051 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f05cf1e9-9dde-3002-ae80-797ca8684f16 | -13.04314 | -51.14481 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 63d08ea8-93a8-39ef-bbe0-8cc74313ad6c | -13.0424 | -51.14911 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1d4f465a-b625-3635-97a6-f4a898e5e469 | -13.04025 | -51.13988 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 33b72d10-f3d8-3531-b6ab-92bac5c52c76 | -13.03951 | -51.14418 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d53538c4-6f6d-32c0-8799-75edecdf10e5 | -13.03737 | -51.13494 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 99d4245a-8492-328c-b99f-809be179b4da | -13.03663 | -51.13924 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 04e323e2-3653-337e-9feb-52a4fb9d3744 | -13.03589 | -51.14354 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 13d84e69-33fe-33d8-a5f7-92d3285ed744 | -13.03375 | -51.13431 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 6ef711c7-4dca-3067-ab9f-159176dc416a | -13.03301 | -51.1386 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ee16384e-d044-388b-a8c5-b5fe288463b4 | -13.02939 | -51.13797 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7341dcf4-c11e-3665-9dbd-5b9f5b109117 | -13.02577 | -51.13734 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c0f1d7a-a1b7-368e-aa5d-352ad15b4fdf | -13.02215 | -51.1367 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 122dfdd5-0454-3c38-af30-7bbbabc13181 | -13.02169 | -51.13367 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b4a851c-3c1c-30c9-bc40-b871545338f9 | -13.01853 | -51.13607 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44035977-6be2-3ca7-a9c3-612e24b0ea79 | -13.01155 | -51.12745 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 376a9910-1d83-3e6f-a157-6285c07fa42b | -13.00792 | -51.12682 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf638cf1-c567-3291-82e7-7b72686e3c5d | -13.00503 | -51.12189 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2d278c5-113c-3941-ac96-0fb818a53e3d | -13.0043 | -51.12619 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7d07690-3820-388c-9ddd-87bfaf288695 | -13.00141 | -51.12125 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1610e2ac-aa6d-366d-8f90-4adccdfc8dbf | -13.00068 | -51.12555 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bb206ff-bd03-3f1e-b8d1-1ede9517fcd8 | -12.99996 | -51.12985 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e399384f-6533-3d64-85cd-d85d8b4f1959 | -12.96737 | -51.12411 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc1f688a-9597-38a3-b189-50b2db3ed43e | -12.52589 | -50.61943 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8e7f630-8f4c-300c-a336-b0ed88eb2e44 | -12.40005 | -51.01335 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 557a7065-4863-38ed-bfd1-2c511c225082 | -12.39931 | -51.01765 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91711dd9-6679-3ecb-8b4a-326e45be2d3a | -12.39642 | -51.01273 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13186d00-4a4e-35d3-affb-a31c1ea19d85 | -12.39568 | -51.01703 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21728a5a-018e-355a-9ca6-3631bcd90c35 | -12.39514 | -50.95512 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e31a54da-549e-3d46-90e3-5428a89320c8 | -12.39441 | -50.95939 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 974393fa-bc0c-34e4-93ac-b72450cea728 | -12.3938 | -50.95639 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ead0d8d-dea3-36a9-8e92-d6ee4f44193e | -12.39279 | -51.0121 | 2024-10-03 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8e4b691-0dce-3074-92ba-7d2d9a1ad13a | -12.39205 | -51.0164 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1a6971-0c4f-3145-9ab5-0043a0658c29 | -12.39079 | -50.95876 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff9ee03-e867-3c66-ba18-76fd33f5d5df | -12.3871 | -50.98016 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2fd11fc-d8d6-333a-a1d5-3069ed36fac0 | -12.38636 | -50.98446 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c8a0b4d-6b40-330d-9096-b63d0fc25594 | -12.3859 | -50.98148 | 2024-10-03 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4326a70f-5253-3ca7-be9d-5c001dbc8e85 | -12.33538 | -50.43316 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3823018-6768-39d5-b364-ea0781bc26fe | -13.63664 | -50.34539 | 2024-10-03 04:27:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e77761e7-3412-3826-8a49-948aa31b9ee1 | -13.63383 | -50.34087 | 2024-10-03 04:27:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 614cf0d5-4489-3c7f-8875-f4d2e79f266a | -13.63317 | -50.34478 | 2024-10-03 04:27:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bbf87db-fa6f-33c6-b74c-89cc166195fa | -13.07664 | -50.84148 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b868f794-2a00-3813-b73e-98469b277a8f | -13.07593 | -50.84565 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 018f3e2d-183e-3767-9e0d-3fa0f9bee575 | -12.7927 | -50.58716 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f289a71-d96e-3b00-8ace-1676d9fdf3e4 | -12.78916 | -50.58654 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ffc6727-1f9f-303b-9755-3b231d1bb4c3 | -12.78573 | -50.58697 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 587c8e66-c754-3f63-a0c9-54718675e856 | -12.78562 | -50.58593 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c83af354-15fe-3882-b17f-b022f987926a | -12.766 | -50.59616 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0cc7e5e-0839-33a1-9d76-12a31574c4de | -14.40876 | -50.03858 | 2024-10-03 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0a0fab2-d34a-33a5-a056-284df482752a | -14.08736 | -50.36459 | 2024-10-03 04:27:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a50f2e29-b5c1-35c5-ad31-a2d324885337 | -13.93655 | -50.85276 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 742e7079-d34e-3839-941c-ee129c95497c | -13.93095 | -50.88681 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2eeb4224-d245-354c-98dc-3160429d8142 | -13.93092 | -50.88555 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4202d201-f24d-38fe-b611-6c374ed087a0 | -13.70913 | -50.86641 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5103c4be-fa52-3e0a-bc75-331f962f2648 | -13.70892 | -50.95034 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a9e0eae-a4cf-39ab-8bce-dfb78d474e0e | -13.70844 | -50.87053 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f5c857-74e8-373f-8672-26afe97c2957 | -13.70668 | -50.94691 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93fff0d1-9644-334e-a549-55aefca9f8a1 | -13.70607 | -50.94557 | 2024-10-03 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7631a7eb-23f9-3393-93ed-67561e73b767 | -6.95346 | -50.58501 | 2024-10-03 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5224d35f-de21-390a-8f4b-f15378f07d79 | -6.83466 | -51.22398 | 2024-10-03 04:27:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ad3a7b-c2aa-38c4-9196-046bc1ac0fca | -7.86858 | -50.22744 | 2024-10-03 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c7f155-f288-3a13-baaa-1c9762e04529 | -7.78604 | -50.2289 | 2024-10-03 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 935ed8e3-8c73-304f-9872-562ed0697cf4 | -8.52497 | -50.97613 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2933c52b-c039-3e2d-9422-0129a63460a1 | -8.40217 | -50.7564 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d8e17ce-9be5-3799-91ea-e49290404152 | -8.4019 | -50.75935 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34c00890-f1a9-39f9-ab67-fdb1d9a71460 | -8.40137 | -50.76131 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87f45118-c2bb-321d-bc51-965cdef2e4c2 | -8.28835 | -50.92484 | 2024-10-03 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51f86809-b36d-3b52-ba45-05f2e1f75963 | -8.28378 | -50.67303 | 2024-10-03 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README96.md)
