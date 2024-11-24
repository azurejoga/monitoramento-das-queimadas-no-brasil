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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ebd41c1-10db-3840-8aaa-a931d33ca258 | -4.0507 | -48.320999 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0552998-e5d2-3e21-b2e7-07d0a1dad41a | -3.8378 | -44.0555 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0b861b4-88ae-39d6-906f-85af863cf61f | -0.2875 | -51.602699 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 54eb093c-a297-326e-ab94-0e00bfd64eca | -4.1157 | -49.434399 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a601b47a-90a6-38a0-9ee1-53fe9ebe7917 | -4.6374 | -46.862202 | 2024-11-24 00:25:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 090bd02c-d0f7-397f-b8e1-9c1c344c820a | -1.4004 | -54.4478 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00007fc-160e-305e-bad5-3cb8938b3699 | -4.5978 | -44.7132 | 2024-11-24 00:25:00 | METOP-B | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5214372-4405-30f6-ae40-fa2f22ec1497 | -2.6824 | -45.657299 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb46f07-b990-3615-9e97-13021b418ae5 | -1.5987 | -52.581902 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cd3e34-9f39-3253-92e7-48e1005f67e2 | -2.1367 | -50.666698 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2cc37e5-fdcd-3ce3-8dc3-2f6e5f865d93 | -1.5047 | -54.180099 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8c13955-6b59-383e-bff5-7cae365fd2ba | -4.3551 | -45.269299 | 2024-11-24 00:25:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f10cead9-342e-3ebc-8e01-cfd4027bb603 | -1.9533 | -49.530602 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd5d5d9a-2357-3474-a4ee-e7e36ec4e31e | -0.2532 | -51.633701 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3d44d127-0f57-37a0-9a38-d864a53eb7d4 | -2.3208 | -51.3041 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d445f658-8f87-33c5-800c-36f73c7ff799 | -4.2396 | -48.701801 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75b07e61-48cd-3b96-b65d-e198a10498a4 | -3.8427 | -46.000099 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad53c1ce-11ed-3b4b-8d4f-13651d8271a5 | -2.1509 | -50.913799 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e1e29c-a19f-3515-a0c8-983eeb91f182 | -4.3532 | -45.260899 | 2024-11-24 00:25:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e74bc1de-f0a9-3eb7-9fe4-cf1b78b11b07 | -4.4856 | -48.102001 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6309750c-2746-3e1e-b637-b4844d7604b2 | -4.5246 | -42.894901 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74263fa2-c500-3076-85db-7159e0db3de8 | -3.7648 | -44.0513 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01f820a8-d43e-3b24-b47b-1161ae47cca9 | -2.7095 | -46.272099 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a62cbb2-fcde-383a-8604-0292502e1c14 | -2.5928 | -44.951199 | 2024-11-24 00:25:00 | METOP-B | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c996a0cc-cc51-367c-913d-007ae5e76d0f | -1.7273 | -53.2481 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe8bfb7e-4ade-3b86-9a53-b1d36a5d7412 | -5.1957 | -49.1521 | 2024-11-24 00:25:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 172980b2-f707-366b-b26e-0109e07659bd | -3.2932 | -49.9002 | 2024-11-24 00:25:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2057804-a38b-3b62-b25d-4459b9a2fe48 | -3.51 | -50.5462 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb21861-87d9-3689-b01f-92720466a72e | -5.109 | -43.148102 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 392b3390-f741-39f3-80e2-9eae8bea45ec | -4.4872 | -48.108799 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634e7841-057f-3df8-90de-6c39e36d3e80 | -3.4702 | -50.000801 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb9a70d-ba03-3dad-a463-16e4c6dcf25f | -1.7567 | -52.690498 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68c1c681-5a06-3698-8fc9-e8e958f71592 | -4.42 | -47.675201 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed3e498-ad09-3630-9fa6-04087e3f56b9 | -1.2781 | -52.253399 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 414ab84a-4161-31c7-91c4-65424b3628db | -4.6569 | -46.044701 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52ddf268-c0cf-3c61-8eb4-b6c614be0158 | -1.5168 | -54.1884 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c04ad3ec-752e-352a-bed8-f17bbbbd06ce | -3.4717 | -47.675098 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8543b6eb-6989-3236-a7b7-24b8acbdf4fe | -0.3347 | -51.537701 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7d6cd8-7247-3bec-bcba-c85d8e92a60f | -0.9753 | -47.118599 | 2024-11-24 00:25:00 | METOP-B | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4a62c7-c665-3d4a-b577-2998e9d57d75 | -2.8669 | -45.833099 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0bbda776-fb5e-3506-88e3-f23dec1a50cf | -1.1951 | -51.929901 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1ab1be4-3ff7-3b32-9378-6ec5d5541d88 | -4.2411 | -48.708698 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 129a8fad-98d9-38b0-8a43-ecfb56c75232 | -2.5039 | -46.093399 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4699fb4-0e0f-387b-919e-d90e8ddd7241 | -2.4159 | -48.9776 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3978af-be23-386c-a9e9-f72e154158b6 | -3.8652 | -44.173901 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a591040-13ed-3d56-aad5-1676b124fbc8 | -4.0491 | -48.314201 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96a87a28-24d4-3285-a303-f67c982b7088 | -1.4501 | -53.3867 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba580bcb-e76e-3178-b634-be0f22578e0d | -1.1102 | -53.383499 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27082b3b-77a1-357b-aada-4d6317a4dbe3 | -2.9284 | -46.689999 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f7ac4f-98ae-395c-b7e4-8a6c65fc2efe | -2.6807 | -46.145901 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2bdcce-89cf-301e-b1b8-bbe99ad8680e | -4.3116 | -48.0616 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb19b452-81fb-3289-922b-48d3bf224663 | -0.9443 | -51.638699 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e4bcda-3b32-361b-8a96-4de51c2d2803 | -1.5604 | -51.9981 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d9197c-dee1-374f-bd05-410911065f8c | -3.8086 | -51.3321 | 2024-11-24 00:25:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b07701d9-711c-3877-ad7b-1158d7c68abe | -0.8779 | -51.709099 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| aa646a93-64f4-37e3-8e49-63ec79a3a001 | -2.1588 | -50.489799 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a8db88-61dd-362a-8c0c-d7eb3f1f8bc5 | -1.2712 | -52.6805 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c33283-a8e3-3a24-b333-fd1e8cec6039 | -1.4232 | -51.112301 | 2024-11-24 00:25:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7305c813-242f-33be-a291-9338ffcdf95e | -1.6066 | -52.571301 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 999fc2f1-f7c6-381f-b119-5086129b3a3d | 0.4078 | -50.849499 | 2024-11-24 00:25:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9e175d07-5644-340e-905a-b45c521a0e1d | -2.073 | -49.604599 | 2024-11-24 00:25:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e014137b-bfb7-3d7f-9bdd-700c97235491 | -1.7708 | -53.625801 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aacac32d-c1b3-3064-a7d1-43371c823d85 | -1.4564 | -48.197102 | 2024-11-24 00:25:00 | METOP-B | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e646bdc-64df-3442-8084-04bd5333eec0 | -2.1606 | -50.452099 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9689cf25-7e04-3a9f-854d-f5a06db0a8a9 | -3.7008 | -47.594601 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 699df414-55df-396d-80c8-12348ec9b28c | -5.4594 | -44.8288 | 2024-11-24 00:25:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbc2e831-0863-3e1c-8f2f-6b9fb5185acb | -1.1978 | -51.758701 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7096166c-3188-3c91-9657-5bb666add60d | -2.604 | -46.849201 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77673e47-5537-3d6c-a2e8-9f086725a8ad | -2.8182 | -51.780602 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97f3b85-3d69-3a1c-9d31-42e52622b993 | -0.3313 | -51.5229 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 16a5e12b-e820-3631-85aa-4a855efe6a10 | -2.0745 | -49.611401 | 2024-11-24 00:25:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a33a21-05f1-3f26-bd4d-2baad6321088 | -4.0275 | -47.262299 | 2024-11-24 00:25:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f419622c-390b-3de1-80a8-c683995950d7 | -3.6099 | -47.5117 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a872dfe-f15f-3a02-9fec-076973914e6d | -4.0832 | -46.150299 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28ad2adb-0802-395a-ac33-dc80121e85e8 | -2.5313 | -46.3941 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d272255-522a-31d6-85e7-62e205651078 | -2.8 | -54.0079 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236ff9f5-c136-3929-af0e-70849361305d | -4.0699 | -49.184502 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4626a71-cc4a-3424-99f8-da0a36a8bfb4 | -2.5112 | -54.092999 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 548cb7b4-da0b-3db8-9349-3ea79608cde2 | -1.7003 | -48.455101 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ff9211-5488-3fda-992c-f3487b49c9f0 | -2.766 | -45.9328 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7610698-a69f-3316-95a6-569212c14e6f | -0.1927 | -51.639301 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 690e842a-29a4-3a6d-8c9f-1c040b2e1f10 | -0.9793 | -51.702599 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f2e91868-fa87-3022-a1df-061926053780 | -3.0722 | -45.9655 | 2024-11-24 00:25:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff4e03d5-4ecb-354d-8d88-7051f4a668ba | -1.2452 | -51.7402 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 827be6f5-3720-3489-823a-b0315aed5d3e | -0.8381 | -52.538799 | 2024-11-24 00:25:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 505ee792-ceba-3f51-832a-023cc8807c8c | -2.6894 | -46.0938 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68ee498a-4f97-3e7c-94df-574a72d10238 | -2.1077 | -50.125099 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47cb35e6-84b4-38ef-85e7-caeff8fa82d8 | -2.4267 | -49.025299 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587e84d8-bc07-3d6f-94f7-de3edc609582 | -3.6067 | -47.497601 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02f882da-69b2-3b34-83a4-39e73a537623 | -3.7746 | -44.049099 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b7e4191-293d-37e1-8cb7-c6bc1f9eaeee | -1.279 | -47.868401 | 2024-11-24 00:25:00 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 568a45a1-2cf6-3dc3-967d-007641bad9b2 | -6.3536 | -47.292301 | 2024-11-24 00:25:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f7a90e6-b933-3314-b86d-b2e11067cc8d | -2.4126 | -49.0998 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ba1ca9-5f6b-37e1-a90e-4f251b994579 | -1.7665 | -52.688301 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2a7ba6-2f29-3d0a-abe0-f71d97daef74 | -3.3549 | -50.1297 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e626e55-0741-3bf0-b1f8-7cd92c35f90a | 0.0042 | -51.1768 | 2024-11-24 00:25:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a0859b29-a3f4-359b-8856-09d40acc7be5 | -3.6992 | -47.587601 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23e18f57-53b2-36f1-a0c0-435ff5e833e9 | -1.4867 | -54.0541 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff99216-abd6-32ed-a387-a483ec5e024e | -2.6026 | -46.254902 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86dca2da-7bdb-3c69-86cb-3fbeacd924aa | -1.524 | -51.606602 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
