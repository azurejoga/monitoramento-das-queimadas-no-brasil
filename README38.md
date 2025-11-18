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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a01295da-0af2-3e7b-b41c-740a6c1a45cc | -1.91402 | -48.79844 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92cb4adb-3834-3ed9-9187-15802d03acd9 | -2.33566 | -55.79923 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab249f81-2440-338e-8905-115b0137f8d1 | -6.70964 | -40.78964 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc0fa62d-3650-3f6b-8607-e8e8252f8428 | -2.9386 | -51.07136 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c457043f-6680-3d86-8480-e1cf1fe9788c | -4.759 | -45.77673 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59517baf-d5eb-3d09-a54f-c6492aff5560 | -2.45461 | -53.80532 | 2025-11-18 04:48:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a389108d-21e4-35c9-a981-88aa7a06e7f3 | -2.97867 | -51.07767 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed54c5fc-b6c9-32a3-ac08-f093416ea0eb | -6.44459 | -43.81332 | 2025-11-18 04:48:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93f38f79-5c69-3f7f-a84b-43d6faf4e8b1 | -4.1798 | -44.23991 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f0d60ea-58d9-3c0b-aa02-cee8ab149bb0 | -4.16503 | -46.83507 | 2025-11-18 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34dd12b2-822a-38dc-9ecd-e87fd8457994 | -5.46042 | -40.97536 | 2025-11-18 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea0582c8-0c11-3d73-b2d8-98eff547ec90 | -3.02487 | -47.83874 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 113a9f93-aa9a-3360-89da-5f662bd54bab | -2.85999 | -45.23456 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca7acb2c-29d0-3dd7-826f-66b5af6fc273 | -6.94165 | -39.62887 | 2025-11-18 04:48:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2759f4f4-85f0-31fa-ab5d-37cfc5b2e5b1 | -6.40265 | -42.32505 | 2025-11-18 04:48:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53ecc226-be08-309c-a79a-4d70fffc5022 | -2.53061 | -58.02354 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88299495-2087-324b-801f-267da9b5cc27 | -6.93845 | -39.62989 | 2025-11-18 04:48:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 708ac651-973d-37ef-b35d-bb1dcbe6f376 | -3.84774 | -51.06128 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77f69cba-8a23-33df-8cea-0c7bb6d04285 | -3.68601 | -50.54245 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c459ad7-fd64-3113-9c0c-b19dd0809cd1 | -3.24122 | -50.50761 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d199dbe-732d-3ad5-b983-7f3216ad6107 | -3.24987 | -50.68943 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79ab572d-2ad7-3d61-8c68-a790d5f515ae | -6.29137 | -43.80275 | 2025-11-18 04:48:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e4e8b3a-a770-3c8e-9eb8-ea91edf7737c | -3.25439 | -43.03569 | 2025-11-18 04:48:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 807dd32b-0419-3295-a8ba-16dfb0ac4dd8 | -6.21601 | -46.88384 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be3cb337-bb81-30b8-ac58-7d562c1d9b00 | -3.65509 | -50.22676 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58410c5c-377e-30f6-bb6e-275206f31dcf | -5.1878 | -46.07388 | 2025-11-18 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f16a4321-afaa-3d23-85ad-98a2c1bcd47d | -1.91682 | -48.8025 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7bce8f7-21ea-3568-b90b-db0a18d5ac37 | -4.48675 | -46.59565 | 2025-11-18 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a70539c5-082f-3612-85ca-ef7da05adc5e | -3.54646 | -51.42235 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a29a45-904d-3632-b554-5be87722de7f | -5.75554 | -48.90257 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58c3a9fe-5aa6-3d87-9611-c11753ae4068 | -3.1461 | -51.32324 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c3e0f1-306b-3fe9-9498-b4764c2c3075 | -3.12788 | -49.23251 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24e9763-a1c8-38bf-af49-2ef31036ef90 | -3.08694 | -51.2634 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 848e11be-190d-3cef-a396-18dfc2e69bc5 | -3.81353 | -51.34213 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 574b6136-9873-382f-bad2-8097cf4a6869 | -3.13802 | -49.89775 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f5e676a-8052-33c1-a3d8-e32ea694f700 | -3.27327 | -50.02505 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 751d264e-070c-3ae3-8bc9-d37c98e76240 | -4.23277 | -46.34475 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db1ac68d-5142-3c51-9639-395de69420c9 | -3.08177 | -51.09037 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48669b68-a35f-35cd-b5d1-f8df8054fefb | -3.48168 | -52.35494 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca4d8af0-47fe-3879-a99c-b8137731429f | -3.84884 | -51.05433 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e1369d-bd92-3407-84e4-f8db2e4e0314 | -5.42298 | -43.04777 | 2025-11-18 04:48:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdbb6019-48c5-396c-bad9-5fc24263c884 | -3.41856 | -50.35229 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 326707e2-b9a9-3ebe-ba88-90caced95f38 | -4.72748 | -46.37769 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f211ddc4-2164-31cb-9e8d-3f2b9e80fc12 | -4.23631 | -44.58732 | 2025-11-18 04:48:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a6aa181-84b3-35c7-a173-d57fdc8cb9b0 | -4.18546 | -44.23209 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 18c709ae-90d2-3e7c-b48b-cb6ee4b86727 | -3.24967 | -43.035 | 2025-11-18 04:48:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ca17f5d2-5242-33b2-b27f-ff835d8be6ea | -5.79338 | -43.99366 | 2025-11-18 04:48:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f43e2aeb-671f-383a-9c91-84e3ce15345a | -3.24232 | -50.50071 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c248874-cf0e-36c8-b07f-ff0d46967af2 | -3.23845 | -50.50364 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaa5c298-4b0b-3dc7-883e-10ba42d9233c | -4.70201 | -46.30994 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfe39c71-a5f8-3bcf-98f7-00df4ee73542 | -3.21413 | -50.1891 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8841b6b0-a445-3de6-b1ea-16a3fad068d3 | -3.60058 | -43.61012 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0207f44-9c48-3e66-8ba9-035743b977a8 | -4.70475 | -46.31343 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6449e441-56bc-3811-be50-2a2d0039200d | -1.34293 | -49.32632 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2a86ed1a-4a70-3bd9-bff9-acd42062a187 | -2.91911 | -47.84708 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c67e84-cc61-3cea-a396-a5d9a2fd46ec | -3.75432 | -50.94704 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84709492-03ce-3da1-9f49-c5e09647eff0 | -3.50803 | -51.31893 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1387feec-d0a6-3741-b7b0-f4ecd7ad8ad5 | -4.08892 | -51.05266 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4c6ee61-9cc5-3dfe-a3f6-2a5f95fa7ab1 | -3.67436 | -50.80962 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170b82c4-e92b-3756-92da-6a221235d358 | -2.80288 | -51.35316 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55310b0e-89ab-3d46-a397-c574858b0ea5 | -4.14361 | -46.34811 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7d9e71be-ce14-37c2-ae9b-95c13371d9db | -4.98031 | -41.85554 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50c91717-7ca2-3513-9c61-6a0071561e68 | -3.47316 | -50.81718 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2863fdd-ec94-35c0-b61b-1ea20cd891cf | -2.96139 | -51.03556 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea17e73b-380c-3515-b316-9f6e0f3429a4 | -2.89772 | -51.45859 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 367f078c-318e-3201-a6f8-e6ddf48ecf80 | -3.51396 | -50.2823 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45b5e579-62e4-3e31-9fd7-73b4e116c126 | -3.5837 | -43.59843 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 363361ff-5620-388f-b7cc-3732c2c6e736 | -3.04897 | -51.14615 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96554fd-a5ea-3878-b87c-6cde0403ba27 | -3.28246 | -52.42377 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68158f08-f3a1-31ee-8bfd-f2c99ffa2a9e | -2.94187 | -50.39023 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be8f5819-ebb4-351f-85eb-90ebfb241f38 | -3.14607 | -53.14043 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ee0fc3c-afe2-34af-9d46-c7efefd64aea | -3.26357 | -50.04841 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d18aa022-672f-3350-bb62-df26c7bd695a | -1.92018 | -48.80302 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 833bff70-f177-3713-802f-169222756ebb | -3.03113 | -44.47995 | 2025-11-18 04:48:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9f59e31-7a1f-33e1-86b8-a863bcd314bc | -3.72412 | -52.0633 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3da0f85-0b08-360d-a107-349d37c9f8fa | -3.51451 | -50.27885 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4829951e-9271-3a38-9bad-fe5991faef7f | -3.47225 | -46.06628 | 2025-11-18 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 739e95bf-06d4-3270-818b-544c58cd4391 | -4.97163 | -49.77042 | 2025-11-18 04:48:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb1bccb-e126-3074-a487-d7a9d77c13cb | -3.01099 | -51.34206 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4e42021-a87e-3817-beda-3dbadb9c9c91 | -4.1921 | -53.43391 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d824d936-a59a-3811-8aba-daae5408be4e | -3.60086 | -43.60751 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7b58343-efab-3abc-b674-e01cfa96e31b | -3.29993 | -50.07167 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 938d3522-752f-3ceb-a785-9e1c4b9943d6 | -3.61041 | -43.60686 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da26171f-985e-355b-9173-cf9cfdfe9749 | -0.8878 | -50.64589 | 2025-11-18 04:48:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc6339f-6137-37e5-86ec-1d6d382a3231 | -7.16986 | -40.65561 | 2025-11-18 04:48:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 003c00a2-921a-3f2e-ac81-1a8bddcd99ab | -2.81734 | -48.2496 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 676c3f80-4ce2-3f82-b580-ab2b7c561c41 | -3.94425 | -50.30069 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb58b4e4-fadb-3551-893b-1932aa57d94b | -3.13036 | -50.289 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e013d499-1e03-3cd8-9fea-1a5d2046a584 | -1.45719 | -53.42907 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a91448-9c77-304f-b557-ea2a4dff161f | -1.43377 | -48.90134 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a6b2991-a705-37ea-8a62-fcce210e724e | -4.64431 | -47.95071 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6ff980d0-4c13-321e-960b-4dbf2e99ea5a | -3.16378 | -50.16357 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 659ba270-3124-3d20-b3c2-77dc1fe2ecf3 | -4.70919 | -48.31903 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2fd9a5f-d00e-3be6-8590-bd1514cdc81f | -3.17163 | -46.60043 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b553eee-06ed-33c1-9f20-6602cc51621a | -4.18787 | -53.43739 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30b21a48-4974-3cef-bc4b-295bbb8c736b | -2.51275 | -47.81467 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50e235a8-77de-3af5-a8ad-ab00f0d513cc | -3.14368 | -52.17256 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901022ab-1712-3d6e-b086-9bf21678e89a | -1.42097 | -48.91734 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6252ca8c-81a0-3662-bee1-c6d20b8f705b | -2.9859 | -51.07522 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6630f057-f299-3c85-9c6e-f4a17a0a20fa | -5.36665 | -44.80992 | 2025-11-18 04:48:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README39.md)
