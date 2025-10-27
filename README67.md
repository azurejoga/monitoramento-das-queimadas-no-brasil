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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 585457c2-8d33-3234-bb1a-d75ff37f15a4 | 2.51261 | -51.07684 | 2025-10-27 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6c7c81c-ad1b-3428-ad98-faa28d8f70e8 | -2.22356 | -48.37224 | 2025-10-27 05:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a211cb4-9ec6-358f-9842-9f9600d67f98 | 2.07053 | -55.70107 | 2025-10-27 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9420d199-9059-3d5b-adf2-c156cae61c06 | -2.32305 | -48.58452 | 2025-10-27 05:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 538c601d-7d78-34f3-919d-f396086be873 | 0.43401 | -50.82449 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 000f40f1-dd92-3130-8069-306ea259c3bd | -1.1876 | -53.38595 | 2025-10-27 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f97ffc93-073e-3479-bbbc-6821310a531b | 3.63987 | -51.83086 | 2025-10-27 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 730c2ace-6aeb-3bcb-861d-856774c879bf | -2.22589 | -51.87313 | 2025-10-27 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5febbbf1-2215-3896-a7cb-6ce6b5e55bf3 | 3.02501 | -51.4522 | 2025-10-27 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aa46260-7366-3858-a2fa-e21dc37ab7b9 | 0.4373 | -50.82025 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 68114657-ceff-3b03-ab52-2a1314952594 | 2.34804 | -51.54152 | 2025-10-27 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ac42736-a80a-36c5-ad62-a3def9c3030b | 0.43862 | -50.79049 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c103ad8-51bd-3609-8225-bbd5cd0303b8 | -2.25317 | -51.88797 | 2025-10-27 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57809927-e5c8-3bc5-83a4-076e2b0e1a7a | 0.43642 | -50.81459 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4a70959-e217-3ed9-947c-3aab41ab94b5 | 1.14737 | -51.07188 | 2025-10-27 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39937578-9080-3289-8dc2-345711c5eeb1 | -1.3837 | -55.34902 | 2025-10-27 05:21:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75facdc1-2cfa-3127-822c-8cd0c3ff843e | 0.43805 | -50.81811 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 11b32672-d42a-3db5-b825-0722f75343d5 | -1.23295 | -55.69262 | 2025-10-27 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91642ee0-80c8-38b4-a55f-473f97844d58 | 0.43818 | -50.82588 | 2025-10-27 05:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2e42ad13-a028-3593-a71b-21be79cc052a | -14.39841 | -51.54571 | 2025-10-27 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ff8c4b88-35ed-344a-8f5e-4833949a3f8a | -3.73761 | -52.43301 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e9bc7ec-a80e-30e5-a4d5-4d5fda2a0749 | -8.12172 | -47.03745 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cddc441-55c5-3dbf-b1ff-1efc4399764b | -13.29648 | -54.37526 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82de1bea-b8f7-3f0c-9429-c2e08365cc3d | -7.87521 | -47.25625 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9f4e0a6-fb0c-3e43-9024-180bfcfdfc0e | -13.30805 | -54.36093 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4185c711-a878-3d01-b786-8b070f6546f8 | -2.89827 | -53.13099 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fe2878a-085f-3aa4-8e50-3986f74572b8 | -14.84425 | -52.42775 | 2025-10-27 05:23:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee6c6e12-1d87-300c-8be6-2d919f02d8bc | -3.98209 | -55.74522 | 2025-10-27 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 344c9e85-627a-3e98-98ca-850d1350f5f2 | -3.07887 | -51.27535 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bc87794-b7ab-3696-a2f5-a7a5fa5bee1f | -3.24158 | -50.64976 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35e7708f-2d18-3ce5-b1e3-cc285aaf5d4e | -9.284 | -57.53765 | 2025-10-27 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa154454-9044-33cf-8589-e3b6b16db5d3 | -13.32447 | -54.38549 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011f37b3-4cd5-3e3a-b60d-955652bb3bc3 | -13.28362 | -54.39985 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d144a22-a09d-3e59-9621-138c458bcc9e | -3.12825 | -57.61602 | 2025-10-27 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6f9f722-7722-30ef-b079-1daa86a0356e | -2.7903 | -54.41874 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 61882de7-d767-3303-9be6-cbd9c6b4987f | -10.20574 | -52.6603 | 2025-10-27 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cca6e55a-4d2a-35fc-bdc8-91378a5b032c | -3.05948 | -54.61616 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00aecd8-39f9-3f2d-a1f9-791f4bf8af1c | -13.30737 | -54.36615 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 65cf9d07-66a4-333b-9fd5-42545d88dfb7 | -14.39792 | -51.54997 | 2025-10-27 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d864d93f-a153-386f-a8b3-bd54089fc632 | -3.98532 | -49.29205 | 2025-10-27 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 702d1cc6-7a66-3e9e-9dda-83fb7466ed4c | -13.29238 | -54.36935 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9c43b04-fe6f-309b-b7f7-90ab8cfa6854 | -13.29991 | -54.3863 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bedaf75e-1d39-3b23-afc9-5593317ed272 | -3.24225 | -48.77505 | 2025-10-27 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae4fcc3c-b1bf-332d-bd05-47c60ae1c11c | -4.87822 | -50.85911 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b19eeb79-389b-30e1-8a02-55abb5ecd329 | -13.32039 | -54.37817 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 11ebb305-16e4-34ab-bde5-5d0ad5254d39 | -2.90207 | -53.13606 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 184a411e-29a2-3374-afce-d42db25f934b | -4.15917 | -51.08471 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7fd63a9-7c47-3ef7-ba2d-8da71ce1e24e | -13.32161 | -54.36925 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fa0a8b4-b2ee-3512-b14f-88deefe778e0 | -13.28349 | -54.36288 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 766578ec-5bf5-3e4c-8ef4-353dceb0647d | -8.96045 | -47.19572 | 2025-10-27 05:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 78f30360-a782-3731-b69d-869d171b197c | -3.11635 | -59.11553 | 2025-10-27 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f8adda5-9275-3152-b420-1e7b2b5e5b1b | -3.8617 | -49.8032 | 2025-10-27 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2e0a54-1477-3f02-a9f9-de45e3d3410a | -3.2411 | -50.65305 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f509baf-1490-3317-a97e-3df20b7bf9ed | -7.33445 | -47.14508 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96d30913-b7d3-3409-9c4a-e46021913393 | -4.96882 | -56.2781 | 2025-10-27 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71c20fde-aec8-305e-8b16-9abbd73666cd | -3.26032 | -52.58785 | 2025-10-27 05:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 758d342d-05c7-33af-a2f4-89369d6460bc | -3.11689 | -59.11208 | 2025-10-27 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2234f10-4d30-3474-9ee2-3d5be0b1594b | -14.82659 | -52.43424 | 2025-10-27 05:23:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d06d599-72bc-3121-96cd-530608929719 | -3.25161 | -50.03909 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b17df668-577a-311a-b381-a99ae5dc2878 | -8.10033 | -47.06354 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d974bdad-e6b6-328f-8421-d916e039b303 | -8.69626 | -50.8139 | 2025-10-27 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8fbc7b0d-917b-35b9-ae6c-b99e01aea8c4 | -13.28827 | -54.3635 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f913553-dd5b-3d9d-909f-8c5f39baee4d | -13.30469 | -54.38687 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32e7291c-1ee0-3f70-8086-b71ffc90e381 | -3.46958 | -49.97342 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9e84ad2-acea-37c4-973e-66377d476951 | -13.28838 | -54.40055 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a2f0ac4-ae39-3be9-bad3-b96891703555 | -3.81222 | -51.78394 | 2025-10-27 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c519401f-4b39-35ce-a4ec-69196fd8c174 | -8.05935 | -54.92685 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cf66ad7-f946-3bde-afee-19fd72532946 | -3.23579 | -50.65221 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4ac354b-04a0-3337-9d08-a3f34359b9f1 | -13.31493 | -54.38284 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94858a14-5d4a-39f9-82cb-1cfc555e27e5 | -13.26781 | -54.37157 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 939b9b18-096d-3f60-af10-a9d37264a441 | -2.12701 | -56.84611 | 2025-10-27 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 599ec3e5-798b-3a80-82c6-6ec0dcb24f44 | -3.83943 | -55.79537 | 2025-10-27 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dff6429-2d6c-3fea-9c85-3c52a834e413 | -3.09369 | -49.45348 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437fb4ee-84ac-36f0-9667-5ae680b83587 | -7.24672 | -46.95974 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6c5f8161-9e88-36e2-869b-2bf05e092d4c | -3.11428 | -51.21315 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2938dce1-64f5-30f7-81bb-40c69fad422d | -13.25416 | -54.36433 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 61938b37-2122-34bc-b033-3ed2410a9dda | -1.94027 | -56.76651 | 2025-10-27 05:23:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d759bec-2c56-3f50-b72d-8292c0bd8c7d | -3.05044 | -53.01955 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0cb5aaa-2e7b-3a04-907f-f4fab7710213 | -13.30058 | -54.38111 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87c08268-6f40-3072-acb1-09344ec166b9 | -3.09942 | -49.45442 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a580b18-d7f7-3030-a066-19cb47ebfe05 | -9.13739 | -51.30357 | 2025-10-27 05:23:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1c238c31-be31-324a-96d5-88611302a907 | -13.28283 | -54.3681 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bedface1-e4b4-3c47-9ae0-1c304f708f5e | -8.22037 | -46.94297 | 2025-10-27 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dbdb24b-8083-3528-a0f0-aa44737429b1 | -4.3524 | -50.33124 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee3cdbf8-a4fb-381c-8310-9fadd547d56e | -3.97617 | -56.09049 | 2025-10-27 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d718e66e-1795-3374-8f09-a5614c71f8f0 | -3.97926 | -55.74282 | 2025-10-27 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a44c81f8-7fdf-34a8-8727-3bef4d0f4058 | -8.12611 | -47.03066 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 388d83b9-7322-305c-87a4-ef2d112f1043 | -8.05509 | -54.92623 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71b17595-9cf9-3321-808f-6aecf5027a04 | -2.67985 | -54.65168 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36ad6d20-cb25-3f44-996a-c132d79177f9 | -3.86597 | -50.88983 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa2f0c9f-7eb2-37ac-9e0d-e7ead855d859 | -13.28904 | -54.39538 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cba2da4c-1b6a-3501-9424-0820348c4dfd | -3.10118 | -49.4492 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18cf7bcc-6a96-37e9-956c-a01e28b476b0 | -4.35739 | -50.3356 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f070757-5aa7-3f5a-9e58-2913972849fb | -3.10066 | -49.44632 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 104cdedd-a339-368b-bae6-b3be540c2a08 | -13.31696 | -54.36722 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dac13817-c15b-32a4-aece-d602b53c9a1d | -7.06359 | -46.75336 | 2025-10-27 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b194c89f-2ba0-358e-8ee3-a5e83229204a | -5.71968 | -49.28494 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6878739-9344-3235-8bfa-f02f7b1a90d0 | -5.77382 | -51.56445 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40767a5-0c58-308d-bc75-46ae0f16ab7e | -8.0696 | -46.9591 | 2025-10-27 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 557ff705-e4ca-3df3-b8b6-364217b413d8 | -7.94648 | -47.242 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README68.md)
