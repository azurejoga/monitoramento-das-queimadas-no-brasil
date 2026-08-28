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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 977307d4-68fe-38d7-b691-328647cee530 | -25.20904 | -50.70065 | 2026-08-28 17:41:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 5098af24-5993-388c-b4e5-fecd2c08290a | -25.03601 | -51.20245 | 2026-08-28 17:41:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| f073b94b-ffb8-3f60-8f85-f2a7399557b2 | -27.32729 | -52.43347 | 2026-08-28 17:41:00 | NOAA-20 | BARRA DO RIO AZUL | RIO GRANDE DO SUL | Brasil | 4301925 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| cdf54caa-557c-3efa-ac0e-bc729a0bc92b | -27.11876 | -51.00653 | 2026-08-28 17:41:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 037c6feb-864b-32a6-8923-350e4f2fd10c | -27.33054 | -52.43353 | 2026-08-28 17:41:00 | NOAA-20 | BARRA DO RIO AZUL | RIO GRANDE DO SUL | Brasil | 4301925 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c741762f-b55b-34b0-8899-3daeaae57a6d | -25.20726 | -50.6975 | 2026-08-28 17:41:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0a67d505-c884-3f15-8b95-24f1ca0e0e18 | -25.09258 | -52.74643 | 2026-08-28 17:41:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| eb6fbaf4-d4c2-30d2-ba11-61ba2b943919 | -20.69627 | -50.48054 | 2026-08-28 17:43:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| e7a2e0c0-695c-3cb7-a970-9ce3dbfc20c1 | -18.1179 | -51.61407 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a25b4e90-35af-39ea-ac57-db11435d03b4 | -19.22636 | -57.65736 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| c9db69f7-a092-3cab-bef2-ff47b0ba3202 | -20.54985 | -57.24352 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8806458b-886e-35ae-bf0f-bd8d3826462d | -18.11586 | -51.60424 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 08e6d100-ac3f-3911-b800-9f0ffa834378 | -15.73441 | -51.18255 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39b59569-b97d-345d-99de-bd5d0b16f195 | -16.84585 | -49.24445 | 2026-08-28 17:43:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1d0032f-cba3-318c-985a-af11a8df71b5 | -15.35854 | -52.8273 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d51f42d1-2616-3787-8945-05907c0edb73 | -22.08869 | -55.97373 | 2026-08-28 17:43:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| effbc8ee-c38c-328a-83a3-dd59f84b6267 | -15.72818 | -51.18002 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 33f1e09e-ea33-3b8a-84b9-175825676d1f | -17.28047 | -46.02345 | 2026-08-28 17:43:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| de44490c-0b2b-34f3-a535-819a30430ceb | -19.22564 | -57.65312 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 3b800497-6627-3968-855b-5a20552bf88c | -22.17586 | -50.38705 | 2026-08-28 17:43:00 | NOAA-20 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8cfbc2a7-14b3-3ecf-851f-072099534577 | -15.36003 | -53.79191 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| bf0269b7-2e38-3e06-a96d-8349369eb1ff | -17.55595 | -51.11232 | 2026-08-28 17:43:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 832a4834-0957-339e-a157-630640a67772 | -15.73026 | -50.72862 | 2026-08-28 17:43:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6342483f-2178-3521-b506-c5318d3dcdfc | -19.22434 | -57.66695 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dbe356fe-0b04-3a6b-95ca-16e5e753af65 | -20.69698 | -50.48392 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| 70fc5182-ed6d-32f6-9a0a-ca2fcedc220c | -20.93912 | -57.61868 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 895423be-ab77-3e2e-a54e-de95f1122930 | -15.37611 | -52.67582 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7b1ce543-59f9-38b2-877e-8e29b394d7b5 | -16.57029 | -49.3857 | 2026-08-28 17:43:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f7a9196-bc1d-36c4-8802-5fb2e8bebd92 | -15.37729 | -52.68197 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2ec8a2de-43bb-3928-8dd3-7a3bc0bee35e | -18.1217 | -51.60664 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 286811df-7120-3eb3-8687-533bf265b849 | -20.69186 | -50.487 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| cd50f548-f46a-3bf9-bdcb-409e33302a05 | -16.17118 | -58.58419 | 2026-08-28 17:43:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d8340d1f-1796-392f-aa91-0939a0e39732 | -14.33747 | -47.23605 | 2026-08-28 17:43:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 81f7e66d-a50e-3374-b836-a46f32efc98b | -19.06433 | -57.40428 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 410bed8a-68fb-3622-89aa-a314728a2d3f | -21.04474 | -57.83547 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 645231c9-efdc-3059-a354-1f4e0e867067 | -15.35471 | -52.8342 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecd0d893-e6f1-3342-af04-fb8b0ece305b | -20.32292 | -46.58385 | 2026-08-28 17:43:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 08a391fc-fe5e-3fc1-8627-ef8128a68887 | -17.56197 | -51.11444 | 2026-08-28 17:43:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4f7cb740-dace-37f0-bb14-68e4693d0941 | -17.98345 | -50.18235 | 2026-08-28 17:43:00 | NOAA-20 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e348944-efb8-3ccf-be3b-28f5c4841454 | -17.55883 | -51.11329 | 2026-08-28 17:43:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3b277978-8650-3769-bf89-910f1fd8343f | -18.7956 | -50.91932 | 2026-08-28 17:43:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 235b5413-c0df-3594-bfaf-1531c0ac83e0 | -21.04197 | -57.84009 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 7982ee24-c810-323f-962c-5fa64941d359 | -16.58434 | -49.78112 | 2026-08-28 17:43:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6f860b1c-3522-3b68-8a90-c72bd5b3266b | -20.47049 | -48.78569 | 2026-08-28 17:43:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| adfc175e-b4c3-316c-a352-757cccd316e4 | -20.54704 | -57.24842 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f703d947-dd3a-347f-9993-07274e66cb69 | -15.34974 | -52.83528 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d5d4741-387f-3b06-bd43-bbcc7c456d23 | -20.68664 | -50.48672 | 2026-08-28 17:43:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| a57b335d-3cbb-3b33-8968-2e193927d201 | -17.27841 | -46.01488 | 2026-08-28 17:43:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bc27d991-bf37-351c-bfdf-802fc646b3bb | -18.35798 | -54.99068 | 2026-08-28 17:43:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| e350a6d8-e9c4-350b-b1d4-8cc0c44e704b | -18.84113 | -47.39935 | 2026-08-28 17:43:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12a57921-324e-3839-a357-477806317f5d | -21.03853 | -57.84073 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| f49c876b-c040-3a05-bb26-6e0389e9a152 | -20.62897 | -52.65226 | 2026-08-28 17:43:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 58d7cfa4-659c-369d-aa19-863234a7ea08 | -16.79144 | -50.02018 | 2026-08-28 17:43:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b880070-34e6-3a3e-8e15-ddce34670f46 | -15.38495 | -52.6729 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ee4e1fc0-18de-37eb-9e33-d9f4bf94df03 | -15.36233 | -53.7929 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 46c78c97-2a59-37dd-a634-6db2506ce086 | -15.13217 | -52.83358 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f8b52d72-5d1c-387a-a205-8dd2999e3528 | -15.37663 | -52.68359 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d7e18677-ed67-3090-96b0-77e159397f1c | -16.94037 | -47.20371 | 2026-08-28 17:43:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 762376e0-fec5-3a07-b67b-6aa5f3826b50 | -15.72875 | -51.18396 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 871c832c-b2a8-3798-b138-0faeb6869d5e | -15.38372 | -53.87824 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| da7eaab6-1f29-3520-a76c-c5c87ce5ff38 | -20.69556 | -50.47717 | 2026-08-28 17:43:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 8cc83a06-894b-343a-9251-8dbaff75a8d5 | -15.7694 | -56.44299 | 2026-08-28 17:43:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7269346e-f603-3866-973b-808af0ccf664 | -18.37705 | -46.01067 | 2026-08-28 17:43:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11701a61-e75e-3cb1-afc0-7877be6509ab | -16.57846 | -49.78243 | 2026-08-28 17:43:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8e3d6f8c-4685-3390-b20b-81a147792060 | -18.11654 | -51.6075 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 435dcc2e-8038-373e-a122-5433672728f3 | -18.11205 | -51.6116 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ccd47b42-511b-3382-b830-3a2992318bae | -18.38025 | -46.0074 | 2026-08-28 17:43:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5d59440a-6d22-30a0-a827-18775d3aa730 | -21.75157 | -48.99239 | 2026-08-28 17:43:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c82e953e-e2b8-34d9-be4a-b0a4bef85dda | -20.62798 | -52.64734 | 2026-08-28 17:43:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3cb9355b-82c1-3eff-a5cc-a8911f47721e | -17.27921 | -46.02619 | 2026-08-28 17:43:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a112385e-790e-30e2-b40e-8eb3ac0989f9 | -20.55056 | -57.24776 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b8e50d9-3e08-352a-8e67-e6ca0342147a | -22.21 | -56.06346 | 2026-08-28 17:43:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86ef5af6-41a0-3a57-9d8e-8b50b1bf2edb | -19.06789 | -57.4036 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 4e01c33b-d4dd-300a-a31c-9f80d83d732f | -14.33632 | -47.24635 | 2026-08-28 17:43:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d2a71dcc-0fc0-37f6-abfb-44976432ee48 | -17.59454 | -51.63686 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 01ba525a-bbfb-3b5a-9d05-1a821099da93 | -15.38109 | -52.67975 | 2026-08-28 17:43:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5a07c596-28b9-3993-a739-4672b25f58f9 | -22.24273 | -56.01421 | 2026-08-28 17:43:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32a40493-c2ec-362d-af7f-7795ca0f3441 | -15.41851 | -54.35886 | 2026-08-28 17:43:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2e8bfb18-76e1-3fbb-8635-1f500cf73e32 | -14.6013 | -47.96907 | 2026-08-28 17:43:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 44c17372-7acc-3c8e-99ea-0d97f6bc85d2 | -15.72746 | -51.17638 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a2eb0e2d-f202-32fd-b74d-9639531bda47 | -18.11138 | -51.60836 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| ee2115ba-06ae-3f6e-8d53-78d44cd2ba05 | -19.07074 | -57.39867 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 82a31c18-7736-3eb0-bd62-370df1e3c1a7 | -19.23057 | -57.66077 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 300d681d-81fe-3167-a818-0697be92c619 | -20.69557 | -50.47891 | 2026-08-28 17:43:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| b11939cb-31fb-3edf-ae46-ea374d5fe8a7 | -20.59598 | -56.98091 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 75882c9b-421c-3230-9c81-c442602e26fa | -17.54824 | -51.11588 | 2026-08-28 17:43:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91e083e7-c645-31b3-8fec-1a8ddc2a4fbd | -20.55338 | -57.24286 | 2026-08-28 17:43:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c17e66ae-b37e-3f8d-a704-d64019a6b4ca | -18.79632 | -50.9228 | 2026-08-28 17:43:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 7cfbb3a6-ba60-3e89-bc58-2706f0522af7 | -19.22709 | -57.66158 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| f7864540-d807-3de6-b260-dd5bdc0aadf1 | -20.9024 | -51.54362 | 2026-08-28 17:43:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ad9ef610-2787-39e7-a86f-cc6e2c4c3033 | -18.79109 | -50.92413 | 2026-08-28 17:43:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d3626752-340f-33b8-95fb-853f0bdba4db | -19.22288 | -57.65819 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| dce8c058-fc6f-3425-8d1b-4e50d40c0463 | -15.821 | -48.22022 | 2026-08-28 17:43:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cc93eb51-4c37-30e9-b9e5-da39ed92334b | -15.02197 | -48.14785 | 2026-08-28 17:43:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cdab1d6b-72bb-3726-9b4e-635be3c2bdf5 | -16.79145 | -50.01908 | 2026-08-28 17:43:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d7409551-71cb-3ea6-acf6-c45a01964c8d | -19.22222 | -57.65411 | 2026-08-28 17:43:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1d96efc3-38f2-3ede-aa20-8213878501d4 | -15.76638 | -56.44878 | 2026-08-28 17:43:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7537b725-73cc-31a2-922d-1e59942acc12 | -16.17051 | -58.58015 | 2026-08-28 17:43:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4b5b52e0-4b8a-39fa-8ee4-db4cc2be8a78 | -15.73276 | -51.17564 | 2026-08-28 17:43:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 06c10d35-0a53-3ba7-b4e1-ab1b9dcc4f35 | -18.11518 | -51.60094 | 2026-08-28 17:43:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |


[Clique aqui para ver as próximas entradas](README136.md)
