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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be6869b9-3360-3de6-a1f7-a1b71afc5c59 | -3.58424 | -50.53851 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccab170-1b57-30d2-add6-a050ed721c29 | -3.79959 | -50.98013 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0e82cd6-40e0-39b9-80ac-5f026d87be95 | -2.65088 | -46.11876 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63dcc516-62be-3ac5-be16-241866f622df | -4.07917 | -46.68996 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f1d88f7-8d93-35a2-b25a-b91fba59ad95 | -5.20218 | -46.16758 | 2024-12-04 04:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b6aebc6-f458-3ea8-bd62-07381408a3c0 | -2.23256 | -53.6992 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 437026cd-3ab1-3465-89f1-3408e27349dc | -3.28529 | -53.71808 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c3fc1f4-7758-34af-8046-4223ee19d267 | -3.02415 | -51.53952 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5091d465-457f-393a-9ab0-5741614fa034 | -3.82091 | -52.12053 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5156dbf-19d4-3064-8ff2-63bbf1abf353 | -3.72917 | -51.08563 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21c69462-e433-39f3-afd3-7226178610e7 | -3.9204 | -52.40162 | 2024-12-04 04:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f44803b6-f662-37f7-bd8c-058f9e4f19ec | -4.07879 | -46.68246 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a593003-3941-33aa-8acc-58bbf032e5cb | -2.00337 | -54.11795 | 2024-12-04 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c363ad0-5941-37e3-8b30-a802949735fa | -3.20597 | -50.64661 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1c33cb23-22cb-337c-b6d8-60feaf879872 | -3.30113 | -53.66217 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c384b18-e9e3-3dd2-8204-d882e0aaf98e | -2.91878 | -52.21258 | 2024-12-04 04:10:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55779fb6-d94a-3f9e-bd0b-ab112a6597b1 | -5.623 | -44.83865 | 2024-12-04 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 87682722-181f-3813-93e4-bcd7af28ab62 | -4.0537 | -46.60394 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a83f102-de09-33f8-a450-1dac76d544e4 | -1.64618 | -52.0522 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 253d7b2f-d2d9-3c16-bd38-eae55d6a77d8 | -3.7728 | -52.20841 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac0db8c-b633-330c-ade8-bcf0e8bd5143 | -2.31497 | -45.42035 | 2024-12-04 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2e3a1d1-c23f-3078-9f47-5a2dbe483306 | -4.71237 | -47.20296 | 2024-12-04 04:10:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0d1cfa1-26dc-3559-8cd1-cde4eee67e8d | -3.78519 | -50.97147 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 631f68ce-9750-39fc-bec5-2a8f7767792f | -2.73368 | -46.25327 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439e9887-bb87-3d59-9033-f2ba4667017c | -3.6813 | -50.25964 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f15de1da-4250-3386-b2a8-250cd617f90f | -3.13531 | -39.9053 | 2024-12-04 04:10:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e09e3a95-c360-33bf-8ae6-5cfabb9428f7 | -3.54694 | -44.95135 | 2024-12-04 04:10:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9362abd3-fbb1-32b8-8d48-031df5fab4c9 | -5.57299 | -45.14954 | 2024-12-04 04:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a682b0d9-5637-3edc-8ead-25d53236a5ee | -3.55521 | -50.40136 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23a626bc-5dbe-34d6-b9c4-258da8bc097f | -2.73395 | -46.25528 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4fb1867-24dc-3359-bf6c-2fd17a73cea1 | -3.11456 | -54.68068 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14fae3af-0999-3309-bca1-188aa29d04fc | -2.81757 | -53.04741 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 343592fe-b33a-3f21-b55b-f5617a8dc1c4 | -1.75249 | -52.64193 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e8d5b9f-53a5-3e4e-b544-6eb2c89f44d3 | -2.63033 | -45.74187 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a41fb5b-60e3-3dd7-a2b3-0ebc56d5b330 | -4.07842 | -46.69472 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8e4215-1054-31e8-b858-72967b2648f5 | -3.08356 | -53.38194 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55e321d7-5387-303c-b89c-b7e6f1b965e8 | -3.09184 | -53.25622 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bec05db9-de64-30f5-8cc3-674a25fb857e | -3.3372 | -51.20617 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc8b02e9-5c7e-31d6-a138-4f646fcfbfbf | -4.07182 | -46.70078 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9dadcc1-7eca-3ef5-a7e0-099b1cfaaee0 | -4.05562 | -46.81359 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a643d89-93c2-309e-be09-d40ed4814d1b | -3.08699 | -53.25892 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a73d6c-e87b-3036-88e9-b46d36ffb870 | -3.57212 | -50.30917 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3e126f61-9c36-380f-8580-8a398a70036b | -2.68861 | -46.12488 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629075ca-115e-3886-afe7-9a1944b66269 | -1.66628 | -52.75679 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c2d0ef5-3eab-3f89-9172-c5abc94694bf | -3.24413 | -50.42162 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef2ec2d0-2af2-308c-b505-bf22b3723f50 | -3.25667 | -53.66709 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7a0be1f-24ae-34af-aff7-75c5601aab6e | -3.21537 | -53.72438 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e147f2e2-195d-3e0b-98e8-287a452a9ed4 | -2.84878 | -54.82819 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d1274c8-8967-35ca-a2ce-7bc302b53aa2 | -3.83525 | -46.61275 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b15002c1-c476-3ccf-9d9e-cead3a52c09a | -3.25904 | -53.6527 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67b84fca-61f6-3132-908c-acddeacb80af | -1.66259 | -52.76144 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a62fcc8d-22e2-3be2-b333-e14e721c4e60 | -3.49414 | -49.93343 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8a3ce11-81dc-3ddb-9dfa-0159568b2850 | -3.3376 | -51.20594 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ab4f85e-4776-396d-b027-9c49f4983d8e | -2.84967 | -46.79652 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6e18a23-9fbc-396c-a6bc-3080a3fbcae3 | -3.51931 | -51.31171 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f39d0fab-e9b4-374c-8836-b60e35413e57 | -3.53225 | -50.38631 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0089dc37-4e1f-32ca-9671-8dba71d137f6 | -3.04086 | -51.27302 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbc15562-4e07-3a02-a133-5cb2ae008829 | -3.1994 | -50.65464 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15441476-d1a9-3e6b-a4d1-b7bf8ec68e21 | -3.49184 | -51.56283 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 095cdd61-4463-3d1c-ab60-d17d03cf2933 | -0.90157 | -47.31633 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbd2f311-9772-3b59-b56d-338c72d86844 | -3.07861 | -53.37967 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d8e6bd7-739f-3441-94ea-8bc022149550 | -3.09111 | -53.26067 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6f3c2e4-bac5-34de-87ad-6ff9b3fb1512 | -2.67661 | -46.62558 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5448d167-423f-3621-a9bd-3589d5a99ded | -3.81287 | -46.95167 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d70224d-1e4c-34b8-aabc-049e42ba6fff | -3.12012 | -54.68777 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 284b5004-1dcc-3bca-931b-7e2d0f6bc680 | -2.62764 | -48.06 | 2024-12-04 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a85d4d-7b7f-3f51-a739-e9087adc0cdc | -3.24833 | -50.61116 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1302367a-64ea-302a-9db2-65ed881c0188 | -1.68956 | -52.33449 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b59bd73-b6b7-34ab-aff5-3b9e6008cf16 | -3.27318 | -50.55519 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e897297-6b43-3315-9934-37ecd852e59d | -3.26204 | -46.27193 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 383d4254-b0ef-3806-b1d7-6a8ccc0bb634 | -3.25757 | -53.62326 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38b17e73-1806-3e45-b01f-54fb0a767a38 | -3.90476 | -46.6591 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 599cc320-7f56-328a-926b-8255637b4ae9 | -3.66057 | -47.12527 | 2024-12-04 04:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 111db112-07bd-32a1-ad23-474b2e309e7f | -2.81995 | -53.07053 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9e3d028-23ec-3320-95b9-52a8de88da3f | -3.52533 | -50.85806 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66d8fd01-90e2-39bb-b631-c1c10977ff40 | -2.67352 | -46.62006 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f3189ca-5ac4-3d04-ad24-28875e645fc2 | -3.55924 | -51.52234 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfb57e12-b016-3531-95b5-7df0950682ea | -1.65958 | -52.76017 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| daf6acfd-7be2-3d3d-b59b-f198f624f43e | -2.94359 | -51.01659 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cfb0b52-556b-34a7-bcec-5e155c1897d3 | -2.96989 | -44.98191 | 2024-12-04 04:10:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f28a7db6-7d07-354b-94b3-1f4b5a7d2cd7 | -1.74939 | -52.62379 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d94bce5-f893-314f-96be-232fd2d70a39 | -3.07752 | -53.38071 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b2039a-8e2e-326e-8d35-c8eba39f46be | -3.20647 | -50.65341 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70c51b6b-2f7d-331f-a8fd-6813f8e69fe7 | -3.7278 | -50.05934 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61eb0ecc-4a75-33e3-a7ef-bc8d3d108fe7 | -2.56919 | -46.1931 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04ac214f-29f3-3b01-b343-14bb33ee1d23 | -3.10335 | -54.66713 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b220572-dc01-386d-b3a4-79e370c57e58 | -3.30035 | -53.66674 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec9ef306-3853-3e5a-a046-1d94926d9e54 | -4.07181 | -48.33993 | 2024-12-04 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad2ccfc3-437b-33e3-b76b-93bed05d7775 | -3.18956 | -54.5162 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 695b8f94-6002-342e-ba44-4d11392f10f1 | -2.9204 | -48.01532 | 2024-12-04 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32cabb81-3e61-33b2-bc5a-24b4e2747e2a | -1.64585 | -52.38213 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73dc32c8-f7c6-3155-be42-921182281d1b | -3.06755 | -54.06273 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 079afeca-4be4-3d6a-9b4f-5d66e0daff15 | -2.10103 | -46.13777 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b066951-73da-3b29-b9e4-a122b0cfe3ce | -4.07992 | -46.68525 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7ed8816-a38d-32fe-9c7c-49fe34650462 | -4.11706 | -43.92748 | 2024-12-04 04:10:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a741fda-8c04-381a-bbad-feb976ee63fe | -2.85055 | -46.68993 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16497ff5-2c43-3df8-9ac1-979b2ea68e8a | -4.05569 | -46.99112 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a0eb59-bcf4-3600-922a-c7c60c64d41e | -2.69719 | -45.65453 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 142d1683-7c9b-3616-bb23-7c31c54db908 | -3.24387 | -50.42198 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c00dedbb-e98a-395c-a5c4-24ea7d369696 | -6.03257 | -39.42603 | 2024-12-04 04:10:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README26.md)
