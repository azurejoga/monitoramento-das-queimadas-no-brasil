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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3d07645-f53d-36c1-be72-e06bd83a6cbe | -13.74427 | -48.40003 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e60cf776-c08c-384d-b755-a8de272c6c07 | -11.44934 | -49.75674 | 2025-10-28 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf2c721b-8cd3-3e79-b756-21ae338a4b64 | -13.73025 | -43.99567 | 2025-10-28 04:44:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6281d234-a646-3981-8277-6264ee9ca2f8 | -10.56404 | -49.79603 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 403421bf-679d-300b-b0fb-813249eacd49 | -12.09174 | -45.67673 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54780099-5c6a-3e4a-ba7e-e2796edf6f11 | -9.14108 | -51.30145 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6a29b40-159b-37fc-a31e-13b96b592226 | -8.64006 | -44.77186 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37b7bb37-b9b7-356e-8e36-eef96651ddbf | -13.73659 | -48.42792 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66263f9e-8a87-3857-9ec6-3035bb04cf8b | -9.95687 | -47.11543 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc135ad0-c225-302a-b701-7b3a8604386a | -12.1917 | -47.02209 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49a47ca6-7f45-3e0a-9e45-94140925c156 | -14.56646 | -48.00565 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a5fec3d-2ff8-39ba-9db0-7982e4257a44 | -9.24384 | -45.60293 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74e107f8-ec96-3251-a797-94318b0baf58 | -14.73032 | -47.36016 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6009cf64-ddb9-3107-95d5-5dfc7e2099f5 | -12.62021 | -45.07367 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3833bd18-5f3c-3b92-98ef-3b01b8fbbf3f | -9.42021 | -49.32179 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86e416ba-bcfd-3dba-b77a-cb76680cd2f7 | -9.04291 | -46.93208 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0901e3c0-6e4d-3a97-af9a-e630467de10f | -13.66984 | -46.53067 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34d8bb32-7d45-31ad-bded-d2ca3a1049fb | -14.31719 | -46.51608 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c6b8e56-f9c2-3f5a-bf31-875f287fb560 | -10.92772 | -48.0146 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5cd24e7-530d-35a0-a872-170caafe7690 | -13.73717 | -48.42389 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bb65596-c998-361e-a71c-fed68aee7f74 | -8.56164 | -47.73443 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee88a610-c717-320f-aa08-5b2124786463 | -13.21797 | -47.10168 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0da07d3e-d60f-3679-8f16-b4af74404b0b | -10.15065 | -48.74816 | 2025-10-28 04:44:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7548f1b4-1ba1-309a-b128-7127b394306e | -15.57507 | -43.19971 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dbd7ea71-091b-32bf-9434-7b8b98dd0dd9 | -12.25407 | -47.92727 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3b83cc8-838d-3b93-90d8-b9c83cefdd9c | -14.56282 | -48.00497 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6e64882-3948-3b73-a374-59cd611d25dc | -14.62324 | -48.41411 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9d132f7-ffb0-3d5c-8c96-5d816ea84440 | -14.31556 | -46.51286 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dbd4ce9-b267-39d9-b1d1-aeababa98b98 | -13.36521 | -47.39119 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ae24f0b-cb62-34d2-8729-ccf3adfd55d1 | -11.3772 | -48.18728 | 2025-10-28 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 971d526e-2627-3611-92f2-aa7ff71853b6 | -13.44428 | -44.48185 | 2025-10-28 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94201c73-b292-324f-91b4-ae4cacd53621 | -15.56684 | -43.25828 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 673f8656-c516-307d-83a3-2f2134c0fb16 | -13.67057 | -46.52562 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce6997f3-6df4-3e3b-a939-377a64e31e06 | -15.31319 | -48.02831 | 2025-10-28 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 637312c2-1dc8-3fe9-abb3-8e0c8dd2d5b6 | -13.63439 | -46.46901 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c252a1ae-d598-3e4e-8723-c0693d36aca5 | -13.36888 | -47.39216 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fe62839-04c0-39c7-a4d8-3ee21237b8e0 | -13.31056 | -47.69491 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85b5d4e1-4373-3dd3-a805-748e923dcc4f | -10.62432 | -42.31633 | 2025-10-28 04:44:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ee5c0d94-862a-3fa7-9c4c-766372175c05 | -8.71742 | -50.0055 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa2e1593-4b70-36e6-a798-79a99714d52c | -8.62967 | -44.79289 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cea27f3-85a5-3a15-9479-5cda8164196a | -12.63188 | -45.08351 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5f3d3a3-8c3d-3e28-8e9c-029a1a13d58d | -9.53986 | -46.9416 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae192ff1-87a3-33f2-bc65-69cb70a65f06 | -10.29711 | -47.20488 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74d67e78-4c80-322c-9c49-3fa4475a5eac | -10.62439 | -44.89031 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fec1039-8729-3964-9f11-b59a7c0ca27a | -13.54853 | -49.58081 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bf9a78c-1e3b-3bc1-a0d7-85154951289e | -14.53292 | -47.98437 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bc401a8-ebbd-3f84-ab5f-8c8862e58360 | -10.93011 | -47.60661 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ceba6dc-f409-3e7a-9426-74d5d8c1c4a4 | -13.35879 | -47.67195 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 309a744a-a0d8-3c83-8637-1945638287fe | -9.41576 | -49.32835 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1407113-9231-3c81-b866-ed6247888667 | -9.53909 | -46.97211 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f07d05e6-3e56-3cc8-9a47-5cd331778332 | -14.5396 | -47.98438 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc1b898c-15ab-3530-9269-c7aa63a95e02 | -14.53535 | -47.98801 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a1143e-da46-3b81-9cb0-489a0c35dd73 | -10.63005 | -42.31133 | 2025-10-28 04:44:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d6f63852-3033-39da-aaf2-62df59e344cc | -10.32405 | -47.14877 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bc670b4-4785-3e0e-ae05-1568fb46b4a9 | -8.57849 | -47.14881 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68ffc33e-56df-3c9c-aeb1-5ef839bab652 | -13.30645 | -47.07557 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6448cc50-313c-3aa6-8b92-a606d824d22a | -10.55069 | -45.05389 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56e087ae-9b97-3204-8e02-9462e0eba338 | -10.56792 | -49.79303 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f772647-e914-35ad-9908-c25f5570f069 | -10.56238 | -49.80664 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a152b888-5751-3e5c-9c97-a70be2f64dfd | -12.53416 | -47.54259 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12e09c4a-bc8b-3053-b21e-c0b94673d9e2 | -13.6275 | -46.79841 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24e83fe2-d5d3-34d6-ab47-066178ec756c | -9.46611 | -46.88894 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4bf468a-4be8-3f36-a9d7-980e373fcefb | -9.13828 | -51.29732 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf16fc82-1d16-31e9-b144-bad49e155cd8 | -10.55957 | -49.78082 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ddbf8b4b-2e4f-3dd9-b11e-122e930fbe5d | -10.65488 | -47.91572 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26488f81-e931-3fe9-90ab-446e061ff4a8 | -14.0543 | -44.40323 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99ada20e-f946-3fe5-ac51-7e963ce3f672 | -10.92419 | -48.01414 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fcd5b883-9187-3857-837e-2db6d2410c61 | -11.15615 | -47.78445 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 79bad60f-29a9-30f7-a82b-93f2f434d721 | -10.93647 | -48.0281 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b61c011b-0561-344a-b3ff-6f8c26d4cc13 | -12.32049 | -47.45272 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b411a9c-3c53-3e2f-b538-3de8bcea6d8a | -9.95522 | -47.07624 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc84d910-5db1-3c81-b492-2c77a17fa18f | -10.67946 | -47.26097 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddd80cd7-4a1e-3f53-a756-d02f4040b524 | -10.92952 | -47.61066 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f31e5d4-8683-3856-a61a-01a57e0546d5 | -14.65013 | -48.40554 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 188f0c4b-06d7-340d-b3d1-721317d250ab | -10.28485 | -47.23751 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c268a23-bf36-3f54-8247-018ac5961b96 | -13.9065 | -48.49835 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f149157-e3dc-3416-b863-ae97f37a27fd | -13.5587 | -49.58264 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c77144d7-1f85-3388-8726-3476f4233fea | -15.21101 | -47.2162 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1049e8e-c91c-3709-a6ea-fb19a97b210b | -10.23704 | -52.15064 | 2025-10-28 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bac94fb-afa1-3020-84b9-1e9b3dedd644 | -8.3718 | -49.73248 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1209987e-2828-3193-927b-9b60097c20bd | -10.57683 | -49.80169 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 918ae42d-bfce-3880-9c93-c95c0e1e6ec4 | -14.81177 | -46.70622 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 744380b3-ac7f-3960-8ead-aad6ef8bc798 | -10.88549 | -47.98418 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ac4ad58-d98d-3e7a-bfc6-e86b8fa6e1ab | -8.32388 | -46.83647 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 556f00f7-5f6f-34d4-aa1d-2b6ee28862fa | -10.76377 | -44.75242 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e46919eb-3b5f-31d6-b457-84f65250828e | -13.25777 | -47.72996 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac8a2a0c-ab7b-33ac-bcd4-363658731d5d | -14.08086 | -44.15279 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7cd81a3-ea10-36c2-9089-b71b1c0a1c49 | -8.70127 | -50.80664 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c94604a4-84f9-373c-879a-183fd3f2c5fb | -14.7305 | -47.36285 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59bfc4b2-f45b-3a37-906a-d2483d62cbb7 | -12.52749 | -47.53712 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 947348e8-43d5-3ec1-b654-38aa626184bf | -13.94061 | -47.75571 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d69b19a-ecd4-359b-bdb8-eb165fd07acb | -13.3142 | -47.69564 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7a6a9446-9b4a-3d2b-99b4-99d650b6dd1f | -9.21802 | -46.35107 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1db4a838-7887-38a8-8af0-c06ef4ff6946 | -10.89055 | -48.3787 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 386cf491-7f8a-3d87-a19c-26a6dc31656b | -14.41265 | -47.91425 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fcebd88-7efe-371d-acd1-9b641e662587 | -10.91669 | -50.26415 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56a3f512-3f2f-3c5f-8945-b085e9caa5e4 | -10.36225 | -47.14015 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19027de8-15b8-3793-93a2-f4acbb40741d | -10.00064 | -48.07879 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 153e4e11-2b28-3b10-b0b0-8893c6cc117d | -10.29048 | -47.19958 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f0bec08-c85d-35e9-b35c-dd6e7c89ae6c | -10.93055 | -50.26278 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README59.md)
