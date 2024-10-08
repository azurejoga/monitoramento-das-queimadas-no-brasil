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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b6635d3-caee-3448-9826-fe63a8e170c5 | -8.96891 | -52.78649 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe083cca-a28b-31f1-bd33-9ec15d7673b7 | -8.95576 | -52.78067 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd3c379-e417-3139-818e-434bc0dd4891 | -8.95518 | -52.78445 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b318f085-a16c-3794-8226-1f748615b614 | -8.95175 | -52.78391 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6ed6ed9-b9de-36d5-8ae3-5b73a583aa3f | -8.93863 | -52.80097 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ac956b0-1448-3e3c-8927-07036fe9256e | -8.92373 | -52.78349 | 2024-10-08 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ac63d729-471d-3c18-acf1-08c4d7e4817a | -10.70073 | -53.03526 | 2024-10-08 04:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21f671a8-f06a-3b97-bd5c-da5807c434d6 | -13.30109 | -53.70094 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c4d45de-e058-3ff4-8825-048052e4bf7c | -13.30052 | -53.70476 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9191058-9c2c-3fcd-ada3-8a2f5b34166e | -13.29381 | -53.7084 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fbbc565-ee13-38a9-bb9c-a61df69f1cc5 | -13.29323 | -53.71222 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a122dbf-47ea-388e-b5d3-1a3399768683 | -13.29265 | -53.71603 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3435c196-e5ce-374e-b996-5851df53424f | -13.29037 | -53.70787 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5df1a730-7659-3c92-be35-4b46a5afd2c8 | -13.28979 | -53.7117 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f115a550-5699-3141-b6ff-619286f671a8 | -13.28693 | -53.70734 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e24a9a2e-bd75-3fbc-9baa-684c0718467c | -13.28635 | -53.71117 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbf01971-c9d8-3074-bdab-c3bad6ecb7c4 | -13.28349 | -53.70681 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae4b4b9-d991-3d3a-bfb1-a33c8ba40f4f | -13.28291 | -53.71063 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e844e473-a59d-3eaa-8793-3b0773c623ea | -13.27948 | -53.71008 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c040022a-e8c3-3ebd-abd5-260c1b93f5b1 | -12.67402 | -53.19126 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ba35a80-6b9d-3ccf-8fa7-6ed0cd49e6b1 | -12.67112 | -53.18682 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3195cfc2-1900-384d-b032-6a9829d9063f | -12.63498 | -53.11705 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631abf2e-54ab-3776-afa2-89173ad78755 | -12.63206 | -53.11257 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22bbad33-6840-33b2-8733-3ffd30289c5f | -12.63161 | -53.11298 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c240187-d49a-33d4-94d1-dcb1e4be60c9 | -12.63149 | -53.1165 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3210be8-0525-397f-b2a8-c5dfc3bf31ad | -12.63141 | -53.50049 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30f740c9-013d-3c0b-9aff-956199915cb5 | -12.63101 | -53.11691 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2ed1470-e69a-3fb2-97ed-0fe9a8d1651b | -12.63091 | -53.12044 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 882675a6-4e39-3f91-8dc0-215dd942b9d1 | -12.63042 | -53.12084 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b12296c0-1999-3f4a-b890-bbf9dde03041 | -12.63034 | -53.12438 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f494d09-e051-30c9-bf4f-5c65efc5b9b4 | -12.62983 | -53.12477 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a780bb0-8701-3290-aed3-a5a107566c9e | -12.62856 | -53.11203 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc7c850a-b600-3202-89d2-10125fa0a35f | -12.62811 | -53.11244 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94f63227-adb0-34b0-9087-e5a7b2db2722 | -12.62799 | -53.11597 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3644cdff-73fd-3b8a-bfcc-c66937500682 | -12.62752 | -53.11637 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad1347b9-d964-345b-8654-82681b9cc3a9 | -12.62742 | -53.1199 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02b80e8c-4a86-3496-b660-c76c0260753d | -12.62693 | -53.12029 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76805b2f-3091-3025-aef3-bb6218c172db | -12.62684 | -53.12383 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e8d99e-1442-3476-8ded-6f3092ad17b8 | -12.62634 | -53.12423 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4062ba14-3130-3d03-a913-eeedb44a0ce3 | -12.62344 | -53.11976 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 332b8bcd-702e-344e-a447-c44e73316439 | -12.60828 | -53.12546 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c3b15f3-fce3-39b3-809f-f71eacc82377 | -12.60479 | -53.12492 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4428bae2-39cd-3a4c-ba0e-d5c5e1b33b27 | -12.6042 | -53.12885 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e89e1cda-046f-3ba5-bba5-a590c8f0867e | -12.60188 | -53.12045 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a27cf3-ebc6-3d90-bf6c-51ad06e41c75 | -12.6013 | -53.12438 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f36a688c-49a3-33b2-80d7-b48d8a8aae3f | -12.60071 | -53.1283 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4c4e00f-2251-3367-89af-102200f9b8f4 | -12.60012 | -53.13223 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2c5946e-b75d-38b6-a741-f13fbd88a15f | -12.59954 | -53.13615 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84317713-b36d-3294-ac7c-88ffdbee7854 | -12.59781 | -53.12383 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72372cc1-3d2e-3742-877e-c24c7e5c19a8 | -12.57801 | -53.0645 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5a352c18-90f0-384a-9cae-a9a3bf99674f | -12.57743 | -53.06845 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 227d96b4-eb47-33cc-9565-2a1bad7eb111 | -12.57451 | -53.06395 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 914c2dad-8504-369e-a942-8fed0ea277d0 | -12.57393 | -53.0679 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 43b24874-54c6-3803-89be-cb7ecd85c7ed | -12.57101 | -53.06339 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8a614001-7671-3737-8d37-a834a898c3e7 | -12.57043 | -53.06736 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| cdc91b95-da70-3af3-86fc-0273215b49e9 | -12.56751 | -53.06284 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08683d32-5df6-3738-a259-b4637fedd0c4 | -12.56693 | -53.06682 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abb6d685-7150-33bd-a0df-439f9b184c74 | -12.56343 | -53.06627 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cfd5c80-7c7e-37a6-bd92-d33a63c955b3 | -12.55643 | -53.06519 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a194df13-6f57-3e2d-ad24-e174fd915c22 | -12.55351 | -53.06068 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92880e6b-f6ab-388f-b9ca-4e886603f746 | -12.55293 | -53.06464 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a602eb2c-23f7-3022-b93b-8df9de623cda | -12.48603 | -53.14771 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5274034f-1905-35d4-8143-0f32afca9b60 | -12.48254 | -53.14718 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a00a628-17d6-33a6-bd8d-bcb8564ad94d | -12.47964 | -53.14271 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fda4b732-5a55-3099-971f-bd647ca443fd | -12.47905 | -53.14664 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4481e48f-4a66-3db4-b90e-89a8bfe10052 | -12.47674 | -53.13823 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcad467e-0807-36b1-9840-d6be5bbcafa4 | -12.47615 | -53.14217 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38371f5b-6059-3966-8d35-5cda6273f9db | -12.47382 | -53.18171 | 2024-10-08 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 154d1ac6-2711-38e9-9afe-b5d1ae8736b9 | -11.63514 | -54.99685 | 2024-10-08 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 397ace98-2deb-3396-886f-b26742610c96 | -11.3344 | -55.23048 | 2024-10-08 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8b40046-a8fb-3df3-ac04-7584392c39c0 | -11.33182 | -55.22957 | 2024-10-08 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a56e08f3-c134-3029-80fd-4a80c6fd9511 | -11.3285 | -55.22903 | 2024-10-08 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8c3e6bf-d330-3ed4-ba04-c20909cb462f | -12.66624 | -54.71369 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47dd6a65-6857-3673-b2ab-fcde0aaa0c69 | -12.6629 | -54.71315 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfaefb61-96ca-3e3b-ad3a-dda153990226 | -12.66235 | -54.71672 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11bfc715-cf59-32f0-8ad7-bbcf63257a62 | -12.65956 | -54.71262 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f960b832-4021-379a-a1f8-cd6f429d3a8d | -12.659 | -54.71619 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fbc0809-f8ae-3e1e-b8b1-87005829b751 | -12.65843 | -54.69775 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9381c0ef-2026-3d60-aadd-cab7ac98f8f3 | -12.65566 | -54.71565 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b61c968-2090-33ab-807b-d463cdb88458 | -12.65508 | -54.69721 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f433f6f7-7c01-332e-bab8-227415526d01 | -12.65287 | -54.71154 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b67d7ac-3a91-3c5b-a428-2213600b7c12 | -12.64729 | -54.7033 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ab87526-7248-3cc6-b9c7-7ebfaf57f990 | -12.63502 | -54.69398 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2068fe7-8550-3884-9ac1-813261e7d379 | -12.44526 | -54.45477 | 2024-10-08 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94ec57d6-835b-3977-96c1-a25e80444e92 | -7.97598 | -54.77825 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6ab305b-24af-3985-8637-3cb10bf41857 | -7.97543 | -54.78173 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4166173-3144-3b7e-9a3e-9ab13113f116 | -7.97265 | -54.77772 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d53e570-ec94-3c4e-a1ed-f472dad4ac8d | -7.9721 | -54.7812 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 571d2d94-0981-39a0-8c7b-cae359edc55b | -7.96933 | -54.77719 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05a14167-f369-3a4b-85a1-3692fe2defbf | -7.96877 | -54.78068 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8a4793e-6f1e-31f7-ae8f-c71a15d469ec | -7.96822 | -54.78416 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f6bc664-8a84-3404-8c64-f932a5facf5f | -7.60907 | -55.29988 | 2024-10-08 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57de89a5-bd39-33f6-a0a2-0a0147af5cf7 | -7.60851 | -55.30341 | 2024-10-08 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9182cf25-1b65-3117-b2f0-1a55471734bc | -6.82668 | -55.32465 | 2024-10-08 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 318949c7-8e51-34c1-b6e4-8f301415d3d4 | -8.62156 | -54.93184 | 2024-10-08 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f0191e6-8e70-39ab-8fe7-d383cfae7560 | -9.88196 | -56.44088 | 2024-10-08 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19e138a1-195b-3f01-a57e-25ee25a15f24 | -9.81141 | -56.4221 | 2024-10-08 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e268569b-0f72-34e6-a06f-c6caa00c2072 | -10.8227 | -55.72588 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17ba793c-1e7d-3436-8a5f-8024667e9288 | -10.82049 | -55.72503 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4373b1ea-ad7a-36e7-b1ea-f3b6fd892c9b | -10.81149 | -56.2667 | 2024-10-08 04:57:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README87.md)
