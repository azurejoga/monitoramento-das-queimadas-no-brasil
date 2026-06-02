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
| b5c8912e-2683-3933-93e3-34566bad90d1 | -11.85604 | -49.24055 | 2026-06-02 04:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a8fe0c1-221c-3dbb-83f3-b55e342cc50c | -11.63585 | -54.1643 | 2026-06-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c77238d-c151-31a1-a8d5-45192031d49e | -11.74788 | -54.78884 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 36595898-1d27-31ae-b894-112259f8cc8e | -11.79003 | -57.35711 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97ebe8a9-864d-39c9-a08f-7f118ece2035 | -11.47831 | -57.1017 | 2026-06-02 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e704bba-b614-38ff-85f9-4177f571ce2c | -10.03275 | -59.34867 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03fa6322-d328-3623-b1c1-b123a4b6c38a | -14.19026 | -52.88097 | 2026-06-02 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ceba7598-a13e-3e02-8162-76f71fd4089d | -12.32135 | -47.90621 | 2026-06-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbde3694-e524-331f-b828-a21f5561474c | -14.07343 | -58.14253 | 2026-06-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 426a9778-d076-380b-b29a-2fa5ba55f005 | -12.29622 | -52.50521 | 2026-06-02 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f62688a2-85a0-3315-a494-ed54c0224045 | -13.98321 | -53.86215 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797ee0fb-4fd8-3839-ae24-531be031768a | -14.08293 | -58.13666 | 2026-06-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df2294c1-04f0-361b-a4f4-e11cb32394bd | -13.9787 | -53.86887 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8af4ed3-e373-3193-9ad0-b03ab5bf32d9 | -10.04003 | -60.43721 | 2026-06-02 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12639062-9e74-3a52-9e55-a4031ab5ec47 | -11.61857 | -55.17731 | 2026-06-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ea356ec-43d5-3d3e-b2eb-b5b1772b01df | -12.5457 | -57.18022 | 2026-06-02 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a0b57f5-001f-3110-b46a-5a1891c0f992 | -14.23819 | -47.99722 | 2026-06-02 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80845152-9814-3467-90ed-6fc4d36ff59c | -11.88125 | -61.04758 | 2026-06-02 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bbd8dd2-d4e8-3fe6-b0b6-1eb4600e6643 | -12.73463 | -54.19458 | 2026-06-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5afaa0f3-211c-3479-ab02-2e88899c11e1 | -16.15869 | -58.46485 | 2026-06-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ec0f1c16-8fee-3745-a8ec-d5bc6ed124d3 | -10.8602 | -53.74445 | 2026-06-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa914ce2-dc0b-32fd-b611-c9cb785bbc0f | -16.1614 | -58.47298 | 2026-06-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 17ed1d8f-44f8-3e1c-b2ae-d59e1c4733e4 | -17.79047 | -49.19796 | 2026-06-02 04:49:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad69a7df-ca52-39fe-b09a-d07824ce9934 | -17.8635 | -51.78299 | 2026-06-02 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1df1066-5ee2-3e26-8c4d-69cbcbb9016d | -19.17941 | -47.35907 | 2026-06-02 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bde172de-d241-32e7-b057-59f190e8fa45 | -21.81313 | -49.12931 | 2026-06-02 04:51:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| debbed27-370e-39c4-b44a-38e9fb2c9554 | -21.70212 | -48.41256 | 2026-06-02 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b619c795-4fe4-3411-b52a-907a0de0aa58 | -21.54639 | -48.60134 | 2026-06-02 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1065ec13-4399-3776-b319-28dd18ca437b | -18.23686 | -54.59651 | 2026-06-02 04:51:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33d0f89d-c9bf-3290-8902-2f5177928595 | -18.38132 | -55.73812 | 2026-06-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 962ae815-a570-3749-af04-ffc663f40fe0 | -21.4421 | -49.92807 | 2026-06-02 04:51:00 | NOAA-21 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c288cab9-a5de-3f3a-82cf-ed84498231d5 | -18.23745 | -54.59285 | 2026-06-02 04:51:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd16e433-8986-3ff4-a442-60bcd89e1c24 | -21.43627 | -49.92569 | 2026-06-02 04:51:00 | NOAA-21 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c11fff2b-c717-39db-b43c-5048aa7b6e1c | -21.5282 | -53.39612 | 2026-06-02 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edd144c2-286c-34dd-9cb7-549f02e3edd8 | -21.43826 | -49.9275 | 2026-06-02 04:51:00 | NOAA-21 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5d96f3d2-ce29-3e2a-bf10-bd8c784035e8 | -18.40486 | -51.45619 | 2026-06-02 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94810518-93d7-339f-805c-8659d8689624 | -21.81359 | -49.12555 | 2026-06-02 04:51:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3c8bc5af-961e-3e70-8024-7185943f57e9 | -20.19801 | -50.7575 | 2026-06-02 04:51:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 359b1439-f2c8-3393-b7f3-7cf22be6075c | -18.79194 | -50.92739 | 2026-06-02 04:51:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 85c97c5b-e8a6-3c27-b9bd-86ebae26f1f7 | -18.48778 | -55.54169 | 2026-06-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 068539b6-5c7a-39f1-b9e8-5a3c9452013a | -21.27491 | -48.6148 | 2026-06-02 04:51:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c6a3a7f5-7998-3b44-921a-a96e8e0e378c | -21.55103 | -48.598 | 2026-06-02 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f2874e8b-7868-3228-8449-e22dbc5d1a5e | -20.20101 | -50.76254 | 2026-06-02 04:51:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7c6a8d6-8c3a-3fcb-84df-e2d043a74353 | -21.80955 | -49.12497 | 2026-06-02 04:51:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0dee1c6c-dabd-3620-bf16-46eb102413ef | -18.40199 | -51.4517 | 2026-06-02 04:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f6b3736-5b11-32c5-869b-a4090c84cf4b | -21.68003 | -53.54115 | 2026-06-02 04:51:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 507482b9-d859-3059-b369-842a6061a23d | -18.08101 | -50.59167 | 2026-06-02 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88e335b2-d407-34d1-8533-8742a50deb8d | -20.28958 | -50.95826 | 2026-06-02 04:51:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3c883ff0-4436-322c-9cd3-5e2b29311b2d | -18.79254 | -50.92316 | 2026-06-02 04:51:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1dd11bce-61f5-381b-8895-4b30f20ce7b6 | -20.29316 | -50.95884 | 2026-06-02 04:51:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4848b991-7bbd-3481-91d3-c8b04290ec14 | -13.98945 | -53.87276 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e40fb08-bc3e-3793-b946-b237f3c853fb | -11.62066 | -55.1775 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca0875f5-43e5-382e-a1b5-dcb819865ff9 | -10.0294 | -59.33895 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 433c8458-441e-3b71-9d97-61ba21150cd6 | -10.04289 | -60.43366 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb095d4c-662e-3d28-8116-a3107c9ce741 | -12.73529 | -54.19225 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a070052a-802c-3048-8dd1-007bff922880 | -9.18921 | -58.05801 | 2026-06-02 05:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc151733-d147-356c-97cf-bf5fa83c4edc | -11.62663 | -55.17453 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628beb3a-85d0-3caf-be1c-50aaf8ae1c9b | -14.18887 | -52.87706 | 2026-06-02 05:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c5bb158b-7615-3048-a11a-ae336fbbba2f | -7.01714 | -71.68422 | 2026-06-02 05:40:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17a76dcc-39f1-381a-9fe3-8bb10212d4ff | -11.57058 | -54.57919 | 2026-06-02 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddeb7649-a3b3-34ba-85af-225a8909e85a | -8.92636 | -64.30352 | 2026-06-02 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24ada613-1517-3cc1-b49d-8103c7894322 | -11.61469 | -55.18042 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e57f5bbd-0037-3e3b-8bf4-ae89dc8d6843 | -11.88128 | -61.04779 | 2026-06-02 05:40:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| becbe735-75aa-39fd-a7fc-412d643885fd | -12.55199 | -57.181 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d631f71c-4689-3790-bb78-46f3c778b003 | -13.98437 | -53.86201 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37f471c9-06b3-3fc9-a0f7-d5e63c6cdd37 | -11.88276 | -57.83881 | 2026-06-02 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 777633b2-353b-3866-bced-7ea2659698bc | -11.6202 | -55.18117 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92245990-a5aa-35ff-9dc3-6c6c42ee9c8c | -12.73479 | -54.19671 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 282a5fff-8d42-33fe-a48d-4ea0e3a9f170 | -9.2105 | -58.06543 | 2026-06-02 05:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56d5de0b-9ac9-3a6e-8735-fb3a49c30b62 | -12.29459 | -57.40085 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83ec77a0-e9c7-38c2-9032-d7c250622b71 | -7.50647 | -55.00447 | 2026-06-02 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84921e0f-dded-3836-a751-e12b25bd8e1a | -12.5478 | -57.17493 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4b3a696-f23b-37ff-aa46-9d6912f476a7 | -9.374 | -50.54725 | 2026-06-02 05:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 659c02ec-ed74-350c-bd27-7f06092d0a01 | -12.3035 | -57.40731 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3442c27-2409-3017-947d-3f561821cfee | -11.87861 | -57.84059 | 2026-06-02 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8589bb-3483-343f-a6bd-ae8eb11013c8 | -7.50692 | -55.00124 | 2026-06-02 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2396eb59-14a0-3d31-a8b7-10bfef918134 | -11.88194 | -61.04318 | 2026-06-02 05:40:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70571081-92d7-3029-95f6-9beb52d44cf6 | -10.03242 | -59.34671 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfa0439f-d538-3409-bab9-f391169c4a3b | -11.47602 | -57.10431 | 2026-06-02 05:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a9d6d16-8881-36c3-9865-c3b657205062 | -11.61974 | -55.18483 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7823f6f0-da4e-3e85-9827-653a266f1c95 | -9.18981 | -58.05372 | 2026-06-02 05:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bab34c5-b6b4-3c8f-8484-6bf932c34651 | -9.08894 | -50.59695 | 2026-06-02 05:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f16bc5b-e778-3d80-9ba6-83d1b9c16743 | -10.79835 | -62.41197 | 2026-06-02 05:40:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89483b63-9f7b-35bc-a246-1ad10f23ecf0 | -9.08182 | -50.59628 | 2026-06-02 05:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ca0ec83-3313-3b6e-a182-ec4e4999f282 | -10.02836 | -59.34613 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c4c9d91-eb3a-3100-afd7-9e4218bed2ff | -14.18829 | -52.88266 | 2026-06-02 05:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be52917f-e8e3-35ac-9089-c38ffa1b2bd5 | -11.88214 | -57.8436 | 2026-06-02 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65cc44ee-b009-3393-865a-6e76b62d891d | -7.50121 | -55.00365 | 2026-06-02 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51efb683-34dd-3d2c-8734-9e68ebf05bee | -11.62112 | -55.17382 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 789f1fd6-316b-3512-bac0-bf98f90e4ce2 | -10.57422 | -57.32661 | 2026-06-02 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a9324503-6bb9-3388-9173-c37cc3bd5b51 | -10.03909 | -60.43308 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fde51521-11cc-373c-8a07-904654d375ab | -11.62526 | -55.18554 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14371585-c196-328b-a230-c22696d8c228 | -12.16916 | -59.75719 | 2026-06-02 05:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| af147ed4-017e-3bfe-9d00-f7b54cf1fa96 | -7.50166 | -55.00045 | 2026-06-02 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5739511d-5d0a-385c-9ebb-0389a975a89c | -11.87751 | -57.84304 | 2026-06-02 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5687de4a-f02d-389d-b2d3-aea3deb5e9bb | -11.87752 | -61.04724 | 2026-06-02 05:40:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29504342-4d94-36fa-9bc4-27f2291a239f | -12.73142 | -54.19759 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 465a8f7c-3fa5-3ec0-bf21-7f4237402d07 | -7.50075 | -55.00691 | 2026-06-02 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f153dfa-ec07-3f05-8ce8-1f22a5360b39 | -11.6271 | -55.17082 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe40cbdf-2e05-3d24-8ef8-ad0a7f17ab1f | -12.16966 | -59.75356 | 2026-06-02 05:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README7.md)
