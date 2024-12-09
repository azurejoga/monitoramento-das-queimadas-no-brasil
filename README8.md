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
| fb049b78-2abc-3a80-a905-fc1c2ead74ca | -4.08804 | -46.72664 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3475cddf-ea8d-38b9-9dd7-8825702e1e6b | -4.07792 | -46.72162 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfc4c436-5acf-35bc-89d9-08229c610399 | -4.54374 | -48.01465 | 2024-12-09 04:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7deebc9-e82d-3a22-90b1-91843f73d0e3 | -2.46804 | -47.96964 | 2024-12-09 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80e0be36-0b3c-34a7-98e4-0f53dc407abb | -2.90519 | -48.0242 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddd00586-fcb2-3361-b995-55f51f443545 | -4.08624 | -46.71475 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 672db7b4-6ff0-3c02-9b01-fbfdd0c87947 | -4.08969 | -46.69433 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a80dba84-e5f7-3f8a-a236-ce882a2e5b92 | -2.77051 | -48.3561 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37b641b7-7650-35a5-8fd4-e4ac765c5e5e | -4.05548 | -46.88636 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a838100c-6604-3fad-88c4-804503b4ea1c | -4.54299 | -48.0192 | 2024-12-09 04:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec913e4d-4b6d-3771-82a2-8537077576a3 | -5.18492 | -43.92673 | 2024-12-09 04:16:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a56a0e4-dbf7-3d1e-bde3-cde7fb723391 | -4.08687 | -46.71078 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 557c4d4a-98e0-367d-b596-ddc6819785f3 | -4.06062 | -46.89462 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c4033c0-0f72-3885-9c1e-b66ea2addafd | -4.06258 | -46.88763 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65ff4a2-dc34-3186-afe9-95ddd1f1f9df | -4.06196 | -46.89158 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 907971a7-e46a-3b32-89b4-35b7fc4495bf | -4.07151 | -46.80566 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0143e35-cf1f-35e7-a1fa-ba28cc1fb1c2 | -4.81888 | -44.35328 | 2024-12-09 04:16:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b02fbcbf-ccf1-3a2d-a8c2-b61b1834bd13 | -4.01921 | -46.97654 | 2024-12-09 04:16:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3319ec2e-326a-3ec6-a8f2-b22ab458cde4 | -4.07211 | -46.71259 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c115cef-f20f-3be7-862f-afa466e366c0 | -4.06191 | -46.88671 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc85b542-57d2-3536-8ca8-b7cbfd300c02 | -4.05862 | -46.70632 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f554480-6362-35a4-b03c-f72fd484a12b | -2.9005 | -40.44118 | 2024-12-09 04:16:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df3ae849-ffdb-3305-9899-5bfc634e17de | -1.9693 | -48.43805 | 2024-12-09 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ac0dd1-f3dd-32a0-89ae-d9f311ea0e0b | -4.07176 | -46.80643 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5d4c331-e979-32f1-b106-066238bb3415 | -1.64695 | -45.91124 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cc47873-2e5d-39b5-b07d-e9a7186b5ac1 | -3.85807 | -40.44254 | 2024-12-09 04:16:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d19e968-1f26-322c-821e-c2ad256faf99 | -4.09228 | -46.69946 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54d0d6de-88d3-37aa-8d20-e575ddfe5b42 | -4.09257 | -46.69886 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e877ffab-94c4-3f4f-9a3b-59ff65a9146b | -4.08646 | -46.71413 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60393519-baba-324d-919e-ae918f87c83c | -4.08397 | -46.70625 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e511335-e85d-3ca4-96c2-695388456d78 | -4.08271 | -46.7142 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5281b685-c225-341b-afbb-343cbf973bb0 | -2.63284 | -48.06289 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 536abf0c-b6de-3f58-84db-ba2a1642c07e | -3.81432 | -52.35819 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a52a5162-05c1-3d03-8d53-234066ecc48d | -3.81299 | -52.35662 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf5f982a-9196-35ff-8097-adc2cb6e1b46 | -2.62201 | -48.05621 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77b5566d-674f-3e1e-9a28-0515fc4bd5dd | -4.07918 | -46.71366 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8782097d-259d-31d1-8e1d-6a512eb8c805 | -1.6105 | -52.63667 | 2024-12-09 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 172cf72a-d1b3-3af2-a419-eb1ef0807418 | -4.08517 | -46.72207 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d8ea517-4fed-3e7b-9b3b-15bbb81a522d | -4.08896 | -46.6747 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75aac20b-637a-337f-9ae6-c05c6480504e | -4.60918 | -46.2835 | 2024-12-09 04:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73e7a99-05e0-3311-85b4-ee5ce5fa7fdd | -4.08145 | -46.72216 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dbb370b-68c5-31f3-b3ca-2e3cd4a565eb | -5.18384 | -43.93364 | 2024-12-09 04:16:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99b09a9f-cc20-3294-97bb-fdaf7caaaabb | -4.61201 | -46.28784 | 2024-12-09 04:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87ab7e46-ad40-39b7-8662-f0117821c5cb | -4.08789 | -46.72729 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e15ba63-de11-3860-9857-fe416b0610a2 | -1.96772 | -48.43789 | 2024-12-09 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40819dbd-5234-36e2-b07e-cddc33039449 | -2.90982 | -48.02006 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb1cac53-1f3c-378b-96fa-6d8279aa1154 | -2.86568 | -46.71861 | 2024-12-09 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d238119a-fff8-3075-b2cc-69c7a5352702 | -3.1413 | -45.59606 | 2024-12-09 04:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ffcec6-8fb2-3856-87a4-b2008d9a099b | -1.77554 | -46.49097 | 2024-12-09 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a8c53e-6cfd-3765-b020-be3b8a026122 | -1.47913 | -46.146 | 2024-12-09 04:16:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b17d9d8f-a152-35a5-8b23-a80c4ecac3fb | -3.81379 | -52.36142 | 2024-12-09 04:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66e2090c-8db8-33b9-8391-c20d651f9790 | -3.35777 | -45.51381 | 2024-12-09 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92ba05ec-f937-3157-b913-c78742f490b3 | -4.08503 | -46.65388 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89a1e96e-70e6-3aa7-851d-9ab93d02b0c8 | -3.26737 | -45.37735 | 2024-12-09 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f58945a7-730d-392f-8d39-4869fda54f3b | -4.09193 | -46.7028 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5c7abd4-dc72-3534-9aa9-bfe670ffe091 | -1.64757 | -45.90738 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14e914d-18a1-322e-9477-a409d08f6ec6 | -4.06483 | -46.89126 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea40a3ea-2110-381b-bdca-2401940ab060 | -2.14554 | -48.04358 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f9bf147-6e46-3c8b-a0a8-725ce313baef | -4.05772 | -46.89006 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fc5f967-5b3d-3a1b-8df2-7bd9abdfa19d | -2.46682 | -47.96731 | 2024-12-09 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccf2f392-4bd1-32a6-ad71-1cef56c9a7f2 | -2.9106 | -48.01528 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea7aa0c4-8747-3f01-b44a-c247da946bcd | -2.90828 | -48.01767 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 317f8721-a3b2-3c2c-a774-e876885b062e | -2.99613 | -40.28456 | 2024-12-09 04:16:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f43e36a-e8b6-3dc1-bc81-776ece1f74bf | -4.54675 | -48.01979 | 2024-12-09 04:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8c6fd0c6-3488-3d58-9fcf-e0da5e123b55 | -4.81833 | -44.35673 | 2024-12-09 04:16:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e95b813-098e-31c7-8c54-769ddc02b0df | -4.08208 | -46.71817 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac9cb289-da33-35fe-9fed-bc639d858db0 | -4.09125 | -46.68309 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37fff7e9-b04f-31d7-89d0-bae22f028a91 | -1.77987 | -45.91551 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec68f3e-1ce2-346e-acf5-a088a76d4d08 | -4.0875 | -46.70681 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f941689d-cc26-3490-a1cb-804180f4df19 | -2.1507 | -48.04111 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 47cee462-0612-3a44-8a28-e6d45f5a20ae | -3.42658 | -42.9883 | 2024-12-09 04:16:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10166ff0-da04-38e6-a3be-2febb0501774 | -2.03474 | -46.66781 | 2024-12-09 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4584e6fa-b213-33ca-8f65-0b958877a59b | -3.00965 | -48.12228 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f4bc77f-a110-3f58-9336-bc69ccae294f | -2.56012 | -47.59672 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 725e71bd-aeea-3bc3-8491-7a1c131aa00a | -2.46882 | -47.96484 | 2024-12-09 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b772f73-a8c6-30a1-b9f0-3547f4880153 | -4.07505 | -46.80628 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c41fdb-142f-32a8-b9e6-a92012ca59d1 | -2.90369 | -48.02182 | 2024-12-09 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 160ff5f4-e350-332f-9ffa-862e4d8a1e9a | -3.26176 | -45.36907 | 2024-12-09 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18541f2d-2324-3cdd-b971-55ebc3d7faea | -4.07239 | -46.80242 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b81e7931-7b98-37e2-8b99-a0acfe76ed3d | -4.05836 | -46.88609 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f52d3fd3-d0e6-3539-a14b-9fabb42b25c5 | -2.47035 | -47.08736 | 2024-12-09 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 245a80f7-03a2-35fc-a726-5b20a4d9ab64 | -2.03271 | -46.66614 | 2024-12-09 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85786118-c72d-3c66-82cd-ffbefc7f80ae | -3.26399 | -45.37682 | 2024-12-09 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 787ebca3-fe8c-3109-a49a-ac7bc3f3516c | -2.14601 | -48.04536 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 44811c8f-c86e-32a1-b986-7653ec1a9fd7 | -1.45597 | -46.08666 | 2024-12-09 04:16:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f367823-c4d4-3fa6-93ff-130f0c56d508 | -1.64572 | -45.91896 | 2024-12-09 04:16:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7b6ed79-5e96-33db-b7c1-1a34529c6f71 | -3.42712 | -42.9848 | 2024-12-09 04:16:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ffac06e-d828-3c89-bb3e-d05c16577038 | -4.08582 | -46.71809 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70920de6-bec1-3b66-a42d-c85cfa24a3e9 | -4.13076 | -46.34278 | 2024-12-09 04:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6bfdb2b-e3d4-3229-89ef-5bceddaaf642 | -4.08776 | -46.7062 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e998abce-ee31-3630-9f85-267a23c30d3f | -3.35719 | -45.51744 | 2024-12-09 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c8c7a5-3d68-3e47-9de0-0620a25bc8e7 | -4.08044 | -46.70569 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a47e0fce-eb7e-380f-8394-69cdab470fe7 | -3.26456 | -45.37321 | 2024-12-09 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0588912b-e9e6-32e6-b45a-5aa578625a4a | -2.1463 | -48.0387 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 376ec02b-9d4a-349b-9cff-dd66a7de8eca | -4.06133 | -46.89554 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5e37697-4bdb-3b57-85b9-1833c618ff78 | -2.38069 | -48.62558 | 2024-12-09 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d0e2f6e-bb7e-3baf-a7cf-b9a346969836 | -3.96559 | -46.96769 | 2024-12-09 04:16:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1be097f-e977-3702-87a8-767e6ac0527e | -2.14681 | -48.04049 | 2024-12-09 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 60175002-918e-319e-8ce7-faed7309aa7d | -2.04817 | -46.639 | 2024-12-09 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29e7f797-bdbe-341e-9548-c6be104df325 | -4.0753 | -46.80706 | 2024-12-09 04:16:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
