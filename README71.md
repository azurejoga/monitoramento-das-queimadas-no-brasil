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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 497f98d6-3091-3c7a-a675-59c498fe4e49 | -7.0164 | -44.6413 | 2026-09-15 09:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 328.1 |
| 16d6ee0b-07aa-3f7b-97d6-834c5558a3a5 | -7.0166 | -44.6184 | 2026-09-15 09:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| dd2cd25b-2eb9-3584-a1b5-774a56ad0e0e | -7.0164 | -44.6413 | 2026-09-15 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 420.8 |
| fc69cf9a-b50e-3f8e-b0d2-6b539ea14640 | -14.1671 | -47.3649 | 2026-09-15 10:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5aa9202a-e5a6-3303-a69e-f32ff81ae8f9 | -7.0166 | -44.6184 | 2026-09-15 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 3ca5ec3f-58e2-3c38-bc3d-2c58d37a8e5c | -14.1666 | -47.3876 | 2026-09-15 10:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 16f62f6c-594e-312e-b06b-9208f0ae4d91 | -7.0166 | -44.6184 | 2026-09-15 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 3f0806ca-cdcc-3170-b59a-dd337272d1e3 | -7.0164 | -44.6413 | 2026-09-15 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 376.4 |
| e102684b-1d04-3e7f-a4bb-0af5c8e406cf | -7.0161 | -44.6642 | 2026-09-15 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| bfb24ffb-b19a-3617-b120-1b8d17f10e80 | -7.0 | -44.62 | 2026-09-15 10:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9a9ca0-8a79-37de-9bc0-8117dfa153ad | -7.0166 | -44.6184 | 2026-09-15 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 1af73d8f-3e2f-3b1b-b6a2-ed4825aaf49e | -7.0161 | -44.6642 | 2026-09-15 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ec1c2eb5-b210-3a42-be09-1e6e732169ed | -7.0164 | -44.6413 | 2026-09-15 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 402.2 |
| 86332575-ee72-3a03-84de-0ba4913e5df3 | -7.0161 | -44.6642 | 2026-09-15 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 576cf47c-3951-3a2e-8f0c-6b5abd565f51 | -7.0166 | -44.6184 | 2026-09-15 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| aeb8e176-3bfe-3a8f-ba9d-1680217aca9d | -7.0164 | -44.6413 | 2026-09-15 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 408.7 |
| e04e4a48-3997-3122-b631-10504172959e | -7.0161 | -44.6642 | 2026-09-15 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 1c0f8b98-5259-30d7-a450-dd05fc026e27 | -7.0164 | -44.6413 | 2026-09-15 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 390.2 |
| 9e6f5183-69fe-392b-b2d6-099678d64aa0 | -7.0166 | -44.6184 | 2026-09-15 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 050d1707-0bd6-3c3e-a648-9f419f023021 | -6.9976 | -44.6429 | 2026-09-15 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c8d45ec9-117e-362a-a06f-0c22d2eb9c00 | -17.5457 | -45.5054 | 2026-09-15 10:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 345.2 |
| 3d69b0eb-79bb-3600-912c-fafb4c427c06 | -17.5463 | -45.4816 | 2026-09-15 10:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 86534d31-90f7-3d53-b4f7-4d738f61bc46 | -7.0166 | -44.6184 | 2026-09-15 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 48e19e73-1093-3fd8-a6ac-9ddabb8b6576 | -7.0164 | -44.6413 | 2026-09-15 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 367.8 |
| c230372a-9b30-3e7f-8004-a39c03054ac9 | -7.0161 | -44.6642 | 2026-09-15 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 68bdad64-1c86-3e5c-b335-5d7b80b740c1 | -11.5041 | -45.7939 | 2026-09-15 11:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0eb6a7fd-084a-3b30-bfa5-f4aace184550 | -7.0164 | -44.6413 | 2026-09-15 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 339.6 |
| 5d333487-a6d5-3e7e-b7a0-dce92a1efe02 | -7.0166 | -44.6184 | 2026-09-15 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 915698b5-c9f4-3128-9c69-0bf9d1727500 | -14.6734 | -42.8606 | 2026-09-15 11:00:00 | GOES-19 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 8fd64fb8-2501-38c7-8f8a-c4785a0a4919 | -7.0164 | -44.6413 | 2026-09-15 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 645097a6-d16d-35bd-9ff0-0feeae180572 | -14.6734 | -42.8606 | 2026-09-15 11:10:00 | GOES-19 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 95.1 |
| b4a2bbcc-3783-3963-ac1b-31ef73dae03b | -7.0166 | -44.6184 | 2026-09-15 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 3d3db062-8fd9-3397-9570-1957a55d5b79 | -11.5041 | -45.7939 | 2026-09-15 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 4f693019-6e40-3f1f-a6d0-47ebabef318b | -11.5045 | -45.771 | 2026-09-15 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0161f00b-6fd7-339d-94a0-791f2774dc3e | -11.5041 | -45.7939 | 2026-09-15 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| e678ce2c-0d02-32aa-a32b-28e813b10eb7 | -10.8665 | -46.3105 | 2026-09-15 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e7cfdde6-74d0-38a8-94a3-b8cd243591ed | -7.0166 | -44.6184 | 2026-09-15 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| c16996be-241a-34eb-8285-965c2aeeddde | -7.0164 | -44.6413 | 2026-09-15 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 247.6 |
| e9f8e26a-3987-3eae-a0a3-a4c519d499d7 | -14.224 | -47.4234 | 2026-09-15 11:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f4eb18bc-e085-37f8-b2ab-57d04c9f9874 | -14.6734 | -42.8606 | 2026-09-15 11:30:00 | GOES-19 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 847729f1-7cda-3939-b89b-942fc233a71e | -10.9875 | -48.3209 | 2026-09-15 11:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fa8016ef-6a39-3683-adfa-778317d96892 | -11.5045 | -45.771 | 2026-09-15 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 379461a6-8c36-3794-8bd5-379eedf58561 | -7.0352 | -44.6396 | 2026-09-15 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 070b559a-bf8b-3d1d-a02b-e381be191543 | -7.0166 | -44.6184 | 2026-09-15 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| bc9aa165-0824-387a-982c-6dfef78486c9 | -11.5041 | -45.7939 | 2026-09-15 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 6c3f6f24-113a-3715-adf8-c1ec845f8b44 | -13.287 | -51.2832 | 2026-09-15 11:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 43bb707a-4d46-3e9e-bf1c-70d783beba28 | -8.638 | -44.4567 | 2026-09-15 11:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1bff989f-c91a-3177-ae22-01088335e3a3 | -10.8665 | -46.3105 | 2026-09-15 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6505086b-2aac-376c-806c-fcec61dfc308 | -7.0164 | -44.6413 | 2026-09-15 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 1a2934c1-dd40-3e7e-b37c-d8934bacb386 | -11.5041 | -45.7939 | 2026-09-15 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e93310c3-396d-3097-b2a3-bdb055b27347 | -9.3575 | -50.1156 | 2026-09-15 11:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d8a3bfeb-1143-3266-ba95-db88e1faf66e | -7.0164 | -44.6413 | 2026-09-15 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 246.2 |
| 9c4c0ce8-4420-397c-812b-5f783e055f27 | -13.2232 | -51.6744 | 2026-09-15 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9586dbf6-a74b-3e71-9394-45ec2476809f | -11.5045 | -45.771 | 2026-09-15 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5ee4d8a6-7ae8-322a-a4de-7bb223820df9 | -7.0166 | -44.6184 | 2026-09-15 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| c8870f70-26db-30c0-a8f4-58d307d6c9c3 | -10.8665 | -46.3105 | 2026-09-15 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 5f9274fa-ae5f-3e62-895d-7192a513ef11 | -10.8665 | -46.3105 | 2026-09-15 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 981797c5-07b9-333f-82c5-c55734c4b18c | -7.0164 | -44.6413 | 2026-09-15 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| bc098e34-00c8-3059-8b92-c6a11dacb836 | -11.5041 | -45.7939 | 2026-09-15 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 6e73a34f-cb94-3a14-9334-779a88c0d867 | -11.5045 | -45.771 | 2026-09-15 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d6ddd0ca-f710-39d7-8093-3757446e9ee4 | -9.7687 | -46.1067 | 2026-09-15 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 51898bf3-bc93-3279-b120-aa661f757fef | -9.3572 | -50.137 | 2026-09-15 11:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c006bd1c-81df-3591-a3e4-b6deb04fda7b | -7.0166 | -44.6184 | 2026-09-15 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| caae7a12-3791-3159-b73f-7687b8366605 | -9.3575 | -50.1156 | 2026-09-15 11:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 139014a6-186e-355d-97c6-aefffdda1c00 | -8.638 | -44.4567 | 2026-09-15 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| dcf51edd-8c57-3622-9111-4e94515bc65a | -10.792 | -46.2071 | 2026-09-15 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e6e3d7bd-df4d-30c2-b831-253b4adb735b | -10.8661 | -46.3331 | 2026-09-15 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| efa60938-f077-372b-9481-d1cd78170d19 | -10.8665 | -46.3105 | 2026-09-15 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 470.0 |
| 8bf9f67c-1543-38a2-8b64-75a3fea6eacb | -11.5041 | -45.7939 | 2026-09-15 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 7d00eb30-c415-36c8-80e1-2ac896977d56 | -9.3575 | -50.1156 | 2026-09-15 12:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 062f0cdd-9cd3-3bd4-8c30-5d7c702e1501 | -8.6191 | -44.4588 | 2026-09-15 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| afbb6bb7-dad6-32a5-b4a3-de7bbae53863 | -7.0164 | -44.6413 | 2026-09-15 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 9a5a3b3f-fbcc-31bb-821a-50a7e8502bb1 | -9.7687 | -46.1067 | 2026-09-15 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d774997d-de53-3421-ac8d-8207be022abb | -8.8459 | -45.8713 | 2026-09-15 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 654779ef-f0c9-3621-87e6-30cd8e889b7b | -9.3572 | -50.137 | 2026-09-15 12:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ff35bfe1-65e0-3dab-a5aa-88ca28c66395 | -11.5045 | -45.771 | 2026-09-15 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 6af92e77-708d-3000-af07-8ed79133e4da | -13.287 | -51.2832 | 2026-09-15 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1623dede-242d-3dc6-9947-3c8fa3d90d6f | -7.0166 | -44.6184 | 2026-09-15 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e2ed6049-1c07-3948-8186-81c25c9f21ab | -8.827 | -45.8733 | 2026-09-15 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f684d781-51e2-3bbd-9e28-4ac98be6064b | -3.0725 | -51.20064 | 2026-09-15 12:04:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07a0f50b-7279-379c-a599-c8d09de9879c | -2.96355 | -52.15345 | 2026-09-15 12:04:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| eb9f43d3-5126-31c8-a298-4fda4172c974 | -3.49573 | -54.66705 | 2026-09-15 12:04:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 716bbf43-6175-34e1-b131-b25993f23294 | -2.77453 | -49.46171 | 2026-09-15 12:04:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d2aae0ef-d2fb-3f50-9d1a-8a70d81b661c | -1.813 | -48.81239 | 2026-09-15 12:04:00 | TERRA_M-T | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e73cc8c9-0cc9-35ce-8afb-044d7578e19a | -3.85026 | -51.88499 | 2026-09-15 12:04:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 5ee09f7a-759b-3554-a5cc-5eeaa9b93f8d | -2.90662 | -50.41931 | 2026-09-15 12:04:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1f70d240-ac48-3b55-a379-d62af0a33067 | -1.99841 | -47.04023 | 2026-09-15 12:04:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2bf75c44-650a-36c3-aeda-751025d98390 | -3.23385 | -50.58335 | 2026-09-15 12:04:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2204d635-43fb-3a17-876c-6279ed2ac8c5 | -4.08374 | -48.95256 | 2026-09-15 12:04:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 90aeb392-4a5a-35ee-bc98-7c9cdedcbdf3 | -2.78115 | -51.36712 | 2026-09-15 12:04:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51c235ec-d208-3e1e-a8ec-6d759d027baa | -1.22504 | -54.13058 | 2026-09-15 12:04:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f2d09f5b-3e50-36d7-84fc-07d8fcaa0a2b | -3.38075 | -50.39149 | 2026-09-15 12:04:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cdbd2107-6504-3dcf-ad2f-9572d85a6777 | -1.22988 | -54.12682 | 2026-09-15 12:04:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 007eb4f7-b3c9-3c85-a4d7-2e1ba2a2a30d | -4.03566 | -43.24244 | 2026-09-15 12:04:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 9faccc1b-2d15-30a9-8cd5-de246641a591 | 2.20126 | -50.91026 | 2026-09-15 12:04:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fab69ee3-11f5-308c-9abf-de814d5a709d | -3.11077 | -53.94857 | 2026-09-15 12:04:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f8324a7-58a9-37ec-837f-699bd70ef83c | -2.66531 | -57.55701 | 2026-09-15 12:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 3719a956-8007-3836-8bea-8c49b935e400 | -4.08394 | -47.06536 | 2026-09-15 12:04:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 7f3d0bc5-a915-3c84-a063-2ac016d9eb72 | -2.78401 | -49.46302 | 2026-09-15 12:04:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ec5a104c-3186-366f-829b-3af05e015923 | -3.04595 | -51.26031 | 2026-09-15 12:04:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README72.md)
