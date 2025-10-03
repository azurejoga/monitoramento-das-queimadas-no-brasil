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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdffca56-2234-3785-a7cf-4cccae21e7b4 | -7.055 | -43.30464 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc049c24-8243-38fa-a8e2-7a7a4e48742f | -6.32288 | -43.88225 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e478538a-3253-38a3-958a-e2a5f6d219d7 | -5.54232 | -44.64932 | 2025-10-03 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af50dc51-8d67-3d36-baab-9b31dfcf69b3 | -8.59209 | -44.78872 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c59c81b-6058-36a0-85ae-9e5b31dd6bf5 | -5.49053 | -52.13956 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f4abde5-8687-3ea4-9232-5160a9a2c64f | -8.58853 | -44.78818 | 2025-10-03 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| daa6cc66-0276-3370-ac12-b4ed9467db06 | -6.95467 | -45.34743 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0cae8588-8b1d-3891-a4f0-abdd41da5d33 | -6.55309 | -43.88612 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d469f55-f0e5-3543-9359-e52107f5d700 | -6.53332 | -43.37651 | 2025-10-03 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 268bacc5-c8cf-3ad3-8dc6-391f4fe0505d | -7.75687 | -46.26317 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| eb8d57bf-1b87-3d1d-a701-4d07d57c7852 | -6.68572 | -42.84112 | 2025-10-03 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f5f61521-2ce4-3bda-8ed2-d291bfbb9957 | -7.31439 | -42.88675 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f32efb4-5dd7-3dc4-9283-9218a8130078 | -7.3189 | -42.88015 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 101eebd9-5f37-3464-a3c9-b487e013075f | -7.76984 | -42.59645 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 20c5b96b-0184-3994-a70a-fabd08076ab5 | -8.21917 | -45.55075 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22e7aa4e-f77b-3e28-85fc-a5c102ade312 | -4.93168 | -43.73939 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c0c0159-1cc3-3486-80f8-0827a53d3242 | -7.74668 | -42.57763 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eac7ec13-26a5-317b-bba1-88bb55c4228d | -8.61069 | -39.07668 | 2025-10-03 04:10:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f83ad01-b643-3d47-8f68-66ef435ed259 | -7.86783 | -47.30389 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2d4c747-c8cd-391d-b4e1-eba5e1309671 | -5.91662 | -44.2727 | 2025-10-03 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48f5d8d8-9b64-3e48-9083-80de9ad56d77 | -5.63265 | -43.91152 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aa97e78-8afc-3f18-9d0d-799bfdf774e5 | -6.3811 | -44.63196 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14498a48-1507-39be-b00c-7af849556691 | -4.89779 | -45.73256 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3514d59d-c361-3e88-911b-5c371f313e80 | -5.347 | -43.75907 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7103ee65-b835-3025-88f7-b5a891137f34 | -4.99281 | -38.85767 | 2025-10-03 04:10:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 48154702-ed17-3970-af3a-917b2717a3e4 | -6.67294 | -42.79146 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7ad9ed34-4dd0-3b41-ac19-d6ff8614b29f | -8.66002 | -39.43494 | 2025-10-03 04:10:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 664e4316-b7b9-3361-b387-a8ece6f0789a | -8.24627 | -47.03728 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a9359c3-9479-3d05-9b63-124e2db1b01d | -7.25374 | -49.41431 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d96facaa-89f4-3450-85d4-8c4ebc540c78 | -7.74927 | -42.57508 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c22290d9-66ff-3a5f-87d6-ec486138180d | -7.76757 | -42.61057 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 4cec6b54-0afb-383a-9914-41582ec4ccd4 | -6.72731 | -44.1491 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a5379a8b-9871-3262-bb22-08d41bbec3a1 | -6.54343 | -45.80378 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd26cd97-6e95-3d2b-adb2-4a74f93c8953 | -1.08102 | -53.67885 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4dff940-bde1-3e61-8d04-07842afa9c93 | -6.67631 | -42.79201 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ee10d4a-b6b9-31ac-93d0-6d7bd969184e | -6.87567 | -45.47684 | 2025-10-03 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 692ad6ba-fbd6-37a4-ac57-48e0c909ac12 | -6.64053 | -44.98201 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d59b536-f017-37b6-a881-c88c8bf530b5 | -4.87592 | -45.62066 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f0a318-0314-3d54-a0d0-de5718404cfa | -5.44897 | -44.82789 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 509048c0-5012-3932-b234-ff7677a7348c | -7.79052 | -42.55285 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d430c74a-8abc-3d8d-9bd4-078ec1e63e28 | -6.23382 | -44.27589 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb610c1a-973b-3e44-9f20-71ab559e2166 | -6.3239 | -43.89815 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c408dc61-d81d-3d76-9aad-0c645c1a8aab | -4.65498 | -45.79562 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 001cd7bd-016a-3ba7-8df6-deba902b393f | -6.04738 | -42.79168 | 2025-10-03 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c8dc75e-0975-31c7-ad5d-b6af8460b570 | -3.17147 | -48.60912 | 2025-10-03 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60a1fc63-2b4d-3170-a26c-b79377019d22 | -4.82756 | -43.53654 | 2025-10-03 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc3a0b87-7aca-3f59-bc73-47dcf1a91735 | -6.82601 | -45.98675 | 2025-10-03 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 701415c9-4413-39b8-a2c3-b3ecaa686724 | -5.22432 | -44.49349 | 2025-10-03 04:10:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a962c8c-64c2-37e7-b80f-369e5e8d80a7 | -5.90427 | -43.90504 | 2025-10-03 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3de18f4-b23f-3468-a80a-156388057b7f | -5.6368 | -43.90821 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77604aa7-8811-3426-aadf-3d211357f022 | -4.8564 | -45.66722 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfcf62e7-b63a-3911-b728-7998b0ce3078 | -7.75155 | -46.24727 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3d69f671-8bac-3a69-9156-ae551f1cbfe9 | -6.30717 | -43.43659 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17c13269-5f02-36e1-9f32-ee597bb9f3cc | -7.21285 | -46.87948 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8f2addc0-56fb-34e5-8811-8c6fe2a544eb | -7.55841 | -42.40025 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9043cf07-aac4-3cbf-b3be-38c76b652858 | -6.71636 | -42.16193 | 2025-10-03 04:10:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1bd88218-d1dc-349c-9cfc-ea04819ed0f7 | -7.75994 | -46.26873 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 38229c88-890e-318f-a889-b6d4db420edb | -6.72442 | -44.14457 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8100e03a-f7d4-3fcf-a39f-fa71a45f546c | -6.94677 | -45.44287 | 2025-10-03 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36c68fbb-c3f3-3e12-90a5-2fe2d97c4ce3 | -6.48134 | -44.21943 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 450f70cb-0d7c-30f2-bcf2-effeed4157f4 | -6.67396 | -42.82818 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61dedce0-a802-33aa-9495-b911730420fe | -3.09015 | -47.00928 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b899b72c-5b11-3d9a-9148-4ed6e2c770e6 | -7.48237 | -43.03803 | 2025-10-03 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd6fd3b1-855c-361f-8e46-bc464e436f0f | -6.55494 | -43.87464 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f784ecbd-ca8e-33de-b184-4311e34cf25d | -6.26713 | -44.04882 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9354c6bb-d361-3a37-ae76-1ef1f3b4704a | -4.66041 | -45.81179 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b31c5a96-5806-3970-bd15-c0d02383c3ad | -6.23908 | -44.24355 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcc74413-512c-39bc-96ce-081154d0e762 | -7.70981 | -46.21112 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 06b483a4-9607-3aff-a2ca-dd65ed09ddef | -1.07787 | -53.68443 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e4c26b0-31e9-3e56-a6df-aefdd1289e55 | -7.52131 | -50.49577 | 2025-10-03 04:10:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1a81e92-70c0-35f7-b93b-0b30d5114c00 | -7.77331 | -42.51051 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ebc88c9f-3f48-399b-b2ce-e43e0c53907a | -0.91078 | -47.54566 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a02778ad-5a78-364f-905f-f7c2d801f17d | -7.74948 | -42.56004 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abf41860-af33-3b28-a12e-f3e7bdbc4e6a | -7.74612 | -42.58115 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a95f7ef2-d251-37ef-b699-294799512103 | -5.39182 | -43.59203 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02e19f9e-a5bf-396f-9cf1-2781d6678409 | -5.35176 | -43.75182 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2dce975-1361-3953-ae78-3c116fd5cb63 | -6.23774 | -44.25175 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b6daa6e-76ac-33de-8c15-686add7f84ad | -6.70942 | -42.80103 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 46b1ff03-5ef5-3bf4-9564-073f80e4a198 | -6.04743 | -44.61644 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa705265-a067-35df-8237-0bcd9cb61c3e | -6.29751 | -43.90606 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 458611ee-351f-3ece-841a-4340044722d9 | -5.6502 | -44.89695 | 2025-10-03 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6fc6334f-bdda-3e50-bd12-ba461794cdb6 | -7.75619 | -46.24341 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ed5bbff3-ed3d-3e55-a781-cc27e2a84335 | -6.54735 | -43.87734 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f05257f-52b8-3532-a629-12ae75cddcc8 | -3.09319 | -47.01828 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2a07d88e-db6c-338b-a78b-0ecb7051bd8d | -7.76429 | -42.58832 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4b22109a-6201-3608-8a2f-be33f2e1295d | -6.56007 | -43.88722 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70aa3d3a-2e8e-3519-9765-27eead19dc6b | -5.35508 | -41.18802 | 2025-10-03 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 936af2fa-3010-31e1-9a9f-94aa242115ab | -7.41728 | -40.07783 | 2025-10-03 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b158886-242c-3777-b8e7-871298c7b76f | -2.62822 | -46.84054 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b87cf2-9d1e-351b-8bc8-cb65e194b048 | -7.77322 | -42.57532 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9abcc532-d240-3ee5-b859-bfd384038f66 | -5.64963 | -49.13089 | 2025-10-03 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cc74cbe-7605-3d9d-85b4-191897745f46 | -5.9084 | -43.90171 | 2025-10-03 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5658dbf8-bbe2-3fbf-9432-85dd551d88c9 | -4.0073 | -43.27664 | 2025-10-03 04:10:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f7d0783-b372-368f-8bf9-d063aff96f3f | -7.19601 | -45.38676 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2979dd9-fee1-3472-a5aa-672ff02626f8 | -3.49636 | -50.27122 | 2025-10-03 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f3bb931-00ff-3114-b1c7-8056afa6f8a6 | -6.56081 | -43.88712 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c2ee229-2751-3984-9a7f-accdde6ff139 | -7.77665 | -42.51104 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 27903974-3242-3f53-aef8-05b28c87e171 | -7.30822 | -45.26072 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d13e045-51f3-3f25-9bb6-9b35266a8398 | -5.78413 | -45.74679 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9a5f614-29a8-3402-a2d3-d97c80aa00ed | -8.48055 | -44.59252 | 2025-10-03 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README47.md)
