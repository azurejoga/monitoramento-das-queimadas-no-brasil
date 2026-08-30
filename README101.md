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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b745b76b-95b2-3b83-9fa9-d6802e330105 | -10.8804 | -50.4965 | 2026-08-30 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 97171612-7744-33bf-b0d3-37ac34447293 | -3.1267 | -61.1811 | 2026-08-30 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b6c4f605-ca7c-3f59-847b-6c15102dfb92 | -8.631 | -66.5473 | 2026-08-30 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f5811bd0-f187-3797-a44b-717b6fa1316c | -19.0744 | -57.3876 | 2026-08-30 17:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 59647552-b310-3e79-a391-295f184d6e4e | -7.9425 | -44.2538 | 2026-08-30 17:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| b1d20da8-e542-3413-b746-261690affd89 | -11.2255 | -45.3294 | 2026-08-30 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| b9ee3c40-d70c-3ae6-a37e-3726752b0c03 | -6.6541 | -59.4452 | 2026-08-30 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9c12a315-63e6-34f2-8bff-edcd3f91025f | -5.8721 | -57.5569 | 2026-08-30 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 08958cd7-b882-3166-ba67-66608a91728e | -13.3995 | -51.4397 | 2026-08-30 17:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1e48cb55-4429-379e-a8fd-2ae30d23927d | -10.8614 | -50.4985 | 2026-08-30 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e19b53c6-ec18-3594-9e25-495a0b3cc20f | -3.4185 | -61.3273 | 2026-08-30 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d66f2860-e09d-3066-8d24-1ed69791f65e | -8.6487 | -62.8376 | 2026-08-30 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 37.9 |
| d711b0e6-9ba9-3286-83ca-f7bff4df9734 | -8.4643 | -62.7124 | 2026-08-30 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 8dec3287-479c-308d-8b0d-920ba70db0a5 | -8.6163 | -54.6935 | 2026-08-30 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9ecf1e42-fc6a-38aa-950c-81edb2756f84 | -8.6694 | -49.5369 | 2026-08-30 17:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d9a54c44-18d9-3ba6-971e-748d7168d0b3 | -8.8942 | -71.517 | 2026-08-30 17:40:00 | GOES-19 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 99e4c0a5-cf1b-3a0a-904a-ef4b3501cfb9 | -10.9749 | -50.5077 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 11db5f97-7362-3ae7-8f31-48c07be806fa | -10.7598 | -54.0179 | 2026-08-30 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| a5925cbe-6c5a-355b-92c8-459621f459be | -7.5662 | -61.3049 | 2026-08-30 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fa352d94-4a98-3f39-b347-70d0c72cab09 | -19.0744 | -57.3876 | 2026-08-30 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| bc09d7c0-1a95-3623-bc51-adf1cb4af982 | -7.1122 | -48.0687 | 2026-08-30 17:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 517c24ac-b875-3cbf-837f-9ea2cb8b3a90 | -8.948 | -62.3894 | 2026-08-30 17:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 0e013d16-d2fe-3433-8940-af0ffb5d6be8 | -3.4185 | -61.3273 | 2026-08-30 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fc1c9f85-a66a-362b-8e37-25ecff12bdaf | -3.1266 | -61.2 | 2026-08-30 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f8d2ce36-71cf-3164-911a-2e1f23151637 | -13.471 | -57.0373 | 2026-08-30 17:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 0c2e0777-581a-32fa-8280-a9e8f31419ad | -13.3991 | -51.461 | 2026-08-30 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 641eb0e2-b372-37f5-ab40-fd6281530361 | -3.4278 | -58.0009 | 2026-08-30 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 8547f04b-2024-35c0-83ed-05245aa94446 | -13.4516 | -57.0592 | 2026-08-30 17:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 243.0 |
| c113cf89-48ec-3ec3-aa4c-e736284c2e38 | -5.9636 | -57.6704 | 2026-08-30 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| a589d16a-3696-3b1c-97b3-7e7efdd5184a | -11.2294 | -45.099 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 144de246-a01e-3d67-acad-68b2042ef01c | -15.2478 | -53.8666 | 2026-08-30 17:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| aa74a8e1-3246-3687-a9d6-c0c95d742448 | -8.0257 | -72.8223 | 2026-08-30 17:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8d0ff97a-aab4-33f2-8486-37061b15c4cd | -11.3431 | -45.1521 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 0c253df2-0857-3346-a69d-4a706c5315a9 | -7.6155 | -44.8376 | 2026-08-30 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 881cecb5-5829-35bf-becb-f346d0db7135 | -15.3651 | -53.8097 | 2026-08-30 17:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| c2943297-8e71-3d04-930c-a720ed8c893e | -8.3944 | -72.5825 | 2026-08-30 17:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 42db3033-48db-3b61-b9fc-f536ff534a8d | -5.982 | -57.6697 | 2026-08-30 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5d0a5426-8ffc-3d55-9803-4c3a2d0e6e7e | -11.0054 | -49.6893 | 2026-08-30 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 380d3c36-718f-3cbb-8232-2e136fe8934b | -10.5593 | -50.4663 | 2026-08-30 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9219e824-9c14-31f2-9494-20ff99e9841f | -8.6311 | -66.5287 | 2026-08-30 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 1e7c0861-0628-368b-a771-eb3baf6ca291 | -6.6726 | -59.4445 | 2026-08-30 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| cad900c1-8f5d-3bd6-8b08-94aa889d64bc | -9.0797 | -65.491 | 2026-08-30 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 94fc0dd0-50be-3d21-a2e3-adcfa372b144 | -6.6541 | -59.4452 | 2026-08-30 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 90fb3cb3-db2a-3d30-af7d-878934fbc955 | -11.1939 | -53.9993 | 2026-08-30 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 4d91097e-3aa8-35cf-a157-65c6b78f8f17 | -8.7991 | -62.4715 | 2026-08-30 17:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 57fa33f5-1ef3-3c67-8a8f-0de425db8202 | -8.5739 | -66.9754 | 2026-08-30 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fcbe2d81-8c2b-30b6-b9fc-4df54b6a6146 | -6.9514 | -59.0666 | 2026-08-30 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 75347efd-ce76-3456-9af0-beac50e7b73f | -19.074 | -57.4084 | 2026-08-30 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 782b6ae5-c3a7-359f-b294-7c605b282837 | -10.8046 | -50.5046 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e6e48f6c-07de-3461-ba49-71ad5fa163ba | -10.8425 | -50.5005 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 666b7b36-0f72-3d61-9367-59946f61ef9f | -19.0944 | -57.3849 | 2026-08-30 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.7 |
| 6280ae04-e73f-3900-8b99-eb4af8e6bf7e | -11.0244 | -49.6872 | 2026-08-30 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| a70bf70f-2ee6-3385-a9c2-34a2c8a5130d | -11.1631 | -50.594 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 20d67414-d8fd-3e28-90fe-a1cf791e6bba | -10.5596 | -50.4449 | 2026-08-30 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 90839006-e9ea-3f65-9ea7-1f998ea1ff30 | -8.1345 | -45.4923 | 2026-08-30 17:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 4e0a9490-62b0-3a3d-a4c6-f1b9072a7b06 | -7.1123 | -42.7727 | 2026-08-30 17:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 241.8 |
| 776b0a7a-b720-3914-9e72-9349653d40ab | -19.094 | -57.4057 | 2026-08-30 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| f46fcb93-cded-30eb-886f-188da68aa9cc | -9.908 | -67.0131 | 2026-08-30 17:40:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 3163ca95-962d-34c3-b0e7-d84d3e6f6150 | -11.1634 | -50.5727 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 2337b697-80f4-3a61-9d5b-89f4781796e2 | -10.9935 | -50.5271 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| bb8cd883-55ae-32be-bbaa-40379b48fe43 | -11.2443 | -45.3497 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| a1fb1c2a-09bd-3e07-ac50-d989e59fa851 | -11.2298 | -45.0759 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 24b4f058-5a5a-3286-a572-eb87c0a7abd1 | -6.0923 | -57.7238 | 2026-08-30 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| b642f3ee-31d8-3fce-881a-0c9b7415d9c1 | -21.038 | -57.8074 | 2026-08-30 17:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 9132e718-7cc4-35a2-98fe-60701518a12a | -9.7559 | -67.872 | 2026-08-30 17:40:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7126da07-0c78-3370-8ca6-4a0098f0a914 | -7.1121 | -42.7963 | 2026-08-30 17:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| e6fc1094-5a34-398b-ac52-49eb22fe655a | -10.8249 | -45.3382 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| b586f3f1-a00f-3b88-a917-f6f5652d0396 | -8.5555 | -66.9574 | 2026-08-30 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| cf1661b8-9d91-3c31-bd9d-4b47c259fc54 | -3.4002 | -61.3276 | 2026-08-30 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| dfb097e2-f9f9-3a68-bd76-050257cd7a2f | -9.1662 | -60.2752 | 2026-08-30 17:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 19cbe989-78be-3493-bd1f-fb3b13f2a426 | -8.3718 | -62.697 | 2026-08-30 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 06b6d0dd-9d5c-3a6b-8a87-1b06a05afa62 | -6.7699 | -55.6644 | 2026-08-30 17:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 90d0da76-af34-37c6-9040-e11e72cf3103 | -10.8235 | -50.5026 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 07483d2f-9311-3ea8-bd8f-5ff12bfbf47c | -8.1534 | -45.4904 | 2026-08-30 17:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3d53b866-3604-3ee4-9ba8-ff3ad812677a | -6.0 | -45.0889 | 2026-08-30 17:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 8c34ab33-28bb-353b-8fce-bc1f607a0421 | -10.3202 | -49.9782 | 2026-08-30 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9b451500-cb13-363a-9c6b-20f0f4181c4e | -6.7514 | -55.6654 | 2026-08-30 17:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| aff18e73-df4f-3761-a25a-ae8177a833ac | -11.2255 | -45.3294 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 3f9bd33e-9885-3557-aac2-1ffbf6385103 | -4.1516 | -60.6878 | 2026-08-30 17:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 432.1 |
| 25aae82e-0172-3c3e-831a-1d39a9ed4ca2 | -10.8614 | -50.4985 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 586248a6-e8e4-39ec-8413-f39e91a4f446 | -13.4187 | -51.4372 | 2026-08-30 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| bec274cd-9b70-3485-b839-b10bc048559f | -7.529 | -61.3635 | 2026-08-30 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 7973111d-6480-314f-8fc2-21fdcdf288c7 | -11.0057 | -49.6677 | 2026-08-30 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8d5e7b89-9168-3bba-b84d-74fe3cf99ae6 | -8.6161 | -54.7137 | 2026-08-30 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 180e55ca-20d9-307c-bad8-b143238b198f | -10.8232 | -50.5239 | 2026-08-30 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 3282a8fd-e555-30ce-a11c-adcca1316244 | -3.1267 | -61.1811 | 2026-08-30 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2ff4229e-fdbf-3650-9442-6ebd162198e9 | -11.3427 | -45.1751 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 391.4 |
| b0bf9d5a-b9a3-34d2-a262-bc22139f4dc9 | -7.9907 | -46.5177 | 2026-08-30 17:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| c53c20ca-793e-3ac3-86a7-eb199d9b188e | -11.3619 | -45.1724 | 2026-08-30 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 6ab3057f-0986-3aa1-be58-b20729525bbb | -8.3717 | -62.716 | 2026-08-30 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5514e6b3-56b4-37b9-9dd5-3a121b38c947 | -7.2562 | -60.6302 | 2026-08-30 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |


