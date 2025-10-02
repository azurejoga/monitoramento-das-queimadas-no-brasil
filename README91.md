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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1db0c6c-25b1-32bf-9902-3b0802e97cc9 | -19.4583 | -44.27585 | 2025-10-02 04:32:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d50ac88-d0e2-3aa9-9eca-79cf559acc75 | -13.30518 | -47.84857 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25a9ede4-c9d1-3330-b53b-e06e89df0f84 | -15.32512 | -46.2739 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51eaf6d0-f31d-3547-8f43-bf1009824fb5 | -15.25695 | -49.27134 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad06ed5a-4ea2-3079-8014-13e80970895c | -13.69682 | -48.61772 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4a811bb-32fa-3671-af70-b9c132c787e2 | -14.41496 | -46.09879 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9d6af85-d113-3cc6-b1c3-eda81af47088 | -14.8992 | -47.18135 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6383310-449f-356f-8473-2fba42b52add | -11.92567 | -47.88462 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3ffd8c0-1468-3f51-94d9-e825e8f3e1e4 | -12.82031 | -47.05473 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db388d8a-928e-3b12-b173-87bd069c0437 | -15.94718 | -43.32573 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acce35d8-885e-3896-9127-4d40323fe8f1 | -14.48008 | -48.43552 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d57b73f-bb7e-38bf-ae89-ca731525e031 | -15.9333 | -46.24073 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 979dd519-c5bc-35e9-99f7-2c5d358dab0f | -13.55814 | -47.28665 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 75c9fb0c-802b-344a-9335-38933d6f7158 | -14.34269 | -47.15306 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cfeb965-7d2b-30d6-9e82-715f0e81c1e5 | -12.72662 | -44.84537 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78ac453d-ac20-35b7-9df1-4913e4aba587 | -17.09094 | -48.56444 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c003489c-f822-3295-8fed-40cc6e9e88b4 | -15.24695 | -46.98328 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 532ae5f7-55e7-3f0a-a069-d27e4eb39b44 | -15.34412 | -46.28902 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c08c38a-9873-3bf2-951f-f566a94f20c6 | -13.55146 | -47.28554 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c593b7e-64ef-3fa9-81c2-b9d8e42d3be3 | -13.80097 | -48.04986 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9bdd28df-caa0-3851-9685-74f036d7ec15 | -15.78959 | -43.7341 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abefb360-a5bc-30d6-9813-eca1d9da63f6 | -15.26008 | -49.30536 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23d746de-7e5b-3125-ae7d-fc6a062ad4dc | -15.29365 | -46.39142 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef109c7b-f49e-3ab5-a665-cb20f60807d4 | -12.28146 | -45.37626 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97e6e234-2eab-326b-81fc-b412f14728e5 | -15.32407 | -46.40027 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2075ae14-ba6e-3f12-bce3-d94d641d5c88 | -14.61019 | -48.23417 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97851adb-b13e-3000-bd80-632866dde83b | -13.79543 | -48.04165 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc1cfb12-9409-3ce5-b138-a06c66df7700 | -14.90536 | -48.33373 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 116b384f-0156-303e-a623-3e429a4cd932 | -13.93284 | -48.09317 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d122501-726b-36e8-84f6-38f2ef8affde | -13.34214 | -47.32921 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76eeab1f-db83-3fb6-85ff-9ffed933ab99 | -15.1475 | -48.0179 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeb267aa-1fa5-314d-9cbe-64f260d89938 | -15.23474 | -50.1176 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 570ddff7-e2eb-3459-90aa-b7da3e08194a | -13.45563 | -47.25201 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a18c07cd-60cb-3630-b013-99136d30c480 | -17.66539 | -48.1516 | 2025-10-02 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 624adb99-5dd0-34f7-9d48-debbe5f0422b | -15.48357 | -45.92683 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34cd2fad-e30b-3289-8a91-42ce0d447857 | -14.66596 | -48.11888 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa7ccbc0-78af-313b-8fac-56e25daad11f | -15.92856 | -43.3416 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 320957a2-7777-39cd-93bb-20a06f5cd7c8 | -14.48447 | -48.45094 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5db6de4-20b4-3e23-ac68-759f084788c0 | -12.06616 | -47.98375 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 708ee544-ba0d-3e5e-a227-23724465ed02 | -13.18503 | -47.79581 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf5719ac-61a1-3ca5-a6ce-5307d5ad9a13 | -16.37007 | -47.02108 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07d41104-e0c1-3e1f-9d93-085a5e0f869a | -13.80199 | -47.52723 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e688a4fe-cca8-3854-a286-38c675a253ee | -13.80927 | -47.53978 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f3621131-7d83-3dfb-a801-4e65e176d49e | -18.65672 | -43.69378 | 2025-10-02 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2031ae70-3b64-3b1e-a5ac-fc34ca6bdef8 | -12.45991 | -54.32155 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96325a42-4405-369c-91a6-703d076c5e7c | -13.75953 | -47.94444 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 992eaec0-60e6-318f-8cdd-9a6c85b01633 | -14.89319 | -48.32435 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0d6b556-1dc6-3746-b6b0-303059f61528 | -15.35275 | -46.27859 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e432cc7-66a5-3bfe-be95-4a4ddc4820fc | -15.26128 | -49.298 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 341edf39-d7ec-3223-a7fc-f69077bea63b | -14.90373 | -48.32245 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97abe0ee-32d5-3204-9b27-5952af0ed7d7 | -12.47585 | -47.2702 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c2b4108d-560a-3b17-a9f0-6572a9614e8e | -14.89871 | -48.33262 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b1954d5b-a6e8-367d-991a-93c7fd67460c | -15.25618 | -49.29752 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c629b6f-cbba-30da-9d5a-4c245493b1ee | -14.36738 | -45.9576 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa799303-7382-3847-99db-80a12c9a207e | -14.31475 | -45.97724 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71cb16d5-de54-372c-a036-dcd30481157b | -14.48845 | -48.42591 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ac3641e-a5c2-33e3-80e1-a2896572c0b7 | -13.76832 | -47.997 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30731d5a-7b79-3989-8986-33dd20cc56bf | -13.15673 | -47.80204 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3aee1a3c-78d5-3d61-87b4-fd773dcdec38 | -19.72007 | -45.87498 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d479e1a9-07a5-3c66-b187-cb7b2e45231b | -13.29986 | -47.57821 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 798cef07-03f3-36a8-b7d5-4e47f90de5c1 | -15.31084 | -46.39439 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31d9a13f-6465-314d-b047-447cdceb7c0d | -15.11412 | -48.48985 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5b97df48-761a-37c2-8400-235c126c89a4 | -14.34112 | -43.84835 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f9cc8ba-a3df-3f93-976d-b96256a96853 | -11.87216 | -48.01416 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cffe756-d1f6-3b7d-8fb2-10838ab96023 | -14.36337 | -45.91329 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cf6cfca-4c72-3b59-8153-c010a7682ebd | -12.68378 | -46.91615 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a4fb2c8-b0ec-3412-91c1-4a6f473fcdfa | -19.96531 | -43.71681 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4f098820-30d9-36d3-b93d-088655025e4a | -14.6934 | -49.62478 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75b43e68-9dd3-322c-9822-e00a30d1341a | -14.3425 | -43.83862 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45b1101f-8e6c-36cf-bf5b-318cfb2e5f7d | -13.75897 | -47.948 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f71d9f0-f85f-3742-9994-9cece8299beb | -14.65395 | -48.25973 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24c40cac-7b2a-3a13-aef7-72b795698178 | -13.40176 | -44.39185 | 2025-10-02 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bce70e80-7ada-3769-a3c5-8cbf81d003c9 | -14.31188 | -45.99653 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c860176e-2716-3110-b69a-683cd338456e | -14.29793 | -45.89881 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7063a935-272c-3bb3-a9fc-fa288d35545b | -14.68482 | -48.1074 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 356f0fcc-6fd9-3372-b4d5-c1fd66176fe4 | -13.29141 | -47.24777 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a2bc41b-5ac8-3ec2-9338-3ec6c11847b6 | -17.17693 | -47.02801 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b6b2f4c1-8fcf-3b78-9a39-9cf91accc0be | -16.03946 | -50.88515 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c390382f-961b-3de2-8be6-a319711c82cb | -13.36535 | -46.33873 | 2025-10-02 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa7e6657-77f9-3760-b601-f376f6edd3c2 | -14.02888 | -47.95546 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ac178c6-5b95-320a-8586-8e4d60ef4f92 | -13.17338 | -47.80478 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7604091b-867a-34df-a86b-7d9e549e91bc | -12.87045 | -47.01882 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5acc2cd0-f9c9-3bfe-8a18-04be521b1304 | -15.25318 | -47.91031 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 123d4e70-21d6-3bc5-89d1-5b4267a984ef | -15.25894 | -49.30177 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b9449ed-76c0-3ee7-b4c7-d57539febd10 | -12.94213 | -46.94253 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e438c34-48dd-364e-8c00-d47679dc7023 | -11.97829 | -47.01615 | 2025-10-02 04:32:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 836ca439-47bb-3af4-959a-436a2cb2c284 | -14.90762 | -48.31944 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d27e83b5-6203-3abd-a571-a268e94d047a | -12.89099 | -46.93054 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c94328fd-5088-386d-860c-70994ce36374 | -17.07279 | -44.91094 | 2025-10-02 04:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e1e1db3-c25a-3760-9feb-2a14b743e0a6 | -14.86885 | -48.2914 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ca89e53-0cc7-37cf-8d8d-681dd4d2b4f3 | -13.24472 | -47.32784 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a696902-9a9f-3a12-8fad-ae4e68e8c18e | -17.5496 | -44.4845 | 2025-10-02 04:32:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c42b04fe-f01c-3cbb-85cc-32c331019628 | -12.65758 | -46.95233 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f50f993-3e8c-3560-b31a-8e3aebf48dbe | -12.896 | -46.92037 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4704363-f80b-3b6b-b0ae-d2a0b834c530 | -14.02716 | -47.98806 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 413ee00c-d1c0-36a5-ba1d-144b945ce04a | -13.86593 | -51.25077 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c567f2-d419-3b08-9145-06bddcef3967 | -13.807 | -47.51707 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92c970f5-a8cf-3539-b538-6e289a3d4ec7 | -15.59614 | -46.90839 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24cb0a6a-f26d-3caf-b462-9968ba31b850 | -13.32144 | -47.21995 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3039cba1-f83f-3b98-9b88-e2d2a436c0d2 | -13.31069 | -47.83496 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README92.md)
