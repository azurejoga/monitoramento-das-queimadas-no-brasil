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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cacf26d-5d25-30c4-8e6f-36d235f7ec88 | -15.82905 | -42.02728 | 2025-10-10 04:02:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 97481aec-abfb-3da5-b8ef-64d0e9e120fc | -17.65306 | -47.25291 | 2025-10-10 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a72e6cc-30a3-36f8-8cd4-13b01f4079b2 | -13.31397 | -47.99152 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56f2deae-81b8-3146-b69b-d5182a0d7913 | -14.39232 | -46.00735 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fed1ad7f-4e87-3a3f-958e-66a1b8f3fecc | -15.90982 | -43.2999 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8674b5a-d168-33eb-870a-a89d5ad71bee | -14.42238 | -48.00157 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ff5c064-3b35-3669-b20f-e4e7de228331 | -14.98784 | -47.19829 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7b6c7e95-dce3-3dd4-b564-84b963935701 | -11.72189 | -45.34655 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46744ec3-c401-3607-8566-8798a1d469d6 | -11.63262 | -47.52753 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 24927217-73de-331e-9661-71c0f106e000 | -15.09472 | -46.58601 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88ac6851-fd5c-3920-aeb1-98116663bfe2 | -14.89075 | -47.2272 | 2025-10-10 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08e622cf-cdcb-33e4-865d-6a01ef8443af | -15.91043 | -43.29617 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7235add-d5d5-3581-9deb-52be0487b428 | -13.84558 | -45.85262 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa222e11-0d5b-39d6-a3ce-546cdbeb0297 | -12.73673 | -45.85726 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 156016b8-0d82-3fea-b07f-5dd392e9449b | -16.73576 | -49.82831 | 2025-10-10 04:02:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 532ff1fc-13c4-36d4-9829-44c89851b37b | -15.09401 | -46.61252 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e8f0a3af-1ebd-388e-bc5f-e69b80de9e97 | -17.93155 | -45.03477 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10817c5c-e1f8-3af5-a098-fbcdf8d336eb | -13.32263 | -48.47801 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 843c8a26-2956-3f53-837a-a69cd255e2c6 | -15.97856 | -42.17753 | 2025-10-10 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25ec247f-2488-3cf3-9ebd-b5e60fea27c7 | -11.0958 | -41.05218 | 2025-10-10 04:02:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| feca507c-7921-3737-9c26-053c532b74bc | -15.55537 | -44.32811 | 2025-10-10 04:02:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5490d6b5-9cc7-3572-996a-db360f5d9312 | -17.94407 | -45.02466 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0db3956-e114-338f-9e70-f9de85cb676a | -13.84346 | -45.84211 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0285cfeb-d5c2-3d5b-b726-24f455d4e042 | -14.94418 | -46.77161 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e73dacb-4cec-30e3-8362-8ce2c0d17af2 | -15.46044 | -48.53475 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a86193c-6e03-3d31-9541-d4e2f150df97 | -17.56888 | -43.52568 | 2025-10-10 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68b23097-9f9d-37a4-983e-bc3756a40b14 | -13.31424 | -47.74347 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bda0dd5-94c0-3939-9c7e-62a012d3ce88 | -17.38869 | -45.06898 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4930b100-c31d-39bd-98df-01cb6c3ba429 | -14.89415 | -47.23179 | 2025-10-10 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 815b55df-27bc-3f68-a732-966a4e4ccdae | -13.35958 | -47.59951 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48bddd45-c9cd-3162-a8fa-b188fdff92da | -12.02484 | -43.63541 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37531e58-02b2-3c43-8559-2fcf8b8fe1bc | -12.74364 | -45.86372 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b294cdad-f4b2-35fc-8f2d-256d983d801e | -14.5737 | -47.46 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6d4860de-022d-3efe-90ce-a83ac9e16461 | -15.28595 | -40.78308 | 2025-10-10 04:02:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4e304dc-d2fc-367b-8c91-6cb3ccb2441a | -15.83149 | -43.77585 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a336d47d-fc2c-3e72-aedf-1dce08de0220 | -13.0604 | -43.84267 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9da59d1a-80dc-3a73-9b68-40bd8e1287a0 | -14.88665 | -47.22641 | 2025-10-10 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e64fea40-f92f-3a7d-b3b6-72938c6ca9ca | -12.62864 | -45.07154 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d9765791-d08e-3fbb-8ee2-e0e19621c17e | -14.9704 | -41.68006 | 2025-10-10 04:02:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc5fad03-d770-3628-9a4a-984d2b40f9e6 | -15.00433 | -46.28302 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5fcca88-e909-3573-ae73-d19c8a1da354 | -13.3799 | -47.2066 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14c82f5c-00a6-3cbe-870e-fd0522203b03 | -16.9278 | -46.56118 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55cd227a-2d5e-3bca-88ce-5d95805dfe99 | -13.37196 | -47.75092 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c049e08-e369-31da-9aae-f602beee56e4 | -14.93065 | -46.77805 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61f8eaee-aa32-3c34-b5f9-1b0cd1046b38 | -16.29068 | -45.24229 | 2025-10-10 04:02:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b191337-5eb7-3f40-9f12-e81eb1248346 | -13.27133 | -48.02326 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a58252db-104a-3324-820e-6de871334cc4 | -13.32177 | -48.48257 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bce39394-6263-3c5b-bccb-b3e7e23f49d9 | -13.4111 | -47.63475 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a34ea20c-ca45-3828-815a-76115aa02f82 | -14.72789 | -48.36128 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59cabe4f-f277-318f-bd4b-901b997a8439 | -17.96815 | -44.9524 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99789c94-951a-3d9a-a2ca-610d5f376410 | -15.3928 | -47.29637 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc242acd-8707-3980-bd74-5734f90cff04 | -10.92717 | -42.8456 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08f4c12f-e68b-3e0f-81ad-4ca6b50c9cf3 | -16.2914 | -47.14963 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1a664b3-4a1e-32ba-bb91-c2839d080d35 | -17.24866 | -46.90231 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20954f3e-de61-33de-83d3-43fbfa815c10 | -15.0056 | -46.29152 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c4b8b245-06b4-3451-8469-c2ed58b05aae | -11.70745 | -44.29488 | 2025-10-10 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4847071a-558d-32e2-81af-2e19ae20712a | -17.93225 | -45.03062 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea301923-43a3-3fe2-bda1-41355cc0946d | -13.31933 | -47.74019 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e17706e4-63d3-3091-bc09-af77daae7846 | -13.36663 | -47.20792 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7e4d09c-9d2a-3eb3-a53c-b2165019b266 | -12.13866 | -47.93224 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3e9fea3-d994-3c48-8687-b927f845adad | -11.63778 | -47.52434 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 12bf4d92-d8bd-3aef-84cb-e6558184f150 | -14.93675 | -46.76719 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc77e16b-1411-3aae-b4a3-ff9f11ee2fbd | -13.32455 | -47.73944 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 646037fe-2659-3bc6-9835-8109295b3763 | -13.41075 | -47.25282 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22aa19c1-a691-33d9-b95c-2a2f99c4b3a6 | -12.62491 | -45.07088 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ffe4997a-3661-3dc4-8786-55af2fa50e74 | -11.78596 | -45.04409 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24b66049-8b36-3a8e-ba68-60c1a98cfa94 | -15.91104 | -43.29242 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 175dddaa-91d2-3677-be01-03ee1e32f1da | -16.80267 | -49.08576 | 2025-10-10 04:02:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccf3f49a-387a-35f6-8324-590bf72bc48a | -17.32086 | -46.84128 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68151b56-a616-325e-879c-c7ae1cf17590 | -13.36759 | -47.75019 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72def597-0a70-32b8-bdda-d84c27498c78 | -15.56617 | -45.32378 | 2025-10-10 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a12487b-17f1-33c9-b873-4910243ada4b | -15.00064 | -47.55752 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cfb9242-b63c-3713-8983-19c29c7ef2b6 | -14.81388 | -40.81162 | 2025-10-10 04:02:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5279efe4-265e-39ac-8283-4dfc437e14b2 | -17.93946 | -45.03508 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d54e703e-04ea-39b4-8206-f4bc13a03c17 | -14.56095 | -43.52026 | 2025-10-10 04:02:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91373259-7f85-3766-8f72-eedc0f53b8d9 | -13.8426 | -45.84704 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c99c7052-92ba-3181-8d02-d828d113c93a | -17.21279 | -47.6539 | 2025-10-10 04:02:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 68dc9530-4b1c-3755-805d-ba8139c4e0a6 | -15.28509 | -46.15368 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b32f841-6687-304a-adbd-297df75723eb | -13.26369 | -48.02392 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07497120-f2bf-3f6d-b813-f2f0baa39229 | -13.32296 | -47.74508 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57be4c02-753f-3b7c-a386-e02fdabc8308 | -15.5707 | -45.29748 | 2025-10-10 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e5ce22d-e518-32f7-ae97-c66923625b48 | -15.50357 | -44.28675 | 2025-10-10 04:02:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fcf72e7-4e06-37ff-9c7a-d1a5e08d43cb | -16.67491 | -47.59328 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c75d36f4-a79b-3fb3-9377-8dd4d006006b | -11.45266 | -44.94833 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c62f1722-6a7f-3f30-9dce-9e0878b93d5d | -15.00651 | -46.28624 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a371db2a-63af-3184-9c67-c43e1631a50e | -15.30421 | -46.38281 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4e26125-d463-3d66-8c44-089013faf939 | -10.89804 | -43.82323 | 2025-10-10 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19790dd9-ffb9-3f50-9aa4-0a76a648f976 | -17.9946 | -44.96564 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df8bec2c-36de-3447-9095-85a28ad22f27 | -15.21939 | -42.35777 | 2025-10-10 04:02:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eabeca0f-d79a-3ca9-8c76-b2eb60bd3ff2 | -12.6892 | -47.69416 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f524d741-9e8f-32e6-85ee-ef940989c98b | -15.37957 | -48.04947 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc0caf7c-b224-3949-b035-8b55b3ba0bd5 | -12.22798 | -43.78689 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4dafc8a-fe2b-34bd-bc65-03313f02c045 | -14.1161 | -42.76922 | 2025-10-10 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 47994337-a39a-3416-9eec-f2882355733e | -15.52112 | -47.96815 | 2025-10-10 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e906477-ac60-3014-90ad-e574384f3796 | -16.2688 | -47.16031 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9f014ea-a5ec-3eba-b91a-c9cfa4c22bfc | -13.37087 | -47.2085 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34cf33db-687e-316e-98a2-595200080df7 | -14.89897 | -46.85379 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03b26833-f496-368e-b563-5fe6f458bbe7 | -13.06739 | -43.8439 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f4dc13b-51b9-3667-b4fd-977319b55ad4 | -16.25084 | -47.11422 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bde3285-356e-3004-8694-940bd4c3dda4 | -11.46359 | -41.89789 | 2025-10-10 04:02:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
