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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a169c1bb-6285-378d-8153-57af779fd213 | -6.586 | -44.1702 | 2024-10-13 00:58:43 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5308e4e-2675-3dd1-9ecf-72ae502b90d6 | -6.5763 | -44.1726 | 2024-10-13 00:58:43 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e349f107-c51a-3d31-886d-488ffcf2820d | -7.8389 | -49.470299 | 2024-10-13 00:58:43 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f7290d-c0d9-3a35-ab8e-140af1c3916f | -7.8405 | -49.477402 | 2024-10-13 00:58:43 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379e9447-d1b1-3425-9866-7ace5ed0ec46 | -6.5324 | -44.414501 | 2024-10-13 00:58:45 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9f0e066-88db-3d86-af7b-8da0cf7f9a86 | -6.5357 | -44.427799 | 2024-10-13 00:58:45 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1dcb160-d98b-3eec-bb55-d8025b0e3cae | -6.5227 | -44.416901 | 2024-10-13 00:58:45 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13dfbcaf-c217-3699-8e51-56f5ee1f1673 | -7.0182 | -46.812901 | 2024-10-13 00:58:46 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d655ec1-63ee-3366-8155-11bd88b814da | -7.0204 | -46.822201 | 2024-10-13 00:58:46 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df88975d-bd75-3492-b553-51482e6cbb20 | -7.6296 | -49.4132 | 2024-10-13 00:58:46 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27f05140-ee4d-3eb0-9d69-954beb6b2e79 | -7.1327 | -47.599602 | 2024-10-13 00:58:47 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5de53c33-7dff-3b85-85be-619b7eb8a08c | -7.7737 | -50.171398 | 2024-10-13 00:58:47 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 747252ec-994c-3a7e-8f7b-a3855ffed44c | -6.4125 | -44.514099 | 2024-10-13 00:58:47 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9494f191-7cd4-3c29-b828-071bf2a3566c | -6.4028 | -44.516399 | 2024-10-13 00:58:47 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c183e2a6-a180-31a9-aa54-302845b7ec02 | -7.5727 | -49.568802 | 2024-10-13 00:58:48 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b323d88-9351-3151-8ff6-88106781b9b8 | -7.677 | -50.2444 | 2024-10-13 00:58:49 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3059ea6-d7e1-37b3-b73c-c1714bdd753a | -7.6786 | -50.251301 | 2024-10-13 00:58:49 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c36b963-764b-3a5e-a20b-22a9c296bfe8 | -6.4139 | -45.668499 | 2024-10-13 00:58:52 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2761b667-bf04-36f3-8a15-c2cc946c0467 | -7.0236 | -48.319599 | 2024-10-13 00:58:52 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24dd1832-e693-3333-84e3-ee4380ab4c84 | -6.1331 | -44.720299 | 2024-10-13 00:58:52 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9e84091-d4ba-3914-b5a1-2b4e65ae68d3 | -6.1362 | -44.733299 | 2024-10-13 00:58:52 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3ff6976-1dce-38e0-9693-f6ac678c207a | -6.0785 | -44.6227 | 2024-10-13 00:58:53 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbcc3756-a233-342d-8488-fe10cfcc38b6 | -6.0688 | -44.625099 | 2024-10-13 00:58:53 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0584f970-f0bc-3786-a452-1e305d51605a | -6.072 | -44.638302 | 2024-10-13 00:58:53 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27286b03-812e-33b9-9ac6-724a8f27c936 | -7.1526 | -49.447399 | 2024-10-13 00:58:54 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae70c536-728f-3b51-a846-34b4f339f49c | -6.7404 | -48.168098 | 2024-10-13 00:58:56 | METOP-C | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 382d7b8e-3185-3ab2-a72c-ed9073bcc0ca | -6.7423 | -48.176102 | 2024-10-13 00:58:56 | METOP-C | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 68dd90d8-b3f8-384c-83f3-59419fe55dce | -6.2467 | -47.387501 | 2024-10-13 00:59:01 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca3d4591-0c24-3793-a0b4-ef5cdfe96243 | -6.2348 | -47.380901 | 2024-10-13 00:59:01 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffe26907-7a5d-36a8-8a67-709c4f7e6dd8 | -6.2369 | -47.389801 | 2024-10-13 00:59:01 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee3eb894-b0cb-34e6-83dc-db2b9e37ba16 | -6.1346 | -47.262798 | 2024-10-13 00:59:02 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef2462fc-520b-3cb1-aba7-ee10f0b14a12 | -6.1368 | -47.271801 | 2024-10-13 00:59:02 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 683de64a-cae5-3eaa-9819-09a912217fc2 | -6.1389 | -47.2808 | 2024-10-13 00:59:02 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 538ca624-a76a-3137-82a7-9659e10a67f6 | -6.1248 | -47.265099 | 2024-10-13 00:59:02 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f09bf13c-0c0e-3e29-b6af-72280d41d953 | -6.127 | -47.274101 | 2024-10-13 00:59:02 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9259e9e7-45c4-3a63-a286-8cd0e1a24d28 | -6.1291 | -47.2831 | 2024-10-13 00:59:02 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30543545-0b74-3173-9afe-859d5fcfae93 | -5.8688 | -46.448299 | 2024-10-13 00:59:03 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47296f3a-07ed-3904-832f-dbf92c8d4e31 | -5.8712 | -46.4585 | 2024-10-13 00:59:03 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 472ac846-efc9-3906-a3da-b0e00f7f3214 | -5.5722 | -46.156101 | 2024-10-13 00:59:07 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c9fcdb3-d0c0-3a8e-b6f4-ffcab6510c26 | -5.5747 | -46.166698 | 2024-10-13 00:59:07 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5cf685d-c342-3e04-9008-04247c7e48db | -5.5624 | -46.158401 | 2024-10-13 00:59:07 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6751ab07-aa7b-3214-a7a4-658d338d1310 | -5.5649 | -46.168999 | 2024-10-13 00:59:07 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f76efd-1f72-38a6-8c4b-893da85692f0 | -5.4715 | -45.8214 | 2024-10-13 00:59:07 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecfbca23-3b37-3fa8-b0ea-3bb1a743e2a2 | -5.4742 | -45.832699 | 2024-10-13 00:59:07 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d93a6a2-7bbe-30b3-bc49-0d0177c382a1 | -5.1956 | -44.931099 | 2024-10-13 00:59:08 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2628ac30-e019-365c-a58d-c8f13bd475df | -5.1987 | -44.944 | 2024-10-13 00:59:08 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e93a8ce-ff52-386c-8aa7-eda70220576c | -5.189 | -44.946301 | 2024-10-13 00:59:09 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2b451b-6609-34e4-9d8a-3074d1863830 | -5.0536 | -44.854198 | 2024-10-13 00:59:10 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8fa8c38-6fb6-363b-b3aa-1677f4bf95ea | -5.0407 | -44.8433 | 2024-10-13 00:59:11 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e9efb9-b964-3ce9-9ebe-80a2b1489d92 | -5.0439 | -44.856499 | 2024-10-13 00:59:11 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05b54a20-e4ba-3327-a7c9-9819ca519c12 | -5.4937 | -46.7785 | 2024-10-13 00:59:11 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dad9eed0-8473-33a1-8d96-18e483459fda | -5.496 | -46.7883 | 2024-10-13 00:59:11 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19af4327-ce89-3fdf-ada6-4b4fcdfa1b34 | -5.4983 | -46.798 | 2024-10-13 00:59:11 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 969c97b8-9498-3126-a454-22a293a806b6 | -5.1394 | -45.382099 | 2024-10-13 00:59:11 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 375a2245-f4ab-3804-aaad-6f070fc3b00e | -5.1423 | -45.394199 | 2024-10-13 00:59:11 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bcb686b-1cce-34e2-af14-8fe090208356 | -5.1453 | -45.4063 | 2024-10-13 00:59:11 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba20aa75-f0aa-3f9f-b960-6851441e5b77 | -5.1297 | -45.384399 | 2024-10-13 00:59:11 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb35576-e627-3bb5-b155-f9f6efef6692 | -5.1326 | -45.3965 | 2024-10-13 00:59:11 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89e489e7-5db7-3446-9339-dd693e115ebe | -5.1355 | -45.4086 | 2024-10-13 00:59:11 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c99e9d8-5229-3a45-bb38-ae9e2887dc90 | -5.5296 | -47.1036 | 2024-10-13 00:59:11 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c289f661-c820-3b89-91ec-c03f6156e30d | -5.0945 | -45.838902 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3f1347b-4380-3db5-ad40-6ede3825beaa | -5.166 | -46.138199 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a28e8703-8621-338e-8177-3d1fe4a4e7dc | -5.1686 | -46.148998 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfe0868e-607c-3d35-8125-291dd5e801fb | -5.082 | -45.829899 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 314af007-9bfe-3c0f-8bf9-c62fcc1f1383 | -5.0847 | -45.841202 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11e62075-b0e2-3165-97ac-195da649e605 | -5.0874 | -45.8526 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6bf785b-6187-365b-8f8a-02c7ac7ac2e7 | -5.1588 | -46.151299 | 2024-10-13 00:59:14 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01267a80-adf5-3fa3-95e0-dbce1bb1e57e | -4.8709 | -45.035599 | 2024-10-13 00:59:14 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a799a576-e8b8-33ad-a05c-cbbfc78023e3 | -4.858 | -45.025002 | 2024-10-13 00:59:14 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47771612-83f5-330f-beb1-a74951a815c4 | -4.8611 | -45.037899 | 2024-10-13 00:59:14 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a49a5c3-2789-3f74-888f-93e5686236fa | -4.8642 | -45.0508 | 2024-10-13 00:59:14 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d31c2a00-d422-35eb-ab9c-1138de939612 | -4.8483 | -45.027302 | 2024-10-13 00:59:14 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe179d85-d649-3992-afe2-0678450c9d67 | -4.8514 | -45.040199 | 2024-10-13 00:59:14 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be59c75c-b395-3fee-9e0a-02d0f9b3f83f | -3.7187 | -40.690701 | 2024-10-13 00:59:16 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 638dc1ed-b0bc-3699-b383-66347c32b5d2 | -3.7253 | -40.717499 | 2024-10-13 00:59:16 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5e451f16-77e5-353d-99ba-6ccd893597ef | -3.709 | -40.693001 | 2024-10-13 00:59:16 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e7cf33ba-0de7-342b-be67-aaae583cec52 | -3.7157 | -40.719799 | 2024-10-13 00:59:16 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 95a2799c-ace2-3866-a1a6-8621449ba76b | -4.8791 | -45.756599 | 2024-10-13 00:59:17 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9e1c7e-cee4-3f56-a7d4-e8a274da1f78 | -4.8818 | -45.7682 | 2024-10-13 00:59:17 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1aca8c9a-a236-3b99-8f79-3197c4de39f3 | -4.8638 | -45.735699 | 2024-10-13 00:59:17 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 173ef8ff-e847-3b8e-968f-4c566d89362e | -4.854 | -45.737999 | 2024-10-13 00:59:17 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6617fb1d-9840-377b-a4de-2858071b969b | -5.0765 | -46.845001 | 2024-10-13 00:59:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f782485-a6d8-3473-a513-8e7ba2d494b6 | -5.0788 | -46.854801 | 2024-10-13 00:59:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34a3e74f-654e-3660-ba66-f85491e010b5 | -5.0643 | -46.837502 | 2024-10-13 00:59:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 933734f3-39d5-3bf3-a84f-7e030dd5dea7 | -5.0667 | -46.847301 | 2024-10-13 00:59:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 858f2322-1707-3cb7-a850-e1dcb31ab24c | -5.069 | -46.857101 | 2024-10-13 00:59:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75072f5f-6354-3389-a0e1-37808bf062fb | -5.1227 | -47.3452 | 2024-10-13 00:59:19 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7649d0-9f1f-3497-9216-7f9ae1a93235 | -4.982 | -46.794102 | 2024-10-13 00:59:19 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15b1c794-0646-3a1c-93fb-79693753cc01 | -4.9722 | -46.796398 | 2024-10-13 00:59:19 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5adafdae-47c1-3801-b52e-0794bdf86bcf | -4.9745 | -46.806301 | 2024-10-13 00:59:19 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f814fbbd-7a82-38e5-88f1-1561c5501765 | -4.3958 | -44.4725 | 2024-10-13 00:59:20 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd915275-7307-36ea-b394-9615b1a8d989 | -6.0512 | -52.153801 | 2024-10-13 00:59:22 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31924f5a-14c3-3274-9429-d211d6fdc4f0 | -6.0528 | -52.160801 | 2024-10-13 00:59:22 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8987d1d-c1f1-343b-9606-782a224dedb6 | -6.0544 | -52.167702 | 2024-10-13 00:59:22 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df5c87a-14b7-3233-82d2-edcae6854f0c | -4.0948 | -43.906399 | 2024-10-13 00:59:22 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e70d961-9c66-3bff-aea4-7af6d045c3c4 | -4.0987 | -43.922298 | 2024-10-13 00:59:22 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8deb06d1-74b4-3e11-9060-b7eeaae04ebc | -4.0851 | -43.908699 | 2024-10-13 00:59:22 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f55bce67-88e3-3078-93aa-1fa7b0015848 | -4.089 | -43.924599 | 2024-10-13 00:59:22 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23e03e13-002b-30f9-b23b-6dec3453d730 | -4.8229 | -46.862598 | 2024-10-13 00:59:22 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc7b7376-f6bc-3b2b-b59d-7fa6af41e412 | -4.6921 | -46.745499 | 2024-10-13 00:59:24 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
