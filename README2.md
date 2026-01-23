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
| 3b025b90-86ea-383c-bfc3-a221c8c323e7 | -5.00546 | -37.5344 | 2026-01-23 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 131d0bd2-90fc-38b5-be0e-7d80793d8006 | -5.09452 | -37.78972 | 2026-01-23 03:42:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c01ab9f-e9b8-3ab4-b7be-2af4470424df | -4.52126 | -38.42936 | 2026-01-23 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 20123a65-3b7f-3dfc-aec8-ef2350382e22 | -8.38634 | -35.30612 | 2026-01-23 03:44:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14d91a7f-7e68-3683-b2cc-2c136affa5fd | -10.16247 | -36.24163 | 2026-01-23 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 44af710e-c037-3354-9073-59c2d600b6f8 | -8.16229 | -43.18666 | 2026-01-23 03:44:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74d35a70-ada2-39e0-bb03-45f80819f603 | -6.76616 | -35.18058 | 2026-01-23 03:44:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24ef5bb7-b3ce-30a6-8273-eef4769474bf | -5.93696 | -39.68724 | 2026-01-23 03:44:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b362d227-cdd2-31aa-b83e-d2abbcedb7f3 | -7.57143 | -46.48368 | 2026-01-23 03:44:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c9f1079-b12b-34a4-9f01-402e0a4c1ba2 | -5.57543 | -39.20072 | 2026-01-23 03:44:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 931cc190-a4d5-3bd8-b900-99264ce34c4c | -5.62093 | -44.84521 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 79adcbd3-1388-3870-bf17-b1b3f2e7d278 | -12.22038 | -38.14797 | 2026-01-23 03:44:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 707ecd37-ccc9-3a64-a3cd-c454a8176b29 | -8.75097 | -36.60341 | 2026-01-23 03:44:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4021585-990b-335c-8b43-357f80353e5c | -8.1554 | -43.18874 | 2026-01-23 03:44:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54e7b5ac-9e77-3762-b813-4b1592a2fc76 | -8.75373 | -36.60742 | 2026-01-23 03:44:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebc0f230-27e6-3c82-af78-7795a694aa67 | -10.35299 | -39.07122 | 2026-01-23 03:44:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8421fb6f-4138-33a9-8dd9-715a44f16603 | -9.99148 | -36.35703 | 2026-01-23 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 73af1495-fe1f-3c81-81e3-486b561f2b75 | -5.62649 | -44.84605 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 53d9065f-69da-3c81-93af-21df996fa852 | -10.93063 | -39.48528 | 2026-01-23 03:44:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2af37e98-e49e-37aa-85e4-ea0661aa778e | -7.35125 | -37.69922 | 2026-01-23 03:44:00 | NOAA-21 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3c617263-2a42-31f0-b72f-33131e0ff613 | -5.62154 | -44.84162 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b304023a-6591-36f6-bb97-d2bb9368c9e0 | -6.99417 | -42.86662 | 2026-01-23 03:44:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a03eeb0e-b83d-3db3-91db-0de337340fb6 | -6.74921 | -37.94811 | 2026-01-23 03:44:00 | NOAA-21 | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 49fbc974-bab5-32a6-9485-489f239f0157 | -11.07607 | -37.39216 | 2026-01-23 03:44:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 288bd909-0b5e-3fee-982b-2800e4e116cf | -10.51012 | -36.73486 | 2026-01-23 03:44:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cc88bc3d-dc1b-3c97-a81a-a26e08d04b3d | -10.16522 | -36.24564 | 2026-01-23 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f0e1e6c9-916f-35d4-9c09-5d48abfdc0a2 | -5.62215 | -44.83803 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b2c7753-18f7-37fb-a6ab-ec638773dd50 | -8.33169 | -35.26549 | 2026-01-23 03:44:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 373aa7b8-4c56-3f9e-b8a5-7d438bef06d2 | -9.99478 | -36.35755 | 2026-01-23 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93b87501-2e99-399b-8ed0-45e5f0efd4b5 | -6.7667 | -35.17712 | 2026-01-23 03:44:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 071f3044-a560-3926-a32f-6ebdd38fff49 | -5.62223 | -44.83814 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8a7bac3c-294b-3610-bbe5-3280f9dd4701 | -10.16852 | -36.24616 | 2026-01-23 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c2a61e7a-8672-3cf6-b5ca-c54fc7b2eaed | -5.63266 | -44.84327 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc26b082-a641-3cd8-b9fe-3e308ca06158 | -5.62713 | -44.84246 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5ce8a048-462a-3e07-8028-669da81eff9f | -5.9353 | -39.68887 | 2026-01-23 03:44:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a5fe40f-5956-358a-8f62-c8f01058a0b6 | -7.04711 | -36.35771 | 2026-01-23 03:44:00 | NOAA-21 | SOLEDADE | PARAÍBA | Brasil | 2516102 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4d9651ec-e34c-3092-8ae5-c4cdeccf7fa3 | -6.41569 | -39.64179 | 2026-01-23 03:44:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7decd521-a1f6-3160-84d0-118adaa0ca81 | -6.30901 | -37.53585 | 2026-01-23 03:44:00 | NOAA-21 | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abee4d54-a224-3065-acce-87baf0611735 | -10.16577 | -36.24216 | 2026-01-23 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ee12f9b3-582a-3a82-b94c-2b58ac54d5a8 | -7.34781 | -37.69868 | 2026-01-23 03:44:00 | NOAA-21 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b99632e7-2b1d-37be-8b57-e86690b0c017 | -10.16907 | -36.24268 | 2026-01-23 03:44:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 586ea828-4636-329e-a9ba-7e9cc0f9b00f | -5.62159 | -44.84172 | 2026-01-23 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0f49c1d8-0c39-36b3-aaf0-8d83bdafe650 | -7.5747 | -46.48681 | 2026-01-23 03:44:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a2a3ab8-c91d-3f50-b22e-c71b91932875 | -8.15067 | -43.18799 | 2026-01-23 03:44:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| def819a9-da3f-3f92-a5ea-4305f8c5805a | -10.47098 | -36.74644 | 2026-01-23 03:44:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 19620690-6781-3ee8-a417-904f1cc99248 | -7.49656 | -37.44957 | 2026-01-23 03:44:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6db82eeb-30ee-39c7-8f7a-80d318113c61 | -10.35366 | -39.06718 | 2026-01-23 03:44:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5a8bf4e-f940-324c-9cf0-fa54d0dfc5db | -7.55118 | -37.78866 | 2026-01-23 03:44:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f7a6a2dd-4079-3450-8ff7-dd015bf5c53c | -7.45387 | -35.17978 | 2026-01-23 03:44:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| bb7dbf2a-9fb7-364a-95f8-b51e17ec04f6 | -7.23925 | -37.95314 | 2026-01-23 03:44:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09801be2-97fa-365f-856c-1e161b12e60c | -6.26104 | -40.61191 | 2026-01-23 03:44:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b140aa95-b956-3cbe-8c03-1b2d2652ec70 | -8.17202 | -34.97908 | 2026-01-23 03:44:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fd871e6d-228e-3d49-bf7c-32ee8ed56827 | -6.61946 | -37.89925 | 2026-01-23 03:44:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08f3763d-4ed1-3c4c-bc51-a2634b794092 | -8.75428 | -36.60393 | 2026-01-23 03:44:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62c13715-0f4b-387a-a493-b66a8d2de341 | -9.81538 | -36.26457 | 2026-01-23 03:44:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7139d7a1-d92f-3756-9afc-6bfc7e7b71b2 | -10.51343 | -36.7354 | 2026-01-23 03:44:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7eba582-3ad4-3271-b0fa-7e1ca7382edb | -7.97013 | -38.27957 | 2026-01-23 03:44:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ebb3c33-6f9d-3d8b-a278-fa7c9b1a6782 | -8.16013 | -43.18952 | 2026-01-23 03:44:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ecc2d793-0d9a-3577-88e5-d16c1da1f741 | -10.47043 | -36.74994 | 2026-01-23 03:44:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 02e4ec44-2bc3-33a0-8da7-58af5b829460 | -22.6132 | -49.57109 | 2026-01-23 03:49:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4003aa18-9566-39af-beba-78ca38282a78 | -22.04017 | -49.50553 | 2026-01-23 03:49:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fc5731b8-80c7-3f9c-b306-be564352442d | -22.04045 | -49.50402 | 2026-01-23 03:49:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| faafb383-f0a6-3d0e-89b0-ba492639b6c3 | -23.05675 | -49.06082 | 2026-01-23 03:49:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12e6fd7b-b741-3306-9222-c8be99e896a2 | -22.606 | -49.5776 | 2026-01-23 03:49:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7de8f017-9d33-322a-a531-50f01f102877 | -22.60783 | -49.56958 | 2026-01-23 03:49:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| af50c1a5-4754-32d5-b734-aea9e78cd382 | -22.61229 | -49.57511 | 2026-01-23 03:49:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47a13dfb-bdaf-3618-b223-5774b8f56a8d | -20.90685 | -49.14149 | 2026-01-23 03:49:00 | NOAA-21 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 866f2125-3c68-3bf7-9af3-e5f575db1b96 | -22.60871 | -49.56572 | 2026-01-23 03:49:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ff1503b-6576-3447-bc24-6a753065b833 | -22.03959 | -49.50788 | 2026-01-23 03:49:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8ac02132-7f0d-3779-b002-1089771ed214 | -22.60692 | -49.57357 | 2026-01-23 03:49:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c57eee80-9faa-3c31-a88b-983e28b26223 | -20.84133 | -51.74022 | 2026-01-23 03:49:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b1762104-dc2d-314f-9426-75194a5dc2ac | -29.88947 | -51.23139 | 2026-01-23 03:51:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| c4253ba1-4382-3d7c-a8b4-cc64fa11d529 | -27.09929 | -50.52559 | 2026-01-23 03:51:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e02bc63b-0ea2-3fe9-999e-2c2e1a359347 | -27.56452 | -48.65989 | 2026-01-23 03:51:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d2c86fb2-4abe-353c-ae26-599a2b998345 | -29.88862 | -51.23487 | 2026-01-23 03:51:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a9f6b0cd-b10f-3fa4-b9a4-fee3157fef01 | -4.51789 | -38.42945 | 2026-01-23 04:12:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cfc95a21-a1e1-3b8b-9754-d03d16549ff2 | -3.48482 | -39.20736 | 2026-01-23 04:12:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64015296-c690-3cdc-8db7-e90c85aed607 | -5.09615 | -37.78762 | 2026-01-23 04:12:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb003274-7d5c-3678-9801-b2d017f764cc | -2.88346 | -40.50896 | 2026-01-23 04:12:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0acfc5b5-9156-311b-b13c-445d75b8f821 | -4.54166 | -40.16612 | 2026-01-23 04:12:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f40c6c50-94c5-398c-9471-3678425e9828 | -3.47797 | -39.2063 | 2026-01-23 04:12:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e62e8e36-89a7-3aa3-902c-b5fd4a3d617c | -2.98565 | -40.29392 | 2026-01-23 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa0ad5f7-41d0-3a6b-b88b-92181c5389a4 | -5.00741 | -37.53448 | 2026-01-23 04:12:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e35cdc8e-f293-3a57-885c-90152bbe6034 | -4.77109 | -37.81855 | 2026-01-23 04:12:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a6aaa518-4d46-3dbe-b814-436cc08afc9b | -2.91326 | -40.44975 | 2026-01-23 04:12:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 13173ea2-1162-327d-b02c-d868a2c2e412 | -6.30919 | -37.53509 | 2026-01-23 04:12:00 | NPP-375D | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1af0ab1-b034-350c-8638-dfe4d71b1d7c | -4.77478 | -37.81911 | 2026-01-23 04:12:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f7541c4-03f0-3460-9ae8-c638a9af758a | -4.5383 | -40.16559 | 2026-01-23 04:12:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cccecbf4-edbf-3c16-85cf-3113d9464918 | -5.00673 | -37.53897 | 2026-01-23 04:12:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 437e98bf-ad62-364f-a672-6bbdcacd1780 | -4.52145 | -38.42999 | 2026-01-23 04:12:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d5264c80-309d-3817-8f6d-8115df4cff72 | -3.41003 | -42.46191 | 2026-01-23 04:12:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e0ae119-6009-3af2-9337-9000f8bde230 | -4.20515 | -40.58095 | 2026-01-23 04:12:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 496603c9-cb62-3ea5-a58d-b3f73eb8c1e5 | -5.40865 | -37.8601 | 2026-01-23 04:12:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17271f03-6b59-3365-946a-a8965007d965 | -2.83518 | -40.23499 | 2026-01-23 04:12:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5903a0a6-f40a-305b-b414-fa2b6f0cd30e | -4.77176 | -37.81423 | 2026-01-23 04:12:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 86211a44-2daa-3df0-b2d6-ec22fc176ca9 | -4.07284 | -39.82397 | 2026-01-23 04:12:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ddb15091-6173-3ce3-a3fd-585e20214277 | -6.76411 | -35.18207 | 2026-01-23 04:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 492c2551-e88d-3074-bf95-bddf0f7c5fbe | -6.75961 | -35.18147 | 2026-01-23 04:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 91cd4f8c-8731-35e7-bf41-e709e4690eb5 | -3.53712 | -39.13929 | 2026-01-23 04:12:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d12306d8-fde4-33d4-a527-3e09dc867dd5 | -4.07339 | -39.8204 | 2026-01-23 04:12:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README3.md)
