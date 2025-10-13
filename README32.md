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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5890870e-9e29-3ae9-98da-b0d73f96bc15 | -17.34531 | -53.80986 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8365a34-a67d-30d1-ad13-dbaa6cf3e6ef | -12.15768 | -53.6316 | 2025-10-13 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9209eac-3ad0-3ea8-9a9b-d998b0da5338 | -12.74232 | -50.65882 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bc39e15-e28c-3fb6-a4ec-72a773aa61b7 | -13.858 | -45.4953 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd1d79f5-2898-3fe1-a0f6-dd020973526f | -13.83867 | -45.53662 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ffd4460-7d0e-3b79-a0f8-94a730ab0e6f | -14.23781 | -51.48771 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deca393a-9e10-3b97-9c64-dd1b30049cba | -13.83929 | -45.53182 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b72deef-33c3-328b-a16c-1553ea97983a | -14.21096 | -51.51377 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7070d28d-8e99-3e14-b730-70624cfc0ada | -14.30538 | -51.53952 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48cf037f-d0f1-36a2-8f09-0fda90997428 | -14.30984 | -51.55511 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e720cb64-9539-3211-a6b7-54bb47b7f5b3 | -13.80082 | -52.79209 | 2025-10-13 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56af7f12-18ab-32a1-ba6f-7a56f7d4ef11 | -15.02215 | -48.7482 | 2025-10-13 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c8941da-c4b2-3111-9bcf-4f178a1f8ea6 | -17.32427 | -53.81365 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f00bbb3a-a4d2-3781-a3aa-a4979bd3f96d | -13.85028 | -45.5189 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a76c8ff-7864-3215-9798-9a5629350064 | -13.85986 | -45.48103 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e19d2f2-af55-3208-850f-e2e0d3ca9d5a | -12.23369 | -54.39254 | 2025-10-13 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e84fe7b4-07ec-3e39-8747-80ea8c8667d1 | -17.34041 | -53.79786 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a18ebf21-e9b2-304a-b240-2235df0a5d09 | -9.88403 | -60.36438 | 2025-10-13 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fa3a12a-0c58-3b30-9371-96b2ae1185b9 | -14.20817 | -51.50961 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2f7c409-63b0-36cd-b356-ea9d959ce60f | -13.86383 | -45.48642 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc0c3db2-20a0-3859-958c-739ebcc35ec8 | -9.81748 | -62.18906 | 2025-10-13 04:46:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa0e083a-cfb2-385d-acdd-88f096b61931 | -12.77793 | -50.67581 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d1862e0-fd33-390d-b710-3d98ecba16a9 | -14.31431 | -51.54839 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcac4ea6-b927-3985-a15b-28b14efbfcf8 | -17.32269 | -53.80222 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d512f9df-096f-35ea-bf1b-73e352cc961c | -16.1186 | -53.97974 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9fd8209-3d82-3868-9966-d346f1500ca5 | -17.34199 | -53.80928 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcc5dc78-e52b-34d0-b6b2-8c1c30b83c1d | -17.32658 | -53.79918 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad4f780a-28bb-3184-9784-aea5397d2aa2 | -11.15097 | -51.28495 | 2025-10-13 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6085da39-6673-37e6-83a6-66e9b8318721 | -17.67288 | -46.96138 | 2025-10-13 04:46:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d20b230a-bf6b-32b7-a7e2-8e4609d2e96c | -11.5961 | -47.5132 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aba6600-51f8-364e-be05-291677577eef | -12.7491 | -50.65989 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ef58ca2-b6d7-3cb1-bf09-bb27d9a48902 | -13.85863 | -45.49049 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a4c04c-3342-398d-92af-1b83def4c1e8 | -16.2014 | -57.58928 | 2025-10-13 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5ecfda20-b427-340d-b0ef-4c1da2fb9d1e | -13.84299 | -45.50323 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49f922f1-7b84-3aaa-bf74-df615a04fd95 | -11.59294 | -47.50746 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca7762c4-6cfb-386a-bd9b-1c2aeb743d20 | -9.67189 | -62.5138 | 2025-10-13 04:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d426ba54-1eb0-3b0e-a77e-e80cff57cdc3 | -14.221 | -51.51538 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f33dd0f9-9767-3415-82a0-22e74fe75f21 | -11.74131 | -54.71841 | 2025-10-13 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3e2943b-68b6-3bf1-ad47-6d421abf4df7 | -13.50477 | -51.29845 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cbac545-7aa7-331f-82fa-6ad42f32bc5e | -17.32601 | -53.80279 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcb93e62-a629-39e5-a1c6-600a81d9042d | -12.77115 | -50.67474 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b92be756-3b69-3cd0-bb0c-84aa0e68df2c | -12.74627 | -50.65565 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0526a273-993e-35ae-836b-f3666d6f6643 | -16.27561 | -56.0352 | 2025-10-13 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1401f2d5-6264-3a21-af30-471a96806b99 | -17.33436 | -53.79309 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98ec71c3-882a-3e69-88ad-a13fbf26f197 | -14.21487 | -51.51068 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 305f712a-1013-3f93-8679-ea4b46af7b35 | -15.84401 | -56.75099 | 2025-10-13 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b2f4c69-da41-3124-be84-60f62a7b283d | -12.44385 | -54.50241 | 2025-10-13 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86b2e41c-d804-393f-9832-a84691838428 | -17.32817 | -53.81061 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 880d4156-dfe0-3bf9-870c-4de67ea9f198 | -13.51631 | -51.30373 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b09521a0-07c6-3ad6-9bdd-e8cf5a7c544d | -13.8509 | -45.51408 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fe68e67-df2c-3787-9092-03ed4a9007bf | -12.9362 | -47.00053 | 2025-10-13 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b0e1739-39f1-3bc4-874d-c93e52d4e3c3 | -12.75815 | -50.6689 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89835801-3451-3e1b-bd5f-04b1f8de13aa | -16.12468 | -53.98452 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87090594-46f5-3a65-a919-62c39892fb49 | -16.91022 | -43.95559 | 2025-10-13 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9f70721-ed46-391e-8bdd-98693eacc9e7 | -14.24171 | -51.4846 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5555bda5-f0fb-3a2a-a0aa-b13e5bac05a2 | -13.28099 | -47.78682 | 2025-10-13 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 504a01a6-055c-3f2f-a08b-cba1fa3cbb0c | -10.18961 | -57.91373 | 2025-10-13 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca87d69f-2ace-3a04-8627-5bdf96ba65a2 | -17.33321 | -53.80032 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 889dfc78-d441-32a8-b57b-8ea11356b347 | -14.17341 | -44.62736 | 2025-10-13 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6450f7d2-88fe-3568-998e-0711624c378b | -14.18753 | -51.51001 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 623b97a1-5049-3d34-bd99-3fd9a866df1b | -14.21431 | -51.51431 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c6a2937-d711-3ffb-b40a-3203ddb6770e | -13.8295 | -45.53562 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96203196-e184-307b-9783-4ebc99d7e95e | -16.12702 | -53.96998 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 302d6c23-726c-3287-b472-ad1594aad1f0 | -14.91243 | -48.48082 | 2025-10-13 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b8d8ce0-862d-309d-b298-762f6fef56b3 | -14.26574 | -51.50709 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b3b7e0-c7c2-31be-922c-c98c91edac15 | -14.26858 | -51.55592 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d7ba88c-2963-3a7d-99c5-dd62f82d525f | -14.22044 | -51.51901 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca148832-3d80-39e3-af32-c439e6b6999b | -11.66499 | -47.55848 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66bce470-bd81-378f-b3d7-37975a63596b | -14.18808 | -51.50638 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 983620dc-b60d-30a1-b2d4-c75b03b78362 | -16.1231 | -53.97304 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4b9e9e89-3567-3559-bdb8-a21c93abac9d | -17.34257 | -53.80566 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 287ec2a3-ba3b-3a97-9785-304ab53e75c1 | -16.9778 | -55.98334 | 2025-10-13 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 51753bec-762e-3ffc-a459-b2d1d7db8165 | -14.21152 | -51.51014 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89e8a7f8-1f1d-33f2-b23d-0fcbd5a6fc15 | -14.18976 | -51.5178 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bc4b357-47ba-398a-a79c-4ef491ae7bf0 | -14.24234 | -51.52566 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f86ed3d5-bb70-3d4f-9371-d386541f80aa | -16.12761 | -53.96635 | 2025-10-13 04:46:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 340acf40-7b08-3391-9869-d6cfa170ff89 | -17.33594 | -53.80452 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c731ec50-f936-3b5f-9e0d-79771db29731 | -13.49807 | -51.29738 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a1bbfdd-f9ee-3336-9ffa-9ea2ddf76557 | -14.24289 | -51.52203 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0d043ca-4cf0-3f97-8eeb-2022d0116b62 | -11.72961 | -64.95931 | 2025-10-13 04:46:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbca86c9-2f14-3293-b078-a72f46989845 | -12.77059 | -50.67845 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf5c2616-d92a-34da-b584-fe1cf92f6b50 | -13.85925 | -45.48573 | 2025-10-13 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b60fba0e-57c4-32fe-83f9-908a43e32429 | -14.08652 | -44.09173 | 2025-10-13 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ff0c8ff-8ba0-3005-a7c2-820d965422c6 | -14.25176 | -51.48621 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8f99cde-96cd-3bd9-b6f3-fe278807e5f8 | -17.67225 | -46.96273 | 2025-10-13 04:46:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45d672c2-5ac7-377b-a957-2b27c445e972 | -9.82171 | -62.19828 | 2025-10-13 04:46:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a10fe898-e11a-3363-b959-bfd54f053ead | -14.25686 | -51.54288 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c071d948-40cd-33fd-b196-36d501f6b649 | -10.97776 | -59.02461 | 2025-10-13 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5e153bd-4ece-30b8-9960-404af5100ff8 | -16.35714 | -42.38621 | 2025-10-13 04:46:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8335dc1c-85dd-3664-87d1-d3eb3188b795 | -15.63063 | -56.02885 | 2025-10-13 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 349c7a7a-a880-34d8-bbdd-48f55087c042 | -13.50961 | -51.30266 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb61846e-6cc6-3a55-9d8c-54fac7ffe1e6 | -15.86741 | -56.76993 | 2025-10-13 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e5c28ea-71b6-35fe-8dd9-d26a361c0e99 | -17.33479 | -53.81176 | 2025-10-13 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 166aeeef-1af5-35a4-ad8a-6c1cf1f0c948 | -15.65933 | -43.90732 | 2025-10-13 04:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d690428-e3a0-32a3-af05-080e3da6e6dc | -16.97498 | -55.9786 | 2025-10-13 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d6ff6a20-8cd6-3436-b855-7190f2cae1d8 | -13.21821 | -54.14658 | 2025-10-13 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc0e5bad-eda7-3875-b0d8-a8bf405adaaf | -11.59222 | -47.51263 | 2025-10-13 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d058ab7-7d29-3b9f-adac-6af08eda4095 | -12.1591 | -53.6318 | 2025-10-13 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c80fa77-7a39-3e83-b21f-7c530aae6b40 | -14.25072 | -51.53817 | 2025-10-13 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3554fd4e-e748-35c8-be05-58aedd581be7 | -12.50168 | -52.4157 | 2025-10-13 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README33.md)
