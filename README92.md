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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 296ec8a3-8f9f-3704-87e9-743e72740bb1 | -1.14717 | -51.67688 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bae22f5-4a9a-3a7e-aae8-aa3d54e036bd | -2.98071 | -53.89956 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d3b6368-0353-30c5-bc5c-1f9a2025b6f6 | -1.1565 | -53.68618 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bae83a32-c2d1-31c1-ac11-6448cd782a97 | -2.71093 | -46.12948 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bcbaec0-4bd8-3bf5-adc5-ee595948c02b | -3.68746 | -50.92334 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b6d10c5-e9fe-3d3e-9a1e-c822d569e604 | -2.87324 | -54.00191 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fe88ec5-7ba6-3a20-8083-61f92775db1d | -3.41575 | -50.24556 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c8c8b6-2158-3890-83ba-5eccccca771c | -2.85419 | -53.9486 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ac30c40-943e-34c0-8e13-d74df5fd1c45 | -4.11532 | -54.40942 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1be9f01-12ff-3d40-86c7-bb0f1ef44b81 | -3.29458 | -53.83575 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4821856-ed8d-3f74-89fa-8fdd28e89b7d | -1.61874 | -53.88628 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 423c4c94-7f59-34a3-b1e3-ec5c9635e935 | -2.82547 | -54.06626 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b5996d5-192e-3dbc-83e4-865f8332e814 | -4.31134 | -48.21325 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1927bd1c-8b95-38b0-8aeb-f647abacf23a | -1.18914 | -51.77248 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a18fcc3a-728a-3d2a-ba87-26abd9d182ef | -0.90644 | -51.64578 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0eb4bf0-b6a4-38e3-a858-88e369d2ea35 | -1.21313 | -51.73515 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa1bf11b-f0d8-3cde-8edb-0bb10e2359ab | -1.14096 | -53.698 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3726efbb-994d-3b4c-b4f9-901c0989c147 | -1.09436 | -53.61202 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fa0bb14-c6af-3774-804a-5b4236fecbbb | -3.03762 | -50.97893 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d8b874d-1b39-39ee-9681-2010462a3f72 | -2.80081 | -51.58872 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2201e7a-0ca8-3894-bfe7-8f7b944e5666 | -2.2435 | -48.2586 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61255c41-77dc-3c26-b71e-0781a5557a86 | -2.24109 | -50.48113 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39770738-6b60-3805-abd1-0bc2c2cf9724 | -3.04966 | -49.36847 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b357a46-fb02-3a8c-927d-d6ee7f33b55d | -1.82981 | -46.301 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b57a2d2-4e57-3864-b45d-db2c02ebcc9b | -3.48199 | -50.25193 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 641e032c-b890-3299-9263-43825f8dae4a | -4.20363 | -50.68478 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bbd45651-644d-305b-ac99-3ae6020c2e5f | -2.9779 | -53.89553 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 800e2375-ef1f-3ef0-be6d-c73dab7f09c2 | -2.9031 | -54.77777 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5d12310e-4d74-3474-b586-3d9a6f6ebf69 | 1.21175 | -55.93281 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70c14299-03b5-3222-af7d-1d68c0e4557f | -1.13898 | -53.79762 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 689d839f-4f0d-3699-bb6a-40234ce24704 | 1.88155 | -55.72552 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b211e95-b53c-3a6a-8c44-009b7cb0697f | -1.13708 | -53.70096 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c43a65-b055-300d-bfd2-3bd71ca243d7 | -3.02933 | -51.53291 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81254b3e-bac0-38b7-806d-b14ab04a029a | -1.23151 | -53.36225 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79a7a220-6278-31c6-876b-53a397957f21 | -1.6415 | -53.87184 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| baa49d59-ec5c-3d50-a69f-a56d158ae156 | -2.96627 | -53.94783 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e781bc-9e14-367b-a639-f47f70c5d053 | -2.71569 | -48.59723 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a77bbd-7d51-34e8-b091-1206e5f0cf4b | -2.60439 | -54.07443 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37033a21-ad85-394b-a6b2-5bc782721bf6 | -2.77863 | -54.21253 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e87e0275-995d-35c7-b4e2-e686f9aa514d | -2.8788 | -53.32427 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ccc01d57-a30b-3259-a08b-49c4da6331a8 | -1.57757 | -52.01125 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cc14fc4-2f78-3c12-977f-009dc3aa8c6c | -3.31994 | -53.29412 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09f6010d-977e-37a8-b206-fe95b387211a | -2.78893 | -52.983 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb031f8b-a511-304b-a823-91b746edb64f | -2.79735 | -53.04149 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e33c074d-2143-3f41-aafb-fd804e1fb07f | -3.72446 | -54.52702 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88cab175-a60d-3c46-aaee-507c4025c312 | -1.14119 | -53.78356 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9134e495-9b49-3109-9699-d8591a6f9f0f | -2.82761 | -54.03073 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a3d719e-20f3-33bc-87c9-85aa14e0ef2a | -0.35628 | -51.72882 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17780916-ef55-3cc0-b6c0-54d92045a3d6 | -2.61391 | -54.33953 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc76b5c9-f602-31b0-91f7-4696b06faea7 | -3.41202 | -50.32349 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e503c42b-9303-3446-ad18-2ef842446760 | -2.60585 | -53.99958 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e24a4fe3-6e05-3ab0-877d-e74d2d6fd63c | -0.2772 | -51.63676 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 644812f1-e47c-342b-bc72-dcab9ea060c0 | -2.59055 | -54.09727 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faa120b7-5680-3688-b205-ed0aedda4f07 | -2.63887 | -54.07261 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba40a3c3-efef-3767-98da-8bdb0ed58bab | -1.18377 | -51.76892 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f70d038-3b9d-3d10-8a7f-e8d1bc6b5fa8 | -2.82492 | -54.06976 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97720fd7-1fed-3ebc-8f08-0c146cf347eb | -3.22725 | -54.17868 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9610a26f-e1f6-3abd-aa0b-baa5bf7f9e8d | -3.10507 | -53.81703 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b22f7c1-50a2-3805-8678-af42d97786fa | -1.58251 | -51.27703 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 554d1a09-65ce-3b99-a4f8-cc3a9ffa1b5d | -1.26471 | -51.75544 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1553055e-865a-3327-b7c1-9f4c8e9b08be | -1.57813 | -52.01185 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c838562-0d1f-3a0a-9943-57ff104755d9 | -3.46867 | -50.52912 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c99c43a-b05c-3f5d-b624-23320dffa62d | -3.62365 | -42.73494 | 2024-11-30 05:01:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c27f03e4-a88b-3fd7-afd8-6ca0716052af | -2.60494 | -54.07094 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ac1128e-bb49-3ef8-8490-7bb9e1b057a5 | -1.45843 | -51.49872 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 797c1c4a-501a-3889-9931-df9c19dc9439 | -2.77019 | -54.07933 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76b5f686-f606-366d-8d0d-d680fc45ba68 | -2.78564 | -52.86823 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e7b7fe3-e681-38b8-af20-cc29603393d8 | -2.88659 | -53.98242 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb084ff5-3d9d-3ca8-a8fa-c823aa685270 | 0.0998 | -51.46814 | 2024-11-30 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 154c267b-89c6-3bb5-989c-830a47ba2124 | -2.82777 | -54.09526 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74765d02-57e5-379d-9196-5236f9b74421 | -4.30959 | -48.20954 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa6f54a5-2e01-38dd-81ca-bd817a6fbde6 | -2.58965 | -48.2019 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab747ef6-d48f-3e19-832b-e0b0cb1eda02 | -1.05871 | -53.21611 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2689aa6-a80c-3229-a7f8-4e6f7d92c43d | -2.04541 | -51.19423 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05a4cad4-5482-34cf-bbb9-4d64450d7816 | -1.36734 | -51.97227 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 611912fd-e4ee-3774-b2d8-5274fbf4236e | -2.67284 | -53.34783 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff8c2f64-9a7f-3dfe-ab2a-2c42a64bce29 | -2.83117 | -55.66637 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b53794-b824-3377-9755-96e318e1294f | -3.21911 | -53.62715 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72552664-a256-3b8a-9b44-fcfec2a4af9b | -1.19793 | -53.87431 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79004411-b7f4-3c76-8ac6-c58395536d82 | -2.46928 | -53.68685 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bfb22d8-7a9f-33a3-9540-9bb63f4c53fc | -1.14452 | -53.78408 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81e74282-68bf-38f1-b25a-18f5f450a151 | -1.72941 | -52.49909 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f25a68a-fea3-3a3b-b05f-7a72844b862b | -3.0232 | -52.38308 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b485d4c-ba4f-3ad8-9d34-9256544d54b8 | -2.97147 | -53.73868 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e430023-50ad-3ccd-9872-62a238809c79 | -1.96867 | -52.89464 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b141c248-134b-30ed-8d02-8ea36f05dccd | -1.44715 | -55.19335 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ba082d3-6a74-3c25-b286-9e45b3da252b | -1.6644 | -53.20926 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0cc857-e9fc-374d-861a-6a2bc3132250 | -3.26161 | -54.11226 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f772e40-2364-3a22-aedf-66e27d0efcc0 | -2.79759 | -54.0476 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d487ee7-5156-389b-a5ff-ec503dc0bec3 | -3.22592 | -53.06776 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d5fe824-d07c-3fb0-9eee-2152da407419 | -3.05434 | -53.67801 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea04e91c-4145-355e-b54b-a3370996da58 | -2.89784 | -51.36827 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55d0f9ef-1ca7-3cad-a5cf-30ac267e515a | -1.05589 | -53.21206 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f60c99b-cb30-32bd-952e-5fbb149595bc | -1.06693 | -53.21708 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60d3664a-6367-3857-ada5-17a30a3e7af8 | -3.10197 | -54.03338 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79555da6-8b6d-3f17-99cb-bc2997e53943 | -2.95889 | -53.88531 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8740b1ce-3719-3576-a213-79cade157b8c | -1.26053 | -54.55279 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc3cd997-35bd-3234-b6b2-7b6c7e41506d | -1.61314 | -52.29153 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef03d17d-d2ec-3729-8362-deb8dd113efe | -2.84167 | -54.09384 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3f35fe7-0760-3093-b273-72a589571e4a | -3.16116 | -53.23562 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README93.md)
