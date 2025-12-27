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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80b715f2-2403-3d98-9015-4d05b7996124 | -0.1012 | -51.2738 | 2025-12-27 03:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a01b7489-87ad-3188-bf94-34ea55b74c1b | -15.8955 | -43.4523 | 2025-12-27 03:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 38a4f376-4b6e-34b0-8d72-c92f7782728e | -0.1012 | -51.2738 | 2025-12-27 03:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 89c62d54-bdea-347a-9563-84cfb0e699a6 | -0.0828 | -51.2738 | 2025-12-27 03:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0eb71a3c-4276-3a62-bf7e-f605c62ec587 | -3.313 | -47.37477 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a6c84840-89ff-3a23-9ede-b5ecc20c2d34 | -6.09044 | -37.39714 | 2025-12-27 03:46:00 | NOAA-21 | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b8986a9d-fc19-383b-a621-f86081d10b41 | -3.90069 | -42.55616 | 2025-12-27 03:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 4d8d58a1-1fbc-3059-ad1b-785be21d2df5 | -4.89794 | -40.44352 | 2025-12-27 03:46:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c891f1a-7857-37e4-a9bf-bd26a7f5bc9e | -3.63039 | -42.20999 | 2025-12-27 03:46:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13a3fe81-5953-389e-a2b8-d3008d7a91c8 | -5.82143 | -39.08315 | 2025-12-27 03:46:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61c39816-a21a-38d8-a583-c0b10410fb6d | -4.65765 | -38.78487 | 2025-12-27 03:46:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77e7b80d-a7d9-39b2-9e01-ce109333fdb0 | -3.75976 | -43.56104 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcc4e42d-3b21-3700-8e8d-10117627e295 | -3.30724 | -47.37617 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd08821f-6fd6-393c-a199-a11e7bd526e3 | -4.89695 | -40.44464 | 2025-12-27 03:46:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ee93ef8b-ed69-32a3-ac93-d711fd33c725 | -6.4812 | -35.38792 | 2025-12-27 03:46:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e790096-b536-3772-9139-deba3966879f | -2.4576 | -47.78457 | 2025-12-27 03:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4fddda31-04dd-3de0-a83c-f2adb2947817 | -4.58596 | -37.80713 | 2025-12-27 03:46:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0672ae32-f8ae-33c0-959a-94b26ef91e5d | -3.65346 | -43.52029 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46e77cc5-2845-3f57-9822-4c20e8faeb90 | -3.31762 | -47.38471 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f8db4eaa-c478-3eb1-aba6-d9845950f1a6 | -4.10319 | -38.25639 | 2025-12-27 03:46:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d2148a1e-aca7-36e2-9704-eeba9cc0d369 | -3.31909 | -47.37581 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 713caa3a-93eb-388e-8c6e-6c376843e629 | -3.73399 | -44.54033 | 2025-12-27 03:46:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f91501-3169-3322-ad10-fe9a080b5ef7 | -5.49621 | -39.16357 | 2025-12-27 03:46:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 128bf8f1-3fa1-3768-b30f-c7d59d0c7b65 | -3.97323 | -43.40971 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 005d36fd-c9ad-3bd2-a44d-671d6800110d | -3.5574 | -39.10794 | 2025-12-27 03:46:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee05841a-819d-3f26-8e96-346635105661 | -3.51053 | -40.84142 | 2025-12-27 03:46:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f02caf8f-9bbd-3617-aa17-44ea858cbace | -5.34778 | -37.03724 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d425c0e-ad2c-3a6b-89c2-c5861cb9b987 | -5.61858 | -39.52983 | 2025-12-27 03:46:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ceca903-80e5-3881-a34c-98197fb76a86 | -3.31409 | -47.37283 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ebed331f-3a2d-3411-af8e-36e7b459b7b5 | -3.97465 | -43.40747 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6404aa4-6eff-3b0c-8fe6-abec01dcfea1 | -5.40501 | -35.31523 | 2025-12-27 03:46:00 | NOAA-21 | MAXARANGUAPE | RIO GRANDE DO NORTE | Brasil | 2407500 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 65d6dac0-f234-3969-a4bd-a5ecf9b3b54d | -3.31153 | -47.38361 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e95a3409-1fee-3261-8e76-e250a32241ce | -3.56045 | -43.57419 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e16a0d6e-0357-388f-81a6-75f9e4b7aeb0 | -5.18558 | -40.11252 | 2025-12-27 03:46:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7adba632-8fb1-3565-a55c-f898cfc71647 | -4.44532 | -38.92965 | 2025-12-27 03:46:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e481d6e8-f533-35b9-ab69-a168b71a3424 | -3.32586 | -45.99829 | 2025-12-27 03:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e624c963-2ed5-37e6-93c6-d4f7062f916c | -5.61568 | -39.52526 | 2025-12-27 03:46:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7665e01b-4abc-327c-bdfe-2338d666a218 | -3.76527 | -43.55692 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8960c137-8658-3153-8b0d-d1be08761194 | -4.67799 | -38.06515 | 2025-12-27 03:46:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6e3888ce-5dce-398c-85c3-e2e9d2feac18 | -5.15625 | -37.36646 | 2025-12-27 03:46:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ec45f12-3cbf-3b4d-b4a1-5219ef0134cb | -5.43017 | -36.70728 | 2025-12-27 03:46:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 344867ab-435a-3c02-857c-82fd46ccbd25 | -3.76995 | -43.55778 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ce0f6093-b73c-3c4f-9237-b45ab5c13eb6 | -3.32438 | -45.99955 | 2025-12-27 03:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d23afbd0-a7a6-38c3-b718-a237917088f1 | -3.32501 | -45.99591 | 2025-12-27 03:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88649b45-15f2-33c7-8d38-b01c80567526 | -5.34891 | -37.05158 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a223c747-9038-351b-b200-e6be9bc9cff3 | -5.50071 | -40.69872 | 2025-12-27 03:46:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 79ad393d-fedb-3aaa-a3f0-b4cce0b11cfd | -3.75891 | -43.56606 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84a1c2c5-f112-3631-a69d-bce92c84ab86 | -3.31256 | -47.38168 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 57f028ef-f750-3d92-b943-a5eb0ea1593e | -4.91983 | -40.66455 | 2025-12-27 03:46:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc6dc302-6f9a-3d67-9e55-428109805362 | -5.50043 | -40.70004 | 2025-12-27 03:46:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97ee8d2d-ecad-3960-9edc-77b6739dec71 | -3.31835 | -47.38031 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c111a538-0047-34f4-a4d4-3a2f6eb4dfa5 | -2.45849 | -47.77924 | 2025-12-27 03:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 09fe601c-3fac-31ca-b6ef-cf2a4b9d7a60 | -5.34174 | -37.05401 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 736718ee-19cb-3754-b638-03890dbe5ea8 | -4.44008 | -38.06102 | 2025-12-27 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb1a93b2-d6d0-3fb9-af4f-8d1166d3be6d | -3.89991 | -42.5563 | 2025-12-27 03:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 933e10fa-9287-340a-b3d5-afe680813371 | -5.0094 | -39.71436 | 2025-12-27 03:46:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa6da0b2-2d16-31c2-bf75-5ee865d52b09 | -5.34284 | -37.04709 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6ff81530-de3b-3177-9bc0-420b8b9bf766 | -3.6598 | -43.51114 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a42ae11-6267-3eac-a5f0-a8cfd57bd61a | -4.67034 | -42.40134 | 2025-12-27 03:46:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ed1171d-10cd-30ba-a6cf-ff0f76692a53 | -5.0448 | -42.36544 | 2025-12-27 03:46:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd890fe8-3be8-3ce5-9cfb-51020d59e031 | -3.31864 | -47.38277 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9075642e-d04b-3c1d-96a2-59034f628294 | -3.3194 | -47.37835 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4712b61e-503e-3c83-acfd-e3db65bb92d3 | -5.40556 | -35.31165 | 2025-12-27 03:46:00 | NOAA-21 | MAXARANGUAPE | RIO GRANDE DO NORTE | Brasil | 2407500 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 83606c4b-01c2-36c3-b16e-29f14e30637e | -3.65429 | -43.5153 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9dd9075f-dba3-3768-8d3b-3316d6fed102 | -3.90506 | -42.55687 | 2025-12-27 03:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 1b033567-a3fa-344d-8622-16cfa030e7d4 | -2.67911 | -42.7449 | 2025-12-27 03:46:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af014fef-b212-353b-a54c-29e487c9701f | -6.12524 | -37.69234 | 2025-12-27 03:46:00 | NOAA-21 | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3865872a-d36f-3ec6-8b6c-a4ac258ef431 | -5.34669 | -37.04415 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b55aef37-b0fd-336e-95eb-66a5ff102799 | -6.08594 | -37.31816 | 2025-12-27 03:46:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f425610f-cdfd-301f-af8f-9290268f652f | -4.89718 | -40.44806 | 2025-12-27 03:46:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01e13843-3020-3721-9278-6fac8dc995e7 | -3.55319 | -39.11143 | 2025-12-27 03:46:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 024d15ee-b91a-3679-94a1-2876bc64e31f | -6.48065 | -35.39152 | 2025-12-27 03:46:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2e154c7-007c-36f9-963d-f48cd84897a9 | -3.31227 | -47.3792 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f4e0a2b3-41d8-3c16-8d36-4fe28475c3ee | -4.67741 | -38.06877 | 2025-12-27 03:46:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0df684cc-aedc-3ef5-b8b8-aa42094c6038 | -5.01577 | -41.83897 | 2025-12-27 03:46:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49697732-1ba9-3209-92aa-4e06898f1dd1 | -3.31332 | -47.37727 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5151959f-78a6-3ce8-a4d8-0d8366607310 | -3.31179 | -47.38609 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09a71a53-8526-3151-8550-f87bca50b73e | -3.90429 | -42.55701 | 2025-12-27 03:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 122e4e2b-9d40-3023-a15e-7f226c4ee208 | -3.65597 | -43.50531 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 042c1d89-5699-3cf3-9696-3aa79733ac9f | -5.08144 | -37.6457 | 2025-12-27 03:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f9337b5-1ea9-3e0d-95af-548f8d8ae93e | -3.30618 | -47.37815 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38f8644e-6c1c-3097-a772-fde4935058aa | -5.34065 | -37.06092 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d0dd15e2-681c-3c7d-acb9-58048ff57247 | -3.31788 | -47.38716 | 2025-12-27 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c994dbf-0d4a-3f3e-a8cb-38b17f830564 | -3.32646 | -45.99463 | 2025-12-27 03:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26fe63fc-00c9-3ef4-8a72-c96e21155afe | -2.88748 | -40.51191 | 2025-12-27 03:46:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9ee6db84-b26f-36a6-89c4-a026f72738d1 | -3.76444 | -43.56186 | 2025-12-27 03:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1903de91-5bd6-3b61-ad1b-4785b7da03d9 | -5.0058 | -39.71376 | 2025-12-27 03:46:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 02cc6c0d-b952-3b1d-b261-e76d14195140 | -5.3412 | -37.05747 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0c5fcdd-7d33-3981-acbd-cfbb333f733b | -5.34724 | -37.04069 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7286bec9-07a6-3ddf-9bef-350b7d980a18 | -2.87206 | -40.41042 | 2025-12-27 03:46:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13c8c885-9fb7-3c40-9b2d-c50fe9677a25 | -4.50895 | -37.78046 | 2025-12-27 03:46:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ab5918c1-8ff8-3840-8cac-a3d9ded95dd2 | -5.35055 | -37.04121 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce4a1942-68b5-3436-8271-c08257cc34b8 | -6.47728 | -35.391 | 2025-12-27 03:46:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 71f0dabb-dc2c-3a70-999d-8c48b700aef1 | -5.49558 | -39.16746 | 2025-12-27 03:46:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 37736653-8ef1-3943-a257-e69f24111656 | -5.33789 | -37.05695 | 2025-12-27 03:46:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b7e34e0-259a-3745-91e8-d3682220b8fd | -12.29587 | -44.35199 | 2025-12-27 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fef71dba-0a3f-3360-8142-ceb07d7037c9 | -11.85403 | -43.73667 | 2025-12-27 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e775e2ba-f4dc-3c81-9eec-2f4fdbf8a49d | -6.25885 | -38.26281 | 2025-12-27 03:49:00 | NOAA-21 | RIACHO DE SANTANA | RIO GRANDE DO NORTE | Brasil | 2410801 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d20bbf3-1599-382e-9060-d7a3315a8d18 | -7.63403 | -34.81896 | 2025-12-27 03:49:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dc574d6b-b7b8-3300-9ec5-23fc040d3715 | -5.45381 | -46.17987 | 2025-12-27 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
