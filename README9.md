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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31b04996-64ff-36ec-a16f-1794b46eac30 | -7.77574 | -46.07211 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6bd92799-e14b-3cdc-b0a4-d83f9c0eaa4a | -3.64324 | -49.21267 | 2025-09-10 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dfd91017-fd4a-3c20-b3ee-00c1b13fe05c | -6.43994 | -44.05844 | 2025-09-10 00:33:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4aeb1a60-b071-39ae-afd0-20cba48d7403 | -5.7959 | -51.66884 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 18f6646a-ae06-39f0-8899-dfed4790414d | -9.08309 | -46.97292 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 875dd359-28f2-3346-9e54-1f62a3b87287 | -5.58066 | -45.03917 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 315.2 |
| 58813ea5-5f27-3c49-896a-082c42308d9c | -5.80521 | -51.73682 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5dbbbf4a-1bf5-3d8a-aa31-8a85dd41decf | -7.78785 | -46.09069 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 261c0945-e970-3498-83ec-f02041b1cefd | -8.24 | -47.85789 | 2025-09-10 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9d11eb87-0efc-3a06-90dc-5321b6c11dd5 | -9.67356 | -46.64782 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f742f464-0989-3ae6-a894-61f70251a2b9 | -7.56239 | -44.65591 | 2025-09-10 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dcd148f0-4884-363d-a0dc-a0bcae53cc0b | -11.24115 | -49.41618 | 2025-09-10 00:33:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f1d5fff-eed5-3df4-adf9-109469572627 | -5.66821 | -43.359 | 2025-09-10 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 483a7612-c977-36fa-8981-e8c0f0fd59d9 | -6.87111 | -47.89281 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1e61a118-dbf4-3f5e-81f3-ce8573aa4262 | -5.93682 | -42.78318 | 2025-09-10 00:33:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| b946ea77-3800-3734-8507-48e0449a3c05 | -9.00738 | -46.05317 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fc6e41e5-cdf9-371b-a33c-445551a85094 | -5.66109 | -47.4878 | 2025-09-10 00:33:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b37bcace-9ade-3d62-92b9-cbe8f621f499 | -6.85469 | -47.90413 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 86b62cee-2030-3e18-a750-8616cb2846dc | -8.8667 | -45.85069 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| c8d73ab3-a7d9-3e4a-819b-444836c63c11 | -8.84873 | -47.27322 | 2025-09-10 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a961ef20-90ff-348c-910f-d88c739922a1 | -10.65563 | -48.6132 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fe638374-6ba9-3a42-a8f7-6ea98d84e983 | -8.86088 | -45.8575 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 0e94dad8-da7f-3432-81a8-642b7093f91f | -6.25161 | -43.40935 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 07eeccca-7ca0-3052-9dfd-700cf39321c7 | -5.57178 | -42.92233 | 2025-09-10 00:33:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 0724ad59-cdb8-3bf8-aca7-79dcd75101c8 | -5.7249 | -45.61089 | 2025-09-10 00:33:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 924006d1-a6de-3496-9b26-4bac015f57e1 | -9.06814 | -49.8217 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 468d669c-130d-31b5-8b67-fe30bc6739ac | -6.68278 | -51.41351 | 2025-09-10 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 35b8fa46-c54a-3dc8-8a78-de91b26bf93d | -7.54301 | -48.21378 | 2025-09-10 00:33:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fb29c0e6-3878-3638-abb7-7d55b2c3fb6f | -9.60906 | -48.03751 | 2025-09-10 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 110346e7-c4d2-37fb-81b1-01a694df1d66 | -9.98886 | -50.30778 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7a2810b6-4557-3bca-8c5c-a23a708a067e | -5.74938 | -47.45957 | 2025-09-10 00:33:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a46d978-b515-3495-a6f7-4b3586309938 | -8.49123 | -51.34623 | 2025-09-10 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 287bbd85-55f1-3e3b-a0eb-0ad21d0f9510 | -7.86232 | -46.03317 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 552b74f9-9d1f-3b82-b6a4-6f31f60ecf34 | -10.56431 | -49.45129 | 2025-09-10 00:33:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5be9eed2-c22e-36d2-9681-3f48fd408186 | -5.22529 | -43.70079 | 2025-09-10 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 76e390f1-5a41-3aaa-8a63-9a034d8d46e9 | -8.06643 | -48.66937 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 7bc0146f-f080-3fdd-a630-2fe7e165c1ec | -10.84237 | -47.75673 | 2025-09-10 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2a640657-4216-3e03-bcec-2b30f03af4ec | -9.98205 | -50.33046 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 436dae94-5c0d-349c-9313-e0198343c833 | -6.33491 | -47.09878 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 11ea42f1-0458-3e9e-bee6-c51e5c85dcf1 | -8.20461 | -47.1528 | 2025-09-10 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| aa3123eb-091f-3778-a42e-e8dd8f2eff8c | -8.48347 | -40.49711 | 2025-09-10 00:33:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 23.0 |
| ca186fe8-1376-319a-8e5e-6732d65219ed | -5.68805 | -44.28158 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f6036327-cc31-3893-bfb0-4734810806d4 | -6.21027 | -43.36814 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 041f402c-a9ae-365f-affe-c0d6507540de | -5.80516 | -51.73103 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 76f8f36b-b3cb-370b-a6cf-15ea21890c0f | -6.85345 | -47.89529 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bc633beb-6a21-3764-9e98-091d05bce4bc | -9.61151 | -48.05533 | 2025-09-10 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d3ca7098-ef8e-3841-a714-93277a3c8823 | -3.63444 | -49.21391 | 2025-09-10 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b0acb581-ab0e-3a13-954b-9627db681f51 | -5.67743 | -43.34141 | 2025-09-10 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 74cb12d8-8555-3037-9a25-931846d064d4 | -7.78019 | -50.7696 | 2025-09-10 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 116a8dc0-5d5b-3eb0-b882-0f52bc598e6d | -6.86987 | -47.88395 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| b185bfce-d0a6-3256-8f20-6400762eca19 | -8.04766 | -48.6784 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2500b7ad-29f7-3121-9d6a-a8419d3453c1 | -5.53102 | -46.49405 | 2025-09-10 00:33:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9180a31c-3dfe-3991-a491-decdd2e615f4 | -9.51093 | -46.54298 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b9d84959-ac47-310b-82b0-8b5bc58cd020 | -9.61028 | -48.04642 | 2025-09-10 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e1b0caa1-c3fb-390b-8640-d370b5d12c3d | -7.74568 | -50.73082 | 2025-09-10 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 71604804-ff14-3441-ae1f-c33289ebd37f | -6.40562 | -47.33483 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d2cf04c-1236-3282-87d7-43d37527a78b | -8.74033 | -47.09343 | 2025-09-10 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 94a8fd04-87f6-3a32-a9ea-6823d790373e | -7.59762 | -49.28745 | 2025-09-10 00:33:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 70e4736a-7f97-3049-b7ad-91143014a865 | -9.73761 | -49.11271 | 2025-09-10 00:33:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4624ea92-56cd-3f27-9e22-cc06cd588a9f | -8.46311 | -48.95357 | 2025-09-10 00:33:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c192a1e4-0379-3068-a9fa-5ddc3071a866 | -8.74922 | -47.09216 | 2025-09-10 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 086dae54-1f22-3247-a968-ccf48eb21eef | -5.53289 | -42.65668 | 2025-09-10 00:33:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| e90d2f1f-67d3-3a44-b01d-d9e6e7d7cf0b | -8.05013 | -48.69632 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e0b96ef9-4f8b-3f9e-b978-559a2733d663 | -9.21352 | -50.55497 | 2025-09-10 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 39226997-4425-3199-9107-e2e80ef17c77 | -9.07897 | -45.715 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9574cbc0-93d1-3b20-a172-8ac0f5086ff5 | -11.23983 | -49.40624 | 2025-09-10 00:33:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3f671447-ae14-347d-b4ad-8b0c4657fbd4 | -5.9672 | -45.80642 | 2025-09-10 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 07b1aefd-f23c-3305-aa16-a11bc84367d0 | -8.48869 | -40.48977 | 2025-09-10 00:33:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 6612d97a-3e17-3b15-beea-9a3411fefc57 | -8.69491 | -48.89314 | 2025-09-10 00:33:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f94ebd3-3eeb-3017-9d34-5a67be330472 | -8.97438 | -46.07427 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 38b61840-c3ea-3e9e-98a9-5a575e5490e3 | -6.16841 | -42.65631 | 2025-09-10 00:33:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 3fa0b5dd-9701-34e4-9474-307b6c037701 | -9.71729 | -48.08849 | 2025-09-10 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c96a7664-ab9c-38ac-896c-1747ff0ffb98 | -4.48838 | -42.93779 | 2025-09-10 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ecdcf8ff-b62c-30a9-b213-5d745c0c9872 | -9.06659 | -46.98465 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| ba83be76-8af6-3f09-b134-fff150bea205 | -7.88648 | -46.26962 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 03dde15f-a14a-3720-bb0e-9af403314259 | -5.67223 | -45.46523 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ac90be66-74f4-31b4-a6b5-777fe71b144c | -5.69312 | -44.28891 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 55db8fb8-e608-3e31-9d36-1002e718d421 | -7.79083 | -46.06408 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| a696a2a7-275c-36c5-b933-e70ecefe58a3 | -2.38337 | -47.71508 | 2025-09-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7af90180-851c-3d9d-ab52-c28f5fbc4dee | -2.34818 | -47.59538 | 2025-09-10 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 9517bb5f-2de5-309f-8cf7-8207481b3d47 | -2.38467 | -47.72446 | 2025-09-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a2e6929a-a65f-3e69-b500-7127e0a4f530 | -2.34686 | -47.5859 | 2025-09-10 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ecd74adb-d825-35b6-8c89-ee073cf08803 | -3.04705 | -48.96674 | 2025-09-10 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 74809555-03ed-3e79-af5e-79d04a9c78d0 | -3.24861 | -52.855 | 2025-09-10 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7abef041-765c-3a07-9c37-ea42eace66a3 | -1.83967 | -54.73238 | 2025-09-10 00:35:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 4d979617-4f4b-313a-bfbc-0883029bdf0f | -3.1229 | -52.00727 | 2025-09-10 00:35:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7721d5c-cf4c-3023-b2c6-d331c33fcd20 | -2.63083 | -46.84122 | 2025-09-10 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 83e46974-50ab-3d2e-9812-77f9887ef42c | -2.33905 | -47.59665 | 2025-09-10 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 16ea77ff-dcfb-3ca1-947e-7cfe259e808a | -15.8673 | -51.8303 | 2025-09-10 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 195.9 |
| b10e0e90-061a-32b6-825d-c80108efadd8 | -5.6788 | -43.3425 | 2025-09-10 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| aafa7a43-3274-3433-b7f9-83eb229685a7 | -15.8869 | -51.8274 | 2025-09-10 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 360.9 |
| 75c791dc-6467-3032-b25b-058539f69786 | -15.8677 | -51.8087 | 2025-09-10 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1892c504-0ba3-3372-b0fa-589ddb0b7fa9 | -8.8647 | -45.8693 | 2025-09-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 4acbdd1c-0422-382b-b382-913a661e4058 | -15.8865 | -51.849 | 2025-09-10 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0f72e286-6d03-3890-89ab-b869af77c198 | -23.0342 | -50.114 | 2025-09-10 00:40:00 | GOES-19 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| c2116c30-da21-3302-8251-5dc1a86a2d10 | -7.7705 | -46.0684 | 2025-09-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 42abcad6-319c-3386-9d21-3a2438aeab7e | -6.2595 | -43.4129 | 2025-09-10 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 05372ce4-da91-3f1b-91a7-5b12c6be9365 | -13.937 | -48.2522 | 2025-09-10 00:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| bed8479a-c406-3d84-a1fb-3e688289e4e1 | -5.589 | -45.0505 | 2025-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| e66747ab-7d4a-3595-8419-1a8b6c62c4a8 | -5.66 | -43.344 | 2025-09-10 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |


[Clique aqui para ver as próximas entradas](README10.md)
