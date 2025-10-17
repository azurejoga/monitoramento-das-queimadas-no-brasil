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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 549b3616-af5c-34cb-9d77-9359332063e3 | -9.1378 | -46.6261 | 2025-10-17 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a2440ad0-78b8-3a9e-a169-50da40ce9b69 | -9.1564 | -46.6465 | 2025-10-17 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cf0fe95a-4d54-3436-9fe3-937be3c59ffc | -10.2748 | -44.0247 | 2025-10-17 04:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 01492331-f850-3cb4-885c-b3bd4dd44d5d | -10.2745 | -44.0481 | 2025-10-17 04:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3705345a-b37f-3b08-9980-6e6e493f46d4 | -14.3227 | -51.4475 | 2025-10-17 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| eb78a208-30d2-3cdb-aed5-8d8ea0cee3f3 | -10.534 | -49.5471 | 2025-10-17 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e304afde-a8a2-3637-b0fc-556a383684e5 | -2.7401 | -49.3927 | 2025-10-17 04:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7425c74f-6945-367a-a60b-2e2604983861 | -10.5136 | -43.4052 | 2025-10-17 04:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 4f508c90-a72f-37e6-8cc0-faca24646b44 | -14.3417 | -51.4663 | 2025-10-17 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 75498eee-1bc6-3243-b1de-51d7e5a8ffe4 | -11.3976 | -44.2167 | 2025-10-17 04:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 378bb3f9-c803-3ee8-b7b3-bb5186dca720 | -12.4264 | -51.3027 | 2025-10-17 04:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 125f29ec-0dd0-370a-bf93-80b85326c595 | -14.342 | -51.4449 | 2025-10-17 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 6c70d762-cd24-360c-9969-1f59d3190ed1 | -10.2939 | -44.0221 | 2025-10-17 04:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 0e318003-ed54-3573-a728-4491885c91d6 | -8.0977 | -45.428 | 2025-10-17 04:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ee9e1e07-1d7a-396e-84bf-b49349513d34 | -10.4941 | -43.4315 | 2025-10-17 04:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 43c8e253-e151-3e37-abf5-e06894a89ef2 | -14.361 | -51.4637 | 2025-10-17 04:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f66013d7-1d73-3708-849e-54310b2aefb5 | -14.342 | -51.4449 | 2025-10-17 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 158.6 |
| c3887ee6-961a-30fb-bffb-0802e73c830e | -9.1375 | -46.6485 | 2025-10-17 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 88bb3f98-82cb-3989-8fe6-b84710483b72 | -10.5132 | -43.4289 | 2025-10-17 04:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9d47b7f5-dee3-39bd-972a-fab9e699d6bb | -4.4059 | -43.4049 | 2025-10-17 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| eed78523-4f02-3ec3-a85b-b4c5cf16413c | -10.9472 | -49.782 | 2025-10-17 04:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9fb67fb7-9fa1-34db-bc94-0537290d34f8 | -14.3227 | -51.4475 | 2025-10-17 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a071eb92-2d7d-3f21-9731-578afa7a268d | -12.4455 | -51.3004 | 2025-10-17 04:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 57518d33-28db-32e8-a04f-e85620b351ce | -14.3614 | -51.4422 | 2025-10-17 04:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e060bcf9-5e5c-3b00-be3f-f75657a7b908 | -10.534 | -49.5471 | 2025-10-17 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0a069124-a1bc-3909-b2c7-f7684f3b5e98 | -10.9475 | -49.7605 | 2025-10-17 04:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6c5c932b-ec41-3b0c-a42d-d9986cba6884 | -10.2748 | -44.0247 | 2025-10-17 04:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| aad62371-1f80-3a3d-8c4f-9cb13fed7327 | -10.2939 | -44.0221 | 2025-10-17 04:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 157.6 |
| ef453351-3bec-376d-866e-67f773575c4d | -12.7866 | -44.8873 | 2025-10-17 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b2509403-482b-35f6-8fa4-c9cc7acd89ed | -10.2745 | -44.0481 | 2025-10-17 04:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1a7bb857-5b9f-336e-8040-d4eec754213c | -8.0788 | -45.4298 | 2025-10-17 04:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6827b752-2220-3580-8ae1-cdeb059cb558 | -10.2935 | -44.0455 | 2025-10-17 04:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 6e222673-03d4-37f3-b984-b9669f191cc5 | -14.3417 | -51.4663 | 2025-10-17 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 7460f1a0-6070-3646-82e3-a1676cc1645e | -8.389 | -46.2333 | 2025-10-17 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| b74e09da-28bc-37d7-9770-48f4232c0dfe | -12.426 | -51.324 | 2025-10-17 04:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 85620c77-7031-3e45-bf10-8a1ae88817e7 | -5.9095 | -44.7545 | 2025-10-17 04:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d02131a6-cb43-3f4a-8c82-8622c7204718 | -14.3424 | -51.4234 | 2025-10-17 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8c775aae-717c-3b2c-9628-59475f8831df | -12.4264 | -51.3027 | 2025-10-17 04:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 0251fc6e-d812-3fe6-bf88-def5eaf061da | -10.3126 | -44.043 | 2025-10-17 04:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 18d6d336-5ad0-3987-8945-ea4b9cb79775 | -2.8075 | -48.66376 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f099bb4-3ad8-3d81-8f68-3927907a3b7d | 1.73996 | -55.78108 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3813ca9b-bd15-3ed2-970c-4067524a51a6 | 1.01951 | -51.16076 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84e55272-c205-3969-b1db-779d2785dbbc | -2.29724 | -47.99376 | 2025-10-17 04:17:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09ef40c5-6f7a-3cbc-82b4-baccdefce0e3 | -3.327 | -42.7958 | 2025-10-17 04:17:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5e1a904-5c16-38ca-888e-2a53654a8040 | -3.88002 | -42.40837 | 2025-10-17 04:17:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 460fb9b5-2925-35b8-81e3-71cffecf3891 | -3.76575 | -41.71465 | 2025-10-17 04:17:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 379d2e80-4983-3892-8c02-be5841a0a03c | -3.32311 | -42.79881 | 2025-10-17 04:17:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b2a5881-1259-3fbe-b45d-0241900e1dff | -3.98469 | -42.09378 | 2025-10-17 04:17:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14bf9af2-76c7-38e9-b62c-9227d652c775 | -2.6899 | -48.46759 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d3392b0-a0ac-3a4e-b38e-c15493c9447b | 1.73413 | -55.78835 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f57ad4d8-c471-3f46-8730-a61543e28cd6 | 1.10063 | -51.15279 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44e22947-252d-3fd7-879f-518a0cb7d348 | -3.23907 | -45.98306 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 187b7e5f-1946-3ddf-a806-d86de67a6f43 | 1.01451 | -51.1615 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f28e1289-ef88-349e-8e23-2acfe1dc3637 | 1.77695 | -55.73711 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2002b1bf-f2d2-3194-b525-de7d7d806723 | -1.5182 | -51.62297 | 2025-10-17 04:17:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7f9447c-1c20-3101-9db2-4e20f86aa9aa | 0.33566 | -51.35214 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7644362-550b-3a45-ae8f-44ca0dceb1f5 | -3.97895 | -42.49427 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2e0de39e-05ec-3271-a682-1be9d0ac5006 | -3.98233 | -42.49479 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e5aef0f-e7d3-34fa-ab56-9870fcbe2de1 | -3.24142 | -45.96812 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 454023aa-8f5a-378c-9664-67cb010345ee | -3.23281 | -45.97823 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2219f2d-938c-354e-8e83-e6366d40db17 | -3.61073 | -41.58615 | 2025-10-17 04:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27b201e7-c8a9-36f4-b593-e4d707a5c080 | 1.04023 | -51.09219 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ef3aa62-6287-3c4a-89bc-dc06d9c29170 | 1.78186 | -55.90801 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a10f24f8-7045-316c-bd71-cc1714dfcfca | 1.72829 | -55.79551 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9d002c6d-fa33-364c-a1d9-4dc569f69e73 | -3.23516 | -45.96336 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a223a8b4-7b45-35bb-94b0-bbc230860196 | 1.83422 | -55.70353 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5f6a3dd0-8d30-3db3-920f-71a2dd674220 | 0.33156 | -51.35876 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f554ba6d-28e8-33c8-ab27-0610ab69f680 | -1.25478 | -49.03709 | 2025-10-17 04:17:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70ae78b3-79a2-3e99-9dfb-2f7766047440 | -3.24426 | -45.97237 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f97949a-8b2c-3fc7-9409-41b0f427c5d5 | -2.94687 | -47.31279 | 2025-10-17 04:17:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fac55ece-0bd8-34f5-a345-c736daaecef2 | -3.43574 | -42.4664 | 2025-10-17 04:17:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3804e84d-2b7d-37d4-a48e-996e577f659f | -2.96469 | -48.58721 | 2025-10-17 04:17:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5deec1ad-492e-3db9-957c-abeb326cf9d1 | 1.04521 | -51.09145 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb135bb4-05bf-397e-a80e-79e1d98157ff | 1.72342 | -55.80904 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2860d64c-bfc3-3134-a28c-ed45000b5a3e | 1.82308 | -55.70693 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 87840057-abdf-39c1-83ba-3a77b6d3d38c | -3.59204 | -42.84031 | 2025-10-17 04:17:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fe971ff-3c41-3692-bf61-40143c21e50c | 1.77789 | -55.74334 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3c1b111-c5f4-33e4-a1f5-ac346db8b712 | -4.57755 | -37.99664 | 2025-10-17 04:17:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4aff685b-9762-30c9-be92-c8fb58ac14b5 | -3.89307 | -42.56925 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99919bfb-1bcf-3e44-892b-76e82dee2e3e | -3.23457 | -45.96707 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c567847b-487a-3d65-9dfc-2982e2a970c5 | -3.77733 | -43.44408 | 2025-10-17 04:17:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 161e8d32-c6dd-35e0-94ca-1cbb9728ce25 | -3.84968 | -41.57326 | 2025-10-17 04:17:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e859b571-2d75-3845-87f0-13e465affef3 | 1.73495 | -55.78122 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 03730673-9708-317b-aca9-3b33a2dce077 | -2.64633 | -48.38653 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7c09d3a8-9e50-3f4e-b915-d2d373a1bf50 | 1.04762 | -51.20802 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a83a7ab-b391-34ca-8dee-afb0c17348b2 | 0.32655 | -51.35954 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1fa0038-e367-365a-af3b-0bbc21c26026 | -3.24025 | -45.97557 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc7d9036-ff58-3de4-af06-0f52132cb2aa | -3.24827 | -45.9692 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16416308-dcce-3dfb-b190-bb7f1a5b4020 | 1.02746 | -51.10867 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6681ae3e-d56b-3963-9a7e-3d5de58eb3e7 | 1.73679 | -55.79359 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c19d0b4c-d6ed-349f-b9c0-51f16b56e4d3 | 1.01977 | -51.15925 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 436fb6c2-8756-31fb-8fa4-bea3914e7676 | 1.85828 | -55.66447 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d357404-823b-356b-8954-19c6172c88f2 | -2.99104 | -44.3158 | 2025-10-17 04:17:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 102b8af9-5c39-3303-bfb8-b5ad32c46841 | -2.71107 | -49.41391 | 2025-10-17 04:17:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1964b737-7a0d-30bc-9da7-81b19d858975 | -2.7117 | -49.4101 | 2025-10-17 04:17:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e74a60b-23ed-3918-be8a-31dea2a3871d | -3.56224 | -40.52071 | 2025-10-17 04:17:00 | NOAA-21 | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 218377d4-8a49-385e-a456-635cd5d246f0 | -3.6621 | -42.25265 | 2025-10-17 04:17:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c602660-88de-3ee6-b698-4dee0e95a138 | 1.72246 | -55.80283 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 637fdcdb-2fc6-3855-b89b-f7708663046b | 1.83487 | -55.69299 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 677d5d06-d933-32e6-a440-4b5ef7d3cae9 | 1.77202 | -55.75042 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README35.md)
