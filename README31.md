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
| a90e5f07-6536-3933-873d-177911055048 | -1.0731 | -53.63002 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26cff8ec-262c-35e4-8846-c2f99d0e9660 | -4.04053 | -46.8343 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf36c46a-1860-3498-bea1-03c01795e7b7 | -3.12683 | -45.97953 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2221f254-5f5c-34a4-9b03-23de3ba23756 | -3.89863 | -46.67179 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22f0dac8-7c1b-39eb-b0c1-ef4470eb31ac | -3.78517 | -46.70113 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94d94507-db91-37be-b21a-94dcc48d970c | -1.43363 | -55.24739 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a6cf42-c7c7-3229-abbc-63bdf0705c39 | -2.96043 | -50.57406 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3a0cca29-5951-3282-82e1-0ff6415b8d08 | -4.47874 | -44.5811 | 2024-12-01 04:21:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbe3adb3-1e87-36be-a3da-836b4d1b004b | -3.27408 | -50.2046 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05ecf15a-6470-3093-8b4c-c24ae9739eac | -3.01578 | -51.79117 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2de883a-f8b5-37ae-8e85-04c0e60211f5 | -4.10951 | -46.11294 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb9695b7-e2e2-3a99-8f48-26464b5f3885 | -1.80227 | -46.63029 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e00755f-64fa-3628-bdfd-ce854e4b901a | -2.48319 | -45.44672 | 2024-12-01 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9258c942-6e0b-3dcc-bfcb-4ee875bdb665 | -3.11924 | -51.312 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5bac90c5-b560-3ea0-9388-c1b7bb2ac0c4 | -1.53226 | -52.66246 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8df8f50-b8c8-3e37-aad1-60239c92d41a | -3.76789 | -46.51947 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e1b1034-3c3c-3260-a358-ded7ea0f991b | -2.59278 | -53.98362 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20003119-9638-36f0-a7ed-80d09ba7aac6 | -4.39277 | -45.90539 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 735b17dd-89d9-3dbc-a72b-ecd15087948e | -3.99859 | -44.75975 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 8177a77d-92ef-3f4c-a610-6035e69e5756 | -2.63581 | -46.8844 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7def392-d599-3d19-a69c-4f4efd29ff27 | -1.26271 | -47.50651 | 2024-12-01 04:21:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6964beed-cd2a-3c8d-90b9-f9edb6594d7a | -4.31281 | -45.09969 | 2024-12-01 04:21:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c45b63d1-d611-3075-a59b-99ea0d2e6c3d | -3.99352 | -46.64733 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36b2d119-9089-355b-b3e3-9c788dd9dcdb | -1.70275 | -52.4678 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f231d24-2bd0-344a-bed3-d486b23079e5 | -1.24695 | -54.54841 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2fce0bb-1213-3a9f-b4db-6ae4b14c6fd6 | -3.24235 | -45.37584 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 038ca207-4558-3dc6-ab6d-5e36b71fefc9 | -2.75214 | -51.75211 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4da2e472-d512-3dfe-a3e4-a912a7e2f834 | -3.41658 | -50.23853 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e00246b6-f443-315c-8470-80de45a38a1f | -3.1768 | -53.63752 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b891d7a3-f63f-3b88-84a7-cc4ccd30742c | -3.90924 | -42.42396 | 2024-12-01 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8467d26f-a8c9-3e3b-b075-1a5374f5b52b | -1.69785 | -52.64 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 816f9468-17ba-3d67-b078-98c5f550245c | -3.4014 | -50.66397 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0378ea9a-5709-3c14-bc2c-6c10643c0dd0 | -1.26727 | -54.55124 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4347543-db60-3d30-a48f-c55d00b3230c | -1.26635 | -51.75977 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bf3cba40-f4e1-355d-991f-f3b4b32e0dd3 | -1.07653 | -53.63213 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feeede0d-33d9-3422-ac87-2eae472a93b5 | -3.05698 | -51.06012 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2acefac3-d153-3151-95e6-b05cf621d8e1 | -3.42576 | -49.99523 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cca7217-7c05-3fb4-9ba1-06c24ecd26d8 | -2.47245 | -46.56575 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0470ea00-dcce-3ed0-9078-bedd80c9c33b | 0.93833 | -50.74842 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43528371-d70f-352e-aef9-849614a57f02 | -3.09874 | -50.3589 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1815270e-f922-3f14-8725-fb8016434fe1 | -1.49146 | -52.6496 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d851dd8-d16b-3160-862c-40f2bf175f1c | -1.97343 | -46.4635 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d958db5-80dd-3596-b2e3-6590ae5d0967 | -3.14346 | -53.83741 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8396ac3c-f148-3249-ae62-a2afe53b6da1 | -3.98028 | -46.64134 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442c9b45-b585-3737-8bc1-17381f1083b9 | -1.25365 | -54.54481 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efacb481-a152-33c9-aced-de9f8c1ab5ca | -2.87074 | -46.79834 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f171eca6-4bac-3391-8e1b-5fa72c182f77 | -3.12626 | -45.98318 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d818d99-b4f0-30cb-aca6-6939bdb7813e | -2.60943 | -51.8131 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06a968ab-4087-34f2-b59d-2c1acce644f7 | -3.69348 | -47.12017 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111e8c87-fc87-3c90-81bf-c54869b785ed | -1.61038 | -46.23075 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3876c990-d732-305b-b31f-84d40a1093f2 | -3.99232 | -46.65489 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a3ad746-1418-3241-8d07-be9c6078962a | -1.72374 | -52.48181 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70283eb6-4713-3f7b-8714-d4ae9979bea0 | -3.31463 | -50.14483 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ef5c853-d331-35e1-9d6b-8d8356eaade5 | -3.21369 | -53.12452 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4f25e5d2-27b6-36b1-9aca-9155837fe16a | -3.10309 | -50.35961 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a8f6fae-9103-33a4-9f6f-691aa9093c74 | -3.05725 | -45.08046 | 2024-12-01 04:21:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcefd485-5460-303b-89a4-3a0250292824 | -4.69573 | -42.39547 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c742fe83-f089-39cb-9f23-8d8da76b077d | -2.33007 | -50.6712 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc616967-4d20-3687-809f-2013fd241e44 | -2.71713 | -46.12809 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d549709-ee33-3eb4-a0d7-bd50e45ae583 | 1.15501 | -55.98747 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ce2bcb82-afcf-3be1-893c-24222c06657f | -3.68036 | -44.70618 | 2024-12-01 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68edbe74-f0c5-3de4-8b04-91b0706b2d78 | -3.79335 | -46.69447 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e6cd35-3563-39d7-9b80-f3439f717b04 | -2.56183 | -46.40586 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb0388b1-0cec-3681-b4d6-8133224acfd9 | 1.14919 | -55.99441 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| dafe6dfb-4971-3556-bd1b-6bc1108159c7 | -4.09235 | -44.85567 | 2024-12-01 04:21:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cc180ec-d317-3107-99c9-1a7dc3b27779 | -2.33456 | -50.67193 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85ea85e0-278e-359d-9c53-3da3c52068c6 | -2.7251 | -46.23282 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac2b7015-6783-3bb7-9893-bf071e57104a | -3.26415 | -50.21134 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83b48d72-0157-33ee-9d6e-f21d174c1cca | -2.81001 | -53.05499 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6c84ae9-8567-3c28-a31d-0082b7374213 | -2.65991 | -51.87059 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f312da34-013f-3d2f-b404-46f743047d44 | -3.90754 | -42.4123 | 2024-12-01 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e19a0fdb-65fa-3f47-8ac4-9407917c5464 | -3.26077 | -50.05031 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| edca9082-163d-32e7-9260-da6705b65f70 | -4.07494 | -46.8201 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1369d21-8c40-377c-b2f1-1cd2825e6a26 | -2.26129 | -45.51859 | 2024-12-01 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6094fdb0-54f5-34d2-918d-ed71806304b0 | -4.68313 | -42.36269 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd949d42-0912-3752-873e-4cba766d29df | -1.50045 | -54.9496 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe26c55f-c5bb-3dd0-b2c2-b00738f86011 | -1.63918 | -53.86591 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb6132e1-9ad9-3e40-bd6a-4d840b7b6dbc | 0.93793 | -50.75051 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb64981f-1e60-3009-b795-7443e43e9536 | -3.20838 | -53.12309 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38ea440d-2cb0-3d9c-969c-74a52c292b44 | -1.24128 | -46.0266 | 2024-12-01 04:21:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 475775be-fae7-36b9-a7e4-b3aa311b358f | -3.3432 | -50.74587 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b083f47-aa2f-3f9b-9b79-5fe30d184c72 | -2.92304 | -54.26776 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19944b13-6cb1-314e-914b-d9f85bb8394e | -3.35178 | -49.91643 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8df700f6-feaa-3259-b0b5-ea9ebe55d5d7 | -3.46915 | -50.26779 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 15de5de8-2654-3c15-bb1f-9315b37763dd | -2.99981 | -51.06547 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7227653c-4cfc-3fdc-b5ba-75d30ffb7da9 | -3.07287 | -50.99144 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e0024310-4c61-3650-bc2d-d4c42fbb6c4a | -3.86013 | -47.05227 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62b4dd97-6f78-3350-a635-79812981e60b | -4.09248 | -46.13275 | 2024-12-01 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6cb7d66-372b-38c7-b32a-af355b299f47 | -3.84564 | -46.51962 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f03b0003-7ad0-3dc7-8535-a22eaf026705 | -2.83367 | -54.09271 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8db3a26a-6659-34ea-acb3-46a36a8bfe16 | -2.97137 | -53.29071 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af944e2b-9398-3b44-b3eb-ce51145c30b2 | -2.96859 | -48.03754 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05891810-5f3e-32d9-a67f-79be9c837332 | -4.34926 | -45.92823 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4be13102-e65a-3299-83ae-95888bdb2dea | -3.79366 | -48.09113 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ae35991-bf32-3ed2-b776-366404073e16 | -3.8009 | -46.6917 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bbb8c6d-4100-308c-96c7-1f8194d6ce02 | -3.03316 | -51.54092 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f537a98e-dab2-3449-8729-231e5e21faa3 | -1.98488 | -52.89522 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cecb6c5-6b4b-3f84-82a2-c483d7cddfc9 | -1.43713 | -53.40046 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83171755-c8a9-34d7-9887-6dfed5de3d8a | -2.52589 | -54.07271 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba3a6b96-0cbe-39d3-bcc2-2c630907a322 | -2.86775 | -53.99366 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
