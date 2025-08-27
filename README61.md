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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01ef3f08-f716-3721-be86-b7c14364b34a | -11.83015 | -46.81106 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59e060d0-1ecb-3df0-850a-2fb9ab1d041e | -6.63633 | -58.54935 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3b7980c-6ac6-38c7-ae32-d3cbf12fab3f | -9.64 | -59.6364 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 358b47d6-7ede-3e19-a84a-2b97b8eab552 | -5.45554 | -60.15736 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6de04c2-79bb-3b7c-bfe2-c23b1242a5d5 | -7.25607 | -57.66302 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55fdbe3f-244e-372c-84cd-cc9d29065c70 | -8.07352 | -61.54071 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95339329-2a47-32a7-83e4-8c56de1966f2 | -6.82922 | -58.96989 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43bb5e96-f893-39ea-8b12-65f7f822c9e9 | -13.3749 | -46.89976 | 2025-08-27 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cb645f92-d20c-3362-a47e-c2b55b78efe8 | -8.5564 | -51.35452 | 2025-08-27 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a659ff0c-bff7-31ae-b769-6ad2a493fc86 | -12.77004 | -48.17743 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 904cc9fb-ffe8-3a9b-95e6-4ecf3faa7382 | -9.40528 | -60.50328 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 394f8f6e-ae36-32b1-b6b3-6990e4c508ba | -9.80316 | -64.26378 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94e146f9-efb5-3570-a4ab-70fe545de466 | -9.63615 | -59.63942 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6764a30-d978-3fdb-ac87-eabe82eec690 | -8.12694 | -55.55033 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d02a32b-a571-3ab2-abfe-ba5c38dc7a13 | -9.1786 | -59.69493 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4cccc08-dab4-38d4-9c98-be51a5f70dea | -6.24087 | -60.01019 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b60a4ce-81a3-3e51-856c-2f3bfd6a57e5 | -9.16615 | -59.5576 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a55dd6f7-d1e4-3ef6-a40a-4cc58827fd80 | -9.61014 | -55.37196 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8bbd223-975e-3bd7-8c6d-21603804a480 | -12.70337 | -48.18268 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a7057ca-c371-3f67-b8a0-ff0b208c80a6 | -8.96411 | -65.94328 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3f95b63d-712a-3d96-958e-6bf4790e88ea | -10.77342 | -60.77933 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d49a029a-9569-323b-bdf3-b5f32cef2b7b | -9.26027 | -59.76116 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c9cd86-2fa7-3990-8626-bf646dbe32ac | -10.09771 | -62.89302 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0285a86c-53ce-3fc7-9321-f4be072784f2 | -8.95978 | -65.94252 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b63e36c0-5523-350e-91aa-e6d02a7950a3 | -9.66903 | -67.5097 | 2025-08-27 05:18:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5d73159-1039-368c-8eb2-fb12cf8e9dd6 | -6.81877 | -58.9718 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7f23137-143e-3071-a0f0-0bb5a171f685 | -8.12622 | -55.36769 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f957200d-9d3c-3918-bb69-643ea1b7f3fa | -9.19579 | -59.51955 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2405d48-4c0b-39bf-877f-c73bdf664ba0 | -6.87563 | -59.82494 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2ad1f23-154c-3c53-899a-ef602fc2824d | -10.08926 | -62.89991 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 49cd01f1-110a-3c24-bc20-7d1bbd312210 | -8.07069 | -61.53641 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce58a12d-3f13-3242-b299-e9471ebcb14c | -6.62306 | -58.54727 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22e4e0f2-48b7-304d-81d2-da265c5972d4 | -9.41577 | -60.54457 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2167ba22-dd02-3c44-9902-7a02f73b45e5 | -9.6205 | -62.26516 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4027decc-0d8e-3a37-a3e5-3e2c0379ba0a | -9.18533 | -59.52148 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e543c95-dc72-38b5-80bb-c84325da075f | -10.4153 | -57.70657 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e54fcebc-517b-3977-80a1-022f47155a05 | -8.94604 | -65.94446 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79ecc3fe-4268-3bc2-9ced-512baa572652 | -7.29468 | -59.62495 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35113fbf-bc87-3cd3-8759-f048eef2ef17 | -9.40472 | -60.50679 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c21b3eec-ea77-3065-9ec8-89bff9e54ba7 | -11.83157 | -46.7976 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3a7a02b-ca65-3341-92aa-2aa823717742 | -9.18238 | -59.45325 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d6f8d4b-917c-343b-bf59-b5024054724c | -10.26941 | -64.49141 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a0b97f53-c2f6-3abe-9ad6-a3784a43a0d0 | -9.1792 | -59.49555 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc089f79-550b-36d7-9825-0c1ac45acfeb | -10.84135 | -54.01082 | 2025-08-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b32e13d-1836-3fa4-a900-0db063a8a8f7 | -10.09416 | -62.89238 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e76dd5ff-d371-38c5-9246-ba76d9fdc269 | -8.07962 | -61.5457 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2ba3d87-9091-35cc-a1a4-9fca56b52f19 | -9.69581 | -61.28404 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e8a678e-3619-3112-8e4f-9dcbe8cd0079 | -11.81686 | -46.80296 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13266a32-6a70-3cae-b8f9-3453708fa92e | -5.52495 | -60.21186 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91b54e6f-32d8-32e1-98ec-a0c67760bff6 | -7.62123 | -61.03613 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52041a84-63f1-3ae1-88b2-950a1b31988b | -9.40194 | -60.52436 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6780f6d3-5aeb-34be-8052-e9703281e8c8 | -7.27363 | -57.66896 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51c607c1-b36a-31fb-8b59-c3d2291e15b2 | -6.6253 | -58.55475 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 908e0146-b7b5-3c50-aae2-a47bfae09413 | -7.38529 | -64.34672 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08c79a54-9526-3a22-92c3-5ee6ae7cba05 | -9.17523 | -59.4557 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f316f18-d513-32a6-b8ff-25ff02f0bd08 | -7.35659 | -57.62561 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fbfbb64-9735-3d0e-aa15-ccd6c87190b1 | -6.81546 | -58.97128 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf4d482c-63e8-38c7-9aa2-1789895c3d6a | -9.56993 | -55.37606 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c62908ef-8788-3767-b312-2730a2760fe0 | -10.0864 | -62.89513 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5c588a4-1441-37c0-977f-97f54436e052 | -8.89797 | -60.76134 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4d2171-37e2-35ba-a5d1-1e52b0f3f88f | -8.35115 | -62.94159 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f3ac13-3637-3b9a-8be9-da0898297f8b | -8.92939 | -65.93732 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef587b38-8647-3054-a51b-51dbc976f0a2 | -9.79406 | -64.24731 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b12e5d18-13e1-3c58-a1d1-454888f0edf5 | -9.02662 | -65.72353 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33c2e159-7f27-3cfe-83ff-ec0f47bada50 | -9.65197 | -64.99428 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e93ab614-af7f-3895-ba48-851bf4cb8b0a | -9.23865 | -60.8237 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a920c76-4ed0-3d6e-9d1c-e15fc28329ab | -9.01485 | -65.69711 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71a60036-2817-3b3e-98c3-26005f0b1519 | -9.1717 | -59.45453 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1124be02-f760-33ca-8cf6-34a6e905f588 | -8.8553 | -62.43509 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1766616a-c8bf-3650-939a-5690856885f8 | -9.14652 | -60.78338 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 560e61a5-535f-308a-9b3f-de4f8c946b39 | -9.1881 | -59.52547 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8bfe630-780d-3a4b-9b51-1ce13b4961ef | -6.30758 | -59.86661 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38a2e40-d2b7-39b2-a7c0-97ac52e8614a | -9.4014 | -60.50627 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25e4fa82-b1c8-3506-8276-b96e8ed8d496 | -12.87633 | -48.10752 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5859876c-eb1f-307a-b33b-b10e1db5a920 | -11.31682 | -55.21465 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c2f9928-4852-3119-a9c2-8e343d02919c | -8.90018 | -60.76899 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc2a47f8-e020-3a8b-b12b-4f735f8058ca | -9.19639 | -59.53743 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5db5293-efa6-3222-a432-79ab06e0e098 | -7.60678 | -61.62593 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79000a9b-d0e9-3dca-bc51-54d9d565cea2 | -9.41008 | -62.48235 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2651ad0-2914-3182-a30e-55259af1f9ec | -7.2561 | -57.68536 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bb08eab-3708-3cca-9230-7f0ed1a71324 | -8.89854 | -60.75778 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 301e04fe-052d-3baf-9100-897db4cc57f2 | -5.42425 | -60.15973 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 048b7322-53cf-3507-bbab-e2f4d416bdfe | -5.80454 | -59.21444 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd4a1354-b7fa-3ac5-b234-9b491b1bc947 | -6.23809 | -60.00615 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d10922dc-0022-3464-9dfe-0a33596d0686 | -11.32083 | -55.21526 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c5e05d-6f34-3efb-94c9-5c2467529e80 | -8.91784 | -65.92665 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7931a49c-85ed-32ce-a26d-a211fcbef506 | -9.67564 | -67.50005 | 2025-08-27 05:18:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a2a9a6-6619-350d-b3e6-d61c9b66f42a | -9.16555 | -59.5397 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e6566d3-eca6-341c-b9ef-0a060cb33695 | -8.71975 | -64.02334 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b45fa55-be0b-3868-91df-cc4656418261 | -8.85333 | -62.44711 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1027a110-d35f-311f-96d7-9aa042f66491 | -6.87349 | -59.90312 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8081dacb-5b06-3a44-a5f0-6a4fec2cb848 | -7.34923 | -57.62829 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3761b488-d638-3af0-ac8a-b9a01c546335 | -9.15845 | -59.56352 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ceb270d7-b874-3d2f-b0cf-eb65b2b31989 | -10.09924 | -62.90591 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99ee1f5f-4a2b-318d-97cd-11b1f66d6e07 | -11.19542 | -62.64708 | 2025-08-27 05:18:00 | NOAA-21 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0994f7f6-12ce-3a66-a920-27aaa4e96077 | -9.80558 | -64.24928 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99da2f32-05e3-3856-a8c8-77efc90629d8 | -9.40913 | -60.54351 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6829b72d-0ede-36da-aa91-1038d2cf11a5 | -9.63946 | -59.63994 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d3501a6-ab8d-3f2d-84ab-bad0a5f94db8 | -8.92578 | -65.93237 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aac65cfe-bd9e-33ae-aba9-6c84ff57ecf6 | -6.55934 | -60.061 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README62.md)
