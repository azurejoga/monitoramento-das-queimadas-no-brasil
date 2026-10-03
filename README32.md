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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efacf0ad-e5bf-390c-8bf7-6a9ecc98af48 | -5.73742 | -55.73934 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b05d7f8f-7dfd-3ac4-a41d-474fb807eb63 | -3.00853 | -53.87176 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dc7de0d-e0a4-3232-9b79-08ccec137dd2 | -4.04152 | -54.22727 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f8081b2-5a00-37a7-9cc3-062abb7286c8 | -5.96209 | -55.34793 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3df097c1-15f3-3f4e-94af-640d90343b20 | -3.10352 | -50.29958 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1ce3ad4-2030-304b-91c5-89c742953adb | -3.17925 | -54.07552 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e74f017c-b098-3e8f-a145-557ec7e24987 | -3.22141 | -54.30804 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5833bfe3-a2d5-3608-af29-40ff57f80715 | -3.26912 | -54.00671 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70390630-7d3a-3322-afc3-d74adade56bd | -2.88905 | -54.11626 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bd6cdd8b-898e-3cef-b4b8-65d61ef64a2b | -3.00596 | -54.74654 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25d774be-61a1-304d-bf7c-699b65ce549b | -5.94488 | -43.6473 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5caae9bb-403a-3a06-9bdc-6faea187bbef | -1.27896 | -54.56329 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35ef8f0f-aaaa-3065-9d02-724f475bc559 | -4.71394 | -56.15158 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56d48a1-b20f-3640-af3c-c2f17c5b26f0 | -3.14247 | -53.75053 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1de1ee3-71fc-3930-93af-f0721c5f94e9 | -3.01864 | -53.89509 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7996340-7911-3503-9c9f-b57ed9ddce55 | -2.98398 | -53.26824 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d984c989-8616-3f37-b009-627ca444ca02 | -2.05023 | -56.86646 | 2026-10-03 05:16:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920795c1-417b-3010-94f8-efcf7a5b7d0c | -1.27176 | -54.5657 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8f8fe3f-c434-325c-8f47-7805cd915eb6 | -3.13346 | -53.74183 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c5790a8-571e-31a5-a5f0-16619a51da09 | -4.36022 | -47.77244 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f566b817-6a06-3933-997a-2f4a4d0ae77e | -3.07385 | -51.27408 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48658f0f-ff58-348f-8d00-40852c1b6f81 | -4.16713 | -54.33372 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7e7ab1a-d1b9-3f26-af50-a1807c72488c | -3.01508 | -54.20043 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e85c6e3-8ba1-3839-be6b-cdf8bb7e5064 | -6.05733 | -62.5355 | 2026-10-03 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f053e65-095c-3fb5-bb44-1cfd0584f0ea | -2.95036 | -54.09713 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23f3c1ac-e7a4-3e70-a438-6724c3a5e4d7 | -5.21548 | -46.02328 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d016c40a-8d6e-3a49-b3cc-e710f1628cb0 | -3.1759 | -54.07501 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a10d9f7-349e-30e0-8e01-cd9964f2c6f3 | -3.13795 | -53.73522 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e8a9cf2c-3064-3104-963a-4b79471138a1 | -5.2976 | -45.80196 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f26529f6-8204-3bae-909f-913d3960b506 | -5.88856 | -55.48923 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b27ac6d-cbd9-3f86-bb93-b190b4ab491e | -2.17237 | -49.7603 | 2026-10-03 05:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 854b1c1a-4456-3f2a-8e4d-47d17381b502 | -3.21312 | -53.94721 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9e5d5f2c-54f7-3ccc-8709-15400792a0af | -3.85345 | -55.8034 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55939537-1940-33f7-8f2a-2b36251721d5 | -2.89577 | -54.13881 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e12a120c-6115-3e05-ae6b-341bd22cfbbd | -3.8518 | -55.97553 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 211acc50-f12e-382f-809a-b3ae67294607 | -5.94276 | -43.66277 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2ba42058-3940-3a99-913d-4623ca603e9c | -2.2479 | -51.93031 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0034ce76-7727-323f-a0be-36706b0f5fb5 | -7.46306 | -54.99111 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb1027d9-519a-39e8-b0d0-64abedfee27a | -5.7301 | -43.28451 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e44d09c-383a-3405-a0bd-10f15ed2cec9 | -3.12842 | -53.75199 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6af707b-dca6-37d5-8db5-7c83c7583a05 | -2.89298 | -54.13479 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07c74d43-516d-315a-bbc8-edbfeb3a5c28 | -4.26419 | -50.74551 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 069f0746-a8a0-3b84-ba31-190040443219 | -3.13179 | -53.75251 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26283f1-525a-3189-9cc3-96e5043ad51d | -3.12953 | -53.74486 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577ff8eb-1736-320e-bf77-f35754510d2a | -3.29206 | -53.83989 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9177c903-a64a-3e39-aa49-7fc7a7f56c29 | -2.89411 | -54.14929 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e535874-c7f8-3e83-a6f5-2b993eae3d70 | -3.71435 | -50.66181 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5345bc3c-4a41-3c25-9fd9-90d851356365 | -3.01528 | -53.89457 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68283b78-6249-32c4-82b4-63ae04228fd3 | -4.71059 | -56.15105 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c09f769f-a35a-3490-ba12-b831ee992033 | -3.95619 | -55.32205 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5858d8-116f-346f-b3e0-341587224246 | -4.45472 | -47.92368 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e31a452-7e75-3d86-94ea-7aaae411147d | -3.2842 | -53.82408 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c7ab865c-7d2f-3a3e-a858-2fc5614c3ce5 | -2.89188 | -54.14178 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f87e1965-085d-34a8-a46f-21bf92d8e42c | -4.29642 | -50.77068 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3295dd3e-eb99-35a5-a6a4-1d76548e9e5f | -3.71117 | -50.65633 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af736c92-0e41-3fe9-9628-aecf589839e4 | -4.79359 | -55.71729 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aa10e8e-c5cb-35a5-9d0b-cb01692fe692 | -1.85946 | -54.89165 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dbd722f-ece3-33a5-95fa-e1874f6b6ad3 | -6.21507 | -53.27048 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c6f1c0a-97c9-3cd0-998c-6bc40c582cc3 | -3.67323 | -54.18839 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78d7e9ad-ade4-341f-b697-986cecc1ca08 | -3.35326 | -43.3816 | 2026-10-03 05:16:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b0928fb-2f51-3a97-be0c-18c89af0efc6 | -3.84959 | -55.96798 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c06c22e-7fd2-3b56-b29a-dfc3fcf45305 | -2.92862 | -54.1045 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b41891b-7da9-36d5-a76a-34322e90b839 | -5.86357 | -53.47686 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a394358d-ab37-3051-8164-e555a957e751 | -2.33848 | -51.94703 | 2026-10-03 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d577a5bf-2ee9-3488-a655-bbda5ae0d4a7 | -2.27605 | -48.74433 | 2026-10-03 05:16:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1899d13-8c83-345b-9092-2b668fc5060b | -5.86223 | -53.47355 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 532cd396-d88b-3dde-b219-6964972b0a53 | -1.76752 | -55.02609 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2d52ced-affb-3fda-a7de-ed62b73e0598 | -2.89682 | -54.08877 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 192efb60-2bf5-3024-8040-1b9437d135b9 | -6.0464 | -59.93226 | 2026-10-03 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59c03ed7-7b31-3651-9111-5eb2ee906b7d | -3.53795 | -55.52908 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c4cd437-885c-3baf-ac09-14257d5a2f01 | -3.26456 | -49.52328 | 2026-10-03 05:16:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe8b091d-de3f-34e9-b8df-9f55a0ac8091 | -2.90691 | -54.13339 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 469c36d5-f9d9-3c27-92a2-c7d0196279f2 | -3.09921 | -51.08943 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9911c0d-99d9-3f13-8dbb-28ddd67dc8a5 | -2.46225 | -56.07921 | 2026-10-03 05:16:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b765f79-f059-3727-aca6-0d54965f9679 | -3.71043 | -50.66124 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 020c1031-b5fb-3d60-9b17-d1b595d5707b | -3.01247 | -53.89051 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e8dbe54-81c8-3e9b-b2a3-6f39a4a9fda1 | -1.24723 | -55.87832 | 2026-10-03 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90bb5fa1-afc5-3c78-b677-e3cca43e6b5d | -1.49653 | -55.82957 | 2026-10-03 05:16:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74cc23bf-bf33-39db-92ae-d748418827a7 | -3.67658 | -54.18892 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f618bc4-a3ff-3053-8439-eab05f7f3f77 | -3.4116 | -52.83366 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| caf87274-b307-3721-bf55-33687be66698 | -3.1239 | -53.73669 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| eea820e2-5bd1-3a0d-bb6a-bccf82eb3f29 | -5.8651 | -53.47784 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc901aae-58ff-32c3-9fd5-0d97a6df437d | -2.91021 | -54.09085 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 446a2b52-cc40-3d03-b6f0-a2f36d1d4063 | -5.25501 | -55.92547 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43103e10-7b67-3fb2-8437-82a59ffc9a75 | -3.28757 | -53.84647 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b38848d-c328-3cbc-a49a-254dd0d5350f | -3.12616 | -53.74434 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75ee3303-ef53-355e-96f4-bd31606c831e | -1.2795 | -54.55984 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5adf6de-61f9-357f-9ccf-b0c32dbbce35 | -5.09453 | -56.25494 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91558444-9783-3ea7-9f2c-48b222d0bc8b | -5.61873 | -57.23444 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2780951a-a4d9-3442-baef-09242df0e06c | -3.12783 | -53.73365 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 17d6511e-a5bd-3010-afe8-140f1fd48670 | -3.00409 | -50.47304 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 719398c4-4b68-3f8a-910f-bb0eadd279f1 | -5.97044 | -55.3813 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62736dac-ff22-3e6a-a9a1-c1653d31d21d | -5.63419 | -44.36555 | 2026-10-03 05:16:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5e33838-b572-38ea-b0d1-b1d9dee2b4bf | -4.04782 | -51.08656 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8757b2f-f80c-339a-88b3-1787994a1842 | -4.26811 | -50.74609 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f72adc9-9af1-3fc9-b932-663bba6d1cfc | -3.28981 | -53.85409 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e6bd5cc8-17c8-3b53-9fb3-37750d3e0f36 | -1.08457 | -54.10818 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e75241-f6ec-31e6-b0c8-817908725b5c | -4.2929 | -54.80019 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39248c89-c852-3fbe-b381-d4d04ed17c70 | -3.27418 | -50.08659 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a8f5f71-e197-30a6-9f4e-7cfd31268491 | -4.78748 | -55.71276 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README33.md)
