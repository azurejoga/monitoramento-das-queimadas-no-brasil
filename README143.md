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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c05867f9-5309-37a4-8461-e6874bcaadb2 | -2.93561 | -58.39487 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8e958402-dab3-3098-93ba-0b3bf21349e8 | -8.98018 | -71.41093 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.4 |
| edeb7209-1fca-365d-a44d-63151f67c8e7 | -8.91798 | -68.86213 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b9d5be6-63c1-370a-bc11-4d4b6f8f440a | -8.23038 | -54.69484 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e20eb9b9-0d99-3889-b5fa-e9c79dbc653a | -1.32785 | -55.27996 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d332514c-b5ce-30ec-917d-673ed628b569 | -1.68001 | -55.05982 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8ae0f7b9-50fc-3091-864b-ae56bbcc6f14 | -1.9634 | -55.38585 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ad79949e-7aed-3270-918f-2205699d35d9 | -10.67001 | -69.53188 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8ec72946-7bd5-38c6-b8c7-35fd4e2d34d6 | -2.3423 | -57.11743 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 37d18e86-6706-3823-9910-adabaf89b691 | -9.6724 | -66.8278 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0b37e93b-7bdb-3c03-881b-f5561fb56294 | -3.17937 | -60.0667 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 555c129c-a977-37ff-a8f0-af50950cc718 | -7.23084 | -55.17711 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 84450323-693a-39b1-a91a-994ec416d8a7 | 2.27433 | -59.78788 | 2026-10-05 17:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cdc9ea7b-c10f-3d6f-b997-db0afb2013e5 | -9.13343 | -67.92804 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f46b656-4d76-31ef-a13b-50a5c2fbbaca | -8.65948 | -54.53848 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| b7ac2e5a-7efd-345f-8e20-7a5b3222e5e5 | -10.24918 | -68.30005 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8c21feaf-0b6d-3e78-a991-4960af3b5653 | -9.77133 | -64.98055 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8b213f71-3b37-3a85-975b-555b3d7a8232 | -2.34227 | -57.11882 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1d90a60-f4b7-337d-b485-ffee54e5911a | 3.56014 | -61.36217 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86c170d8-e4a9-3b85-8bfb-6ab75f8ae5d8 | -9.94778 | -68.99818 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9b5da94d-040c-3238-ba91-a0a01efa7a29 | 1.49805 | -55.64167 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 489811c8-3369-3aea-a9c4-811afb5596a7 | -3.48996 | -68.99017 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 97c0d7c8-ac18-3ee9-bf44-88e4cb13740f | -8.99515 | -65.69362 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 12fd3db3-127e-39a2-9476-3a460b3df20d | -8.64247 | -66.66792 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4db1135f-68dd-3637-8f99-b523da2b3bf0 | -1.22456 | -56.20629 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1eedf73e-e5a9-3c18-9c90-9f5fb1b1b23d | -8.72349 | -68.89884 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| f9b54ef5-f863-307b-8cb8-95ac3a0dca0f | -9.4739 | -64.3393 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bc7a5806-f394-32b8-8c6d-29afc15b49c0 | -8.58805 | -67.14233 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47a0a82d-4247-3f4b-945e-2d5f0aa343c3 | -7.22206 | -55.18745 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 38190bd6-0179-3224-b25a-a39924212cc8 | -9.00752 | -65.68768 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8b9213a6-9987-388d-b37b-7087e8b2b5f2 | -1.7801 | -53.77769 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9d570ec4-89f8-3b8a-9df8-9ff6235479bf | -2.53886 | -58.03074 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 14cb0689-9ade-38ea-8510-284791c0ebdb | -9.23336 | -67.86974 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 30d5e626-3b55-325c-9ff8-efa76c7d9a10 | -9.13523 | -64.37894 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bd044037-963c-3149-ae41-1476da170909 | -8.75463 | -68.97138 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0c2de6b3-7a9c-3938-9c64-982b97087212 | 0.43801 | -60.53645 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 2699c26b-0a18-307b-b18f-6adb9a0f8f5a | -8.89857 | -69.34834 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6e4bed5d-e8c2-3eed-b54c-88841fc127e3 | -2.53899 | -65.87054 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 7bc37f5b-1388-331f-8923-f24fd031274b | -2.77655 | -57.65844 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ff0e1c31-dc93-3e67-9b75-0a09f364f5af | -1.49364 | -55.67085 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 69ba22ae-16b8-3867-af6e-46e3bece33b4 | -9.1046 | -67.74779 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| ea0ebf60-40b8-35ad-9dba-ed20c84810de | -9.43685 | -68.05891 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c22abb05-6931-35c0-a29c-c399ec30d93d | -9.3393 | -65.8158 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4c955930-8d8b-3ed3-b024-a5bf5c374cb8 | -1.21978 | -54.54104 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8f51720a-fbf9-3df0-8346-5f0f98eb5e30 | 1.61191 | -55.78025 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4ed89968-8ea2-356a-94e4-c5e7cd94f365 | -3.40379 | -66.03452 | 2026-10-05 17:37:00 | NOAA-20 | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a69656f0-1267-3136-9ebd-5483f7f91e89 | -9.97569 | -65.05376 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e56aa655-6ab7-34ec-b3c8-780aa31f0d5b | -8.93131 | -67.34515 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 94d2f758-d13b-3ef5-9d58-2e56178c630c | -10.08831 | -69.17789 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7fd23ae4-8e55-38b8-92a5-34ec04c71072 | -9.11155 | -65.35085 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 93438a5a-1089-30f5-a622-7d3896c5387a | 2.09974 | -50.73685 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3055821d-cf2b-36cd-b2ee-a5e202f32984 | 1.98133 | -60.61128 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 6a0ecbb7-c5b4-32cb-ae17-465129fde6e8 | -10.56331 | -68.33942 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 759fe52c-6075-323a-a74f-30b884c87d51 | -10.11492 | -69.25406 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 70ec0a4c-9711-394b-9536-e28294077d92 | -6.45463 | -55.48742 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 02f37a4a-a2ac-3738-9ff3-7dea28e60e93 | -9.76718 | -64.98116 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e8594abd-cf19-35f1-8523-e4eaec5584fc | 2.73752 | -60.17529 | 2026-10-05 17:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71209657-a245-39a5-8c3d-e827cda82af7 | -9.24412 | -67.27908 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f175db5f-b663-38f3-9bc2-ec5e6ca5d65d | -8.86394 | -66.78132 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f1ce2934-f2da-3659-9fb8-0cca3e23c112 | -10.60208 | -70.0396 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9ce67afa-f538-3a98-96b6-40b737bbb199 | -8.97674 | -69.30412 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 7b472144-e8a3-37b3-9e6a-ad901565cace | 2.49043 | -50.934 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c0b82148-32ad-3231-8285-0c253f1de400 | -2.37019 | -55.27125 | 2026-10-05 17:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 87cf84c9-e32f-35f6-8441-3f297d2799a6 | -9.35294 | -68.79597 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 83adbc55-eea4-3b20-86bd-f0b6b2da5aa8 | -2.5468 | -66.08716 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe10da0d-5bc2-3985-874a-c2d9246c36fd | -8.83989 | -67.3917 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 07eacf4b-9787-31c8-824b-0c0d5db37c3c | -9.38634 | -68.32471 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b94c116d-1e20-357e-9f6d-bc24e4f3c038 | -9.53829 | -68.66448 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 43ff0e09-4a3b-39da-8d1a-536d73766c28 | -2.49049 | -56.82457 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e2291b0-3ffc-3dd3-bc60-9d01d211126b | 3.44901 | -60.40446 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9834bea-99cd-3bf3-abb7-2781b1c3bb66 | 1.81677 | -55.55296 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 472e3448-a4fe-32c7-ba8d-dbd80ff82a7e | -3.0866 | -69.20493 | 2026-10-05 17:37:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 5d20c8c6-b69d-35ac-a8eb-172e4e9f3d99 | -10.41762 | -67.98086 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 19.6 |
| acfb528a-13ea-3699-bf30-c82bbcb8320f | -2.78423 | -57.68339 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d37794f4-92ce-3f38-8a1f-c50e73e54542 | -8.66071 | -54.54568 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 5300d0ab-5ecf-32bf-a8dc-3a8a624638f8 | -2.56243 | -57.31411 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aca6cdb1-7f3a-3995-b48d-0dd5abfd55e3 | -9.00559 | -69.394 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca670730-9416-3ff5-9a66-1249d6880f3d | -8.64269 | -66.66992 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b38e5891-2b3e-3f8c-a02f-7d7c53144205 | -9.10258 | -67.69604 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 61366fe8-dac1-3eda-90a5-ef754f83ec10 | -2.64713 | -57.98122 | 2026-10-05 17:37:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3daf2284-1f09-3444-863b-f9c424c20fd0 | -8.63 | -64.11338 | 2026-10-05 17:37:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 16252d4c-6e7f-32eb-9ea2-baa9683c6fd4 | -8.32666 | -62.91828 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52657f61-940f-3090-99c9-2f55ea114af9 | -9.24547 | -67.28098 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 451e73b8-0768-36a8-96a6-0cf8df073639 | -9.4872 | -68.94733 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 75f9892b-cae8-3498-acf5-6864c5346d7e | -8.98844 | -69.3522 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4704cc47-cf4d-38e4-bc6a-c6a4e9bcc450 | -9.30953 | -68.34428 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f995fce7-7e1f-3c3d-bbba-0d544105ae48 | -9.06902 | -67.24184 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| bacca12e-c15d-3266-b797-a2e1b2feb5e0 | -3.01009 | -59.19369 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6705dd3b-9a66-3aa3-9663-41f3f975bfa7 | -9.29007 | -67.53525 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a7167041-db65-3ed5-a2ef-1714e2b7667a | 1.73511 | -55.62134 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f264884-0e1f-3127-a5a9-525b648ac874 | -8.54495 | -66.97676 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 72cf0f5c-05c5-3ca4-aa35-5c2a559aaa9e | -8.96019 | -69.3064 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 25.6 |
| fff8bc73-718a-34ed-b261-2cf052cbbb44 | -8.79471 | -69.24013 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b661e930-3ce4-3d4e-9369-ebe9f9457802 | -10.66388 | -69.11581 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d69dc4ab-2cb6-3012-981d-76b880c53b50 | -9.89591 | -67.33144 | 2026-10-05 17:37:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01728e4b-97cd-3adc-846c-7888fb5cc29c | -10.67222 | -69.10019 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 90cc1534-e82b-32f5-93fb-057a32887bd6 | -8.62454 | -66.98368 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 25b001b2-dfc0-35b2-9b52-a614072fd92f | -1.85226 | -55.80272 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b9aedbc-020d-3755-bd86-557c88bd086f | -7.23569 | -55.19605 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4d2b7384-6bd6-38bb-8c2b-a7c22f7a9363 | -9.14223 | -68.29651 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README144.md)
