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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 511061ca-b242-3c92-9066-7c918cbaf274 | -2.58856 | -53.96504 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d2f4877-be62-3dff-9040-ac176823720d | -3.69685 | -47.67494 | 2025-11-23 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cb5a1c-cab9-342e-9478-c9bbab84d2b7 | -4.5209 | -45.42775 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79d24a04-072e-3e8f-8ac7-45fbe2271015 | -1.73742 | -52.02512 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ca70cfc-f96b-3798-9bdd-8dbc87f61848 | -4.71923 | -46.46637 | 2025-11-23 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ec8d876-2cf9-3e66-8d40-9b25629af069 | -1.6485 | -55.55791 | 2025-11-23 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c15d520-e4bd-31c8-b0f3-b86b87639363 | -4.60237 | -43.28553 | 2025-11-23 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5194268b-57bc-3693-9d96-81ddee073134 | -4.55299 | -45.49451 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16f8a237-3d03-3b55-b553-f9a160caf8e7 | -3.35945 | -46.86625 | 2025-11-23 04:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08589a9b-bc31-3fec-9b48-9d3a2dd8bb74 | -2.8894 | -45.27718 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf47c9de-a61f-32de-ab0c-548d7bb0b744 | -4.04687 | -42.52047 | 2025-11-23 04:53:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b71bf955-2619-3059-8092-72e01be8be34 | -1.30915 | -53.1412 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91f178f1-fc8f-3f6b-b849-69f5ca629131 | -2.7319 | -45.2146 | 2025-11-23 04:53:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f2f8fc5-adb0-3978-9ac5-498f4e7f94c5 | -2.63475 | -47.30107 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 072b553f-b38e-3587-9e71-1a04774711bd | -2.04493 | -52.04834 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b7f24369-f956-30eb-b224-9c5a31716be3 | -4.71498 | -46.46575 | 2025-11-23 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 7addd441-086a-3691-842a-18ab3df10979 | -2.27528 | -46.4458 | 2025-11-23 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e5ad4de-07aa-3fcb-9fbc-22bab671d74e | -2.63549 | -47.29825 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b0e013b-42f1-3c4b-880c-8f8fa0c08671 | -4.61305 | -45.63096 | 2025-11-23 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 027b6377-218a-3623-b766-4ff7273ff246 | -4.55755 | -45.49504 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c926871-bee4-3809-a30e-c41f34ec1748 | -2.6394 | -47.29884 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93075bae-0c32-38e2-b5d9-0eb00a1585eb | -1.74684 | -52.03013 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa32089b-2149-337f-a002-b77fe486c921 | 0.6422 | -59.7293 | 2025-11-23 04:53:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cfaf95a-22fa-38bb-b9ea-5916c1de8218 | -0.99663 | -53.74235 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f87bcb9-9698-301b-8b4c-b863b1c09b7e | -5.97499 | -40.38391 | 2025-11-23 04:53:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 0cbbd99c-c9b2-33fa-ba3b-65d63e96a313 | -2.87839 | -45.28922 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b7dd28d-d669-3486-a299-d38730753246 | -1.98362 | -50.24728 | 2025-11-23 04:53:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da3f88f0-cad7-3748-a5ff-3d82d12ec2ab | -1.73852 | -52.0182 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1be2993-ad17-3dae-bc86-1f76fcc9f8dc | -4.60285 | -43.28226 | 2025-11-23 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 866fdcd8-22d8-3c22-acdc-9ab49754b4b3 | -2.95968 | -45.43453 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 88fe74bd-4295-39e7-9e6b-7c91eb414363 | -1.74129 | -52.02218 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af2d1179-46f7-3baf-aef9-ce0a196239e8 | -3.94016 | -46.97199 | 2025-11-23 04:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64467008-2dc7-375b-a6b4-4304f46ecc60 | -3.05057 | -45.66077 | 2025-11-23 04:53:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c990395c-3ef5-3f95-bc00-6519070d9a1c | -1.3114 | -53.14902 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ed65a7c-f07e-3948-862f-d8235c8bb602 | -4.04084 | -42.52317 | 2025-11-23 04:53:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 71230d52-4988-3df4-87b5-2c8ac8e38c2e | -1.75316 | -52.14106 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79493489-4b39-39d4-b361-b01029c8783b | -2.44423 | -49.09731 | 2025-11-23 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cedefc6-3f29-36da-830d-0d07e91ee1c5 | -4.8055 | -45.6143 | 2025-11-23 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 765fd9e8-bc7b-3f5b-a5c8-0acab80302cd | 1.93244 | -50.86975 | 2025-11-23 04:53:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 429a3d61-ca9d-393b-944a-85adb7200ac4 | -4.71981 | -46.46247 | 2025-11-23 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a31c71f1-8555-3bc9-9f5a-e113c84f02fc | -4.63973 | -45.47354 | 2025-11-23 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75d50d0c-8ec0-33c7-b8b7-88c2f3809991 | -1.72727 | -54.09097 | 2025-11-23 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a70f25a6-92a8-3b3a-a706-57545f49d3ba | -1.86046 | -54.07127 | 2025-11-23 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35cc9484-513a-36f3-8d91-319b6884ae8a | -2.02654 | -47.15202 | 2025-11-23 04:53:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af6f659b-502f-3b22-a9a1-328816321276 | -2.7296 | -45.21678 | 2025-11-23 04:53:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af345999-adfa-372e-b55d-78a2f2b4db19 | -4.55911 | -45.08154 | 2025-11-23 04:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57e02aaa-13d6-3594-bfe7-569f3d3e64a6 | -1.2909 | -52.87942 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8fed41c-53b6-38a5-9ae5-459b1f02c431 | -3.46219 | -52.22919 | 2025-11-23 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81f825e4-d7e4-39aa-99ef-e306797798a4 | -3.69612 | -47.67977 | 2025-11-23 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b921edb8-0879-350d-8edb-569f17ed3d7e | -4.46037 | -44.1058 | 2025-11-23 04:53:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceab6894-e2b4-38d2-bf02-812eec3fe884 | -2.63942 | -47.29678 | 2025-11-23 04:53:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a5b0128-1be0-3fab-a532-de441994a956 | -2.88288 | -45.28989 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 985b0a49-1515-32f2-a877-fef1d8603e53 | -2.69918 | -49.51494 | 2025-11-23 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 095ae67f-508e-3438-bfda-0369bc334274 | -1.67216 | -46.45853 | 2025-11-23 04:53:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 777ec3ea-8d97-3bb5-9d14-63d92d69f197 | -1.48199 | -54.20328 | 2025-11-23 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c45c0933-4169-3c43-981c-a64157315a7a | -3.45379 | -45.53935 | 2025-11-23 04:53:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3168959c-5aa6-3ffc-a1dc-48a98f26b59f | -2.28895 | -50.43629 | 2025-11-23 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e03059-8493-36f8-9680-557939e7f03b | -4.11684 | -45.72204 | 2025-11-23 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfb9af80-08e0-3665-944f-b47d1c82381f | -3.26375 | -53.26351 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5488fc1c-7234-3163-a37d-3be36a70cd74 | -1.74462 | -52.0227 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f827581c-d959-322d-832c-f036c9e85d8d | -2.8939 | -45.27783 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26a4bdc1-cc92-3035-bdef-f66b395ba8e1 | -3.86415 | -51.14312 | 2025-11-23 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5366135-a051-3a39-9b2a-50b1bb727248 | -4.0474 | -42.51689 | 2025-11-23 04:53:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e9b6f20e-38a8-3456-a15f-13f96cec5c08 | -4.39206 | -45.73604 | 2025-11-23 04:53:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c310fcf9-8468-304c-b5d3-53e449e22b97 | -3.94071 | -46.96841 | 2025-11-23 04:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edf36419-fd70-3985-aefe-3def0ea222a0 | -2.49803 | -47.10088 | 2025-11-23 04:53:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2133ba7a-f4e4-328f-828f-f59ce65381f0 | -4.83771 | -44.06695 | 2025-11-23 04:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55031dd6-b51e-3009-8924-adaa9af806c8 | -1.33391 | -55.39638 | 2025-11-23 04:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be0af757-3b2e-3714-90b7-21ae55dc1a62 | -3.01259 | -44.4342 | 2025-11-23 04:53:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac0c9a13-a4d7-386a-bb7a-0d0c7c2c0b9c | -4.16911 | -44.21837 | 2025-11-23 04:53:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e12818ca-8d88-3e06-972a-2a1f4ae389c8 | -4.03636 | -42.51521 | 2025-11-23 04:53:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f729085-5b2b-387e-b064-cf6e6ed5ba1b | -4.75562 | -47.52 | 2025-11-23 04:53:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27791df1-8c71-3bba-8aed-a52a558c0a4c | -2.44776 | -49.09785 | 2025-11-23 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d184063-18b2-3e48-ace2-f34e52844682 | -2.9598 | -53.28261 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47126765-0581-307a-b190-f8c7c84628b1 | -2.95591 | -45.42944 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a474ac90-0805-3f1f-a640-3d77677d3c57 | -1.19558 | -53.71813 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d8c4d05-0c61-31c9-9146-44ba04f303a3 | -3.69998 | -47.68038 | 2025-11-23 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d36031c2-fbfd-3476-87d7-7bd48337a2aa | -2.48631 | -50.47062 | 2025-11-23 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea61dd40-00cc-3216-84d6-6dac8185a9ae | -2.23074 | -53.64884 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f46f87d2-52b0-3630-88fc-460445e15da8 | -3.29495 | -45.73644 | 2025-11-23 04:53:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e5b34cf-5f4b-37a5-b727-f86fc72b4ea5 | -3.19225 | -46.60079 | 2025-11-23 04:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85742e3b-f8e4-3f48-9b84-de54a6b8d49b | -1.74739 | -52.02668 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5c1cbc6-dc3b-3a85-b5ed-090c284e030c | -1.19211 | -53.71758 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58fdbe83-7315-33b8-820e-923904806c92 | -2.22789 | -53.64458 | 2025-11-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d8be5a-91d9-3884-8e9b-a1d7bf12012f | -1.74075 | -52.02564 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a29ade0d-c91d-3593-a7ce-3961fca1f7ab | -2.44485 | -49.09337 | 2025-11-23 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b7dc286-8a57-350e-8ab9-a7fc24c7131b | -2.95015 | -45.43745 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd5a598-c202-308b-8807-d30cd81d7a4d | -1.31198 | -53.14539 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc0ba6fa-47f3-30b5-8285-daccb77e5dbb | -4.16761 | -44.21712 | 2025-11-23 04:53:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b501cdf-c976-3c1c-bddf-8c5cac0ee250 | -4.39648 | -45.73692 | 2025-11-23 04:53:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 763a3c77-49d7-3ba2-8166-5449d62cbe04 | -3.38808 | -47.18979 | 2025-11-23 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e597c56-846f-3f68-8d16-a279bedd540d | -1.31597 | -53.14225 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14fabb6e-3087-3b22-8eb4-2521827905d0 | -4.83856 | -44.06512 | 2025-11-23 04:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 566865e3-f45c-32ab-97ba-9497111d4083 | -3.46551 | -52.22971 | 2025-11-23 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 476f6304-cefb-350b-9102-3f101919c69b | -2.96037 | -53.27902 | 2025-11-23 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc42dc22-50ff-3fb2-9238-1e51cbfb6c7d | -3.29115 | -45.72906 | 2025-11-23 04:53:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86e38f8a-323c-3db2-be8c-5566fe9629f5 | -4.5537 | -45.48973 | 2025-11-23 04:53:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59fbd977-7418-3270-a8bb-b2fe8a811f90 | -1.66647 | -52.04597 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0eacaef-fafa-3568-96c4-77e2c16327b2 | -2.44132 | -49.09282 | 2025-11-23 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40ce3f33-7633-3d7b-b020-3edd42a4855f | -3.86517 | -40.64491 | 2025-11-23 04:53:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
