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

## Dados Diários - Página 211

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60445e69-c7bc-3ca3-a311-d6399ff87905 | -8.9244 | -45.6367 | 2024-10-03 12:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 1e52ea1d-0264-3aff-9251-de625bc94a01 | -9.0515 | -67.871 | 2024-10-03 12:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e2771c3f-40ec-3fd9-a887-816947e04cf7 | -9.5772 | -46.2639 | 2024-10-03 12:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 274.3 |
| 1fbf122e-561d-3bd9-a79c-fc8c660f8ab5 | -9.5775 | -46.2414 | 2024-10-03 12:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 4c9a77a7-63f8-3262-adb1-c53f9e5b74a9 | -9.3833 | -68.3256 | 2024-10-03 12:36:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 35d7edff-723b-33ed-ba43-81b35001325e | -10.4775 | -48.1829 | 2024-10-03 12:36:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d89966a2-2ef6-3542-be0c-e26af0f461f2 | -10.6981 | -46.1287 | 2024-10-03 12:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e395de5f-4175-3c0b-9b28-f7e8a61cc6dd | -10.5736 | -48.0839 | 2024-10-03 12:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 245e5b75-7d7c-3eb2-97a0-3fd081a42507 | -10.7312 | -47.6904 | 2024-10-03 12:36:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 24f298e1-7222-36ee-ae1b-a3ed21dbb5ee | -11.0342 | -46.5369 | 2024-10-03 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 372bb28c-87c0-3fe8-99d6-456d63948d7a | -11.0345 | -46.5143 | 2024-10-03 12:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| b2c432b8-a450-37a7-87e3-c0f75a5842bf | -11.1579 | -45.9551 | 2024-10-03 12:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8e0a10e1-c746-36c8-8909-cf5f400a738c | -11.2783 | -43.388 | 2024-10-03 12:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 93ffe69c-5a89-3d97-b94c-498b540686f8 | -11.2779 | -43.4118 | 2024-10-03 12:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5d0a8aa2-cc80-3813-b2b7-f89a90262763 | -13.0017 | -44.7357 | 2024-10-03 12:36:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d84ab903-24b1-3e2b-8a19-7f7f2d1502e7 | -13.0591 | -51.1623 | 2024-10-03 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0ad52ea6-5345-3eee-b82a-c160c8f423af | -13.0594 | -51.1409 | 2024-10-03 12:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.6 |
| cd873f74-76a6-3d81-8959-87ea04fd2f75 | -13.1805 | -45.4489 | 2024-10-03 12:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 41c15237-398c-30c0-9faa-d2d57a8e3d88 | -13.1976 | -48.6489 | 2024-10-03 12:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0ddf8276-d655-3dd1-abfb-4e4414cdfd24 | -19.0344 | -43.1944 | 2024-10-03 12:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 147.7 |
| e5042d8c-0226-3390-9b42-90f85c06e4fe | -19.7908 | -45.0014 | 2024-10-03 12:36:55 | GOES-16 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 151.6 |
| ed03fd63-f481-34d8-a1b1-03f6219d08fc | -7.2199 | -46.6751 | 2024-10-03 12:45:47 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a53704e8-9c2f-38e7-af95-b94bde8b0a41 | -7.6486 | -45.2218 | 2024-10-03 12:45:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 283e6583-eace-3de4-9a6f-7a95d3728293 | -7.8149 | -45.4782 | 2024-10-03 12:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| f64201cb-e4d6-39e3-9c24-11868ebe822e | -7.8626 | -43.0969 | 2024-10-03 12:45:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| ed94cfb3-29ce-3e36-a554-fa45b1a3a3d7 | -7.8629 | -43.0733 | 2024-10-03 12:45:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| d41c7d35-8222-3908-b6b6-aaae95c3fc13 | -8.1937 | -46.8324 | 2024-10-03 12:45:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b7114601-5c0e-3e02-b3fc-697dd182d3e2 | -8.1567 | -43.7211 | 2024-10-03 12:45:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 3e5ea866-2512-3d03-8ea4-76320e36e58e | -8.1756 | -43.719 | 2024-10-03 12:45:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 5c0d9e9d-0899-3bdc-b8fc-b684a538f640 | -8.7225 | -45.204 | 2024-10-03 12:45:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 3c4bdc32-2cff-35f9-81f9-b846741aa7fc | -8.7414 | -45.202 | 2024-10-03 12:45:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| c159e700-2c00-3aee-a9b5-63991b126573 | -8.9055 | -45.6387 | 2024-10-03 12:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3422f5ec-77cc-3ccf-84de-c5d4fced0831 | -8.8356 | -45.2145 | 2024-10-03 12:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 19febad5-e399-3dbf-82ac-421129e79adb | -8.9244 | -45.6367 | 2024-10-03 12:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 363.3 |
| 2e92faa8-506f-3e7f-ad1f-44bec211292f | -8.8885 | -44.1045 | 2024-10-03 12:45:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 778e5f68-58c7-354e-bc34-cc52febcfff9 | -8.9074 | -44.1024 | 2024-10-03 12:45:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 0cefd405-47af-3ea8-bfd1-48750e59c7ad | -8.9433 | -45.6346 | 2024-10-03 12:45:57 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4938e6b6-a962-3e5f-a279-3614c88cd3dc | -10.2381 | -47.7038 | 2024-10-03 12:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 71b8deca-0600-30ce-879a-15f90addc6f1 | -10.2195 | -47.6839 | 2024-10-03 12:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3c5dacb2-8376-3cd8-8192-9e49cba8de75 | -10.7312 | -47.6904 | 2024-10-03 12:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0259517c-0309-3e86-b68a-92454d844d3d | -10.7459 | -47.9757 | 2024-10-03 12:46:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5da6dd7a-a1e9-320b-98c6-061f4b7b99fa | -11.0345 | -46.5143 | 2024-10-03 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| ec25048f-1ffc-3d5c-9b08-6a274189ee99 | -11.0342 | -46.5369 | 2024-10-03 12:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2d026517-7a8c-366d-b724-31603b51d1fb | -11.2783 | -43.388 | 2024-10-03 12:46:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c3a9482b-b4a4-3a84-8e3c-7985f9cb856f | -11.2563 | -46.9348 | 2024-10-03 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| fefcb728-4449-3ed9-b50e-70c9926fc077 | -11.2758 | -46.9098 | 2024-10-03 12:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 241b32f4-3c37-36df-9204-262f6135ebab | -11.9671 | -50.181 | 2024-10-03 12:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 25367b68-59e9-3f83-bb82-90a2afa4ace2 | -12.7815 | -50.5758 | 2024-10-03 12:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3c4b83f6-90bf-3d9c-8ea0-c4752f4af562 | -13.0017 | -44.7357 | 2024-10-03 12:46:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 97482113-67aa-3f54-a12f-2af5a1a49225 | -13.1976 | -48.6489 | 2024-10-03 12:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 7f8c2a2c-0d24-3bc8-ae47-aca9f8694929 | -13.0783 | -51.1599 | 2024-10-03 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7cd1e7db-e01b-395d-8f81-63109d40967b | -13.0022 | -51.1266 | 2024-10-03 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5a3bba99-8eb4-379b-9fce-c4fa01117b71 | -13.0594 | -51.1409 | 2024-10-03 12:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 486e112a-b607-33a5-8151-1b503960e5bd | -13.2493 | -51.2452 | 2024-10-03 12:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c3e4b952-aef7-3932-b925-62fd14c3bd0f | -13.2496 | -51.2238 | 2024-10-03 12:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4cd9689f-c6b5-3edb-ac55-8499ad5d7762 | -19.0141 | -43.1998 | 2024-10-03 12:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.9 |
| 5f4fefbe-9377-3b91-a242-fa68d313c079 | -19.0344 | -43.1944 | 2024-10-03 12:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 137.7 |
| 4528526c-93e2-389d-9a74-f819c4f7a03f | -19.2962 | -42.5779 | 2024-10-03 12:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.2 |
| bd18db80-8481-3790-90aa-6e12625511e4 | -19.2954 | -42.6032 | 2024-10-03 12:46:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| c67fb23f-918e-3adc-b3ea-52e71935a827 | -10.23 | -47.73 | 2024-10-03 13:04:28 | MSG-03 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 099596ff-469f-354a-a378-c792f1430160 | -6.9479 | -47.6668 | 2024-10-03 13:05:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 28a5cc82-7103-38cb-8605-f2c8765cceed | -7.2199 | -46.6751 | 2024-10-03 13:05:47 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c27849a9-5a81-3154-9a8c-acad30128311 | -7.6441 | -42.458 | 2024-10-03 13:05:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| cb778dbe-ad40-348e-be5b-1e4a37d3492f | -7.8629 | -43.0733 | 2024-10-03 13:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| ae85d67f-225c-38bd-b615-bdf451290d30 | -7.8149 | -45.4782 | 2024-10-03 13:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4c96bbc5-9773-32ed-b1e4-57db1f5b3531 | -7.8626 | -43.0969 | 2024-10-03 13:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 025dde9f-2a4d-3981-b860-acb5c2fa74f3 | -8.1951 | -43.6703 | 2024-10-03 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 08343ec0-61ea-32cc-9436-1269cb854607 | -8.1937 | -46.8324 | 2024-10-03 13:05:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a1eeac99-1849-3f7c-bdf7-5cae42b058ef | -8.1759 | -43.6957 | 2024-10-03 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ec9f8500-39fd-3fbd-8888-fd61876ba433 | -8.1756 | -43.719 | 2024-10-03 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 114.6 |
| b2a85e92-3f28-306e-a8b7-791bf1cc06b5 | -8.157 | -43.6977 | 2024-10-03 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 2458c17b-42ed-3137-afe0-729418969716 | -8.1762 | -43.6723 | 2024-10-03 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 68609d34-4069-3e89-a1c2-0a3794fe5f3e | -8.1567 | -43.7211 | 2024-10-03 13:05:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 0aa973e7-08d4-3592-b020-f08ae6cc1b95 | -8.7225 | -45.204 | 2024-10-03 13:05:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 06a6993d-60fa-329b-8e67-4a192a810add | -8.8356 | -45.2145 | 2024-10-03 13:05:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 260.5 |
| b19e0454-b541-3759-8f85-c6a26122c8ab | -8.9244 | -45.6367 | 2024-10-03 13:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 242.7 |
| 7142838c-2403-3792-8533-b089e611f8d4 | -8.8362 | -45.1688 | 2024-10-03 13:05:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0fa6822f-2172-3105-9af5-9a19865c324b | -8.9074 | -44.1024 | 2024-10-03 13:05:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| f8116ee7-b608-36f2-ba39-7b25a9f7a24b | -8.9055 | -45.6387 | 2024-10-03 13:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 0bfcfda7-37b1-3c52-be8c-28e3d466d53c | -9.0149 | -67.7423 | 2024-10-03 13:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| af288577-e758-303f-9844-766a952fb9f4 | -8.9791 | -67.4099 | 2024-10-03 13:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 432be74f-f32e-3579-8d92-da5b32835b2e | -9.3833 | -68.3256 | 2024-10-03 13:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 69fc332e-30e5-30d6-9ce7-df4863521531 | -10.7161 | -46.1942 | 2024-10-03 13:06:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 0543e1b0-7442-3f6a-8b47-97756099f4d0 | -10.5926 | -48.0817 | 2024-10-03 13:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4262ab23-06c0-3bdc-a1a8-ace70a92e9c2 | -10.6981 | -46.1287 | 2024-10-03 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.2 |
| a02953fe-e502-3bef-b920-3fb6260ac0c7 | -10.6791 | -46.1311 | 2024-10-03 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| eb677f7d-9b3a-3153-9085-82e84ace3c7c | -10.6794 | -46.1085 | 2024-10-03 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 0eb5e199-72e3-3537-a323-c059cef1e731 | -10.7158 | -46.2169 | 2024-10-03 13:06:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 2b732852-c56f-345f-8089-268b2fd06bb7 | -10.7348 | -46.2145 | 2024-10-03 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 0f73bf7b-3bb7-3328-8bd7-1825a71caf9e | -10.7459 | -47.9757 | 2024-10-03 13:06:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 097db7ba-4f1e-397c-8fcc-b4b4fe316782 | -10.7352 | -46.1918 | 2024-10-03 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 04b063aa-b95f-3cfd-bb47-fb356bc1fd2a | -10.7122 | -47.6927 | 2024-10-03 13:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7445c22b-4bd5-3353-8419-e317652fabe9 | -10.7309 | -47.7126 | 2024-10-03 13:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| d4bd83ed-7654-3315-8e1e-1698b126b60d | -10.7312 | -47.6904 | 2024-10-03 13:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 92f973d0-ebaf-32e4-9f7f-2026ed8abd59 | -11.0345 | -46.5143 | 2024-10-03 13:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 4c3396b1-fc1d-39f8-94a9-b171a14566f1 | -11.2779 | -43.4118 | 2024-10-03 13:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5f13a481-22b5-3193-b21d-e8a3daedc741 | -11.2783 | -43.388 | 2024-10-03 13:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1da0707a-c28d-3a32-b865-9c1614f27bd4 | -11.1579 | -45.9551 | 2024-10-03 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d2ba6c38-5704-3f9c-b677-d17d256f1849 | -11.2563 | -46.9348 | 2024-10-03 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 96371d24-6838-3212-9ad7-629ee8b4ac95 | -11.2758 | -46.9098 | 2024-10-03 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |


[Clique aqui para ver as próximas entradas](README212.md)
