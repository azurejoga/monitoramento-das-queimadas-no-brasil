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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4b140ac-06b2-3ea5-825b-1a2f5c8e6ef7 | -11.44842 | -47.53083 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c8a7de9-fc98-3201-a022-0f1c185bca5a | -7.1739 | -59.31648 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58e91c38-c66b-38a3-8c65-5154037f78bd | -7.17751 | -59.31709 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4718a478-37e4-3652-abe0-4314a36913e0 | -9.63565 | -45.51833 | 2026-07-27 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d856035-157a-359a-a52b-4148ed2b1479 | -7.22927 | -49.59695 | 2026-07-27 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a2f30d-adf8-3a66-8347-d737785e165d | -10.06253 | -60.50087 | 2026-07-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 983f3ef9-ae76-322e-80d4-7efd9fbddc6a | -7.90379 | -48.05234 | 2026-07-27 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 755777e3-1744-3ac3-a074-61971d810f4f | -9.45671 | -51.8274 | 2026-07-27 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53a4b94e-f65f-3e70-9b04-ee9d9dd813da | -13.34461 | -51.36077 | 2026-07-27 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c81237-bb9a-3eb8-b30a-2ac6da70ec02 | -10.53189 | -48.61489 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29d77153-2ad0-3465-88d9-84a8ca769e9a | -11.47898 | -47.55265 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfd4eb42-fdc7-30f7-b416-b867cfeeb19d | -7.16961 | -59.32003 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 263e745a-622a-3796-acdd-71d04b2a91d4 | -7.17029 | -59.31587 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b027c866-3394-3acd-b4d7-4f7cf29bd607 | -11.84289 | -50.22533 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04fb10be-c774-3429-891e-2001055a7279 | -11.49013 | -47.55215 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ef3062-2d26-3aae-848f-29656f4bb348 | -12.32481 | -47.18625 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 241e9b88-d790-32c8-b449-7fa6885a41eb | -13.6924 | -51.91009 | 2026-07-27 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6467b469-a669-345a-a4c5-30b2229391fb | -9.47877 | -63.36789 | 2026-07-27 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16e56ab0-9f55-30df-b6cd-14129b3b777e | -8.82749 | -47.08833 | 2026-07-27 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf66615d-ddc3-3fde-a81e-a417c0a8ea8d | -12.32236 | -47.18291 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91933f6e-f91c-3b3a-8896-21e0494e0cba | -7.17683 | -59.32127 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 218c3d58-c23e-3d28-b9e9-4226819047d9 | -11.99013 | -45.56772 | 2026-07-27 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc62018b-dcb6-3ac0-9be7-f1f4ecff362a | -10.90622 | -56.36297 | 2026-07-27 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1956a66-5bf9-306d-9477-d08374acfe77 | -11.49623 | -47.54782 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ff77d4-2dab-3ee2-b3c4-120b4ad7c8b5 | -11.48941 | -47.55782 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14288703-03cb-334b-8e81-2c39bb3f27f1 | -13.6961 | -51.91437 | 2026-07-27 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a824461-a142-35ab-a3fc-4379c9e66889 | -7.06274 | -55.51045 | 2026-07-27 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6361cd64-5cfe-3e21-ae99-8feddf73d9cf | -10.53229 | -48.61197 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8a4cf06-31ef-3f62-809f-9e42fce6dba7 | -9.47431 | -63.36698 | 2026-07-27 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06da4da3-0f23-3f36-b575-119fa07d972d | -8.89557 | -60.59986 | 2026-07-27 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642d6460-77f0-302d-96dd-65d48b7c00bd | -10.54258 | -48.61186 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae3d3581-0461-3d7a-8127-3d230922eeee | -12.32435 | -47.19017 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a3ab89e-f5e7-3511-be50-ed259d31bc89 | -10.93482 | -43.06001 | 2026-07-27 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 06b39ef1-f2bd-3745-8335-63d410657fd7 | -11.46495 | -47.53187 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6889b7db-ea44-3fcc-8ef1-f133977f19ca | -7.16805 | -59.30692 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33014aae-0eee-3e24-a2b5-245e8d6228ce | -11.45921 | -47.53337 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb21bd0f-411b-3bed-97c1-863e2e8bd655 | -11.98586 | -45.56422 | 2026-07-27 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c5f150-a634-3742-95b9-e46cfbac3746 | -10.93643 | -43.04581 | 2026-07-27 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4beb7b72-1342-35b4-ba4d-0cd6d217dd4e | -10.53753 | -48.6115 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 73434b3c-0465-3fcd-943e-209db8a49194 | -11.48979 | -47.55485 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98e4b1ca-3576-3663-b74b-0b54cfd3cc19 | -12.3127 | -46.38702 | 2026-07-27 05:10:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb3fd4f7-7eb6-3992-ba4c-8e958fd60eb1 | -12.31918 | -47.18539 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e362c48-4604-3765-a6d3-489e081a2fad | -12.32287 | -50.37431 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2d0da53-b970-356d-b77c-dcc127226565 | -7.16668 | -59.31528 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e44655f-11c6-341f-85aa-7989fa18ab2f | -7.90419 | -48.04951 | 2026-07-27 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61c9b20f-f69f-3da3-8cba-fe6ab0f87f3f | -9.73137 | -63.42806 | 2026-07-27 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6aa5e4-5af9-3f4e-a1b7-8945c0f9aecc | -11.46222 | -47.55358 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69c0b46c-938d-38e6-972b-3b2ee4cc9eb9 | -13.69931 | -51.89066 | 2026-07-27 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 930d6d5d-7bb5-3917-8a23-fab7a504ec97 | -7.17322 | -59.32064 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0ec5a73-5682-3cd3-9f68-f99d5464ce62 | -12.31501 | -46.38827 | 2026-07-27 05:10:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 132a186f-1c93-34d9-a21e-7ee7b0e9d85a | -13.69293 | -51.90617 | 2026-07-27 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2423da4f-65a0-3d64-95b6-53e28762cf3b | -12.32528 | -47.18235 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20172d28-6a8b-399e-8eeb-eb5ef62d5854 | -11.15284 | -51.19912 | 2026-07-27 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46fe43b5-4fd6-373a-86a1-42a0e5875908 | -12.31672 | -47.1821 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0fef81e-2125-3f12-acdd-0cb8e609db05 | -8.83336 | -47.08567 | 2026-07-27 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ada42406-c74d-3cd8-9dfc-146cee1789a5 | -10.93563 | -43.0529 | 2026-07-27 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| b147da62-62d8-3695-b8b1-3e0eb5c339ce | -8.29933 | -55.11162 | 2026-07-27 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dd52f06-af23-31d1-91ed-4089afec86d0 | -8.75434 | -64.84483 | 2026-07-27 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 39d23418-a7b2-3f4b-b4b1-f66cb159a850 | -11.48473 | -47.55104 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a3ef3f3-c9d0-3985-a36f-a8dd0fed46b5 | -11.45954 | -47.5307 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aa90a9d-5f3f-3f72-86a3-d26ca92a4a72 | -8.75381 | -64.84776 | 2026-07-27 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 09cb44f7-0da9-3b55-a387-d09a9c16a591 | -10.94197 | -43.06084 | 2026-07-27 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e065071f-0066-3ef3-b8cf-c9cc1f08b5ac | -9.43747 | -64.5667 | 2026-07-27 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b420ce3f-3a59-3a27-a668-38f7c4ff7bc2 | -10.53215 | -48.61368 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| abe16933-20cd-3787-9a27-7a9874cfd2b6 | -13.70351 | -51.8912 | 2026-07-27 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d819f710-dc1b-338b-91d7-fd77a61c1db8 | -12.32187 | -47.18681 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3fbc0264-b191-359c-83b4-bbb3892bf8bb | -7.17097 | -59.3117 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 260a1239-d332-3bfc-a68e-19d802a84ad4 | -12.31871 | -47.18933 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bab9738b-f06b-3a3e-92c4-eb09c763d7c5 | -10.5364 | -48.62025 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dc2eaa82-90e8-3beb-9657-064400e2447e | -11.5024 | -50.18421 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc19df3-60b2-33d2-aaf9-077287975064 | -10.95202 | -51.0063 | 2026-07-27 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdd038b6-08ca-37b8-b413-37c73cd3a169 | -11.46266 | -47.55007 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c290833-0257-34aa-9e50-15fd1fd8a113 | -11.49587 | -50.16412 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e18bd3ea-43c1-3df3-aa7f-9c830fd48e9c | -11.98647 | -45.55917 | 2026-07-27 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c289de3-a1ce-3206-8626-a0d88e5fbe02 | -11.9907 | -45.56273 | 2026-07-27 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a130365-e2d1-3dc8-b034-3581ef86e337 | -10.53566 | -48.62603 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba76a3b-4baf-3f5c-a761-7b45568bf83a | -12.31964 | -47.18148 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd20b174-f0c3-3945-82a9-b4a411b1ff52 | -12.32138 | -47.19073 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e0eae6e-7308-3af5-919a-53b2bdc69442 | -11.46462 | -47.53448 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 570214dc-fe4a-3c8a-a665-e38d4ca4039c | -11.49588 | -47.55058 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb3f439d-75a2-35c4-b9d5-c0d2052659d3 | -11.44257 | -47.53328 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7b815b-5dea-3f07-95cb-844255cb682b | -7.89877 | -48.05172 | 2026-07-27 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0495c17-bb98-3ec3-a87a-f4f2cc77f6e0 | -10.53715 | -48.61443 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 26106577-2d8d-3283-98b4-97ee3bb6ed14 | -10.94116 | -43.06796 | 2026-07-27 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 282df48c-eb72-3e44-ab8e-84d47068fe91 | -9.4036 | -48.94404 | 2026-07-27 05:10:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 502b4cfb-eef8-3da4-9ffe-d19a779e6ee0 | -11.46811 | -47.55085 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99123698-e5a1-30cd-a500-98f34d93d16f | -12.31824 | -47.19327 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fab34316-6757-3a1b-9956-7a4725dd2696 | -10.09797 | -59.14771 | 2026-07-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be13354c-2559-3159-87c3-a58d03df9567 | -10.90953 | -56.36349 | 2026-07-27 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c9ea0e4-f0a0-31e1-8add-e78e50a06977 | -10.53177 | -48.6166 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47f53663-1e91-380f-a2d8-b3d917378c20 | -10.53791 | -48.60852 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a0f328d-ad62-3350-a6c1-12e63ce9eb05 | -12.32204 | -50.3768 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89e85f36-0865-3208-91f4-8645fd20c331 | -10.05883 | -60.50022 | 2026-07-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88b80f1a-c9dc-34c4-859d-cc4f1898e320 | -8.82794 | -47.08488 | 2026-07-27 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c69122d-6e97-3c84-9af7-faa34f52f023 | -11.49652 | -50.1594 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a44522f6-a693-3c27-9480-a76686e8501c | -9.77131 | -63.37317 | 2026-07-27 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a82ed629-1a40-35d2-bc72-454b06e85bf9 | -11.88996 | -43.83261 | 2026-07-27 05:10:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e36d13a6-85ad-3ea1-8425-3c67124c0a70 | -10.53149 | -48.61782 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebf4f9c2-8fa8-3ec9-87fd-fddf86d4ee17 | -10.53678 | -48.61734 | 2026-07-27 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41b7bd55-e2f2-329d-a95c-d35255864dda | -12.31623 | -47.18601 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README8.md)
