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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 786d5b14-8d0f-32f5-a799-773c7bca5728 | -5.9938 | -43.7366 | 2025-07-03 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cc0293fb-97a3-300a-98c9-47434d9d230d | -6.9602 | -42.9052 | 2025-07-03 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| eb7a5578-d3ce-3dc0-8fb7-57861c7eb241 | -6.2943 | -43.6891 | 2025-07-03 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 485da022-9b29-3204-a8b6-1040bb0d0a6c | -6.9605 | -42.8816 | 2025-07-03 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 268.5 |
| 79a4a7f6-fcbe-3bfe-9dfb-f87612be4dbe | -6.9416 | -42.8834 | 2025-07-03 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| f4b0d24a-9199-3997-8acc-fc136bbbf594 | -6.9605 | -42.8816 | 2025-07-03 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 233.1 |
| 3f7e2f63-ac7b-32f7-b9f5-fd493146a958 | -6.9416 | -42.8834 | 2025-07-03 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 19942a29-c171-3e44-99a2-fa2c210470eb | -6.9793 | -42.8798 | 2025-07-03 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| c5d22dd6-eec9-3dce-8f75-36b37b051056 | -5.9938 | -43.7366 | 2025-07-03 05:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a2f7e0f5-c0f8-391e-a199-ebab99ea3620 | -6.9602 | -42.9052 | 2025-07-03 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 9ac020d3-b8fe-348a-b70c-12aeb8a3f2e5 | -6.9607 | -42.858 | 2025-07-03 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 1109da9f-302d-3c8d-ae78-b149b7b47bee | -6.9602 | -42.9052 | 2025-07-03 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 0315e538-8c84-35e1-956a-c23a992d27b7 | -6.9793 | -42.8798 | 2025-07-03 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| e6bc7f0b-237f-3603-ba16-705b960dc51f | -6.9416 | -42.8834 | 2025-07-03 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 1762d1cb-a98d-3457-9c4b-d04daba2c63a | -6.9605 | -42.8816 | 2025-07-03 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 216.1 |
| 3b7d740c-4ba7-37cb-b729-d4f574d00a85 | -5.9938 | -43.7366 | 2025-07-03 05:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0f72475a-622c-35f0-a55c-6e9aea6b6e80 | -6.9605 | -42.8816 | 2025-07-03 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 224.7 |
| ca9c4cfa-224d-3674-8a33-5f065bf7177e | -6.2943 | -43.6891 | 2025-07-03 05:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c04ccb7c-67d3-3c6b-ba74-2f410859aed8 | -6.9416 | -42.8834 | 2025-07-03 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 962a63cf-22e6-3580-b4c0-78389954e45a | -6.9793 | -42.8798 | 2025-07-03 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| b0f91ed5-114f-3d22-b81b-ee9dbf9a24bf | -5.91854 | -61.30443 | 2025-07-03 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda8f300-ac2a-3b17-ab9a-32ad04f6365a | -6.53971 | -55.04878 | 2025-07-03 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4867233-7b5f-30cb-8057-cc911d6f3e3b | -6.54176 | -55.03292 | 2025-07-03 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f448fd5d-b6e3-31c2-bc4b-9fa836c310d3 | -6.9605 | -42.8816 | 2025-07-03 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.3 |
| 59f81753-e47c-38eb-8221-ae940e004940 | -6.9602 | -42.9052 | 2025-07-03 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 52f06e1a-d94c-355e-b61e-4382bea29b50 | -9.08963 | -59.48277 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70ecc991-0c4d-3b3b-b816-f8e203656dbe | -9.22401 | -67.90857 | 2025-07-03 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acdfa902-4e1b-30b4-bd08-8835b5cea6b9 | -9.63422 | -61.464 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc60008f-9ce1-3e8b-a708-dde3c7865e98 | -9.63375 | -61.46109 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a3c3cb57-af2d-33b1-b24d-17cc24cb45ea | -9.63315 | -61.46538 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b246d3e9-9a49-3575-82eb-8ff853ff7425 | -9.62927 | -61.46768 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f4a5b22-b73e-35bd-9f9e-e8a0b10668f3 | -9.51571 | -65.58572 | 2025-07-03 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87966b77-a498-33b5-b1d6-8fc9cf7db8ec | -9.84177 | -63.67012 | 2025-07-03 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac2f2ce6-4642-3003-874f-3991d6278bc0 | -9.63365 | -61.46829 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7ba6c10-4526-3b6f-87a9-723b9fbdde1b | -10.89374 | -56.45755 | 2025-07-03 05:50:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c8cb6c4-076a-38d7-92d0-057c5a379f7e | -12.05164 | -62.99122 | 2025-07-03 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54b7e2f6-8faa-3a7c-af3b-632b3e98bd07 | -8.72137 | -64.17234 | 2025-07-03 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df0fe0d8-9735-3ef2-b93e-004addb4bcd9 | -10.30737 | -57.14008 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c18fa43-c481-34d8-947d-43012477ebaa | -9.63254 | -61.46965 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ee0735af-3249-32f9-89de-15c4d26f2d2c | -9.25128 | -63.63281 | 2025-07-03 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31b281a3-11e4-38b6-86ca-52c2a2ebfcba | -10.29929 | -57.12423 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c892486-cc84-3785-8036-47084c072927 | -9.53304 | -58.19336 | 2025-07-03 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e6c9b78-2efd-3ace-b04d-60b8f27d24ab | -9.62985 | -61.46338 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7071711-f0ff-308b-be88-d7c2e6d95c59 | -9.73188 | -61.40357 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d9c7d9a-2a96-37ab-bdea-3c50bf695fa3 | -9.51514 | -65.58952 | 2025-07-03 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbc6ac34-9a76-35cf-b30c-c3e682f7d0fb | -9.40102 | -63.25805 | 2025-07-03 05:50:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5a7e624-3309-3454-84aa-eb82a0aaad35 | -9.18529 | -61.57937 | 2025-07-03 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d16f629-ea51-32ec-9656-5fa49cecdf17 | -10.30789 | -57.1357 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa6db847-da32-3327-a57c-5f5761e63cd5 | -10.2971 | -57.12544 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b978707-8269-3055-ba73-d9bb3412d440 | -9.70345 | -56.18703 | 2025-07-03 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a936e7b2-041e-3ca6-9e6c-fc0fd9a686d9 | -10.30301 | -57.12622 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dda8f4d-026a-3f69-9959-15768b54578e | -9.09191 | -62.66856 | 2025-07-03 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 835a79fa-852b-3928-b721-73eb97c1ae8b | -10.89435 | -56.45248 | 2025-07-03 05:50:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76076062-0405-340c-aaef-bc0c55e8196c | -10.30355 | -57.13809 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec7ee370-3d59-3a90-bbb8-c54cc6c74bf5 | -8.72502 | -64.17288 | 2025-07-03 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0098cffd-f461-3e21-bf37-aa84184d3a57 | -9.53377 | -63.57927 | 2025-07-03 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef7554e4-ed11-387d-88d9-08fc7e2533f7 | -10.29873 | -57.12864 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fea92fce-84cd-3458-aa32-c7d155529aa3 | -9.07782 | -64.4163 | 2025-07-03 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47dfbbe9-57b4-3b45-9dbd-6748007794e3 | -9.63479 | -61.4597 | 2025-07-03 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c827545-6489-3105-b385-c5a25702abb6 | -9.09141 | -62.67209 | 2025-07-03 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36b78fe1-bcca-3b51-a20e-a6e2c14cab5b | -9.53258 | -58.19688 | 2025-07-03 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62f46070-5c16-3fe3-880f-21addbc2f22d | -9.18315 | -61.58081 | 2025-07-03 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e86f08d9-7294-38ae-a2c8-f0197d9d4a8b | -10.88813 | -56.45169 | 2025-07-03 05:50:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94af60a8-0ce8-3002-bcbe-9bcdad38a191 | -10.29763 | -57.13741 | 2025-07-03 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cbff308-3657-372c-83a9-e739908f19f0 | -18.65324 | -55.74152 | 2025-07-03 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| eb3ac80d-012e-3fbf-933b-70d74ad094c4 | -21.88859 | -56.11492 | 2025-07-03 05:53:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25593a18-dfe3-3416-bce2-cc4a19075b99 | -21.61461 | -57.5625 | 2025-07-03 05:53:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74fee8b8-9926-34fb-8f22-bf2e4648ee4e | -18.669 | -55.75323 | 2025-07-03 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f8530dc1-0234-328a-91cc-fffcad65621d | -20.72783 | -56.66129 | 2025-07-03 05:53:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a30b3899-07bf-3b4f-baae-02fe9831812a | -21.88542 | -56.11438 | 2025-07-03 05:53:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c94a4bbd-17d7-36fe-b2d6-9ab08d752d2b | -18.6603 | -55.74225 | 2025-07-03 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 2dddb5c1-869a-3c2e-8122-262109444802 | -18.65606 | -55.73771 | 2025-07-03 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 1dedf869-e356-3108-bc4a-fca46b3e9939 | -18.65548 | -55.74479 | 2025-07-03 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| c1d118ed-d399-305b-9b98-9e3aa8ace26b | -20.72845 | -56.65296 | 2025-07-03 05:53:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ae24e64-1de8-3142-b331-c2bae317ccde | -18.66253 | -55.74549 | 2025-07-03 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d7d4b81f-f754-3699-8d8c-114e491f9800 | -5.9938 | -43.7366 | 2025-07-03 06:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| aa1b9497-3b1a-30d4-a349-38a5cc19e6d9 | -6.9605 | -42.8816 | 2025-07-03 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 199.0 |
| 09dad4c0-4995-3947-9ebf-a83d39e0ec20 | -6.9793 | -42.8798 | 2025-07-03 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| a6954061-7e3b-3f02-88e3-32e20f03b8b7 | -6.9416 | -42.8834 | 2025-07-03 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| cbdbe958-c998-38aa-885c-3c233e654196 | -6.95204 | -42.88063 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 273.7 |
| 8e5c5de8-ab27-3411-9113-db9ce8c1be6d | -6.28808 | -43.67237 | 2025-07-03 06:03:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eacd8d43-561e-3d00-bd03-ca7aa35ae349 | -5.86665 | -50.14547 | 2025-07-03 06:03:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 34b577a9-6bb5-3314-bd9e-452e24187444 | -6.1729 | -48.0452 | 2025-07-03 06:03:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6ea4c201-3de7-320d-8367-551636f37881 | -6.29395 | -43.66821 | 2025-07-03 06:03:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d1650790-278a-32e1-888e-adedc90abc97 | -6.96551 | -42.87711 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 79641e57-dc6f-3cb5-a648-4234520f4d71 | -5.87549 | -50.14677 | 2025-07-03 06:03:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5c13dc3c-10e5-3112-9468-12e0a782f67e | -6.28034 | -43.66607 | 2025-07-03 06:03:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 56d5f5a8-c0f3-376b-a99e-282ae25c04ca | -5.99882 | -43.72123 | 2025-07-03 06:03:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f3d91d28-a721-37a8-9ef5-055e5c23d352 | -4.28382 | -48.18586 | 2025-07-03 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 08da99c5-76af-3000-9a4a-77464f3ab6e1 | -7.21889 | -43.04369 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| a40a072c-82d3-3c51-9bd9-9352cd897edd | -6.9508 | -42.87521 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 228.3 |
| f21e8090-7a60-30e9-afa2-57e8255dd075 | -7.22914 | -43.06507 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.9 |
| d7df4548-2de9-3eed-815f-97b3d4e41042 | -6.17133 | -48.05619 | 2025-07-03 06:03:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 29c293c5-1c33-3e26-ab85-161ef9a3b34c | -6.2772 | -43.68892 | 2025-07-03 06:03:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 104b9558-5d4e-3926-b533-2b4dfb4ab061 | -5.99574 | -43.74348 | 2025-07-03 06:03:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 59bc6ebe-03cb-3053-9eb0-504a4bc2944c | -6.96676 | -42.8825 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 436b8cc0-d05f-3535-ba5b-3c87fd34b546 | -6.68714 | -43.1497 | 2025-07-03 06:03:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 648e134f-4904-39e4-80b9-87ace6b2a84a | -7.23 | -43.07235 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| d1b6cb35-14d7-30a8-8bb0-563c23fc375f | -4.53603 | -48.02339 | 2025-07-03 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3ddad1a9-3714-34cf-8487-932c457ff001 | -6.95557 | -42.85308 | 2025-07-03 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |


[Clique aqui para ver as próximas entradas](README24.md)
