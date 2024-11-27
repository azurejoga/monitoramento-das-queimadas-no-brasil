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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75dbe2c5-7a26-3ddf-b55a-df52871be13b | -1.62149 | -52.27261 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88184e99-8c4e-3f64-a5e9-16acc0b40120 | -2.71521 | -46.25847 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6177b6b-eb5e-3195-b70c-60b6947646b0 | -2.4664 | -49.04332 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0991562f-6d33-3f0d-b516-20ee2d2f9258 | -2.02075 | -46.38432 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a24dd9f-ad51-314b-a976-9572a72b8f16 | -1.66365 | -52.71544 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b55f6bff-0f79-388a-877d-3380f1205cd9 | -2.99813 | -45.46776 | 2024-11-27 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a041a580-16dd-3e5c-8133-2e936b317201 | -3.83705 | -52.40368 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18300696-6f86-33fd-a077-f0a9290f85ff | -2.79703 | -48.68386 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08439a27-8745-3d00-9b2b-82beb22defa9 | -2.87455 | -54.00309 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6312e7e-007c-373e-8734-15dae80d5ee7 | -3.54404 | -50.40176 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e24075a-f99c-3e57-9554-2bb7facf8e62 | -3.97202 | -48.0811 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8789874-ecac-3dcd-ba33-9626118b84a5 | -1.62851 | -53.86937 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cccc45e-9006-3030-b228-7e1f179b60d6 | -1.41655 | -54.80724 | 2024-11-27 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc64ffb5-090b-39cf-abc4-0cf9f88b743c | -3.72445 | -50.18319 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77f74347-3014-32fc-a00e-4e8b068300b0 | -3.18108 | -48.44193 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e490793c-0a12-3c8c-8206-e79ba32a6f57 | -3.09779 | -50.36646 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2dd8112-024d-3b4e-8488-c80f7e0fcbe4 | -4.72938 | -46.57307 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fecb6ad7-7951-3986-b614-9218d1171598 | 0.94557 | -50.73944 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38b6bffb-d165-301f-927d-a0e8dda48a80 | -4.22824 | -48.67075 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef975f95-d930-34d1-abef-cc5162baad4f | -4.1824 | -48.6265 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 501ce9e5-6610-377a-ba40-ea8cd97f05a9 | -4.25322 | -48.66705 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcf4c25b-1e89-31e9-8129-e49238cd8b18 | -1.61158 | -52.35798 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04e54f52-a645-3bc1-9fa4-b006cd4e48b0 | -1.84542 | -47.97327 | 2024-11-27 04:42:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae149d36-9823-38e4-9ab5-35748d914337 | -3.08526 | -53.26958 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 464d8c2f-2acb-3458-aecd-9cc153920739 | -1.74808 | -52.66265 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d9b319a-b0c9-3bf1-bd36-aea2dfaa18cb | -4.23596 | -50.01961 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d48ddf-9aa8-346c-8a9a-2da2bb500bf1 | -3.27849 | -53.83742 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8147ccd9-1ae0-3b99-9628-49e829fa3703 | -3.26515 | -50.23101 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64e8b512-ed29-3ad8-bf37-b8d3e1086da3 | -3.09376 | -53.26242 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5c822744-0be9-34df-b36c-9dcb43ea283d | -4.29833 | -48.1919 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20839b6c-aa14-38ec-ab12-78a69f248304 | -1.71671 | -45.37585 | 2024-11-27 04:42:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e700000e-e8f1-32ca-95f7-dd108af728a9 | -3.49562 | -53.81554 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b50d710-3d80-3440-afc6-b7cbdfc86106 | -3.10551 | -48.02328 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12774b11-823b-3d02-8a20-a71a9998a7eb | -1.65629 | -52.51124 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0227a00d-9a53-3ccc-bf3f-21974b3f09d0 | -1.65664 | -52.41924 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5edc7289-aad5-376a-aed7-19e9f859a445 | -3.97843 | -48.0624 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38b5d437-ca03-3f41-a9ac-e424faf91044 | -3.08538 | -51.0265 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce0cb3a4-c4c4-31ba-857b-e01413a7e95a | -5.03079 | -47.01302 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 005306fe-19f7-3bd4-9d35-68221292fbe7 | -3.28871 | -51.15873 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53aff865-4182-3c6d-9a61-06cee23b2b5c | -2.90488 | -48.32511 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 644015b3-01bb-31b2-b7ed-4ec1522ca695 | -1.15076 | -53.68182 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75c7245c-a998-36c8-83fb-c92389e1beed | -3.7326 | -49.95875 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d819ea96-00b3-3cbd-8e2a-bf5fd72fa879 | -1.6877 | -52.60908 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f40728c-1356-35da-8cc1-0a7f3d793e7f | -1.368 | -52.12837 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab00def7-2ef2-3b68-b9c9-d30b6db79cdf | -0.76341 | -52.45629 | 2024-11-27 04:42:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 206d91c0-d616-3fb5-81b8-01b059238421 | -1.7623 | -53.63308 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fb72d30-9fce-32db-b75e-73fb763b9867 | -3.37517 | -50.11448 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2ebfa35d-738b-3b58-ad43-1acb28d0a43a | -2.93235 | -48.01317 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2766cb41-21e0-3e1b-a4c8-37185b46e3ea | -3.78552 | -50.2703 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c8f3d57-77d7-3715-9ee6-60307e7b36b5 | -3.46078 | -50.84394 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7381cf1d-8ead-3797-aa7d-1e7534cfdd91 | -2.87493 | -53.31876 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f60f1c1-74d9-3c1b-9d62-2fc67e4722a1 | -2.77358 | -52.90848 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0265056-fee5-3404-ac66-f617bd051d65 | -3.39414 | -51.09302 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ade20f80-9036-3c36-ad13-54266fd20ba7 | -3.09147 | -51.03103 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 264cfc62-7a8e-37ff-9cc5-ec3efb8fd898 | -2.00556 | -51.17389 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 763da1c3-8580-37fb-b6c7-8ab9cc09facf | -3.11105 | -53.26937 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4133fcf0-3c0b-3475-b00c-04977934d4d1 | -3.46782 | -51.66012 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9a14abb-252a-3b82-a884-970eef358ec5 | -3.4674 | -50.263 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d02c3a52-0395-3813-9999-da4ee5a1b693 | -3.3949 | -50.31507 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cc48b24-25ff-3a08-a9e0-1242e6372662 | -2.82473 | -46.81888 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ecd3e07-a4a7-3416-941b-b87a5f244065 | -3.29869 | -47.02182 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f5bc5db-bb19-31d2-b992-bc76a22a3ac9 | -4.21496 | -50.88817 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2199a929-bf94-3c75-994a-85abe8ad17fd | -1.31528 | -51.74768 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff73e114-7d93-3819-97ac-431b20b63972 | -3.73146 | -49.94444 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01114d2a-a8ee-3cff-83e9-f46634c17a95 | -1.87982 | -53.05912 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d17c960-b17d-3d6d-9252-51989c225bc5 | -3.27195 | -50.61966 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19734746-901e-360b-b700-e3d143b09a78 | -3.58125 | -41.9553 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a2f262a-71b5-31e3-904c-de45908c262c | -1.66504 | -52.45649 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1182eec6-453f-3cac-ae5b-669b5dfd607a | -4.11294 | -48.48737 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9772807-7994-36c1-8afe-a65dd8b01df6 | -3.70781 | -53.75526 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b48298d7-b4b5-3c81-8113-ee8c5838ff50 | -2.25385 | -53.62072 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13308659-9d41-3a9a-9700-03956a3bbc04 | -2.71931 | -46.28223 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00bd260c-ae0e-3193-8874-f0e61a8e97cc | -2.00835 | -51.17796 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 245a826d-a489-3fd7-b02d-067a39f5d425 | -3.94258 | -47.9831 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7eac9dd-0617-30a9-bc63-1ca92fd66367 | -4.32923 | -48.58434 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3479bc7e-e421-3106-836b-30797c4c6c27 | -2.54269 | -47.97485 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d98a0f5-7168-337b-853b-c2d5aad8d264 | -2.80303 | -53.01957 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6c2d46c-8ca5-3125-9574-1a5c61d62950 | -1.5136 | -51.19539 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43787c78-f517-3300-98b1-9207bb842f59 | -3.96473 | -53.85787 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7a56643-7373-3759-a217-b5b238ebce99 | -4.25548 | -48.67495 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72dead8e-3e52-3376-8163-4fb2516502e4 | -3.69044 | -50.22722 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cf814fd-62a0-3ab4-a273-71fa6ae28061 | -4.01855 | -46.43966 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac08475f-929e-3f15-bec3-b2ceed485221 | -3.23582 | -50.1807 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a176ec98-b925-3b80-bdc5-8a47b96e3440 | -1.97031 | -48.43305 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13d0a864-a405-3f52-b1d6-1490b97229b3 | -1.20215 | -51.75348 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 968ca1f1-4514-39e5-abe5-eb2e49a23d51 | -3.2681 | -50.62259 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43163c92-a727-31b6-8b79-08fff4ff0731 | -4.58908 | -44.81131 | 2024-11-27 04:42:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7af4ed9e-f6e5-3891-a5cb-69c8545dc069 | -3.27992 | -48.75068 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 855146ee-7cb6-3839-8e4c-ed0f3b7f1ab8 | -3.09735 | -53.26298 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 072f2a0d-42fe-35d0-b629-1872f2e0ec28 | 0.35473 | -50.67037 | 2024-11-27 04:42:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85d06165-eedb-380a-bf4f-ddc28585df8a | -3.66913 | -53.55445 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4740b76b-1f4e-371a-9526-8778d9b0dd15 | -3.0456 | -48.5037 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8c246e-efae-35e7-b4b3-d7df88493071 | -4.23278 | -48.64128 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30eef704-47d6-339f-ac0e-689bd78fe94e | -3.09442 | -53.25833 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a3212410-e466-35f0-bbbb-de145898290d | -4.11637 | -48.48787 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a29d14c0-0efe-3a63-8f93-e97943aa3d51 | -2.63182 | -54.38657 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e450f748-eeb4-3e5d-a431-d2df9ea82524 | -3.66604 | -51.9566 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 908cac67-c496-343a-841d-1e440d92696a | -3.5962 | -47.34631 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef45672-0ef0-37e8-ab39-a19c40890c83 | -2.48442 | -54.73398 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 927e80ce-8241-3b2e-9497-9b6fc4e16e9f | -1.98577 | -51.51817 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README67.md)
