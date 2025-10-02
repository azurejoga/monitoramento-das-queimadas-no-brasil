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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07e8e1a3-cf82-38ee-958b-d5414a78a94a | -14.22913 | -44.9389 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 926a3933-9cae-315c-9661-229b2cb5e055 | -15.22893 | -50.12057 | 2025-10-02 04:04:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 53733330-88bd-34e5-b878-d58e424b28ad | -15.25612 | -49.30875 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1d575d82-9026-3442-9c87-ba3b910070b8 | -13.74336 | -47.91869 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aafbb7cb-33cb-3bee-ab0e-82854e77d950 | -13.30855 | -47.83987 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1884117d-c654-3981-9c5a-31058ca510ba | -13.75803 | -47.96024 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31a51c9b-1264-39c3-adeb-a22fb13e5012 | -15.50563 | -45.90782 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46cd5a8a-d2d7-364f-9749-5eb0ce938a9b | -15.31766 | -46.28911 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f6d4c365-1a1b-30df-9713-729db78061ba | -15.25971 | -49.31496 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3cb187db-d922-3b7d-b32f-84bb4ee66397 | -14.36093 | -45.96809 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c836f5e-9806-3284-917a-e38f0a242087 | -13.21164 | -48.51625 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff89d64c-5638-3a8f-b46f-6908236e5fbd | -18.43034 | -46.52948 | 2025-10-02 04:04:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac2bdba4-746b-3759-b8ae-4231a9452b77 | -15.80067 | -43.73362 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a41b1a42-3bc0-3346-bbc7-ae4992ba0f1e | -13.30617 | -47.85288 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1860757f-5bed-3ae7-a8cf-2014a2c179ae | -13.76119 | -48.69053 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9f907d24-e616-3e82-bd39-0efc9870d4b6 | -14.70834 | -49.61699 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 033a76a4-b9b7-3aec-863b-1e9002327764 | -15.94832 | -43.32654 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5ce624f-b18f-37cc-92be-88a629ee4a21 | -13.9378 | -48.09592 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efb94ad9-85a5-3e23-b9cb-ff306368cf81 | -18.68464 | -47.04523 | 2025-10-02 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 070b7e22-e2eb-31cd-acd0-3aedcffbbaec | -13.31097 | -47.58921 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad28b9c9-9edb-339c-afc5-c52d8ec4d1bb | -19.5945 | -42.4753 | 2025-10-02 04:04:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 019dc119-dc58-3f21-8602-bd92950f7714 | -19.01076 | -44.99792 | 2025-10-02 04:04:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bec42b9-7baa-3b8a-8f69-233cc194fb9c | -16.62274 | -41.57021 | 2025-10-02 04:04:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 98db5760-b3a1-3320-bc95-1dbecfcc65fd | -13.52339 | -47.25811 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d4d41c1-ff4d-3420-b7a7-7ec86c73c3c1 | -17.51609 | -43.48777 | 2025-10-02 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3f22946-8ffd-3694-b15e-a7f0ce2937c0 | -15.7973 | -43.73304 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| eba1d98a-3e17-38d9-a6f0-9d2877085ac4 | -14.42153 | -46.13498 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 79029883-1d20-3b32-9060-1633042dbd6d | -16.01062 | -50.90887 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 439e7e0c-ac8a-373d-ab31-499f06f6a96e | -13.17896 | -47.8303 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c2a26ac-70af-3127-8a8e-b10966c936ab | -13.37825 | -47.29227 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93f6d362-ada0-38d2-8212-c4a52045fd3f | -16.14088 | -46.68005 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 521fbd02-0fbb-36c0-b6ae-45198f743eca | -14.30908 | -45.99783 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| befde3c2-6841-3acd-8cd0-7214dd576ee2 | -14.61222 | -48.23606 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e2800ef-825c-303e-819f-a615e8efebf4 | -13.28938 | -47.25171 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb045d37-f76c-3aab-8702-ee5fbc20cad4 | -14.35799 | -45.96259 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2be9483f-0438-3cfe-aa27-43e2c3e4e4b1 | -15.94773 | -43.33019 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 442fb371-e5f5-3180-bb14-18a780732fe0 | -14.08851 | -46.65407 | 2025-10-02 04:04:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2ed6e59f-a6de-31c3-a652-f819cdbb5aab | -16.04175 | -50.85692 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ebdb7e9-be3b-3145-b038-170301d84df2 | -17.67 | -48.15274 | 2025-10-02 04:04:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98d58249-01bd-3ecc-8974-e2fd3e4b26aa | -15.25473 | -47.90633 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 34f6a084-1e8d-3d9f-b5d6-303b0bd24379 | -12.76251 | -50.55812 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b99a7101-b169-3f1a-9282-a968a933328d | -15.15867 | -48.39809 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a22fda6-c734-3864-9bab-8be135bf063c | -19.46133 | -44.28097 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 094c0f89-7545-3674-abdf-81f0e07bd0bb | -14.43715 | -46.35267 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ece063ad-af4e-3bec-9923-42e88eb79bdc | -15.28789 | -40.78378 | 2025-10-02 04:04:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebdc3dec-d26a-318f-9ec1-3b45267d269f | -12.70717 | -48.58297 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1494e5d3-8b5f-338d-925e-1747cb956f03 | -13.7753 | -48.04547 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3ebd018-55b5-37a8-985a-cf62c378adea | -13.16246 | -47.83708 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3235e8c-fbb2-34cd-a562-7bbac1768c09 | -13.47653 | -47.24536 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3762247-f5d4-3841-a827-3847a3bcc888 | -13.78622 | -48.05161 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b34fa888-1e0c-3529-99e6-24f7c84a8d7b | -13.56744 | -47.59215 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9108d933-6061-308f-831f-007bb76ccf1d | -13.17532 | -47.8017 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ab80f72-857e-3101-8187-4c272e2d2ad1 | -14.47424 | -48.43695 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3c52b301-f21e-3b64-a0f5-660940d33dc0 | -15.28176 | -49.29733 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87363aca-40d7-3cf2-9611-b47c6ff7c477 | -14.10647 | -45.64386 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f289a40-b287-35d3-aef4-f1ac48eac9a7 | -14.21281 | -46.12661 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 71a9eb97-3a89-38c3-8561-2e7dfabaaedf | -13.80416 | -47.53745 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c54879fc-28d3-3d69-90b0-096f84e36756 | -12.94773 | -48.43726 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf705592-a87d-3fb8-aac3-f4cdc973dbf8 | -18.55117 | -43.44639 | 2025-10-02 04:04:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5e58694f-f5e7-3e91-a136-496e2259dfe4 | -13.31523 | -47.20352 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9ff3365-77ee-3e10-bf61-b2a0a204221b | -17.95504 | -45.03794 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9414b27-95f2-3d67-9b00-4408f4b047cf | -13.21435 | -47.34953 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8879c32c-0448-3b42-905b-5537e74d4c50 | -14.90954 | -47.22192 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e2ba6ed-e689-3ea6-82d0-f9a2e4f68d51 | -13.32707 | -47.81157 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3878b0cb-f41e-3a4a-8109-543aa9c7f4dc | -13.37355 | -47.28417 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2590a1f6-9246-3c5c-bfb8-9cf0e537c44a | -14.5796 | -46.36592 | 2025-10-02 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e1130f9-8f3f-3b2a-a9a5-16f56ac4d480 | -19.69134 | -43.68324 | 2025-10-02 04:04:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41904b69-a792-3c4b-aa6e-6290c1731f94 | -15.75688 | -43.68392 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2d2fe9d-17b2-3d03-9476-1b454e4a3885 | -14.48517 | -48.42707 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 541bf25a-ce56-3150-9728-766391ae22a6 | -13.53704 | -47.27717 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9067166d-60ed-357a-b0d6-6bdbea7a5281 | -14.47166 | -48.40247 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ffebce3-1c25-3a61-a385-8c76e72deeb9 | -15.19852 | -48.16161 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d19bc633-5f1b-31d9-8f27-272b70ae8631 | -13.77899 | -48.04972 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64874aa2-6250-3f27-a19b-b6d0f6436b90 | -14.86365 | -48.29747 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e9accc5f-4d1f-3d9a-b22d-2e432f3fcbde | -13.3148 | -47.8544 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f445adbf-6b37-3ef2-ac85-86398485f32f | -15.25127 | -47.90164 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c868efc-2e08-3231-8218-01a86da310b3 | -14.69697 | -49.62506 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd46a518-6915-3936-9acd-a6a190a0e28c | -13.07204 | -47.02016 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24e14632-ca62-32dc-a949-1d5de5e996cf | -15.27972 | -49.30959 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b5f344a4-259d-3b7f-b5aa-b7eb32162c06 | -19.02199 | -49.74616 | 2025-10-02 04:04:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bde4f125-b639-3bdc-ab17-7f0dc970c36e | -14.31536 | -45.98419 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| aaee9f4d-2872-3a39-a96e-46660ca7491a | -13.80155 | -48.04886 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16394074-b310-38c0-95c5-50e78bfa3bd5 | -19.57977 | -41.90141 | 2025-10-02 04:04:00 | NOAA-21 | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 18b72693-b007-3ad2-89d4-b17a49064cb4 | -14.30364 | -45.96213 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 76acc8ca-7d12-3a99-b784-4fb7866843d2 | -15.93988 | -43.33635 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6abd4bfc-c93d-3748-bd26-eabe67f71d50 | -13.21497 | -48.49813 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b45b52f7-f82c-3899-a711-a0659b8df819 | -15.83339 | -42.62127 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6a85b6bf-ec6d-3654-a411-2e316207c2ee | -15.28157 | -49.29968 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf2713c5-ce01-3299-b6db-a5d6faa612d2 | -19.71224 | -45.9087 | 2025-10-02 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6abb7065-fd58-3281-a9ec-b18f63857404 | -20.12465 | -44.01734 | 2025-10-02 04:04:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b9de29f-8b06-3e49-acc1-3906a987c99f | -13.85449 | -51.24603 | 2025-10-02 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdc05c61-aa9b-3899-9f59-da1d18e7ded1 | -13.21996 | -48.44576 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9331f275-c341-3280-b68c-b295ab9d0050 | -14.69266 | -49.61612 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c96c9993-f31e-30b7-9967-50d4c8b982cb | -14.43155 | -46.3618 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98da1352-343c-3b4e-9106-d64db94e18db | -14.47953 | -48.43282 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 68440889-9c64-35b6-be64-24c04d4a4c09 | -13.53753 | -47.25068 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88708c9a-a6c6-3b7e-ae02-9c922bcf4b2e | -14.21534 | -46.112 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f5953ef-9052-3e55-8d97-13a0a83a8a93 | -16.06342 | -51.00531 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a3a32d-9cda-319d-bb05-9fa31c64d991 | -13.66347 | -48.08448 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fbc643c-55cb-3803-91c5-d52b9da85bdf | -18.60988 | -50.70007 | 2025-10-02 04:04:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
