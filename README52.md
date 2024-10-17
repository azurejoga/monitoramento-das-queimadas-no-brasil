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
| 6de14d9b-2255-3645-a3bb-fffc9744422c | -9.55795 | -66.72468 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0588959-876e-3295-a9bc-ac87aad64b96 | -9.55785 | -66.72231 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a2b7926-4e79-38b6-9411-6609e7f4703c | -9.55718 | -66.72931 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d379ea-1d06-318e-ae64-a0b32de72611 | -9.55705 | -66.72693 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4305309c-1004-312e-8b4f-3c89211479a1 | -9.55493 | -66.71939 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66172d0e-bf0c-38ad-afc4-997107e791af | -9.55486 | -66.71703 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05358056-c1fb-3c82-a84f-b97342de5d19 | -9.55416 | -66.72403 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdfa3388-dddb-396f-91b1-562bb8453329 | -9.55407 | -66.72166 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53173126-a81f-36c4-98b0-dc9ade19c773 | -9.55339 | -66.72867 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 270117da-9111-3d12-bfb4-c4997909fbdd | -9.55327 | -66.7263 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66ed4c2e-cca5-32ce-a776-486ca2b4b8b9 | -10.2999 | -67.53529 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a769560f-3bf1-3d51-9b77-fba636af8324 | -10.10003 | -67.34676 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59c99ffc-2971-3818-914b-577191602d0e | -10.09928 | -67.34969 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d10c1594-e9bf-37aa-beef-6a3fbe32eedb | -10.09663 | -67.22289 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8848ca8d-789e-31ef-9cb2-54907e3e2277 | -10.09622 | -67.34406 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac014b75-bf3a-3094-853f-023aee0f6575 | -10.09614 | -67.34605 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7477fa03-66b5-3c1d-b145-42a5a849bff2 | -10.0958 | -67.22779 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d243d554-138e-397e-93ac-605f893ac201 | -10.09539 | -67.34896 | 2024-10-17 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 296c113f-c96a-3f3f-8bb7-59b7be2cb59b | -10.02262 | -66.92764 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fc3e14f-b348-359e-a3fc-95b329bdd578 | -10.01803 | -66.93163 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e80bfca7-558c-3ab7-82bf-b89c39e6ab8b | -9.15101 | -68.6778 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4735ecd6-e1b9-35f8-9a37-5c7b9150ab8d | -9.15029 | -68.68189 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4b19cda-124c-3b0e-91a6-3437b530aa3b | -8.88088 | -68.7533 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee44f3a-934d-3ba5-819d-2ee589e049d9 | -9.41235 | -67.84766 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a30348b8-88e3-3ee1-a1a0-453096f3de0a | -9.40829 | -67.84695 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a7b0312-939c-3100-880b-7210a31b3b8c | -9.39548 | -67.75248 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8201adb8-66e5-3571-96a1-3c6fe3aee0c7 | -9.37545 | -67.86724 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644b33bb-448a-37ba-b27c-7fc5a30798c3 | -9.16228 | -67.67843 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee2d0ba2-2f18-3e2c-b71e-f55ef40423fd | -9.07853 | -67.72994 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecdca844-c8e5-36af-871a-c689b1acd1b1 | -9.07448 | -67.72923 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a44c8a25-d6fc-31a9-a9d7-12b3a015d10d | -9.05685 | -67.83045 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f7f64d9-4143-3cb3-afce-6e3217cfdf01 | -9.05621 | -67.83409 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfc30576-9966-361a-8b9c-0790b3e6443e | -8.97693 | -67.49548 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f51d4d37-938e-33f5-afbf-2df7a01ca22f | -8.97263 | -67.35103 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55d80384-182d-30e6-a7bf-2e0e7962dc29 | -8.94429 | -67.61558 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ab08d1-c061-3d04-8401-04d3521e7ba6 | -9.30809 | -68.04472 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5fc773e-3bb1-377b-b90f-9da30a83ccdf | -9.30296 | -68.30514 | 2024-10-17 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41e196a5-8c65-30df-95f4-e24a81fc7ee4 | -9.27135 | -68.33617 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89927e85-6fb5-3e45-8095-ea9e6e8c2b15 | -9.04534 | -68.51402 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e3730bc-f796-38ca-91bf-042977e2b336 | -9.04463 | -68.51804 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ecec63f-2cf2-3d27-adab-91283720ada9 | -9.03045 | -68.12862 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8598b6d-79cb-3e5a-9189-85326a6c3db3 | -8.946 | -68.56295 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e2a1fbf-bcff-31b6-80ae-10d40cab1f7b | -8.941 | -68.56629 | 2024-10-17 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b93c51-8c20-340e-94b7-86ef56990fef | -9.76872 | -68.80561 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08b4aacc-29a9-32fa-bf0f-01b07cdc9a91 | -9.76799 | -68.80973 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87e93a64-ad44-3705-95bc-bd5a09a6e69d | -9.76442 | -68.80487 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835d7ec2-3c54-353e-bd08-bd4becfb6f0a | -9.63414 | -68.6665 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a44efcb-6a8b-3bb6-8418-b40ffcc67b83 | -9.63344 | -68.67053 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dfaabf3-b463-336e-a477-2ec9610d1740 | -9.62917 | -68.66979 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b8943de-809b-35ba-a63e-ede0837b1308 | -9.62278 | -68.68129 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85d5c8d2-5b3f-35b1-a354-3240f062420b | -9.61002 | -68.72949 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acec7af-98b0-3cb9-83c0-31ef3123932e | -9.58643 | -68.73797 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32ffdba2-fe2c-39b4-8df8-4a06fcd11190 | -9.52454 | -68.72773 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5a3a7ff-5280-3e52-926b-dd00d07aa4b3 | -9.44397 | -68.88383 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f19bc4-4185-345f-8c85-f84543525c6d | -9.41995 | -68.70583 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95e6c072-9441-3660-acb3-816335ea5408 | -9.3726 | -68.90308 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97143183-7e98-3166-9340-b7b98b2cb7aa | -9.3684 | -68.69666 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acb59ce6-24db-324d-ad7e-4b290d2a4338 | -9.36769 | -68.70078 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa829727-f8be-3f33-ae3e-e239adedadf8 | -9.34605 | -68.79871 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e95d5c9-c190-3fcf-acf4-d4c7aa1fae94 | -9.34555 | -68.67563 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a180be6c-f970-3421-b426-9bd639b60f25 | -10.63253 | -67.84261 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f597bb9-cf81-3f2b-bbf0-408d200214f5 | -10.62855 | -67.8419 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d7668d3-3966-3601-abbf-1f9a0586b9aa | -10.6274 | -67.72977 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e17d493-3655-36fb-9629-5be9b5a443d6 | -10.62726 | -67.82551 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afb68dd0-dea5-386f-93e6-b120332b38b2 | -10.62636 | -67.83071 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ab9823f-bbfb-36eb-9127-42bfda0b299c | -10.62433 | -67.72396 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8126c4b-72df-3d71-9f0e-3e9fd5dbc397 | -10.62329 | -67.82475 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a1d90e2-f401-3cc1-80f5-7bf305c34d99 | -10.62239 | -67.82999 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e65a71c5-b740-34e6-98b5-523f015e4991 | -10.62125 | -67.7182 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 989d9536-1091-3576-bd02-3803f05673cb | -10.62037 | -67.72329 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df422136-dea9-3b37-b9bf-5ffa8b5563fa | -10.61841 | -67.82928 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d4ac4e2-390a-3d9a-8fde-81b9be635c34 | -10.6166 | -67.83974 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb5ab632-0d7a-3eb0-8ca2-7c820c1e5aaf | -10.59923 | -67.86888 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 64e03abb-4e92-37ba-a3b3-09e6a3c61b1f | -10.58374 | -67.76952 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b9c10656-992a-3b2d-9534-2c4a1c8a81fe | -10.58032 | -67.68295 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1665f0-5774-3bae-8331-9399b0e8cd2a | -10.57978 | -67.76878 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9aa3be6a-9899-3a8e-b678-bd2b2bee58da | -10.57945 | -67.68809 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be594932-898e-3631-97d2-76b3d59f5774 | -10.57834 | -67.68418 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66268785-88ed-3572-a209-50cac912eb43 | -10.57581 | -67.7681 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47e46c70-0308-3f9a-a0ab-2ff825ab1057 | -10.5755 | -67.68741 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce38d19c-dcc8-357b-b4d9-05f296f8a792 | -10.57439 | -67.76639 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 292f12e6-f449-3d26-9dae-a3cbf7c0e74b | -10.55674 | -67.77404 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38b8caed-512b-39b2-8c82-f1b58f88cbbe | -10.52315 | -67.82677 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5761d7-7f70-3cdd-b26a-5e2a5af1c7e2 | -10.52005 | -67.82088 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd351198-a31a-3400-9e5b-4ad84bb9fed0 | -10.51607 | -67.82016 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d90abcc1-69dd-36e4-b348-4ee43672ae59 | -10.49066 | -67.64404 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2ab11bb-3b89-3f65-8a1f-bb778d020682 | -10.48917 | -67.64578 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a68b3b90-4803-36ce-a51c-d1d977f8a324 | -10.46694 | -67.88984 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ae388f-02ca-37b2-a42c-36d5a1fdc4b4 | -10.45078 | -67.84096 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 587f3ebe-ef85-3dc2-9dde-ff91c32eea0e | -10.44965 | -67.83892 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb9a7ee9-dd53-3935-b2cd-c10a5cbbd7a1 | -10.42558 | -67.90791 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ff77b5-ba18-3e0d-bec4-92a440a12349 | -10.42336 | -67.89667 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7280a2d-5580-38c8-aa87-a4d7f4d245fe | -10.42277 | -67.90018 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77bb6471-5922-3235-aab6-35ce686bb55b | -10.4071 | -67.91927 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9af328c-51bf-360c-967b-c1aa18f95312 | -10.38946 | -67.90155 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a26ea61-c901-3e62-bf36-35168d7490f0 | -10.38606 | -67.89731 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323d76c3-1f39-3690-994e-4f338240e49b | -10.38545 | -67.90083 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ffb9d9f-be8a-3ba4-82c4-b2fc37b06c43 | -9.86993 | -68.77184 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d839e91a-3d26-3056-a894-9279f88d8584 | -9.86922 | -68.77586 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e43cb9-031b-3a0d-89f2-0da53d8c72d3 | -10.79447 | -68.56294 | 2024-10-17 05:29:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README53.md)
