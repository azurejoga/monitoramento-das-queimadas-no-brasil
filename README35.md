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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3a479f8-6e0c-3a30-9c15-cf26319466b2 | -3.7935 | -49.4636 | 2024-10-06 02:15:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 71d08e87-9d5a-324f-8594-2acfe6ca1884 | -3.9103 | -48.3466 | 2024-10-06 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 40c8bb54-ac16-3145-97be-ff73474316aa | -5.5716 | -44.8927 | 2024-10-06 02:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 483a500e-ba10-3b2c-a4ff-a3f61daeca17 | -5.5718 | -44.87 | 2024-10-06 02:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| bf7e1d5a-b6ad-3f85-8be1-b417c84ab7a2 | -5.5905 | -44.8687 | 2024-10-06 02:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 87c9a71d-ee50-347a-b8c3-7fb5480abc6b | -6.9514 | -59.0666 | 2024-10-06 02:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| bbd49328-2e62-3a9f-b86e-9be5b980c02a | -7.1532 | -59.2898 | 2024-10-06 02:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f2c68543-fb03-3caf-9236-4adc0c1802af | -7.9825 | -54.7752 | 2024-10-06 02:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| af1b3d4f-dfdf-3493-ab47-4b6659e32ca5 | -7.9826 | -54.7551 | 2024-10-06 02:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 67f06c5e-cd48-3ced-90b1-920278512e87 | -8.2139 | -61.2022 | 2024-10-06 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 38ca4492-db80-3ec8-a553-5af3d9280f0e | -9.1449 | -60.6612 | 2024-10-06 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c34c5ef9-1d0b-3f0e-9061-bf4672ba5b99 | -9.1759 | -61.5794 | 2024-10-06 02:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a186a3f1-a67b-373f-80fa-10f300c19b3f | -9.3278 | -46.5385 | 2024-10-06 02:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 11ffebcf-2be5-339f-a6d5-344f8331861f | -9.3464 | -46.5589 | 2024-10-06 02:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 01209304-4aed-3d20-b2b0-bb947afbc496 | -9.3467 | -46.5365 | 2024-10-06 02:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 219.4 |
| e568d8e4-3752-39ed-9016-36d41922348e | -9.347 | -46.514 | 2024-10-06 02:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 07149d4a-bba2-3dc6-b549-9ca2c6f19328 | -9.3647 | -51.0898 | 2024-10-06 02:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8090e97b-8b4f-3c97-a7ca-3098309c5f86 | -9.3835 | -51.0881 | 2024-10-06 02:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 79a0cba6-102c-37d2-9619-e76662879086 | -9.3637 | -64.3378 | 2024-10-06 02:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 9c55bced-b775-3fad-b0ae-e5ba797dba73 | -9.3638 | -64.319 | 2024-10-06 02:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 200050f2-dfb8-3075-b9fc-fd04ec70bed8 | -9.6778 | -64.6457 | 2024-10-06 02:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 958aac7f-873e-3a4d-a7ba-ae12827ef967 | -9.6779 | -64.6269 | 2024-10-06 02:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 0def63dc-63a1-3987-880e-13e26c9fcc63 | -9.6964 | -64.645 | 2024-10-06 02:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3fdcfd99-d7a0-3a4d-8fda-b9479896664a | -9.6965 | -64.6262 | 2024-10-06 02:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.0 |
| c14af353-128a-3663-adc1-4398652b9a96 | -9.8552 | -60.2966 | 2024-10-06 02:16:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4acbdd9c-e894-3454-820c-b944a1318c15 | -11.0966 | -54.2336 | 2024-10-06 02:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a1b38479-f64c-3dca-a616-fff1e88495d8 | -12.0211 | -63.7478 | 2024-10-06 02:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 21d629e1-b3ac-39b8-8f7f-c3d339b9bdf3 | -12.6089 | -53.1338 | 2024-10-06 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 7e99f610-05fd-35b2-854c-5eee53b06158 | -12.6092 | -53.1129 | 2024-10-06 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 02d6ad62-8e25-39f0-827a-bbf630865709 | -12.7822 | -50.5328 | 2024-10-06 02:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| de80fcca-3bd0-37f0-aadf-cf6674bf1295 | -12.7634 | -50.5136 | 2024-10-06 02:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 0db8f317-d5b5-379f-b715-bcbbd9fbdbbb | -12.763 | -50.5352 | 2024-10-06 02:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 332.1 |
| db3b305d-e115-3d79-921c-23f31ab0e5e0 | -12.6532 | -54.0415 | 2024-10-06 02:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7a25d398-d896-3578-8b86-eafc38534dde | -12.6283 | -53.1108 | 2024-10-06 02:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1ed36af4-4ca1-3f66-b308-d7d6c7bbb755 | -12.628 | -53.1317 | 2024-10-06 02:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a58124bd-d7ab-3df9-a9c5-d9b025135f9b | -13.6724 | -51.1911 | 2024-10-06 02:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 208.8 |
| f4e5d007-1978-322d-bb02-03d3708235d9 | -16.3959 | -57.3641 | 2024-10-06 02:16:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 97fb7791-93c2-3235-84ff-e38dd36dc017 | -16.5553 | -55.9287 | 2024-10-06 02:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| a6c55bc5-17d3-3724-aa96-92d18dbd0302 | -16.6923 | -55.9117 | 2024-10-06 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 2fbe0c67-d213-387b-a92c-f8fb1e8bc808 | -16.614 | -55.9214 | 2024-10-06 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 13df850a-5709-3768-8649-6c21d6641da1 | -16.8238 | -57.4584 | 2024-10-06 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 1276c632-a538-3fa7-9ee4-407e930620d3 | -17.1284 | -56.7661 | 2024-10-06 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 966f4140-16cb-355a-a414-d69d9129f8fb | -17.1182 | -57.4039 | 2024-10-06 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 6712e857-e841-398e-aa52-c937ba2ea5b1 | -17.0207 | -55.0371 | 2024-10-06 02:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 04cd5425-6236-325d-a973-ceae5ef63807 | -17.0203 | -55.0581 | 2024-10-06 02:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 159b71a7-1234-3ffb-b90a-ae77d60348fc | -17.1375 | -57.4221 | 2024-10-06 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| ec989e2d-b83b-31ba-a636-a118309569cd | -17.1571 | -57.4198 | 2024-10-06 02:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 9d4553c7-dfdf-34ac-b57c-ba296b865d0a | -18.6387 | -57.2785 | 2024-10-06 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.5 |
| f34fe207-73bb-3e9c-ace6-f9af391527ec | -18.6586 | -57.2759 | 2024-10-06 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 42f18d3d-ab7e-38b0-a103-fb85dd832ac8 | -18.659 | -57.2552 | 2024-10-06 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| b9b752b1-225a-3dc9-b585-c966fc0aeec8 | -18.7165 | -57.372 | 2024-10-06 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 4459fc23-e6ba-3d0b-8757-5409deb4b93c | -18.7169 | -57.3512 | 2024-10-06 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 5f01d051-258d-33b3-944e-dddcd2e56821 | -20.5813 | -49.3865 | 2024-10-06 02:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 3a71f758-1995-3874-b69a-1fbecdcd4d1d | -20.582 | -49.3635 | 2024-10-06 02:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d82d90da-2b8c-3c40-a471-925d48c255bf | -20.6018 | -49.3821 | 2024-10-06 02:17:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0e9cbd80-7f94-3096-af67-7279d7ff30c4 | -20.6024 | -49.3591 | 2024-10-06 02:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 16df36e7-8717-3241-b28d-8ac07403b51c | -21.5218 | -50.9088 | 2024-10-06 02:17:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.1 |
| 71536d34-306e-34a4-bc3c-1d8bb54ac5b4 | -21.5224 | -50.8862 | 2024-10-06 02:17:05 | GOES-16 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| e3851b9a-357b-3507-84c0-f324b89844f4 | -21.5425 | -50.9045 | 2024-10-06 02:17:05 | GOES-16 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| e0ec3f9e-e6cc-3709-a28d-d93b42e4b38d | -2.7981 | -48.6873 | 2024-10-06 02:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8d137bd8-6ca0-3d7a-9a0d-2845d34cfe20 | -2.8166 | -48.6867 | 2024-10-06 02:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 17898a9c-2852-3a71-af19-5397df259824 | -2.847 | -50.4648 | 2024-10-06 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| bda9db24-5451-36aa-b0ce-a392c885931f | -3.1129 | -48.6131 | 2024-10-06 02:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 1a655f7d-bfb1-35c9-b9f4-1f8966312c40 | -3.1314 | -48.6125 | 2024-10-06 02:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| cecc5ab7-1abc-342a-88ba-b6a2d78a9697 | -3.1315 | -48.591 | 2024-10-06 02:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1e12add0-2bc3-3fe0-9a11-2649fded2946 | -3.2223 | -48.9733 | 2024-10-06 02:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 03fbc32f-01ba-31c3-88db-0069d1104969 | -3.4195 | -50.3844 | 2024-10-06 02:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 15e13c18-b4bb-3d1e-8b99-70e76f2483e0 | -3.7068 | -41.6758 | 2024-10-06 02:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 99bcc8fa-8355-3363-9922-bcb1e4a35229 | -3.8008 | -41.5989 | 2024-10-06 02:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| e61bc770-216b-35b7-a2e8-8da110758af0 | -3.7934 | -49.4849 | 2024-10-06 02:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| d044eb3b-add0-3fdd-b6c6-670d4e5d75ee | -3.7935 | -49.4636 | 2024-10-06 02:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d2a1a44d-7e65-337c-ad49-373a94426a74 | -5.5718 | -44.87 | 2024-10-06 02:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f11ec3bd-e1e9-3935-8275-db1e016d7b2d | -5.5905 | -44.8687 | 2024-10-06 02:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a97c5f79-be22-35bc-9af3-ce1ad396b52e | -6.9514 | -59.0666 | 2024-10-06 02:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8107efe0-2ced-3c72-bf4c-1abfcf64a87b | -7.1532 | -59.2898 | 2024-10-06 02:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3210b5c9-26d3-3e43-b568-3433a62d1792 | -7.9825 | -54.7752 | 2024-10-06 02:25:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| bb02a9c7-96c7-3fbd-9a17-b305b4011a6d | -8.2139 | -61.2022 | 2024-10-06 02:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 086d0c50-fd1e-3131-a69a-50ba8b45fec9 | -9.1449 | -60.6612 | 2024-10-06 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4da49627-b71b-3b67-94ca-dda0adb2a9bc | -9.1573 | -61.5803 | 2024-10-06 02:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7f7a29b1-5fc9-31a6-9afe-2aa66d9d3e5f | -9.1574 | -61.5611 | 2024-10-06 02:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 080193b2-3724-3188-b94f-921a69240565 | -9.1759 | -61.5794 | 2024-10-06 02:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 1148f67a-78c1-35c2-9217-831e169810b0 | -9.3278 | -46.5385 | 2024-10-06 02:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d5058e69-81f7-32d9-8746-0802d3cc7611 | -9.3464 | -46.5589 | 2024-10-06 02:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 59de3982-d05f-3a23-b0a2-ddcb2bbd2d5c | -9.3467 | -46.5365 | 2024-10-06 02:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 59a3ea1a-1fe0-38fe-b2f8-f8fa94062f04 | -9.6779 | -64.6269 | 2024-10-06 02:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e7ec3b37-e2ac-384f-9499-c60acde93eac | -9.6965 | -64.6262 | 2024-10-06 02:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b3eae9b1-3801-3b00-9c12-25d3ef175683 | -9.8552 | -60.2966 | 2024-10-06 02:26:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 63165a0f-d7ca-33ab-98ba-11fdbff9ebb5 | -11.0966 | -54.2336 | 2024-10-06 02:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a38bc6f6-4d27-3100-a8c0-8700e05cb267 | -12.0211 | -63.7478 | 2024-10-06 02:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3309d381-de7c-30a0-a31f-c901d3e72ee3 | -12.6089 | -53.1338 | 2024-10-06 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4f8f80d2-00e7-3f53-b39e-12ea98461d8a | -12.6092 | -53.1129 | 2024-10-06 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 24cece9b-b566-3f05-bfd5-4ed46c32bb3e | -12.628 | -53.1317 | 2024-10-06 02:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 0fb8363b-f4e4-327b-8f61-0c4e92bff18e | -12.6283 | -53.1108 | 2024-10-06 02:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 4e43b953-9f02-31c5-bf81-07547929caaf | -12.7627 | -50.5567 | 2024-10-06 02:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d858d25f-83b9-3de1-b4bd-6db1eeeb518e | -12.763 | -50.5352 | 2024-10-06 02:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 400.0 |
| 43537157-6f4d-317f-8393-4b3c4b3417b6 | -12.7634 | -50.5136 | 2024-10-06 02:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 2cfbbd84-8479-306b-8af7-39a0154bab58 | -12.7822 | -50.5328 | 2024-10-06 02:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 5aad6e1a-4907-39e4-9a39-04ded4722a56 | -12.7825 | -50.5112 | 2024-10-06 02:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1bfaab40-96cf-3906-83b8-42e17b966b7d | -15.768 | -49.9334 | 2024-10-06 02:26:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 457d9f60-9075-3d78-8d66-6fd5bd3291e3 | -16.3959 | -57.3641 | 2024-10-06 02:26:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |


[Clique aqui para ver as próximas entradas](README36.md)
