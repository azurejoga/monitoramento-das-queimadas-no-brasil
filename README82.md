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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0601d597-e839-36eb-bb0d-8cd35ca1d45b | -0.88017 | -53.68301 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5b3041b-c6a0-36c6-8168-ad72cee4193c | -2.45023 | -54.00422 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30be65c1-90ee-3385-9ba2-913fc15a27b7 | -3.28524 | -53.27008 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e4df2bd-3a8c-3334-9b89-4d425f8d81b5 | -1.0846 | -53.3906 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c488ae0-2233-3ffb-92dc-0a5bc749f51f | -2.75191 | -51.66343 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a135a598-0a10-380f-a9b8-04a9581314fe | -2.53452 | -54.07088 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 811f2c95-6896-3cfd-a013-ed786a9a16e9 | -1.2864 | -52.10103 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 269fc48a-469c-3366-a5a6-402430c7e7ce | -3.24717 | -51.34875 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4649b518-25bf-3aab-8004-f4202318ee43 | -1.26439 | -54.54987 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf078cea-080d-316e-a471-f66ac32da94c | -0.0551 | -51.60398 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ff6545-c74a-39c3-9ad3-d1addbea2360 | -1.63537 | -53.86734 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 30ad4176-d9b0-37eb-938e-ef517ff7313b | -3.22988 | -50.31742 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63bd7dca-f227-3094-89ed-27adc439488c | -1.26385 | -54.55331 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 36e2be61-5d09-3f96-9f10-e88c33430f74 | -1.26408 | -51.75945 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7616ccae-61df-3bc0-be45-3755698e47a9 | -2.59585 | -54.21589 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 071848ea-c6a9-31d1-9925-8b7796865cc8 | -1.09715 | -53.61606 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdaf3c91-7750-377d-9dc9-36a1b6e53aae | -3.15355 | -50.6297 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb051c34-246d-3f69-aeec-0d57ef4771ce | -1.46222 | -54.49603 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a2b0c17-9da1-3b68-b83e-43f340c42817 | -3.26808 | -50.203 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5133a03b-bd28-35ba-9e12-cf3e53749ecb | -3.08873 | -51.40766 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| efa6bbe6-e2da-3791-90e8-dcc56bd85921 | -2.61418 | -53.99011 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 010d82f2-7979-3f8b-aee9-471da76418a1 | -1.70493 | -52.46514 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f804f70-3912-311f-914b-3d1885405d73 | -0.95933 | -53.20464 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0d15ba3-cac4-3635-9202-756813c06820 | -4.14045 | -50.65742 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d28096bb-f013-369d-935c-e655ab480cbd | -1.14411 | -53.61243 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bef3bb9-3551-3e1e-a4c6-1eddab51cbb9 | -3.0532 | -52.76598 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb26ea1-f003-31a5-9e2c-a64a57d2341c | -0.20518 | -51.40485 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 539cb3f2-d054-3148-a85b-40fffdde1f0b | -1.75689 | -53.64953 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23aa4aa2-a44a-3f50-9082-cfc1a7fd8352 | -2.58799 | -53.98247 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3945e8bf-d168-3828-a610-e8ded4da619a | -1.21322 | -54.18867 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c570cd76-10de-3c60-be01-192cdf46003a | -2.43332 | -53.89406 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ee0ac64-cdc1-3272-b62c-5b39f03e0156 | -1.56878 | -52.00233 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09cce17b-edd8-3ee5-8f9c-3cdb5fe22a20 | -2.95779 | -53.89234 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d942a8b-a4b9-3f48-a814-0e040e1e3b02 | -1.66619 | -52.79989 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baaf42a1-e565-30cb-8031-d1f0eb4f9ee3 | -3.83033 | -46.55008 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7859e59a-04be-35c0-845e-3befc0ba204c | -2.70674 | -46.12563 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3feb7ce-b8dd-3da6-b5f4-0d12bb8ff66c | -1.00268 | -53.69472 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 823097cd-cf39-3c86-8f24-6b925215c832 | -2.42711 | -48.5494 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b26236e7-c628-358c-b1d0-f9c5dca58ead | -2.82054 | -54.48565 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867d0a21-8df1-3999-80cb-21023f2ea9c8 | -3.25738 | -53.64784 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f48923e0-3a37-36ee-8be3-597fdb5c0a79 | -2.92078 | -54.25953 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 503c3a94-1d5e-3869-8e49-df6cfff852c2 | -2.58881 | -48.20328 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3457d3-7596-3c0c-aa1a-3c16a41fc022 | -1.58351 | -52.27515 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e2f089a-d382-31da-b333-ef47793efdcc | -1.48265 | -52.67342 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6e64f2-ffab-3b9f-bf3f-3ea7452201c2 | -3.27718 | -53.81478 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40465938-78dc-38c5-9748-bd5b58099a3e | -1.39465 | -55.01139 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4006f1f9-ea12-3477-bd94-a416b8b0b6fd | -3.05727 | -52.76271 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c431247-085a-34b6-9471-24dbd77c363b | -2.77122 | -54.02933 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecd31c60-56f9-3705-bca0-dbbef46c3a2a | -3.2654 | -50.20512 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50aa63af-fb29-3f6a-9953-c82da17a66a8 | -2.83783 | -54.11829 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b3df047-af10-3a70-a036-ebeb201c951f | -2.24137 | -53.78134 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1400bd1-2c7d-3f40-99bb-82ced947f0df | -3.61486 | -50.19129 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42e684ff-5002-3b9a-b2e0-ef3ebc72d033 | 1.67724 | -50.66657 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea386f3c-0b95-3248-afee-7516812bd0ae | -2.6036 | -53.99206 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cfd7a79-a0f2-30b7-baf9-2a7c0bc5dfca | -2.92539 | -52.6885 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e6e5ee98-2548-3398-a6ca-07eee1d31354 | -1.11328 | -53.60067 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82c34a16-bf10-313f-937f-840fb15ef1f3 | -3.44142 | -50.022 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 898e1c2d-a952-3983-8968-780b131a471f | -2.58853 | -53.97897 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00237225-c210-3209-9dfe-8730360d58c0 | -3.49361 | -53.81495 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c2769f2-2d73-337f-bdd8-6e808b156072 | -2.88154 | -52.68587 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99e5be1d-e995-39c7-8ced-9ffc47abf991 | -2.86883 | -54.02995 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 989df78a-c116-3934-b8de-c66b03feb0f4 | -3.07317 | -49.10287 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 983c3e0c-9083-3669-881b-bf28a6e8ac3a | -2.79984 | -54.05512 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8db238c3-6144-33af-9e88-c8d6212da471 | -1.43561 | -55.24487 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9d5ed75-20a5-3839-a020-de3a5cc77acd | -2.86773 | -54.03696 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20b2f91b-9c2c-3901-9c68-4b91aadd42fc | -3.05129 | -50.27803 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13e6fb62-3c79-3900-b649-b3909e7d05de | -3.22342 | -53.42088 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57c401c2-44d3-3795-bab7-dc06cb67a729 | -2.25111 | -46.45092 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2727a017-f015-3719-b02c-d81831cc1f13 | -3.49575 | -50.45689 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 006349f5-cfda-31ca-836a-463943eb25a4 | -1.0977 | -53.61255 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 285b066a-dfd4-3e2b-8a60-c55edb06e0ed | -3.28602 | -48.7642 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8b9f96-f338-3e06-9285-3597aa4c285e | -2.71995 | -47.54683 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 007e89e9-ba43-3af5-88fd-f4b28d45ee6d | -1.28341 | -51.72953 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2b762fa-77e9-3fed-a00c-97c0aba37110 | -2.96898 | -48.03823 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b98c458-20cc-321c-9f59-1ebc22fb4b07 | -3.60106 | -49.98381 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ff0b7259-3c46-3765-8ef2-1979fac5c9f2 | -0.13955 | -54.59928 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2fdfcde-2bec-3a8e-ad14-3f4617d4c253 | -1.00562 | -51.72549 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e337e7c6-7fd9-31a7-8cd0-195f722d573b | -1.15346 | -51.70675 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be6f44c0-108b-3627-8066-e32c01e44eb1 | -2.73336 | -54.03061 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1cba7a6-c601-34dd-8823-f3b8a986bb21 | -4.00925 | -53.43828 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 037cba1f-8e31-3070-bd6d-25db7bb4643f | -3.09079 | -54.01725 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99daf857-8017-37f7-bb5d-401a51d320c1 | -1.4861 | -52.41286 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 626526f8-4bc2-38fb-a57a-cc6be07a0933 | -3.29513 | -53.8322 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ac8f6ea-17e1-3751-b860-e34c8ab33cab | -2.6294 | -54.06762 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c40d3f31-dcec-3810-a5e5-bd60714b1b3a | -2.52999 | -54.03445 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f1bbe8c-2cfe-3e52-ba51-1f9280079ad5 | -1.68065 | -46.78362 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 96b6eac5-2670-31c5-a57e-1e7af0985261 | -3.70279 | -45.6827 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74bd17f0-f07e-3895-b61d-2a8a36cc3d73 | -3.22493 | -53.83243 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252e1c29-4896-397b-8d7b-9f9d94d7c946 | -4.04911 | -48.33918 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01be6e52-3d6c-3fc8-8947-3cc3cf883c91 | -3.96918 | -48.09085 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62cc37cd-9ce3-3b83-8fcd-8a1fa2d3aba2 | -0.54353 | -51.41156 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e223a3b-be4d-30fb-83db-2d3fce3e6bce | -3.15718 | -53.23875 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b464a43-a98d-37ac-9da0-28945a14eb78 | -3.12763 | -51.12358 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d00dfae-027f-386d-8bcb-8e48dbdf707a | -1.08154 | -52.43462 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd26e62b-f882-37b4-9ad8-1cab84cfa8db | -3.07785 | -53.27956 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fc1168e-ddbe-3ea6-941c-0ea21426e616 | -2.84035 | -52.53829 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b10afd0-379e-3f92-9f3e-e148ed781f57 | -3.28152 | -50.55231 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b63babff-4d67-32c3-919d-12919fcb0dd5 | -3.25263 | -53.86192 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16bec27b-b3b9-3e9d-85f7-a3567085f6f0 | -3.78766 | -52.4041 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d65f78f-4f39-3399-a3c0-22e46f76a8a5 | -2.90611 | -54.17884 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README83.md)
