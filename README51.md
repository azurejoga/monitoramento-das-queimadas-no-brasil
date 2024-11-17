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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3eaade2-9da4-3696-987d-f58aed02ad2b | -2.81941 | -46.66133 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b0f0e011-2ab1-3762-a41e-ff83a0191a5c | -3.89493 | -45.91251 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a19ec6a5-2be5-3953-89dc-a1aa4564d084 | -3.13348 | -45.8936 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb2c2208-08b7-311d-9fd8-5067d33bb15a | -2.66867 | -46.21336 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 94eefdbe-419c-3a3d-a1e6-d48acb7e0575 | -2.49795 | -46.39231 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a6d3018-5d16-302a-a167-7b2752479c19 | -2.39131 | -46.18398 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cc8126a-b61e-3323-9f8c-fd9d7e9229d6 | -4.32317 | -49.3863 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f49032fa-2d3e-341e-9b52-b593fa81c2ad | -4.11217 | -46.93089 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5a6b2a0-5a64-3a24-a4cf-9869b29dcaf5 | -2.64192 | -46.83808 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bddc5cde-183a-319a-be95-37548b02d413 | -4.21361 | -50.69614 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02a7a09-5542-30e1-98e2-4258a081ca46 | -2.53144 | -46.3303 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70d8454-3a36-3357-bcbe-e07c52053e16 | -2.34081 | -48.59763 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51ccde81-513b-35d7-854f-642d48486ceb | -2.95644 | -45.80472 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 142e1f11-8ae2-385c-a1e5-ef30fcff49d4 | -3.20911 | -46.47129 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1049379-f9df-3b97-b10b-3f3390fa0699 | -2.67694 | -46.20395 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cbb405d-bb3d-3899-9fc4-e69c2909e7a6 | -3.81229 | -50.95576 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98cc084e-f85b-3e28-b5ae-1b99bfeea3bc | -2.27343 | -46.58997 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d69b20f-6c7b-3df6-a2de-902af18f32f4 | -2.15751 | -50.70509 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86f35489-1877-377e-9176-4f27e0e6f234 | -2.68358 | -46.20498 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68cf27e8-c5fd-3c2d-b598-dc2afa1ca084 | -1.01621 | -52.27761 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27e6abe5-39f5-3bc9-8424-a1ee93c85ef2 | -4.25274 | -48.53553 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f721f1e3-faab-3db8-80c5-a6cd9d7e9457 | -3.16097 | -46.60546 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ba80877-ea96-3fbc-a5bd-a4c1412bd88b | -2.62515 | -46.25254 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25b8c7f3-af98-3569-8c6e-1ab1c39002d4 | -2.18023 | -48.74843 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 711c0b95-42bd-3072-a657-5e4c029a395a | -3.03873 | -47.98539 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3204ade7-2411-3cfe-9247-d374f720efa3 | -3.78499 | -46.04472 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaeebb9f-8af0-3609-8b59-d469bb7859ea | -3.82317 | -50.23416 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46eb1d9d-6e86-3a90-a4b4-0c479a018139 | -3.3447 | -46.32188 | 2024-11-17 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8befa19-242b-321b-a4f4-68b5ac7448ab | -3.56104 | -50.26143 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fea9dc9b-c9c5-38e7-bff0-4e4a5490b58b | -2.41592 | -47.79837 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06140505-911c-30d6-ad97-a722a394bfe5 | -2.08263 | -48.6134 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9877684-9692-3b1e-9366-304253cf1f2d | -2.82494 | -46.66924 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eab350e0-2fb6-349e-a5ba-ead0f3383091 | -2.66528 | -46.19147 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 419c8340-4eed-3b61-8252-726cd7dbb288 | -2.9908 | -52.60918 | 2024-11-17 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7db2020-be30-3d45-92d5-4f407d2f0370 | -4.23129 | -48.02956 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29864226-7cfa-37c2-b349-d0d17af51009 | -1.23054 | -51.78716 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0839e6a4-9751-3cb4-8441-aa50cda796e1 | -3.51984 | -50.51569 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6712b563-baed-3626-8b63-c4aa79b12a96 | -3.94738 | -46.70323 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a822d29-389e-3d70-8a77-5d61a835076c | -4.66296 | -49.51895 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45537f02-5600-38b5-8f60-64f716239d09 | -2.85301 | -46.66302 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e12c5e7-ebc5-32c5-9a8a-2a6796860888 | -1.36848 | -51.10971 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 780ec669-a73c-3da1-93f2-f1de3971e42b | -4.33246 | -48.61713 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1570e6f7-3e56-34f2-8111-721483a1a198 | -4.28512 | -48.20551 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec31ad9-4e09-3e98-a172-dbe70e84683d | -2.12009 | -48.21318 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adfb85a0-f72d-34df-a5f6-07d502616d6d | -3.78314 | -50.39203 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fd18d6d-2db0-3550-81b6-2923b0f8e382 | -4.03507 | -45.46676 | 2024-11-17 04:29:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd2941c4-f374-3a72-9fa1-b9ebed7f597e | -3.94298 | -46.70965 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8486990e-2798-3b96-98b0-553628ac9ad1 | -2.36929 | -47.94475 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10658e57-9348-366b-9508-dfaa13e231db | -3.25068 | -46.5309 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f947043f-bb9e-3a7f-a444-54625f8b6f62 | -0.92996 | -51.73935 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fccedec-3d1b-3d41-b6d5-5c087c322fad | -1.90921 | -48.66598 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 099c4d15-f979-3559-b646-c9ed21619ae6 | -2.65646 | -46.20435 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37af07b5-1b6f-34c9-a4f5-137348d19b59 | -3.52208 | -50.23932 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e34df1e0-e6b8-3a2d-8249-c8d00e554281 | -2.15307 | -50.70897 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81b9dcb8-04a5-374e-b558-6d9812006e78 | -2.80558 | -52.92066 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bba8ba3b-5d1a-3731-a1c5-d0090ed00891 | -0.89667 | -51.94622 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5fa7085-ccc1-3b85-b306-6cdcaebe03a9 | -2.07353 | -46.47803 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23b5bbef-b166-3ff9-b0a8-45c301457bd7 | -2.10057 | -50.37132 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eef224fe-b758-3171-b7b0-3546afce2022 | -2.60873 | -48.21294 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8985bcf1-1b11-329e-a585-7fb08f745d68 | -4.10813 | -46.87018 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62bb5b2a-e753-3aee-9856-e4644a229307 | -4.36787 | -48.09048 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d154e49-cf84-3dba-88d5-da4383e121c5 | -2.66744 | -46.17756 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 875cf19d-097a-37e3-aae9-65fdc7f1c8a0 | -4.23208 | -50.67605 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7672d9c-c334-32e0-ae84-3bff09b5693e | -2.64216 | -46.55638 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44463cd6-d0e6-3fd7-967a-d60287b265cd | -3.80156 | -46.50677 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1f5b43d-705c-3875-9a82-342b8644c721 | -5.39938 | -42.77129 | 2024-11-17 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7eee433d-82b6-328b-a0cf-b82366f603b4 | -3.36185 | -46.08093 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96296614-e5dc-3b8e-9c76-e0907acabd2f | -1.98285 | -48.71041 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c315f031-f690-3437-b867-ab2b21d4357e | -5.34551 | -46.07837 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549c56df-54f7-394d-9584-4373f80c02d8 | -0.80658 | -51.48952 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12361107-7d5a-336d-8557-797286605b02 | -2.35196 | -45.69796 | 2024-11-17 04:29:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d4034a4a-885a-3a99-b4a3-3606131ed8e8 | -2.6747 | -46.19648 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 081470f3-afbb-3472-9640-014764eb5792 | -3.66145 | -50.1147 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22661f25-a587-3c99-835a-98f58d846415 | -4.1495 | -50.76896 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7987b1d-f398-3ae4-806c-36412a996fba | -2.36326 | -46.4276 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64412297-e462-3442-a3db-ff40c8016aa1 | -2.59849 | -47.56747 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91bf5b3-3101-33af-a464-a4c0fdae9ae7 | -3.4329 | -53.32912 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f072db66-be7c-34cf-9874-13c039c4708a | -4.35525 | -45.86885 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31b0eac6-6ed4-3ff5-9276-0682132e32ee | -1.20679 | -51.77964 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05b8213e-fa57-37d5-98f7-34b27375a71e | -0.15712 | -51.59344 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392732e8-20f7-3043-bf2d-96a14db90862 | -2.07569 | -48.47457 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870dc75a-a859-38ac-a431-2d194c518dbe | -2.08368 | -48.2696 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96531166-8caf-34d5-a3e0-46828420636d | -4.11827 | -46.76199 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a61267b6-9b5e-377c-9501-fa16bdebc820 | -3.46773 | -43.88844 | 2024-11-17 04:29:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f302975-512d-3592-8f35-531e06e6f7fc | -2.16622 | -48.32664 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e50a843d-82ee-356c-9a7b-fded46da6ca9 | -1.29103 | -51.9593 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fc35bce2-4c4a-318b-bea2-1215032db41c | -2.85632 | -46.66354 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 287a2e6b-dcb5-3883-af82-c9325f6d68e8 | -2.27548 | -47.91578 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d01b38b0-ba44-3dbb-997c-0a9f3c647e15 | -2.6808 | -46.20099 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d32c9562-ad1c-3fbc-87ce-3f64e0dadf85 | -2.70943 | -47.72641 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3cfa079-dfe4-3ebf-9497-dd89a6e03271 | -2.25655 | -48.33324 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27e32d67-f6c6-3bf4-9ae1-04c1393401a8 | -3.42121 | -41.02866 | 2024-11-17 04:29:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 955f30aa-d4e4-3cf2-a4c1-37cb44f1c694 | -2.22809 | -46.83312 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dd045a3-7117-3dd3-b139-d707ba739435 | -2.67353 | -46.81143 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5c5d332-05ee-3b38-958d-a04a6f6b2a66 | -3.71416 | -51.83941 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3a501d5-b5a6-3b8c-bcdc-034b2ff7123b | -3.87988 | -49.94707 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fb29b15-c712-3e9f-8642-eb65c667ce38 | -4.12708 | -46.94382 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a62ef556-9978-3e13-a942-3eb5d88bd6ae | -3.5322 | -50.24508 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a40545-6231-3c69-99dd-2d3810cc6d73 | -4.2818 | -48.20498 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a508fd9-b5de-3b6b-8d70-4d0f6ee29554 | -2.66535 | -46.21284 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README52.md)
