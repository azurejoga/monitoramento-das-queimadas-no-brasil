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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60b8ea66-fdf2-37df-beec-27e105dc2fa2 | -9.0429 | -65.4361 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2a469525-4f82-307e-9e3a-fd82d71d20c5 | -7.6805 | -69.9395 | 2026-10-05 16:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8d1d7f56-dd0b-3eeb-b783-139ba42997dc | -9.1445 | -67.7577 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 0fd7f649-67cf-3431-a66b-d705e7e68bbc | -9.4819 | -66.7836 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 498bb456-b642-3a5e-8366-18a5a3b9e978 | -8.5733 | -67.1422 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 03e0d86e-c79d-39a1-acc9-05e1b47d4c06 | -7.364 | -72.6079 | 2026-10-05 16:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 04f9ee98-a1f3-304a-8c30-901a5c9bc349 | -10.2546 | -68.7494 | 2026-10-05 16:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 87963658-c28e-3ca3-9670-056e3807a8c8 | -9.1221 | -64.4031 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.2 |
| a5fe9890-1e54-3383-8c8f-bd3d1e84a34c | 1.8399 | -55.8218 | 2026-10-05 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 77970567-57ff-327c-8900-2f4987df3e7a | -9.0341 | -67.5567 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| e0fa4b18-f5d8-3230-8523-010ed1c3c7e4 | 1.7487 | -55.6256 | 2026-10-05 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7dcbd26c-b1ac-3d65-8e97-f6634865bb26 | -9.4751 | -64.3336 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ee98ce9b-b8ef-3290-9545-178ebfe81b4a | -9.1332 | -65.9373 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 401aa1d3-efd5-3631-9539-b4b629636e9b | -7.7127 | -73.1158 | 2026-10-05 16:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 174.8 |
| 758dddc7-cc7d-3135-8cd0-a191292806d4 | -9.1244 | -68.2021 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0e469dbb-64ca-3d91-a881-fb056d3d7baf | -9.0046 | -65.6988 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e32ebc69-f661-3bca-9306-3ab6bdc65f16 | 1.8767 | -55.7621 | 2026-10-05 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 22048725-28cd-36fa-b089-f3d68189b12e | -9.1335 | -65.8813 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7f73133e-6656-352d-8a8d-2f892d3de4fc | -9.1442 | -67.8317 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a23f18be-9655-3e2f-991e-7c9618118a34 | -2.5353 | -65.8819 | 2026-10-05 16:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 78809309-5a81-3e97-848a-f093ab9525b2 | -8.593 | -66.8081 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| b03cb8e9-8f80-3955-aff0-7b9442bfa062 | -9.0585 | -66.0887 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| e882feb7-cbe3-36f7-95ab-300408c3c4ca | -9.1408 | -64.3836 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 017e1836-86bd-326e-93d6-90f0ae3c4150 | -2.5353 | -65.8635 | 2026-10-05 16:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| a5213012-eea7-3993-a543-a25d8dfbecae | -9.1072 | -67.8326 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 49f79e46-d543-3998-aec0-aa6f340c5e64 | -12.446 | -62.4607 | 2026-10-05 16:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| eb7c37a3-3985-3b00-ac2d-f1e9b86b610c | -9.9175 | -65.0313 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2a553b41-cb8d-3c1e-86a0-0de08fb05c37 | -8.5918 | -67.1418 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 856b98c4-ac53-3268-b08f-329924a4b253 | -9.1148 | -65.9192 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 31124852-8ee2-3eeb-9e3b-808a7dd589d7 | -9.1076 | -67.703 | 2026-10-05 16:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| afe0954c-14dd-3871-bb6c-65215028b47d | -9.1407 | -64.4024 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 07fd6c21-cd0d-3a5d-a3f2-d7ed208cb2f3 | -9.9174 | -65.0501 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| d80a280d-0476-3dd0-9b06-f8669fcab3bf | -8.6293 | -66.9926 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c81192bd-cafe-3fc9-aab9-8507f4e5b663 | -9.7499 | -65.075 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 81fc25d9-ca4c-3a31-9864-4f4af9c1a4a5 | -9.4565 | -64.3344 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fb6d89d1-0e03-3301-a54c-a34fde79cf19 | -9.0045 | -65.7174 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 147e0657-5faa-3dad-ba42-2adc73d1efbd | -9.7126 | -65.0951 | 2026-10-05 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a6d2c5b5-668e-37e9-a75d-a31ee67fdcb0 | -8.5929 | -66.8266 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0e59b847-b051-304f-9189-1938be49ace1 | -9.1147 | -65.9379 | 2026-10-05 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| dcabaaef-eb07-394f-a29e-0d027053e03a | -11.69 | -43.64 | 2026-10-05 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89334137-c2fd-3566-8f02-fd715d3909c9 | -6.69 | -45.22 | 2026-10-05 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d18cb36d-65ef-3e8b-95bc-2023db8635ca | -4.81 | -39.98 | 2026-10-05 16:15:00 | MSG-03 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e3144f19-b92a-381a-982e-437ad5f08146 | -4.78 | -39.98 | 2026-10-05 16:15:00 | MSG-03 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8382ba4a-bcd4-3973-8161-eb718d7c01f2 | -6.9 | -43.69 | 2026-10-05 16:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1635210-a30f-34f7-8870-5bc54edc89e5 | -6.69 | -45.27 | 2026-10-05 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f87a0d32-c2d7-3058-8c77-c7c99592ae99 | -11.69 | -43.68 | 2026-10-05 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b764be7-7302-34ca-814c-ad569dd6fa86 | -7.83 | -45.31 | 2026-10-05 16:15:00 | MSG-03 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4c1e27e-317c-344a-950b-7987500c436a | -11.66 | -43.63 | 2026-10-05 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56759707-543e-34f6-acc8-a6c950575d55 | -6.72 | -45.23 | 2026-10-05 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3c4f0d0-8c0f-3927-b600-e69693bf5998 | -6.61 | -41.6 | 2026-10-05 16:15:00 | MSG-03 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f8b0daf-b75f-30ac-92f4-0ee6ed8641c2 | -9.1221 | -64.4031 | 2026-10-05 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1a886f52-442e-331d-9ea7-7180daa0224a | -9.0232 | -65.6982 | 2026-10-05 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5a4a6fbb-598c-386f-ae22-0f1e2a250ce7 | -9.1408 | -64.3836 | 2026-10-05 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 57540ee9-47f3-3138-b711-db5659a4c1fa | -2.5353 | -65.8819 | 2026-10-05 16:20:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7c1cc711-d4d7-30f2-8c3b-e83c9f164866 | -9.1243 | -68.2206 | 2026-10-05 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b60a924b-af7e-3104-8751-87b18d63f82b | -9.0045 | -65.7174 | 2026-10-05 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 43490cc0-8623-3358-bd3d-46edd5da24f9 | -9.1072 | -67.8326 | 2026-10-05 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e926cd6d-b425-3086-960a-0794f24511d1 | -9.4819 | -66.7836 | 2026-10-05 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7a870ecc-288f-38e0-9479-a4b980c069d1 | -9.7126 | -65.0951 | 2026-10-05 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 78743fdf-eb6e-326f-af49-ba60a0147210 | -8.5554 | -66.9945 | 2026-10-05 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 78d904f7-8b16-36ff-a6ac-86f80b888ac5 | -7.6805 | -69.9395 | 2026-10-05 16:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a29d4f3e-4662-3a5d-b33d-b8509c4f4e5f | -9.1438 | -67.9428 | 2026-10-05 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d637f24d-bd69-3093-858f-c3ef1fe57bfc | -9.1253 | -67.9432 | 2026-10-05 16:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 89d4c650-c443-3acf-ac42-ace1d5137214 | -9.1221 | -64.4031 | 2026-10-05 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 90728a67-849f-381c-808f-b4aa3518387e | -9.0045 | -65.7174 | 2026-10-05 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3afea998-ea27-3f0b-883b-f4ba34cc8dc3 | 1.8767 | -55.7621 | 2026-10-05 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5a20c4d4-342c-3e7b-b599-4497c77b79e4 | -8.5918 | -67.1418 | 2026-10-05 16:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| aad4e63a-a382-3396-af7c-cae8e354f75f | 1.8766 | -55.7819 | 2026-10-05 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8e47ddaf-9e86-36c2-b3b0-3ec4b33ede89 | -9.1147 | -65.9379 | 2026-10-05 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 128e7528-199c-3bdf-839e-bcf09374fb66 | -11.8814 | -64.9323 | 2026-10-05 16:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e378da2f-a8c9-3131-85fa-e0dd6ba142c3 | -9.7499 | -65.075 | 2026-10-05 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 597b7147-db71-36ad-a8c2-615edbbf43e0 | -9.4819 | -66.7836 | 2026-10-05 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fc7c353a-3eb8-3f60-ba9e-8da9798ccfaa | -9.1408 | -64.3836 | 2026-10-05 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| eb8cc207-d42b-37c3-b7aa-e9f739b8c508 | -9.1037 | -64.385 | 2026-10-05 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0be5a1be-ab6a-3b63-b60d-eae5503a30c8 | -8.5733 | -67.1422 | 2026-10-05 16:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e90959ed-2518-3db1-95a0-64a60f29add1 | -7.7127 | -73.1158 | 2026-10-05 16:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a1f7106e-5b34-37e2-a687-454f513819d4 | -30.00874 | -50.67252 | 2026-10-05 16:33:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 8.0 |
| a3018766-6c13-3909-9943-e2e64439c301 | -30.01102 | -50.67426 | 2026-10-05 16:33:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| e87e098b-1a51-3997-864e-db6726108ba3 | -14.21495 | -40.44757 | 2026-10-05 16:35:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5e273ba4-d1e4-3703-b39b-95af92fd09c7 | -15.19026 | -42.12619 | 2026-10-05 16:35:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 99e27b47-ab55-3bbe-b33d-216c32704424 | -16.58609 | -41.54148 | 2026-10-05 16:35:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| af13935a-6184-355b-bd5a-6bc760354fd0 | -14.8375 | -46.68604 | 2026-10-05 16:35:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbc870b7-529b-32d3-b77d-35ce8cfc822d | -14.51657 | -43.8322 | 2026-10-05 16:35:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f8cb18b1-b36e-3808-a49b-ca9b8b11271f | -14.20323 | -43.95891 | 2026-10-05 16:35:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 95e7d24e-8765-30f2-be43-43904ed39e47 | -14.9243 | -41.43693 | 2026-10-05 16:35:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ec4e2fbe-75b0-328a-ac33-fb0e470a5c2c | -15.85269 | -45.15054 | 2026-10-05 16:35:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8351e573-d5a8-35e7-8c64-82ae825a3f54 | -14.0498 | -42.49305 | 2026-10-05 16:35:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 03a96943-6338-3abf-a057-532b559825f7 | -15.84939 | -45.15108 | 2026-10-05 16:35:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8ea720e7-e2b5-3b0c-9d80-ffe7ff3d850c | -16.4041 | -39.42302 | 2026-10-05 16:35:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6e9d264c-b23c-36e1-b1bc-06142d4b6811 | -13.74718 | -41.10619 | 2026-10-05 16:35:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| bf7cb2b6-0dc6-3cd5-b382-3fb17f80cc4f | -14.55215 | -41.28474 | 2026-10-05 16:35:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 99b6ecd9-2b69-337c-a6e1-3fae71d8c28b | -15.69394 | -39.78674 | 2026-10-05 16:35:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| dd759f18-c04d-346e-8a34-035dbef9c8c1 | -14.69259 | -44.2969 | 2026-10-05 16:35:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1e21e18-7deb-32f1-8ef1-19159b4304be | -14.30392 | -40.42989 | 2026-10-05 16:35:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 837eb664-8853-3759-a0a2-9bfb959951d1 | -16.34872 | -42.04005 | 2026-10-05 16:35:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 96381f34-d86c-3b56-b082-8a7c0754d6cd | -16.32172 | -43.74147 | 2026-10-05 16:35:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97223a4c-5111-3b78-a625-43a041123f9f | -14.89839 | -44.2436 | 2026-10-05 16:35:00 | NOAA-21 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e025054-4c00-36ba-ba2f-da1175812102 | -14.92809 | -41.43631 | 2026-10-05 16:35:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c6b876a3-52ec-3e33-9254-0f8d3079e00c | -14.13034 | -41.20166 | 2026-10-05 16:35:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 830eaad8-4248-3a35-96bd-e73114e4ecb0 | -14.82147 | -41.27172 | 2026-10-05 16:35:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |


[Clique aqui para ver as próximas entradas](README79.md)
