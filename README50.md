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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 819d1e45-b2ff-31f1-a2f6-75b9799e94c0 | -2.18382 | -51.74093 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdc4ecfc-1b74-3274-a16d-7668aeda9664 | -2.71999 | -54.15068 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b627663-e83c-34a9-8df3-148f28e257b6 | -3.0306 | -53.27365 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c06c40c7-73ea-3c63-826a-38dd3aa60176 | -2.94683 | -54.1364 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0808df9b-61aa-35ea-9a0f-669d3cad2b67 | -3.15702 | -50.20325 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc49d53c-abed-3a97-9188-2efc0f8acb7f | -0.35755 | -51.41684 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7d6983d-7632-3d83-abad-1cfbf35922e8 | -2.84025 | -52.9063 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32b9dd9e-9a0a-3d78-8551-c8138a69b6aa | -2.85375 | -51.77238 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b25b5f36-04d2-3a21-9c02-5bd18b1e3ccb | -3.32149 | -51.57107 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11f96cf-0764-32c8-8125-482031cab3f8 | -0.04238 | -50.79808 | 2024-11-07 05:10:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6285a451-3ad1-3398-8961-880243cb3df7 | -4.25856 | -50.69286 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0e233c6-dcf6-3efc-af17-114cbdbc9173 | -3.48501 | -50.38337 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79713301-86b9-33f8-9fcd-af78bc8f02d7 | -1.13784 | -53.71842 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 010181fc-e84f-3f77-bd60-c7a43ce83533 | -4.39259 | -49.76727 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 809dca9c-da4e-3132-bf84-e58786053d56 | -2.27401 | -53.72918 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16adf6bf-e237-3642-a951-b44474754720 | -1.32592 | -52.24075 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 071c9b3c-44be-362c-bfd8-55fbcba51707 | -1.66188 | -54.97443 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e970a6e4-7e43-351e-905a-0ef984d2e6e9 | -4.25418 | -50.69218 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4972a569-9b77-3f73-a852-a53befb8a36c | -1.35005 | -51.41126 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ec50699-d874-343d-9e1c-1251f6ec1199 | -3.32784 | -50.07758 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e386e12-efb2-38eb-b854-825911011855 | -1.84082 | -52.34799 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1de4738f-eb45-3131-9a26-151ae0199f58 | -1.33752 | -54.6054 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddf2ee60-4549-362b-a3f3-f1e35acce95b | -2.04327 | -53.58027 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3699bf2-6428-310b-8574-a73820a475d8 | -2.84661 | -48.67619 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ba3a8315-de30-3a9a-8800-50b5586d6d3f | -3.02306 | -54.09093 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f57ca59-d0ec-3199-973f-85147d12d48b | -2.2809 | -53.80232 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 401d3975-9c0b-38ea-8ea4-b7368d627f17 | -1.92636 | -46.48041 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18d23ba4-c24e-349c-89df-44d1b4398991 | -2.9323 | -54.11427 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b22b62dd-da46-30ee-ab10-bf33e268eab6 | -1.3807 | -52.26353 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7182d62-aa6a-3e89-ba1d-78aaf8fbe272 | -2.91497 | -51.04437 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdd58014-0545-387b-af35-679cbd261af1 | -2.27046 | -53.72864 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3f6961-b5fe-3972-822c-f413b42a1c10 | -3.05041 | -51.07029 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba398191-49ac-3a1b-8635-7f22775a552f | -3.66306 | -50.25008 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c9e93981-f7f1-3ef5-995f-e8def5e9ae76 | -1.44406 | -52.8246 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20c58085-4228-3778-b9db-7f483912f5f3 | -1.15526 | -53.74478 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7be341a0-7dc7-3bfe-90c5-c4ffeb78c675 | -1.72575 | -53.28481 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57bbf309-ba1c-3504-88a3-150b3758f103 | -2.43571 | -53.66582 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2683390-0cca-3cc8-8a03-32154489971d | -2.84871 | -51.77874 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a386f690-d276-30d4-8fa8-f30832f5a614 | -2.81852 | -52.94843 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 80e84fc5-1bc2-3441-8c22-eaca80918264 | -3.21946 | -50.38431 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1e4c6faa-a117-3902-87ec-e5f41e66e445 | -3.64236 | -50.17344 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b78bf8-95c8-31c2-8c7b-a3582d081c3f | -3.15998 | -50.20534 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4868257-3408-3e5e-a584-b0e732fb2592 | -1.11252 | -53.60224 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f91e650-474b-3133-8d84-974e019caf09 | -2.72992 | -51.73962 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7d56fd7-2d36-38b0-84ba-37560241e570 | -2.73044 | -51.73616 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 216e107c-b0fa-3191-85de-9a2e772198c9 | -3.07152 | -50.98614 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9ba8fcb-a5c5-3430-8fb7-b8bff7476774 | -3.58443 | -50.2366 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2f36272-31e9-3770-9592-50c8f545d3d6 | -3.00751 | -51.44324 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 582190ae-fd28-3a8f-b9ec-ffde7ac3e201 | -1.28054 | -54.13467 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a87776d2-4544-3e59-a0b0-f55256efcbce | -3.11331 | -54.16439 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fce055f7-496b-3523-868f-49dbf0a7dfae | -1.44339 | -52.82893 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 729828bf-45f5-32c1-adbc-f69688c635db | -2.74956 | -54.05178 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f83c76f-63b3-3daa-8b75-1843f7ab6069 | -1.3347 | -54.60124 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30e4535f-aa3a-36b8-83d9-971578d9cd41 | -2.84524 | -51.77465 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39508e21-b432-333b-bc29-8ee0547760ef | -2.84226 | -51.35228 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46b337e1-39ed-3e79-9418-812fd2dd66e2 | -3.74363 | -50.06097 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76c03879-bf30-3bd2-be00-0347e4491607 | -2.74265 | -51.89788 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6e438f2-c188-35b1-84a0-325ef8c1ab1e | -2.7568 | -53.22758 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51f28ac8-ef9f-3ca0-ae83-2f9a8ef27f12 | -2.10075 | -46.47625 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16ee05bf-8ea8-3040-b6be-2e4f98d040e5 | -1.33413 | -54.60488 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 027a1775-8ce8-3264-b347-e44b75f35f72 | -2.72208 | -51.70992 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870d87cc-e908-3eb1-bd50-0fa901d71bc2 | -1.1589 | -53.72134 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37f45e70-1fc5-32eb-a10d-afa4279a65b1 | -3.13918 | -51.20008 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44e9feb4-752b-322b-9fca-6352720fb2ed | -3.27373 | -50.35054 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e2801769-ab54-321b-986b-f740db1ebc50 | -1.67711 | -53.81589 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 779b0f88-ebd0-395a-8d6c-5fe481315919 | -3.30949 | -50.13935 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f111e223-046e-3f36-82ee-792ade8c338d | -5.02392 | -46.84472 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b5a0fad-25a6-3e3e-8b79-987aab8464dd | -1.13493 | -53.71405 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee2fc6b7-6f01-300d-a03c-55b256a91c58 | -1.38837 | -52.18846 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a884d12-a4d8-3d7b-a07f-ccdc30b8c123 | -2.97391 | -53.86589 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba64b7e-e04b-357f-a385-8527e6365d3d | -1.45075 | -54.44178 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c37607a4-ce18-3031-9411-afab950e6fc5 | -5.03139 | -46.83893 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2efd689-ab1e-3027-ba41-42f2c23de6e5 | -3.22451 | -50.37832 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18a1fca5-70cb-3790-aebc-b6d6f8d6b8f5 | -3.61513 | -51.33958 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fb6e2b5-c604-3b6d-b479-4576efe0939d | -2.28677 | -53.81132 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 8ffa2f72-68c7-39e7-8055-56f90da06bf6 | -3.66172 | -50.25902 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31fac93b-1b2f-387e-8338-5438da7612e7 | -1.33018 | -54.60798 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74109bf3-d50a-3af4-a518-ad64207ca233 | -3.02967 | -51.09457 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd5c9e36-05a3-3523-8961-07f29b286cad | -2.15265 | -53.64612 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 828c1eb5-45bb-34d2-bb11-69ae810cf57e | -1.60013 | -53.39713 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d776556c-00e8-3449-a228-0306180aa85c | -3.04092 | -53.27966 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38a40a77-7bc2-3980-b00d-df02563c9260 | -2.8192 | -52.944 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 51b9178b-e954-3074-8f80-f2380d3e0137 | -2.96976 | -53.86935 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b8de1a-189e-3222-84dc-849aac873914 | -3.17794 | -50.59858 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49078e18-8976-38f7-b74f-a2a0b24047e1 | -2.84162 | -51.79879 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 316eb8d2-dcf3-3844-a81e-df3cd5f11e11 | -2.65847 | -49.8795 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5dfecad-c8e0-3592-9c0a-e258e00d41e9 | -2.62036 | -51.30419 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7cda8b78-7a8b-33ff-aa08-09c8cc33d7b6 | -3.14336 | -51.20062 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb16ebd-f5ba-348b-a4c5-afeae02c347d | -2.87673 | -51.31145 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d9100eb-12cf-39e5-bf9b-d0761dc4d750 | -2.96622 | -53.86879 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e63e9209-26ef-3c90-b5f7-e3184614cc8b | -3.6204 | -50.19757 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b22fd6eb-4df0-32a3-a4f3-b0033ced5a2f | -3.21803 | -50.30434 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a9c92d1-95c7-3405-97ae-5b3eb482f7a4 | -1.29025 | -54.56735 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3def1eb4-c5c4-3e9a-a24b-04984ad48dd8 | -3.45971 | -50.37065 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4f04cb2-220d-3d0d-b6fc-911b5104dbfd | -2.87728 | -51.30776 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba6abfd5-4d3f-34f4-bbf1-0aa6828f549c | -1.14195 | -53.71503 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 84a8b675-042d-30cd-bfcc-2feca6de6f0a | -3.62557 | -50.19369 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f927b2c-433d-3ae8-a47c-4d2a2c37caa5 | -3.15634 | -50.2077 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 402936de-7bf4-3c4f-9895-e95c8a54fdbb | -3.33168 | -50.08278 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 286cf454-898a-305c-a4c3-1b2de70ed3cc | -2.84746 | -48.6706 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README51.md)
