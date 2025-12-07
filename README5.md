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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8cc4c1-205d-31bc-b620-859314f83678 | -20.91576 | -56.3712 | 2025-12-07 05:37:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ceaa6972-401b-39fd-9338-cd2c8620682d | -20.91993 | -56.38201 | 2025-12-07 05:37:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f5b0c8c-dbf7-3731-9816-3d67c0e3437b | -20.92099 | -56.37191 | 2025-12-07 05:37:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 057f8cfb-d98c-30b7-a6d2-da0110612839 | -22.02885 | -45.93821 | 2025-12-07 05:46:00 | AQUA_M-M | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 27132dd4-bfcc-388c-81d7-f89d1107cd2d | 2.00832 | -55.69462 | 2025-12-07 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf242349-3d4b-346a-bf56-2bfd036ca911 | 1.96991 | -55.69735 | 2025-12-07 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b15771e-9646-3406-bb1d-a892f704caf4 | 4.34867 | -60.23591 | 2025-12-07 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 961af1fc-4fd3-3b33-a668-768c0d76dfe1 | 1.9753 | -55.69246 | 2025-12-07 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e279852c-6d81-3060-b8e8-92b45c6e6aa3 | 2.71905 | -60.74345 | 2025-12-07 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3500d179-a222-33cd-9802-e8b312d37a3c | 3.30771 | -60.79194 | 2025-12-07 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 353cf55c-0256-3126-b129-7254b7501c57 | 2.00907 | -55.69911 | 2025-12-07 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc01fb24-a7e1-3b9b-baef-54a11b67739a | 2.00753 | -55.68996 | 2025-12-07 05:52:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfc417ac-d0fa-3299-99ca-b321f35a974e | 2.7184 | -60.73949 | 2025-12-07 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 841de1a1-da70-397d-a296-39ce74ee6215 | 4.35214 | -60.23625 | 2025-12-07 05:52:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 859d7a12-7ec5-3cbe-8529-8abec79ca427 | -5.13704 | -60.38923 | 2025-12-07 05:54:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dfe83603-5bc0-3478-86cb-e0b071d46945 | -5.13977 | -60.38606 | 2025-12-07 05:54:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55a816d9-c1f9-3be3-9624-aa280fb36ca8 | -10.54606 | -59.41832 | 2025-12-07 05:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ac4d3ed-bcd9-39e3-b8fe-008964a8a70d | -10.54656 | -59.4143 | 2025-12-07 05:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecb09b80-9c7b-3724-bff9-cdff3b7dac1c | -5.16832 | -39.1175 | 2025-12-07 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 303c3acc-8351-3374-ab33-f961f9c2df89 | -9.05557 | -35.60466 | 2025-12-07 11:36:00 | TERRA_M-M | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d508add2-5693-3ae9-a4cc-f766d9c89435 | -8.54263 | -38.63101 | 2025-12-07 11:36:00 | TERRA_M-M | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7baeebd4-b3f7-374a-98a7-ea776853be96 | -7.73659 | -38.14613 | 2025-12-07 11:36:00 | TERRA_M-M | MANAÍRA | PARAÍBA | Brasil | 2509008 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1908c733-8681-36c4-9572-ae46435ee8e7 | -3.41726 | -43.12809 | 2025-12-07 11:36:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 3f4467fe-b850-3d8f-b469-b6d199c8d65f | -6.14558 | -37.91088 | 2025-12-07 11:36:00 | TERRA_M-M | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 9cefc573-0ade-3cbf-84ac-cb3716032426 | -8.1986 | -37.999 | 2025-12-07 11:36:00 | TERRA_M-M | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4fe05230-9db0-3a5a-8310-5ce45e1b717c | -6.73707 | -38.74426 | 2025-12-07 11:36:00 | TERRA_M-M | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d6b8d695-8ab2-3aad-a01d-84381706751a | -3.51385 | -40.21416 | 2025-12-07 11:36:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 760e7332-00e2-3083-b18e-8c314d952301 | -6.14432 | -37.91971 | 2025-12-07 11:36:00 | TERRA_M-M | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 9ec30b03-2c7b-30e0-b583-6e361fe8fc08 | -6.50051 | -37.5531 | 2025-12-07 11:36:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 01bb243c-2c3c-3b77-90fc-452896093744 | -7.70923 | -39.10406 | 2025-12-07 11:36:00 | TERRA_M-M | PENAFORTE | CEARÁ | Brasil | 2310605 | 23 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 844c8d4a-bdcc-3441-939d-6c92eaeddc99 | -5.16701 | -39.12656 | 2025-12-07 11:36:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4c942957-cbf4-3eb5-b3ee-2ee1b92b3ca8 | -9.05714 | -35.59297 | 2025-12-07 11:36:00 | TERRA_M-M | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |


