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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 299660ae-1049-389c-adb8-b05351df92e4 | -10.88255 | -46.03536 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71e821eb-dff0-3e4b-963d-2e853de30ec8 | -10.88195 | -46.03934 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d782060d-7c9b-3b7b-b783-27d89dbb2423 | -10.88136 | -46.04334 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d877cde6-c6db-3a54-9436-7e6a282c8399 | -10.8802 | -46.02685 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88b955a5-f500-31e7-88a0-2c161b869963 | -10.87961 | -46.0308 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2737636-7b60-373b-baca-9b1d2ad75b77 | -10.87376 | -45.99722 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6303047c-9506-3d5f-b83a-666c6a8bb092 | -10.87373 | -46.02181 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4defa09e-4cf9-339d-ab06-425106fffd3e | -10.87141 | -45.98862 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a857f4af-7f08-3806-b3eb-8fc08e9a6bb8 | -10.87079 | -46.01728 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ef2fdab-481e-305d-9392-0fcc0cd5ed5e | -10.86907 | -45.98001 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc281b66-8d3e-3d39-b8b7-23532f2e08e2 | -10.86847 | -45.98405 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c736d1b5-c20c-3f3a-8eff-723dd3b18eb8 | -10.86613 | -45.97543 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e119acb5-0127-3cf7-9a12-e62c12368d21 | -10.86553 | -45.97947 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89ea6157-3823-3bb3-a23c-af87c545848a | -10.86259 | -45.97489 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0a27964-ffbd-3243-ab58-a89e6c04f99f | -10.85964 | -45.97031 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6196d8e7-b442-3d74-ab0c-4619870032fb | -10.8561 | -45.96977 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e614e271-f57e-3eaa-9318-54505cb8b877 | -10.85256 | -45.96923 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62c00f77-3d4d-3a5d-aa99-8c4f6a0e49e3 | -10.85021 | -45.96059 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a6ba47d-7785-3815-b042-4625a3ac73fa | -10.84962 | -45.96464 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 538257ea-d729-3211-a490-7454bbd5acd0 | -10.84667 | -45.96005 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b413105-3ee9-3184-91d3-376dbbd2069f | -10.84313 | -45.95948 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a686a1e2-cef7-3654-8cd5-7070955abcdf | -10.8396 | -45.95892 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8e8e510-a805-3f8e-8e78-ea1510e469b0 | -10.83252 | -45.95779 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2278cf1-7e2a-32cc-b75f-275e4584a740 | -11.248 | -45.66262 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae737d96-371a-3769-9c2a-16582a34c4bd | -11.2474 | -45.66678 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00b78f37-fe72-3e67-85ab-4bcfe6b1e6a2 | -11.24563 | -45.65365 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c793d7d-1fe5-3008-8f1a-1bf508d8b283 | -11.24504 | -45.6324 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52a3c255-67df-312e-a810-06396452699d | -11.24502 | -45.6578 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b17d743-c0eb-335e-a113-12cb7f6cbaa7 | -11.24441 | -45.66198 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9a57335-b190-35c7-8dca-fe8f0427673e | -11.24382 | -45.64072 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eda605d-9fea-3356-b90c-6dfcc592592f | -11.2438 | -45.66618 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc5f2e21-7f7c-3463-ae23-5d0e99bdcc8a | -11.24322 | -45.64487 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3ba4995-0496-3175-8892-b9d2714ce1f9 | -11.24318 | -45.67039 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b977aecc-136f-36fa-87dc-932d224c4f82 | -11.23784 | -45.63115 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bcf7898-c7a2-3cae-822c-4ed1b51dd459 | -11.23483 | -45.6264 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f122810-5c95-3931-b178-b7025f3ab48d | -11.2342 | -45.65612 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d876e301-611c-3e3c-a61e-f0fe16fabc5d | -11.23059 | -45.65562 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c956495d-efc6-3b51-a379-f3d87bcf9087 | -11.22882 | -45.61691 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1e4861f-93d7-3f56-8f6e-c8e90ece6e2b | -11.2222 | -45.61161 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c64aead5-b9e4-373d-80b6-def9b641a0c9 | -11.21972 | -45.65427 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef6a4c4a-2fd3-3907-9cbf-6eea3b9a4bde | -11.21911 | -45.65852 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fc3b1ec-045a-3441-b8fe-01e50a65de77 | -11.218 | -45.6407 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dd85bc5-9405-3205-830f-9b9ccfc9369f | -11.21613 | -45.65366 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbbc3a2c-c620-37eb-a6cd-6f54ec2ab7c9 | -11.21551 | -45.6579 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3a07f4a6-4c69-3a9c-813c-cb5ad22c355d | -11.2149 | -45.66211 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f1c5c78e-64a5-3a39-98ed-a3fd5e1b8c96 | -11.21438 | -45.64017 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b5ab195-3682-3b2d-9b64-ba5a6155ac1e | -11.21429 | -45.66634 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b7ca8886-93fc-32ab-829b-544097ee22b3 | -11.21139 | -45.63536 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0475fac0-adda-3a39-a213-9e058e277568 | -11.21131 | -45.66148 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 727b7f84-786b-3a55-941c-789bc4c46a4d | -11.21126 | -45.68735 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02bd971b-6ada-3e51-97c5-7f626da14d8a | -11.21077 | -45.63962 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ac0d4dc-8d3c-39f8-a93a-6954c084841f | -11.2107 | -45.66571 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 550d1776-f895-3698-bdc4-4e126fc9d7e7 | -11.21005 | -45.69569 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ca2b193-b0ce-33a0-afca-a2c58487889c | -11.20944 | -45.69992 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e2b26dcf-f811-3749-9390-8a0ce1bb108f | -11.20882 | -45.70417 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e20ed0c8-202e-3e0e-b2cc-287292ef726a | -11.20839 | -45.60489 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc5496e7-d94a-34b6-b6c3-6d245f43d490 | -11.20827 | -45.68254 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a20dd0e-25bc-38ca-953e-de422e44c794 | -11.20766 | -45.68674 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d95353-e4bc-37f1-84c6-157f8123a5fa | -11.20644 | -45.69516 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03392804-8a9c-3e13-b9b3-9ff54b51ed7a | -11.20583 | -45.69943 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2b42bcb5-f198-351b-b45d-3756fe83cfa8 | -11.20478 | -45.60424 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b20fd0b7-2846-3058-b624-85fea4a20f55 | -11.20347 | -45.60517 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c172701-67ab-3e9b-b032-d40dbd68987b | -11.20116 | -45.62948 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71d85189-aca9-36b2-af3a-5f2914e2e2ad | -11.20055 | -45.63375 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9b02bed-5d41-3561-9290-889227a0f01c | -11.19971 | -45.6304 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f241b500-e923-36d0-8e2f-7aa8d99da5f3 | -13.17379 | -45.45723 | 2024-09-30 04:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68e12a12-d12e-3f5b-9cd2-f78ab46f2281 | -13.17183 | -45.45513 | 2024-09-30 04:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92de6d77-fea5-3515-a6c2-a6cbca4f2a7b | -12.72905 | -46.41842 | 2024-09-30 04:32:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 472caea9-b167-3c01-a518-c763947f556a | -12.72846 | -46.42245 | 2024-09-30 04:32:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50e99590-a04a-3496-bb88-0c60630ba79c | -12.72493 | -46.42187 | 2024-09-30 04:32:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 88c9d9e9-647b-3639-a932-ea0ff89a0c9b | -12.72434 | -46.42595 | 2024-09-30 04:32:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a929173e-9e32-351d-9510-9259bddc45b8 | -13.25653 | -46.36334 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a889d50b-55b4-31e2-9d69-4c668a06d07f | -13.2537 | -46.36387 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7359201a-e51b-3e2b-90fe-7d50e11da97d | -13.25296 | -46.3628 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd3ca936-4fef-3b3a-b68d-2659f44217a7 | -13.25238 | -46.36687 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 067de774-fdbf-3d39-89c4-2a0dc370e2ca | -13.25195 | -46.35104 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4cab990-404b-361e-b90a-a506390a204e | -13.25134 | -46.35518 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4457c823-ab99-333b-a6be-51f9a84ca14b | -13.25074 | -46.35925 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3645a346-29d0-35a6-ab6c-9acfa14b1e68 | -13.25014 | -46.36333 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c6ca37-00cb-345f-88d0-9d4966720674 | -13.24717 | -46.35871 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd965ea5-febd-3bc0-8e67-b122ba1d5d72 | -13.24186 | -46.34531 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0edfa36b-e198-3597-9126-e498f7010a70 | -13.24064 | -46.35356 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c9231f8-c49a-32b5-87e0-510dd5a87e42 | -13.24004 | -46.35766 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc4be449-ff67-3b99-8f83-8cd882436ff4 | -13.20616 | -46.31506 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 328bdc4e-7f18-34d5-8eac-12d9f2b6ce89 | -13.20441 | -46.35222 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45989b79-3128-3177-8619-974952c01a69 | -13.20261 | -46.3144 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 360ad3ed-9dda-3f6c-8da2-086b7f80d483 | -13.20204 | -46.31833 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f06ae7b-cce5-3ac6-86aa-488427e886b8 | -13.20146 | -46.32233 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 025bea2b-0725-3117-ad18-4a58a03c54cf | -13.20145 | -46.34755 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95daf71b-6880-3393-8451-ad2825d2b4ec | -13.20087 | -46.32643 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e2c66c6-ed1c-323d-9973-3caaffda71c0 | -13.19962 | -46.30991 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d41298ca-06d2-33c1-8bfe-77b844c06d24 | -13.19848 | -46.3429 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3212fc5f-f7ee-33d1-b4c9-93f5e7dd669e | -13.19788 | -46.34705 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0ba68f9-cd90-3b62-b02f-74c70b33788e | -13.1973 | -46.32589 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 28af4a3c-9038-31b3-8787-319eae95e1d3 | -13.19728 | -46.3512 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a35b1b40-8cdf-3f1d-9caf-fc3e76f93e05 | -13.19671 | -46.32999 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d9f9b370-3458-3c33-b9c3-3164b5746a5c | -13.19668 | -46.35534 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dd650b7-1f42-3758-90b7-7e7821b04fa2 | -13.19611 | -46.33411 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 605f5424-1b76-3272-9dc6-abcae254cb03 | -13.19608 | -46.35946 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a930fa4a-60c8-399c-8a3c-a94a5e263570 | -13.19551 | -46.33825 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README36.md)
