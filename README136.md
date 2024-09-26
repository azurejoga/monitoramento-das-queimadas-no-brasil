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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 713b0470-6fc7-3b06-9524-095a24dfef31 | -9.04349 | -60.42797 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ad87309-f199-3a9f-927c-6ae5aacd0f9a | -9.02217 | -60.45224 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c15a433-5fc7-3264-b3d0-c53591cbaf34 | -9.1021 | -61.12352 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8821266f-6f5a-38e5-be15-d0ce1ac1533c | -9.09699 | -61.12701 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6783041b-e565-3066-b261-79b404c33250 | -9.09336 | -61.122 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 50a9aeba-8a54-3c80-99e5-371e63cf8d45 | -9.08898 | -61.12129 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 02b21181-30a6-3675-b658-f828fa4ff823 | -9.08823 | -61.12556 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c883ee3d-afef-3a28-9065-6889c36fafcc | -9.05259 | -60.43286 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd3c4d97-4376-3d86-817c-1d41f08c0df5 | -9.0491 | -60.42827 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 284e2ca2-cb33-36bd-a44b-ab1c7d0026eb | -9.04842 | -60.43213 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6ec46d8-18e7-33b2-84eb-a9942c949a3b | -9.04702 | -60.43256 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a486cf22-abb4-30f6-929c-563146ddb295 | -9.01733 | -60.73226 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c320a009-ee4c-3d62-9199-26b5b9fc69c1 | -9.01234 | -60.73562 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d92cb76c-aff8-3bd7-aa0c-451d576f849e | -9.21663 | -61.14207 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e380640e-4829-3922-b416-776edce11c9c | -9.21589 | -61.14635 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c6bca0a-29d5-30fd-a481-5ee4237a45f3 | -9.21226 | -61.14134 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e6d38cb-4bc0-3613-8add-1abef1a18118 | -9.21152 | -61.14561 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67152b0a-c48e-3d65-b7a3-e412a4365420 | -9.20854 | -60.90732 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc4b7cac-edb0-3ba3-a15a-973a648de60f | -9.10646 | -61.12432 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94224a70-a243-3c00-95d8-97cb8c3d29ba | -9.10572 | -61.12859 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4f3f2ed-bc57-32e3-820e-72d2aa850707 | -9.10135 | -61.1278 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1e17bb9-9229-3013-9b98-db68fbfca761 | -9.09773 | -61.12274 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 93cca569-8261-3bf1-b313-65129e8cbc1e | -9.09261 | -61.12627 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 442e34e8-2c42-3d51-8433-0bdfaee33267 | -9.08536 | -61.11627 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fca0946f-31be-3769-a24b-ceedecdce041 | -9.08386 | -61.12482 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e973cef-cf4d-33fd-b43d-b3f81317404d | -9.01306 | -60.73154 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e39d041-b2c1-36af-8221-f5e3d03fd533 | -10.73553 | -60.74483 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2fc42b95-fc3e-35cf-b9ef-f907b42f0061 | -10.73273 | -60.73657 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c255b432-4f0f-3d1e-83f6-8b2795b5d1a1 | -10.73073 | -60.73586 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51ce25f9-593f-3083-8731-1264bfa6be9c | -10.72859 | -60.73584 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10ecfc7d-735a-3efd-b252-72cac0ee09c1 | -10.72519 | -60.75483 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ea22463-9499-37f1-b1cb-ba8dc7f040cc | -10.72028 | -60.72221 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 11fbd738-06aa-3328-95e0-5458af81e688 | -10.71962 | -60.72602 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d03a9dc-d230-3d1c-a3f9-a24793d5910b | -10.71614 | -60.72146 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 147c9058-7693-3f28-8d37-be6bd1feb464 | -10.71548 | -60.72526 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b16da4ef-44e9-3864-a61b-c91343746c10 | -10.71134 | -60.7245 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a5a4387-49b4-353d-85f8-74187b3d5cb5 | -10.7072 | -60.72376 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d676f4f3-bca4-3397-b275-83e77f939dcd | -10.69427 | -60.74903 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71bc9d76-e46e-307b-bfb9-cf1d3191309c | -10.69078 | -60.7445 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53134f8e-df1d-38d4-a663-36e36e334c28 | -10.69012 | -60.74831 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af69967e-02bc-3181-a119-e7239462ec71 | -10.68663 | -60.74378 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aacda202-ed1f-33c5-b1dc-f2b8a33cda3c | -10.68597 | -60.74759 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b41aa138-c67e-3500-aeb1-e41e892ca4e2 | -10.68248 | -60.74306 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f215cb-8f18-3c3d-8032-0987e0cd1863 | -10.68181 | -60.74688 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48254b43-7d42-3bf0-8bfb-9c00d6fb6bb6 | -10.68115 | -60.75069 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 552c4959-4278-3366-acce-3389b1a68fd4 | -10.68048 | -60.7545 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a2c3a17-5cba-33d1-91a3-148f5dad02be | -10.67833 | -60.74234 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 777c9048-0d68-3563-9e75-24cec3f8aa01 | -10.39701 | -60.70436 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af996cdf-4581-36e0-9895-abf7dd78252c | -10.22771 | -61.27084 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a90e81c8-da04-32b0-8f02-c6d8bb2f28f4 | -10.04464 | -60.43636 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c9393d6-f508-3ef2-bde7-8837b13035ca | -10.03921 | -60.44312 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed3b1f01-f103-31d3-a4e3-4ae521128536 | -10.03576 | -60.4387 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7842a515-c983-3bc2-bac6-f2fca64863d3 | -9.86683 | -59.86604 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81e378f3-a077-35e6-bb6a-c275a52f9fc5 | -9.86528 | -59.85121 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb8247d9-bdf5-3974-be41-71ea2f5b7d80 | -9.86468 | -59.85469 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb59b7b9-1734-3e07-86d9-7b7c8fe89c6a | -9.57667 | -59.77199 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ebe5b7c-e96d-3c54-bd93-25ec2367399f | -9.5761 | -59.77541 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5c0e0e9-0648-3983-8a42-0ddfebb039e4 | -9.57552 | -59.77885 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13c67f58-709e-31f9-ab7f-a483c347cc0f | -9.57492 | -59.78236 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a70b4946-4ceb-3188-92a9-911da56c3a65 | -9.57094 | -59.78172 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a6e0e3e-7104-34c6-ae78-8f9567e4cfc0 | -9.57035 | -59.78522 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca3c590-88ba-3b84-b4b8-38dfc01bf9e7 | -9.5699 | -59.76377 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59f3459c-ef48-3bd5-936b-176f1f70dc03 | -9.56931 | -59.7672 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a310b009-5f5c-3e7a-83ed-3eabb29121e1 | -9.56873 | -59.77065 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4e25b87-09a0-3bca-990d-84d4155eb446 | -9.56815 | -59.77411 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d41aad25-67ac-3e74-a49b-2f9d9e8ec5fb | -9.56756 | -59.77759 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0870970-71e4-3a4a-a3d6-723bd281e07e | -9.56697 | -59.78106 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 392661f4-62b6-3a7e-b529-67ef6da5c0ae | -9.56417 | -59.77345 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98db3845-b379-3af1-84c0-e2f15916d313 | -9.56358 | -59.77692 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0777e86e-f501-342f-a80f-a62edc8361ff | -9.563 | -59.78039 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185b47df-bd78-324a-86fc-2d8d0cad2961 | -9.56241 | -59.78385 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b5e9cde-63b5-3d87-8adc-4245f451f80b | -9.56182 | -59.78732 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa5efea6-5858-3536-acee-a5b538d4c8c8 | -9.5602 | -59.7728 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e0be08c-6486-3a8c-af62-b9a921becd63 | -9.55961 | -59.77626 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c08476b-5019-38e6-8d1f-acaec32659f3 | -9.92226 | -60.75907 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3ea8c54-9d36-3091-b40c-771900de112b | -9.91874 | -60.75443 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fa4da2d-4c4f-3c94-8ace-510c70419895 | -9.91023 | -60.72875 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb8b369f-1873-3bfd-b51d-8d86d8c7dd07 | -9.90116 | -60.73115 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 368ccde0-1a9f-397b-a590-716da5b55f49 | -9.85218 | -60.73542 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48130607-dfae-34bb-87ac-9aa57b4cf6bc | -9.8461 | -60.77092 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10737d23-e5ba-3ac1-b72f-d7adc41210a6 | -9.84542 | -60.77489 | 2024-09-26 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2faee99-787c-3318-a6cc-10f83be6d114 | -9.36292 | -61.02734 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b76b7188-0262-372e-84aa-93404707d50f | -9.82417 | -60.47595 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 947ce6b9-2330-3819-838b-1d70d8d9dd24 | -9.82351 | -60.47973 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f785e908-9bd3-3a0f-8013-8cfccdaa6769 | -9.82151 | -60.49111 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858481d7-d9b9-3209-b46e-c2a0f2e39da3 | -9.81803 | -60.48664 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 545dbd5a-4239-31fa-8b2f-b2ccaea81f70 | -9.81737 | -60.49039 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8839518-3d4d-3154-8400-4cc9f3873ae3 | -9.42416 | -60.29749 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83bb519c-58a7-3ef2-a557-02d76fc0f00b | -9.4194 | -60.30048 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 245b91f1-c9eb-3ab5-bdcb-32febafab29d | -9.41529 | -60.29977 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eda42f6-d783-38ee-8db8-9333727fb8f3 | -9.41464 | -60.30352 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96e37700-d712-3820-ad46-dfd510cc9fc7 | -11.95931 | -60.36214 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0228395a-f38d-3015-9f74-69b4f6182500 | -11.9587 | -60.36563 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f0f98b3-3e96-3f68-9a01-42782b5c4fa4 | -11.95595 | -60.35794 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2325b01d-19fd-3fa9-80c1-eff4b8ed1105 | -11.95534 | -60.36143 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 47c3d5f7-a4bf-3d06-bafe-e6351a60dc22 | -11.95473 | -60.36493 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6d16f85d-2833-35bc-8f1c-64d10a40cb67 | -11.95198 | -60.35723 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0085d502-3838-3e93-9b2a-6463c617daf0 | -11.95137 | -60.36073 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd648aa0-4fa0-3443-a275-be4bb60a685d | -11.95076 | -60.36423 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 99f5b1a1-9053-3309-8041-32207fdec9f1 | -11.94223 | -60.36628 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README137.md)
