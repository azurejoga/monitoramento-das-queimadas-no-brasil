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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c231b336-360d-314e-bd6d-c768de9170b7 | -7.23907 | -43.07998 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 229baeff-ccf2-35b3-8419-11d6b3d0cec9 | -7.19205 | -45.32713 | 2025-07-05 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7adcd5f8-e762-3a2c-b7aa-c203d814b9bd | -7.2428 | -43.08413 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5936270b-9652-32a0-aff9-47567ab41d01 | -8.385 | -44.05556 | 2025-07-05 03:30:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ae9926-5f9a-3337-b4c0-14877475f452 | -7.22869 | -43.09475 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b1e47e8c-c106-3631-869e-a5097ca61d91 | -5.06636 | -43.72769 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4ccd29ce-55ef-3c2e-82bb-e14def807cb2 | -6.80445 | -44.75232 | 2025-07-05 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49150553-948a-3d91-9f34-97f29573cb09 | -7.29962 | -45.36091 | 2025-07-05 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3476010e-130d-385f-b698-abdaf1bccf30 | -4.9021 | -37.36357 | 2025-07-05 03:30:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d956630e-3660-3b5f-8f74-2e7fe75a872d | -3.99813 | -43.23921 | 2025-07-05 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1774ff4d-5af4-3cc2-9901-27c7647fae93 | -5.05222 | -43.85742 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58a2a1b2-ad30-3830-9812-e3552ef1c66d | -6.84622 | -42.79873 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8c61db72-e784-3cfa-bf38-7805f7a34ec0 | -5.06835 | -43.73218 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7ae7ff75-5007-3b3c-b0d3-c4313d05b996 | -7.24869 | -43.08509 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 175fa8a2-64fb-3c19-9c3c-573fc9a71b4a | -6.84769 | -42.79079 | 2025-07-05 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a344cb2-6c2d-3532-a4aa-b6335d92beb1 | -8.37888 | -44.05445 | 2025-07-05 03:30:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2cbcad00-103a-31b5-bba3-13ccb00f424f | -8.08851 | -45.39304 | 2025-07-05 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e252a4c-c0f6-39e5-b2d9-c17b145d79bd | -7.24495 | -43.08099 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8930a1b4-f41d-3a48-aafd-4ef1088393f1 | -6.84803 | -42.78977 | 2025-07-05 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e5ad67ae-0590-394d-ad54-cdd298a62c1b | -7.22438 | -43.08529 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b3fca97f-beb3-333d-80c8-8d179a08132c | -6.84662 | -42.79771 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7a9595d8-cf0c-3bfe-83a5-52d967ac6d27 | -6.80343 | -44.75789 | 2025-07-05 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81dd8734-2806-3f8c-90a8-337b8d316114 | -7.21991 | -43.08536 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b72d8b0e-c82f-3a1d-9ab3-b0792b30bb24 | -7.00526 | -43.54222 | 2025-07-05 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1419fde6-f053-32ec-8a29-d48dc82e756a | -6.84696 | -42.79474 | 2025-07-05 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d52110cd-f5b9-36e5-8d44-3421913c3028 | -7.23772 | -43.07881 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dc3a28eb-bca8-362d-b544-2b94f87daf53 | -8.17108 | -34.97934 | 2025-07-05 03:30:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0c02774-23c9-36ae-ae3d-e81dcaabff7a | -3.99636 | -43.23633 | 2025-07-05 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2123c614-f49f-3c97-9bed-42525a61e273 | -16.2943 | -45.10271 | 2025-07-05 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82029882-2653-3eed-8922-beba949666fc | -10.65613 | -46.39902 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34c4cda7-b4ac-3dce-b62e-63f1be246030 | -9.5837 | -44.61147 | 2025-07-05 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 586d85b0-e82b-3ba1-a8aa-e0bdae462c81 | -9.58469 | -44.60631 | 2025-07-05 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 492c2ff1-fe9b-3440-a772-f42268028f56 | -16.29997 | -45.10398 | 2025-07-05 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f7b09b4-15ad-31f8-b4bf-1fc17af7d749 | -10.63323 | -46.40777 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3cdcc1b-f982-3856-b335-b309e2c12c8a | -10.64128 | -46.4028 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a485dd4f-0fe6-326c-b8ab-b447881f527a | -11.87388 | -44.87168 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 318969d7-1399-35dd-8580-862620e1211e | -10.609 | -46.42288 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 955ff090-eda7-3cff-a136-8efe9dd44790 | -10.62387 | -46.41919 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05009bd2-a61b-3b55-b01a-68889bfc00f8 | -10.64 | -46.40915 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20a02b47-8555-35c9-b889-6f615dae8552 | -15.75198 | -43.3756 | 2025-07-05 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 951aa0bc-2549-36c4-84d7-29f673631f45 | -11.45059 | -45.11518 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5682039-bdc2-3c7e-956a-ae6d9a70d6df | -11.87299 | -44.87609 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d406f5a-29dd-362d-8ee1-0c84139c3af7 | -11.87902 | -44.87743 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e7ae8cf-08fb-3ceb-a71d-66ba1dec248e | -11.87202 | -44.88086 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a04773bf-dce3-341a-93a4-c777a8d72859 | -11.45158 | -45.11019 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3c4aded-8435-32c0-aea1-21df801b658c | -12.75406 | -44.41323 | 2025-07-05 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af78d5dd-d117-34d7-85b4-f43b14e8b5ac | -15.75712 | -43.37668 | 2025-07-05 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39764a8e-d3e1-3c2b-9eb9-e0697cd4b43f | -15.70278 | -48.30473 | 2025-07-05 03:32:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 192bf199-c4cb-3401-a840-b2357d797498 | -12.7624 | -44.4017 | 2025-07-05 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e630648-b449-3c87-a45e-53c18be2fe49 | -10.61579 | -46.4242 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 174f705e-9903-3337-92a0-d095c2af6dc7 | -12.75322 | -44.41746 | 2025-07-05 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1893d7d1-b127-3169-a2c1-c3f95eed9303 | -11.87814 | -44.88179 | 2025-07-05 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd16b5ac-11f5-3322-8345-f24a26c391e5 | -10.65484 | -46.4054 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fc9eeb2-92e1-380a-a9c3-66000c48dadd | -10.60767 | -46.4294 | 2025-07-05 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 78aa9b17-6318-3f1a-9b42-eeee6abfe9b2 | -13.16634 | -40.82445 | 2025-07-05 03:32:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e14d7fc4-6381-384c-8199-b0c7dfcb9978 | -18.85177 | -47.48927 | 2025-07-05 03:34:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ecc3ee88-ee82-39fb-bca7-9d9f3f90c369 | -19.7174 | -40.352 | 2025-07-05 03:34:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9e9a2bfe-f604-3a9f-ba6c-5255580e1c9d | -18.84866 | -47.48593 | 2025-07-05 03:34:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc5bbf9b-7d59-3366-acd9-22f3591c6f79 | -17.67936 | -43.69747 | 2025-07-05 03:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e1ce27b-fb72-3d58-ade7-fa4ee55dc010 | -20.08873 | -44.28364 | 2025-07-05 03:34:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce2cf4ba-8ebc-3256-b7cd-fa1b5b487938 | -19.26138 | -44.43401 | 2025-07-05 03:34:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89ba43f8-23f7-3514-9a6b-0dbf6e4b1a7c | -17.91147 | -45.54186 | 2025-07-05 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95fe3dc8-57eb-3593-b564-b25a5a5a28d1 | -19.83019 | -42.70262 | 2025-07-05 03:34:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3e538137-bd3c-3705-9439-16e36577fda0 | -22.67435 | -42.86193 | 2025-07-05 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bd2562f1-859c-3d94-a56f-dde4bebfa88f | -19.07743 | -43.87005 | 2025-07-05 03:34:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 178b8d20-4088-3a93-b8d8-760f53aa26c4 | -22.67526 | -42.85734 | 2025-07-05 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 96fdac06-515c-3733-be30-a463fbf168d0 | -18.85357 | -47.49318 | 2025-07-05 03:34:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 298896bc-25d3-37b8-a6dd-a68eb241f6ba | -20.08938 | -44.28051 | 2025-07-05 03:34:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bd493be2-4c79-3189-a62e-e3c765503dc6 | -18.03561 | -46.05395 | 2025-07-05 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75305f08-2f98-3e42-8c88-16c0fd72b753 | -17.91235 | -45.53782 | 2025-07-05 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9986dbbb-8561-3721-bf6a-9fcf2c506cf4 | -18.84749 | -47.49109 | 2025-07-05 03:34:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9f0b019-587a-3760-b380-48c2727af4c8 | -22.78767 | -43.75703 | 2025-07-05 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 926724fc-705e-384f-9d37-3c4750064f7e | -19.07678 | -43.87326 | 2025-07-05 03:34:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c261657e-eaef-3cbe-a72c-72d225ea3305 | -18.03461 | -46.05851 | 2025-07-05 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82ca4ede-2084-352a-bd50-dc9eb9ab189e | -20.76434 | -46.77129 | 2025-07-05 03:34:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ce08edf-7f65-39a8-8327-065ba50c7f99 | -19.26208 | -44.43068 | 2025-07-05 03:34:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 419c3beb-0e17-3cc6-a425-f0c802c8ece5 | -5.9938 | -43.74152 | 2025-07-05 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba9152a7-215a-315d-bcb0-50b2ac649485 | -4.11211 | -47.93009 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b74adc-f92f-32b5-b7e4-db51740411fb | -5.61167 | -45.17007 | 2025-07-05 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 966ab73d-4a55-3ff6-8057-dff7967e1630 | -4.98439 | -37.92445 | 2025-07-05 03:55:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9fd4872a-485d-3a65-9abb-18d2c7ef01ea | -3.52029 | -48.44178 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3736ce8e-b276-3fc3-828d-88de9d5f204f | -6.01108 | -44.52892 | 2025-07-05 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddb80066-fdfe-3d7b-823b-298064edb376 | -7.24121 | -43.08207 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e6374684-50c0-3832-b637-3d7074431905 | -3.48828 | -48.44993 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0a530a0b-177c-3817-a893-71c8c27fd380 | -4.11303 | -47.93232 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47d43f49-0bfa-360b-a7c2-21de09fdf0f0 | -6.60757 | -43.8889 | 2025-07-05 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de3212dc-e9e1-3df9-a283-696246e6510c | -7.53211 | -45.8062 | 2025-07-05 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce396b45-982d-34fd-bade-dc913d446965 | -7.94519 | -44.84935 | 2025-07-05 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb0154d4-8ebd-3967-b141-799eff415e8f | -3.41898 | -43.16426 | 2025-07-05 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ba6a613-fd2d-377c-aafa-d100d93585da | -7.23729 | -43.08142 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 540392ba-9c34-3d0e-bceb-a40046c92ae8 | -7.2278 | -43.09 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 03e57c4f-ed4f-3974-b119-20657dba7474 | -3.48902 | -48.44561 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f29ae23-8c75-32e3-81e9-fec395574dd8 | -7.28855 | -45.70586 | 2025-07-05 03:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f6fb85a-a35e-378d-bef9-9da3e005586f | -4.28199 | -48.19289 | 2025-07-05 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f48b8ad0-ae7a-3602-900b-6d0821766f31 | -8.25096 | -35.71307 | 2025-07-05 03:55:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 75f75d84-9fc8-3284-8c32-a7be9bd81a28 | -5.72762 | -49.11207 | 2025-07-05 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c97a331a-40e4-36ed-8e67-7b57b6bdb59a | -4.00244 | -43.23828 | 2025-07-05 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26c64d7-a987-3e2b-b13b-ff9354ac886d | -5.78579 | -43.6073 | 2025-07-05 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f76f0958-e0ba-3599-a6b5-79a12e751b11 | -8.09302 | -45.3934 | 2025-07-05 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0426642e-7a56-3e09-bf4d-4719c7c4068d | -5.07029 | -43.7302 | 2025-07-05 03:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README4.md)
