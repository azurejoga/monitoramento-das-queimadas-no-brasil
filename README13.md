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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a72f966-eeed-30c0-bc30-da2c8e9d6833 | -2.83633 | -45.47646 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0039f30b-b85d-30cc-809b-bcf686ae010d | -2.86426 | -46.73854 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 84bbcd91-9797-332c-a1aa-6f9c12e35205 | -2.59397 | -47.55396 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b5057f4f-ad6e-30bc-9722-9c241567a304 | -2.97444 | -45.82717 | 2024-11-17 01:04:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1e25a10b-01c3-3515-a662-a53bff0a6f34 | -1.80154 | -48.43973 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 7fc5fdff-2665-3c73-ac35-d2ade9d84147 | -2.90345 | -53.05255 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 546cb141-6bf8-3816-8b0e-e72b7f13d19a | -4.82262 | -47.32167 | 2024-11-17 01:04:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d174375-9c80-3aef-b3de-97ac8f30dee7 | -0.93993 | -51.72126 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d4465e5-9ddb-39cf-86f8-cabf8c805215 | -2.62306 | -46.02232 | 2024-11-17 01:04:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 84a5e8e5-2aef-366a-af1e-bdf610a19b12 | -0.40112 | -51.62756 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9db7dcfb-425e-3413-b2fb-2015c9ad2c52 | -2.16539 | -48.76604 | 2024-11-17 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e9ab5e97-c70e-3be3-a494-612ba28c0b88 | -3.04571 | -47.98205 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1ce1e0e8-ecb9-39dd-8847-5a11be17a05c | -5.28161 | -44.90688 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 423920ce-dd3d-3e45-b53b-f2e810207624 | -4.23342 | -41.93465 | 2024-11-17 01:04:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| f77ec14e-6d88-3ff5-b746-c0e3906825a2 | -3.0652 | -45.35701 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 3d4ebd7e-c4ab-304d-bfd9-45d58354b133 | -3.62436 | -50.22282 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 735fed2a-88dc-39c0-af3e-c3975e33b640 | -3.52972 | -50.2762 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd6f2712-9d55-3277-a48a-598f6ad77fcb | -3.79474 | -51.37461 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fba0c6ea-8326-3b25-8cde-0bcfe292e656 | -3.92475 | -46.52985 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a84eda09-edb1-3221-90c1-4c444a714bfb | -2.86006 | -46.70995 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 679217ff-e7a9-3134-ae9c-c9581535e7cd | 0.51311 | -50.74593 | 2024-11-17 01:04:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| becb7f7d-3d42-3783-bed2-d400140e689c | -2.10255 | -48.39508 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| d7bc9ae5-d631-378c-ac29-09dbd2dc42ec | -3.53739 | -50.26001 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fc481b22-fdae-358a-bd96-0f7c4657cdd2 | -0.92837 | -51.7677 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25fc80bf-a8e7-340f-ab24-55c2270d3598 | -3.62506 | -43.16393 | 2024-11-17 01:04:00 | TERRA_M-M | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| fb676dae-6aba-3d1f-a3ce-1c15c04d7e8b | -3.51155 | -49.94773 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ff7f3d4f-b33b-3563-9f9e-0a3abfed59ea | -3.01857 | -45.40643 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 6aba2016-58b4-3474-9c43-9063ddac8053 | -3.52058 | -49.94644 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4a365c03-af3f-3b4b-acd9-43fdd3ff493e | -1.7916 | -48.44115 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 06a64211-3962-3ced-8576-ad690de17484 | -3.47614 | -43.88657 | 2024-11-17 01:04:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 706fca36-040f-3e5d-87d7-99b9c5e98352 | -5.26931 | -44.90888 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 30a7ef34-d4ab-3cbb-b104-fe4632de45da | -2.84941 | -44.95691 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 40.4 |
| d012f949-4813-3dfc-8afc-30af3bf0ccb5 | -2.98728 | -52.59837 | 2024-11-17 01:04:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| afd8cc75-3490-3ad7-908c-24c38c143d0e | -2.3316 | -53.57201 | 2024-11-17 01:04:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 24cade36-2000-3d03-8410-bd59e0e41ce8 | -5.69188 | -46.56542 | 2024-11-17 01:04:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e27b3957-b7f4-3dca-a138-9496f29fb91c | -2.59885 | -47.55917 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1e15a30b-eb6d-3e0a-ab0f-092b761c46fd | -3.81995 | -50.23807 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5f8ca5be-76ad-3ca8-ba40-46ccb7ee6e58 | -2.39818 | -49.04049 | 2024-11-17 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eadd2c6f-bd1f-3bd2-b283-902f6d7eaf97 | -2.85164 | -44.97 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 561686ce-fb2d-310c-8d5a-290ecfd29998 | -2.67395 | -46.21177 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 447fe434-d945-381f-b36c-e6f412800fc7 | -2.99631 | -52.59705 | 2024-11-17 01:04:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b015be2e-e1d2-35b4-977b-113c29e09ba4 | -2.86677 | -48.7247 | 2024-11-17 01:04:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dcc27152-0bc0-3893-b075-d775d3117590 | -0.32374 | -48.69027 | 2024-11-17 01:04:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d9c705db-00ee-38b3-badd-9d142a61ad40 | -1.79317 | -48.45243 | 2024-11-17 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| eaee40c4-dbe2-3f39-94ce-cfe023316dde | -1.01053 | -47.76249 | 2024-11-17 01:04:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 98b08571-b106-3e23-8c4a-8c37b9189e7d | -2.96011 | -45.81219 | 2024-11-17 01:04:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 154.8 |
| cd4c5886-daa1-3959-8d02-f850ddb69d8b | -3.06868 | -45.46649 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 47e6d07b-b22a-38f5-be70-2524be60c907 | -2.23552 | -53.61195 | 2024-11-17 01:04:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 705eda92-597e-3c6e-84e2-a0eac3d4905f | -3.30038 | -48.8394 | 2024-11-17 01:04:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f17e8c6-429e-3206-8e14-efcebc48f327 | -1.52019 | -47.46626 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6fbe80ee-636e-39b4-9722-febb4322cfc9 | -4.41069 | -45.51539 | 2024-11-17 01:04:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 271ec313-c034-3435-b903-0c171566be76 | -0.9527 | -52.40959 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 152c1e4e-d520-3e0f-ba09-8d952a5b43c4 | -1.29667 | -51.96055 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bc3f2b97-32f6-30a6-aa1a-712ada409d00 | -2.66793 | -46.1901 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| dd04dcaf-484f-3323-8ab1-6883b26ce36a | -0.93354 | -51.74009 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b842745-c65f-3ab7-9f05-029010d47cca | -2.67265 | -46.22162 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d7cde9b7-2b55-389b-9234-3a26133b2cee | -5.40553 | -46.34918 | 2024-11-17 01:04:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 07be64bd-0240-3715-939c-83c14f0488bf | -4.39877 | -45.51709 | 2024-11-17 01:04:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 3ca90259-e096-3dc1-bb2a-ce108ff1cc0c | -1.59047 | -50.43948 | 2024-11-17 01:04:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a74d2ca0-c2f9-31a6-b8e9-546e5739997c | -3.91045 | -49.04399 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a11934ce-8e58-3891-a553-ec149bb19139 | -2.09713 | -45.27554 | 2024-11-17 01:04:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3bf05693-fca3-3c47-b98d-e76b674844b9 | -2.51632 | -45.45602 | 2024-11-17 01:04:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0413fb7a-10ec-35a7-b164-aea4c1235469 | -4.03881 | -44.75813 | 2024-11-17 01:04:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0e6eb33c-7e96-3654-b710-59dd9aba7bb4 | -4.23076 | -50.67996 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| eaee95ed-1918-3f59-bed0-5a98bceebf61 | -1.29383 | -51.7456 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f4035fba-73a4-3269-a1c5-3e2e399fcc94 | -4.22287 | -48.64496 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f7703c83-de1d-3219-9cfa-27ffc4f10887 | -3.34379 | -53.31728 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0cb1f885-ae09-3b74-8ab4-13e3f7cf5541 | -3.48513 | -49.69567 | 2024-11-17 01:04:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 428205b7-8d97-353d-861b-ba0800430559 | 0.11497 | -49.8464 | 2024-11-17 01:04:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de993223-883e-3b8c-83b9-12367b93eb12 | -1.8339 | -46.60975 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f61dbd95-b90c-3908-82d3-5f4b2cd14981 | -1.57154 | -47.41179 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 08f797dd-e079-3bc1-b45e-4642e5692019 | -2.59016 | -47.57329 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 7417dece-430a-3b58-bc11-be1d220f2143 | -3.78558 | -46.04726 | 2024-11-17 01:04:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1e825433-bd6f-34ca-84ef-07c3142d610d | -0.02925 | -51.66846 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f5fbff99-4d11-3826-aeb9-eccc406a16eb | -2.21804 | -50.51128 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a5d9b80b-ddf7-3c4c-8d7a-1e5adeb6f57d | -4.05109 | -44.75059 | 2024-11-17 01:04:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| db689646-493d-39d8-977e-dde7745f2cb3 | -0.32076 | -51.50414 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5dc1e189-8e8b-3061-867f-30658c6d9ec7 | -2.3071 | -48.46732 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 89cbde51-f0e7-3b33-bfe7-fde50effe844 | -3.40704 | -50.25391 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 32bfacf5-6281-3c3e-8587-8c3cb2a96e68 | -1.61831 | -52.49208 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d499d251-741c-3bbf-ab7e-675c51a61624 | -0.3999 | -51.61875 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1ef061b-1778-3f09-a0b8-569633c45bd2 | -2.27996 | -47.92481 | 2024-11-17 01:04:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 23c4a88c-ae6a-3de6-976a-a49806de0db8 | -3.50514 | -51.02085 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7aa4f184-2631-3eff-a42a-dbe6df85e416 | -4.21111 | -48.69912 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 98fc3c06-6c28-31e7-869d-e7b32a3f7942 | -5.5892 | -45.19913 | 2024-11-17 01:04:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2ff2ef84-0b14-30a7-b30c-453fe1dc70f8 | -1.90949 | -46.56789 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 300.2 |
| 166b8a12-1f30-3778-91c9-f00400b8f675 | -2.22083 | -47.22087 | 2024-11-17 01:04:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5d4061b8-191c-334e-ae14-5ba31db4f02f | -1.9094 | -46.57753 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 353.2 |
| e4a92aad-7fa3-39be-8c70-25e373a42e20 | -1.50948 | -47.46783 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a659b1de-649a-34dd-b679-fabebd5543cf | -3.21143 | -46.68328 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8244aca7-4747-3ce3-8184-b9fa17b7d83e | -3.60703 | -47.53591 | 2024-11-17 01:04:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 55b0aa44-6e08-3cd6-b1db-ebc27c82d287 | -3.24618 | -53.52699 | 2024-11-17 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0f927f73-6a21-319f-a2aa-5b6f528841c1 | -4.22432 | -48.65531 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 98604b6c-5acf-3272-ab2f-daf76177fdab | -1.10903 | -51.93622 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 888e7521-8cb8-3232-80b2-3c9433a7f059 | -2.93127 | -46.72203 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 499bae54-de68-3593-9e01-409432cd3cce | -1.9116 | -46.58307 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 26642040-ea44-334e-8bac-49fd0d1c9003 | -2.333 | -53.58196 | 2024-11-17 01:04:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f1bd6cc-a2de-3a6c-aec9-11cb0c85df03 | -2.2316 | -48.37067 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38f76d59-4df0-3152-9fbf-78ab8f15025f | -2.98856 | -52.6076 | 2024-11-17 01:04:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8d3c9e2a-123d-36ea-b00c-62bfd3fbaa46 | -2.59896 | -51.79072 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README14.md)
