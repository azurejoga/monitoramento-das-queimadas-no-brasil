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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91ee283c-40e9-3f36-b45c-a371654f4b7e | -12.0314 | -45.1901 | 2025-10-04 03:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 279.8 |
| e44d67c8-3b21-3b0d-a3b1-3e153877427a | -9.3276 | -54.5215 | 2025-10-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 693b2977-2de2-3a91-9f9e-dd10b4bfd37d | -9.3379 | -45.7947 | 2025-10-04 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 4a8378fe-95ba-311f-aa63-5fb0dddae734 | -5.1965 | -45.0768 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 287.8 |
| 2a91ac28-ca1d-3c4e-b197-81f29e137390 | -5.2154 | -45.0529 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 56949503-4214-31cc-908f-16edd1a2dd01 | -10.3346 | -50.3188 | 2025-10-04 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1b7c5d3f-23b7-319e-aa59-a553c6477a2d | -10.3154 | -50.3421 | 2025-10-04 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4b553208-dc63-36c1-8829-33601ea5452d | -15.0374 | -49.4549 | 2025-10-04 03:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9f901836-cee9-3b20-8fbe-55007cecf6c1 | -17.7044 | -47.0821 | 2025-10-04 03:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7079b3e7-a351-3023-9192-f624721efd38 | -5.1967 | -45.0541 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 200.1 |
| a7a0be85-1cef-3217-b4a3-a74b18fa412b | -4.4443 | -43.263 | 2025-10-04 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 114a3fda-fac1-3fa3-809c-c3c941038b4f | -15.6023 | -52.4675 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8bc4e345-d9b3-3c78-823d-cfce158b853a | -15.6019 | -52.4888 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 8f81abfc-26f7-331f-9ece-87c6e5846df6 | -4.6133 | -43.1594 | 2025-10-04 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c597c964-c5eb-3367-bc4b-dfb84888c693 | -4.954 | -45.0694 | 2025-10-04 03:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2e963536-1df8-303f-b6c4-03da16de8eb2 | -12.031 | -45.2132 | 2025-10-04 03:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 02a71635-ef6e-367c-9060-162e9d384f64 | -5.2152 | -45.0756 | 2025-10-04 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 6cf2e19b-2482-32ac-b276-80dbb1ce68f4 | -5.1967 | -45.0541 | 2025-10-04 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 42825f95-2508-31d2-a2fc-8f635605cf22 | -12.0507 | -45.1872 | 2025-10-04 03:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| bf5e8bd0-89d8-30d1-8d40-08361bdf00af | -4.4445 | -43.2397 | 2025-10-04 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| f719af83-94e8-3d08-b717-beb53ed0dd7b | -12.0502 | -45.2103 | 2025-10-04 03:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 366e9e6e-1bd3-3804-84c9-d54e0bdc9952 | -11.9147 | -46.3726 | 2025-10-04 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 3056fcf6-37b2-3ece-9c5e-a25d7e6fbb8b | -10.3343 | -50.3402 | 2025-10-04 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 4947f4a0-e0e1-3c5f-af02-22c7b7e16984 | -10.3346 | -50.3188 | 2025-10-04 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 11c38f96-0736-3a31-91f1-38860e2680a9 | -14.2515 | -46.076 | 2025-10-04 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f1b3370e-ba5c-343e-9f11-c1920740d20f | -2.9013 | -50.7351 | 2025-10-04 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| fd9ea6a4-fba6-3a5a-9c51-5fb96a7a135b | -6.0806 | -42.5118 | 2025-10-04 03:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 240.3 |
| 7d6cbf71-7d51-3043-8741-0e0e08151ae8 | -4.4443 | -43.263 | 2025-10-04 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8ee4e223-8ec2-3226-814f-bc700d6115d5 | -11.9343 | -46.3472 | 2025-10-04 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c00f1522-4576-3181-9455-882dea88e0ab | -14.2321 | -46.0794 | 2025-10-04 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 48ee938f-095c-3f26-811d-160fb05c1705 | -13.3229 | -48.0993 | 2025-10-04 03:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d4d5a689-358c-3324-a6e9-6d3665aaa9c8 | -11.9339 | -46.3699 | 2025-10-04 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 74f8d7f5-5253-3aa8-a97f-a916ae8ebecc | -12.031 | -45.2132 | 2025-10-04 03:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 5bc10174-c6e6-34d2-b4d8-688f55b6adfa | -15.6019 | -52.4888 | 2025-10-04 03:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 94eb104d-bb39-303a-82db-ad2cc1010d9a | -14.2316 | -46.1024 | 2025-10-04 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 685faa5c-4ce7-3d29-8412-6e65daa3bfc3 | -12.0314 | -45.1901 | 2025-10-04 03:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| d5a32dba-a9e7-339b-b2f7-ac7c081f1961 | -6.0809 | -42.4881 | 2025-10-04 03:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| ffa019b3-0844-33d6-9d01-5635db03bc54 | -6.0618 | -42.5133 | 2025-10-04 03:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| b286ba53-2d0e-3ffe-85ee-9e0ed88bceab | -5.1965 | -45.0768 | 2025-10-04 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 292.5 |
| 91b9f827-6a00-3023-8f06-ac8ff164f981 | -9.3464 | -54.5201 | 2025-10-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7f141f4d-4d97-3e81-82e8-678414280e26 | -17.7044 | -47.0821 | 2025-10-04 03:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e4fc4e86-deff-3a72-bbfe-2c78ee5ffd63 | -9.3276 | -54.5215 | 2025-10-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 50522d4c-2abb-3cf8-adea-7f0973f8bc7e | -4.4258 | -43.2408 | 2025-10-04 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2687d38d-8521-3dc5-b801-96da69a01e97 | -5.2152 | -45.0756 | 2025-10-04 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| cf66bdc0-6a98-3c57-9aa7-94a4bb4d9a24 | -15.2205 | -56.8414 | 2025-10-04 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| adfa3cf8-8a2b-30bd-9914-6cf8c3cc8a16 | -5.2154 | -45.0529 | 2025-10-04 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d7849833-6479-3cbc-ac5b-255f454e610b | -10.3154 | -50.3421 | 2025-10-04 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e1ae89d7-e017-31d7-af00-7affd1342591 | -17.7038 | -47.1053 | 2025-10-04 03:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 81174ee6-dd39-3822-8c25-327a036ce75e | -14.672 | -48.2933 | 2025-10-04 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 30e1270b-d60d-3e43-9ebc-6b2ab26a7e17 | -14.251 | -46.0991 | 2025-10-04 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| afdcbc07-128d-3124-9335-f14da9365874 | -11.9151 | -46.3499 | 2025-10-04 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 302fdb1b-3092-34ad-8bfd-37fc7a092fe5 | -8.6322 | -54.9949 | 2025-10-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 63e7391d-d8fc-38c7-a026-fef91beed4c3 | -5.40886 | -41.34526 | 2025-10-04 03:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 83406eb2-f60f-34fe-a154-8f7c0fb189c0 | -3.84631 | -41.57723 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ba9e3ab9-268f-3d68-93c7-9a67f469dbed | -4.61668 | -43.15739 | 2025-10-04 03:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| dc40ba7f-6e16-34da-8ff9-fac9c5785fd9 | -3.84436 | -41.5647 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 7098b762-05d3-3947-b513-92868067dcb5 | -4.60985 | -43.15633 | 2025-10-04 03:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5b03d968-d285-3588-ae9a-f32f4b88a926 | -3.84976 | -41.57084 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e34f08eb-8096-378c-a221-65d04937ce9e | -3.84716 | -41.58614 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d86d1f48-8011-3c58-a060-d9f98be29522 | -5.01773 | -43.66381 | 2025-10-04 03:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6e7678a-fa94-31fb-b5f0-e20fe77d95df | -5.08206 | -44.08882 | 2025-10-04 03:21:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 44ec9f38-3109-3fc4-97cd-0a0976bcdaa2 | -3.84721 | -41.57213 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 3ee5655e-0937-314f-bef3-e3f7aeb37e21 | -4.14189 | -42.17194 | 2025-10-04 03:21:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c1ef1eb0-8dcd-389b-b3c6-26ecc9111dbe | -3.84521 | -41.55973 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 6b07fc51-0c1b-3fa8-a20b-a496bcd5bd3f | -3.84264 | -41.57484 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| f9cccfe1-1bd8-3b2e-98c3-13e0cee75efb | -3.84803 | -41.58104 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| c4068939-d369-327c-b4c8-ad940c6fee5b | -3.8489 | -41.57593 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f0d32986-a9b9-3e10-b1fb-3c8d61c3623d | -4.61779 | -43.15113 | 2025-10-04 03:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 9afa4d88-b243-3fc3-ba21-664c3765a72c | -3.8435 | -41.56974 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| f6223614-2299-38ff-81da-faab5cf12b76 | -5.26328 | -39.26348 | 2025-10-04 03:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f05c0c31-b291-310e-a941-4fb6f8226199 | -4.61096 | -43.15007 | 2025-10-04 03:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b0881fe0-5723-3f07-b901-93a1a3098206 | -5.84237 | -39.25803 | 2025-10-04 03:21:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8f3a702-7400-3ab0-8dab-bb0e7653d071 | -4.14834 | -42.17312 | 2025-10-04 03:21:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 71fba4ab-fae2-3aad-b604-ed8e104f4efd | -5.38646 | -36.83576 | 2025-10-04 03:21:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bd13692-d98a-3715-aaf3-257a6f70cff1 | -5.41477 | -41.347 | 2025-10-04 03:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d82991a3-1fcf-3eeb-81a9-1e7268637fc4 | -5.01887 | -43.65733 | 2025-10-04 03:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5abf19d9-8ae6-3ea0-bd77-cb120e701c58 | -3.8454 | -41.58234 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| e211261e-d765-32e1-8110-05ff31643744 | -3.84176 | -41.57997 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 13989cb8-29b2-347f-8b2b-7ec4e8f0e2bd | -4.4281 | -40.76529 | 2025-10-04 03:21:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1506f285-b4b9-3adc-86fe-884fde65721d | -3.85062 | -41.56578 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8b90b029-7800-3fe5-affd-8bbcce3d375f | -3.84811 | -41.56708 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a599077d-3d0f-32aa-a9c0-2bc24b96770a | -3.8445 | -41.58742 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 84515f07-d0dc-381c-857e-2bc1c9613425 | -3.849 | -41.56207 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2f23252d-a08b-35be-8460-c41aa61c0188 | -5.41062 | -41.34626 | 2025-10-04 03:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5e6df488-307c-33de-b5d5-3f934220883a | -5.41141 | -41.34191 | 2025-10-04 03:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 95597baa-764e-3c2a-8c6a-f20d0199d51b | -4.16244 | -42.17188 | 2025-10-04 03:21:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80b19f4b-05b1-3875-8ff9-3f2eaea8f78a | -5.8476 | -39.25891 | 2025-10-04 03:21:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e861a0f6-643e-37a0-af8e-4fa339bed78b | -3.84273 | -41.56104 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c5cad5de-1a5a-3a15-9006-233be8db58b3 | -3.84185 | -41.56603 | 2025-10-04 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 2645366b-e4b9-3081-bfcd-73c493f78a89 | -6.98335 | -42.79781 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 498350e3-da88-3b17-8742-fd960f762b4c | -9.66065 | -42.93234 | 2025-10-04 03:23:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 59e3e363-4426-3da9-a4ae-afee9e4b598a | -7.75115 | -42.52324 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ca271047-1a9a-3f5b-8d9b-fad2d76660c0 | -6.28372 | -42.44808 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9bc8d5a9-a488-3e50-9831-c0bfa2661374 | -7.74345 | -42.59996 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 90a0bcba-86fa-31ad-974f-b9ba58465abe | -5.49058 | -44.10522 | 2025-10-04 03:23:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 56df1056-9d7f-3bd3-a462-0e4cfcec6e97 | -10.27519 | -44.34769 | 2025-10-04 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ebed0c4-7fe7-399b-99c6-4c7d81af6016 | -7.10938 | -35.03772 | 2025-10-04 03:23:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38c94f0e-153f-39d4-97fe-3c2810fc105f | -7.32642 | -41.44622 | 2025-10-04 03:23:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e939ce8a-9a50-300e-8bca-9cb0e2d9e000 | -7.79077 | -42.57611 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0b1fb4a9-8353-3bc0-a327-7da72d0e13ec | -6.71283 | -42.80756 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
