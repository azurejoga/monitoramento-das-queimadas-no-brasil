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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70500458-b302-3b3b-854b-0ffe416182b2 | 1.06593 | -60.6026 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7d9887d-0ad9-36a8-b62c-25b2b7b544f9 | -1.55854 | -51.84934 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be11e7db-890c-36c1-b5ae-982dc677a26f | 2.35205 | -55.93954 | 2024-11-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d845c744-f393-3cfc-aec5-686fed654061 | -1.25232 | -55.69233 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 447cca38-1ec0-3368-817e-6e4d3e4c7329 | -0.36819 | -51.74096 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61bbef37-7821-3b31-9ebd-3b5595484599 | -2.21442 | -53.7483 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5a7c102-1a13-301d-a44f-dcb1876773b0 | -1.22778 | -51.74567 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50f406dc-b96a-3d5e-8af5-93504032228f | 1.30624 | -50.87085 | 2024-11-13 05:20:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d31837ff-85e9-373a-a1aa-6892899bef96 | -2.1491 | -52.09527 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17b6be62-da77-34f5-8afe-f8698cb5aa13 | -1.57422 | -53.79873 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbf9e797-b008-3b6e-ad51-fb18ac910d36 | 3.59945 | -59.94783 | 2024-11-13 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ab0dd9b-dad7-394a-9bf8-4d39e2aa204c | -2.42683 | -53.88285 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 189b08a0-82f8-3553-a7de-d3134bda8630 | -1.64489 | -52.53662 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3803ff3-f238-3a36-9a98-1b72394f2a72 | -1.64562 | -52.53199 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b996df77-b3f1-3119-baf7-9d1da2ddbd61 | -1.56147 | -54.26373 | 2024-11-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6220909d-4482-3a80-b0a1-49478a6452d2 | -1.57509 | -53.73642 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f1e498-8dc9-3b52-ad22-816434a7bcf1 | -2.96725 | -49.28477 | 2024-11-13 05:20:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 953db25b-afce-3f0b-8f36-b2005ba4d2a5 | -1.95574 | -53.31796 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5daf2df0-8d68-3c9b-b886-9008e75d1487 | -1.64432 | -52.53925 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 718f138a-69ec-3b33-9c48-d6a99d3f2c45 | -1.21352 | -51.77519 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dc87952-5dcd-3d46-a328-0ebec4a927e2 | -1.21469 | -51.77305 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40a3a778-c242-32f7-89bd-2f0ed15db9f1 | 1.05508 | -60.60051 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 96b185de-91ea-35cf-81dd-e26e82526542 | -2.11783 | -50.69106 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eceb3bf-7170-380d-8dc3-143ca4b4a7ea | -2.78372 | -51.40178 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 021dcb43-c590-3a02-bb99-ea1ab8b016c7 | -1.97989 | -53.13645 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1773bde0-cd9a-3b88-9708-a4621a84c3ba | -1.65913 | -52.62639 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b5ac83c-4754-3691-81ad-a96dfe31043a | -1.30589 | -54.66782 | 2024-11-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59de343f-ca67-332b-8170-625b48429ba2 | -1.51624 | -54.98831 | 2024-11-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8a2c84-c6d0-3614-88dd-035764b2cb21 | -1.23258 | -51.74641 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b927c38a-e413-34a7-8b0e-76b50c42a453 | -2.79171 | -48.08421 | 2024-11-13 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf102036-2ba8-370c-a545-34e85d1128db | -1.64114 | -52.52926 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4058b68e-d7ec-3293-915d-6ab75ae3d263 | -2.46076 | -53.97085 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fab2419f-9f60-3b5c-b616-9e7c056879a9 | -1.61962 | -52.51851 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46cd2bfc-eecf-376d-8570-ef6cad63a6ad | 1.10882 | -59.18943 | 2024-11-13 05:20:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac27eb8b-d04b-3071-bebb-77b6535f0a9e | -2.66358 | -51.72199 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65abec52-35b3-31da-bf25-ad50d0cfb484 | -2.39399 | -53.73516 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47e0c689-e31e-3bd8-9dd8-75487c9535fd | -1.6136 | -52.52708 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ffc7b0d-bd30-391b-a26c-7d1df2d639d6 | -2.39097 | -53.66974 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6bf5239-c372-37e4-9d9d-80592a30b14b | 1.0625 | -60.60313 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2bbc38df-e4a1-3b04-9dc1-323b87ef755c | -1.984 | -53.13517 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e21d65-b522-38cf-8ec9-521f55779e75 | -2.78739 | -51.40248 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd61a154-2dea-3358-9a0c-f8cd35a2b8ad | -2.11686 | -50.69733 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65fbc286-8730-3738-8d2e-ae7857263104 | -2.61031 | -48.24836 | 2024-11-13 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2d7f1f7-8b73-3558-abdd-7d11842d39c1 | 0.89427 | -60.28501 | 2024-11-13 05:20:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 047d6da1-9111-3eae-aae6-98acd69d99f7 | -1.47052 | -52.30314 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42495f46-d3f5-3559-a0e4-f0d050ce41cf | 1.06078 | -60.59206 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b859cb-c537-3da3-aa46-9e216c00e387 | 1.59579 | -55.77238 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db04b6e0-cab2-3c31-a54c-3f6ea862a717 | -1.21753 | -51.78108 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dccf52f6-47f3-39df-8d03-877bcb4aa612 | -2.78575 | -50.29902 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e3bca03-72b5-3102-a426-b0173d182710 | 1.14153 | -60.59439 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55188f75-eb50-350d-8341-cb52d37fd807 | -1.88194 | -54.20233 | 2024-11-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a42e7536-4d29-3698-b999-001879681e15 | -1.65347 | -52.54066 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 457d8967-6c15-38d3-a140-bb38a64338f1 | -2.78544 | -48.08322 | 2024-11-13 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9330c136-e126-35d3-9689-8f0089473649 | -3.03694 | -48.07701 | 2024-11-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c752470-b931-3a68-ad51-1eab07493748 | -2.1283 | -50.69263 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8402b2e0-8ed0-397b-a76a-a216f312f542 | -2.12258 | -50.69503 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57e0d5b6-0beb-3f34-84df-fd38a81ddf89 | -2.61231 | -48.24948 | 2024-11-13 05:20:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f43fe98b-0ab0-34d1-9e95-98df0aac8903 | -1.6242 | -52.51921 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05bb68f6-53c3-3bd2-888e-0cd9f834d86b | -2.24895 | -53.74979 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d29d0269-f20a-3b23-b6ff-f9b2604b508e | -2.20708 | -53.73927 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bca627fb-a448-3e06-8691-970b9492f7c3 | -1.42113 | -51.11123 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f08b7d5-04aa-392e-b481-6502391b551e | 3.6057 | -59.94311 | 2024-11-13 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d52925da-e0a8-33f7-8a23-5ac7e0d580ee | -2.72782 | -51.7381 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea726be7-8297-3ac6-b5ce-86c4482547cb | -2.24955 | -53.74586 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9bb25d6e-3888-3baa-8f2c-6364c8eed04c | -2.7798 | -50.30168 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 709dc5d2-ff26-366e-b789-4b0de54c82db | -1.03429 | -48.85001 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3b5609b-2ef8-3854-b38b-73ea954ba0e2 | 1.00977 | -60.57659 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9eb1528-c34a-3186-ba64-2dad59ab0824 | -1.39688 | -51.10153 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf0d2715-3c2c-3e45-8d2d-cc139716246a | -1.65417 | -52.53603 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c05de9a-fadb-38bf-a546-6a051fe5b0aa | 1.00919 | -60.57293 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eade8a6e-dbdb-3e43-86e0-70de15e5f529 | -2.45827 | -53.93118 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4868d4f6-6134-394a-acef-54313145cea7 | -2.14881 | -46.40385 | 2024-11-13 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6919c3da-09d3-3b98-b90d-b514c29f2f6c | -1.65804 | -52.54136 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3f90213-2e12-37e5-b78a-968141e5aa87 | -1.30867 | -55.8497 | 2024-11-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d600667f-8c25-3cc6-a1e8-a527064ba0ab | -2.11212 | -50.69336 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d43f4a2d-15ef-3d28-b58d-fe89e5724b53 | 2.35143 | -55.93935 | 2024-11-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5067e4-7594-3e1e-8f93-1f88f801b213 | -2.29809 | -52.20198 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0165974-26d7-372b-8bb6-ccda0009df0b | 1.30306 | -50.88252 | 2024-11-13 05:20:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c41988c-0947-3149-b732-59f5456b10cf | -0.28202 | -51.6706 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3f6fbdb-986b-3af2-88ba-40ccd74dda54 | -2.46496 | -53.9715 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01644b59-ddb8-3a99-b13a-5202e26a55d2 | 1.56529 | -55.8007 | 2024-11-13 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4562efa8-9547-3da6-983b-53b5bdc25df6 | -2.20868 | -53.73693 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56b531df-e16a-325e-8c3b-a747010e54ce | -1.30195 | -54.66716 | 2024-11-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 664e913b-f198-3ef5-a57d-b802ce2a4ab4 | -2.65949 | -51.68199 | 2024-11-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 892b0e7a-5603-339d-94ad-56fa77b7a144 | -1.43976 | -55.45828 | 2024-11-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2bf26d-b537-3bbd-a584-02ee0bbe8d32 | -1.73405 | -53.28026 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aae475c5-f87d-33ff-a1d5-9b843c794370 | -2.24351 | -53.75695 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8cc8f91a-ce10-398e-8e20-ff543235f7d6 | -2.24411 | -53.75304 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 39d8507b-9036-34b1-b0e7-d4c3fc0308cd | -2.23987 | -53.75232 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 000d02b3-2ab5-34c4-b507-1ab5d62144b3 | -1.73795 | -53.27809 | 2024-11-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ca55d80-bc71-3868-8e2f-52c25bc02566 | 1.00861 | -60.56924 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e627d056-88b8-3206-b179-d1c1e9bb6ae4 | -1.40146 | -51.10519 | 2024-11-13 05:20:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95b9399f-8873-3be4-a6ff-338e66bd9e89 | -1.21274 | -51.78036 | 2024-11-13 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dfaecd1-a609-399d-a19d-5a4a0f8ba19e | -2.34171 | -48.59384 | 2024-11-13 05:20:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0d4ca04-9cc1-3eab-a2f9-d19a8c881a25 | -0.38183 | -51.74934 | 2024-11-13 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5191d17-1c55-3c5a-99bb-c0e6890b8508 | -1.88548 | -54.20657 | 2024-11-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 11f75336-49e8-30a3-b77d-a83ecc5187b7 | -1.52012 | -54.98886 | 2024-11-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2932a2d-390b-3c6d-89dc-5e9bef86ad22 | -2.30414 | -53.8695 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1960924a-6d26-36af-be9a-a475b3016ed0 | -2.39525 | -53.67042 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9ac3c7c-82dc-3e8b-93eb-ca2154ff2b8e | 1.0585 | -60.59996 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README45.md)
