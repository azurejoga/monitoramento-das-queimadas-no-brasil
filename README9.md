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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a68e4d27-3c79-3501-95b4-b09b1242f6f0 | -3.33701 | -44.38351 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8b9de7b6-3827-39f0-ab72-26d2bbc38fa0 | -9.33814 | -40.46756 | 2025-11-09 03:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a707ee4-407d-3d79-b01f-242677539b6c | -3.58873 | -41.65732 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 33fa8808-c3f8-3058-b8c5-b4001c3accbe | -6.22457 | -47.01835 | 2025-11-09 03:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b67bc27-2312-39b5-9787-1ad1f9db2093 | -7.56037 | -45.85814 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f48ed2be-a727-3aa1-88e7-0edb444a0814 | -7.56684 | -45.8824 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49e14cde-5cc6-3892-8183-5713cb4d099e | -8.84061 | -40.0752 | 2025-11-09 03:46:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c8cb780-126f-3c53-bc18-a6c2023a0e29 | -4.8067 | -38.69351 | 2025-11-09 03:46:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bc054393-f576-3e60-a98d-cda580c193eb | -3.33969 | -44.37826 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8da9f536-fbc7-3373-94ae-13386bb9c666 | -3.45379 | -45.6551 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3e7cd6e-8b38-3443-bd41-7f27c4aa0ff3 | -3.32541 | -44.36969 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fd0095ef-b5cd-35cd-bf92-71dfccd36ece | -3.42552 | -43.16783 | 2025-11-09 03:46:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f1f5ad1-3a38-3760-8975-5af63f6919e1 | -3.7704 | -44.28988 | 2025-11-09 03:46:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 316c08b7-1141-3f3d-a27b-1fc18c52394e | -2.92111 | -40.0063 | 2025-11-09 03:46:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 05540dee-6245-3588-af45-b7532cf63947 | -3.33509 | -44.37444 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a6d949b-6763-3175-b5be-7ea7b8be77f9 | -7.17532 | -44.95232 | 2025-11-09 03:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fb8f0f79-6b93-3922-a290-fe285fbbea35 | -3.59714 | -41.65871 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a3db9c17-5c9a-3eda-829b-ac4f7a5b9474 | -3.15242 | -44.57271 | 2025-11-09 03:46:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a87d081-45b1-3b20-aa74-2eb4c02a3b1b | -7.56159 | -45.8815 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08e55c33-7141-38a5-aa5b-d08192b6f6cd | -7.40129 | -40.07051 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 934359c2-74a4-3b70-b1e2-75400582ec95 | -9.39736 | -40.60339 | 2025-11-09 03:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f13dcb5a-1f37-37b8-bc10-3bf8572e2d1d | -3.76975 | -40.5138 | 2025-11-09 03:46:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 013a854e-96e6-39f5-b6ba-d8b63b3dde3c | -3.34066 | -44.37229 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 66f00310-3ec7-3d39-b824-dbdd31c2f9fa | -3.45453 | -45.65317 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03ad482c-99d8-32f3-820f-42b84c9cf9d5 | -2.60492 | -49.22915 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fe268aea-6558-3709-a6de-af5ce9ed0eed | -3.32591 | -44.36663 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81d8fab7-d7cf-34ea-b9a9-2506847f35df | -2.94521 | -49.35872 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| dba37d11-993d-3874-857f-b299b9161799 | -7.4092 | -40.06748 | 2025-11-09 03:46:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 654a142c-58fa-35b5-98e6-453f966ae4c7 | -9.41427 | -46.20233 | 2025-11-09 03:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 756ecd11-539c-3339-b1e5-0e0a28980f30 | -6.03098 | -46.55883 | 2025-11-09 03:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01096f47-03c2-3dc8-b6b4-0f15a8f16c6c | -2.7415 | -45.16754 | 2025-11-09 03:46:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8a81a6f-7570-3e02-8846-6b589f4fdc6c | -6.6873 | -46.66941 | 2025-11-09 03:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcabc734-6258-322d-ad7b-fb47771c7de1 | -3.33803 | -44.37756 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| feb3a504-d939-3a2e-9637-dbf23b84b1c5 | -8.01928 | -38.55037 | 2025-11-09 03:46:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4396cd3e-058f-3e3a-a3c7-e0f0fb29d7f0 | -8.99471 | -37.53501 | 2025-11-09 03:46:00 | NOAA-21 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 19b8ae58-a509-31d0-9516-3266f89a7087 | -2.94353 | -49.35838 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| dc3c7ac5-6dff-3233-8ee9-72102ee1f5ca | -3.44888 | -45.65059 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 03b19e85-c131-361e-b5fd-a529f5696943 | -7.49326 | -46.60783 | 2025-11-09 03:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de17b3a0-2e8b-3d51-a915-670877b6cf63 | -3.47468 | -39.57392 | 2025-11-09 03:46:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d8010b7d-fc12-3cd9-b740-fe526d73d565 | -2.99381 | -40.38049 | 2025-11-09 03:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 117dd9f5-6fe4-3c54-8a7c-2d7fd94941db | -9.09396 | -44.3226 | 2025-11-09 03:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be3c77f4-c0e3-3386-85cd-ae0f40ed598c | -2.97227 | -41.68318 | 2025-11-09 03:46:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 694e9c31-1b8f-36f2-b7f5-d9856bfa6049 | -4.76199 | -38.68254 | 2025-11-09 03:46:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e429b659-13b5-3ea4-82ec-1a7fb8f0ce75 | -3.33363 | -44.38338 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9ac825f8-b537-3ca5-968c-160a65aa496b | -3.33607 | -44.3684 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b182f219-34d1-315a-8088-075934d2b11b | -9.38062 | -47.07822 | 2025-11-09 03:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d88c0b7-320b-3248-b796-75ee283b88d1 | -3.48642 | -46.11198 | 2025-11-09 03:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5742d11a-2bb2-3ba3-a839-b76d75da0950 | -7.56218 | -45.8782 | 2025-11-09 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 928325d0-4a1a-31fd-a76f-585fc072938d | -2.55037 | -45.15586 | 2025-11-09 03:46:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9ea8e31-9073-3bfd-8afa-68c7df260d6c | -8.04389 | -39.68946 | 2025-11-09 03:46:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2651c72c-7b78-39a6-a590-28c45f74290f | -9.39805 | -40.59914 | 2025-11-09 03:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f529c723-e9d1-3926-a171-d0c03032a591 | -6.21877 | -47.01744 | 2025-11-09 03:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d3aabf1-7890-3c72-99b0-a38a410a55cc | -7.49879 | -46.60902 | 2025-11-09 03:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1394378-522a-360e-bec8-9925af97144c | -10.06163 | -38.55586 | 2025-11-09 03:46:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b9d99ea-a14e-3309-aecc-e188b32b793f | -3.26041 | -41.4296 | 2025-11-09 03:46:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 655fcab1-fe78-3daf-a675-69c431105cce | -8.82426 | -40.61925 | 2025-11-09 03:46:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 42d97a9a-29f0-3bd2-8459-898e9838a931 | -6.99996 | -42.79025 | 2025-11-09 03:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e8ca9e93-2562-3488-8fbb-1410a780600d | -3.51317 | -40.3554 | 2025-11-09 03:46:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7053921b-3851-3d5c-a564-db5d67a7c835 | -3.59358 | -41.65412 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 64568333-86d6-3717-9a7f-ddeeb01dde96 | -3.44839 | -45.65592 | 2025-11-09 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23e8d9f6-bad8-3204-936d-66e165a5996b | -3.34187 | -39.99703 | 2025-11-09 03:46:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0fe784a7-0c93-3cec-8f1d-a13ff3d97f3a | -2.96717 | -41.58112 | 2025-11-09 03:46:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c216547-e48f-33cf-9539-c72d8e73d0b7 | -9.41364 | -46.20109 | 2025-11-09 03:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea3fd9a5-e01a-3213-8bc9-5be08e06c3ea | -7.84743 | -38.43674 | 2025-11-09 03:46:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 735f992b-ffbd-384a-9782-535f013e625b | -2.94633 | -49.35204 | 2025-11-09 03:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| fa0eea75-2a6f-392f-8cc6-e5243eaf163f | -3.76538 | -44.28899 | 2025-11-09 03:46:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a996ca4-8713-30f0-9094-abfbca43104e | -3.87442 | -40.98574 | 2025-11-09 03:46:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6c3bd369-b9eb-3671-b0ff-d6ae00b38cf6 | -3.59778 | -41.65482 | 2025-11-09 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a5dcfa68-4b4f-3168-ac81-bcae5cae19ff | -3.54965 | -38.91211 | 2025-11-09 03:46:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e11a00bc-6e17-334a-a48c-b363c8c0eb2c | -3.3346 | -44.37742 | 2025-11-09 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 0c7b4db0-d18d-3e35-b8a1-5566bb4a457a | -6.19709 | -39.55319 | 2025-11-09 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38d24069-73f5-3651-99ef-2e9d34d85002 | -12.11123 | -43.64267 | 2025-11-09 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61a64af6-cff6-3d6e-beaa-bfd09c21a6b7 | -5.2063 | -44.41625 | 2025-11-09 03:49:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 369c90e7-4639-3326-8cd1-7b51f9ebb746 | -4.63285 | -46.39911 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc2478e7-6365-3a5a-8338-6cfba4ccad72 | -6.34114 | -36.08018 | 2025-11-09 03:49:00 | NOAA-21 | SÃO BENTO DO TRAIRÍ | RIO GRANDE DO NORTE | Brasil | 2411700 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da78084c-6a27-3579-8162-1d7b2cd49645 | -17.2861 | -41.93039 | 2025-11-09 03:49:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fdc33f08-d708-3647-8ddd-0886d1811c84 | -4.96293 | -44.94262 | 2025-11-09 03:49:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2ca08c19-4e76-3f22-b09f-831e9e8f9c10 | -4.39741 | -45.97341 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0757decb-3453-3b6b-994e-0253f6f7a4bc | -5.91829 | -42.70988 | 2025-11-09 03:49:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b585144c-ee7d-3c45-8057-5651d9e23de5 | -4.12436 | -47.28947 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fa516e61-467c-3cf7-8e96-20528a91cafb | -6.20273 | -39.73542 | 2025-11-09 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3fcdb0e4-a5a2-30d7-b2ec-16f72d113957 | -4.61674 | -49.65794 | 2025-11-09 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76101f1d-149f-37dc-a2ef-b6a730f1ec12 | -6.95477 | -40.25242 | 2025-11-09 03:49:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2823a006-4cca-3ed8-8224-eb480b0fb63e | -3.80424 | -46.00104 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22c47bf-9e5a-3209-b185-3815cf4251ce | -6.1758 | -44.38838 | 2025-11-09 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1515a2d6-a10a-31fb-83b9-fe8cd7bb469a | -14.41467 | -43.18883 | 2025-11-09 03:49:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f70fdd9-83dd-3436-8c2d-dbe1232721b0 | -5.27962 | -44.95494 | 2025-11-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0008d80d-70d2-3e59-a2d4-b63dd1a2fe1b | -4.54498 | -44.60922 | 2025-11-09 03:49:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 349eebda-6a42-3703-a26e-420dae11a82e | -5.93931 | -38.17437 | 2025-11-09 03:49:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 55ebf997-9d1b-34f9-ac6e-5ce3b1061ed1 | -10.71323 | -47.74136 | 2025-11-09 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74aa8a37-ffc7-3144-9d7c-0de5153855a7 | -5.18057 | -37.86915 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6bc8837-331d-381d-9f9f-56bb26e6cf6b | -4.9057 | -44.64025 | 2025-11-09 03:49:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52617774-f828-3ec2-9fd0-0a88d4753bf3 | -3.86897 | -49.38616 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0d207c9-8804-3d7e-8dab-ba5ab83b8f49 | -3.86906 | -49.38855 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cb3543e0-a73e-3315-a9d7-91f3134884ee | -4.90523 | -44.64307 | 2025-11-09 03:49:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46b57414-732a-3ff0-b9fa-4e385aedd27a | -6.83357 | -37.70791 | 2025-11-09 03:49:00 | NOAA-21 | SÃO BENTINHO | PARAÍBA | Brasil | 2513927 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b958a4b-4d33-365f-aef4-b384ae520231 | -4.39553 | -45.9512 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db9bfb05-55a5-3594-8225-74da3bb0064f | -6.26788 | -42.23714 | 2025-11-09 03:49:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 54065bbb-6e21-3328-9f6d-49607fa2da94 | -4.9103 | -44.64385 | 2025-11-09 03:49:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4f8d18c-653d-35e2-931d-b11062f87456 | -11.55514 | -48.54674 | 2025-11-09 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
