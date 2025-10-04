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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dacac23-cfad-34b8-98e3-a6d2e21c1800 | -4.44965 | -43.24092 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| f203cd17-1aa8-359d-b631-fe76a8f65727 | -3.16362 | -49.4773 | 2025-10-04 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 787011c5-5fe8-32cf-817f-9fd308b2b867 | -3.94806 | -50.62035 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed80f6b7-c64f-3529-b3c5-2b045cb008ac | -3.69944 | -49.57038 | 2025-10-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd825525-5106-3e06-9fdf-e1835e6ecac6 | -3.53074 | -52.868 | 2025-10-04 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3fda400-9dec-346a-8afa-afed8b990539 | -7.54885 | -42.40268 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 26bc8203-978d-3301-92ea-bd9fadf60d44 | -9.3435 | -54.52221 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b7ca2070-bb9a-3f83-b7b1-1734da8b18e8 | -9.93605 | -50.24366 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 907913fc-9339-3b2b-9dd4-1764b081af63 | -4.89322 | -49.96338 | 2025-10-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 941bfe40-b581-3c61-a69c-b8af21fdf6d0 | -7.16548 | -46.21858 | 2025-10-04 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b05156f9-5e66-3ee5-ba5d-8e25b6f3046f | -8.61385 | -54.96664 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daa3f0bd-8033-3d4a-8a37-5fd85f652215 | -7.54585 | -42.40606 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 60a5dbdc-a71e-33b1-a5f8-7be8fc220c79 | -6.74483 | -44.59849 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7947a4b-dd6e-3833-803a-0507ffec048c | -9.34406 | -54.51847 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f0959535-800c-3511-ba01-fd0e3c13fc81 | -3.69157 | -50.88823 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03ecf000-2e0e-3f91-8e83-3a2590d42a31 | -6.65245 | -42.80453 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ddd10d1e-e2d0-39cf-b2c6-2b9902344830 | -5.63031 | -51.89275 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1de5eee0-0b44-325c-8d93-354c3f5517d8 | -7.79581 | -42.55229 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c4a2922e-4ed3-3658-9807-08562370f30d | -6.67367 | -44.20384 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf9134a6-6569-3b66-a20d-de0c36b75e2a | -5.08063 | -44.0886 | 2025-10-04 05:04:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0bf8614e-6c68-3c97-b819-3d86e4673d8e | -9.34683 | -45.80195 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3159dfe-203a-36d7-a7c3-2fb1380a93bc | -3.11949 | -59.11285 | 2025-10-04 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03a83723-0e23-3ef7-8dfc-216c6cbab730 | -6.36986 | -43.90403 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e77d803-3eda-3bce-ae35-e65232736e3a | -7.73844 | -42.61147 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 33998238-2021-314f-b273-be5dad722ca7 | -8.54228 | -55.0148 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da04fd40-4f02-3613-accc-7ac2cd6cca7e | -9.48225 | -54.60067 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37b0b12c-844b-3823-b99f-fe682694b474 | -9.10526 | -44.39234 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b56933f-5b81-3447-9adb-4625d8373efc | -8.61947 | -54.97485 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e66f3968-dd62-3bb3-8d3f-3fc67f668d11 | -3.86447 | -51.81103 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8c8fc9-9ab2-3cb2-b420-e721651ab8aa | -5.07896 | -44.09162 | 2025-10-04 05:04:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dd81e90-fd83-30a6-a940-5920500fd868 | -8.51161 | -54.59428 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d72ffcdf-d2f7-3323-89bf-981a6e68e1d3 | -10.07549 | -48.18463 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dea2ddb5-e208-3c70-ba3d-9e2e59404ede | -3.8458 | -41.56962 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 4620ebba-b6a7-30ff-968b-a3285dbbfc98 | -5.91019 | -49.29885 | 2025-10-04 05:04:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e071a27-f8c6-3a6d-969f-54a43e62b7f3 | -7.55683 | -42.39672 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ef739be-e701-3f9c-b29a-b65b2eb45442 | -8.11088 | -55.0792 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdf1e10e-20f3-3014-943c-c7f05d57ec3b | -4.43516 | -43.24982 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d111be8a-9198-3c88-8cc9-eb7891919a2d | -7.25118 | -48.47915 | 2025-10-04 05:04:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c3b57c5-a2ba-3aa0-826b-0a842a5cb8ff | -6.87868 | -47.23458 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4b9e13f9-8565-3e22-be0c-f1570f13b29a | -9.4659 | -45.53769 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab4fb27c-5041-3910-8071-04bccb49e95a | -7.74138 | -42.52926 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5f83381a-dc9f-36b3-8dee-b1f266eb7493 | -10.02255 | -48.27427 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9c0687-0041-3749-8368-b5788ac4cbd9 | -7.87522 | -61.68405 | 2025-10-04 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 329f9d58-e57d-30b3-bf75-44230f8e79a7 | -7.64946 | -46.76975 | 2025-10-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2819d62d-16a8-33e1-8ae7-5d82d5de5200 | -6.34318 | -43.46399 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9cbd1f9-6c7b-3baa-8ffa-d27c36056394 | -8.10421 | -55.07816 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d38232e-8ad6-3641-a59b-66ce6321f7d7 | -8.85765 | -46.73924 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b0725eb-da7a-368b-a77d-6d790cf76880 | -9.90187 | -43.73954 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aebd4ccb-ab00-3b62-8c72-fc3150dfecfa | -6.67685 | -44.20873 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85687e9c-9ab2-343a-9fed-5c749709c31d | -10.34262 | -48.16355 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7880142d-96db-3064-bf3d-0d20edae8900 | -8.33318 | -54.82426 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5b3d98e-45cd-3ac9-a9e8-01e956164555 | -4.31643 | -48.08509 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b83e286c-fc15-31ba-b420-7c8f09665a79 | -5.50703 | -51.01527 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d2078ff-67a5-3cd6-aa8b-aae5999e3208 | -7.34753 | -44.3446 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1cc170dc-f625-3217-bcf8-d392a3d52bcb | -3.84152 | -41.56845 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b03d379c-fd86-37b3-a7a0-6cfba3dc1563 | -6.67639 | -42.83485 | 2025-10-04 05:04:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4df6d954-ba8c-3c2a-8810-da428c15207f | -7.53879 | -42.40496 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3c9ff9e1-bb13-3d15-8c21-f9f8b9bfd7a0 | -8.10907 | -55.02432 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3026d2ca-18ff-3acc-9aed-6f950197e0b7 | -4.95895 | -45.06719 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f2ad2c7b-6642-39ab-ae5f-53aa86d55197 | -5.48944 | -52.13392 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a82dd6c-6551-3d46-be39-189be9bce8ed | -6.2252 | -55.63701 | 2025-10-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dff1b65b-26e3-38ed-8584-e056ce038159 | -5.19617 | -45.06657 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 6477c422-b287-37a8-ac33-033abe950ac9 | -3.88154 | -52.18743 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ab203ad-ae94-30d5-8473-e35f9ccbb7cb | -8.52252 | -50.0323 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddc157f8-e952-3913-b89e-8dacacb4623a | -9.32815 | -54.53138 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b681e5f1-4170-31ce-810e-d4e0373d8311 | -8.06342 | -44.79911 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8533ebe5-615c-3120-ae39-c5862fc5c687 | -9.34975 | -49.00545 | 2025-10-04 05:04:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdd5c250-4704-3254-b173-0877d8520973 | -7.74411 | -46.31335 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| be94a44d-a736-32ef-9251-2988f2fe6944 | -3.31167 | -48.72377 | 2025-10-04 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc981bf0-4124-3995-89e6-1c60c022740f | -10.28154 | -44.34116 | 2025-10-04 05:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c571cab5-9bd0-33de-9f08-0fd10128df34 | -6.6573 | -42.81004 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 00d6aa28-7eb0-3d66-9437-e558b0d34bfc | -8.54176 | -50.15884 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 697fcd43-a83b-3c78-8a41-c58f2e3e3620 | -5.33161 | -43.34391 | 2025-10-04 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53f25c22-63a6-37d8-b972-1ea46a60f6c5 | -4.55616 | -50.47488 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4158d7bb-e308-35e9-a123-04ee666d8649 | -5.83775 | -42.88386 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 36eeb966-acf1-3737-be48-d4b59c129214 | -3.19779 | -51.68593 | 2025-10-04 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60646b7c-21af-36d4-82fa-0d5c1822f663 | -3.4531 | -53.8322 | 2025-10-04 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93d4b6d6-b493-3d76-bbdc-26a6f71b1fa0 | -6.94629 | -63.10043 | 2025-10-04 05:04:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57c5b14e-a81d-3f52-9a4d-e1020646524a | -3.63753 | -51.79889 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7cd42f2-cece-3906-ba8f-24333a3ecc08 | -3.64466 | -48.32148 | 2025-10-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 744a15e1-dc2d-3e33-a3e7-69ddd5e1a96f | -9.11022 | -44.39298 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ea177f6-4846-3d34-a518-9bb5e73f9c9f | -8.61502 | -54.98153 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77afd159-f67b-3ea0-9078-9729783f4f3a | -9.31339 | -54.53373 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aebc13c6-7363-38bc-95b9-5e10b830783d | -6.07714 | -42.5138 | 2025-10-04 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bb0a2354-3db1-3cb5-8d97-80c514568bfb | -9.91925 | -50.5018 | 2025-10-04 05:04:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 153cc941-80ee-3331-8a75-a0f65705b885 | -5.68547 | -42.85044 | 2025-10-04 05:04:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e2535f4f-5ac3-3703-a9db-6e7ed6cdc47a | -9.6383 | -54.31025 | 2025-10-04 05:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6a8ed6f-ccac-3ef9-8ccb-a92970061bb0 | -6.61677 | -44.29388 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26c500a6-7617-3401-9699-ad63a502e4d5 | -6.7054 | -42.82584 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 040c4336-73bf-31a2-b31b-3033539902a1 | -4.95249 | -45.07084 | 2025-10-04 05:04:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 07f1be12-4dd0-335f-8068-18143bfcf5ba | -7.93602 | -55.02355 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6500ab5-ceaf-3f43-b2f0-563232130d4a | -9.56471 | -48.68285 | 2025-10-04 05:04:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac53894c-d19b-3e67-b01d-a1ca84d97f9a | -6.21932 | -44.27459 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b25dd3eb-b637-37fe-83e0-b3d5d25fe2e4 | -8.53763 | -47.21412 | 2025-10-04 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee970f13-4b1a-3d21-8ea2-625c685057e9 | -7.77586 | -42.59737 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d66af8a7-49e7-33bf-97a2-775af61da9da | -5.48432 | -44.11126 | 2025-10-04 05:04:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2e65bc36-abe5-3421-a895-bde5f1e2e320 | -3.76867 | -52.07012 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46119ef7-9d70-3e90-ac08-aef0f384c09e | -8.11033 | -55.08276 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71971029-9817-3b9b-8cc9-07ba83c4d92c | -6.70957 | -42.79404 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9f5f0ed3-ca48-3ede-ba58-db8fde96cedc | -6.17045 | -43.92104 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README103.md)
