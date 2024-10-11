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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63d0fcfe-b1a9-3bed-bdae-8324563cf031 | -6.33033 | -46.34725 | 2024-10-11 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0eed7c0-20cb-38f7-b927-05b41e3dc140 | -6.33002 | -45.70448 | 2024-10-11 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce112c59-99a1-3c68-8828-93bfacb14880 | -6.32365 | -45.70313 | 2024-10-11 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe81adfa-5a81-363f-b364-2c3df63374df | -6.32265 | -45.70856 | 2024-10-11 03:36:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4df8d44e-18f6-3f15-98b6-f91b489f0528 | -6.1986 | -44.37715 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e81503d-e875-3e03-8561-68939c1df873 | -6.19786 | -44.38123 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 06668de6-99c9-3091-a3d5-925dcaf83d1e | -6.19713 | -44.3852 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51a6616f-494e-3069-8055-099c8d51a97d | -6.19458 | -44.37774 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04f50d1e-1fee-3e4b-b540-8f26c3c8522b | -6.19387 | -44.38177 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6b75e9c-312c-30f8-bbb9-9e45fe854629 | -6.19318 | -44.38574 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 74457c61-5741-369d-874b-063e6950d470 | -6.19195 | -44.38009 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1bd64d75-edbe-341d-8863-c706e6d74c0a | -6.19123 | -44.38406 | 2024-10-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d8e31913-475c-3e3b-b2c0-ca44582047e6 | -6.13261 | -47.27966 | 2024-10-11 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 865f5302-37cf-3f12-824a-61e2ffbbbbdd | -6.12684 | -47.27161 | 2024-10-11 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dce4d7b6-6534-334e-9398-696357050201 | -6.12555 | -47.27851 | 2024-10-11 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5ce5f0c4-0b2c-38ff-ab43-d73d10e7f372 | -6.10921 | -47.26162 | 2024-10-11 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 523046b9-e13a-340e-a042-26f76950cbfe | -6.10798 | -47.26839 | 2024-10-11 03:36:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe83c6be-149a-3e2f-9396-69612480262c | -5.81377 | -44.12359 | 2024-10-11 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb7e6605-ea05-31f7-9746-23d69c79ddaf | -5.74462 | -44.33683 | 2024-10-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04a5f873-15f1-3fe7-9bf2-c20b67251fa9 | -5.7413 | -44.33601 | 2024-10-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60645e5f-8823-37ae-9814-575df7bdd115 | -5.73862 | -44.33605 | 2024-10-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf450b6f-32f8-31e4-9b4b-5f588e43d46c | -5.60878 | -46.36734 | 2024-10-11 03:36:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eed9e058-31c7-3311-b60b-8cfd0209ed86 | -5.28536 | -44.20492 | 2024-10-11 03:36:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bda61315-2ecb-3f40-b924-1d9ab2170e39 | -5.2794 | -44.20397 | 2024-10-11 03:36:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adfee84d-a15c-3b13-ab12-429a36f330d0 | -5.27861 | -44.20842 | 2024-10-11 03:36:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7207739d-b960-3007-852a-e214c0c47442 | -5.27783 | -44.21281 | 2024-10-11 03:36:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8748ff8-e951-3bc3-b6ca-37a7cd15550f | -5.19402 | -45.95065 | 2024-10-11 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f67d8968-a132-3152-83f8-d8ed718f62d8 | -5.19301 | -45.95625 | 2024-10-11 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e4655fb1-9323-3bff-b680-b1feeb6c0f67 | -4.93832 | -45.73896 | 2024-10-11 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22011e77-4b0c-3cd4-a555-1d638a02d397 | -4.90798 | -46.70852 | 2024-10-11 03:36:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c038620-0352-34b6-b848-fde21cf4fb49 | -4.9073 | -46.70814 | 2024-10-11 03:36:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5992d47e-b136-3f0e-a252-1e47dc33be99 | -4.90675 | -46.71546 | 2024-10-11 03:36:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d42e96e-e42d-367c-baa1-8d05454831c7 | -4.90603 | -46.71506 | 2024-10-11 03:36:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d47aa862-b3b3-31bd-866d-203680aac87e | -4.8706 | -45.78545 | 2024-10-11 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00971f48-9b9e-3f64-88b7-e8ae68be4d3a | -4.66344 | -46.8049 | 2024-10-11 03:36:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4b346f6-2a10-31b1-86e0-8850630bb54d | -4.66221 | -46.8018 | 2024-10-11 03:36:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab3e4b79-770e-35b4-b50c-8075ddc628a3 | -4.66092 | -46.80882 | 2024-10-11 03:36:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17a380f7-676e-33aa-9172-1c02ad8ab91c | -4.21482 | -46.89289 | 2024-10-11 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b74e446-4383-3a7b-96d6-180d8172cbfc | -4.20778 | -46.89139 | 2024-10-11 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6133d838-651b-30e2-8d12-52696fa03ca2 | -4.04154 | -44.26727 | 2024-10-11 03:36:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9c698c2-869d-349b-ad18-f7f17f044049 | -3.93269 | -46.4367 | 2024-10-11 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eaa09cc-75bc-3456-9a37-0cc4dacf3b9c | -3.93155 | -46.44309 | 2024-10-11 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08d425b5-a39e-3865-b02c-5d57eb53274f | -3.92789 | -46.46377 | 2024-10-11 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dc94cd5a-8ab1-32a2-859f-c7a4c4ec1f45 | -3.80175 | -44.05085 | 2024-10-11 03:36:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b81f7fa6-fb34-3343-8b2a-ce10cbf8e85c | -3.80097 | -44.05537 | 2024-10-11 03:36:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0723a7e8-9515-3546-9d59-c9b8858d50f9 | -3.61573 | -44.78556 | 2024-10-11 03:36:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c7397aa-6346-3a4b-87c2-b67918318c52 | -3.61483 | -44.79063 | 2024-10-11 03:36:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d742219d-99c6-339b-9721-4aa9eb770d79 | -3.61256 | -44.78761 | 2024-10-11 03:36:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 78a0a03f-c482-3b4c-afc8-f6ff11d915dc | -3.61169 | -44.79271 | 2024-10-11 03:36:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 5946c4dd-6dca-3bd3-ad2b-a800ca7f775b | -3.36855 | -44.36979 | 2024-10-11 03:36:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9a5b798d-7350-356b-ac59-62ce9d2668f9 | -9.6389 | -64.9664 | 2024-10-11 03:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 0b6042f9-d639-30f8-ab23-6446dd76fd51 | -9.6575 | -64.9658 | 2024-10-11 03:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| dd605616-30c8-37f1-b6f4-17f1b1ee5830 | -9.9481 | -58.1092 | 2024-10-11 03:36:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1a8f58ae-3f78-3fa0-9556-b8ee534f09b3 | -10.6962 | -53.0354 | 2024-10-11 03:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 21a4374c-5243-3af4-bbce-a0d8632808b2 | -10.6965 | -53.0147 | 2024-10-11 03:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 10238b10-793b-385b-afd1-14a5479e5c6c | -10.7059 | -64.1138 | 2024-10-11 03:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 743fa018-57e8-32e4-989e-0fca33306267 | -11.2912 | -50.9208 | 2024-10-11 03:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 313fafd3-75a2-3635-b0d7-4066456740fc | -11.2909 | -50.9421 | 2024-10-11 03:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6aaf9aae-2b82-3438-ae61-dd3568892266 | -11.2906 | -50.9633 | 2024-10-11 03:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 10662907-efd0-3215-86c7-3551f75e19fd | -12.4563 | -53.1503 | 2024-10-11 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7b943f7f-c31d-34a8-ba2c-d048d2a3bac8 | -12.4373 | -53.1523 | 2024-10-11 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 891cfe4a-b717-3a27-9efc-3b1496478c43 | -12.4182 | -53.1544 | 2024-10-11 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| c3d7108a-013c-32a7-8e02-a707b0084091 | -12.4179 | -53.1752 | 2024-10-11 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 650db84d-718b-357d-a00e-1c606dd0dca5 | -12.7673 | -44.8904 | 2024-10-11 03:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| db5de362-abfd-3b14-8c75-f1929c746c70 | -12.7678 | -44.8671 | 2024-10-11 03:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e63f7c66-7883-3bbf-b8bf-f6beed839ab1 | -12.7866 | -44.8873 | 2024-10-11 03:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 06759112-6a16-311c-ae4b-7d5f095e782a | -12.7871 | -44.8639 | 2024-10-11 03:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 57097afb-a739-38c5-953f-c0a849033b7f | -12.8708 | -53.4799 | 2024-10-11 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b3d43b5b-f82b-3cee-a3a3-a6026972d3d9 | -12.852 | -53.4611 | 2024-10-11 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bd024542-a4af-37a3-b14a-4f5cf593aca9 | -12.8517 | -53.4819 | 2024-10-11 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 462e5552-96a2-359c-b07c-a60e04345a4c | -13.7346 | -60.6079 | 2024-10-11 03:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9433a028-30e4-3b82-b0d0-bc58b784aa0c | -12.29875 | -47.21114 | 2024-10-11 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e20efca-1ab7-378b-875e-f97f3102645b | -12.29984 | -47.20596 | 2024-10-11 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29516df3-7944-3447-8631-70c1281d608e | -10.60319 | -47.70426 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 616dde34-9591-399d-b852-a94228bce0fa | -10.60558 | -47.70545 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bccd045b-2198-38cc-bc95-d3a58f37fe52 | -10.60868 | -47.71178 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a99970e1-2359-3717-a123-df8c2d077d60 | -10.60988 | -47.70574 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0b579e55-7ad1-3e0e-95b6-d83c8467d3f2 | -10.61104 | -47.7129 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6d4bbc15-8fb3-36d1-b2b8-c92cbc35281d | -10.61227 | -47.70692 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aa487714-e823-30c5-a2aa-31b4d3ffb1bf | -11.52008 | -43.99535 | 2024-10-11 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f16b82-cbb0-3554-8808-86c944d8ba28 | -9.58177 | -44.39557 | 2024-10-11 03:38:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a913201c-cfa4-368c-b10c-5b3b741796d0 | -9.57615 | -44.39461 | 2024-10-11 03:38:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cfbaf896-9082-3d10-a3bf-bd35aaeb464a | -9.57543 | -44.39849 | 2024-10-11 03:38:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 328e3c25-a369-3066-8e25-1d9870dcd294 | -9.52753 | -42.99191 | 2024-10-11 03:38:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95896281-fc7d-310e-b3bf-7437e912e35c | -9.52697 | -42.99497 | 2024-10-11 03:38:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0569e3c2-81e6-3bc9-b052-85730f282051 | -9.2587 | -43.5392 | 2024-10-11 03:38:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 25653211-29ab-3ed7-a51a-85276587bb03 | -9.25799 | -43.54298 | 2024-10-11 03:38:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 08640173-0930-39c1-adac-b2263fabacea | -9.25566 | -43.53642 | 2024-10-11 03:38:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 17b6e4ca-181e-3b10-9715-921bb6fa3e2b | -9.25405 | -43.53464 | 2024-10-11 03:38:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cdf9882b-f5c1-3c13-ba32-884e73033dd6 | -9.25336 | -43.5383 | 2024-10-11 03:38:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f5e703b1-f0ef-3973-a540-bb912c40dbbb | -9.10046 | -35.30195 | 2024-10-11 03:38:00 | NOAA-21 | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7f09f775-78a1-37fb-b6a4-d3771ee14f26 | -8.93901 | -42.59304 | 2024-10-11 03:38:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ef88b08-a4af-358c-8a65-33e11d31266f | -8.934 | -42.59206 | 2024-10-11 03:38:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 56295508-1049-35b7-b1a8-a49d21cf29c5 | -8.93347 | -42.59501 | 2024-10-11 03:38:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08b79e2c-36ac-3b06-8f7b-be361cd462bb | -8.69103 | -38.23586 | 2024-10-11 03:38:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49693a51-a961-36f0-ac39-d008aa41a286 | -8.61764 | -40.52584 | 2024-10-11 03:38:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b4c9eba3-1f3d-3301-b6a1-877fae97507c | -8.58574 | -39.48771 | 2024-10-11 03:38:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4124734a-85b8-3e84-9874-da7bdef0d864 | -8.42765 | -40.82807 | 2024-10-11 03:38:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da23287d-d7b1-38ca-a707-f11c2cc51512 | -8.41372 | -40.235 | 2024-10-11 03:38:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c6e4c9f5-e372-3bc8-8022-01afd010e057 | -8.37594 | -40.58549 | 2024-10-11 03:38:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
