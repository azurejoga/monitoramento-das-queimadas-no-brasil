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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a59edb6-1861-3779-a153-3e6c44567f29 | -11.9938 | -45.1496 | 2025-08-13 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ae7aa178-dc87-31ee-a926-4243807550df | -16.3153 | -52.9201 | 2025-08-13 00:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 4d2d7fc5-cd36-3a2d-a07a-4a1913f7c1d5 | -21.1405 | -49.1022 | 2025-08-13 00:40:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.9 |
| 95e1c0f7-4f8c-38fe-be53-77b8e19e8d1e | -7.2746 | -60.6294 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6cf58fdf-5191-3a7a-b8f6-1b298b56ffd5 | -7.1483 | -60.1174 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 96a82482-bdd2-3d57-b918-aadced71bfe7 | -7.1482 | -60.1366 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d8c16557-f4a1-3613-a656-17757c21b477 | -12.3225 | -46.0638 | 2025-08-13 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| df572cfd-89cc-358c-ab59-7b4032ace1ab | -11.7695 | -48.2021 | 2025-08-13 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| d05a68dc-7703-39d1-90cf-69f2a90937f8 | -9.1894 | -59.6558 | 2025-08-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8cdf2117-29fa-3950-84f5-42b09ccf6ce6 | -9.4192 | -40.3695 | 2025-08-13 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.2 |
| ab4ecf77-01cc-346f-9a32-f87fcb48c56a | -9.208 | -59.6548 | 2025-08-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0d843e22-6f22-37ee-8791-8a09d12e1ae9 | -8.1061 | -55.5501 | 2025-08-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 6b400d49-817c-3b1c-8313-ca9db34b4672 | -7.2562 | -60.6302 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f664bb7e-7274-395d-be9c-b1664f42bbe6 | -15.0787 | -51.364 | 2025-08-13 00:40:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 1f7fd9e7-26eb-3fbb-b777-5511fa8a4317 | -12.3229 | -46.0409 | 2025-08-13 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1ee38da8-9b49-3eb6-aa2a-3406e34922ca | -10.9693 | -49.5639 | 2025-08-13 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a58357d7-01f3-33f4-a8ec-3039af1b78de | -7.1299 | -60.1182 | 2025-08-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 2094c394-adaf-3b18-a7f8-0f403019a12d | -8.1061 | -55.5501 | 2025-08-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 73848da0-676f-3535-bdf4-4be26cf76c68 | -7.1298 | -60.1374 | 2025-08-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| e64859e4-0ad9-3d73-881d-6881d19d5ec9 | -21.1405 | -49.1022 | 2025-08-13 00:50:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| d32c1651-8f83-3d69-8b81-bdd3774ed251 | -7.2562 | -60.6302 | 2025-08-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| cca57125-ea1f-3a8f-a090-0ea95e3ff563 | -11.7508 | -48.1825 | 2025-08-13 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 852da26b-bb3e-3ada-89f0-82e6dff96485 | -22.3869 | -45.4716 | 2025-08-13 00:50:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 244.3 |
| ff16ae05-caca-36ee-b905-5ea73062cfd0 | -11.7695 | -48.2021 | 2025-08-13 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 78667f8f-e8b9-329e-8226-1e07adb424e3 | -7.0935 | -60.0237 | 2025-08-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a3017408-9f4e-34e2-b72e-41a666eb1f88 | -10.9689 | -49.5856 | 2025-08-13 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 457423d0-0a37-35df-a0be-4a14caccb512 | -15.0981 | -51.3612 | 2025-08-13 00:50:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e5e30e6c-0bb8-3b6a-9bfa-7eb5b1900ba0 | -22.3877 | -45.447 | 2025-08-13 00:50:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| d2e96be6-3fb9-37f0-9548-28f29fd6f13f | -9.4379 | -40.3917 | 2025-08-13 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 7f727b44-002f-3de8-9e31-a9b3b2da4d79 | -9.4196 | -40.3447 | 2025-08-13 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 06ebc6af-0152-3fc9-b5f0-9575ad2b22da | -10.2415 | -50.2215 | 2025-08-13 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 42cbb152-787c-3c32-ba21-8eca6f32d499 | -12.3229 | -46.0409 | 2025-08-13 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 46f3dba3-e535-3e4d-b28a-6a4d50bc662f | -6.6112 | -43.8941 | 2025-08-13 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 46eb0340-fed0-3560-a096-c61cf0db822e | -7.1483 | -60.1174 | 2025-08-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 334d464f-d9be-3889-bf11-b1aa8857dfe7 | -9.4192 | -40.3695 | 2025-08-13 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 197.0 |
| 829851ef-3211-3b6a-b399-c8fe4ea835a7 | -7.1299 | -60.1182 | 2025-08-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 9d502e47-985e-388c-8138-4ea89e1a174d | -21.1205 | -49.0837 | 2025-08-13 00:50:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.4 |
| db6a0f3e-f71e-3506-93c8-2e42cd38570e | -9.4387 | -40.3419 | 2025-08-13 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 220.3 |
| 8d0cafc5-ad88-33af-8858-d93c3f7df85f | -21.1199 | -49.1069 | 2025-08-13 00:50:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 165.1 |
| 2d447d36-c78e-35cf-878b-c25ce6a6356c | -9.208 | -59.6548 | 2025-08-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4d4b3e33-587b-3db3-a38d-2956e525db6c | -8.1247 | -55.549 | 2025-08-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7334a2b2-cb5a-301c-971b-575ba7ac790a | -9.0521 | -60.6466 | 2025-08-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0b89c94c-2de5-3acf-b13c-387e51cb13ff | -9.1894 | -59.6558 | 2025-08-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 82f95229-461e-3316-bf8f-604f80a4b434 | -7.1482 | -60.1366 | 2025-08-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| cda73584-1036-38a5-8dca-03359f143a93 | -8.1058 | -55.5901 | 2025-08-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 9cc725f2-86f8-318f-9eac-5e3e1818d82d | -11.7699 | -48.18 | 2025-08-13 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| e8777c4e-62e8-3398-97f8-a8edda5a48aa | -8.1246 | -55.569 | 2025-08-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 09a361de-4830-303b-9aa6-d1d5c0ddfae1 | -9.1892 | -59.6752 | 2025-08-13 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fb093654-b04a-3a5c-a289-199b6488c93d | -10.9693 | -49.5639 | 2025-08-13 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8ccf77b1-809c-3215-a718-39b0ee2869ac | -8.106 | -55.5701 | 2025-08-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 87acfa97-04ff-37b3-a0b9-bafab18bbb03 | -9.4383 | -40.3668 | 2025-08-13 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 504.6 |
| e2814cdf-bf69-3bad-b26f-3cb0f93b985f | -22.4079 | -45.4657 | 2025-08-13 00:50:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| 5fcac303-dbd5-3c7b-a462-35e467df3094 | -9.1894 | -59.6558 | 2025-08-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| bc69a6dd-74d5-3777-a8ff-384c29195980 | -22.3877 | -45.447 | 2025-08-13 01:00:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| d8ce0e3c-7936-3d04-b57f-96c74b127228 | -7.1298 | -60.1374 | 2025-08-13 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 4f08abdc-e85b-38ae-89de-2083423f8110 | -10.2415 | -50.2215 | 2025-08-13 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 29a69b5f-547e-3522-ab7a-17c148cbff50 | -7.1299 | -60.1182 | 2025-08-13 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 51d7f673-5fb8-3c24-b094-193451ecdc60 | -11.7695 | -48.2021 | 2025-08-13 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| fe6b8690-0789-3898-a077-921631d79411 | -22.4079 | -45.4657 | 2025-08-13 01:00:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| f5b0b2f2-e705-3f59-82a6-ee81fe390e05 | -8.1061 | -55.5501 | 2025-08-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3e2556bd-8a32-36f4-9360-b7a606b8a401 | -12.3225 | -46.0638 | 2025-08-13 01:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 76c97543-2e85-3285-a469-6558d9e554ff | -22.3869 | -45.4716 | 2025-08-13 01:00:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 271.4 |
| 4c11c127-939c-3492-8247-03f980b62a6c | -8.1246 | -55.569 | 2025-08-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 04cba562-1c17-3934-9fac-415ffcac0d64 | -11.7699 | -48.18 | 2025-08-13 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 0dbe3227-e373-3129-93af-0800e0385d86 | -7.0935 | -60.0237 | 2025-08-13 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 42591ad2-07cd-3806-ae5d-2a9d64b77d6f | -12.3229 | -46.0409 | 2025-08-13 01:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 34055cb2-e80c-3942-b21c-6b840cbacac1 | -21.1405 | -49.1022 | 2025-08-13 01:00:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| eb6bbd24-ca28-3d37-836f-75e563d45d7f | -9.208 | -59.6548 | 2025-08-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 56955f9c-db69-3e24-8528-23442d393fcd | -9.0707 | -60.6457 | 2025-08-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f303878b-f113-3053-af72-04d8db44095e | -11.9938 | -45.1496 | 2025-08-13 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9f268c88-a793-3d5c-bc14-302d80d491f7 | -10.9689 | -49.5856 | 2025-08-13 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 4b440ae1-4ef9-300b-8877-7642955a80bf | -8.1058 | -55.5901 | 2025-08-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 37fa498d-9233-38ce-b224-7e7079ffa1fd | -7.1482 | -60.1366 | 2025-08-13 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 83ea6e9c-cc0e-36e3-9230-83c38cca488d | -15.0985 | -51.3396 | 2025-08-13 01:00:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| b6f981ec-875a-3ee6-9a7b-17a0ce6cf3b5 | -6.6112 | -43.8941 | 2025-08-13 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f726e2ca-b112-3728-911d-3e0ffda532bf | -7.1483 | -60.1174 | 2025-08-13 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 88be7ef0-7752-39b2-80e6-338bbbcd77bb | -10.9693 | -49.5639 | 2025-08-13 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 30f93abb-892a-3ba8-a751-3ff58d8e3892 | -15.0787 | -51.364 | 2025-08-13 01:00:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c5c8566e-979f-3251-85f0-cc63c3d3fc35 | -8.106 | -55.5701 | 2025-08-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| a162a0c9-6f70-345d-a067-eff1c9ba1ac3 | -9.1892 | -59.6752 | 2025-08-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0c7a08c7-390e-36f7-8cb1-9ab4fa99c30b | -15.0981 | -51.3612 | 2025-08-13 01:00:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 3eb3368b-ed41-376a-be8b-5093b7fcd07c | -7.2562 | -60.6302 | 2025-08-13 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e3b546b3-ae2e-367e-968d-e3930d0a5751 | -9.0521 | -60.6466 | 2025-08-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 153ed348-4025-39f1-ad2b-82fb711edfb6 | -6.9003 | -59.142899 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60003640-5629-38a0-b8d7-64078e6037cc | -12.3189 | -46.037498 | 2025-08-13 01:01:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fedeb119-b104-340f-881a-5f8bce97a5a1 | -6.871 | -59.1492 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 132f6570-8e1e-3da9-a8d3-47113b221018 | -10.2416 | -50.207699 | 2025-08-13 01:01:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d532dbb-250d-32f3-b66f-38e70ee2f42b | -10.2355 | -50.2258 | 2025-08-13 01:01:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26f80534-deff-3b0a-87d1-12ea90129a11 | -6.8685 | -59.137798 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5254d793-ccbc-32c0-bf50-6db35b6e7f8d | -10.968 | -49.5658 | 2025-08-13 01:01:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0ff1f89-4b1d-32be-a925-fbbc48c34968 | -6.9199 | -59.138699 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94ff4614-2d0f-3d99-bcfb-b3705d42a3e5 | -15.0999 | -51.3437 | 2025-08-13 01:01:00 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fbfbef1-9a7f-3caa-9409-9e434f3b9d45 | -12.5482 | -46.955601 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b34bed84-e6b2-30ce-bcd5-df6dbd2d065d | -7.1274 | -60.098701 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aaa76d49-f5a3-3050-9a71-178398bc607b | -8.5717 | -54.708 | 2025-08-13 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c82dbc27-2a3c-3045-8615-0ef295a2c791 | -7.4646 | -59.862801 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5bbbeb2-2b5a-37f7-a603-38e64a719003 | -6.8636 | -59.115101 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2088075-6a30-3552-aaa1-a310231d7d9c | -12.494 | -46.945999 | 2025-08-13 01:01:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 420193b3-4dbb-3619-acc7-40ea45334bf9 | -6.9125 | -59.104599 | 2025-08-13 01:01:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac8bafe9-6be8-3965-9aa2-22364351cd53 | -6.3054 | -51.389099 | 2025-08-13 01:01:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
