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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1faa5f54-8ac6-3880-b43f-a80326611b34 | -11.63619 | -48.44703 | 2024-10-07 05:16:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b1827d6-9de8-338c-a2b7-0326f7989ed5 | -11.62995 | -48.44619 | 2024-10-07 05:16:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 269b6b29-9238-348f-9222-5b4898193495 | -5.49342 | -48.94131 | 2024-10-07 05:16:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44c70bd1-1a2c-30e0-9efd-d0163b09f1d6 | -5.49289 | -48.94498 | 2024-10-07 05:16:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c98e927f-982a-3fc7-aa3c-341e904d6a19 | -10.54233 | -49.1086 | 2024-10-07 05:16:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a342d99c-a64a-32b6-8ff4-ffbf383a956e | -10.53643 | -49.10785 | 2024-10-07 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62238b9e-324e-3051-be44-7bcc83120a73 | -4.37314 | -50.81891 | 2024-10-07 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c00144d-49a3-3090-b39e-f7b04cc3f4ea | -4.36833 | -50.81818 | 2024-10-07 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eb6cb87-5714-31d7-aaad-ea8cd7435644 | -6.55961 | -50.05787 | 2024-10-07 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a59fdb5-510a-3763-a355-818239c8af0a | -5.29269 | -50.71056 | 2024-10-07 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a294581b-34a1-31f7-9b00-614823b407bb | -11.29178 | -51.36702 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 003929f4-ec1f-3886-9a14-cb2d9f1e703e | -11.29139 | -51.37009 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6834f3ab-8f53-3dbd-86ec-0cd3a67ece00 | -11.291 | -51.37315 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5bd4f5-f657-3313-a40e-f1d7f13031fa | -11.29061 | -51.37622 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63634bad-86d9-35f5-85f8-e633d398ddaa | -11.28625 | -51.36937 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0503308c-561a-34bc-8cc0-d42d1abc5d93 | -11.28548 | -51.37552 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ecaccc-5298-3719-ac95-5781b0a03a33 | -11.28509 | -51.37858 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b286f27e-4a59-3cd3-9903-88e4b518cfd5 | -11.2847 | -51.38165 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c61a53e1-51fe-34fa-a357-7147b9ca7d06 | -11.27239 | -51.35501 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b07db594-16bc-3212-bf01-0775998381b7 | -11.272 | -51.35808 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d23696e6-d929-3016-b8f0-b1cdc35b54d8 | -11.27161 | -51.36115 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4f7e4c7-0264-368e-bdab-f3141a52ca81 | -11.26226 | -51.39415 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03f9a508-54bc-3064-bd2f-39c9c55982fe | -11.25751 | -51.39039 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0a2c5ff5-2695-331b-a716-12645ef797f5 | -11.25713 | -51.39345 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c2bf1a0-5738-328b-a7e4-5550d7315e0a | -11.2484 | -51.37981 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c48ea0b-fff7-35dc-9621-f85ad28bb89c | -11.24802 | -51.38287 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa20ae06-3ba0-3496-bbf8-d4e97c721e20 | -11.20513 | -51.88662 | 2024-10-07 05:16:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b23269b-cb64-3959-b55e-886c0fa5afc7 | -11.20413 | -51.88571 | 2024-10-07 05:16:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a53b0c8-8bfa-3fc6-a92b-3f0417d77c5d | -11.20019 | -51.88589 | 2024-10-07 05:16:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d565a0fa-c0d9-3abb-b176-39694395bc48 | -11.19947 | -51.89153 | 2024-10-07 05:16:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63a1c5ca-69bc-32d7-9127-54d060497412 | -11.19843 | -51.89061 | 2024-10-07 05:16:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0450e75-84f4-30f3-a218-cfa403175698 | -5.77547 | -51.44921 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ebece10-a0b6-3bcb-aeb3-34684743909c | -5.77474 | -51.45416 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79220595-0a14-342c-943e-008532b67e28 | -5.77003 | -51.45354 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5c3cbe1-236f-3309-97d4-e1db8554ce5d | -5.76604 | -51.44788 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ac17d6f-42ff-3b06-8ef4-53c9d507d331 | -6.44307 | -52.83858 | 2024-10-07 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2f72135-7dc4-310f-b691-5dbeef88309b | -5.92583 | -53.42111 | 2024-10-07 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83dd1bb2-74b4-3732-9b57-bb3b72aff578 | -7.98255 | -54.76397 | 2024-10-07 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ecab699-b798-38c9-b289-fd7fd9b5c787 | -7.97866 | -54.76339 | 2024-10-07 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bafd117f-f341-3874-862b-a173c8a10957 | -7.86391 | -54.89226 | 2024-10-07 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a3452ae-f23d-3923-95dd-57a22cfc8188 | -7.8632 | -54.89703 | 2024-10-07 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac8f6417-a0de-3a07-82d3-a43ff04ef33a | -7.86006 | -54.89169 | 2024-10-07 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cc89d1e-e7d1-3781-b37c-1a1816ef9643 | -6.9594 | -59.05804 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 285ac0f3-3dfa-36bc-b79f-a4eda7000dbb | -6.95608 | -59.05751 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93de734c-52ff-3375-81b6-209460df25d2 | -6.95275 | -59.05698 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c8a310a-4974-318e-b11b-d780625d8fdb | -4.28826 | -60.01676 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33516a40-13da-3f50-bcb8-45cf5e088c7c | -4.28486 | -60.01622 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f1bde54-fd79-3672-a381-f1f6afaf3689 | -4.28145 | -60.01568 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7db2b5ce-958d-3d6b-b892-84d0ea008050 | -3.96472 | -59.19334 | 2024-10-07 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46f1595d-c226-3299-a8fd-15e92fd4cf87 | -3.89458 | -59.72869 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cac632e-5e0f-3c54-b6f0-a9e2f8eca315 | -3.74544 | -59.32825 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3415f7be-b970-34ab-8fad-2fa19b318202 | -3.74488 | -59.33178 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccf25ed4-c957-377a-a1b2-121467d37d2f | -3.74152 | -59.33126 | 2024-10-07 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 938d8674-d5ba-326e-a4f0-0a1e0c88b41d | -7.15559 | -59.38091 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 428594de-6af5-37a2-9df9-657f079b5269 | -7.15504 | -59.38439 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6caabbca-bf6e-3fe3-b0da-2b46981c066a | -7.15494 | -59.29871 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc5cd35e-b801-38e3-9480-a85b97d312d1 | -7.15226 | -59.38038 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d52980a5-6822-3115-8673-43e8ae2b3b71 | -7.15217 | -59.29471 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 517e8c91-afb7-3722-bb85-f811892789bf | -7.15162 | -59.29819 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0758a56-8596-3e98-a023-c402b6253fed | -7.15107 | -59.30166 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf457341-0209-356d-89a4-1452f783114e | -7.14884 | -59.29418 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f11cdf2a-42b1-32cd-a8eb-1d6b4659949b | -7.14829 | -59.29766 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a5cc1f6e-06e9-3469-8ca2-193b8a26cbe4 | -7.14552 | -59.29365 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 91cb85d3-f97c-33af-8a1f-6f31272f9ec8 | -7.14497 | -59.29713 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9f1401a7-b107-3e6e-908e-2cab665af045 | -7.14164 | -59.29661 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3e2a67d4-7379-3789-a849-9e1b3ce5fae4 | -7.13777 | -59.29956 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f45bc915-e66c-33bb-9d1f-aa46bf1eef21 | -7.02652 | -59.40343 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4acc659e-8726-393b-a091-003dc71ead33 | -7.02319 | -59.4029 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86619642-686d-374d-87af-6cc4631537d3 | -6.80281 | -59.14734 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41d63157-f00a-3866-8cb5-ebe7f6cde6ff | -6.78643 | -59.35861 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| adf55fcd-c9ec-3c50-b5e5-20fa60178a57 | -6.7403 | -59.67037 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcb64d62-708a-3110-82d1-f2d8add6f595 | -6.73588 | -59.63369 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bb5f82-8f2f-39d7-848c-012286e2ec48 | -6.73532 | -59.6372 | 2024-10-07 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa4b141-a007-3948-9c87-91c6b28467e5 | -2.95527 | -60.01519 | 2024-10-07 05:16:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bc33996-fca5-319c-8a2a-59f292828d81 | -3.77941 | -60.12317 | 2024-10-07 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25b51840-1e73-34c4-8559-bc191ad4ea56 | -9.74016 | -63.99566 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 691e3e10-9267-3892-8027-8d1422c2ccf8 | -9.73713 | -63.99005 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cc27847-85c0-3070-815b-01d56a6df5c9 | -9.64446 | -64.22446 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d35f26f6-7798-34d0-a0e0-c159f18256ab | -9.63965 | -64.22881 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07225876-fbf8-300c-8391-709c63988c32 | -9.44259 | -63.62774 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9405702-0ef7-3bfa-bd14-661817b8e161 | -9.43957 | -63.62245 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a83b4f-f5fb-3def-9225-efad9a2b4799 | -9.43877 | -63.62715 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 749ca7c4-38a4-3a97-b562-7ee3c821ab50 | -9.35909 | -63.80643 | 2024-10-07 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.1 |
| a9ec5160-77a6-3a85-8555-f6bd644cea37 | -6.82085 | -64.32564 | 2024-10-07 05:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28124816-1463-3cf1-92e3-801ce0613410 | -6.81321 | -64.3205 | 2024-10-07 05:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 711d30f1-2fbe-3ee0-b53b-4d2faa3bb98a | -8.82292 | -64.22449 | 2024-10-07 05:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19fde0d5-f6bd-3741-9e6a-a34e78b25f80 | -17.27538 | -56.1912 | 2024-10-07 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2a928d05-ab26-313c-ae8e-04133b6af0ab | -17.26729 | -56.19005 | 2024-10-07 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 444bb31a-9fad-338b-9f94-08282de42f3d | -17.27943 | -56.19178 | 2024-10-07 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 11a3d5d4-b5ed-3431-ba35-50603a59883b | -14.21473 | -46.45501 | 2024-10-07 05:18:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef85a84e-74fc-30fc-a51c-9848d58b70a6 | -13.09016 | -46.3464 | 2024-10-07 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cfc1e05-c568-30e6-9a8d-c1a8f686615f | -14.20887 | -46.45213 | 2024-10-07 05:18:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34f359b4-5d70-32a0-89a0-259889d85796 | -14.20823 | -46.45893 | 2024-10-07 05:18:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f569190a-a6a5-38eb-967f-bb4a62dc0775 | -14.20689 | -46.46032 | 2024-10-07 05:18:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4152bddc-aac3-377d-b564-7cc90556abf8 | -16.13526 | -48.89513 | 2024-10-07 05:18:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bcaac891-8104-3a6c-994a-aa1b3f35a8e5 | -16.14162 | -48.8962 | 2024-10-07 05:18:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9fabe966-3f9b-3920-aa62-5f89d740677f | -16.08629 | -50.21603 | 2024-10-07 05:18:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c8ab7ef-9e72-3ed7-b911-0d6ad11c8ac7 | -16.07375 | -50.22174 | 2024-10-07 05:18:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f260781f-1823-3261-9260-7b2e716ce436 | -16.3105 | -51.28294 | 2024-10-07 05:18:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 930966fb-530c-30cd-b031-b2f6858eb0e4 | -17.14289 | -51.7103 | 2024-10-07 05:18:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README112.md)
