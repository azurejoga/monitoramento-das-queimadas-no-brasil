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
| dfac1d53-c825-310d-ae8c-1bf00d16f134 | -12.4033 | -44.8089 | 2026-09-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 546d15b8-c314-391c-8903-ad433c7f4dad | -6.6882 | -59.9628 | 2026-09-03 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1943f946-c2d7-3921-98e6-bcff0fafb7f4 | -8.7613 | -62.5869 | 2026-09-03 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| db66f58a-cb23-343f-ba52-51de9e1fdd27 | -7.0428 | -59.2173 | 2026-09-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8a027d64-dcd1-36ef-a918-72691d7b66d2 | -11.0006 | -45.0847 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 285.1 |
| 2a44ef8c-0092-3462-bda0-2cb3dcd4034a | -6.7464 | -59.4223 | 2026-09-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 6dbda6f5-64dc-3def-a01a-05ba8fd6cd20 | -6.6727 | -43.4006 | 2026-09-03 00:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f6370583-121b-3f98-b770-29c3ba41d05b | -6.436 | -48.5301 | 2026-09-03 00:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 98ebfd2d-f153-3c01-bb88-1a77f6e376d8 | -18.7559 | -48.9267 | 2026-09-03 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 21f304f6-1813-385d-9f4b-9ec4a0e60b02 | -6.6697 | -59.9635 | 2026-09-03 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 096a8188-be0f-3717-b38c-ed86d3a1493b | -8.4295 | -54.7464 | 2026-09-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| eedcac14-5a88-3549-a4ed-36ada1f77808 | -9.0415 | -65.7349 | 2026-09-03 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 9dfa3148-09c0-3abc-b98e-91f8598c45df | -6.7067 | -59.9429 | 2026-09-03 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 8f7366dc-0664-33e4-b694-20b7fda7e489 | -14.0155 | -41.7727 | 2026-09-03 00:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 8679dc4e-917f-3ed5-83c1-db4fdade54c3 | -6.3052 | -56.0442 | 2026-09-03 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 64e4e5da-0298-3ef7-9d66-6473922b3a6d | -12.4225 | -44.8059 | 2026-09-03 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| cac355ac-2be4-373d-bd62-02e0aeab4ea0 | -8.0737 | -50.9656 | 2026-09-03 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| dcbe2b90-1898-32e1-ad21-9e6e87704a4b | -10.9815 | -45.0874 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 5c8acb4e-7806-37af-9116-f27e6c45131c | -18.1699 | -51.8122 | 2026-09-03 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 89c5ceb1-aa20-312e-9ac8-2e3ab34e2b15 | -10.8826 | -45.3075 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 691d80bc-fcb8-33eb-b79b-fe94c0409d9b | -6.6883 | -59.9436 | 2026-09-03 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 271.4 |
| c4df2455-3dd4-3e9a-8da0-d44a87c3f4a9 | -18.8407 | -46.4417 | 2026-09-03 00:30:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| bcca93cb-e99b-3e0a-a58a-9e0756657ffd | -6.6698 | -59.9443 | 2026-09-03 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| ae3de75d-82ea-3e0f-8a1e-deb66ce1d596 | -11.0003 | -45.1078 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 631ff1f1-8218-325c-b3d5-be615efdb077 | -10.9819 | -45.0643 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 05f41d7e-3bac-36cb-bc53-fe02dfdb265c | -6.4208 | -58.3137 | 2026-09-03 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| cb91c75a-4c68-32a1-95d7-339ecccb9206 | -8.0924 | -50.9642 | 2026-09-03 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| bf0dc78e-feeb-3be5-9060-1d67e38f22b4 | -11.7532 | -50.4851 | 2026-09-03 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5e7338e6-8e45-30bf-953e-8c9532a6f4a4 | -8.6132 | -62.5739 | 2026-09-03 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 14b772f7-dc98-31a0-9d55-8797e1210752 | -6.4209 | -58.2943 | 2026-09-03 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 84366823-d7b4-399e-8af2-5bfe375ed06a | -8.4296 | -54.7262 | 2026-09-03 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 4406d790-5157-3bd4-a31a-5443f8fa4431 | -10.9017 | -45.3049 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 16b10909-d055-35ea-a87a-c6c7c11ac105 | -8.7612 | -62.6058 | 2026-09-03 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 266f627a-38c6-3755-9ca6-de512b15c5d4 | -9.713 | -65.02 | 2026-09-03 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 5b2129c7-2e6e-347d-8aca-bbc68aef5109 | -6.1474 | -57.7605 | 2026-09-03 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 4e55f878-6ee5-3d2c-b19f-fb4fd8a8a67a | -18.1505 | -51.7937 | 2026-09-03 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| f398f2cb-1012-3d27-9267-8c12c0cd7a63 | -9.023 | -65.7355 | 2026-09-03 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4cbed322-d6d0-31d6-a0a3-ed4b923a18be | -9.0415 | -65.7349 | 2026-09-03 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e8ccae15-13d1-3d31-abfa-96d6297d3838 | -8.9111 | -62.353 | 2026-09-03 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6feb2d86-0015-3724-9013-cdb388d47362 | -10.9815 | -45.0874 | 2026-09-03 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 72996970-f232-3bf5-829e-767c553e2dd4 | -8.4675 | -54.6631 | 2026-09-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 1051f10c-ece5-36e8-ba72-bcf9124ae7e9 | -8.7612 | -62.6058 | 2026-09-03 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1e1c16a2-6469-360b-a7ff-e4db45200a65 | -6.3237 | -56.0434 | 2026-09-03 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 0180eee4-2993-3ca7-be1c-08f3a4a69adf | -11.001 | -45.0617 | 2026-09-03 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 5a6bbcab-fe31-3e3e-9d9a-5616438982d9 | -12.4225 | -44.8059 | 2026-09-03 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f2b61e42-04d1-3ad0-8010-f19fdf6e09a7 | -18.7565 | -48.9039 | 2026-09-03 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d7671b3b-a533-3052-9b85-ba385765bd2b | -8.7798 | -62.6051 | 2026-09-03 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1f0f2d2a-dfaa-3ae9-ac4e-bcb3b338aa5e | -8.7613 | -62.5869 | 2026-09-03 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f8887132-ec48-37da-abf8-264c016a6a13 | -18.7559 | -48.9267 | 2026-09-03 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 359d863a-075c-3bdf-a842-eb5f53425568 | -8.0739 | -50.9446 | 2026-09-03 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f236cd2e-0962-3ee3-a582-276ed33017d5 | -11.0006 | -45.0847 | 2026-09-03 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 341.1 |
| 2e9a91e0-8530-3492-9ed1-a6e5a74811a2 | -6.4208 | -58.3137 | 2026-09-03 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e9579d38-7cd7-3c1b-a9fa-0188868d2c8c | -6.3052 | -56.0442 | 2026-09-03 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b18ef80f-a79e-3522-8d17-45d463c6f6c8 | -18.1505 | -51.7937 | 2026-09-03 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f6cc3480-18ad-3f72-b522-6de91c1b1d7c | -18.1704 | -51.7904 | 2026-09-03 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 858f6766-abbb-3621-bbc4-6966ddb4fc20 | -6.8412 | -58.9746 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f4e7a615-3515-3db5-9142-f31c4713883c | -9.713 | -65.02 | 2026-09-03 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f9aacc42-7c41-32b1-8caf-a16cb1e0e1ad | -18.776 | -48.9226 | 2026-09-03 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 90ea9f92-6c69-3747-814c-118c519f6c54 | -6.1474 | -57.7605 | 2026-09-03 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b5196c96-a3d1-3f73-89b5-17b91522621d | -6.7464 | -59.4223 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 96250bd3-3674-3c95-a79d-5c52e1c7aa1a | -8.0737 | -50.9656 | 2026-09-03 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| ac774d16-a635-30c6-b62c-32b1ee820e6f | -6.6542 | -59.426 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 78d380e5-14b9-37c1-981b-04f742a51bb8 | -18.7766 | -48.8999 | 2026-09-03 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 102.0 |
| db35ad61-e4da-3317-8913-9c7b7bf521da | -9.7131 | -65.0013 | 2026-09-03 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| dfb653d9-c499-3bc8-a48d-dbe742a3617d | -11.0003 | -45.1078 | 2026-09-03 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 9c68ae45-977b-3cee-a145-8459112b7739 | -8.7799 | -62.5861 | 2026-09-03 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e98d532b-50f4-374e-a188-23f6d7591e1b | -6.7463 | -59.4416 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| ddd7e9db-b8a7-3da5-8ddd-49edeeef96dd | -18.1699 | -51.8122 | 2026-09-03 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 7022668d-c6be-3cc6-b4a3-429d66bbaa80 | -8.0924 | -50.9642 | 2026-09-03 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| bb8656b6-392d-395c-bbc8-1143a8241c1d | -6.6248 | -55.2331 | 2026-09-03 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8b498474-5405-363c-ada7-7f9959522b65 | -13.4157 | -42.4999 | 2026-09-03 00:40:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 33b8e25b-8830-35cb-9000-a8c9fcb57cd6 | -18.8407 | -46.4417 | 2026-09-03 00:40:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 79a5d969-5cbf-32e4-a897-66ebfaa5e578 | -13.4162 | -42.4755 | 2026-09-03 00:40:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 7ea89fa0-681c-358c-a7b9-857ef8e3387b | -8.0926 | -50.9431 | 2026-09-03 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7e3c2f6a-3d33-3761-8990-86ee81190845 | -6.6764 | -58.7686 | 2026-09-03 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4f454e29-6d2c-364a-bff1-405b00dcf9bd | -6.6725 | -43.4239 | 2026-09-03 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| df874033-a3ac-3778-a804-515c9d9e0738 | -6.6913 | -43.4222 | 2026-09-03 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a13ba7bf-0cd2-3c70-a86e-ae5ab64d68c4 | -8.5916 | -67.1788 | 2026-09-03 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6517cab2-3877-3e3c-8cb9-5a7a68376798 | -12.4033 | -44.8089 | 2026-09-03 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 810cbb90-3f0e-34b1-93c7-6db49938c4d7 | -6.7649 | -59.4216 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| bff8e384-d834-38b2-89f0-c3f6b1da7622 | -8.4488 | -54.6644 | 2026-09-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 66241e05-5524-32dc-95da-f47c69d81093 | -6.4209 | -58.2943 | 2026-09-03 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1a676e10-e7c8-3996-8dad-3297530d7b90 | -18.15 | -51.8156 | 2026-09-03 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 62c17963-2f52-3af2-b776-048153a75747 | -6.6541 | -59.4452 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bdc7d291-1e5f-3788-bd9a-ed2058875956 | -8.4677 | -54.6429 | 2026-09-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| dafd5a9b-1a2e-3303-b62c-aece41d2d485 | -6.7648 | -59.4408 | 2026-09-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 8300ee5b-eb6d-34f7-8bfe-9424d4abfb40 | -8.0737 | -50.9656 | 2026-09-03 00:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| b8c07a2f-b0b6-3c42-8502-4515e76f722a | -6.6882 | -59.9628 | 2026-09-03 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f6834a3d-e499-3594-af11-fef7aafe1418 | -18.7559 | -48.9267 | 2026-09-03 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 67323c8a-760c-3a93-861e-6c567c52374e | -6.6725 | -43.4239 | 2026-09-03 00:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 51199dd0-6314-3d70-b05c-4a9ab0eced3e | -6.7463 | -59.4416 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d8e32c44-1232-3c2a-afaa-a5c3cea78dc9 | -9.023 | -65.7355 | 2026-09-03 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c47c662c-0a37-33c5-ba28-2b50af83e526 | -11.0006 | -45.0847 | 2026-09-03 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 302.0 |
| d93e89aa-2714-35d9-8f16-ec0a9352023d | -6.7648 | -59.4408 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5ebc5aaf-5620-3ee9-a3fe-17c4f7fd9982 | -18.8407 | -46.4417 | 2026-09-03 00:50:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a79b0f2a-8f07-34c9-ac0b-f815a11b0f92 | -6.6358 | -59.4267 | 2026-09-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 25e70418-f812-3193-be7f-5c4a1eef2b20 | -6.6697 | -59.9635 | 2026-09-03 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8a175326-5867-3fc4-848e-de014fe5d088 | -6.7067 | -59.9429 | 2026-09-03 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| b96c789a-bcb5-3bd0-8208-43b2436a9fef | -6.6434 | -55.2322 | 2026-09-03 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| e404a9b3-a604-39a8-a7f8-f89d919a0302 | -6.6247 | -55.2531 | 2026-09-03 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |


[Clique aqui para ver as próximas entradas](README7.md)
