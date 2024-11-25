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
| df9f47e6-bd51-32c4-8f44-b86d183c0b9a | -2.67113 | -46.60665 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18950d2c-1500-38a3-93e0-3a74f10fa15f | -3.68263 | -45.89122 | 2024-11-25 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea703587-a636-3fb3-a6e6-2857d8bb7363 | -3.94548 | -46.89726 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b10c50e-0139-37df-933e-cecf5bb7fd7f | -4.29922 | -48.18415 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd63a31f-5677-34fc-a940-7eab7ba4e66a | -3.74349 | -51.83673 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b332a96-3f69-32f6-858a-fe0a2ce710eb | -3.8504 | -52.14756 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd5fb7ff-1ca9-37ab-a800-e1047bc2fdd0 | -1.44944 | -52.44978 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4c8e123-fa8f-363f-9ae5-6bb5a313b157 | -2.82269 | -54.09986 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cca487a7-86eb-3cc2-b7c5-41c88052b7e6 | -2.82879 | -54.11979 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe376d95-0c4e-3090-aef8-5d84ddbe48d0 | -3.42523 | -54.59223 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcb2e3ce-6e0c-360e-a510-d56c8070ab85 | -2.77573 | -52.89152 | 2024-11-25 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fbf5511-e1c4-3ab5-804a-54088027053a | -1.6233 | -52.43819 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43b32077-ea5a-30fd-8e08-3b2b78456526 | -3.25399 | -46.42221 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff65e6ac-8fde-3ced-8611-76ed41230d49 | -1.97049 | -51.9827 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb892e3b-e554-36c1-a58f-b241795431c0 | -3.27407 | -48.75615 | 2024-11-25 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec14c1a3-0c27-3e81-94f0-46b34d2b7e92 | -3.89543 | -46.67186 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c34bb49c-8b32-3f97-b716-00295c15cae8 | -3.82369 | -51.21707 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ffc5a64-3015-3d90-a9ee-bcae02aabef2 | -2.92539 | -51.76704 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fb5c670-c463-3838-b6bb-b3220e90d056 | -2.81124 | -54.02765 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 918cd207-5ba1-3c08-a549-bffe3e92062e | -3.34356 | -51.21235 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e9fcb09-ca38-3e56-9817-c49ac7ac3abc | -4.26693 | -48.69362 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93d77788-f839-386f-8367-f978f2024bf5 | -3.89373 | -46.66087 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0dda5b7-3d08-3a5e-8229-97c1187c8c0c | -3.80462 | -51.26436 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c1d9655-b9f2-3bc2-a120-ddd9caa0f1c5 | -3.64829 | -51.38632 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1eaaff6b-1705-32fa-be81-89e4951e6c14 | -4.70809 | -45.72303 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96bb35ee-f47d-32fc-aca4-61443c665dd3 | -2.73245 | -46.10435 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5c61841-2b6c-3004-bf28-83f84d7d2fcc | -2.71055 | -46.26341 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 529b5d6d-5758-3644-90f3-8ec4380aa761 | -10.11398 | -49.06293 | 2024-11-25 04:36:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8791d9e-335e-38a7-8808-7ee747886465 | -15.53531 | -51.02633 | 2024-11-25 04:36:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ecdb3cd-5f09-3f8a-98dd-358ae5d4f1bb | -9.81697 | -48.17106 | 2024-11-25 04:36:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92946555-b694-3f24-a039-c4a91d8d5c1c | -9.81751 | -48.16754 | 2024-11-25 04:36:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7d9bfa3-d996-3044-8960-13b887693c71 | -10.11453 | -49.05944 | 2024-11-25 04:36:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 288852a4-709f-3ab6-b8d0-8f1e7777680c | -15.08022 | -48.94448 | 2024-11-25 04:36:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41d5d801-1273-3a05-b3a2-782009f0220b | -9.96156 | -48.07065 | 2024-11-25 04:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e99d844-8006-3f7d-851c-06d900d2f5ce | -9.82362 | -48.17211 | 2024-11-25 04:36:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44081c0b-3d07-3bc6-9162-f5e6ae3b622f | -19.02176 | -57.62141 | 2024-11-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a6f0b88d-7434-37dc-8118-637b736eabe0 | -20.25366 | -49.67632 | 2024-11-25 04:38:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efab49b6-5b32-3dc3-a0d2-9b8968941456 | -17.7563 | -52.43807 | 2024-11-25 04:38:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21376268-1677-371b-b60f-b394ebc3ee18 | -23.29918 | -46.78255 | 2024-11-25 04:38:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a137f3ac-a194-3901-962b-dcd522806d67 | -21.55307 | -45.83513 | 2024-11-25 04:38:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84734335-eb0c-3110-add7-200ffbbb0fbc | -19.54837 | -56.71681 | 2024-11-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b2798fbc-4852-3b3a-9a3c-3ae40548f6f8 | -22.67884 | -42.85338 | 2024-11-25 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c726b647-3807-3087-b6f8-845f6cff7d6d | -21.93917 | -46.23325 | 2024-11-25 04:38:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| df7da753-1be4-388b-8d2f-f03110c1e816 | -21.31765 | -55.94678 | 2024-11-25 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 869fa6d8-dc99-3e76-bb9d-5deed6eac389 | -17.35231 | -50.52444 | 2024-11-25 04:38:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4a1661f-4146-3ec1-b5f3-79ffa25cd2b8 | -21.94324 | -46.23385 | 2024-11-25 04:38:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 221f04f0-9857-387b-a45c-f5729434fe90 | -22.70309 | -48.26709 | 2024-11-25 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a389b92d-5272-378b-9f9a-1b2cc50d9893 | -22.70247 | -48.2717 | 2024-11-25 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76a12225-a5b9-3b68-814c-a92e0a43a14c | -21.32053 | -55.95245 | 2024-11-25 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09c5d84a-4140-3db0-b1e8-8b5f745640bd | -20.99601 | -51.7925 | 2024-11-25 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 85232466-715a-395d-a991-2872139c5739 | -17.09509 | -43.80332 | 2024-11-25 04:38:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55989f6c-934b-3fa9-90ee-fefa8c18bdb7 | -23.66155 | -47.65939 | 2024-11-25 04:38:00 | NOAA-21 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5de611f3-7243-3ff0-b4cb-dd9febc5e479 | -20.77134 | -47.16547 | 2024-11-25 04:38:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57769251-b6c6-3c38-a4f5-b70e452094dd | -22.32346 | -48.2632 | 2024-11-25 04:38:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea63d603-5241-3048-b255-9344494128c6 | -22.67675 | -42.85206 | 2024-11-25 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 04c6be11-c388-36e3-a4a4-cb74e57bdd17 | -19.56833 | -55.04483 | 2024-11-25 04:38:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eb744e5-fa86-3c33-bdf7-537782ea4912 | -22.70245 | -48.26883 | 2024-11-25 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da453385-e2fa-3661-829a-abc4e6c65bb7 | -22.67645 | -42.85529 | 2024-11-25 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63cd6830-ef14-3672-9baf-af79d9f001fd | -23.59249 | -47.44127 | 2024-11-25 04:38:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3d54474f-25bc-3158-87fc-ac88c99452e7 | -20.25027 | -49.67574 | 2024-11-25 04:38:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73bb635b-daf9-3ba6-9e59-2304440861ed | -20.76404 | -46.76705 | 2024-11-25 04:38:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 90488253-4844-3c24-b41d-b30c97b4b2e3 | -22.43884 | -47.67684 | 2024-11-25 04:38:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51c83555-1d3c-3d4c-af73-2d9604a04a19 | -22.30793 | -49.76638 | 2024-11-25 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa826023-c61e-3da3-8f94-ca5e73a8fc6e | -3.9494 | -47.9776 | 2024-11-25 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 422ede0f-013c-35db-84b9-51a0f5c689a4 | -24.92007 | -48.93692 | 2024-11-25 04:40:00 | NOAA-21 | TUNAS DO PARANÁ | PARANÁ | Brasil | 4127882 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f0edeaf9-90eb-3956-bc86-70ff7bb5b126 | -23.11477 | -55.06544 | 2024-11-25 04:40:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6be9292c-7bdc-3675-9681-1f89c850cd42 | -24.84332 | -52.38762 | 2024-11-25 04:40:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ad059e22-9a55-36aa-b41a-facd653af0cc | -25.02755 | -51.96333 | 2024-11-25 04:40:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 864aaccc-a386-3995-9dfe-b38ffad7d281 | -30.26893 | -52.87376 | 2024-11-25 04:40:00 | NOAA-21 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 6ead5e38-3514-3211-87cb-7d20d25a0c55 | -24.60491 | -50.23107 | 2024-11-25 04:40:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 986134dd-746e-3ff6-98a4-ca5f6c8ed24f | -29.86546 | -51.16519 | 2024-11-25 04:40:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| e3ce7f3f-77e1-3cc2-ba96-e74c3ec41584 | -24.8093 | -51.90171 | 2024-11-25 04:40:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8212e065-c581-3b0d-ad86-f76f577e4e4f | -24.24231 | -50.73897 | 2024-11-25 04:40:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2276ad0b-6acd-3914-aaff-57e28372e3f5 | -26.19064 | -52.70836 | 2024-11-25 04:40:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5256c72d-0526-31af-8514-7c4ffa085ce7 | -29.68467 | -51.17487 | 2024-11-25 04:40:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 588b1fd1-805a-3bb4-993d-04a69482a6cf | -25.19267 | -49.32827 | 2024-11-25 04:40:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 56f0a6ae-fd24-3330-9906-26bb00a490b1 | -10.82794 | -37.40666 | 2024-11-25 04:44:00 | AQUA_M-M | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a38d246d-71e1-333b-9755-035a3c62a496 | 3.22748 | -60.19844 | 2024-11-25 04:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77bbfdb7-f077-39a0-a703-53f4eb825e5c | 3.22704 | -60.19551 | 2024-11-25 04:53:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a91dc1-419d-38e8-afe3-0e0f436d64ad | -1.07618 | -53.37071 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab089b0d-0848-35cd-b269-19f3ec00a507 | -4.69752 | -47.18385 | 2024-11-25 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c43aa82d-b1c9-38ea-b831-ff885c9d7d3b | -3.28729 | -53.85898 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6ecd3ac-3357-3502-94c0-2677dbb07b4f | -3.24676 | -54.22343 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3425e94f-d1e6-3c66-8b23-1673533f850f | -3.41854 | -53.28535 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d2ec961-14f6-39e4-a815-e1c0283a1dc4 | -0.34125 | -51.97989 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fedbd06-ff89-375d-af5d-a74029538115 | -2.79212 | -53.00742 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f395dfa-83d8-34ff-9249-75dd1d388837 | -3.00405 | -53.23108 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba7211e-23d6-35a6-892e-b22717e3dea5 | -3.52012 | -52.74807 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ec97f3c-4825-3e9c-b4eb-c9cae5173417 | -1.27519 | -52.17099 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 869239b1-caa9-3b61-a3c1-57760d54c425 | -2.3221 | -51.30701 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f4924d0-45e1-34e0-80a1-3d7208219e3a | -3.31653 | -53.28715 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bee1af5b-2018-3539-8173-f420560bff53 | -3.83039 | -52.29174 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c01dc535-da44-3cb8-8dd2-d220e4a9d7b2 | -2.80716 | -54.02575 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2164f79-0ed4-3207-a757-5feb2041c4e3 | -3.84405 | -49.96168 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 456cae0c-0ac1-315b-8a20-22921ad2d5e7 | -2.5405 | -53.98083 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd0f2d94-88cf-3aec-9eb3-8c14c11ca089 | -1.28683 | -51.73781 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2281bad-01ff-3954-9081-432d56aed301 | -1.24073 | -51.61415 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f270ea6-93e2-3181-a12d-cd4dc4c23db5 | -3.2856 | -50.51903 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41d1ab3e-c251-3e4a-b702-8802cf6aaf58 | -1.06655 | -53.19956 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b05d697-e257-34a4-ba28-abfa519339de | -3.52552 | -53.78675 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
