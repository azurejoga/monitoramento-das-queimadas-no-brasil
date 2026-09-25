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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 784810c9-3bb0-3194-a45f-a25413c22e44 | -11.35325 | -43.4243 | 2026-09-25 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09bc5370-a174-3d6b-9692-74ffc607daf3 | -14.73057 | -46.22532 | 2026-09-25 04:27:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 80bd28b5-4c48-3208-9ddf-d83561b4cbc4 | -15.95902 | -42.96001 | 2026-09-25 04:27:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc15de0f-0b63-3e35-8c48-2ee77cdd2581 | -19.91427 | -45.53637 | 2026-09-25 04:29:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fa1849e-b210-3585-a07f-49f9769535cf | -21.2004 | -48.27283 | 2026-09-25 04:29:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0931b93-9819-3a8a-baa8-2ffe7dbe365c | -23.00585 | -48.62016 | 2026-09-25 04:29:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7b3000d-dd59-36a0-a603-7d2f8e6a73ba | -20.45168 | -47.55883 | 2026-09-25 04:29:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feb02266-b1a1-364d-bd80-87262a93b237 | -21.05155 | -48.47224 | 2026-09-25 04:29:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a4a1292-55a2-3cac-8011-df07f773dd7a | -21.04812 | -48.47156 | 2026-09-25 04:29:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d08249d-169d-3fc8-bc03-2f3973776f7e | -18.99786 | -46.33921 | 2026-09-25 04:29:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 384f5d46-1dd6-3d38-9be7-386c5fa45fe3 | -18.08905 | -51.14719 | 2026-09-25 04:29:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d171cf9e-354f-31b5-90d2-7e84a630f442 | -20.4521 | -47.5622 | 2026-09-25 04:29:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd3bd082-fd6f-32c5-8933-9cbea944adb7 | -19.87341 | -47.05756 | 2026-09-25 04:29:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 121df23f-ed99-3b1a-89a6-030259efe7cc | -19.52344 | -44.73358 | 2026-09-25 04:29:00 | NPP-375D | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3721c769-18e3-38ab-8763-424ed7c2b18a | -18.95844 | -46.95267 | 2026-09-25 04:29:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0f25484-c2d3-378e-95be-eb3c05364736 | -18.6061 | -48.25616 | 2026-09-25 04:29:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 108a9f88-d090-3af7-ad9f-904ed9036b3f | -19.87676 | -47.05819 | 2026-09-25 04:29:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14298238-0a98-3b22-a9b9-d57cb5ef1462 | -19.3754 | -46.32178 | 2026-09-25 04:29:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d58de27c-7b56-397c-ae19-714aa8f1e90e | -18.9557 | -46.94836 | 2026-09-25 04:29:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4421b55a-d627-3123-a653-48a61514ddbb | -21.20105 | -48.2689 | 2026-09-25 04:29:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddbdd454-56e5-38d8-bbca-5d7ec60ab878 | -21.20026 | -48.27185 | 2026-09-25 04:29:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2ec2639-0186-30b1-9902-f5a2d9210de6 | -18.42445 | -47.2008 | 2026-09-25 04:29:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28b14064-ea6e-3d00-8216-ef9f7c75ac3e | -18.95905 | -46.94896 | 2026-09-25 04:29:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 931a4c16-a8ea-3a12-ad63-e7d81b5145c2 | -19.30406 | -47.44162 | 2026-09-25 04:29:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df0b797c-3072-3cf6-8d90-55ca70b87307 | -19.18537 | -47.3587 | 2026-09-25 04:29:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e5cd3a9-2d1e-3ad4-be02-221aa8792b60 | -19.11125 | -43.87411 | 2026-09-25 04:29:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddb35c61-095a-31a0-83d1-dd39d627673b | -9.1536 | -59.464 | 2026-09-25 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1b7867dd-84ec-3d4d-8985-747c00e73f56 | -9.1535 | -59.4834 | 2026-09-25 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d069faee-be6e-314f-a520-ec810c1fa1a4 | -3.03246 | -50.39446 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80c0220b-deff-3fd1-b2f1-9a9671473b43 | -4.11818 | -51.08009 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 200021e9-a63c-38d1-b6ba-f6d747e9d552 | -1.21648 | -54.5583 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72d0cdce-de92-3977-8da6-6f91fc20638a | -1.71931 | -49.98297 | 2026-09-25 04:44:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6661d20f-8df5-3f0e-a360-d5527dee0815 | 1.48859 | -56.04214 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9427c1ff-2008-3711-a348-ed2328a41b26 | -3.23101 | -46.94102 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f71237dd-9265-37fa-ac6f-318741e098b2 | -3.73483 | -47.97848 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01ea3089-7d84-3eb8-bc31-19ef37b72258 | -1.12656 | -54.14198 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf7096c-8e83-3ac4-9748-0865e3db2280 | -2.61345 | -51.74075 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc180a08-2193-3925-b50b-82912524d122 | -3.19274 | -50.75108 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14f95be7-33bd-3d03-98ba-1e6c6fa1f089 | -3.19215 | -50.75476 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1ca55d2-3c33-3821-98d5-b725aca74a0a | -1.96356 | -48.3767 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 700b6661-0081-374c-a5dd-7ee0a42d792e | 2.39953 | -50.76424 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5e09f76-ff38-3e51-9b87-5741713a6bfc | -1.53088 | -54.29335 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fdd70d41-508a-324d-8a2a-1348924e90c7 | -3.17857 | -48.01781 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94a508eb-b5f8-38b6-a684-4505f8b94fb3 | -1.21524 | -54.5661 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c653b06-6307-3237-9008-91e86d74d60d | -2.85496 | -48.563 | 2026-09-25 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40f36e41-169f-3d6e-ae07-15eddf737250 | -2.95269 | -48.58897 | 2026-09-25 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b416480e-c89c-33c3-b330-6963de243654 | -1.14601 | -54.10153 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c1fc7785-95d6-3a79-a8d4-3ffb2b7b830e | -4.2846 | -48.60774 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdf4c8b0-1ffd-3baa-8440-bb4935d62a27 | 1.59909 | -55.85976 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d90de7d3-3c2e-367e-9b48-2688f833cef7 | -1.22019 | -54.56292 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ce619f5-3b36-32e8-98dc-af9ac9f703f8 | -4.12117 | -51.06155 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4aac8995-80bb-36bc-9a5e-d4025a9c009f | -2.96248 | -52.15639 | 2026-09-25 04:44:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9356990a-e061-3ccd-af72-c3c3fc35422b | 0.07867 | -51.14481 | 2026-09-25 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4949d954-3fda-39cc-9863-0770422b00c8 | -1.53512 | -54.294 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b3ddf7f-5ffd-3b85-822f-0c747a57ff7a | 1.62003 | -55.89671 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c7935b9-aada-362d-9042-f489e7dc1d63 | 2.25694 | -51.65551 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92366e5a-79d4-35fd-b999-10088bd787f1 | -3.60773 | -48.91453 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73bdb9eb-e08e-3fc2-a547-44a0d4db78f8 | -1.02981 | -53.73759 | 2026-09-25 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fd6e350-8ab9-364d-9b6a-fa91b841124a | -3.50205 | -50.74669 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a5eeb5c-9390-30e9-ae5c-f01189eab5a5 | -3.72784 | -49.05714 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c41c5ff-bafa-323c-90a0-16c3f8f20061 | 0.49957 | -60.5957 | 2026-09-25 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7032277d-6504-365c-8266-de759faa37ee | -1.21585 | -54.56227 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c24609a5-0d7b-3f05-8d06-726e7440400d | -1.13885 | -54.09243 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2718b96-4ec8-30a1-a1a2-82a12fb0390a | -3.17748 | -48.0248 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ecf794-88e3-39a6-8dd0-ee0cd21fe626 | 2.35096 | -50.76967 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 862a3922-5165-3579-a397-5c0ffad4afff | -3.01227 | -51.53387 | 2026-09-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a838eada-ef1d-37eb-a47b-bae29a4282a2 | -3.2356 | -46.9341 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 554072fd-4613-3cbd-9537-8db297d1e97c | 1.58604 | -56.00892 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa98e80c-7086-3960-8103-ce2d8d851688 | -4.27415 | -48.63095 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f30a70d1-463a-30d6-bfd7-582763472d28 | -1.60288 | -49.81514 | 2026-09-25 04:44:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04918810-9594-3870-8d6c-6e654370ff53 | -4.7783 | -46.50216 | 2026-09-25 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4670f6d-3a35-3a18-9806-1b568869aa12 | -0.50293 | -49.14638 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 188133c8-b4d3-3b85-9bf5-9ca5b9facdf5 | -4.17004 | -48.71025 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f493191-3efd-3896-a0a6-a211c7e2af1a | -2.16888 | -48.32466 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2916fa5-dc31-319b-9741-1f5768245000 | -4.93175 | -45.66108 | 2026-09-25 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 042b6824-0559-3fa2-93a5-49fce7c8642d | -3.70243 | -54.19243 | 2026-09-25 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 515ab48b-a292-3b25-b656-9eb191846613 | -0.93565 | -47.55308 | 2026-09-25 04:44:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6543a09e-0ea6-372f-a5d6-adfb337d78d2 | -1.29542 | -54.2231 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef9932af-a41d-3b56-b97a-1f978cb5f93b | -3.87646 | -51.92566 | 2026-09-25 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863f87f6-ca7e-3dd1-98c9-0da7e02478f5 | -3.7088 | -54.20439 | 2026-09-25 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d7eef00-80c7-3c7c-ac75-fe4a7df75e02 | -0.49905 | -49.14934 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b73d715e-e2ca-3da8-a5aa-843f139efca2 | 1.5865 | -56.01181 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b660f27-d680-32f4-8332-9f5c5a4c8ff4 | -3.20626 | -53.40018 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 646e739a-38e8-3d05-8b3f-00373a540572 | -4.29623 | -48.62021 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e337c8a-e330-3864-86c7-9072e725041d | -1.38129 | -52.5586 | 2026-09-25 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3c309c1-1eb6-3368-9a41-a3245fdae872 | -2.74238 | -51.54592 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef9dd6c-0c31-3393-b6fc-e60b976f68bb | 1.48488 | -56.04949 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99aa7960-11c7-3dab-9c2f-cc37acb3155d | -3.03304 | -50.39085 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 346a8f0b-8aa5-3197-b1ad-22f44515d6c8 | -3.49641 | -50.73834 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6549550-99e8-32e6-ab50-7387389dc166 | 1.48402 | -56.04582 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb4c58db-68b6-3957-9812-7943c141ba2e | 1.63286 | -55.94676 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7163375e-2c4f-3b70-9688-f573fa2f01ce | 1.87517 | -50.66792 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91465135-90f5-3f62-bf4b-601beaef2e31 | -3.03188 | -50.39806 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf0d27ab-b30d-3507-ba3a-c9cc669e4471 | -1.95916 | -48.38306 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bce1e9e-2b0d-3c0c-ac41-161c57da8318 | 1.59791 | -50.90773 | 2026-09-25 04:44:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee3f0e5f-fbcc-3cfd-818b-9d5d156d2dde | -2.86542 | -49.63197 | 2026-09-25 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4704948-d2b5-313e-a55a-7fd34ad2a8b5 | 1.58687 | -56.01427 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4305106-8e62-393e-a7c3-7824c7c5541f | -4.37797 | -46.23864 | 2026-09-25 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73ebced0-9902-3f13-a4e6-ce369f88e3f1 | -1.34334 | -55.47734 | 2026-09-25 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9484de21-c056-383b-ab7e-d953245cfcbf | -1.53447 | -54.29799 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
