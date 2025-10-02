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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95aff4b9-5c46-3165-893a-cd411a319768 | -11.59753 | -47.2359 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f47f25d2-5b43-3c26-9677-d7bbd12fdf35 | -9.44884 | -50.89614 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b292747-d0cb-36f5-8791-4e008f2183a6 | -11.35824 | -48.34137 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b9f28f7-4b69-3509-af38-7a76049c3541 | -14.41011 | -46.11558 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 63d89c71-8240-33c7-8cc0-a23a86502917 | -11.03308 | -47.81917 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e17b9b59-80ac-3652-8f64-24bb0f73afcc | -15.02172 | -55.27912 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad85019e-42a4-36fb-823f-70654ff70d91 | -13.20359 | -47.33751 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9160822-c161-386f-baa1-11a9cb295ead | -12.94973 | -46.377 | 2025-10-02 04:51:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2df2ab4f-7a5b-3c49-8fdb-c3a972ad72d8 | -16.04736 | -50.86021 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c653ea3-56a9-325c-a539-0d14ee11c39f | -13.16734 | -47.8241 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a83e1928-1282-3608-8d4b-f0925b198f51 | -11.41992 | -43.49902 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 395ab71e-59cf-36d4-8c23-4907628d5589 | -14.3003 | -45.96881 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4e9ac60-af5f-3c88-b0f1-508e09cfb45b | -12.82338 | -47.02724 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1ada914-a7cf-3476-b3e7-903981211194 | -11.46582 | -45.026 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 887d56a1-e889-3150-a285-5bfae33be138 | -13.32563 | -47.32876 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 464fcb8c-e456-3f71-b775-97437203e10a | -14.88915 | -48.31045 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0c51188-dea8-3679-8be0-03ac10c88e44 | -14.96913 | -49.96799 | 2025-10-02 04:51:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d92e622-c85c-30be-b84e-94aed25b49aa | -13.69064 | -48.64788 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d0addca-e186-38b5-9d74-a908ff298998 | -13.2083 | -48.51334 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e79b32a-11e5-3cb6-a182-6c32a6f43a5c | -14.36355 | -45.94939 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98f63843-12ac-38c7-b6c8-f7af5def66f2 | -9.91666 | -43.71782 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0ed5b8f-0a93-3c9a-b80c-d30bf8698ede | -11.1663 | -47.27251 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4525c9f8-c313-3450-b845-4d2bbf00ff15 | -10.6679 | -48.56601 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7f235d9-70bd-343b-8388-8aa1b16c71e9 | -15.27158 | -56.76886 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fc676ef-8e04-33bf-9445-a93d701ded79 | -11.48068 | -44.99078 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba873e26-ab38-324e-971d-5cd94bb44f37 | -9.4503 | -50.89679 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4f4cbe0-86e6-3cf6-81bc-44fa096fa93b | -13.30666 | -48.7054 | 2025-10-02 04:51:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0981c597-03bb-3bcc-afff-e348f4d5ce19 | -11.48026 | -44.99413 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee20ca2a-451a-3447-9418-110e0fe572ab | -10.81397 | -46.61559 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb5e994-9a72-3394-919d-09853b7d8273 | -14.4107 | -46.10202 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a9c8336b-599c-327b-85e5-498146948bf2 | -10.79333 | -45.35123 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 200accbb-8a9e-3ef6-ac7e-9e111c2d491c | -12.70477 | -48.58485 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7b6c24e5-d7ae-32dd-a04c-9384e545a23c | -14.90338 | -48.31874 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed575900-7311-3bae-ac21-54d518ad472d | -9.93922 | -43.76359 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 624317e9-2d57-398a-985f-b52e28ae4bb3 | -13.3065 | -47.58157 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7c7757e-29c1-3097-a66d-ce4953c8c097 | -12.86746 | -47.00986 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db9d8ac3-268a-3282-9232-2a56b2298433 | -15.25637 | -49.29799 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bc8e2f2-45c6-37de-83e7-560b88a6d553 | -13.66509 | -48.09161 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 364b5e8e-18e2-3e73-9a83-8a60bcfe57d8 | -14.96595 | -49.96243 | 2025-10-02 04:51:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5f11e00-03d0-3c5c-9eb3-077e02b59e68 | -11.86338 | -44.99775 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbfbd56e-aeb2-32d1-8bc5-f39ffb415218 | -14.90557 | -48.33583 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcb27a5b-66df-3620-8a99-4d3e47a85741 | -12.7043 | -48.58831 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8657843c-8988-37d9-aa33-6b0936bc597b | -11.08992 | -47.81286 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 722ead7b-3a3d-35fd-88d6-57662ae0dd84 | -13.147 | -47.84441 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fd21d5b4-4d0e-3e7c-a09c-b8137d6a40c3 | -10.69427 | -48.58125 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fb67d116-b591-3285-9c19-ae6ba715369c | -12.08147 | -44.92228 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc6a3e22-b2e2-3c3c-9add-b127a5ab1310 | -11.42286 | -43.49421 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13126349-36bd-37b8-885f-49f5f2ec0ac3 | -11.35908 | -44.96566 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31f75e7a-9475-3885-9d14-ac4357280f18 | -13.17033 | -47.83494 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65fd4a0a-b42b-3ac3-b5b2-ab639ffe0c5c | -15.60178 | -46.91978 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09677a17-6489-38ca-83c9-e7152318b9bd | -11.99045 | -50.57084 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e6ab530-e1ab-3081-bb48-36d79ea0e0ee | -11.67029 | -44.27856 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 326df60c-3129-3eb9-9fad-99678bfd01a1 | -12.70611 | -48.58298 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f3cbfef4-49c5-3157-b24e-ca917e5e3950 | -12.57254 | -49.8922 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfd4847f-64f4-356b-bf5b-1b36b44f6f5a | -15.25442 | -49.31247 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7da07c0-d773-3ca0-86fa-e7609f4186c5 | -11.46292 | -45.13199 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7655e4a3-4bb9-3d26-9af5-33bcb116caa8 | -13.18083 | -47.78896 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83481f9e-4f78-3d36-b5fa-e97c94d03ad5 | -11.91731 | -46.74651 | 2025-10-02 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7439f57c-377d-31c8-8e26-45389a3d0025 | -14.31321 | -45.98763 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5a3aff63-5ab1-34bb-ac4d-de1d1980e2ef | -13.80653 | -47.51536 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1bc98241-b73e-3cf3-bcaa-6803f73e09b3 | -16.0992 | -51.04259 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39b5eb4a-38c4-3f70-95a6-524399376513 | -14.88372 | -48.31825 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d804e791-7028-35ff-9beb-8112e4cfc8f0 | -9.94511 | -43.71738 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0eab0ff2-ca18-3564-94b8-9d1ddb477916 | -13.69773 | -48.62642 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dce7eeb-f1c1-3a2f-b65c-c5996a70f5c3 | -13.16429 | -47.81363 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39824923-c6fc-3244-a793-17c2b56eec83 | -14.21398 | -46.12527 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa5a9a4e-9f35-3ace-99f8-778b76ada09b | -14.80282 | -46.9683 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58914fb4-a815-33af-81ad-b746e509d50e | -13.80464 | -48.04926 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54bdb39e-610d-398c-9a91-26f0a6eb4703 | -13.24006 | -47.33839 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5323b454-f461-3fed-933d-c723ab3b8573 | -15.24272 | -48.72248 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ea63597-d285-3cfa-8944-3bea53f7fdd6 | -9.91106 | -47.709 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a1940bb-d15d-3f83-8bab-a77a5e4444c2 | -15.17375 | -49.08072 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b6f74f7-a881-34b4-971a-8f7bdce55bb0 | -11.01866 | -49.81696 | 2025-10-02 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52acce57-dcbd-3dde-9889-cf0a724cbb05 | -11.19483 | -47.1953 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4595ff31-62e7-3963-850a-fd2958f5b882 | -12.42669 | -44.09494 | 2025-10-02 04:51:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a23d83d-4af9-34aa-a04f-5a125a10fabb | -13.2431 | -48.50648 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c55bc837-3e53-317f-ac6e-112ad4cd8813 | -14.31104 | -46.00494 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84f34ad7-4cf6-3dde-848b-45599464e11e | -13.96014 | -48.13497 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a1feb682-777f-3b23-a8f3-a00dd035e6e8 | -9.92641 | -43.73298 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 87f23d62-af84-379e-a2d2-4dabbb37003f | -11.09027 | -47.80993 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25fe8383-795d-3a82-b9e2-c98da7cd11dd | -11.34968 | -44.97647 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8c20df-8338-37b0-8a83-88fc40750ae3 | -12.86571 | -47.02319 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5bc8552-b0aa-3e48-b3a4-ec4c65d31c8b | -14.2204 | -46.1144 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bde0211-adcb-3194-aae8-5f0d7b1b837b | -11.70015 | -44.30374 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32a8d182-9f35-3a2c-9958-647a9488fe25 | -9.44623 | -50.90013 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc70e644-39a1-3255-917b-3e785ede4519 | -14.89156 | -48.30825 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a6d693a-4e4f-3047-ad4e-985bdeaf6ffe | -12.94802 | -48.43845 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fe5fcaf-4bae-3da9-9401-78bc6080a25b | -13.42647 | -47.79257 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8271bae4-d4f8-3586-b726-23f659d1ebff | -11.27834 | -47.82164 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69552365-f29d-343b-b3ad-311eaae8da6f | -12.49696 | -50.26227 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7507ee6-c011-3856-a006-85c7dae665e3 | -10.65452 | -48.50277 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9697a0fd-f6df-3c01-859c-c6bff299f5c7 | -11.14628 | -54.1257 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 532a6bbd-7156-3733-9747-c1d2669fbb3a | -14.35398 | -43.84497 | 2025-10-02 04:51:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05353d8f-9759-3511-a63b-05a8668ea2ce | -14.31742 | -45.99501 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 81b63637-98e1-33bd-b517-01226766ed3c | -9.93789 | -43.77398 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6aa82eda-cd84-3c0f-877c-0dffdfc70f8c | -11.18765 | -47.82186 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d67df851-47f1-301d-9ef4-4c0a9d683469 | -15.24143 | -46.96301 | 2025-10-02 04:51:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faf2aa50-f0ae-343f-95cf-a74b36d7baa5 | -11.46993 | -45.11754 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c452b9be-1c88-368e-83e9-36dd920deb29 | -11.46854 | -45.00418 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1785357f-b181-329b-97b6-5326f35ac4ea | -13.32512 | -47.22499 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README134.md)
