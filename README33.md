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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9c534bd-448d-3ddc-a924-753c59fc39bf | -3.83241 | -51.87473 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 644efdd5-50fb-3e4c-b163-a2ad0b05e6db | -4.64193 | -50.93682 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a3dda52-9ba2-3562-9acd-2d10abcfeafe | -4.64028 | -50.94748 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5bc61ab-d815-3f3d-951a-5fcfdb4eb3b1 | -4.63857 | -50.93631 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e2584625-8d69-3781-bf9f-42685593085a | -4.63802 | -50.93986 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 570cb514-1bc1-357f-93e1-7d0f6d0a6f35 | -4.61737 | -50.96206 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18694a7f-2fe1-339f-827b-e798bf3503ef | -4.25404 | -50.97855 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d56cea-a4c7-3692-81a8-b4ba36b5187c | -4.25293 | -50.98565 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acb10594-5101-3c86-85c7-033e33591ab0 | -4.25068 | -50.97805 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8c11767-5987-3505-a2fe-ce09cd65ef29 | -4.25013 | -50.9816 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d59ceba4-2991-30d6-8222-1dd9e8b54186 | -4.24902 | -50.98867 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 85486894-f156-3b39-93d2-6900554797ec | -4.24847 | -50.99219 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b11535ae-d5ab-3a9c-aeec-6184d17fb9df | -4.24732 | -50.97755 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705cd9cc-bb82-3864-be7f-0af740a52060 | -4.16994 | -51.23157 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1da734ad-8313-37de-918a-e5c8e0da22a4 | -4.16437 | -51.0372 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1259ea50-0ad8-3a50-8880-22316b7d9de1 | -4.16381 | -51.04071 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79605cc8-c717-36ac-89e1-26fef10ece1a | -4.12213 | -51.1098 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21cf7170-93ac-3765-a90f-1b1a8d514074 | -4.07545 | -51.14557 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91bd1711-03db-374a-9564-4b35880ed302 | -4.07375 | -51.13457 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9130ce4c-34dd-37c1-91a6-7ee79a852c2f | -4.0732 | -51.13808 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 951e509f-d0cf-3bb8-bd7d-0ac773ebdecf | -4.07204 | -51.12356 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cbe2a8a-c1a4-352f-a122-3edd3011a9d1 | -4.07048 | -50.97943 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58207742-99e4-3baf-86d4-c293f4384ce6 | -4.0687 | -51.12307 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06189f0-709e-3167-9cda-67ff7f0846dd | -4.0659 | -51.11906 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38b1e9eb-a5c7-337b-a130-5a4edcaaf36a | -4.03927 | -51.10004 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c971a24-48b6-33bf-aece-e12874b8a718 | -3.98615 | -51.02351 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23424b7d-7753-30f1-af26-e39ea5da1ea0 | -3.94532 | -50.9886 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7ddeab0-5728-3ef0-a806-f132d97fdbb6 | -3.92281 | -51.23231 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec902a87-e437-3d38-a34d-d96ba4cc6312 | -3.89164 | -51.15619 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c26fac9-d718-3978-ab4c-4711ec1edae8 | -3.89109 | -51.15966 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bf3f119-cb69-3792-92a7-428ec01e7349 | -3.88939 | -51.1487 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc504df2-e3f2-3ede-bfb5-27c9db4707b1 | -3.88605 | -51.1482 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23ca8830-376a-30ad-b2b1-b37fccccd929 | -3.88464 | -51.24438 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba37381d-5903-3c57-914f-b9559395433d | -3.85366 | -51.28953 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62cbc1c-f718-373a-8806-4a5902697adf | -3.84979 | -51.29249 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ce999fa-3f30-33ce-b107-9febb931618a | -3.82187 | -51.14898 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17fd3f62-1a6b-3f05-beb7-b2f030916bfb | -3.81519 | -51.14794 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6c0750b-f3de-3844-8212-8a389b3bbcfa | -3.81195 | -51.19032 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 703791f5-10dd-3f3b-a37e-f594c67b40cc | -3.80861 | -51.18979 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff084c3d-c562-3f33-92a8-3b2e57a86caa | -3.72272 | -51.25847 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26d9fa18-8b04-3390-9546-a8ef9498d8c5 | -3.72217 | -51.26195 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91d5ae6f-d8ea-3a83-ac1c-0ec1c7f69585 | -3.7169 | -51.10777 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c67ae8e-3f9c-3d13-ae17-60319e65f1d6 | -3.71302 | -51.11075 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75961738-e3e0-36d2-b4d6-11f490c4c12b | -4.6582 | -50.94295 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72324224-a1bd-3e99-8054-5a2d159f7fe0 | -4.63973 | -50.95103 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87c5aad9-1895-3ce6-8c88-f696c627b83c | -4.63637 | -50.95051 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6ff27a3-4958-3d56-995a-e63464f8cd18 | -4.63466 | -50.93933 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e7cbd2b-3b08-35a3-bdb9-1b673c9607b5 | -4.59971 | -50.95594 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b03650cb-e18c-3e2a-9f00-b27f0e0fcbb8 | -4.25348 | -50.9821 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 420e0f74-e918-3fd4-874c-f1f984e78376 | -4.24957 | -50.98514 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51c88468-e47f-3aae-ba85-36b77cc651ce | -4.24566 | -50.98817 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 630ad1b1-45eb-3752-9013-1f69addb747d | -4.24511 | -50.99168 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 857a012b-0a04-335b-9d55-d57771d50164 | -4.16932 | -51.03765 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7fc7219-9365-34ac-83cc-82010e6ce106 | -4.16715 | -51.22756 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8563fb58-9c80-3db9-bd64-f48cba1536e5 | -4.16598 | -51.03713 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cdcac11-0af6-36ef-95db-05fa8f3ee5be | -4.07934 | -51.14259 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51adddf0-5b95-3a49-88ea-a793a26a368a | -4.07764 | -51.13157 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35bdfe32-c298-332e-839c-11f580f855d8 | -4.07654 | -51.13858 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0fc4495-e4d9-3060-a426-1721884cbba5 | -4.076 | -51.14207 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d10609f2-fde2-312b-98d0-8fb975ceb663 | -4.07429 | -51.13107 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c74ac87-43c9-3d52-a94a-b4c0bada3719 | -4.07328 | -50.98347 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db4d8283-660e-3d86-9f1e-7a306abb195a | -4.0715 | -51.12707 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bbd6d22-e9b4-3767-aa4e-0982d80e4341 | -4.07095 | -51.13057 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 877d3e65-0cea-3684-884e-3b13a6583cf2 | -4.06993 | -50.98295 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4516ff9-3250-39ae-962e-fd281d55da5f | -4.06924 | -51.11956 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2e7f3c-d6ce-3d5e-80c6-c5e5519d5c0d | -4.06712 | -50.97895 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aa48328-104c-3ea3-a885-b94271411ce8 | -4.06023 | -50.96658 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bddbc12-27d2-35d3-8bf3-cbc14b5c7cf6 | -4.05967 | -50.97013 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87721916-8ecc-3060-abfa-b2394a3c4b6f | -3.99022 | -51.08524 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99389d2c-5c96-340c-967c-a4abb9b757a8 | -3.98561 | -51.02702 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12054a4c-98f8-3fff-8e39-6c133a9e33bc | -3.94198 | -50.98808 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06162e96-ceb6-3afe-ae8f-03cfaae2cbb9 | -3.92227 | -51.2358 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c797a8f-3729-30c3-ba9f-0de3514978b5 | -3.88884 | -51.15221 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3938de69-bc83-3b95-a25a-fe5f3ebfc7a1 | -3.88372 | -51.82966 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2edac93b-8bfa-3ccc-b78b-778b19af6e14 | -3.87393 | -52.08634 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d9a60de-f800-3d19-8443-1e5d69da021e | -3.86748 | -51.95446 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7203ee86-5a4c-39c8-987c-9ff003b7ce6b | -3.86416 | -51.95394 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49bf0c17-eaaa-38c4-9f07-bc303ae5f8af | -3.83749 | -51.90734 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f645d3c5-1773-327f-99fb-296a81fbc494 | -3.83694 | -51.91079 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa4105d-17a8-377f-ab80-611fde86d4ae | -3.82242 | -51.14548 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e23c469b-68be-3136-a2c1-4af93300eaf2 | -3.81853 | -51.14846 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f1da7b-e853-3619-9602-472dbdbb57a0 | -3.78786 | -51.34343 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12aa6083-2dea-3259-9db6-4bbf8e43edb7 | -3.78454 | -51.3429 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9af11300-d94a-3346-a909-2d80ef290e0f | -3.78399 | -51.34637 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a1aab7c-b264-3235-80e2-73cdc7a7dd46 | -3.78271 | -51.82812 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b7bbe40-3c74-3cc3-a935-ce6651d829d4 | -3.78121 | -51.34237 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ba857e6-3c73-388d-9bdc-680945c1abba | -3.77885 | -51.83106 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| caafd9f4-d9f6-3e62-89c1-f566411137b4 | -3.77613 | -51.30956 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a39c9fa-4468-3543-8f2d-d7cdf4354c83 | -3.77281 | -51.30903 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f91581-c240-3171-a6d0-f8433514415a | -3.77167 | -51.83348 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b631e268-343f-3fea-af56-aab506f32d59 | -3.77138 | -52.24021 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec80f04d-66c9-3ff6-a628-81fae9de9d51 | -3.76889 | -51.8295 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91394a2e-3890-3293-93bc-165f8346ca03 | -3.76334 | -51.82157 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c861521-dc4a-37e1-81e8-3bd764b65f71 | -3.75681 | -52.05747 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c37bc76f-62a5-3e83-8a60-1879d85fa864 | -3.75626 | -52.06092 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ee97721-49d0-36e8-b89a-43d5c1f2616b | -3.74078 | -51.36099 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72909677-36de-3076-a05a-1893125ef11c | -3.74072 | -51.33961 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c3db6f1-1283-39ca-9cc3-451349aab567 | -3.74023 | -51.36448 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59d8245-cd82-3b0e-ace0-c4f8a7911520 | -3.73739 | -51.3391 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dffff43-e63e-380a-badb-b2fd8cf9442a | -3.73461 | -51.33511 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README34.md)
