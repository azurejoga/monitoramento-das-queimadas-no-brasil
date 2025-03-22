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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af4e7942-6a48-3fd7-8de5-3abab798ed65 | -21.94453 | -50.51615 | 2025-03-22 03:49:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 093cd595-989c-3eed-8bf4-c13df453ca93 | -21.94913 | -50.51433 | 2025-03-22 03:49:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f0992bbc-ee78-3895-90ef-53f42ddc7743 | -20.14372 | -50.72507 | 2025-03-22 03:49:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f3e077ac-6b1f-36c0-b1e6-541de8047ad2 | -20.23184 | -46.60058 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eedf66e5-bbef-39f4-97c6-67e85764293e | -21.20142 | -47.01083 | 2025-03-22 03:49:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce03335-3e44-34c4-8766-590fc903fd79 | -21.17732 | -53.0803 | 2025-03-22 03:49:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10c0f434-472c-3812-b67c-0d7c7068e1da | -20.22442 | -46.6622 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 193610a6-41b5-3224-bcf6-993eb79009b1 | -20.13683 | -50.72069 | 2025-03-22 03:49:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| dda7591c-a100-3141-90a5-41774641e04b | -20.14155 | -50.72622 | 2025-03-22 03:49:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| aa3ddcb6-720c-324e-ace8-b31a96a227c2 | -20.225 | -46.68275 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38aa2403-b644-3fef-81d2-d2ce373227f4 | -20.78234 | -49.84877 | 2025-03-22 03:49:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ee6152cc-e9d3-327b-9af9-af2b47680bf6 | -20.22252 | -46.67197 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd0c3d19-2987-3ee3-9f05-837bdaafb629 | -20.14331 | -50.7182 | 2025-03-22 03:49:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 21421866-8128-3362-a258-979bd3c3fd18 | -20.77903 | -49.84819 | 2025-03-22 03:49:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a47ce05b-4541-3903-b853-2875877f7e0d | -20.77828 | -49.8517 | 2025-03-22 03:49:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f7d5aecc-c59a-37e9-b964-f556fc45b28d | -20.22066 | -46.68153 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c37e2a4b-a599-33f7-ac5f-102c202ae7c7 | -19.83088 | -40.11159 | 2025-03-22 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9420f3b2-87fd-35a4-9a7f-4d65d31246b3 | -20.22397 | -46.61764 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71d8ddcf-99d6-3a69-9e15-65194d98d11e | -20.99402 | -51.79641 | 2025-03-22 03:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ea1bc06f-3afd-3e94-a957-b756158f7121 | -21.94536 | -50.51246 | 2025-03-22 03:49:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 696013af-f08d-382a-9637-025d32a8eefa | -20.22589 | -46.67815 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f8764c0-4071-3982-90a5-6701c2fb746d | -20.14463 | -50.72108 | 2025-03-22 03:49:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9d92c731-1fba-35a0-a4a6-9451acb3c7f8 | -21.94902 | -47.42038 | 2025-03-22 03:49:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 62568651-aad4-3eb4-b5e4-c40bd5728e6f | -20.1377 | -50.71674 | 2025-03-22 03:49:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b016f218-3f2b-3f25-bebc-9f9095685c61 | -20.14244 | -50.72219 | 2025-03-22 03:49:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1c9bdb27-100b-3316-895d-afa8ad81b5ce | -20.2231 | -46.62212 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9015d312-c554-3873-af64-9fbef518af00 | -20.99182 | -51.79383 | 2025-03-22 03:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c0bb9f45-61bd-3f7b-8afd-c14c1a9f998f | -21.94832 | -50.51804 | 2025-03-22 03:49:00 | NOAA-20 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 22c3836e-f67d-3a10-95b0-04bb7c3e365b | -21.17595 | -53.08598 | 2025-03-22 03:49:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48fe73a3-6c0a-3b1b-8547-58669fd16e45 | -20.76266 | -46.76885 | 2025-03-22 03:49:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34276ff4-1b11-39cd-8c57-0244ac017d4f | -20.22158 | -46.67684 | 2025-03-22 03:49:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b00cc733-3fcb-318e-85e0-430dad0e9a1f | -20.77712 | -49.84726 | 2025-03-22 03:49:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 614b74b8-c4f5-3e78-becc-045e8be05045 | -20.77634 | -49.85077 | 2025-03-22 03:49:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 55a7b6b0-2444-3c02-bfca-b116da4f2972 | -28.93368 | -51.40091 | 2025-03-22 03:51:00 | NOAA-20 | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 403f44ac-674a-3dd3-a73e-cbccdc3b78a1 | -23.98384 | -48.92065 | 2025-03-22 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a63fbfc-23a0-308f-a636-d49fab686b9e | -29.07868 | -49.60985 | 2025-03-22 03:51:00 | NOAA-20 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 71150337-f8be-3cfd-a4b5-9ca2e7a5e4b4 | -29.52272 | -50.67751 | 2025-03-22 03:51:00 | NOAA-20 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f5a61b4b-e9f2-3ccf-9d9d-419e32c6073c | -23.59349 | -47.44001 | 2025-03-22 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 850265ef-fc58-3181-8ed2-f78aa01782a9 | -28.62315 | -50.16006 | 2025-03-22 03:51:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0d6f29b-eec1-35d7-9c5b-66a94a18c1ff | -28.62774 | -50.16122 | 2025-03-22 03:51:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 26d98345-d229-3b74-8901-559e4a2e5c25 | -29.07975 | -49.60495 | 2025-03-22 03:51:00 | NOAA-20 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6431897c-c50a-37da-a448-57c2d2274a93 | -23.76532 | -47.44285 | 2025-03-22 03:51:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2f6a26ac-67ea-3880-a06a-161bbfbeb10e | -26.52553 | -52.91501 | 2025-03-22 03:51:00 | NOAA-20 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e4a753fc-ea1b-3c1a-9898-664ac2c1806c | -23.27196 | -51.20847 | 2025-03-22 03:51:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 25c191bf-0eef-3248-87e0-a1cf30ee531e | -26.52427 | -52.91087 | 2025-03-22 03:51:00 | NOAA-20 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4a4c20b-8958-34fd-8ccc-a376dd0b0b5e | -27.73483 | -50.42269 | 2025-03-22 03:51:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 92aa48a6-d7a9-3a8b-9582-6c413f1097f6 | -29.51814 | -50.67602 | 2025-03-22 03:51:00 | NOAA-20 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 92d00f86-996b-380b-91be-dbf9449e5f0e | -22.72661 | -55.58157 | 2025-03-22 03:51:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d46fa392-0df4-346a-854c-8a1ebc00df30 | -25.19707 | -49.3247 | 2025-03-22 03:51:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b1405baf-cbc1-3704-832a-f8ace51b9863 | -26.52312 | -52.91571 | 2025-03-22 03:51:00 | NOAA-20 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1f79b8d8-12ce-3cac-995a-825de81afd57 | -28.93858 | -51.40221 | 2025-03-22 03:51:00 | NOAA-20 | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8c342c11-f279-38db-8dda-1495d96fed6c | -23.98496 | -48.91534 | 2025-03-22 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c50cf34-2209-3dd1-9949-3b7d9802848b | -26.52668 | -52.91035 | 2025-03-22 03:51:00 | NOAA-20 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4678e6fb-75bb-30a0-b16c-cf0e349d7c23 | -25.19125 | -49.32881 | 2025-03-22 03:51:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6347d530-3fe7-3716-9d32-88e5a659fa89 | -28.86872 | -50.87328 | 2025-03-22 03:51:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92ad338a-5f24-36d5-9c0d-8cdaec4fff9e | -27.73605 | -50.41717 | 2025-03-22 03:51:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0d298d42-cbac-33a1-8b34-d1a70d1fc75c | -5.1218 | -56.1163 | 2025-03-22 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1c981f7-3f27-35be-a5ed-798ac5d0f288 | -12.3676 | -41.43356 | 2025-03-22 04:40:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ccf5f568-9aa5-3d13-960d-b5117ad8eca6 | -12.93955 | -55.94632 | 2025-03-22 04:40:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7859f426-66f9-3c18-9531-20994b593a2f | -12.35817 | -41.4211 | 2025-03-22 04:40:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2103dd9e-fcbe-36ea-b8d6-05afff7c3cd0 | -13.25516 | -41.33196 | 2025-03-22 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 068545d6-e9a4-38ee-8ae6-f187eea77040 | -12.38068 | -54.94566 | 2025-03-22 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3df154df-0f86-3d01-a918-32860f2759a2 | -13.93952 | -50.58188 | 2025-03-22 04:40:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 972f5bc8-4a7d-3656-9a97-3266be225124 | -13.94007 | -50.57832 | 2025-03-22 04:40:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bf4a6ae-9d7e-3fcb-8faf-4abe898e524c | -9.92394 | -59.93658 | 2025-03-22 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f608caaa-ccfd-3e51-b473-20564f2cd747 | -12.94353 | -55.94704 | 2025-03-22 04:40:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d19c2e35-c936-31a9-9a94-06af85b6faba | -12.36724 | -41.43649 | 2025-03-22 04:40:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89535722-9017-3b32-b17a-c8218a4789bc | -12.94414 | -55.94354 | 2025-03-22 04:40:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1bf83b9-4793-3f1b-9df2-74962fbe8222 | -12.38103 | -54.94317 | 2025-03-22 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 26ac1c69-e298-3099-bef9-486d538ec52e | -12.37303 | -41.43387 | 2025-03-22 04:40:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0e7f0c11-0cd0-3a4e-a4fc-c7679c003738 | -12.94016 | -55.94281 | 2025-03-22 04:40:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2b667c8-2de9-33bb-9f9b-d3e7015400ab | -12.36351 | -41.42219 | 2025-03-22 04:40:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e40c90c9-813e-32f9-9791-ab4230de4a15 | -10.35529 | -44.84267 | 2025-03-22 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e53b6dd1-3e1c-3b16-9ec5-1fe1e5c0ba95 | -13.25561 | -41.32822 | 2025-03-22 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 576be75f-b57a-32a5-91e4-4996b7d79b79 | -12.37269 | -41.43666 | 2025-03-22 04:40:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 05a7e3f2-2e37-3d62-ac0f-1bdc689d60f3 | -9.92327 | -59.94017 | 2025-03-22 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10f05531-673d-3aa3-95e4-518e7f59ed46 | -20.25598 | -49.67593 | 2025-03-22 04:42:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4965abe4-b7ba-3dbd-b32a-98ee5f068d91 | -20.12044 | -51.20153 | 2025-03-22 04:42:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4823f4e3-61cc-3271-8623-21b7fb8c300d | -20.14491 | -50.72288 | 2025-03-22 04:42:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 636be1ce-9b0b-3587-a2dc-098edf7a0ecf | -21.19633 | -44.93647 | 2025-03-22 04:42:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6f579d0-977d-3ef0-a65d-1cb0290f1d6d | -21.19633 | -44.93647 | 2025-03-22 04:42:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d07b44a-2cc9-3530-97d8-3f74b892f6ef | -19.4399 | -54.78787 | 2025-03-22 04:42:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6c5ae5f-8765-370e-afec-65e8b225946e | -16.49416 | -57.78085 | 2025-03-22 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aae98019-9ebe-365e-95e8-9695c4c77f72 | -20.14205 | -50.71838 | 2025-03-22 04:42:00 | NOAA-21 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3fa3e4db-aa7f-3850-8a9e-e115a35af78b | -19.43714 | -54.78318 | 2025-03-22 04:42:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d362878-1fae-3363-b282-2f4beeac75e0 | -19.94468 | -49.23187 | 2025-03-22 04:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 843d10bf-4f21-33b8-93ef-3c71eebe1751 | -16.30701 | -53.8397 | 2025-03-22 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2be8aed-9da1-38f7-8ab2-75e3f1cd8368 | -20.14149 | -50.72233 | 2025-03-22 04:42:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7e652517-fca2-32d1-b11a-b7cb3eb47122 | -15.59958 | -57.33387 | 2025-03-22 04:42:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ea1522a-9b84-35cb-bee0-801e683f5900 | -20.14548 | -50.71894 | 2025-03-22 04:42:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e9229439-7b24-38b9-b060-923c39e37994 | -20.23652 | -46.60073 | 2025-03-22 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 691881b5-37e9-34ff-aec9-d31607c426b3 | -19.44058 | -54.78385 | 2025-03-22 04:42:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44f50bc1-e173-3324-af84-4958e350a9c7 | -20.23278 | -46.59604 | 2025-03-22 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9095090-eec7-3bdf-a76f-d21700147d9c | -21.97041 | -57.59359 | 2025-03-22 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afe53a13-4963-3ca4-ab35-1b4539b96f99 | -21.94701 | -50.51426 | 2025-03-22 04:44:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f43f339a-0d57-37e3-9541-6c6e9a7c61bc | -21.89356 | -53.4672 | 2025-03-22 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1889eaa8-780e-3d62-a41d-a2187886b043 | -22.72663 | -55.57627 | 2025-03-22 04:44:00 | NOAA-21 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| de4bf9d7-8c52-3c3d-a798-8e2b99678970 | -21.20156 | -47.00945 | 2025-03-22 04:44:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 945b2e36-f9be-34a5-aad2-2856a1780a71 | -25.93544 | -53.17151 | 2025-03-22 04:44:00 | NOAA-21 | ENÉAS MARQUES | PARANÁ | Brasil | 4107405 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7133e32e-20a0-3fc7-ac4f-1acd76bf6333 | -23.59498 | -47.43839 | 2025-03-22 04:44:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
