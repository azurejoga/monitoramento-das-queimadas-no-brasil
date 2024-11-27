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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce99ed16-b3f3-37e3-91c3-120d611d9819 | -4.66917 | -46.38037 | 2024-11-27 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0f5fb93d-c8b6-37a8-874d-b9548f969f4a | -2.71187 | -53.18625 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8332b01-f1bb-3f4b-8ddf-ec0af95de8e4 | -2.25034 | -53.62981 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4a1a338-2d04-3cdb-8922-7e65a5c0756c | -4.19776 | -48.56634 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50f1082-36ac-3456-a6c7-f819900fa4cb | -3.55953 | -46.34009 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2f912f7-1364-36db-9859-f3e07d6da8a9 | -3.76643 | -46.67122 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c369772-be14-307f-a36d-965d1c5d4ed3 | -2.48066 | -48.84078 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec25fb48-a1dc-3d28-8d10-488444692fa3 | -3.71862 | -47.12568 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 029064e1-913c-3b57-a54c-8fbd51fc7c30 | -3.05498 | -48.70539 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e8e84c1-7ee7-3578-b69b-02b3f3e39dad | -4.13246 | -46.70618 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d7a98a-63ee-3ed2-9975-a2d1e429a1c2 | -2.8117 | -46.82308 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53601a4b-a407-32d6-ab14-d535910b5a2b | -3.18233 | -48.4333 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6519ef3a-14f1-30d0-8c03-31dbe2cf36ba | -3.72364 | -50.18423 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c203aff8-72cc-354a-94dd-6bc074d349c0 | -1.76451 | -53.62834 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45a2eb9a-baa5-36bd-812f-fc2f41510446 | -3.08665 | -53.26789 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67ef8888-fe32-37fc-b82c-d702c99d615f | -2.17165 | -48.3801 | 2024-11-27 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 152c6101-f83a-3060-8a35-37d688f8885d | -4.621 | -46.31441 | 2024-11-27 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28444c94-61d2-3b4d-9717-33b0d40d4939 | -3.71218 | -47.66799 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6b54061-5e15-30c6-bbff-534a063a2276 | -3.09642 | -53.27671 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af96b59a-30a9-335a-ad64-b72e6139871b | -2.59463 | -46.26181 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af2924b8-b583-3493-99c6-cf1584194805 | -5.20329 | -40.6331 | 2024-11-27 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3759b6a6-28e4-3f56-a679-c2840b012233 | -3.37492 | -50.1177 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9421dbe-77fd-3d2c-9c80-07207fdcd0d7 | -3.94316 | -46.71827 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2806f4d3-363c-3022-a182-0362da4c85a0 | -5.36716 | -35.61275 | 2024-11-27 04:18:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cec0c73d-614e-37b9-a538-20347eda61d3 | -3.57155 | -53.02377 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac960b1d-23ef-344d-b6dd-9ae527c72fa6 | -3.09474 | -53.28704 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0539dd9d-0d3c-3699-9934-7124a51e70b0 | -3.46988 | -50.25389 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 483caad3-8bbc-3e0e-953d-66d2eafd2435 | -3.11139 | -53.25927 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46c34131-e8f4-370d-8df2-dfd95d09a517 | -3.81034 | -46.60111 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66118cbf-feff-3803-ac35-18747cfdf590 | -4.00574 | -50.35105 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e1d10df-59ca-32a0-95a8-35ee2d8115c8 | -2.54366 | -45.39085 | 2024-11-27 04:18:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a0882116-0c04-3eb8-8dcc-de442cb3ccb0 | -3.05688 | -51.05947 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6eaae98-0c1b-3ae4-80dd-f39820f8e044 | -1.20334 | -51.75294 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97f7fe5-3672-3cfb-916e-f29f469c0ab7 | -1.79065 | -52.74854 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86b92163-aee5-3b14-999a-702c6471bf82 | -3.5954 | -50.38699 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb728fc0-c38f-336a-8bc3-1813ad2d4859 | -3.70777 | -47.12391 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d0327ab-f0f3-3a4a-a2dd-042aa05d4729 | -2.70256 | -46.19417 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa90a6d-c6ec-37f7-bdea-e78002d6069b | -1.72126 | -46.21997 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 340a71e9-5574-3d2f-9ea5-00c0ef4202f5 | -3.1108 | -53.25729 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 678b03ca-8bb4-3aff-a7b1-8c2ed4ca7df6 | -2.70699 | -53.18193 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d68f3a3-3ba0-348e-9945-dd30e91786f5 | -2.8275 | -54.12483 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7118fbac-5da4-351b-bbfd-649e35a2b029 | -4.01662 | -47.65311 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bda52d1d-0d05-321b-9c00-9badc996be0f | -2.54973 | -46.40805 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6134723-1d01-3722-95bb-94749f8963a0 | -3.08711 | -53.27002 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 062bf789-e6c4-3681-9672-ed0a7c18cf56 | -3.57615 | -41.9545 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| f2e743db-c047-3d79-aa99-82b0460264f7 | -4.02136 | -45.54197 | 2024-11-27 04:18:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47520e86-7d58-38af-943c-46c9da0cf298 | -3.24173 | -46.43512 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd5966f-5e33-3efa-b042-f4b30cf754d0 | -2.89054 | -45.25456 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d71cd0a7-781c-3a97-ac55-bda9c72b949b | -4.05403 | -46.83182 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aeeb153-e0dd-3ee9-915c-051c6adce965 | -3.90005 | -45.62331 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15c86b23-7d41-3c22-8916-e6f83c0d9741 | -3.10173 | -53.283 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b24ff749-f706-30d6-b998-2b6038932c80 | -2.69906 | -46.19361 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61c9401e-3198-3873-8007-27d6dd99843f | -2.82481 | -46.83358 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b3dbb0b-f1da-35a0-800a-8484ea51a519 | -4.50277 | -46.60249 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abe91e54-e7c0-3365-986c-3bd97c7b8b75 | -1.2307 | -51.79786 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22716c60-95f7-3ec7-9149-d33229f9a9cd | -1.27824 | -54.55001 | 2024-11-27 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9dd1400-d826-3baf-866b-c15a2200fe23 | -3.96638 | -48.07458 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6501f188-9b03-39be-bb2e-8260ad557be0 | -3.71434 | -47.12922 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a91d40f7-03af-39ab-a639-3893c54d94eb | -3.72743 | -50.18722 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ff50a51-a470-3955-b7f6-0f40dfd5a755 | -2.723 | -48.60065 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0157a36f-26fa-3808-947b-cb940448055b | -3.37055 | -50.11693 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 997138ba-8f54-3881-a305-69eda113412a | -3.84899 | -47.05594 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b7eb241-45f1-3994-b318-b486f1659dc4 | -3.60306 | -45.95414 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11b031c7-839a-3bdf-aa09-c00ecd0fe49e | -4.24035 | -48.67146 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d99eb48b-1d2f-341a-957a-722b1e142475 | -3.83067 | -46.56441 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e10bb70-79b5-3224-b7b6-768e1e01f129 | -3.09258 | -53.27087 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7d69a84-c441-33c1-8c6d-04ac8a20e4ea | -4.21363 | -48.66225 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fb05de5e-1ec7-3efc-a5ba-38b238ea59b3 | -3.18152 | -48.43827 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17622b2e-c2c9-3e60-9c23-0cba20ae5731 | -3.96332 | -46.90519 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5cdbc96-7f3f-3b05-9682-c23abf8f4710 | -2.00639 | -48.53659 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3456793d-a373-3763-9b66-4593ce45d95e | -3.58352 | -50.37619 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0627b17-e49f-3412-80df-6d100be4ab16 | -2.70422 | -46.20637 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04fbfad4-a902-3fee-9bc3-5bc8157ff4c4 | -0.26604 | -48.6 | 2024-11-27 04:18:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8282c0ad-9e2f-34a0-a897-ce7da0472c76 | -4.18439 | -48.625 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9bf6c10e-1082-3607-b71c-82f0e517816f | -3.64921 | -41.52982 | 2024-11-27 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 19cca43b-43af-385c-b802-37e232c1c4f3 | -5.19027 | -46.14233 | 2024-11-27 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28a37e39-e075-3f3d-a657-1c08150ed116 | -4.14529 | -43.80947 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9634d0e2-1e8a-3423-9c4c-5677210c0fb6 | -5.36148 | -35.61517 | 2024-11-27 04:18:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9d18343-073b-34d2-a888-7cf0a6119b9c | -1.7628 | -53.62906 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68beb85c-3d23-3017-b5e4-faa3a4d77624 | -1.36445 | -52.12577 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d08e89c-cb8f-3f70-9e79-34a586c60b3c | -2.80877 | -54.12997 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6214946-d9c1-3872-a13f-19aa82cc1579 | -3.27468 | -50.01701 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afcafcbd-f509-3219-8b74-3625bc0fd83d | -3.24234 | -46.43124 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31e5633b-a623-313c-a3c0-b7db5b1c2b77 | -6.90629 | -35.04145 | 2024-11-27 04:18:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ec4953f4-a288-3afb-ab26-4e6691d4515e | -3.69494 | -50.22285 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87503f78-6ef6-3a0a-ba34-668ce25c984a | -3.84578 | -46.65125 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c813f930-2d89-3909-9117-7cc13a5244b1 | -3.41578 | -50.44649 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d12ffb3-b2a6-3264-8fab-9b4cac98dbcc | -1.79657 | -52.74604 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e15f0d2e-36ae-3312-828a-361bad6df35f | -2.89221 | -48.27382 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aaa63254-b35b-3ca0-b1f6-ee896bddbd9e | -3.96409 | -48.08847 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d0a6234-f1f6-3bc5-ae78-5b9580801bd7 | -3.75499 | -51.59576 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49013740-f544-30b3-a353-b08e7f130f77 | -4.17606 | -48.4529 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75d323ea-836b-3997-b610-51b21719dc45 | -3.39365 | -50.30321 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af980203-7de2-3c74-a72d-e1520e971ac3 | -4.94562 | -45.87892 | 2024-11-27 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 228681c5-639a-3e3f-937b-d6f7c6e554dd | -1.88052 | -48.5442 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7db5b9f-56ee-3bb3-ba08-c3bc7330d0a1 | -3.11219 | -51.25498 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94a9e9ab-6855-3ec4-b052-134dffc45570 | -3.9569 | -45.55399 | 2024-11-27 04:18:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e32aa070-ad7e-3dce-bb88-4ddb29a3799c | -3.89146 | -46.0947 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 598f67e1-ef1f-3a84-98d2-0e14306a2645 | -3.60826 | -45.11074 | 2024-11-27 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7661eef-6ac5-3123-9486-9831e353aebd | -2.82885 | -54.1167 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README38.md)
