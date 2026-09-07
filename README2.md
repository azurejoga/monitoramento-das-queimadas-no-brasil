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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa09010e-e251-3d2d-a5f8-732b1768d20e | -6.9475 | -59.7414 | 2026-09-07 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 55f6188f-4270-3923-a6cc-4195bb8c6b07 | -3.1462 | -60.6506 | 2026-09-07 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 9741b17d-73fb-3641-ae8c-c797f36003bc | -2.6203 | -46.7602 | 2026-09-07 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| cb48b90f-d6bd-3732-af70-f622603050d3 | -9.7332 | -43.3932 | 2026-09-07 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 216.4 |
| 2ff3af9f-d117-3ac9-9eff-80885a0cdc51 | -9.7522 | -43.3907 | 2026-09-07 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 214.7 |
| 8ae2e3d9-24fc-341c-8d89-e3f7c86a8e5c | -2.9645 | -48.7036 | 2026-09-07 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6ca05ce0-1dd7-3b56-b2d9-88baf23f726e | -2.6202 | -46.7822 | 2026-09-07 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 2302bcb6-6334-34ef-96b0-c0ca12a08d91 | -6.6513 | -59.9642 | 2026-09-07 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.2 |
| df031220-879a-37c3-bd43-b6df760940df | -4.1103 | -49.0461 | 2026-09-07 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8272f3d0-8a2b-372b-80ce-9197554b50e6 | -6.0004 | -57.6884 | 2026-09-07 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b6ed7197-2298-37cd-a36f-e373bb2aa272 | -11.1994 | -44.6179 | 2026-09-07 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| db68d630-0fa8-3220-a205-5f3b3ad0fef4 | -3.6215 | -60.566 | 2026-09-07 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b89d502a-1e3a-37b2-a4f3-0693ac3169a3 | -2.6388 | -46.7597 | 2026-09-07 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 5b26d5b0-e5e0-3249-9c60-014b944f9313 | -3.6033 | -60.5664 | 2026-09-07 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c58bf3de-79fd-3068-a2f2-44fab71bd952 | -6.6514 | -59.945 | 2026-09-07 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 1461765f-1ab8-3d50-9301-f8fc55198ecd | -6.9659 | -59.7599 | 2026-09-07 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2b7ee67b-2f5b-304b-ad11-06b8addf02a4 | -4.1102 | -49.0675 | 2026-09-07 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| a757731d-4879-3047-b7d8-d9c055a2f483 | -9.7328 | -43.4168 | 2026-09-07 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 7b5f792a-6e8c-3642-b47a-aa3fc92b2e92 | -6.9474 | -59.7607 | 2026-09-07 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6d302047-c1b8-3db8-beeb-dd646f4df52b | -2.8839 | -50.4428 | 2026-09-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 350.1 |
| b2b8619c-0a73-3f1a-84be-539be7bafb52 | -6.0002 | -57.7079 | 2026-09-07 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 26505702-3e25-38a8-94c6-1e2eff6ce7e3 | -9.4968 | -40.2839 | 2026-09-07 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 01b82cdc-8ad3-3cae-8dc2-d4f7be4fa13f | -3.1461 | -60.6696 | 2026-09-07 00:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| bcf3bc94-17dd-3b3d-9edb-c22db71898ef | -2.6387 | -46.7817 | 2026-09-07 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| b00075bb-5729-350d-a306-776913de7b13 | -2.8654 | -50.4643 | 2026-09-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8e811a5b-5f98-341f-9075-45ad63e68590 | -5.9818 | -57.7087 | 2026-09-07 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 90667483-845e-3b26-9d9f-6afbda3ee1c5 | -9.7519 | -43.4143 | 2026-09-07 00:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| a69db38b-73a4-3a16-9b53-fde32ce829aa | -5.9819 | -57.6892 | 2026-09-07 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5287a1b8-2ea7-3de4-991d-f0cd69dbf54b | -2.8839 | -50.4638 | 2026-09-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| b4e62e38-79ed-3401-ac6d-b77ef485e5e3 | -6.6698 | -59.9443 | 2026-09-07 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e20b7298-167e-35d7-8e52-682c2ae319ba | -6.966 | -59.7407 | 2026-09-07 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 61c0f8cc-00c7-33c9-9ae7-db7b7c3301f9 | -7.0605 | -56.4629 | 2026-09-07 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7c34f983-e0d0-373a-a66e-07e6bf6b82b8 | -6.9475 | -59.7414 | 2026-09-07 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 877e05d8-8b0f-34d8-8c8e-33483349b070 | -2.6387 | -46.7817 | 2026-09-07 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 2d0b7d8f-c63f-3666-b325-51162d193ec6 | -2.8655 | -50.4434 | 2026-09-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 8c0ef709-0e92-3843-a6ad-2f86c7a947ca | -2.6388 | -46.7597 | 2026-09-07 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 175.0 |
| bfde9031-3ad5-3865-9e47-a4b8618f2454 | -13.2477 | -61.7342 | 2026-09-07 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 9f625f58-a00f-3071-ba4f-9b25bcb1671e | -7.0603 | -56.4827 | 2026-09-07 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7c3188b4-8dc0-3914-b753-d70415e00ded | -9.7522 | -43.3907 | 2026-09-07 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 185.2 |
| a58b94d8-ed10-39c4-b318-aac6e8247b3d | -6.6513 | -59.9642 | 2026-09-07 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| b2ad540e-a322-3965-a59f-401774696d66 | -13.2286 | -61.7549 | 2026-09-07 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 31b923ff-3493-3cb2-9e3a-818364417fda | -9.4968 | -40.2839 | 2026-09-07 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 132.2 |
| bc8a8110-d601-3f2e-932d-9c20d7632283 | -13.2476 | -61.7536 | 2026-09-07 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f89da694-46f0-3709-aaa9-96ca20b0a49b | -2.8839 | -50.4638 | 2026-09-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| f7dd4e07-87f1-354b-91ac-e6fbcc7fbc20 | -3.1462 | -60.6506 | 2026-09-07 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f0857645-2ad2-383a-bd71-d143f6e3506e | -3.1279 | -60.6509 | 2026-09-07 00:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ac31478d-1c5a-37f4-9714-d2f7f8ff2833 | -2.8654 | -50.4643 | 2026-09-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 44b02972-71df-3137-a9d1-839f0d0195af | -4.1102 | -49.0675 | 2026-09-07 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| f9f1f59a-0bef-35ed-a0d9-2dee61e17d48 | -2.884 | -50.4219 | 2026-09-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8a86d2f5-df76-38dc-bd7c-ec5645183b80 | -5.9819 | -57.6892 | 2026-09-07 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| be89c7ac-ce5f-3548-b978-bdb3ddaf7f32 | -2.9645 | -48.7036 | 2026-09-07 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| bc88d8ba-1a4d-3fac-a703-69bbfb0006cb | -3.1461 | -60.6696 | 2026-09-07 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 499b12d2-207a-39da-b857-e4aeeb82522a | -5.3646 | -56.0249 | 2026-09-07 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 60bfa08c-7541-30a6-8242-df6c585f2489 | -13.2096 | -61.7561 | 2026-09-07 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 981c85b5-b385-3d09-8ad8-409aaa722062 | -12.0379 | -64.0327 | 2026-09-07 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 3295bba0-fec8-3880-bbee-557468351862 | -6.9659 | -59.7599 | 2026-09-07 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a3129778-2e8d-32ea-bac2-b3e27adb3d91 | -11.0323 | -44.3396 | 2026-09-07 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 7e5ddd60-0efa-3903-972d-cb2caba62e6e | -6.6699 | -59.9251 | 2026-09-07 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| aef21823-dbf8-3f42-b070-4313100fa72b | -6.0002 | -57.7079 | 2026-09-07 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 19a18c7d-ea65-3919-941d-8fd41893d62b | -9.7519 | -43.4143 | 2026-09-07 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 12c998a5-2adb-3f6d-9b8d-0a80094de2c2 | -9.7328 | -43.4168 | 2026-09-07 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 7b9a49e4-72b1-31b3-8fd2-d66f416b1171 | -13.2097 | -61.7367 | 2026-09-07 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e984b89c-203f-3c60-a516-f358a222ff8c | -2.8839 | -50.4428 | 2026-09-07 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 226.0 |
| 5c0f339a-76c2-3f40-b37a-86f47104b41d | -2.6202 | -46.7822 | 2026-09-07 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 671162ff-06e2-3fb9-be1a-2ffdea7bf745 | -9.7332 | -43.3932 | 2026-09-07 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 240.3 |
| 9a0da250-85cf-3ed7-a4ce-76cc91dfb445 | -6.0004 | -57.6884 | 2026-09-07 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 35d68091-8917-350c-8a63-7cb80c5cdcdf | -13.2287 | -61.7355 | 2026-09-07 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 68341c0f-791e-3852-8b14-1fb00a6b35f0 | -3.1279 | -60.6699 | 2026-09-07 00:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d683fc85-56ac-3db2-a032-e3349cb1b869 | -6.9474 | -59.7607 | 2026-09-07 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1ecba352-4777-319e-9d59-ea26bef325e3 | -9.4777 | -40.2867 | 2026-09-07 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.5 |
| bec1c903-5ce0-3afc-b913-e6c1431a5b7c | -4.1103 | -49.0461 | 2026-09-07 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 084f9174-7032-38e2-86ed-cd860016f824 | -3.6215 | -60.566 | 2026-09-07 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a427a93f-7883-3b14-8c03-273d5e2ee818 | -11.1994 | -44.6179 | 2026-09-07 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| ec06de82-bec1-3801-898e-47635e9ca8e9 | -6.6514 | -59.945 | 2026-09-07 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 01158146-150c-375a-888d-c6e0916d01d8 | -2.6203 | -46.7602 | 2026-09-07 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 65009b66-4c8f-3c52-80d0-e11b7eb2c09e | -13.2477 | -61.7342 | 2026-09-07 00:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 99d70897-edcd-3e33-b8e9-23fca09b4878 | -6.0004 | -57.6884 | 2026-09-07 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 21042480-3818-340a-8654-eb402f60d333 | -2.8655 | -50.4434 | 2026-09-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 38ab46b8-ed4e-378e-8888-07bc0cb20318 | -2.6387 | -46.7817 | 2026-09-07 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 538c9dc3-a1ad-3aca-9c81-ccacd35132af | -2.6202 | -46.7822 | 2026-09-07 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| c900ed13-2e3b-3deb-bf23-cb93675f7f51 | -3.1461 | -60.6696 | 2026-09-07 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 1d6d51ed-f8dc-345b-8c21-078b93def854 | -11.5188 | -49.6304 | 2026-09-07 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| f556852e-9b75-30c7-841f-fd743d394886 | -2.9644 | -48.7251 | 2026-09-07 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6d22dbc1-b017-3a95-88cd-31402d7ff335 | -6.9475 | -59.7414 | 2026-09-07 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 74db1d45-0271-3ac6-9875-c3ed3df87741 | -2.8839 | -50.4428 | 2026-09-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 232.1 |
| 0defa7e5-1f49-3765-8b94-a635d1037815 | -3.1462 | -60.6506 | 2026-09-07 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 77774fc4-c5ba-3ba1-a101-86d18339c88a | -9.7332 | -43.3932 | 2026-09-07 00:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 152.0 |
| 5d938361-4e42-3792-bfe3-c4757d98da3e | -11.0323 | -44.3396 | 2026-09-07 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9304d7e7-b6d9-3073-a45c-0b04c408be45 | -6.0002 | -57.7079 | 2026-09-07 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 41aa1fd1-d3ce-3b4b-b212-651cd2bcca19 | -2.8839 | -50.4638 | 2026-09-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 51882fd3-8a4f-3a39-b0af-d1def96a9dfb | -2.9645 | -48.7036 | 2026-09-07 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| dbf241a9-68e1-3478-884f-5e83d760f5d9 | -6.6514 | -59.945 | 2026-09-07 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| eea305a7-af27-3268-b599-7a366fc48667 | -6.6698 | -59.9443 | 2026-09-07 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8a0d3ac7-4787-33f9-bef3-92de1f73cefc | -2.8654 | -50.4643 | 2026-09-07 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ee32ed10-0d8c-395f-9b36-f621688ec1f5 | -5.9818 | -57.7087 | 2026-09-07 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1e9c0fdb-e150-36d7-a2cf-73b3454f13e4 | -2.6203 | -46.7602 | 2026-09-07 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| fe8185f1-c779-3197-8f45-58c6346ab9c6 | -9.7522 | -43.3907 | 2026-09-07 00:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 133.6 |
| e33e7ac9-e32a-3951-a548-42a9b6cc8eab | -9.7328 | -43.4168 | 2026-09-07 00:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 3aa00beb-8977-3ce8-9a63-6b598b2ce016 | -5.9819 | -57.6892 | 2026-09-07 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| dca1a3f8-ca1a-33ee-8000-ac2c55b694ef | -6.6513 | -59.9642 | 2026-09-07 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |


[Clique aqui para ver as próximas entradas](README3.md)
