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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8480e8a2-4e44-328d-b1fa-73c4a779d006 | -8.48289 | -47.29564 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4feccf5e-5317-394f-b6e6-f4c294b7b4c3 | -9.06131 | -49.82695 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50072af6-6386-36b7-b555-468d47a4ca99 | -8.74604 | -47.09944 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ebd43074-00fb-3b51-b2b0-a3b31e5a278a | -8.74247 | -47.09888 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9eac742b-b87f-3e21-80fe-5f98aed1cf90 | -7.18753 | -44.94327 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 324d76c4-6fa8-379a-b703-8671d97d2d54 | -6.85736 | -47.92828 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ded6789-5774-315e-804a-fb9a142e8382 | -8.84938 | -47.27457 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59a88289-c579-34d3-b1cc-ff9846ed4859 | -8.44879 | -47.28286 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a39c689f-4627-39b4-9bb2-9bdf8e1b2d5d | -11.45678 | -43.62763 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb587300-ad61-376a-86a6-912a8762556d | -8.06647 | -48.66338 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3213db39-5e4f-365e-addc-42bf1328013e | -9.07268 | -46.97811 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f2fdf2e-7211-36c8-8b79-7295eb990ddf | -7.55285 | -44.65676 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4594ffaa-2107-3395-9cc6-560c836c2242 | -11.8377 | -46.74772 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 583ba19f-f7cc-363c-9cab-8751eb43a399 | -6.44286 | -44.04907 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87e7e4f3-f512-3afc-9b09-669bea71622e | -10.01016 | -51.70651 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3d6e818-2dd4-3ca9-9dcc-1f2116d2256a | -11.75244 | -50.62562 | 2025-09-10 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b52bcbdc-c8f8-39d4-bfe2-a1f10ddb35a4 | -9.13267 | -45.56949 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36faa1f3-4bd9-3b73-8b2e-7445042d8abc | -8.46482 | -48.95108 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2868cc0-cf66-3787-938c-5e4450d0e8c9 | -7.562 | -44.65087 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56951d5e-3af5-3490-ac8d-7654a695f06e | -6.88 | -45.52931 | 2025-09-10 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe5e1ee-b5ba-3135-83dc-ac37227afa93 | -9.06686 | -49.83501 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9ad7464-5bf0-3fdc-8f75-4c3b87c04e25 | -8.30695 | -44.8206 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce038674-0f4d-3e25-beae-cfe190ef1674 | -10.27464 | -48.81445 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e98de0b-6235-3e66-b886-6ac17ed9ea40 | -5.86322 | -48.15579 | 2025-09-10 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cc2f741-eed5-36f4-8bb7-991830428099 | -7.19218 | -44.93914 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25a0b986-2c12-3cbc-90a2-0b46d668304c | -9.69225 | -46.81311 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 31c97391-a45e-3538-b481-4e564488be77 | -8.47167 | -47.29855 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4d1487a-e33e-38e1-aeda-f5a4d39784c3 | -9.35304 | -46.4984 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9249d148-efab-35f6-ba53-8bf16c9ed2f7 | -5.80058 | -51.73327 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c57710d0-9db8-3073-9f6c-c8c4f79b0bf2 | -9.79814 | -47.78672 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccc8faa8-749e-3dff-b492-49e98572e5dd | -7.3862 | -44.83609 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9995978-1738-39e9-9cdd-73c35d51297b | -9.82536 | -46.04201 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6b8b36f-0a89-3d91-a533-914b4360bba0 | -9.06354 | -45.772 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cd7158b-7edd-30bf-9461-a0c2b027368b | -8.34651 | -45.05812 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 43ba598f-b465-339e-a433-79b2ab5947f8 | -8.30289 | -44.82014 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f05407c0-fb91-379b-8e6b-862ea0c65606 | -11.45151 | -49.28176 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe79dfd4-9e9a-3cd0-9497-f5b76f1eb70f | -11.44363 | -43.62113 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f9e5dda4-9ae0-3810-8189-77d11636fdcb | -10.39035 | -48.83166 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9aedd23-5f23-3328-a36b-082a80f9b1af | -10.27068 | -48.81757 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d0a8b3f-4bd0-38fa-a2c2-f84d8b7caa86 | -11.83011 | -46.74697 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f65612f0-c7bb-329c-bff9-410966a26e41 | -8.07504 | -50.18498 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7796b55e-a19f-3e58-80fe-9f873ee840bf | -9.05751 | -49.81525 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 706dc50b-858a-3b47-9894-45f8f84241bb | -8.32965 | -44.864 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76945a1a-394a-3f2f-98c7-2e42da5eb8dc | -8.95107 | -44.94274 | 2025-09-10 04:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df2b4045-61bd-33ad-a523-ba627d4770da | -11.53534 | -47.32264 | 2025-09-10 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c823c21-f21f-3b11-b01c-8b11159b55fd | -9.51256 | -46.54507 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aae0088-d04f-3726-92c5-e05d69261dc6 | -9.05919 | -49.82627 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bec30c32-f61e-3760-b4a9-978542759333 | -10.95334 | -48.14874 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae8c65e9-11ea-385d-bd6d-6c0c2cea5737 | -10.00117 | -51.69756 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 314f2979-93a6-3fab-85e2-20dbc07de828 | -7.78362 | -46.09807 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f7679f6-4661-3f92-8cf8-17f486943634 | -9.97787 | -50.30011 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 98c0a10e-6c3f-3ce7-b8b1-be784103fc52 | -9.09865 | -46.97687 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 97a9838b-4b82-3bcf-8b24-790c14b5f09a | -9.89576 | -46.4743 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb9553b3-6f61-31da-a5b3-cb4307854918 | -11.10876 | -48.45877 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b184364-c975-35b6-b1d6-feabe2728235 | -9.04986 | -50.48146 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d076a46d-5652-31f8-850b-8112a787f3c0 | -8.85958 | -47.23086 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6073080d-d811-35c9-8101-30458025b683 | -9.00591 | -49.79628 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b77bde-f235-38e5-a469-790c9805899b | -7.86687 | -46.03573 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62123839-3cc1-3ca9-9b78-3e8e6606734f | -6.44363 | -44.07239 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f702e11-5727-35b9-b4b8-0bfbfff8768f | -10.15699 | -48.87497 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6538e9d5-0b55-373a-a151-3c164f4bfd72 | -9.98065 | -50.30415 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9870588-a30c-37c4-924f-ad6d6e929312 | -9.05152 | -50.49253 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcd09489-4e27-3673-b788-87f5fb6fbe30 | -9.68387 | -46.89462 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90bace33-f39a-3984-b0f8-9956340f841e | -11.54326 | -47.31936 | 2025-09-10 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca24500f-8ba7-3962-851c-2827d56d0a26 | -9.04653 | -50.48095 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc99402d-bbbe-3f03-8835-34bdc090d6ea | -8.52193 | -51.38382 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df8f452b-970f-3ebf-bb7c-3fcff0517225 | -10.63975 | -48.61595 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 743a6725-420d-3f85-8c23-7677ed511c78 | -10.00397 | -51.70177 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bd19526-3536-36b8-b638-e68bfa64a31b | -8.06838 | -50.18391 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ed1b8df2-2dcb-3615-a8f0-3b4e2132237b | -8.0392 | -47.2771 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10f301a9-c552-3418-82f4-e42588795006 | -11.18879 | -48.39712 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5a1a46f-873d-352e-8851-216d719153cb | -11.11335 | -48.45173 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c52b10a1-9833-34c2-925c-28ecda0f19ae | -8.47104 | -47.30267 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4885e1ca-f781-3312-8679-11f9bbd824fb | -9.75788 | -51.06314 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8fc3546-6248-385f-b6d6-2470136bc5b6 | -11.24332 | -49.40915 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93b199bc-7831-3d0c-b249-b1cd647909e9 | -7.54399 | -48.24852 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 009b0e27-b7c8-3a14-b627-4a8d98cf258e | -7.74971 | -50.31593 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f465cf24-4dc0-31ed-995f-9a71f7b6ed37 | -11.11475 | -48.38208 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db0ab1a-26f2-3649-8d04-e080912bac39 | -11.56604 | -44.65714 | 2025-09-10 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47c4d443-c2ed-3cca-9774-6b081b15e501 | -6.93561 | -43.9165 | 2025-09-10 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 604d2385-297b-3b33-8ead-d1fba21b97e8 | -11.66836 | -46.90418 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d09edd6-8d68-39af-a872-e32234f3e333 | -11.19512 | -48.40211 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3841722b-132b-3c2c-b1af-cac6a176a28c | -11.1218 | -45.11124 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dccb46ee-d27a-3929-8880-00b01d60f6f6 | -7.66208 | -50.2948 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d0fe3df-5399-3f31-9102-2893ca6d5bab | -8.10804 | -44.85264 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e611c866-7628-34cb-a027-bcc01a6fbcc6 | -8.04461 | -48.66071 | 2025-09-10 04:42:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b46b2716-247a-3848-8af7-22ab09f37334 | -11.44161 | -43.60148 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de165bdc-887a-335e-8f39-8af236e953f4 | -8.37355 | -45.04058 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 137228c2-6359-3b02-8a66-66253c683f67 | -6.6229 | -43.99796 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcb244a5-8da6-3a4e-a1be-78b98d742886 | -9.20934 | -50.53936 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c3e8f80-c6ef-378f-9fa7-4565a0858bf7 | -7.75027 | -50.31242 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35347799-5b4f-3beb-b7a4-96c87f4d255f | -9.07751 | -46.97031 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d55ba48-aafb-3bdc-a1a7-3ef46f6265c3 | -8.06861 | -48.62718 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75d97b92-0459-3cdf-b671-73398a25be34 | -6.55615 | -47.4863 | 2025-09-10 04:42:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2eb88ad-c5b8-3807-9790-b2f7fa507c9c | -10.38335 | -50.53812 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85531cec-7dc4-3428-9203-536ccc9caa72 | -7.78529 | -46.06194 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e60b063-a617-3f6e-81fd-8816fc419b5d | -11.11124 | -48.45146 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33ac01e9-d386-3212-bb23-897e177d7e56 | -11.67259 | -46.90675 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e5034c6-785a-3547-a23a-29d91511b2be | -10.57299 | -52.02534 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a6fb91-1107-3dbe-8127-abaf5040faad | -11.48216 | -50.41204 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README65.md)
