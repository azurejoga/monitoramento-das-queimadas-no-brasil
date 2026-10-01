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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68bf937e-0c00-3c05-97d6-a5a25f57e9da | -9.07131 | -49.87651 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38fa613a-168c-3cd7-baae-ab69624b3c0c | -9.22703 | -45.83718 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad9fddbc-0227-399e-86f5-de606bb3b128 | -9.23265 | -45.84532 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff0f1fb2-3b19-30c8-9274-98d5e6782e0c | -8.85978 | -50.52559 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c383ec15-ab81-3fad-b9aa-30b47604c123 | -10.4604 | -51.76713 | 2026-10-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dddc5638-856f-3d50-bad8-459e688f811d | -11.43979 | -43.42786 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04361753-8cf4-379c-a75f-2303af4b750a | -12.90509 | -44.81717 | 2026-10-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da77ef71-0fde-3869-aecc-c91e1aeef863 | -7.83487 | -45.82086 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73df2346-1e58-38a8-9542-acb30e3d9cd0 | -11.44115 | -43.41833 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c25f2848-eb4a-34e0-85e7-9957e23d64b5 | -11.39308 | -43.37215 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23ca9c8e-5a84-38d6-9e19-aea989ed4f00 | -13.34641 | -46.82697 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 124f476e-2a05-33fd-a622-a90754d617fb | -13.38921 | -46.82898 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8951b2-4348-314b-868a-d5aac220273c | -9.61372 | -47.76159 | 2026-10-01 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddf23f40-ac9c-300b-9e69-f14f5923c4ab | -9.08122 | -45.00974 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e038f6d7-b46f-3138-a82d-9b6ca4f765f0 | -11.26359 | -43.52422 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0894d0d7-ec1b-3b6f-a409-e496749ecb54 | -10.83667 | -48.71244 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3c51a9a-fd04-3c7c-80a5-cd91e841e2ee | -6.76219 | -48.67811 | 2026-10-01 04:34:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75400c48-a553-3137-8778-bc44ae6bf52c | -9.76604 | -44.81293 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 954c0083-45bc-3169-b843-94f9e01c5d08 | -11.42657 | -43.41129 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7508ecc8-38f9-3d01-90a1-017d96ef69c9 | -11.17986 | -44.8341 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96c02171-9e66-32a1-ba49-537fe771d923 | -9.86036 | -44.98846 | 2026-10-01 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8782482c-105d-366b-81ef-a238d7d09fed | -7.71883 | -54.7898 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05482ac1-10de-3d24-8ede-ed81b0df5ba5 | -10.76941 | -54.75719 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b65336e2-d811-3904-ab58-18daec198069 | -8.15884 | -54.80712 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d2f31ac-1942-3d05-a1e4-816388bb850d | -7.47187 | -49.57539 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccbd3140-5fc0-3ace-99d1-a6503db5d148 | -8.29085 | -46.74516 | 2026-10-01 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 851cb2da-6285-3d6e-8fea-662111e6571b | -10.7703 | -54.7523 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09add0b1-4122-3ef3-a777-e7437daebe23 | -7.49492 | -55.00428 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2e3a6b1-8673-3885-9f69-ede1f840925b | -8.20775 | -45.47357 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b375dd1-8235-30a6-acc1-5c5c8aeaecfb | -5.85577 | -57.75778 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 325e0e9d-47a8-3dcc-b92c-daaafd65e1b3 | -11.74671 | -50.40128 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee31dad-bda8-3ce2-b931-05d7e359c89f | -6.10507 | -53.0938 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 821e09f7-e0c0-37eb-b958-0385049f6eb8 | -10.2055 | -49.96716 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5cfcd86-b055-3978-934a-648ff4e07064 | -8.21282 | -45.48539 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e74b8d8-58e9-30be-9d81-a13d13091f13 | -8.47336 | -44.88405 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c09cd275-0da8-3227-977c-54137544c997 | -11.19981 | -45.20553 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad06e1a9-f26d-37d7-8232-716d9053a96d | -11.95904 | -57.59705 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed45ccc-0f8d-3e10-8ce8-4ace5c266b00 | -9.95148 | -54.66904 | 2026-10-01 04:34:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea710556-31f5-36a4-abd0-7de38e793f7f | -9.06842 | -49.87187 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c811cb14-99ec-35b5-97bb-b3879c48c448 | -11.19461 | -45.19282 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 686fccfc-23e7-3f5e-bb5d-5cd245781671 | -12.70506 | -54.06737 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff9ed6a-0e29-3682-9855-f0d9b769ada1 | -11.45611 | -43.44965 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 925b8458-163a-3c3f-85f8-86b0ce270e43 | -7.84931 | -45.81593 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf988550-6f51-334b-94be-0e10c9002860 | -9.78547 | -44.81101 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 425d8090-a448-39d0-98b5-4e4b169b76d6 | -7.49543 | -55.00139 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9794f5ae-3900-304e-a961-5a09de63fbc0 | -13.38531 | -44.01915 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3031d337-b41a-333b-915b-27b51eb1fd9d | -7.34055 | -55.59864 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6510a15d-fe62-364d-b4fa-3d179678a194 | -13.88324 | -44.45425 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03389824-88c6-31cd-aa56-fd0298d37054 | -11.61438 | -43.55516 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9512f11e-d500-3625-9ed2-a4c36ab3b30a | -12.19036 | -48.43349 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3b979a7b-caa9-31fe-befe-bdc9e602ae24 | -8.33657 | -44.15998 | 2026-10-01 04:34:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7235da99-8cf8-3b40-84e6-2e0e57367552 | -7.69611 | -55.0598 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19cbf079-dc46-3eca-9ae9-f780f0f04e9b | -13.37349 | -43.99331 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae96f226-6cd1-3f29-aa48-775ab5d38c05 | -8.20332 | -45.5022 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 329e0443-68be-3167-b995-4cf0b0d3f18a | -9.07423 | -47.15936 | 2026-10-01 04:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22d0f962-1f0c-35b7-9dbf-15001afe9a8b | -7.70309 | -54.79273 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f2e6dbc-5d62-3dd8-8c10-b5727a4338a4 | -5.85461 | -57.75944 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a026390-24e2-3f50-9a7d-0083ac769d43 | -8.96207 | -44.18208 | 2026-10-01 04:34:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1446c665-a81c-3155-b82a-4f38407e710a | -11.1692 | -45.12469 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c6660fee-601b-32b7-86ec-3f13a1ab5bd9 | -8.96685 | -44.1745 | 2026-10-01 04:34:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c820b528-e9ef-3151-baa4-28ab97629851 | -7.49253 | -54.98867 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51f11573-9ab1-3543-8350-d9f1e4a5559f | -8.04209 | -42.863 | 2026-10-01 04:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 538f6ac9-90c8-3d9b-b274-d3ad5d69fc20 | -13.38081 | -46.81642 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cde0bcbd-6d8f-3fff-81dd-a1390cc8245a | -11.22708 | -45.18994 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d940195d-0ccf-353a-83af-fb0c86d8aae3 | -11.8341 | -50.50717 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f674f247-c82b-32de-b5b8-baefbb4f1214 | -6.13197 | -53.26973 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfc4414f-5acd-3a1f-9d07-cc8315007092 | -10.5516 | -50.04335 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18b471d0-cb00-349f-b25f-95dfad729b00 | -10.53668 | -57.77441 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5ac7eab-187d-3bc5-aedd-3f132aa84e85 | -11.16979 | -45.12075 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48734300-1db4-3436-b1c1-92f1c7ffab0a | -8.32228 | -46.76085 | 2026-10-01 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19d75495-c525-303c-b749-d2500fdb8fa1 | -14.14641 | -46.23781 | 2026-10-01 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e0a3cae-3b10-3b7c-8615-ff25b5ed400f | -13.38193 | -46.83167 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1ca4ed7-ba01-3aa7-9716-905b7bc20788 | -6.32862 | -51.1209 | 2026-10-01 04:34:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd650a7d-65ba-3f96-8e1a-7ebc9c4f208b | -11.20748 | -45.15478 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a46a28a-c19b-3686-8fa0-01cb4ee2f354 | -12.72846 | -47.00239 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff8f829c-132a-39a7-b3e3-bf0fab32f5fe | -8.47623 | -44.88831 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 558546d0-cc0d-3f91-840b-9bb3863a123b | -8.01475 | -42.89183 | 2026-10-01 04:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d240d72f-cb5a-3f84-a5d5-f9778f38c9a2 | -8.84798 | -50.50575 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7b8f6fa-b7c5-3c92-945d-22ee96e66dba | -7.54604 | -55.03681 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 625dc0ab-a3d4-31e0-891c-f9a5f83eb986 | -7.54984 | -55.04225 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bb9966e-f160-3644-88b2-4ccc68bf786a | -8.2005 | -45.49816 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6d98486-1873-369a-8b47-82432936ba4d | -10.70152 | -45.30503 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8be2896c-ad8a-3a5f-8ee3-d5005a8aecd8 | -13.8863 | -44.45932 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55e79cc2-0375-32e6-8e73-445328a69c93 | -12.96289 | -51.10427 | 2026-10-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f6cce7a-b6de-3998-a3d5-bd884b8da3c1 | -13.54061 | -49.16536 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6502f12c-2d05-3bf0-a2f5-87f3669c06b1 | -13.73791 | -48.97258 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31b55337-1283-3cb3-b73b-a7e179c21874 | -9.75322 | -44.82681 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17eef7f7-0671-3822-9ee5-3c37f41481b2 | -8.04798 | -45.47075 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 058dd51b-28bf-363d-80bc-96a3f6b90a91 | -13.38641 | -46.82482 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3525174-76ab-33af-9028-ca60edf19620 | -12.35707 | -46.38163 | 2026-10-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d2c753c-5e1f-3d57-8f78-9523c225a563 | -11.31413 | -41.17933 | 2026-10-01 04:34:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c19efd5-06a2-31ca-9b27-a1f0b0617cdb | -10.54079 | -57.78368 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63bcde5d-cc33-335a-bcf5-5cd3ee0bbaff | -7.54655 | -55.03387 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924c8674-d6be-3528-a40d-c782d8f1d06f | -11.25936 | -54.81839 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64623f8e-fb31-3d37-89e9-ea55b0595365 | -14.35922 | -44.77476 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cc48f19-7142-3307-8470-58b7533fde7f | -7.84653 | -45.81187 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0492261b-1ce0-35a8-971a-b43dd77f079d | -11.18898 | -45.11175 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8716935c-ed87-3d05-86a5-0120d6b071e9 | -12.08922 | -50.69682 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d27b6aea-4f7a-344e-8f2e-2e6d7df355b3 | -11.79336 | -50.51347 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a6ce30fd-a395-3692-acb0-389df91be75e | -7.51139 | -44.5403 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README62.md)
