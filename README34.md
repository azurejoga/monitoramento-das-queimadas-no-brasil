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
| 3d042c60-c325-3dc2-9384-365ab807a184 | -3.5381 | -65.0229 | 2024-10-07 02:15:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b27554b2-fe77-3ea6-ad1c-2eb330d05012 | -4.2728 | -43.7601 | 2024-10-07 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b8b84900-3f4b-3515-929b-40ad4eea3337 | -4.2729 | -43.737 | 2024-10-07 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 11f6ecf9-ee94-3240-aa30-e9926db0d2f3 | -4.2731 | -43.7139 | 2024-10-07 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f95dcf9c-7177-36e7-a9f3-43717f61a611 | -4.2916 | -43.736 | 2024-10-07 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4467d5c3-3318-3c45-a607-41351a139663 | -9.5152 | -40.331 | 2024-10-07 02:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 151.0 |
| 4b96a09b-30ac-3f25-b8e7-0a74a67ccd77 | -9.5343 | -40.3282 | 2024-10-07 02:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 170.0 |
| 659315ff-e1cb-3150-8983-7d2eec7dd3e2 | -10.8754 | -63.9169 | 2024-10-07 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ce899495-2581-3d14-9b9f-ec42397912f2 | -10.8755 | -63.8979 | 2024-10-07 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 61263906-78ea-37c6-8ea9-338d7493a18b | -11.7566 | -44.4897 | 2024-10-07 02:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 2f257c13-d7a6-3615-9021-9a7b182b33a2 | -15.0422 | -51.24 | 2024-10-07 02:16:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 112.5 |
| bfab9582-f53f-3e73-888c-86f7873fa976 | -16.5462 | -57.7344 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 65c76c11-d2bd-3c95-8ce3-fae88f4a7bd2 | -16.5267 | -57.7365 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 9e96f42b-5355-3814-a399-de8375751032 | -16.5075 | -57.7183 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| dca3e882-9911-3723-a408-246225f453ae | -16.4948 | -57.2713 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 419caa23-125c-3569-9fb7-b50a4a2bae69 | -16.4164 | -57.3006 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 96127168-4c62-33cc-b095-705fbfe6f490 | -16.4167 | -57.2802 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 8185b4ff-368a-3af8-a3b7-fd354d21fa5f | -16.4362 | -57.278 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| aa740450-2728-31e2-b854-a47746ed6dcb | -16.475 | -57.294 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 71e9b81d-4428-3cad-8ed0-79226d9558ab | -16.527 | -57.7161 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| ff571dc6-f44f-300d-b490-55537dd1f789 | -16.4753 | -57.2735 | 2024-10-07 02:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 80c9375c-114c-3e7d-bc78-f98c5489e724 | -16.6332 | -57.1533 | 2024-10-07 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| a2de51eb-21b1-3868-9a54-47a4e161d5fe | -16.614 | -57.135 | 2024-10-07 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 661775dc-94ba-324a-af6e-64ac74f44eb6 | -16.6136 | -57.1555 | 2024-10-07 02:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 4f245ea2-09c9-3dc8-a1df-9b5a42d1c919 | -16.9375 | -57.6904 | 2024-10-07 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 6ad3570c-81b6-30af-881f-008a1c6d53d2 | -16.9179 | -57.6926 | 2024-10-07 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| b0da5b91-a6fa-30eb-861c-b20a6a598ea6 | -17.0982 | -57.4267 | 2024-10-07 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 473d5072-173a-3998-aea2-8c8af591458b | -17.0881 | -56.8328 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.7 |
| 58b087f2-2d5b-37b9-acbb-49a6b5c2568f | -17.0688 | -56.8145 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 5747be21-bcc6-39eb-96c9-6784e54e0ccc | -17.0685 | -56.8352 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 6ee06f76-7ecb-3f06-9157-3037d1e0902a | -17.012 | -56.698 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 6f52695e-e772-39a3-b4c3-61608fea0e9f | -17.0116 | -56.7186 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| dabc377d-9b10-3383-91cc-4b58f91d4ca1 | -16.992 | -56.721 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 51b02a3b-22fa-37df-b473-0424fa4cd26d | -17.1274 | -56.828 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 5bf37410-f02d-3043-ace1-e8e2f76ee027 | -17.1182 | -57.4039 | 2024-10-07 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 79bbdf6d-ecda-3ff5-abb7-1d940b12d3ca | -17.1178 | -57.4244 | 2024-10-07 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 2a3025e0-da9e-3557-a22b-a6ba00069436 | -17.1078 | -56.8304 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.8 |
| 3154f842-e01a-3ba1-8dda-348c5d111888 | -17.1074 | -56.851 | 2024-10-07 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| d557d80d-99ec-3c6d-83f1-48a37452fdf9 | -17.0985 | -57.4062 | 2024-10-07 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.2 |
| db2308e0-ef15-3aa0-a620-5a3ad757ccf3 | -17.1584 | -57.3377 | 2024-10-07 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 9b1edb15-2038-30c7-895f-486bcdbca3d9 | -17.1581 | -57.3582 | 2024-10-07 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 2586c6e3-1bf7-33c6-8641-a7d677df2050 | -17.1571 | -57.4198 | 2024-10-07 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 9c59008a-149d-3a68-9e74-c7a9fb480ade | -17.1375 | -57.4221 | 2024-10-07 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 69c5f4a2-e48d-34fa-b5c0-acefded60ea6 | -17.6283 | -53.088 | 2024-10-07 02:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f985e185-775f-38e4-bf7f-5cb40cd2e325 | -17.6477 | -53.1064 | 2024-10-07 02:16:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 4a420f8c-0875-316c-8576-eaffd9b0be45 | -17.6481 | -53.0849 | 2024-10-07 02:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| ad7db67a-625c-3c95-b825-26b47f7f498d | -17.6081 | -53.1125 | 2024-10-07 02:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8d0a66b2-867d-3776-b860-1a1bd80c91a4 | -17.6274 | -53.1309 | 2024-10-07 02:16:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7ba38c22-9d49-305b-b0f8-adad9869304e | -17.6279 | -53.1094 | 2024-10-07 02:16:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 832edc9a-d065-3193-9470-fa3fb6a98d82 | -18.4518 | -53.5165 | 2024-10-07 02:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1be811f1-ecaf-3c42-8753-5d2a03b3aeaf | -18.4523 | -53.495 | 2024-10-07 02:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 3072a2ea-86c1-3588-a24c-aea3d3eb0359 | -18.4718 | -53.5134 | 2024-10-07 02:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 150.8 |
| f8160dc2-a328-332c-a890-7995b0c06183 | -18.4722 | -53.4919 | 2024-10-07 02:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3189bfac-d1fd-3d5a-80e1-4c9c16aa8d2a | -18.659 | -57.2552 | 2024-10-07 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 70dc5357-a4d3-30cd-bab0-9d9ddeecf3de | -18.718 | -57.289 | 2024-10-07 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 319ee829-5fe6-33bc-84d7-162fcffe0b83 | -19.8318 | -42.3542 | 2024-10-07 02:16:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 2add83a7-c513-3fa9-92de-2acb5b6e8db1 | -20.1223 | -49.0748 | 2024-10-07 02:16:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| a84e42ef-f731-30f2-94ab-7572c3742b06 | -20.1229 | -49.0518 | 2024-10-07 02:16:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 178.0 |
| a1911ab3-e0b8-3be1-a05d-53e3959f5abf | -20.1433 | -49.0474 | 2024-10-07 02:16:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 55efcf23-1359-30f7-9962-de0e1b88d5b7 | -20.4449 | -47.6875 | 2024-10-07 02:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b625d155-4144-392f-aa88-f444c2c59670 | -20.4456 | -47.664 | 2024-10-07 02:16:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 29f96156-1d9c-3e5e-b451-72b077dde5dd | -20.4655 | -47.6827 | 2024-10-07 02:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 201.5 |
| dbfe54cf-d470-3459-91a6-baf345c28925 | -20.4661 | -47.6592 | 2024-10-07 02:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 395.6 |
| 0f9998b4-1c64-3d9a-9c6c-2055253c46ac | -20.4866 | -47.6544 | 2024-10-07 02:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 9a17f365-3596-3a41-abc1-5b2378d30b55 | -20.5848 | -48.5137 | 2024-10-07 02:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 27570747-9493-373f-8042-a0448b4d01fa | -20.5855 | -48.4904 | 2024-10-07 02:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 281.1 |
| b1c34782-70d9-3a35-b800-4bf521666c8f | -20.6053 | -48.509 | 2024-10-07 02:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 125.7 |
| a56c906c-9e67-3660-96ad-ebba79b0866c | -20.606 | -48.4858 | 2024-10-07 02:17:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 370.5 |
| a9dcd0ed-fde1-3bb1-9e6a-d32ce0f8a82d | -20.6066 | -48.4626 | 2024-10-07 02:17:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 7afc52f7-655b-3328-9e6c-d70ea3b7f3b8 | -21.0712 | -47.2331 | 2024-10-07 02:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1bc1a11d-cf72-3455-b8bd-ec54327bd9dd | -21.3274 | -47.5939 | 2024-10-07 02:17:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e1caff5c-ebb9-3813-8245-59a701a2292d | -21.5843 | -47.9536 | 2024-10-07 02:17:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9df9d772-18b5-36c2-b432-7358f70a9bb3 | -21.605 | -47.9485 | 2024-10-07 02:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 77210602-02dc-319e-bb96-b66e86717afe | -1.0365 | -53.7389 | 2024-10-07 02:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 1e936fb2-9172-3498-b229-f9ece81b3e34 | -1.0365 | -53.7187 | 2024-10-07 02:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4e295adc-172f-3dc4-9ec1-bb14ec1dd372 | -2.2297 | -53.7026 | 2024-10-07 02:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d4fb6b29-2b02-3c32-ba6c-8790b152da62 | -2.8569 | -52.9197 | 2024-10-07 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| fdf77398-647a-30ba-8f1a-a9b08b60cc54 | -2.857 | -52.8993 | 2024-10-07 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| a35a392d-33b7-3376-939a-c3c33c7fa015 | -2.8753 | -52.9192 | 2024-10-07 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| afa70792-f11b-3d2b-86c4-5ec469727ac0 | -2.8754 | -52.8989 | 2024-10-07 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 59d1aa15-29e3-386f-91f5-4ccbfb697d27 | -3.538 | -65.0414 | 2024-10-07 02:25:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| a40d686b-a01d-35ac-8201-d8e74a95ab94 | -3.5381 | -65.0229 | 2024-10-07 02:25:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 29732917-bf35-3912-998c-634dcc57733e | -4.2542 | -43.7381 | 2024-10-07 02:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 77cf7117-69ea-3220-90fc-3f222c8a9fdb | -4.2728 | -43.7601 | 2024-10-07 02:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5e0d4d0a-d8c6-3600-aea3-646a20a3cd07 | -4.2729 | -43.737 | 2024-10-07 02:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 04f1eb23-7e9e-3776-9a32-271d7b306e83 | -4.2916 | -43.736 | 2024-10-07 02:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6e86e920-0262-32a8-8553-cb96580fdfd0 | -9.5343 | -40.3282 | 2024-10-07 02:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 9e0f6298-8a6c-3d89-b20a-3dfca3bdaa3c | -10.8337 | -68.3636 | 2024-10-07 02:26:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 22344347-938d-3a12-97a1-75ab2b25b238 | -10.8338 | -68.345 | 2024-10-07 02:26:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 41.8 |
| ad8685f7-1f74-37de-be82-dc3bf21ff7de | -11.7566 | -44.4897 | 2024-10-07 02:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f43b34f9-9dd2-3885-8bc5-14b18e8349f0 | -16.4164 | -57.3006 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| aa2a94f0-d0e7-3b47-8b27-61a2f0ad6861 | -16.4362 | -57.278 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 16acce49-ba23-35a2-a795-10e5ee6674f0 | -16.4365 | -57.2575 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 169734d9-59da-3a45-8f41-5076314f36c7 | -16.475 | -57.294 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 3671a3f9-e9ba-3902-a052-c64927a5709b | -16.4753 | -57.2735 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 34c6d182-ccd1-3ae4-8b30-254e431133e2 | -16.4945 | -57.2918 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| cc1490fa-05b4-3c58-a002-324b5c0a4ebe | -16.4948 | -57.2713 | 2024-10-07 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 0411c556-88f0-3b2e-8174-4213cf5dc18c | -16.5739 | -57.201 | 2024-10-07 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 212bd1f2-427d-312d-98c7-bda8f2109225 | -16.614 | -57.135 | 2024-10-07 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 6f22cbd0-8e3c-31d5-8797-86d401b5b8b1 | -16.6335 | -57.1328 | 2024-10-07 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |


[Clique aqui para ver as próximas entradas](README35.md)
