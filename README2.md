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
| a3608706-7f66-3f21-9eb2-1935ce5c1605 | -9.74811 | -36.32113 | 2025-12-20 03:10:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e56012f3-64df-32b0-97f6-c9f3781e0049 | -8.62508 | -37.00533 | 2025-12-20 03:10:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a21b85d-397f-35c1-9778-c3fd53a63730 | -14.73837 | -40.33677 | 2025-12-20 03:12:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| af3aca02-f79e-3320-8090-18d7b5ae038a | -14.73831 | -40.33546 | 2025-12-20 03:12:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fde91a6b-c61a-3fa3-ada1-ff08adb8ee9f | -15.45223 | -39.29507 | 2025-12-20 03:12:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0471637-1e8e-338e-b0c1-f4043eae271e | -3.8631 | -40.653 | 2025-12-20 03:20:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 355e46a1-5437-31a7-8e6f-b5d64f01f75b | -4.31651 | -38.12959 | 2025-12-20 03:29:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e67823bd-23ff-39b1-9fca-85d589d0fd45 | -6.71577 | -40.00455 | 2025-12-20 03:29:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3f9bf82d-4947-3800-8ac9-303185e837d6 | -5.56908 | -39.0989 | 2025-12-20 03:29:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba709384-effc-334a-ac20-d6ded4293989 | -5.93379 | -39.05856 | 2025-12-20 03:29:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff2c09ac-6769-3583-b411-767b496b18af | -7.17376 | -35.16714 | 2025-12-20 03:29:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7b1888e7-2a04-307d-8722-5da92719a54b | -3.86459 | -40.64505 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ce349b1b-b637-3637-9362-3e9413e0a6b2 | -6.69364 | -35.04779 | 2025-12-20 03:29:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e2e2e4cc-7e5c-36e4-8165-32cc6f2a0363 | -4.3341 | -39.36558 | 2025-12-20 03:29:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 069d2e3b-4392-3e2a-9853-73d3668aa707 | -5.09391 | -37.55296 | 2025-12-20 03:29:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 532d4607-c78e-3f8f-b5d6-f44904acbd06 | -8.25963 | -35.82928 | 2025-12-20 03:29:00 | NOAA-20 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 58efff2d-4d97-3ec8-9ea0-18ff65432588 | -4.96284 | -40.58391 | 2025-12-20 03:29:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea7f981b-8f8b-32cf-b0ba-660c79b488de | -8.25602 | -35.82864 | 2025-12-20 03:29:00 | NOAA-20 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e04db5f9-cb8a-3167-867a-05a9c3b51d87 | -5.829 | -39.23792 | 2025-12-20 03:29:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9565ae94-e0ce-3988-b547-a1ac3aeb3955 | -6.88027 | -38.97697 | 2025-12-20 03:29:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b38b8ef3-cb5b-3b3c-8695-e2fa0c70306f | -4.08289 | -38.23138 | 2025-12-20 03:29:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2be1afda-0fdf-36be-b2da-a457002b9a5b | -3.8593 | -40.64408 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| a3e4b75a-1cc2-3471-82a0-fe976235a708 | -8.79366 | -35.21737 | 2025-12-20 03:29:00 | NOAA-20 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d6f16b8-2692-39d0-bf4d-24a0dbf008e0 | -5.91649 | -38.22659 | 2025-12-20 03:29:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32b714d0-9bfe-3e11-811e-1b16ed6e5b86 | -8.62731 | -37.00327 | 2025-12-20 03:29:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6162c525-4b2f-3f67-a1c3-dfd5d183675e | -8.16291 | -38.26212 | 2025-12-20 03:29:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 67e4a9c8-2e2e-3c46-a132-6d20e04f9ff1 | -4.73846 | -40.75795 | 2025-12-20 03:29:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e17e597-1772-3129-9bc5-9eafd1e611f9 | -6.4286 | -39.51009 | 2025-12-20 03:29:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 626b3686-9fb9-3522-bbf3-bc43105d7263 | -4.7379 | -40.76117 | 2025-12-20 03:29:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 11d6bfb9-8a10-3110-a149-b0cd99bb10df | -3.86405 | -40.64835 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bf0e7b8e-21f3-3a16-b5a4-4b2d7162bbf0 | -3.85713 | -40.64713 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 390dd0c4-0314-36aa-aa06-8a20162ba4e9 | -5.50997 | -39.09072 | 2025-12-20 03:29:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af43970f-e634-3495-8f29-4469fc630d57 | -6.6972 | -35.04833 | 2025-12-20 03:29:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dcb63922-1aaf-338c-8191-e6db08dd1b58 | -3.863 | -40.64479 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| f420cc35-3274-3d10-87d1-dcca2db9a8d0 | -8.93574 | -35.71228 | 2025-12-20 03:29:00 | NOAA-20 | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b3465b57-d549-300c-bcc5-745798055408 | -8.62648 | -37.00815 | 2025-12-20 03:29:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c9c5407-9805-39d5-b0b7-cf8563c97ff6 | -4.65094 | -40.73542 | 2025-12-20 03:29:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 170f7c91-a26c-3014-8b0d-75befe854d93 | -3.8582 | -40.65069 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| dd9f818f-8d9b-3fae-9711-d64488b765f4 | -5.93297 | -39.06337 | 2025-12-20 03:29:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eac18863-2ddd-30d7-8c0e-11769db21c66 | -7.28522 | -35.15144 | 2025-12-20 03:29:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 847e7540-cbd2-34df-80f4-98dd33a29367 | -6.88478 | -38.97775 | 2025-12-20 03:29:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88283fdd-2295-3f6a-8c07-a3ec748b9b44 | -3.46039 | -41.72615 | 2025-12-20 03:29:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94aeac5f-efb9-3bfb-8af6-29c130805072 | -3.8993 | -40.68822 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee5d093b-95e4-315d-bad9-5e2d71995f41 | -3.45924 | -41.72728 | 2025-12-20 03:29:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 50b3791e-ad3e-3b33-92c9-2f1261cdc207 | -7.51415 | -35.23657 | 2025-12-20 03:29:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa58f3cd-419d-3bd3-a424-39c6aa7f4253 | -3.86243 | -40.64808 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| e4d89c1c-5905-3497-812f-4dbd8190010e | -6.10059 | -38.41754 | 2025-12-20 03:29:00 | NOAA-20 | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cadd34f8-112f-3259-a1c7-0093c9fb7909 | -8.5921 | -35.2947 | 2025-12-20 03:29:00 | NOAA-20 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ed1bd6c-6e33-3b2f-8b47-ebf2173a80c1 | -8.62814 | -36.99843 | 2025-12-20 03:29:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 917172df-254c-3d4d-833b-3ad114e26ef0 | -3.85875 | -40.64737 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| d9b0e8b1-0257-39bb-a5d2-f79846a904f1 | -7.21823 | -40.1379 | 2025-12-20 03:29:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a393ea20-2f09-3ac0-b90b-615184a7b65d | -4.65038 | -40.73874 | 2025-12-20 03:29:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f67a535-5ef8-360f-b142-2fe49e81a771 | -5.56443 | -39.09811 | 2025-12-20 03:29:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6662997c-edc0-3177-8415-36ab8339a2ce | -5.0897 | -37.55224 | 2025-12-20 03:29:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bbee7f15-c8ff-3b22-831c-7e0e52299a62 | -3.86185 | -40.65138 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c621e956-6927-31da-a32b-af5417a6b0f7 | -6.59037 | -37.99012 | 2025-12-20 03:29:00 | NOAA-20 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 573879f8-2c9a-3b81-9621-a3578008ca82 | -7.5177 | -35.23719 | 2025-12-20 03:29:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec8c7acb-35b6-3aa5-86eb-9f1820075bce | -3.8635 | -40.65166 | 2025-12-20 03:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5b5c9c07-42cb-3063-adec-685c3a0dbf99 | -5.31433 | -37.60931 | 2025-12-20 03:29:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6e01d5ca-7a6c-3d4a-aafe-6999ccdfd1a1 | -6.30425 | -41.88667 | 2025-12-20 03:29:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4ed3f26e-48a6-368a-9c76-978985006fda | -4.08811 | -38.2277 | 2025-12-20 03:29:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aba3816f-a086-3c57-b93f-b150358743e1 | -3.8631 | -40.653 | 2025-12-20 03:30:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 67.4 |
| af7fcf3d-6bbf-3b59-b53f-03d901400d5b | -9.56163 | -44.60938 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a332f899-965b-3555-8be3-3296ab2ecf9a | -13.38694 | -44.37738 | 2025-12-20 03:32:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ca3ef1-4040-3b9f-ac5a-022158bdd7ad | -11.15583 | -43.31691 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 68e1da65-fb58-32c2-b70d-fd5d1f53ce4e | -9.56785 | -44.6106 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27db4b0b-186b-3677-89a8-233edee1a299 | -9.57983 | -44.60379 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d779d1c0-1515-3270-a253-8751a30277f9 | -11.15511 | -43.32073 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fb8d32a1-f594-3057-93dc-20545dd615d5 | -9.11575 | -40.21113 | 2025-12-20 03:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ecf73f4-bb19-39f3-a9cd-32664aac8899 | -10.61089 | -37.05394 | 2025-12-20 03:32:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c5fbca00-30e1-3728-af1d-a234e1d1c26b | -13.94453 | -44.35341 | 2025-12-20 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d3b713c-cffa-3273-8b16-63db8fb8eb40 | -10.76667 | -37.14316 | 2025-12-20 03:32:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 37858118-a161-381d-b60c-558d03bb2a82 | -10.32605 | -36.65263 | 2025-12-20 03:32:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0313227-b904-3bba-a90c-3b849dde5f68 | -11.1595 | -43.31656 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ea00af52-09f5-3e99-9b93-b2c250603962 | -13.96332 | -43.27757 | 2025-12-20 03:32:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fef12f22-37fc-38c1-a505-d9bb22534dad | -15.45021 | -39.29249 | 2025-12-20 03:32:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 43617e3e-f308-3fa4-9554-0422c28e418c | -10.01535 | -42.33242 | 2025-12-20 03:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 86a75f98-4ddb-39a2-8d5b-ea3e115f8ae5 | -14.7393 | -40.33426 | 2025-12-20 03:32:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e1751a96-36d1-3848-b575-91f56e363a66 | -13.9619 | -43.27539 | 2025-12-20 03:32:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 00993e66-a649-30fe-b851-d3363b4c5937 | -13.3832 | -41.3256 | 2025-12-20 03:32:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33dc6bb7-b001-35f1-971e-6cbe02a1496c | -10.01472 | -42.33583 | 2025-12-20 03:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f26d1426-3765-32cb-a53b-d391cb2f39aa | -13.25207 | -41.34001 | 2025-12-20 03:32:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5f94d5a-16ce-32a3-9fbc-9c93002809ca | -10.58234 | -44.97414 | 2025-12-20 03:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fac59077-80a4-3346-8d13-c4c20581b6a4 | -13.96398 | -43.27418 | 2025-12-20 03:32:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ccf3366e-9cd3-3089-8ca9-3f86a492a5ef | -9.56885 | -44.60542 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 79224db7-b6ff-37b7-9ca9-b50e66eac91f | -13.3861 | -44.38156 | 2025-12-20 03:32:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bda2a37-297e-3e97-b434-a916f805db6d | -11.16025 | -43.31276 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 217b019e-4773-39aa-a154-6f74b55c391d | -11.15392 | -43.31545 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 1fae6cc0-887a-3bed-a304-3cc497724979 | -9.57507 | -44.60658 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5603273d-5284-36f0-8471-57a1fa6c85a5 | -14.735 | -40.33339 | 2025-12-20 03:32:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ee115d12-051a-3e6a-b47a-d110ff8a517a | -10.49703 | -44.92809 | 2025-12-20 03:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9f96887-0351-3bab-973c-cd2ea2bc0fd8 | -13.54227 | -44.50131 | 2025-12-20 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0750112-0379-3519-8da6-6b0399b44890 | -9.57607 | -44.60136 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 28cdf855-683e-39b2-ba20-f097d0728da4 | -11.15876 | -43.32035 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4a15a2fc-700d-3da1-bd58-8d32a7ffd693 | -9.11474 | -40.21043 | 2025-12-20 03:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 688dd362-550b-360d-a5c9-a3ea2c8776ed | -10.49284 | -44.92922 | 2025-12-20 03:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26162f34-f1b1-32a5-96fb-d012e87b6e63 | -13.54314 | -44.49704 | 2025-12-20 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d63b6d0-a401-303b-bf4f-183d7d6fd996 | -9.57406 | -44.61184 | 2025-12-20 03:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eb2e2e0d-3b62-37a0-baec-b242a2240234 | -11.15654 | -43.31311 | 2025-12-20 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6ebc7da0-34ff-3a3d-b394-76b896deb000 | -13.94372 | -44.35747 | 2025-12-20 03:32:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
