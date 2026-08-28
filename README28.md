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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99034e26-295c-3d4a-a010-0e4d766ca730 | -11.01016 | -49.65421 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55354095-200e-31c3-a237-a5f23e1ed08d | -15.37754 | -39.48277 | 2026-08-28 04:17:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 794777cb-0643-3215-844e-f8d580c6dcdd | -29.52686 | -50.63924 | 2026-08-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cfe2e40a-edb4-341f-8a11-da77886693a1 | -21.54302 | -55.83675 | 2026-08-28 04:19:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4835b272-8d03-362e-8976-e6c6f563d509 | -26.58268 | -52.79657 | 2026-08-28 04:19:00 | NOAA-21 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68877949-6f90-31a2-a7de-9cf006fe39b4 | -27.29603 | -51.2635 | 2026-08-28 04:19:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8a6308a-5c59-34ae-98a3-c5f0d0b3555b | -21.89788 | -55.36931 | 2026-08-28 04:19:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f435f46f-6e6f-39e9-9e50-3ff5c6dbb0d1 | -22.30218 | -51.51033 | 2026-08-28 04:19:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c20d205e-17ff-3165-b5a7-021e732f78e2 | -16.15644 | -58.59636 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 8c35a091-203c-36a6-8f8e-c36dfe1e92db | -17.94161 | -45.95308 | 2026-08-28 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 870f254e-0e52-3ad8-9605-5177e938e2e9 | -23.13511 | -48.67608 | 2026-08-28 04:19:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 200ab027-4377-371d-aac5-f2fd6ea9de04 | -23.53903 | -47.3133 | 2026-08-28 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cad036e2-498b-36bd-a632-f87d4b9f1cca | -17.79408 | -39.7066 | 2026-08-28 04:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8b1ba6a6-76d9-3c1e-8d6c-523b4cc77edf | -14.89326 | -56.32496 | 2026-08-28 04:19:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d7da2d-4b5f-3fb7-9625-dec49863fc34 | -16.16669 | -58.58091 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| e1a690ab-886a-37b7-8e8c-ab4f251b41ca | -15.62731 | -55.97397 | 2026-08-28 04:19:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5b4857d7-346f-3948-8ac9-2b1071047d65 | -17.29757 | -46.58329 | 2026-08-28 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d536a3a-b405-3e1b-9441-8a27e4aaa541 | -28.08664 | -50.07617 | 2026-08-28 04:19:00 | NOAA-21 | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0baa66ca-949e-37ba-bb65-505f1677d5c3 | -28.66861 | -49.89854 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| bd648de4-7500-3623-8e8f-04857ef5348d | -16.15894 | -58.58493 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 571db126-f2de-3f89-a947-db4c58427a6b | -16.14941 | -58.5894 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| f9ccba96-c1d0-3f84-8ffa-31320822316c | -16.15333 | -58.60253 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 94861814-56af-35b1-9d11-6ae6de06b71c | -27.00061 | -50.58094 | 2026-08-28 04:19:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0eebe2f6-39da-38bd-bda0-e562ee11adf0 | -23.54235 | -47.3139 | 2026-08-28 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2773190a-4660-3887-b2e4-4f3d26692b79 | -21.53807 | -55.83529 | 2026-08-28 04:19:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67fea6da-32b9-3196-9b3a-f7b6ff780eca | -28.61012 | -51.25216 | 2026-08-28 04:19:00 | NOAA-21 | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6f3f7c24-891d-3b03-8447-c95057381e1e | -16.51893 | -47.7328 | 2026-08-28 04:19:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b83a11-ab55-3a12-a042-b2583a5544b0 | -23.02815 | -52.66628 | 2026-08-28 04:19:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7040cb1b-e393-3960-a009-7364449200c1 | -27.87618 | -51.36182 | 2026-08-28 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 49c4294d-4cf3-339f-ad95-10862923e9aa | -23.82118 | -48.71368 | 2026-08-28 04:19:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6149a16e-3cb7-34f4-ad14-76e2968b8e85 | -14.89234 | -56.32946 | 2026-08-28 04:19:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01613c4b-a02f-3a1f-af1a-9f74884748a6 | -28.66729 | -49.90657 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2f05b4db-43f0-32a3-9a92-aa32c29de889 | -15.629 | -55.9752 | 2026-08-28 04:19:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 11e454b1-05d2-38b1-9805-76ccce61220c | -17.7759 | -51.7256 | 2026-08-28 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ddbfd5c-7ed8-3125-9658-d3ef8ec19e72 | -23.64122 | -48.27153 | 2026-08-28 04:19:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e1c693de-88b5-37e4-bb9c-d8dbb334527f | -23.50006 | -47.64614 | 2026-08-28 04:19:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98f39268-5fdf-3528-aa1e-5a2c9f93beed | -23.92785 | -55.40084 | 2026-08-28 04:19:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3fa12cb8-8488-3942-8c23-fc4e0130cf7c | -23.13447 | -48.67996 | 2026-08-28 04:19:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c3e2144-6103-331f-a62d-360b73dc4bbd | -16.7172 | -46.40536 | 2026-08-28 04:19:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9df053d9-9584-3792-a3de-35e41bfb4663 | -16.15118 | -58.58897 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 570b7e0c-2f3a-368c-8a1c-5a11aff7841e | -18.71679 | -45.33366 | 2026-08-28 04:19:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59d89e56-369c-3c23-ada1-1492748ec8d2 | -17.58007 | -52.55559 | 2026-08-28 04:19:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de82087-10e4-39fb-a10c-1511b52d6e18 | -16.15464 | -58.59673 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 379b4d8b-43b7-36f8-98a6-ce58e98cd774 | -28.6646 | -49.90185 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6de5b6d5-a05e-3714-a6e2-4c3084f24424 | -27.87268 | -51.36102 | 2026-08-28 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 981ad191-fc88-38dd-b75a-bde1f6c4fcf0 | -23.82182 | -48.7098 | 2026-08-28 04:19:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fa8e688-72ff-32ac-91b1-d39f8fb1fb50 | -17.53705 | -42.47381 | 2026-08-28 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 659d9078-b8df-3c45-af84-21f4474c703c | -28.66328 | -49.90987 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6782f4de-bdaf-3845-a8ed-bf42e5556f7e | -23.64059 | -48.27536 | 2026-08-28 04:19:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ddbb6160-cea0-3d6d-812e-bd0eb124cb4c | -23.54982 | -51.29215 | 2026-08-28 04:19:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1f10d11a-ea50-3ee6-bb3d-f3eb2a4e561e | -17.53341 | -42.4734 | 2026-08-28 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5372982d-9ec3-3bb3-86df-0da35351a14b | -16.4233 | -49.00994 | 2026-08-28 04:19:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79be265a-3258-353a-98af-a7ef0973755c | -16.71388 | -46.40479 | 2026-08-28 04:19:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89b151b9-5193-3ce9-8ec7-40a7aa602417 | -16.1577 | -58.59059 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 1c4e9532-7797-3e53-b972-330ea24fa6fd | -28.94109 | -50.93527 | 2026-08-28 04:19:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3374686f-866a-3b78-81a0-302d9224dfb3 | -22.30314 | -51.50521 | 2026-08-28 04:19:00 | NOAA-21 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4f899a0f-76d2-322a-9add-faa315e27990 | -19.0421 | -44.99659 | 2026-08-28 04:19:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae8e665b-9ec0-3dbd-89f2-1e45b33e2f09 | -16.16499 | -58.58133 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.4 |
| 46ccdb43-4a22-3022-b59b-53c226963230 | -16.14868 | -58.6004 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 76fdc4d4-212c-3c25-8439-3c65c99ba153 | -29.0378 | -50.36522 | 2026-08-28 04:19:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 367be9e0-f20f-37e4-bb9a-7204510bfac6 | -16.14814 | -58.59502 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 8a7ccb16-52c8-3c03-9ef4-baf6fa612165 | -16.14741 | -58.60615 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 5c14e4ec-6ca6-386e-b980-3965c316e928 | -29.13303 | -50.3853 | 2026-08-28 04:19:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b79472bb-8d51-3106-af63-6053526810a7 | -16.14553 | -58.60653 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 7839d2c7-a83d-3b3c-8d0e-131d725d1c81 | -16.14684 | -58.60076 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 7c638209-5916-3bf5-9d55-439a21c92c64 | -16.15205 | -58.60821 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| d36223b5-5da8-3873-b6fc-110221930088 | -23.53844 | -47.31705 | 2026-08-28 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3231a4c2-d7f5-3679-b304-7a6697f30d7d | -29.70733 | -52.51064 | 2026-08-28 04:19:00 | NOAA-21 | VERA CRUZ | RIO GRANDE DO SUL | Brasil | 4322707 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f582411-5887-3b64-a375-61ced15a5646 | -17.79278 | -39.70438 | 2026-08-28 04:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a32b73ae-ef41-364a-a713-2c807a3fe2c9 | -16.15721 | -58.58533 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| d3fe9dea-980d-32ae-ad5c-7c4ec33f68e3 | -27.86838 | -51.36469 | 2026-08-28 04:19:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74cbb6d1-60b5-3a0c-9bf6-21a3ee991e40 | -23.02889 | -52.66238 | 2026-08-28 04:19:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f96d4621-c01f-392d-af4a-fa19e0317bfa | -23.82517 | -48.71045 | 2026-08-28 04:19:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e8016d9-fc15-3124-917b-2002267e02f4 | -28.67063 | -49.90727 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7898b218-fc58-38ee-8ecb-005d07525173 | -28.66795 | -49.90256 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6d6aaba4-d816-3539-943a-e4adca6dd592 | -16.15845 | -58.57981 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| f9f59b50-28d4-3f12-a5ab-dd26b463ac86 | -27.89663 | -51.36982 | 2026-08-28 04:19:00 | NOAA-21 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bee8c2d2-1d61-3991-b313-1e1981ca004a | -16.1642 | -58.59229 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 2d02e842-7e89-3641-9270-90cbfb9ac5c1 | -25.31719 | -51.89545 | 2026-08-28 04:19:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d157c2d4-94ce-30b0-9d85-82a5881cdd1d | -28.66662 | -49.91057 | 2026-08-28 04:19:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 597d2d49-4276-3ff8-8d81-7ccbf448819a | -16.16244 | -58.59266 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 463c7fd2-b564-34a4-9930-fc88887bfe72 | -17.7767 | -51.72139 | 2026-08-28 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81b0a34b-0fd6-3e72-a13a-d525c8f9980e | -16.15517 | -58.60216 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 5bb1c2df-fba4-3506-96f6-f1b6659b1951 | -17.53416 | -42.47564 | 2026-08-28 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df2af157-a344-3d4e-b1c5-2d5e2cedb761 | -17.5378 | -42.47607 | 2026-08-28 04:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ea63d94-21b8-3487-9bde-f9bfa6b904d7 | -23.63518 | -48.26641 | 2026-08-28 04:19:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7209e715-9486-313f-a94c-0520750f6c8f | -23.49946 | -47.64991 | 2026-08-28 04:19:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 12aa0a61-2fb4-3535-9feb-5572519a84bb | -16.16373 | -58.58691 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| ef2f2dd3-c49e-34c6-a5e7-6ff5b1915987 | -15.84598 | -56.43064 | 2026-08-28 04:19:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0938fe2e-3e3e-3e52-90ff-34802b0c0928 | -15.62649 | -55.97802 | 2026-08-28 04:19:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c41abd3d-6cbd-34cb-b0ec-e89ccdec36dd | -16.16015 | -58.57939 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 9150d98a-59b0-341c-9776-f3053761be0e | -28.42205 | -49.19337 | 2026-08-28 04:19:00 | NOAA-21 | PEDRAS GRANDES | SANTA CATARINA | Brasil | 4212403 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0b6f86a7-4b29-378b-90ad-596d407c18b0 | -25.03458 | -50.72564 | 2026-08-28 04:19:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aa6ec775-1aa8-349a-b2fd-71c8f5315b5b | -15.84504 | -56.43502 | 2026-08-28 04:19:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f2d2ba0b-9b7c-30de-b47a-65ee72ee627e | -21.53938 | -55.83507 | 2026-08-28 04:19:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6865e2a6-c432-3cf5-8d1a-a5987e3f081f | -29.11373 | -52.18543 | 2026-08-28 04:19:00 | NOAA-21 | COQUEIRO BAIXO | RIO GRANDE DO SUL | Brasil | 4305835 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a477c9ec-b82b-3baf-8b35-922a8a5b9828 | -16.15593 | -58.59098 | 2026-08-28 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 2506eb5f-d649-3237-811c-315e0e782929 | -17.79706 | -39.70496 | 2026-08-28 04:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64e0e0f7-3ffe-3b05-a9ba-1cd00b2821aa | -26.68833 | -51.45711 | 2026-08-28 04:19:00 | NOAA-21 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f722871a-afa1-34d2-a850-662cd8a919af | -27.34241 | -50.72633 | 2026-08-28 04:19:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README29.md)
