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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c80543f-5056-3a5e-89eb-14f9d8623ef5 | -9.85081 | -60.31425 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3d55203-b6cb-3fa5-892e-8c0401e77541 | -9.84799 | -60.30986 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15d66a2-a91d-30fc-8bac-5c572df1d794 | -9.84736 | -60.31369 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b030f99-8a6c-3a64-b9c7-03c3de697003 | -9.84673 | -60.31752 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f08c375-1342-3bf4-a99e-a03778ebfb65 | -9.84265 | -60.32075 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e266b8b9-2df6-3429-981a-53db23091fc0 | -9.84202 | -60.32458 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12148e1b-0bf5-311e-9a39-f2f600298bfe | -9.83921 | -60.32016 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80dc6a81-1019-37f4-8fa4-155db46159a7 | -9.83857 | -60.32399 | 2024-10-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 799ced20-d403-3507-aceb-f9f57057b9dc | -9.38893 | -60.91588 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bd56db8-1316-3f99-8f1f-00ea850baced | -9.38538 | -60.91527 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f801d33c-7d9a-35c4-a9c8-dd524d518197 | -9.21855 | -62.18339 | 2024-10-14 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9e15c8e-a46f-3a7c-b759-4ad31856ee01 | -9.16206 | -62.42123 | 2024-10-14 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db646622-43fe-3fa9-9abc-c0d18f20b788 | -9.15904 | -62.41568 | 2024-10-14 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e2bbe0a-b348-33a7-affc-18988d4301a9 | -9.15741 | -62.41843 | 2024-10-14 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8079c809-b015-35fe-9b50-3959ae667794 | -9.11304 | -61.16055 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd48f443-33a5-347b-9467-e2f488782f5e | -9.11235 | -61.16474 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d447d67-e49f-3386-9df5-b11430b80c8f | -9.11012 | -61.15573 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4563a1d1-30fb-37de-9607-4025aaed4c1b | -9.10943 | -61.15992 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6727aa97-7769-36c0-a7ef-da3874a1996e | -9.10583 | -61.1593 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a4c956b-71f1-3e40-b3bf-990bf48e3ae0 | -9.10514 | -61.16348 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95bff6a4-ca5c-3cae-8d75-621705ff4234 | -9.10222 | -61.15867 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78d07216-c75a-3cfa-8cf9-65df66a0e855 | -9.09083 | -61.18272 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0adcd862-20b6-3853-ad1d-25e65c1527fc | -9.08862 | -61.17366 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4c657a0-3bf9-3607-9b9d-5af3fa674fb6 | -9.08792 | -61.17788 | 2024-10-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52c830a4-f819-35e8-b356-922f3ee9ca11 | -8.9014 | -62.36446 | 2024-10-14 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d504bfe-16d7-34cb-bc10-541731b7c5b7 | -8.89671 | -62.36868 | 2024-10-14 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 728f9ba3-86b7-3c35-8e42-c0d71cdb0031 | -10.34019 | -61.65261 | 2024-10-14 05:10:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42e22df5-0f56-3dae-9637-39dbee05441f | -9.42614 | -61.80435 | 2024-10-14 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f1eb46e-59f6-3e7b-ad2a-4435575238be | -8.8125 | -63.18464 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b5f33aa-3116-3e47-ad46-e5a614f3d7e7 | -8.80843 | -63.1839 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2678d0e2-de69-3937-9148-da77ce907ffb | -8.70232 | -63.16962 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ead9447-bd40-3ac4-819b-278fe9642825 | -8.70168 | -63.17327 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beee86da-230c-34e9-8ff5-064a950a22f6 | -8.70017 | -63.15784 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c27357f-b3d9-38d2-9453-d1c13c9a3a7c | -8.69881 | -63.16891 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41e4888c-b37f-3c72-a9b4-fa58853bc5c5 | -8.69824 | -63.1689 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdfd4c1c-d273-3438-abd5-1e03189be0f8 | -8.6982 | -63.17258 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c22a8e1-a6f0-3255-a954-30ca9a1f0b33 | -8.6976 | -63.17257 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cdab2a0-eff5-33f8-b1e3-00a7e7a4abe2 | -8.69658 | -63.1571 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ff819e6-bf86-3683-99c6-87edbd69eb54 | -8.69609 | -63.15714 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a98e49ac-e8d1-3116-9859-bbfe309e5f0a | -8.69596 | -63.16081 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a892b362-28a2-3c96-a711-186f05d06f80 | -8.69545 | -63.16082 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d23e611f-14df-391e-800c-3ce82ef72b33 | -8.69411 | -63.17186 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93e8dc8d-f488-3928-99b9-d10ae4bec348 | -8.69352 | -63.17184 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fc21c8b-6e8d-3569-82d5-93c710f7674c | -8.59518 | -63.25734 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 911b5589-3887-325b-b8a5-7f756bb76a9c | -8.58306 | -63.11227 | 2024-10-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28750da5-4559-3d08-92a6-52bcceb4892d | -8.56652 | -64.04493 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc7488b3-f9fc-32a1-b460-fd96d0deb041 | -8.56219 | -64.04416 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8693cf5d-8592-374a-9389-5ec9d94c92da | -8.1292 | -63.95296 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e37670cb-0195-3d2e-808a-a907b94f9416 | -8.12486 | -63.95219 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13ed4ff5-e02e-35b0-b098-a91b6d3ef095 | -7.95364 | -63.62888 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d81990ed-ee23-3b5c-8d94-85311dc21bfa | -7.95296 | -63.63292 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 456f5f1e-02c4-321c-ad9d-625478455ddd | -7.95005 | -63.62413 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7b087be-c106-3a47-95de-c4f395cb6910 | -7.94938 | -63.62814 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4d564cd-bab6-3f2e-a783-4a1f40605d62 | -7.9487 | -63.63217 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4c2e413-57be-3c30-821e-541e4ea3aff2 | -7.94801 | -63.63622 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76240f43-1d9f-35d8-ae78-aa7a7236695c | -7.94512 | -63.62741 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7122c73a-caf4-3dca-a4e5-f15e1be99d6e | -7.94444 | -63.63143 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2961ac8f-71b5-3f0e-8f98-2fc123808dd9 | -7.94375 | -63.63546 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a842af3a-da39-3d17-b136-66a1645cfc3e | -7.94086 | -63.62667 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b72bebe6-2cd8-39a1-a3d4-6972343ecd61 | -7.94018 | -63.63068 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e013a80-1f7d-315d-bfbf-68c1dbbd2822 | -7.9395 | -63.6347 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdd3960b-304a-3908-b99c-f3f3507903d6 | -7.4635 | -64.25216 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 737ce68a-8ea7-3edb-8ffb-07d74e7c026a | -6.67185 | -64.60896 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc1dc9cf-5e5f-302d-8502-b006d902e77c | -8.5988 | -64.22138 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df787dde-7290-317b-8aff-678dec4fd94a | -8.59806 | -64.22569 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07fcbb4b-3c8a-316a-b42d-5bc51c0b31cf | -8.59442 | -64.2206 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1d5f8e9-ef54-3c51-a2af-f9f635c670eb | -8.59367 | -64.22491 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 272a06ed-64fe-3a61-8006-6fcedacd7f5a | -8.21026 | -64.0358 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a910292-0eb3-3ea7-961a-261276afda13 | -8.20591 | -64.03502 | 2024-10-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85f8f25c-b34a-3935-9666-8e197abcef8b | -10.08017 | -44.20872 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccd1278e-a205-3143-aef2-0c7435280bf5 | -10.08412 | -44.23735 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a346592c-e5ff-3802-87e3-014e9692ec5e | -10.07693 | -44.23659 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| faadbc71-e44f-33c2-8efd-defb112cf53e | -10.07611 | -44.24359 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d9ae2c6f-dd35-37a2-98b9-8bdd5deecda0 | -10.06972 | -44.23603 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 111c032c-569c-38ca-92e5-371adcd572f4 | -10.06808 | -44.25014 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 65c6d87c-68dc-3654-ae6c-75bc097431c6 | -10.06727 | -44.2572 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e0223078-664b-355d-8256-d1d9b966281a | -10.06645 | -44.26421 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c1386bf4-95bd-31d3-baef-c4723bc6d909 | -10.06564 | -44.27116 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d7fffde0-f109-37e9-b09a-abf6bb6675f5 | -10.06085 | -44.24983 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3c17417b-ae30-3cc1-ac86-d7da3b4c7761 | -10.07856 | -44.22261 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee7d3d34-3bd8-3a0d-a481-a3ee85ff075c | -10.07774 | -44.22963 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3eee203b-459f-3818-82aa-e8420cae667a | -10.07299 | -44.20782 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ee5aa3f-b27a-394c-8b3f-b6670e38dafb | -10.07216 | -44.21497 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57d1d7f3-b923-354a-8d66-567635521a76 | -10.07135 | -44.222 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6104f86-fe46-3b2b-b6a9-1338df4d93c9 | -10.06224 | -44.21452 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d8df5ab-2aea-34d4-b75b-897c898fd283 | -10.06137 | -44.22165 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc986bec-b7fa-3867-88fc-81777d7ed511 | -10.04427 | -44.20418 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d11d5783-6908-3546-9ba4-446039726d81 | -10.04347 | -44.21119 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b9821b2-65fe-3326-b630-70f220e3d702 | -10.04263 | -44.21861 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed8a158c-9164-368c-95e2-7aa8cfeaa38d | -10.04157 | -44.20472 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 638f3528-c994-38ed-8b7b-1406ac59ec8c | -10.07383 | -44.20061 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d0aa6a1-9721-3457-9d7c-13a0a4704189 | -10.06663 | -44.17842 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 330b6ad0-f9ce-3a26-b422-db7f67617417 | -10.05052 | -44.19093 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6fb5a102-62ef-3fbd-bf41-62df9741aa82 | -10.04592 | -44.18978 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 841ddce4-fd49-3361-bbf4-98bbacd1e050 | -10.0451 | -44.19698 | 2024-10-14 05:10:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eabeb00-5d01-3816-acb1-a1ce15889138 | -10.9186 | -44.69233 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 518ac3d8-5459-3b03-9bb1-33428dca2c4e | -9.26334 | -45.22765 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d71d770e-66e7-3b53-a8ce-54ac1c27cc11 | -9.26257 | -45.23385 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1f51b53-91bc-31d7-91ad-ae02f2d8860c | -10.92084 | -44.69142 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f3662c-0322-368f-b10b-0c0def7894cd | -10.92004 | -44.69827 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README113.md)
