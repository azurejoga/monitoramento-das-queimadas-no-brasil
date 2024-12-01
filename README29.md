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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5a4cac5-fcbe-3196-b83a-11c43aa5328a | -2.80192 | -46.82008 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db5c2690-a371-3a8b-a7e5-f83822a5ec14 | -3.11053 | -53.76036 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa589b64-11c9-3ceb-a909-063b5740f77a | -3.98001 | -46.75479 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc89b258-1819-37c2-b078-6eae74c47dc0 | -1.19575 | -51.7473 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d632538-a396-3ec3-bfbb-a31a1e8703b1 | -3.85354 | -40.98237 | 2024-12-01 04:21:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 3f5b278d-9990-3b3a-ac43-3a86428fa7ae | -2.62677 | -54.21621 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78357245-cca9-3db4-b4b1-f5ba13380c1c | -2.29822 | -47.28349 | 2024-12-01 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42b2a08e-d61e-34cb-b214-d87d5369fab3 | -3.60653 | -50.37643 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffc88447-01e7-3c59-87bc-3cbaf81a4f70 | -2.11886 | -46.55623 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f02fc06-39e7-387c-ad05-08f969e101a5 | -2.83737 | -51.28396 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c105170-3792-32f9-ba1b-9d6c79153db9 | -3.05622 | -51.06477 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0e00c3c0-639c-33c5-99ec-94c60687197c | -0.82077 | -51.61293 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62323981-8f41-3db9-b617-47e0c7691a55 | -3.33287 | -50.22213 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20aa3831-b2a3-3955-b74c-78dfff222b64 | -2.86712 | -53.99739 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c116d5e-7c94-3acc-bac5-0e8a04c70e48 | -3.2655 | -50.20322 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cdbb0b7-efc1-3475-a16b-b8b11dc3c129 | -1.51653 | -45.9068 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d237a0ee-954e-322a-b952-c5121849641e | -1.49198 | -52.64643 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 46d6939a-34b9-3668-bcf5-480231a539c1 | -4.68658 | -42.36322 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 812a6f42-dd7b-3d0f-81d2-4c83c781dfea | -3.68442 | -50.24179 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a88a90b3-1f3d-3f5b-8e70-c26bbc906214 | -1.69734 | -52.64315 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 571bafc3-4477-3d36-97a5-c01e28deb449 | -3.46799 | -50.53407 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7dd71552-e86b-32ac-86d0-ca303adac247 | -3.35879 | -43.16914 | 2024-12-01 04:21:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65de1568-5acc-3fe4-8991-f33a16318e4e | -2.56309 | -46.56773 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66c46370-bf98-38ae-bee2-9e7e7bece510 | -1.0709 | -53.6314 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d9cb2a-6f8e-3dd6-8988-fc73543082f7 | -2.71653 | -46.13181 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d6d176c-02af-3903-9b3e-e3033ff3bd6c | -2.34353 | -45.78392 | 2024-12-01 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26484506-cffa-3d54-a990-863229595d79 | -1.1865 | -52.12573 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5baeb119-a9bc-383b-854b-fc22871cf7d4 | -3.84837 | -46.52022 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96ce47a8-f099-3f03-ae54-15fa3ea0bc6f | -0.2591 | -51.49826 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 382ce3c5-c822-398e-b36d-1ddd2fcc52e7 | -2.66813 | -46.1284 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 006b5f0a-ff76-33e2-95fd-785eb901f498 | -3.06364 | -50.32784 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0f60204-3ad1-305a-a590-158d4605be52 | -3.03321 | -50.24265 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c72c9f92-fab5-3a20-a2c8-98451558fa3e | -1.54945 | -47.15854 | 2024-12-01 04:21:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 806de7a5-d8d5-38a7-b006-0d1c556076e3 | -3.57447 | -40.99353 | 2024-12-01 04:21:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 912e2a50-72fa-35c8-88d3-cf0b0e6f5e02 | -2.03669 | -51.19814 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d812931c-5a22-319a-9683-3cd68437b591 | -2.64066 | -46.12417 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 981fcf97-af30-3196-b8f2-dd2befd42eca | 1.25754 | -50.68779 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f708bee-eb3d-3123-87b1-a469dfbcdd20 | -2.04401 | -54.67263 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e226b95c-01dc-3616-985a-42e7bb7ee4a3 | -1.41224 | -46.59729 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5ed1b3c-0070-3eda-a376-57f03a82027b | -2.10144 | -46.34025 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1449fbcb-587c-3fc8-9df0-fef9396a07b2 | -1.59647 | -52.53645 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39b73d7e-17f4-3a67-8c0f-6e826fd900b2 | -2.72633 | -52.9748 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac2b7310-7ad3-3580-961c-1f2c664baf1e | 1.14618 | -51.14832 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d48fdfc6-e7d9-3e90-8df8-d69fa5b53a1d | -2.23251 | -46.40315 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6fd92bd-5d61-3714-94ce-e2d335ff7a80 | -1.59597 | -52.53955 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 309872bd-83d7-39bc-9128-8fc79f6d70ea | -3.91096 | -42.41283 | 2024-12-01 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f9039c5-8590-3840-bd48-a0245bc1361e | -3.01191 | -51.78729 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dd403f3f-d96b-37d3-a9c9-b12110e0946b | -2.37755 | -50.38151 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aee8d5f-6d66-33c5-a9e5-9873bad38b23 | -4.69229 | -42.39494 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0db757f6-e85d-3af7-bef7-7dcc2539e5cd | -2.91126 | -54.1129 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8f9d0dd-6969-34df-b325-4fdb87556b12 | -3.14891 | -53.83866 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebf874d9-3435-301f-9363-6e2be3cfbe69 | -3.14045 | -45.98162 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9995d63e-e9a2-3808-8011-24e65f740519 | -3.03821 | -50.23922 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08f1f86e-39ff-3520-8e47-044b5bf7e65d | -1.49414 | -46.31145 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61263642-554b-37f3-976e-5e3c17b22894 | -1.48682 | -52.67822 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db63dcdb-623d-3bb8-b49b-c5cbfa16d66e | -2.06642 | -51.19264 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88380c99-1d2d-37c0-a215-11fad0defa4b | -2.77044 | -55.34809 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8af5c82a-5da2-3ee1-b699-44f060a1477c | -3.41552 | -50.16414 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a1c97ca-824e-3728-8fcb-8ae0e4b3449a | -1.23806 | -51.79955 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8cac34d1-ba16-3bd4-b48f-0c4c38f26ff2 | -1.14624 | -48.32772 | 2024-12-01 04:21:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8def4dcf-5b8c-3bea-9b5e-fad9745f642e | -3.85976 | -46.53738 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f43bbe-2fd2-3052-97ad-dfe7a53d182a | -4.04935 | -46.82384 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2ed8d2b-2edc-3dc7-9fb9-a4e88744321a | -2.98646 | -45.57586 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 36612532-4fb6-3cf8-9ae3-cb5f82f37a6b | -3.28597 | -50.62652 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1559c62-2551-32b1-9430-c9f0002534cc | -2.80055 | -53.04794 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f352861-35b9-3a15-a895-b8b53d2aa0c8 | -1.07151 | -53.62769 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf8a5e76-ad7d-3110-86a9-24b99fbebe1d | -2.96785 | -48.04205 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ebdd611-451a-3e13-b9e7-6ed07f0ca672 | -3.98308 | -46.73543 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a8b693-e064-3ef8-83c8-dfe2762aa70b | -3.99697 | -46.64792 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e73e7ad-cf67-3ab9-9db7-86b1e6247166 | -1.95055 | -53.34148 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1246e3a0-6ed0-3258-9fb7-edcd75a2fa6e | -2.8746 | -53.98705 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 550d6af2-7a1a-3654-86ab-1c95914969ac | -4.17286 | -46.55505 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ea85638-0a5a-36de-a0ae-2169af78a97f | -3.99404 | -47.91296 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b4e0c6c-9a8a-3b39-9f37-1229eb0a12ed | -3.41692 | -50.42863 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f6ae334-eef8-3319-af42-58723f63f867 | -1.70405 | -52.44123 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f494fbe-1d3c-31f4-95ad-49f9d85d74ad | -3.65642 | -50.70723 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f40b6456-fa3d-3e45-a0c3-889a84d90b1f | -4.5223 | -42.93507 | 2024-12-01 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e04fe39d-769b-3cb9-ab24-5488ba8017a0 | -3.77188 | -46.6951 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 227a2637-c2ca-38af-b364-148d87f9a4ec | -3.29811 | -50.7978 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b6e3d97-cda6-3736-88cc-a5fdb9e013a8 | -4.44483 | -45.36327 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c33930b-6ac7-367c-b8e6-a5013df41197 | -3.37064 | -51.12838 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4d7a7a4-deeb-378c-bc5e-75e75d4ef52b | -3.1554 | -50.62408 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a4b2d8d-6add-3b6d-84fa-15065a71c482 | -1.19979 | -51.7536 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23836003-9b7c-38c5-85c2-460e69540182 | -3.82625 | -46.59818 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c428066d-d027-3c45-a6c2-f6af57b0446c | -3.96728 | -48.19756 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d405635-1202-32e4-8192-b7c8651b3c0f | -3.40771 | -51.97599 | 2024-12-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3bf4e11-a38f-3e0b-aad5-ec22bcae43a9 | -2.04542 | -54.66405 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a045be1-1898-36f0-9967-6dc271408d4b | -3.46763 | -50.26647 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9b942e79-49af-35df-a57a-f55e1fd76e07 | -3.17475 | -46.32072 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff1d581-116d-3e10-b0e2-59c24cdb2b8b | -4.07147 | -46.81947 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5d687c4-3593-3391-b6bc-8d12f26b8982 | -3.44072 | -52.04675 | 2024-12-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 229a44bb-7a23-3990-a55e-93cf983b61e4 | -3.8094 | -50.06338 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9be5e4c-aaec-30f2-a7f8-a146129d4008 | -2.60932 | -54.28521 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c7fc613-d986-3aee-829d-9f10685bef09 | -3.09384 | -53.72469 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 192500c0-223e-36f2-854a-be103c07383e | -1.28203 | -47.90306 | 2024-12-01 04:21:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e87b2724-e8f3-3ed7-bc94-2a74fd2d5b50 | -2.6103 | -51.80778 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ba83baf-ded5-3109-8ddd-f2915d0e64ce | -3.69994 | -47.12527 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8d88808-699f-3b4b-a488-0db90b698eb0 | -3.58994 | -50.36948 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caffd85c-f9fe-3b4d-8ce8-99812f944361 | -2.10577 | -47.62524 | 2024-12-01 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa959d96-13b7-38a2-847e-e09474af42ee | -1.77988 | -46.37863 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
