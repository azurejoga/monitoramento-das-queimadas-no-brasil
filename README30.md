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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1382fa8-c938-3de7-97a0-83fdedf97daa | -12.8893 | -53.5194 | 2024-10-14 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b6924ea6-429a-30fe-ba39-acd9cd6450fc | -17.1758 | -57.479 | 2024-10-14 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| ec4d5b4f-23c5-33c2-8798-a1c61e43c2b5 | -17.1764 | -57.438 | 2024-10-14 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| bf7d0a59-382c-38e4-8451-4a36e0e500dc | -17.1954 | -57.4767 | 2024-10-14 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| f98cf122-629c-3e00-adc7-4d2cc8bbea6a | -17.1957 | -57.4562 | 2024-10-14 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.3 |
| a607aade-3ec1-3f6e-83a7-dbf5b97bd9ed | -17.196 | -57.4357 | 2024-10-14 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.6 |
| 87ac638d-2a5b-3bc5-a941-6fded0e27337 | -17.2154 | -57.4539 | 2024-10-14 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 997645f5-b343-30c2-b8d5-155b26322c6d | -17.8651 | -57.3964 | 2024-10-14 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| b5d6c329-49b3-3174-9abc-3acc4343bc98 | -17.8655 | -57.3758 | 2024-10-14 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| d6a0269c-6e10-3560-8685-df5a4ee36815 | -17.8849 | -57.394 | 2024-10-14 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| b5ec0bd6-1f5c-3302-ae56-9852c7b6d2ae | -17.8852 | -57.3734 | 2024-10-14 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 6c484aaf-092a-32f6-ba3a-8c35d78e59cb | -17.8856 | -57.3528 | 2024-10-14 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| db24bc90-26ec-3981-b44d-fc9ce9a4b4f7 | -18.0039 | -57.3588 | 2024-10-14 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 5aab7be0-8ffa-39e1-845f-9cecb662c669 | -18.0042 | -57.3381 | 2024-10-14 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 208a08dc-eb03-3b57-b78f-c7fbfaac7334 | -18.0236 | -57.3563 | 2024-10-14 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 99872d5b-d955-37e3-b217-e9e55cbdab5c | -18.1905 | -56.8394 | 2024-10-14 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 57ad88bd-4a96-3422-956c-77b915e24a5b | -18.1909 | -56.8186 | 2024-10-14 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| ba7dd364-81b9-3777-a3bb-bf2b11c2becc | -18.2104 | -56.8368 | 2024-10-14 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| c826b1ea-7e5c-38c6-92f8-87a3ec1563b5 | -18.2107 | -56.816 | 2024-10-14 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 469456ce-668d-30d2-976a-a4f2d588ab39 | -18.2555 | -56.5196 | 2024-10-14 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 47c52ad2-63d3-30b2-b452-495cad336553 | -18.2559 | -56.4988 | 2024-10-14 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.6 |
| 912ccb00-de8c-33ac-8d53-bf2bff3d66a4 | -18.2562 | -56.478 | 2024-10-14 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| f0f14430-91dc-36ca-93cd-95333a447237 | -18.2757 | -56.4962 | 2024-10-14 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.2 |
| e416ac9f-36c0-34a9-80bd-0c77a1258ca1 | -5.714 | -35.50353 | 2024-10-14 03:28:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5e89bd7-05fa-3be9-8433-c2f09b778bf5 | -6.74257 | -35.26447 | 2024-10-14 03:28:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46a8e01c-4537-3921-9e07-1a6cc9d21e52 | -7.47444 | -34.84417 | 2024-10-14 03:28:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6afff5eb-f302-3434-bc84-2ce2d98fd8e7 | -7.46515 | -35.08049 | 2024-10-14 03:28:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6d5f1810-a86b-3fe3-a04c-cd34e956b4e6 | -7.26892 | -35.12435 | 2024-10-14 03:28:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d00a3be-f8a9-3184-96b5-0f0c39872c0b | -7.26536 | -35.12374 | 2024-10-14 03:28:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4c0c74b5-7eee-3658-87a7-0cce4f338bba | -6.75343 | -34.97418 | 2024-10-14 03:28:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 54b5bd66-5356-3713-8a1e-769044ff52a4 | -8.12533 | -37.5749 | 2024-10-14 03:28:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d60f8dd0-be46-3308-87c0-e208223bb1cd | -8.12472 | -37.5785 | 2024-10-14 03:28:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 435f5d0e-209b-3d02-83eb-2a9819a3f76d | -4.82899 | -37.83863 | 2024-10-14 03:28:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84994a87-960a-339c-8f71-9fa4b753db15 | -4.38042 | -37.906 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 05691401-3128-3b48-8d8b-83c3742c6db8 | -4.37672 | -37.90093 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ec69c336-6150-38f0-9d15-6bd461286ace | -4.37601 | -37.90525 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 128b2d0d-e856-31de-bd19-bc83026bf571 | -4.3753 | -37.90958 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| b47a403f-e415-3586-b1c9-bd0774f74ff0 | -4.37459 | -37.91392 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 145f5cde-ea16-370b-b863-ce9ca57dc311 | -4.37161 | -37.9045 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 06f459af-857a-3351-ba35-812b7cae6968 | -4.37089 | -37.90885 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 79461150-6c29-3c31-9d53-250510f9068a | -4.37018 | -37.91319 | 2024-10-14 03:28:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc573cb7-e51c-3189-b66c-47b67afad0ab | -11.17769 | -39.90213 | 2024-10-14 03:28:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 945d63e4-d9bb-3dbe-a921-c08d6926ea1a | -11.17687 | -39.9067 | 2024-10-14 03:28:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6de4b266-f2ae-3aeb-90b7-411ebd1bb23c | -11.17604 | -39.91127 | 2024-10-14 03:28:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d34a492-a175-3792-bdf4-884d9799b50f | -11.17154 | -39.91041 | 2024-10-14 03:28:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db29967d-ea05-3cf0-9a67-2021561edc1b | -4.78187 | -39.77486 | 2024-10-14 03:28:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f3dc51e-06c7-36c9-8837-5e82bc63d5c2 | -5.95192 | -39.67987 | 2024-10-14 03:28:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a0de61bd-a5e9-321c-8931-5db9d283314e | -7.81773 | -39.4694 | 2024-10-14 03:28:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1472feb-a4a3-3983-ab27-ffaed5035433 | -7.81689 | -39.47433 | 2024-10-14 03:28:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2336f2e-be58-3eaf-b1ee-4ce3f07ef8eb | -7.81676 | -39.46693 | 2024-10-14 03:28:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b3ad5cf-beaf-3d7c-b275-cdc4d900d541 | -7.81588 | -39.47184 | 2024-10-14 03:28:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 711bbd1a-b9f0-38b0-93e4-6266a69e5129 | -7.81311 | -39.46854 | 2024-10-14 03:28:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1464b501-e0e6-38f0-a46e-fbbb1abcdbc7 | -7.71052 | -39.35271 | 2024-10-14 03:28:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c7cb15e5-fa47-3197-a5e2-50b1a2f6cdee | -7.51946 | -40.51615 | 2024-10-14 03:28:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8aedcd2f-7b98-3e67-9460-445603e13687 | -7.51899 | -40.51884 | 2024-10-14 03:28:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb228cce-c78b-33f6-97eb-0034250deb55 | -7.51399 | -40.51794 | 2024-10-14 03:28:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f39756dc-628e-3553-a863-bf7dabf1db53 | -7.51352 | -40.52064 | 2024-10-14 03:28:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 84b17851-88f0-3c84-952e-123493bf6e07 | -9.31382 | -40.62282 | 2024-10-14 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27bb16c7-133e-328d-92b5-d978aac07c46 | -9.10676 | -40.65497 | 2024-10-14 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0265bef9-e846-30a4-b5b5-e3dad4b955df | -8.51017 | -40.24334 | 2024-10-14 03:28:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce532970-b5ec-389b-9024-d106332c885e | -8.37685 | -40.27253 | 2024-10-14 03:28:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7771766e-6cc5-3543-9246-535a2d022d94 | -8.37202 | -40.27157 | 2024-10-14 03:28:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 745bf8f6-b0ee-37c9-95e7-2e81d73bdfd1 | -9.6283 | -40.35094 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e36dbb6a-9967-35e6-a3c2-2d108460eac9 | -9.62894 | -40.34804 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8f737590-14ab-3e09-9c53-703745e8f313 | -5.12903 | -41.71134 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b77f16b5-9c73-3a36-be30-4a3bc8387ddd | -5.12408 | -41.70639 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f13bd0b6-a938-31d7-9f46-4d20197b4970 | -5.12243 | -41.68239 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 084426cd-b602-3065-8362-b8358a3d90cd | -5.12206 | -41.71808 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5897180a-bec5-3063-9671-ca97581315dd | -5.12178 | -41.68616 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5ccb2192-524f-303b-9c42-345b31233bcd | -5.11979 | -41.69763 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d4078fc-4059-35f2-938d-555e89901f44 | -5.11845 | -41.70536 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f172f18e-e98c-3d05-ad56-9f9eb3ea547f | -5.11708 | -41.71325 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 38c7dc07-2c30-39b0-8b60-a5c6b8873d5d | -5.11683 | -41.68127 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 32dd764e-21dc-373d-917c-5a15d60f45f1 | -5.1164 | -41.71719 | 2024-10-14 03:28:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0228e7a5-bb2b-3933-802f-8f5840cfbecf | -8.50257 | -41.40662 | 2024-10-14 03:28:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 549c0863-5c68-385d-a990-c0d49433237a | -8.14134 | -42.33 | 2024-10-14 03:28:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b20f442-3d59-3f26-88d3-a2e129a220cf | -10.48983 | -42.442 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ccd9bd94-68a2-313f-99ba-ce20a719c395 | -10.48919 | -42.44542 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| bcb04d57-cd7e-332b-a7ae-99bf5e5da8f2 | -10.48507 | -42.43759 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 0dc90644-a5d3-3935-a2ee-92df3aaf9e60 | -10.48442 | -42.44104 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 64d6a63a-0845-3ae9-beec-b1460e7ff1b7 | -10.48377 | -42.44448 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 003206d7-f01e-3d17-9aee-7c01670919ff | -10.48313 | -42.44792 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 93f15e95-15e9-3af5-8397-a8720cd7e187 | -10.47901 | -42.44008 | 2024-10-14 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3ae8d0e-1820-3d9d-aed3-a42190930d91 | -3.30966 | -42.83162 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 453d335d-49eb-39f8-b69d-e7ac0c1d18a8 | -3.30882 | -42.83654 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7455834c-151c-3e0c-9465-6377d50c6620 | -3.30799 | -42.84143 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8410615a-44c1-3911-8b61-c5530a93dc22 | -3.30716 | -42.84631 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e81a8375-c3be-3cd1-a4c9-dbc6089a1a13 | -3.30632 | -42.85123 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 213ce6a8-e475-313e-a81f-3db7770ce62c | -3.30548 | -42.85614 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 649ded93-381d-3e05-8d46-ca6b3d88f162 | -3.30345 | -42.83049 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 446f3661-4194-3c78-b12d-604733c930e0 | -3.3026 | -42.83542 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ee11e191-1a38-3872-80b3-a7f6c4a36243 | -3.30177 | -42.84031 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 163914c5-7bfb-389a-bd44-c76c553e3526 | -3.30093 | -42.84519 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 15d28cc1-545d-3b7f-9b0e-88b94c26b45a | -3.3001 | -42.85009 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d36d24ab-f6e6-376d-ae73-369f8c7132e6 | -3.29926 | -42.855 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efe59b53-8d02-39c6-ac83-5ac56757f2c8 | -3.29639 | -42.83425 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3cc974b1-3220-33c4-8ff8-b5cc9026d0ce | -3.29555 | -42.83914 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 49cf1234-005a-3489-8aa1-195bd7c9cf18 | -3.29471 | -42.84404 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e29dba94-88eb-34b3-b2ac-971c377f3ebb | -3.29387 | -42.84896 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 201818e8-cf1d-3e80-b98d-e68f21ec7fcd | -3.29303 | -42.85389 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README31.md)
