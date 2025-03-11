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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e3f0f3c-2b12-3950-9925-7738cab4d753 | -10.3614 | -47.764301 | 2025-03-11 00:16:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 104ea45c-1951-3bc0-8657-cc86a02fcb20 | -10.363 | -47.771599 | 2025-03-11 00:16:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23f0e507-6849-3ff4-b6ca-b642837b147a | -11.8218 | -46.6385 | 2025-03-11 00:16:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab145d04-332f-3834-b022-c8d4b380fd6f | -10.713 | -46.835999 | 2025-03-11 00:16:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc62f0b-4263-3b2c-8011-b1ccf6b345d9 | -20.5242 | -41.678299 | 2025-03-11 00:16:00 | METOP-B | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aee5183d-0c7e-324a-bcb9-c3e27aae6c60 | -17.485399 | -45.399399 | 2025-03-11 00:16:00 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9651043b-4974-3e3c-bbe5-2c7ee494b1b9 | -17.483801 | -45.3922 | 2025-03-11 00:16:00 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d1be9cb9-e1f0-3c87-9b8f-0464f716866e | -11.5845 | -47.624001 | 2025-03-11 00:16:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e06af2c5-1564-3792-99d3-280a95ee665f | -13.8952 | -43.7962 | 2025-03-11 00:16:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41c8d292-e394-3c53-99bd-032b8e92e892 | -6.2267 | -48.046001 | 2025-03-11 00:16:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06f8e69f-0491-3f08-9bf0-447770d6dbb0 | -13.055 | -40.3256 | 2025-03-11 00:16:00 | METOP-B | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0e824bd4-0883-3707-978f-2038d31a59f9 | -10.7145 | -46.842999 | 2025-03-11 00:16:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4005cf-93f4-399c-a13b-885361542c02 | -11.9665 | -44.657299 | 2025-03-11 00:16:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1292e0d7-d51b-3a1b-87da-8b3332486c3e | -14.1049 | -45.0923 | 2025-03-11 00:16:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8f605bb-f60f-3198-9a4a-167e1a2ba46a | -6.2252 | -48.039101 | 2025-03-11 00:16:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7e17b9-7b11-330e-b8d9-1aef6907f194 | -20.525999 | -41.686199 | 2025-03-11 00:16:00 | METOP-B | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6fd1b13-a2cb-36db-bc31-207a65af2331 | -17.527201 | -45.450699 | 2025-03-11 00:16:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb739ce-5585-33a8-b853-a0891f35152b | -10.4076 | -47.976101 | 2025-03-11 00:16:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2ea86fd-a9fa-3885-bcf4-231c204fcf79 | -11.5829 | -47.6166 | 2025-03-11 00:16:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40a2837b-e8d0-3ceb-8b24-adad1c4d9d5b | -16.4266 | -43.7691 | 2025-03-11 00:16:00 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 55df8b20-4747-3496-9a45-e2eaeac22bd2 | -10.4092 | -47.983501 | 2025-03-11 00:16:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0227a92-6431-3f02-9237-11fc14f6ab62 | -10.6589 | -44.3955 | 2025-03-11 00:16:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a7459ec-e243-34bf-bf5e-2837f42c6944 | -16.817699 | -43.949902 | 2025-03-11 00:16:00 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd8a517e-b4fa-34ec-a96b-c51055eb3db0 | -10.406 | -47.9688 | 2025-03-11 00:16:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d72f705-3e3c-3a1a-b560-789333d03b1f | -7.0177 | -35.1592 | 2025-03-11 00:20:00 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 9de7f612-1a97-30d7-922f-bce3eeb5f45a | -7.0368 | -35.1567 | 2025-03-11 00:20:00 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 124.2 |
| c5753dc8-f70d-3e28-9bdd-9c3cc42b7946 | -10.383 | -47.769402 | 2025-03-11 01:05:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03c3368f-ca69-3c85-80a5-c2daccac7869 | -20.2894 | -46.329498 | 2025-03-11 01:05:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6da01c9f-8ec7-3b21-b6c1-b58071a70626 | -15.3176 | -47.147701 | 2025-03-11 01:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb4e296-2641-3fb4-ad70-29677c9727b7 | -25.9848 | -52.591499 | 2025-03-11 01:05:00 | METOP-C | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef9cdaf7-dd20-3af8-86b4-24009c5787d0 | -10.4235 | -47.9729 | 2025-03-11 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f6a2b88-2e5f-33f4-8bdc-849e56734fc3 | -10.4268 | -47.986 | 2025-03-11 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5288a426-c152-30de-aef1-cd0d4b21c6b1 | -25.986401 | -52.599499 | 2025-03-11 01:05:00 | METOP-C | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7edee2d-e8ed-3f3c-ab89-cc4cda3243b5 | -25.96367 | -52.59585 | 2025-03-11 01:11:00 | TERRA_M-M | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8ff62f14-0b28-3e52-9e96-ddbd9b8a1803 | -25.96502 | -52.60577 | 2025-03-11 01:11:00 | TERRA_M-M | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 9aaacac7-c18b-305d-90fb-398940c4199f | -21.61712 | -48.481 | 2025-03-11 01:13:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 705a95c7-182c-3b01-bbc4-0cf600765066 | -20.26347 | -46.34644 | 2025-03-11 01:13:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| de8b807a-11cd-3e2b-b6a6-df8f58bbf6fe | -10.39772 | -47.98383 | 2025-03-11 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 947c999d-ee7f-3b5f-be5b-ca95d6c75940 | -5.07476 | -37.71637 | 2025-03-11 03:04:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6db6052d-d919-3110-8a22-9d4501b74603 | -7.2105 | -35.2132 | 2025-03-11 03:04:00 | NOAA-21 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| debd2e77-13eb-3b8d-9633-29c6cd4c8ab3 | -18.926 | -42.48179 | 2025-03-11 03:08:00 | NOAA-21 | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cac9ea2a-db32-3e04-b248-a6a6d36b273e | -10.34823 | -38.47554 | 2025-03-11 03:30:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5844d0f2-1532-3164-944f-11afeacdc907 | -7.47432 | -34.84505 | 2025-03-11 03:30:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 25f6c924-c62a-3660-96d3-1f0803e532c0 | -6.20004 | -35.43459 | 2025-03-11 03:30:00 | NPP-375D | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 862282df-35af-3d3a-9a85-cd6dde71e106 | -8.3901 | -35.02852 | 2025-03-11 03:30:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b31d28f-5494-30ca-84d7-dd3ec3a6d255 | -7.87237 | -37.20282 | 2025-03-11 03:30:00 | NPP-375D | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 521335ac-9a6e-3335-b4da-ac05b1e4a7c1 | -10.34405 | -38.47488 | 2025-03-11 03:30:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0153c71b-21ee-345d-bc55-84c1bb84ece9 | -10.69553 | -37.04833 | 2025-03-11 03:30:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c736d878-bc7e-3f04-8b48-8e70bfd1ed5c | -7.37694 | -34.88597 | 2025-03-11 03:30:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9373362a-f8e9-371a-8daa-122372b4b174 | -16.61266 | -43.33842 | 2025-03-11 03:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73a31da2-0ff4-3ff5-ab9f-62363f212c74 | -16.42045 | -43.77878 | 2025-03-11 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cd87b83-e276-3b35-9d40-ef18fc7ad518 | -13.04538 | -40.34024 | 2025-03-11 03:32:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86f65e8e-969e-39a6-ac4b-9da2a4fa9c5d | -15.56348 | -42.68242 | 2025-03-11 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 486ac5ee-6a66-3b42-aabb-0fd920c48d2a | -17.74801 | -39.58457 | 2025-03-11 03:32:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd968577-0904-33a2-bf9a-df35f96a0766 | -15.94235 | -48.11462 | 2025-03-11 03:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2bd60c8-c2f3-35f4-84e2-8b92ecf6a1ae | -14.5667 | -46.72012 | 2025-03-11 03:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce62e915-ae05-39cc-9b85-2476b72faa43 | -16.67924 | -43.88279 | 2025-03-11 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b28fcedd-5eda-3ef2-ae57-3829d0013f1f | -12.00833 | -41.38067 | 2025-03-11 03:32:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64b76538-c293-337e-839b-8128ca276775 | -13.04985 | -40.34124 | 2025-03-11 03:32:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb6ba3d6-d5ee-3097-8441-f559de4afc6c | -14.57114 | -46.72045 | 2025-03-11 03:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8619d2ea-d786-31d4-9078-7c71473d31a9 | -16.61329 | -43.33529 | 2025-03-11 03:32:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97966649-35c9-3a25-81dc-95a813876005 | -16.41514 | -43.77771 | 2025-03-11 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4832a629-4d48-35c0-91b5-fad2c954f3f3 | -15.34612 | -43.71275 | 2025-03-11 03:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6fb1088a-0ae8-3bfb-acc9-a71e9d49611b | -18.03986 | -39.92618 | 2025-03-11 03:32:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e096990-64e0-3ce5-9c70-207e4ea28896 | -11.23076 | -37.79939 | 2025-03-11 03:32:00 | NPP-375D | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 501cc46b-afac-3cc6-bbe4-5b4b64ef69d9 | -15.56845 | -42.68371 | 2025-03-11 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d99227f9-f957-3648-b451-961b74dae045 | -14.56548 | -46.72587 | 2025-03-11 03:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df78fc0d-a4eb-3b8b-860a-6540c09a4f7d | -16.67858 | -43.88594 | 2025-03-11 03:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f151f219-6042-3b7d-9cca-0e52682bcfbc | -14.56989 | -46.72617 | 2025-03-11 03:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54bbf363-0018-3d02-8f9a-da42d7aab44f | -20.26553 | -46.34119 | 2025-03-11 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 690c7d39-1474-3bf0-ad5a-0894d693e20c | -22.90693 | -43.26144 | 2025-03-11 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef4c1ebd-c432-3d33-a292-272d8d4c071f | -17.47373 | -45.40499 | 2025-03-11 03:34:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89c9480d-cd22-32c5-b498-e4c5944e33ae | -20.2675 | -46.33254 | 2025-03-11 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4902fb54-d3c5-3ec1-af63-2f7e1b832af3 | -20.26763 | -46.33516 | 2025-03-11 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c5b3f85-dd1f-3b9f-8ae9-e47b066d802a | -18.92646 | -42.48155 | 2025-03-11 03:34:00 | NPP-375D | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 81be393f-19ba-3467-92ca-1b9994c02a3e | -20.26651 | -46.33688 | 2025-03-11 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b79bf11-d79d-3b8f-9085-b815d444a378 | -20.26668 | -46.33946 | 2025-03-11 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b810547-c1b0-3666-9df4-096abb06de01 | -22.91147 | -43.26238 | 2025-03-11 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5dbb4dc3-5637-3175-a26a-d051f30f0a74 | -28.58847 | -49.44395 | 2025-03-11 03:36:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7086551-1cd1-37f7-a8e4-313bc9aaf5a4 | -28.58281 | -49.44192 | 2025-03-11 03:36:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84b8a69e-72c5-3b3d-af1c-01cbc6dce256 | -7.87589 | -37.2049 | 2025-03-11 03:51:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b3ae637-1d3d-379c-8423-c105d36dcd19 | -7.87253 | -37.20437 | 2025-03-11 03:51:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7df16260-677e-31e2-8623-bde8f8dcaf70 | -7.21341 | -35.21244 | 2025-03-11 03:51:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8c0e03bb-9a24-3f9c-b999-ba7a3fafc514 | -8.68906 | -36.99462 | 2025-03-11 03:51:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a3f8da7-7bc0-342e-9fc4-71d7bfba1e3a | -8.39127 | -35.02771 | 2025-03-11 03:51:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a2c92c22-abaf-33b0-a2b8-dea8f3d700ab | -10.34787 | -38.47297 | 2025-03-11 03:53:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 559be84b-ab80-3a89-b4a5-c4e3e865d5f1 | -10.64578 | -46.82566 | 2025-03-11 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26fb344f-fa04-3db4-9c43-afe926a2d43e | -11.23138 | -37.80036 | 2025-03-11 03:53:00 | NOAA-20 | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5fe70359-de4b-343c-b950-500da4d0ae34 | -10.32353 | -39.21479 | 2025-03-11 03:53:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 43090ad9-00bb-361c-a4d0-f46e271a1cf0 | -11.57334 | -47.62901 | 2025-03-11 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 426d8398-38da-30f8-a079-bf201ebe2344 | -13.04732 | -40.33867 | 2025-03-11 03:53:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f0373de9-e19c-3940-bb9e-e2cd53b15695 | -9.98836 | -48.09059 | 2025-03-11 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b003e00-12be-398d-8a0b-6425f6569f9c | -10.34455 | -38.47244 | 2025-03-11 03:53:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a51770c6-75d7-39fc-b54a-73e0c6eed3b0 | -10.35912 | -47.77945 | 2025-03-11 03:53:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6475144-6182-3f95-b905-1e11eba59eb2 | -10.35966 | -47.77649 | 2025-03-11 03:53:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb8bdea1-1ab9-3cde-a0f1-560460f7cc43 | -8.79911 | -38.73534 | 2025-03-11 03:53:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 126d0238-343e-3b47-874b-c3a454c204bf | -8.79966 | -38.73187 | 2025-03-11 03:53:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 946f2583-4724-3f68-ae67-6d907cd0e271 | -11.57437 | -47.62345 | 2025-03-11 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d4b3b54-eab9-342d-8974-42e8d5cb4ca0 | -12.06341 | -46.88121 | 2025-03-11 03:53:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 765b4fe9-4c3d-3bde-a379-8e19b14ec3d0 | -16.80502 | -43.96013 | 2025-03-11 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README2.md)
