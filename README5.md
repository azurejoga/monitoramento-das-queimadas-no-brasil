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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fd63f19-4e19-3415-b373-bb463b017517 | -8.88092 | -60.74544 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 491c6406-dd3f-3485-a8ac-6acd15062be0 | -9.10719 | -65.76916 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c120355c-17fc-33d3-9748-1912476ebaf3 | -10.37289 | -59.2075 | 2025-08-30 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 715452c2-a697-342c-a854-eb2141f6dee6 | -10.07436 | -62.89786 | 2025-08-30 01:28:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f8da6447-0939-3ccc-9418-18366bc48b9c | -9.7304 | -64.91575 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| afbafee2-5405-318d-b1ce-3929d14aee9c | -9.72893 | -64.90478 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0ac201d4-a57a-372f-8eef-a23e2054c5a5 | -9.10981 | -65.77513 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 5c707156-e754-3897-9d24-bc0ed9336ba7 | -8.87959 | -60.73602 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0f1110ea-358d-3371-b1b9-ff7e4b72399e | -10.48341 | -57.9515 | 2025-08-30 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 213e7041-d541-3a89-8e40-e141accb1176 | -11.35498 | -63.24934 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 160e79a8-8afa-3626-80bc-0ed7a9905299 | -9.77771 | -64.25399 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bb92e9ec-2604-352a-9414-30253bee0298 | -9.45628 | -63.09316 | 2025-08-30 01:28:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01af7d24-b97f-3e08-b883-7ee78e443b7f | -8.89 | -60.74781 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c9a77b16-a36f-3c51-8e76-57ae573ea8c2 | -8.93742 | -64.15974 | 2025-08-30 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c97945b9-900b-3b9d-aaa4-d1c7a547814d | -9.55559 | -63.21305 | 2025-08-30 01:28:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b6bdaa9-89be-34a8-803e-2785e19d30e3 | -9.55604 | -65.69182 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5847e148-e110-3567-81a6-1d65d4db0c17 | -10.93867 | -63.63782 | 2025-08-30 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8c67fb47-930b-369d-8872-edfaf182b977 | -10.07394 | -58.36585 | 2025-08-30 01:28:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bc8d884c-9fcb-3163-b1b9-be020c1102a1 | -9.17982 | -59.57803 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| adf18f03-3c38-34a4-9b6a-58b99fa32117 | -9.06802 | -65.46005 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 66e5af4b-4708-3dfb-baae-0b867af34f54 | -8.87826 | -60.72657 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2f8bb462-1b62-3b7d-9fbd-75b37508456b | -9.45354 | -62.33531 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 53f1783f-7ef3-357b-b117-5f059850cb5c | -8.90622 | -62.10019 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 67bf94d2-25cd-338c-a6cc-402f7ac5a661 | -9.67504 | -65.02453 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0ae36a63-a408-346b-a773-7ab87ad487ba | -9.78575 | -64.24255 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 369f42f6-42de-3b11-9711-2765a23c52bd | -8.66699 | -62.4332 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8bc64995-4644-3ea5-98f6-67ec4fa32673 | -11.35625 | -63.2589 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8df4cddc-19c6-3dc0-b877-0c563cab7bc6 | -11.3006 | -63.25358 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 05bccc30-147e-3c6b-a7d7-9c249612d643 | -9.54855 | -65.69837 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6092662b-4711-3457-9ad0-4bb205938c6f | -10.23904 | -68.09444 | 2025-08-30 01:28:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 40fdbbd7-a578-3db7-87f1-a8acb086fa8d | -9.44471 | -62.33658 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 026cfef4-e3ed-3f3e-8f45-63cf4c30718a | -9.11434 | -65.74346 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4d8fefbf-1783-367d-86b3-78fdb92b9d7a | -11.29532 | -63.28354 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ab86a869-0bb2-3e5a-872c-dfcf8c05b69a | -8.8974 | -62.10146 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1aeb113e-9055-30a4-b5d5-7de7cfc52a0a | -9.22003 | -60.86211 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9d64152f-0171-3541-a486-d32abf06f3e5 | -8.85317 | -64.14771 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 21e057e7-0e0b-3f66-aa8f-134fea9fb60d | -9.81161 | -61.19746 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4533abeb-dcfa-307f-a4a0-89a47ed4347f | -8.59931 | -60.58574 | 2025-08-30 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e71933c7-cb52-3a52-8b00-094f8f345df8 | -9.1082 | -65.76305 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 812da482-e477-3c31-8801-627c514ac5e8 | -10.37269 | -57.82844 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4c1f52ee-ae79-378f-9ca3-e446d32ea864 | -9.15593 | -59.57742 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d1cfe2da-4762-3ec0-918d-7e0939ce67ea | -9.16549 | -59.5759 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3ed26110-bca4-3df6-afe6-f3176d1bb240 | -12.42796 | -63.91356 | 2025-08-30 01:28:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1fcd8bca-978e-35e8-a94f-6726226ac6a0 | -9.57823 | -54.48864 | 2025-08-30 01:28:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d60113a9-9309-3c52-8e0d-09796dc27ae3 | -9.06551 | -65.44319 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 702fb9ed-80a4-321a-8809-a11a4afc6234 | -8.88728 | -60.72896 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 399c0079-486e-3180-acfd-5599ee9ba800 | -9.45477 | -62.34422 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8f9ae1fb-e89c-34f3-9ec5-804c080e15e3 | -11.39268 | -63.25377 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b0baa752-0923-39bc-8559-299a80f29ac6 | -10.93736 | -63.62811 | 2025-08-30 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 447a80fd-a25d-3449-b22a-c6db8d8e6378 | -9.76477 | -65.08571 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d27c12e5-26fb-3409-adfa-097959257b34 | -9.17505 | -59.57432 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b6d89a27-932a-3c96-88aa-03ea065049c0 | -9.15282 | -59.55597 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 52cc45cd-876b-3cc1-bb09-13bee6d05aad | -9.07655 | -65.44713 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 9430863d-8d65-361f-a001-02b2ef3d2095 | -11.28621 | -63.28482 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 5d039c40-c81f-36a2-84dd-3ebcbeaf2e16 | -9.73221 | -64.90921 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5eb4b025-8939-35ad-afdb-b47ea63fa83a | -14.79897 | -59.71326 | 2025-08-30 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aef02e29-e614-36f5-b773-f4d134e5e371 | -9.06654 | -65.44848 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 13e05f3b-d514-3626-88f4-ca69379dd7b9 | -10.35698 | -64.46449 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| afbb6123-98be-3f5b-8cc9-dd4b185e05f0 | -8.90746 | -62.10907 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 5575a9eb-36f7-3a84-b36a-a393c7028cf0 | -9.46487 | -60.31331 | 2025-08-30 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8c280c3c-f823-344c-ac18-b39d0ed58c27 | -9.11744 | -65.76785 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 4b73fc6e-c0fe-3522-b58e-fc9154704e77 | -9.22136 | -60.87143 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4967d16c-7fe8-3a3a-b9b3-ac911a299736 | -8.59793 | -60.57615 | 2025-08-30 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 70a7a8a0-ca84-334d-a2e6-600035a690a4 | -9.06507 | -65.43692 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 7e1b03d2-04bd-3f12-b8d0-93e46371ce47 | -9.17656 | -59.58485 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4376a34a-a091-374c-9796-db046f6b0d82 | -9.11589 | -65.75568 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 2a57a054-8baa-37a1-9d5a-f2b3514baea6 | -9.08422 | -59.49004 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 86029987-b51c-3f46-a890-30426dcebc1a | -12.42934 | -63.92405 | 2025-08-30 01:28:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 21a09ea2-fa61-3a98-a2ad-ad1bbb99702b | -14.79264 | -59.73322 | 2025-08-30 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f6ec9f50-9d0e-3001-9a05-bcd3e3f76027 | -9.15437 | -59.56663 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a840226f-f32a-3463-bdb8-c6c067c8e8b4 | -9.07507 | -65.43557 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 6afcc826-0380-3e35-b682-13da3fbfc148 | -11.3914 | -63.24422 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2c70890e-98a8-3898-86cd-fdd872e5e1a4 | -9.58274 | -54.48249 | 2025-08-30 01:28:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9702e05f-64c7-302c-ac81-5789026bdb56 | -10.37465 | -57.84148 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a6609a94-3020-3ff2-85b3-f4bc02da574e | -11.37319 | -63.24679 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3431ebb5-e391-39a7-8b6c-6816cefd9b7c | -10.37132 | -59.19679 | 2025-08-30 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2c8c1372-c568-311d-9efb-1b096be8ea2a | -8.67582 | -62.43193 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 40546df3-c7ed-3d4c-87df-e3c06a128eae | -14.78365 | -59.7347 | 2025-08-30 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c876012b-1b95-3d02-bf6e-8481001d354c | -8.89863 | -62.11034 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c5fc4ef6-84c5-393f-ad95-8d2e01fbde68 | -10.74824 | -59.8173 | 2025-08-30 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 254ef14e-bfd0-3e1c-bad2-18632a0971bb | -10.07213 | -58.35371 | 2025-08-30 01:28:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 440286f6-05c5-34ce-98de-a9bb7d920227 | -8.95908 | -65.96401 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e7dcdeab-5faf-3dd7-bad9-bb2638d2006e | -10.3707 | -57.81516 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5b59e391-f99d-3da7-b309-fd01297790a0 | -8.65688 | -62.441 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 52ebc07b-5b55-3806-a304-fcf1d784410c | -9.13546 | -65.82748 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2948a60d-cb27-370b-aff5-2e6cc84550a0 | -10.36328 | -59.20906 | 2025-08-30 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 8e76e535-575c-3c31-a696-8a9ab3afecb6 | -9.23914 | -59.78229 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b877476-04ce-33f2-a65a-2b2209cfd3f8 | -9.44839 | -62.3633 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b9fe9ebc-7fbf-3b85-9439-5d82b70bbf5c | -8.65811 | -62.44988 | 2025-08-30 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db1d322a-46e0-3e86-8722-1e2302d8e44b | -9.27367 | -60.46248 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a978fd1b-e470-3f21-aeef-b0f7a2f68842 | -12.22596 | -64.22408 | 2025-08-30 01:28:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| eac0f7da-2c74-3233-8199-3c0d670d5e62 | -12.92788 | -56.98342 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 77cda6b0-9e5d-3dd1-9a10-0c074c939960 | -9.18244 | -65.55814 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1d98d8c5-392f-3df7-8c70-c768fdfaa0db | -9.18138 | -59.58856 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 3f192880-bb3b-33ce-bdec-2970c0f0ae1b | -11.30188 | -63.26314 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| a13b3820-0974-3fab-9401-b8ebe8a081c0 | -9.54282 | -62.38026 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58d72b73-d02d-377c-9b18-04f0f7db7107 | -9.44594 | -62.34549 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a7566f19-039f-3f1a-be8f-a0b65981849c | -9.25156 | -56.89752 | 2025-08-30 01:28:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 174b7713-450c-32fd-a7a0-c99191026f0c | -9.1339 | -65.81525 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4a77b971-d4de-3c94-9f8e-bfbcd8340e78 | -8.8843 | -60.7315 | 2025-08-30 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |


[Clique aqui para ver as próximas entradas](README6.md)
