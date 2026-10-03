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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33680087-4ce2-3a20-9d17-e949d157c2fc | -6.06805 | -57.72546 | 2026-10-03 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e816d192-375a-36c8-8cda-9e9b777c6432 | -5.88596 | -55.48557 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 529f1558-68d6-3e93-adaa-a07cf156b7b7 | -4.4112 | -49.96666 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d088660-adfc-35af-be6d-93561ecae8bf | -6.91956 | -59.28201 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec04f5b8-f7d2-32ee-8d5c-5d708532ac98 | -6.91596 | -59.28143 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bce7b2a-e9c0-3dc0-b707-d9cf9f6923cc | -6.23585 | -53.15155 | 2026-10-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 241bcd6e-40ed-362e-b83f-ba993b972ab0 | -3.51411 | -54.60678 | 2026-10-03 05:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dad7a105-af1a-326a-bf5a-602ce7698e6c | -6.07201 | -57.80626 | 2026-10-03 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3570db3e-e1d4-3d55-b5b9-0cd2c288984a | -4.26861 | -50.74636 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61478cf6-83fb-3ac2-9522-3da2e416603b | -6.02019 | -53.54228 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c50ebd32-fd31-37dc-9f0f-2a560f3b4d65 | -5.8853 | -55.49012 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b0743dec-6c95-3d7f-993e-fb71df9115f9 | -12.1341 | -63.17839 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54f7e3fe-012b-3e42-b56e-ecc57ccad811 | -12.1456 | -61.17056 | 2026-10-03 05:38:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12f432af-2fc9-3809-9905-58c03193b7ba | -11.70879 | -61.76308 | 2026-10-03 05:38:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c273b8-e814-35f1-b761-494b0003b81c | -9.50781 | -65.58022 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d049480-11e8-372d-8853-bd9a925753fc | -12.14694 | -61.17019 | 2026-10-03 05:38:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf20eed7-5335-3df5-bc06-ec648ed2b21b | -9.88965 | -60.29342 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d521833-9d85-364e-b8c4-4f354270e9ea | -8.73673 | -66.57442 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90936208-ecea-3667-95d5-d98e2f320ff3 | -8.85963 | -66.78831 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41e2ac54-a6c3-3593-9117-2dd030b6bca8 | -9.54478 | -68.52248 | 2026-10-03 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a54366b-6b41-3eb6-bded-23f96ff169d9 | -9.01884 | -65.70729 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e9227a3-2ecf-348a-b00c-343bc4ba8607 | -9.31226 | -65.77432 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ead9462-8096-3fdd-b148-b49045a27cca | -9.88934 | -60.29256 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a08b722-5607-352d-8ece-56f97e0c9cde | -12.13741 | -63.17893 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348a56f7-1388-3321-9500-ff129f68bff8 | -12.12992 | -61.15609 | 2026-10-03 05:38:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a08c8f7-fd6b-3024-92b0-1ba616f2d3ee | -9.79693 | -60.14293 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0852b7bc-61e3-3c90-b44c-18a13c3a13b0 | -9.8932 | -60.29397 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb160c7-5669-352c-94f7-4af640625e5d | -9.0945 | -65.73187 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b3a0bab-4ca5-32d4-8321-9b6b376e0509 | -8.85237 | -66.78997 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e375417f-b899-3e67-94df-cf8ade7a58a7 | -9.55934 | -62.7293 | 2026-10-03 05:38:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e0f2114-2260-33e2-a123-aad633db1e8a | -9.46766 | -66.57317 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f94b3560-3f28-3599-96de-944b928ea343 | -9.77768 | -65.05604 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 134574cb-394f-3c8b-a81c-ace239c4a422 | -8.70204 | -66.73533 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cba30a84-29a3-3b1a-be21-d17dcf8a72d2 | -9.93089 | -63.98064 | 2026-10-03 05:38:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 258e3ad1-5df4-3b3f-bb13-e5755bfaaab7 | -8.7028 | -66.73077 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 429f9597-7731-3b34-b102-e46b38749ffb | -10.8451 | -62.77998 | 2026-10-03 05:38:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3b31664-2393-3eab-b475-2d40c5c444ef | -9.30872 | -65.77373 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c23ab71d-0fc6-3674-9a1a-fadc4672990e | -9.88363 | -65.1387 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d411712-c411-3c7a-b8be-8c1fb51ed646 | -12.14636 | -61.17413 | 2026-10-03 05:38:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e18f1c9b-c4ea-3617-b31b-0edd59ce299b | -9.63456 | -66.47455 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d583da3f-2fd9-38cc-b57e-3224f96fd16f | -9.88706 | -65.13928 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f965e892-961c-32b7-8e42-f30f5411c3aa | -8.85888 | -66.79288 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83c99523-92a8-3e80-85c0-736f22615ce3 | -8.85988 | -66.79124 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fec8703d-9428-329c-bbab-bafe2eb544e7 | -9.23921 | -63.63297 | 2026-10-03 05:38:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84458822-e8a1-31fa-8810-f332df15454d | -9.88301 | -65.14248 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 663aa1ad-e93b-3b88-9f0e-1417c10a3cc3 | -8.87491 | -69.23259 | 2026-10-03 05:38:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9432f56b-d42b-3b58-99d8-af0ab389dfd6 | -9.90748 | -65.03389 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30aa1273-5b80-35c2-bb10-d3af21832853 | -9.54412 | -68.52622 | 2026-10-03 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5540463-b35e-3e28-a8be-f8eb7775021d | -9.86506 | -60.23983 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5087c00b-af0e-311f-b281-7e13f12452e5 | -9.37666 | -65.47089 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8245aaf9-4161-3ac3-b4ae-2d63d13acacd | -9.90686 | -65.03764 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c24c9877-f6e5-3ff0-ad3c-4a2099512148 | -9.46444 | -62.98537 | 2026-10-03 05:38:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3325c14c-43a3-3ebd-8743-f9916b78bc2e | -10.2727 | -57.73864 | 2026-10-03 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45c8142a-8d16-3ff8-9e18-f189f13d879f | -9.3075 | -68.61038 | 2026-10-03 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 372b25a9-4bce-3cd5-a802-802ae921e025 | -9.62633 | -65.73798 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31a40c61-9377-341f-8541-2afefd6ccc20 | -9.53999 | -68.52547 | 2026-10-03 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9558db7e-e374-3a58-a735-9107e16153b9 | -9.54345 | -68.52997 | 2026-10-03 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0b728a4-bb7d-3444-980a-aee5ce2e9454 | -9.88644 | -65.14306 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87130fd9-316b-38e2-bacd-47f32ed11e2e | -8.05708 | -69.96071 | 2026-10-03 05:38:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4dbf713-d066-33af-84bb-39de1e6fb9e4 | -10.96007 | -60.91058 | 2026-10-03 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ff590e6-4f54-3f0c-bc15-4e337e682b7c | -12.13521 | -63.17134 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab753c0-5eda-3749-bc8b-1c9ba444ce62 | -16.17934 | -59.43965 | 2026-10-03 05:38:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 828afd3e-2e0f-3197-823e-b85a74d8dc7d | -8.89392 | -66.8868 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7195ef8-4099-3ddc-b91a-cca95c9b7407 | -9.75117 | -59.32297 | 2026-10-03 05:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 373b201c-4f4e-30ac-b8a7-89b56e19792b | -10.27322 | -57.73489 | 2026-10-03 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91a62ccd-6c3b-3913-805c-ae5893301f68 | -9.49969 | -66.79998 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 946d73d9-b42d-3097-b291-6b79c10aa9ba | -9.89381 | -60.28994 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43404e6e-3b04-33e9-8cfb-36cc18404d0c | -9.62215 | -65.74133 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 596aa0a1-7e8a-34c0-b323-f65f3e2a13a0 | -10.99177 | -59.13267 | 2026-10-03 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0a0da24c-5f57-3155-baca-cfc3ca61725c | -10.98725 | -59.13695 | 2026-10-03 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d67d561-85bc-3b3b-b2e2-257424f28112 | -10.98794 | -59.13212 | 2026-10-03 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f9e30f4c-ce67-36e9-98ab-0f170846bf34 | -7.70146 | -67.0817 | 2026-10-03 05:38:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 828635f1-d7ad-3b7a-974c-d7e69f19400e | -12.05856 | -58.04018 | 2026-10-03 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 185c0613-c3da-352b-b361-e6bb1570a73d | -9.95347 | -55.32966 | 2026-10-03 05:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9215840-3bac-3884-97db-275d365769f9 | -9.76968 | -65.31507 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f142187e-1d2b-38ba-809e-ad6b8c043405 | -9.15427 | -65.54489 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a37e139-10c6-3188-9bb7-c69c62607024 | -10.14051 | -61.74166 | 2026-10-03 05:38:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c075a0a2-472e-300f-b156-85526e881918 | -9.95756 | -55.33576 | 2026-10-03 05:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c111a667-e4cd-36a8-be2a-99a9d3aea231 | -9.13382 | -68.24915 | 2026-10-03 05:38:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b72d9fa1-fc07-3724-b9d0-1c069f242093 | -8.85612 | -66.7906 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37a1e992-8a88-3c1f-a871-f38f7d52d96b | -8.65643 | -66.93636 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 649e1260-7e08-305d-be00-565162cf0d5d | -12.13465 | -63.17487 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7588abc3-3e48-3942-9792-280da75c332f | -9.89348 | -60.28908 | 2026-10-03 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cbc26b6-fe42-35a0-ab25-0f5ec407ad4d | -9.48411 | -67.16105 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab13c538-325a-3bb2-8973-c93fd3747453 | -12.05693 | -58.04079 | 2026-10-03 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e15c99a-126a-314d-9bb7-0db8664776e9 | -9.37317 | -65.4703 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31525b7f-dee4-3e7b-972a-b49ad41bc477 | -8.85919 | -66.88562 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd37e571-ed50-3ffc-8cf9-fe8892fe7442 | -11.03782 | -62.56817 | 2026-10-03 05:38:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3513c95d-cd06-3ee7-8458-e38467c0bc7b | -10.95658 | -60.91004 | 2026-10-03 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d22a30c-170a-3e5e-98de-55f56ac8f941 | -9.72487 | -66.33899 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15597c93-d990-3fe4-923b-fd1eb493211d | -9.24718 | -63.51915 | 2026-10-03 05:38:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9e6c5ab-a42b-32a0-b310-7111388088cc | -9.95663 | -55.33224 | 2026-10-03 05:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9367bb0f-6a3c-3db5-8066-1ce82efa63e6 | -9.95831 | -55.33039 | 2026-10-03 05:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7712110a-daee-3dfc-abda-225f72eb70c1 | -9.90757 | -65.03454 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3bb0fae-949c-34d2-a1df-6518ffea66ca | -12.13189 | -63.1708 | 2026-10-03 05:38:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67bedd8d-03f8-3ff7-9cdf-53775957caac | -11.49907 | -61.04907 | 2026-10-03 05:38:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55b716f8-81c0-3c0c-96c6-7f89119241b3 | -9.49769 | -64.75034 | 2026-10-03 05:38:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f207a8b8-2114-3890-830c-5f3ecbd459ee | -12.13341 | -61.15661 | 2026-10-03 05:38:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be051b6a-5b08-352c-835b-f9708db412e2 | -9.69202 | -63.20068 | 2026-10-03 05:38:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc847fb-6d75-339e-b878-64d06827db01 | -8.85137 | -66.7916 | 2026-10-03 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
