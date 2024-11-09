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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c75c96c9-bcef-3873-93d9-0cb0359c1a8c | -3.28706 | -49.61818 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84a752af-1099-36e3-a551-7e56965b30e2 | -5.20729 | -46.1116 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a29412e4-af27-331c-b005-6bcdea814788 | -3.75937 | -51.02086 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 863b5f0f-a340-3c18-b233-26cb33f4c410 | -5.55275 | -44.69546 | 2024-11-09 04:33:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 200bed60-e71e-37fd-9ab4-9c21100e6f5a | -8.69355 | -47.95747 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2558e80f-1bbc-36ee-946b-9ab0a565bdf4 | -3.04558 | -53.27506 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a64161b3-c356-3854-90a3-abcd7ceddd01 | -4.06878 | -46.07076 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10edf069-48df-3399-8e95-686afbb70841 | -4.73451 | -48.99272 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0a015ef-ace0-3618-951d-77e46d321b31 | -4.87511 | -45.78158 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5863c454-e457-32ad-b5ea-55d89e2d3a78 | -3.09323 | -53.32317 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0716b59e-b769-35e7-8061-0988560e44c0 | -2.92391 | -49.35679 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e883d5d-7bef-3004-bf78-b3aa65cf8076 | -2.87371 | -50.32674 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5a7c350-ec13-3a13-acc8-8354d8577bdd | -5.25728 | -45.45833 | 2024-11-09 04:33:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adc564e2-f2ff-3543-a079-2f5e0b5cdd49 | -2.84939 | -51.36518 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b45c6065-03e4-305e-a988-25405612c7bf | -3.01456 | -51.03752 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5a201b2-0e79-3e31-81a9-e91099b74edf | -4.75089 | -48.91119 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6629ac23-8d10-3312-b39a-0bd2adb146c1 | -2.847 | -49.44527 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d90eb88-bbc6-3636-9d4c-86d3c17a0d77 | -2.62433 | -51.91327 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f29992ef-0297-3c0c-8ef1-b81a682c936a | -4.17405 | -46.59656 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed20a7e-fff9-338f-ac2e-3d1249876aca | -3.07936 | -50.56229 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2fc9ffe2-1a2f-33fc-8c38-0e490770faea | -3.23232 | -50.4477 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21c47510-c084-3a62-80cf-33e7d5d68a94 | -4.08299 | -49.28802 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7195a728-c5b0-3cbb-87f2-5f942579edf7 | -3.81662 | -50.78239 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4dbb697b-ef9f-34ac-90fd-03b16027631f | -2.98395 | -51.03734 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bee2b3bf-0c10-3f26-9f23-5799902c779f | -3.76443 | -51.75732 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b9df665d-dc09-3a89-9e5c-926fada91890 | -3.87649 | -48.32958 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 090b58ce-9afe-3826-b3ce-82aa5fe0a571 | -4.80515 | -44.7784 | 2024-11-09 04:33:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4ba69287-1b73-3c6b-b74a-4c937698668f | -4.12023 | -47.09558 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f069785-50dd-3101-95a3-fdd8338d30f0 | -4.89808 | -48.64801 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 711e6f83-2d04-3840-8281-05c72d97f541 | -2.81773 | -52.9608 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ec58dcc-8586-3fb3-b9fc-72941ea4ccda | -2.8444 | -49.39452 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8809f92-9a75-393d-87c6-dc2e97b2dc56 | -4.08226 | -48.31915 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b65be3e8-b3cc-3455-aa21-82f172354e95 | -3.96124 | -48.99691 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46061719-aff7-3570-b26e-35fdda24d354 | -2.87962 | -49.37284 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e645c663-d471-3e77-90a1-ace26746332b | -4.44312 | -43.64722 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e560bcf2-c3e8-3bab-a21a-cdeb6c247a26 | -3.2901 | -51.5232 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8388d88a-a470-3879-a6ec-578e6902979b | -3.02837 | -50.36229 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57754a95-cd6d-3d3d-82da-13bd037a489b | -4.34724 | -48.62297 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebcb9192-3b8a-3d67-9d69-8f186e352a33 | -3.63295 | -50.18619 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1f5155b-b86d-324d-80da-034e365649d3 | -2.89274 | -49.40195 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64069538-c6cd-323f-9a41-c9aa8f901e61 | -2.80333 | -52.94255 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83cda093-3bc4-31d3-b112-54085ef3b8f0 | -2.58352 | -51.92041 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c025107-c9b6-3dcb-a2f6-a3dfd08979e4 | -3.23764 | -50.27574 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5b941e9-8856-3f37-9f2a-53423882c253 | -3.24518 | -46.46691 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 780e8bea-3b78-36e2-bbe7-ca2068fac7fa | -5.8141 | -44.12347 | 2024-11-09 04:33:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 54273f38-6e84-3a42-a55c-34634978aeed | -3.95085 | -48.15913 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8436608a-be26-3fa9-ad4c-8bd7114d0d50 | -3.45046 | -50.37444 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb648cb0-3887-3f20-8ea9-fdc41deca9b5 | -3.75354 | -52.09879 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a996e5d-e155-318c-aaa5-22c07645452d | -3.9758 | -48.17377 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3e2b391-03e8-3eeb-aab4-d17b30420c4f | -3.02702 | -51.00743 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4882c384-7132-33cd-a885-ace8f2f3a2ba | -5.46995 | -43.64763 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d4fedc09-8b9b-37e5-9277-a396c6f6bf03 | -2.18953 | -53.63744 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff446ac8-c198-39aa-9ca4-4279f96b69ba | -2.73282 | -51.71423 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d4abf75-bd3c-38fb-a20c-00420d295006 | -3.96285 | -46.467 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb88f515-95f1-3600-b5dd-d41569714a58 | -4.38266 | -47.24616 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72fa90f7-2147-3463-bde4-ed3f1abbd122 | -4.353 | -46.82412 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a80e6db-0b8b-3c3f-be67-8da9243f5877 | -2.93908 | -49.5064 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e98a4d11-c012-31fb-a6ec-e9e5859540c2 | -2.83227 | -49.49366 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab63f809-ab77-3b4d-b321-d0bbef546ee1 | -4.08914 | -48.51387 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 749b6410-840d-3c94-b4a2-2acac46a6ac7 | -3.18722 | -50.59083 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47204444-6481-3224-abce-776e48b2cbb5 | -3.10185 | -53.32464 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb79efa1-d0ff-3138-8938-bdfedf409755 | -3.01751 | -47.94857 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b81fe24-0d7a-33c9-af65-ada032aedf3a | -7.32782 | -49.95455 | 2024-11-09 04:33:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ca47b92-60ba-3043-ab51-ebf6644f3751 | -3.083 | -50.56287 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 7ec17dca-83a6-3624-8b04-d2242baae071 | -6.18183 | -45.44398 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ca060eba-5d15-33ae-99d8-6bdaeaa8517d | -3.79258 | -51.29078 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1922050d-2f96-3649-be95-6a7a1d67cc96 | -3.84826 | -50.04011 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e3a18cc-edd0-3721-b3f6-1d654df4b07c | -3.10118 | -53.32882 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 74a18cbc-7b21-321f-bfb9-c6c49b0a08c1 | -4.66988 | -44.34022 | 2024-11-09 04:33:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e0b3180b-976f-31be-9059-dc7d8ae1663f | -3.96304 | -48.16812 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4811a576-899e-3a91-bf1c-55dc6be4b570 | -3.9785 | -48.13507 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b8ce8af-0978-3076-8e96-b789c4770efc | -2.69375 | -51.70816 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8efe976f-ad88-3218-b93e-6f79c7ae297e | -3.11749 | -48.63752 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3eb6b3b8-60dc-31d6-84c9-3d3ad89505bb | -3.96291 | -48.12546 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cb8e875-4fb6-3386-a5ce-e0a933207392 | -3.02327 | -47.95661 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2baaff6c-56ff-304f-a854-b2cfbdf48bfc | -4.35354 | -46.82065 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcbfbffa-7c13-38cd-ac8c-86c14d0c08ac | -3.90052 | -50.30415 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 521db685-bbe4-3212-ac1c-69e827668258 | -4.6062 | -49.57753 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61dafea8-0a56-3ed1-9951-ac66e084e271 | -4.78065 | -48.68009 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdfb78cf-aa1a-391d-8fbe-f158c1dd221a | -3.97525 | -48.17724 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b3f79be9-3581-33b7-a1de-47a018a91659 | -4.20368 | -48.54255 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d26d935-60bf-3790-a97a-f2519e1a013e | -3.19253 | -48.65623 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a2de9e-397b-38b1-ada8-b11c9e432034 | -3.64881 | -50.13137 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64fc2f13-7310-3ede-a458-290dc99244c0 | -4.079 | -49.29116 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b134aa4e-1abd-3c50-8531-3254a6087d35 | -4.11336 | -46.90018 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c6f78b3-1d91-3bf0-b967-5bd98b0ce283 | -3.24572 | -46.46343 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 390967a6-1c22-3141-a52f-cbb624e4c460 | -4.20647 | -48.54657 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4c84476a-76fa-36cf-858f-7963cd1ffb86 | -3.02386 | -51.19658 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c9ab1d2-1c7b-33cd-936b-0b45568ee178 | -3.95851 | -48.13189 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7820c799-1323-3705-af39-342a0780ad8f | -3.52179 | -51.50655 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a475fe-550e-3844-945f-c20a3612f425 | -3.18699 | -54.31326 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fffbc7c2-0066-36ec-991e-a7e1b885113b | -3.96569 | -48.12943 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bee8386d-3412-385c-bc0a-db559bb4cc61 | -2.85151 | -51.7787 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e0ebf1-eb02-3602-aa68-62c6cb06d0c6 | -2.88121 | -51.31265 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 522c9f9f-5bb3-34e6-a252-a60e8a0cf318 | -3.74741 | -52.03621 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 220803a3-6b85-3afa-b89b-f9e152c3d5e4 | -2.94254 | -49.50695 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 412eceeb-7eca-3a25-9927-36a27c850d7c | -2.98212 | -49.57178 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be73ffc1-fc47-3e1d-8909-39a285cc4776 | -4.75246 | -48.42815 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 804371ad-71a5-3d92-b64e-67aba34c6c05 | -5.44528 | -43.26934 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3405ed11-d64a-3ad9-be03-721e1d68e5b1 | -2.35973 | -54.75594 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README53.md)
