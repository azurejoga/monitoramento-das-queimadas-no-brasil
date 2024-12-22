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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df2935f7-3891-3e59-9357-4162beac2027 | -1.15271 | -53.59428 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8d3327b-237b-3439-967e-6b420fe879cd | -1.29321 | -53.12522 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| dfbe07f9-f2e4-3782-bb91-a15bc3cf4773 | -1.71091 | -52.57256 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ffc6b549-9337-307c-a92d-3ce9514eb795 | -1.17959 | -52.55185 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9a4585f5-91c7-3450-88ae-ab952fa09838 | -1.71298 | -52.58703 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5f7b8fee-172e-3675-8f4a-f1c77108e10b | -3.59162 | -55.43727 | 2024-12-22 01:24:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dd9ac2fe-e354-3791-b1b2-3d1deed78589 | -1.29616 | -53.119 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8b74744c-e111-3b7c-a9a6-1c196c1aba5d | -2.04809 | -52.11656 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 0f846609-577b-3736-9edd-5c252b9a6b6a | -3.94713 | -54.62854 | 2024-12-22 01:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e4a691ee-1c99-3674-b498-6f42f962f4e3 | -2.2228 | -53.79654 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9f810734-1d45-3d40-8da6-66409dc7dfbc | -1.15448 | -53.60704 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60e24eb9-a7df-3b6a-93b4-30e18d604dac | -3.55145 | -51.07482 | 2024-12-22 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f15b43d9-d27e-3b28-9755-b336f358c20f | -1.28949 | -53.09827 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dfe12a86-74aa-3f4c-887e-d27de846bc5d | -2.04591 | -52.10112 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a223674c-1aed-3989-889e-943fa8153fd9 | -2.45033 | -51.80132 | 2024-12-22 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 8e4aca12-67f3-32e2-9f0f-a6cb5858313d | -2.50891 | -51.8189 | 2024-12-22 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7a057253-7345-3970-9b95-7c90c8452525 | -2.97482 | -48.08256 | 2024-12-22 01:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| bd62d224-70bb-3a91-8c8f-64b463a2db04 | -1.37092 | -53.68878 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 632a0a3e-4ac7-365d-ac1c-3581c1ae13e6 | -1.36902 | -53.69526 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 82a29362-a7b6-33e8-8fb6-883610b68aa7 | -1.37254 | -53.70049 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| ab0c7149-0e73-3145-8bad-2100530fd79c | 1.06765 | -59.41045 | 2024-12-22 01:24:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 06de53de-85d5-366f-a9d1-ff74e3be0652 | -1.09311 | -53.67285 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ece53c18-d0e1-3898-a073-b7f2b3036b82 | -2.51879 | -54.22506 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1887a33a-c3f8-3716-a622-6d510fd90881 | -2.44801 | -51.78512 | 2024-12-22 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0b7e8fbf-4056-3214-8eed-0586001d5254 | -2.66302 | -54.86869 | 2024-12-22 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 57d81443-f26c-349c-af0b-6565ce2b2fc6 | -2.03657 | -52.11829 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 462ea217-a444-366c-b623-c3a5c133af0f | -1.36222 | -53.70188 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 27810dba-9949-3d3c-8a81-f9f944bc2576 | -1.72208 | -52.57093 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4ed3c33b-f1b6-3011-9314-73535f1d0807 | -1.29136 | -53.11182 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da26a84c-64c2-30e1-9d74-8af2081f9e89 | -2.67898 | -54.84589 | 2024-12-22 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 6130105c-49e7-3567-99a7-af502d9abea1 | -1.29809 | -53.13227 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c54e9144-cf2f-3055-8f46-e48b878ec678 | -3.94854 | -54.63847 | 2024-12-22 01:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 359e887b-15dc-3cd1-a2c0-f5122b9bf41f | -2.03437 | -52.10279 | 2024-12-22 01:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 79486beb-51af-32d7-befe-bfb119e8db82 | -1.19088 | -52.55021 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 592e0789-b298-3611-a343-f5f974d4e6d9 | -2.66445 | -54.8787 | 2024-12-22 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6363f9fa-9d13-3dce-839d-867e2108ef1d | 0.64091 | -60.30383 | 2024-12-22 01:24:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 456bfde1-67fc-315a-9b00-fc6fa988aee7 | -2.82292 | -52.86153 | 2024-12-22 01:24:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| adef66bb-ae69-31d6-be2f-5db021255886 | -2.68839 | -54.84456 | 2024-12-22 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| bac6702e-340d-33da-8af9-7f03f1675fe9 | -1.36056 | -53.68994 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 74c9208c-9554-3bba-ada2-fe004941543c | -1.36733 | -53.68357 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| afa8aa18-9e1c-3dba-9473-3e993d76e852 | -2.43626 | -51.78686 | 2024-12-22 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 544c2a98-5590-3eb5-8be4-5bb4934bc727 | -1.37074 | -53.7071 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| c37cd71a-2c3b-3753-a1e8-0e99777cc684 | -2.23292 | -53.79514 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0937217c-3992-3733-b834-ee9f320ddff5 | -2.22448 | -53.80814 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0022b649-218e-386c-9764-c3a94e0d8891 | -4.03169 | -50.05706 | 2024-12-22 01:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0df4a8c4-ec3b-36c1-a1b5-4ba0642f64b4 | -2.51126 | -51.83491 | 2024-12-22 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a7eea666-9c2f-37af-b699-0f143d5961b3 | -2.6898 | -54.85456 | 2024-12-22 01:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b2f5dfbf-5704-39c0-b58a-f0cc1953ddac | -3.09722 | -54.54753 | 2024-12-22 01:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69dc5279-f084-3f87-89af-e365a40bdc97 | 1.93222 | -60.66352 | 2024-12-22 01:24:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14ea3527-d011-3acb-909a-40fa14e3534c | -1.2942 | -53.1055 | 2024-12-22 01:24:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 05f1be4e-a9a4-3f4b-bfdb-24f38d2f65b7 | -2.12312 | -50.70692 | 2024-12-22 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b18e9bca-1c55-3635-acbd-c88000915883 | -2.14516 | -53.45881 | 2024-12-22 01:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bfa8fcbe-b508-35f3-a6d6-06e3984e9e6a | -7.51458 | -37.77629 | 2024-12-22 03:10:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 670b5dbd-d3c7-328e-8ab6-961843d4820d | -5.42861 | -36.73544 | 2024-12-22 03:10:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8eb5e093-3309-3e00-8655-8cfc036378de | -7.5152 | -37.77863 | 2024-12-22 03:10:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f58709c9-d771-3f06-9bac-7d887bd452da | -7.89731 | -35.2503 | 2024-12-22 03:10:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 73db01a1-bf5e-3ee9-931d-d422bdd49b54 | -7.50942 | -37.77802 | 2024-12-22 03:10:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d9866f8-e906-31e3-ae15-f1bafe5c6013 | -6.06105 | -35.27744 | 2024-12-22 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e42564d0-9ba0-37cb-b54b-e6038ec119a9 | -7.51383 | -37.78049 | 2024-12-22 03:10:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3286d30e-dc9d-36a2-bae2-7fa87987db2d | -12.44456 | -41.44382 | 2024-12-22 03:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 201031ee-7393-3ee4-8ed6-ba319ccbfa04 | -12.44664 | -41.43374 | 2024-12-22 03:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b0421a99-1902-3c50-9381-18f733abd7e0 | -12.43903 | -41.43753 | 2024-12-22 03:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9933794b-8c29-3769-8967-0b82605365fe | -8.47522 | -41.82507 | 2024-12-22 03:12:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c6ac0f8d-0394-3cbd-921c-b791ab4b1fb6 | -8.4743 | -41.81953 | 2024-12-22 03:12:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 52c7bb8a-0251-3e4b-b5d7-c29a77d2618f | -8.47666 | -41.81785 | 2024-12-22 03:12:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c910c4ac-84fd-3c50-b8d4-efc3a0152153 | -12.43643 | -41.4501 | 2024-12-22 03:12:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a0034f50-1103-33b3-951a-9d304cb564b4 | -8.48141 | -41.82113 | 2024-12-22 03:12:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a3aeef9b-e553-329c-8c79-385dfcebefaf | -12.4379 | -41.44299 | 2024-12-22 03:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 00c1ba93-f6aa-3d56-bbf9-34cc3192571a | -12.44563 | -41.43866 | 2024-12-22 03:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| eb065f8f-0c00-38fe-8976-0961f4f3e598 | -13.40408 | -42.31838 | 2024-12-22 03:14:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1a145e2c-4256-391f-98f1-9427c3b7d199 | -17.73799 | -39.52761 | 2024-12-22 03:14:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b1c3862b-825e-37b8-bc85-2eabc61c80c0 | -13.39735 | -42.31672 | 2024-12-22 03:14:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a4d9ef50-7d6c-3c98-af08-9ffd6fe2accd | -13.39596 | -42.32316 | 2024-12-22 03:14:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f32b720-d766-355e-b2bf-75ae6c7d621b | -13.40271 | -42.32473 | 2024-12-22 03:14:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f202c608-1cb5-3193-bab2-ceacf7de922c | -2.04936 | -45.48699 | 2024-12-22 03:32:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7933d3e2-e41f-3afb-b289-17925c10923d | -2.56386 | -45.96324 | 2024-12-22 03:32:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66bb93f6-c7d3-3a14-bdf5-7380ca9f7dd8 | -3.27225 | -45.50003 | 2024-12-22 03:32:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f943a5c-82f5-3656-9859-a103a0e1fce2 | -2.75264 | -45.56462 | 2024-12-22 03:32:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34328789-2f7a-3b8a-8a78-bfdf01c33c28 | -3.27517 | -45.50286 | 2024-12-22 03:32:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce770a32-b800-3504-8100-73e1972b0167 | -1.93796 | -45.64661 | 2024-12-22 03:32:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b55f5673-41a6-30ba-951d-0aec0c0f2777 | -2.75941 | -45.56573 | 2024-12-22 03:32:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37def43c-cfe0-36d6-bb9e-84718ca93ee4 | -2.05037 | -45.48094 | 2024-12-22 03:32:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc5d42c9-2e79-3d13-8d2a-b57fbb78aca0 | -2.56378 | -45.96824 | 2024-12-22 03:32:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7e2e36d-f4b9-342f-aaa5-4fc319465ff4 | -1.93907 | -45.64017 | 2024-12-22 03:32:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d91ed07b-cdc5-367a-849e-699b4a2231c4 | -3.40812 | -44.12435 | 2024-12-22 03:32:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 041ef032-13fa-3439-9680-bfbcf77780fc | -2.75161 | -45.57066 | 2024-12-22 03:32:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 132fbf7e-c1ff-3401-8e48-21d816af1466 | -2.56487 | -45.9617 | 2024-12-22 03:32:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d72781ac-648e-35ad-88ca-556451b28642 | -6.00183 | -45.41147 | 2024-12-22 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74d23c6d-abeb-3090-a8ee-e261215dbaa5 | -9.0524 | -38.32088 | 2024-12-22 03:34:00 | NOAA-20 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c8c55a4-bc8a-3069-ba31-287c6f4d4c4b | -3.94522 | -46.41818 | 2024-12-22 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e86f4f5d-79e7-3e02-aa25-a4120fd53d1f | -6.0604 | -35.27631 | 2024-12-22 03:34:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7ddf6928-ef08-38ec-89de-965f6221cd01 | -8.4768 | -41.82657 | 2024-12-22 03:34:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 13449cab-210b-3477-ab2a-a9093e3e9c87 | -4.81882 | -44.41463 | 2024-12-22 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 697c84e6-82cc-32a5-b2b7-b1b53b2474a8 | -4.05639 | -44.05395 | 2024-12-22 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7c4b162-c420-335d-9400-d568ea9a646d | -3.94454 | -46.4136 | 2024-12-22 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7b80859-3542-321b-96b9-bf71117b086a | -6.06381 | -35.27687 | 2024-12-22 03:34:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 13a779c3-b2fe-33ad-b777-442e72e6eff0 | -8.12333 | -38.76567 | 2024-12-22 03:34:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c7b52815-3d54-3735-a06a-4533fb31fc9c | -7.37801 | -34.88621 | 2024-12-22 03:34:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 82c47a8e-37e0-30a4-aa9e-3e4f7b33f6c4 | -5.22925 | -44.33944 | 2024-12-22 03:34:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd3fa594-e1de-3580-b564-7b29b4b7e960 | -3.99785 | -46.5606 | 2024-12-22 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
