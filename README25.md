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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f49e5d3-58b5-3e9c-9adb-0786bea6d1f2 | -4.58673 | -43.33992 | 2025-11-06 05:14:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e9bc49c8-1b51-3930-8200-99b3ec2fef01 | -3.77803 | -51.67638 | 2025-11-06 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3733b9e-6abf-31e2-b65a-b5a2524a7a22 | -4.18326 | -52.09059 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eac575e3-716f-33d2-904d-272ea3ed568d | -4.49296 | -55.79909 | 2025-11-06 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b874876-e031-31aa-a8c8-737a213e7423 | -4.67421 | -50.44328 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3dfdf0e-0305-31eb-95dd-84cb124d7c89 | -4.60273 | -50.99636 | 2025-11-06 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd6ac1c7-f952-333d-9217-ad4bb8f68de8 | -2.82003 | -57.66256 | 2025-11-06 05:14:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f3aa2aa-dabe-334b-9cf3-d8af1f82f76a | -8.06875 | -54.92061 | 2025-11-06 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99cd38f-09b0-3401-b6b4-66d08cc8f0cc | -2.79232 | -50.30959 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f147824d-4668-3131-9bd7-40a3e9c720ca | -2.79103 | -50.31811 | 2025-11-06 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f717cb20-a03f-37b2-804f-c54cbcdd8e8d | -2.98348 | -52.8192 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2068caa6-89dc-33bd-90d3-33f283f225c6 | -4.67635 | -50.44608 | 2025-11-06 05:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5be0290-37f8-39aa-8b61-92d9e91d50dd | -3.07048 | -52.63017 | 2025-11-06 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a55798c4-49eb-3a37-b190-1854c3c6c939 | -10.22612 | -57.80331 | 2025-11-06 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 761a6d33-6af2-331f-bca0-3254861b663a | -11.85806 | -56.86261 | 2025-11-06 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8a9305-8a6d-3c92-a6f6-9e5281e85656 | -11.72861 | -59.32026 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dfe5c82-623d-3e90-b50f-cc6127dfbb69 | -9.4632 | -63.51696 | 2025-11-06 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 020a3554-601e-308d-b655-55871ad50da5 | -9.64601 | -63.11206 | 2025-11-06 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 756be43f-a826-38d9-9ff5-67667076ada7 | -9.65002 | -63.11277 | 2025-11-06 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05ca51de-0df9-36cf-bc7b-780c9fb80786 | -12.64035 | -55.71042 | 2025-11-06 05:16:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9474f822-eb9a-33e5-aa0a-b77606046f5f | -11.72251 | -59.31561 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29cb0f82-6194-3be4-bfa3-7bb4bb8d041c | -9.44366 | -56.64349 | 2025-11-06 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4d904af-3fd0-3605-8433-22218abb7f54 | -10.45684 | -58.1427 | 2025-11-06 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2be7d462-294e-3121-9328-ff9e79895118 | -10.22895 | -56.77831 | 2025-11-06 05:16:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf385806-0510-361d-a33e-2456362967fc | -12.07389 | -56.6785 | 2025-11-06 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e171d95a-9526-36e6-a3f8-8087aad537e7 | -10.23234 | -56.77883 | 2025-11-06 05:16:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b55dc97-55a6-354b-be43-25fff90a58a4 | -11.73365 | -59.31016 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4776dcb2-2d86-38f7-9f03-046c4caaf7b0 | -11.73666 | -58.30788 | 2025-11-06 05:16:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87883214-2a5e-39b3-a08b-9fea96e37491 | -11.73642 | -59.31425 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 507d6cd9-68b4-39f1-9403-b0c69f18c2f2 | -17.19477 | -50.86869 | 2025-11-06 05:16:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 281468e6-4b75-37b1-aaf5-519cedf3b5a5 | -9.46255 | -63.52071 | 2025-11-06 05:16:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99abfcd2-6c5c-3f8a-a5a5-f1706cdea964 | -10.94733 | -59.10141 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b40982e7-50a9-36d9-aea3-c9faf4e603f4 | -10.95066 | -59.10196 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 396b34ae-31c9-33c0-b8d5-9db56ca8e707 | -12.07044 | -56.67797 | 2025-11-06 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4af52d51-c59e-3779-8bc6-905b3f3c3fc3 | -10.22555 | -56.77778 | 2025-11-06 05:16:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67fc3d3c-f9dd-3ed8-b369-101d4f9cb7d6 | -11.72918 | -59.31671 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd169138-9a31-3c8c-a31f-4068fcca221d | -9.59866 | -64.15636 | 2025-11-06 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 614fb643-7902-3914-8543-d0190ec0a290 | -9.21751 | -62.4531 | 2025-11-06 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f80e5eb-1a58-3c3a-aa75-f390b4c43091 | -11.72194 | -59.31916 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aceb06c-06b3-33b6-9240-839302350730 | -11.72755 | -59.30552 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 213b1dde-b78f-365d-b3a0-26f4e5d8366b | -11.72585 | -59.31615 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fc7b6b9-5e79-311c-9976-1223aa63dadd | -9.44705 | -56.64402 | 2025-11-06 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42f767a5-f0ad-3bd2-bc29-4e83a6bca421 | -11.85464 | -56.86209 | 2025-11-06 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d50acad-cd09-3a7a-90a2-f598ef3fe1f4 | -11.73032 | -59.30961 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8956af85-a673-3096-a437-2dde59a7e76e | -11.73422 | -59.30661 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 289a1a85-3c79-38a4-a624-c98db39143a8 | -9.59937 | -64.15227 | 2025-11-06 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a62f7238-a791-36de-9c88-477f64c7a38e | -11.72471 | -59.32327 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 682e0678-6d61-394d-ba8e-18fcab573d86 | -12.41525 | -51.53845 | 2025-11-06 05:16:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16c620d5-0e9e-3ad6-9bd8-d6a291dad764 | -17.19439 | -50.87196 | 2025-11-06 05:16:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e13009d0-36c0-3255-89e7-a7688b8138c2 | -11.72804 | -59.32383 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26dc69a7-bfa3-3b53-8831-2992a8221e08 | -9.44423 | -56.63985 | 2025-11-06 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a94f19c3-1b46-3fca-a3a0-8da2e9374295 | -11.73088 | -59.30606 | 2025-11-06 05:16:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0878f7ba-11f0-32f5-a7a5-c15bae6a83a3 | -17.96941 | -52.69729 | 2025-11-06 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5deb75-2b27-3064-a97e-8f24f6c9e9d3 | -17.96645 | -52.69822 | 2025-11-06 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a71b11c-50ef-3544-8f3b-4fcc2c637af1 | -17.96409 | -52.70194 | 2025-11-06 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14afe0f3-a4f7-3e9a-939f-5e71bab76aa9 | -4.6121 | -43.3227 | 2025-11-06 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| fffd2b4e-96f1-3cdf-90d9-5eb322a420ae | -4.5934 | -43.3239 | 2025-11-06 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 5b0df13f-650e-343a-8aec-51398fcbf62a | -4.5745 | -43.3483 | 2025-11-06 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0384fdfd-82ab-3e9f-9446-f14608993415 | -4.5932 | -43.3471 | 2025-11-06 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 233.2 |
| c5c81fd7-5bcb-3a37-b263-15f9050d0c9d | -4.5747 | -43.325 | 2025-11-06 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b0807136-eead-3b93-a130-df8314d5116d | -4.6119 | -43.346 | 2025-11-06 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 794c68df-ec68-37b5-893a-763941b07bb4 | -29.27185 | -52.83274 | 2025-11-06 05:20:00 | NPP-375D | LAGOÃO | RIO GRANDE DO SUL | Brasil | 4311254 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 67ae43fe-5c39-370c-8bc7-01cfa9e0a393 | -29.26994 | -52.83115 | 2025-11-06 05:20:00 | NPP-375D | LAGOÃO | RIO GRANDE DO SUL | Brasil | 4311254 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 059614a6-8b25-3806-a0c9-6c8c91c8e0ce | -29.26966 | -52.83488 | 2025-11-06 05:20:00 | NPP-375D | LAGOÃO | RIO GRANDE DO SUL | Brasil | 4311254 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4b3e8dbe-2727-3ef0-b6f9-b163f504a326 | -4.5892 | -43.32403 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f527be5c-c27a-3152-b25e-7ed1080e945e | -3.8923 | -42.54279 | 2025-11-06 05:29:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 7667f826-5f4c-3553-95dc-4a8776bbc1b6 | -3.43159 | -42.54631 | 2025-11-06 05:29:00 | AQUA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7c48841a-8d99-3a6d-86a1-33a27aa32db0 | -3.90346 | -42.54447 | 2025-11-06 05:29:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| f075dd0a-4d2c-3822-b410-63942376f7ec | -4.60095 | -43.32578 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 38d34c68-8e26-36a2-95a6-0ab543875c96 | -3.47057 | -43.66555 | 2025-11-06 05:29:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 10aace47-860b-3a2c-be53-11748d049ad1 | -4.58662 | -43.34037 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.9 |
| c55cbaa0-363a-355c-aad3-f8df965fd384 | -4.46271 | -43.23223 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 35b8d373-756b-3353-9f6e-19f0a3eaf11d | -4.57744 | -43.32232 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d015b184-179a-38f4-a07d-06c69c1e2324 | -6.27264 | -43.67398 | 2025-11-06 05:29:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cc7726f5-92c3-3d5f-be37-364c39937d2c | -4.45104 | -43.23045 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1512eb5c-06b0-3c70-8875-0d3290b6ba55 | -3.47349 | -43.64737 | 2025-11-06 05:29:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 446722bb-b9e2-311a-987e-d71c00a4791e | -7.069 | -41.58412 | 2025-11-06 05:29:00 | AQUA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 50c594b8-1ab8-304c-b38e-28b66dc33c51 | -4.59837 | -43.34221 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d9b7e5f7-1469-3d28-b22b-054d1eb6a2af | -4.45644 | -43.22422 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| fdb2fe64-a270-362a-94e4-8ea598e26c09 | -3.61366 | -43.50986 | 2025-11-06 05:29:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f783c0d1-5867-3dfa-ba3b-e66a981c0494 | -6.1068 | -41.62986 | 2025-11-06 05:29:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4ed53f5f-fed1-3a68-8b2d-2cc80c180f18 | -4.46531 | -43.21614 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 27c8930f-d26d-3121-8f1b-aeaa70a285a0 | -4.58402 | -43.35685 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3b669487-f984-3e81-91ae-dc0fbf2ca259 | -7.2415 | -39.39923 | 2025-11-06 05:29:00 | AQUA_M-M | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b34988ee-7375-3c43-8404-82dbcc22ba75 | -3.47175 | -43.64002 | 2025-11-06 05:29:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a8302e0b-5fa5-3135-b2fb-2ae2ab870ace | -4.46811 | -43.22604 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2b801d97-8a5f-342b-9b58-55375bac714a | -4.57485 | -43.33861 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 8e491878-0012-374c-8b6a-3acc29fee327 | -4.45365 | -43.21438 | 2025-11-06 05:29:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9a7a7ccd-9af8-35c0-81cf-cfd773c526a0 | -3.46898 | -43.65812 | 2025-11-06 05:29:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 5d2c1fac-21a1-34d4-9d5b-c9ab16cb9d3f | -4.6119 | -43.346 | 2025-11-06 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f47ba52d-85ee-3cf7-9311-480a5d54de68 | -4.5747 | -43.325 | 2025-11-06 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ec49f2f6-8de4-3bae-bf50-399080428701 | -4.5745 | -43.3483 | 2025-11-06 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| afcabd84-4ea9-39e3-a9f1-9897249d84b0 | -4.6121 | -43.3227 | 2025-11-06 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 15afac22-af92-382f-bf89-b11389e638e2 | -4.5932 | -43.3471 | 2025-11-06 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 70fe19c0-30c7-3f4e-b496-9038e03f91d0 | -4.5934 | -43.3239 | 2025-11-06 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 57103d9d-99af-3e94-b888-23eaa332170c | 3.23833 | -61.20573 | 2025-11-06 05:31:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce0508c6-a1db-301d-8a0c-00d7352edb78 | 2.62239 | -51.01279 | 2025-11-06 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f23057bb-d414-3180-9dcf-c6def638efc1 | 3.23779 | -61.2023 | 2025-11-06 05:31:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eb9c8e5-e169-3e35-8cdd-d474bd89b0d6 | 2.62354 | -51.01218 | 2025-11-06 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08b3f660-dbe0-3761-8be8-714b3c893b13 | 2.62165 | -51.00854 | 2025-11-06 05:31:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README26.md)
