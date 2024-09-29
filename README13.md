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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68495e69-8f40-3718-9e05-2c4ce0228b2a | -9.57026 | -50.20486 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 89feaa1e-ed4c-3e8b-9a18-6a31db1de35b | -9.56902 | -50.19594 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 431a83c4-8426-3d03-9bba-e031f885be3d | -9.56251 | -46.51997 | 2024-09-29 01:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cae75b7f-58a3-373f-80ce-11e0bdea2b98 | -9.55232 | -46.52158 | 2024-09-29 01:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 02887cc8-10dd-32ef-81f3-788592503efc | -9.54372 | -50.20869 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2032e124-7051-319d-a45c-e2c3877b9020 | -9.52944 | -51.3783 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a30f15e-2d17-3837-9408-3f287c90a7c6 | -9.52873 | -47.79167 | 2024-09-29 01:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 17f42ed0-79e2-33b5-a5b6-659ada7d884a | -9.38908 | -50.0187 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fa68e6b2-a353-362d-a9ab-837c5314e513 | -9.38783 | -50.00978 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cf166a76-eb26-3946-a9c1-d1c1fffad541 | -9.37916 | -50.02644 | 2024-09-29 01:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0633a06-e6dd-31db-949d-b3dc25a512c8 | -9.34341 | -50.75771 | 2024-09-29 01:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68b1f115-f81a-3d7b-accd-86e89fa87a31 | -9.0071 | -52.13768 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 428009f7-655c-3a7b-ae9d-60f58582bb16 | -8.80127 | -46.76697 | 2024-09-29 01:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| fbbd6ae6-3f4b-35af-97c7-0595a1053363 | -8.7995 | -46.75498 | 2024-09-29 01:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8f9ee76b-33fb-3317-9f47-78c6b2215f9f | -8.62193 | -49.48474 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 22b533e5-c848-389c-a880-885088f73c73 | -8.46342 | -49.60317 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b912f08-9f2c-3528-92c5-7c54de20963f | -8.24251 | -46.32324 | 2024-09-29 01:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4143e657-f922-3a52-8a44-7184cf73d3ff | -8.24102 | -49.39835 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cbe02aa6-e509-35cf-aa7b-a0a3889d15dd | -8.23972 | -49.38921 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7e3005cc-2f87-324d-a67c-d62c67c0edcd | -8.23844 | -49.38016 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fd67d05-d7be-305d-8f47-b043f2cda05d | -8.23685 | -49.76468 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49c3ec61-ee6a-3ae6-8bd7-3376f9799733 | -8.23208 | -49.39968 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 09fc38c4-dcbd-33ab-b5e0-dae340b2d4c3 | -8.23078 | -49.39054 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| baebc65a-990a-3aab-935f-496f1db96a48 | -8.22183 | -49.39185 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b260dd22-d5fc-3eb0-b1a8-28a7de842217 | -8.21318 | -50.77288 | 2024-09-29 01:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7659a5d6-2929-3f48-9ca0-fa7190861d1a | -8.18227 | -49.8275 | 2024-09-29 01:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 807f54f8-1b04-3a8e-8dad-a6fa303925ff | -7.88555 | -46.73264 | 2024-09-29 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b6315447-39c4-3ed8-8e13-5d3ecb74aa63 | -7.82077 | -45.5183 | 2024-09-29 01:07:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 268eb1d3-ef7e-3dbd-9db9-770c9d114d57 | -7.81416 | -50.22943 | 2024-09-29 01:07:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 92b5b02b-d754-3140-abff-f105fd4d8778 | -7.7387 | -50.01344 | 2024-09-29 01:07:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 971fe098-2592-31d9-bae1-4d39c943974a | -7.72513 | -46.55858 | 2024-09-29 01:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 368c2c2a-fcc7-390d-a2b9-869218788402 | -7.58472 | -49.19051 | 2024-09-29 01:07:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 569e795a-5683-38d8-87d8-25292e7d96b1 | -7.48799 | -46.133 | 2024-09-29 01:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bf538563-d340-36c2-81d1-bad069604d33 | -7.30064 | -44.9773 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2e27a048-6e75-3e24-aae7-129e5ef3a935 | -7.29797 | -44.95995 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e149b927-a1a0-3808-b958-6861e04d9edf | -7.28866 | -44.97894 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2c2486bf-cba5-3aef-ae52-f97ee27a6dbb | -7.28064 | -44.92719 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ec6dff0c-d881-3a05-a148-eb1cb3d9aae7 | -7.26069 | -45.03419 | 2024-09-29 01:07:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 30a70f0a-f07e-34b7-8403-948a88b432b2 | -7.25803 | -45.01738 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5bc7bdd9-e766-37f1-afc3-9a7089d10aa5 | -7.25243 | -45.02395 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 53c6423e-9cc4-37f2-8e8e-a4839d6d9243 | -7.25173 | -44.93792 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c22985ed-5906-3776-ad11-e14bfde5bad4 | -7.24745 | -44.95045 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0e7973b3-c9d4-318c-95f5-8bc775270394 | -7.24474 | -44.93332 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3716123b-1198-3d0e-96b4-d16905bcce4d | -7.18884 | -51.22854 | 2024-09-29 01:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 05fa04ef-3af0-326d-b848-f2300f4060b9 | -7.18735 | -45.89454 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 69531595-d171-3ffe-a3ca-88b4d8cfe012 | -7.17775 | -51.14813 | 2024-09-29 01:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5c1e4615-6fbc-3a34-a3e7-3e92be4d7553 | -7.14259 | -45.5959 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 8401089b-a190-3bde-86b4-f328eddddecb | -7.05207 | -46.14708 | 2024-09-29 01:07:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8f3e0771-d747-3710-a845-72d9695342b3 | -6.94058 | -45.86132 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fd549e84-ed21-394e-b409-d508b4404ed4 | -6.94006 | -45.85497 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b206acbf-2a06-3870-9660-81afa92d47ef | -6.78672 | -51.3895 | 2024-09-29 01:07:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 838cbe9d-15b7-3952-9d5e-1fb0e4bd38d4 | -6.60987 | -51.03853 | 2024-09-29 01:07:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1672b8e1-cbe1-3b33-a470-8f3d585733a8 | -6.3949 | -44.79852 | 2024-09-29 01:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ef9c5bd7-b263-3b79-9d80-5b8e96158f30 | -6.3923 | -45.96182 | 2024-09-29 01:07:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6b4a8a3b-a444-341a-9e63-d8b4b8198106 | -6.392 | -44.78016 | 2024-09-29 01:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 555d9d4f-f5bf-399c-af17-1b934066508a | -6.39076 | -45.95355 | 2024-09-29 01:07:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8902d693-8727-34ec-93ff-cf891a75503f | -6.39003 | -45.9471 | 2024-09-29 01:07:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 54888ac7-d465-388a-b1b9-a7617bbb10e7 | -6.38948 | -44.7873 | 2024-09-29 01:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 2823fa17-eba2-3a73-9173-00230f71d423 | -6.16617 | -47.71736 | 2024-09-29 01:07:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3479dd55-5385-30d0-91fd-cac94529bb02 | -6.16453 | -47.70599 | 2024-09-29 01:07:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 91cdf43f-42af-393f-8445-3300642bef7c | -6.15627 | -47.71874 | 2024-09-29 01:07:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 88c9a93b-d09f-319b-9d4f-a1bb4a00914c | -6.15462 | -47.70739 | 2024-09-29 01:07:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 925f9612-dee5-381d-b6d3-963a8a9f1774 | -6.1224 | -47.27224 | 2024-09-29 01:07:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d16997d0-44e2-3c33-99a3-39887187b025 | -6.07832 | -44.71965 | 2024-09-29 01:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9c222a5f-72e9-3182-97a8-5ba707707667 | -6.07551 | -44.70119 | 2024-09-29 01:07:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| dfbf065a-973d-3ad5-99d1-4e7022887688 | -6.03774 | -48.8139 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9d72c8d3-6c2e-3406-bc73-54d27e76de41 | -6.01188 | -49.34309 | 2024-09-29 01:07:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 190e2fde-c11d-3cd1-98c4-567a1a808348 | -5.95236 | -49.1878 | 2024-09-29 01:07:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3e1a6fe0-1fc0-35b8-8135-ac1113e373b0 | -5.93879 | -49.21547 | 2024-09-29 01:07:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| eb5952cd-4867-39ff-92bd-36c80477899e | -5.93745 | -49.20597 | 2024-09-29 01:07:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a125b16-b6b9-31a2-be6c-66fb66277f9a | -5.93611 | -49.19646 | 2024-09-29 01:07:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4fe6190f-8c9a-3671-9c63-688de62b021e | -5.92696 | -49.19781 | 2024-09-29 01:07:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39484413-520b-3f02-92f9-4b52c9280cd5 | -5.84939 | -53.56321 | 2024-09-29 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3b3d14e9-36f3-3b28-8cd3-df94d3d0e3c1 | -5.78963 | -51.03872 | 2024-09-29 01:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90ffc4db-9329-3145-a0b0-f43e431f1500 | -5.72027 | -51.07252 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0db495ad-0563-3d0a-9815-7a8c6d42b59e | -5.71904 | -51.06369 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60e0d96f-5881-3e18-b681-cd77641aacf5 | -5.57836 | -49.02138 | 2024-09-29 01:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| cf62f9a2-6f92-326f-929c-6cec6f5c2bd9 | -5.5691 | -49.02271 | 2024-09-29 01:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7cff38a0-7ddf-35f5-a278-5fbff57d48f4 | -5.5677 | -49.01297 | 2024-09-29 01:07:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4288078c-7e7a-31d7-b9c0-372aba365d86 | -5.40552 | -46.59258 | 2024-09-29 01:07:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f72cf5f8-ca06-35e2-b9be-0003e80ccace | -5.40345 | -46.57884 | 2024-09-29 01:07:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 37dbaea7-0aab-3309-9dfd-19d2b5a11aa6 | -5.32955 | -44.98597 | 2024-09-29 01:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 551d4082-c2d4-331d-bd31-14f32d292019 | -5.32428 | -47.69947 | 2024-09-29 01:07:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8a4ffaf7-9e4a-377d-81fd-3e73a26cdf98 | -5.27381 | -48.89385 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97e41300-3b67-3c01-8efc-a3d91b620efb | -5.27237 | -48.88393 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d81a1167-a9be-3960-a7c2-b9b0d1210299 | -5.26447 | -48.89521 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3d46aff-daf4-3a09-9989-99afde2c97f0 | -5.26303 | -48.8853 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d1e9aeb6-da27-37df-a18f-39985c210281 | -5.25839 | -49.23035 | 2024-09-29 01:07:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be633a98-4356-3def-9434-e7c3d784098a | -5.24906 | -47.39804 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e02d6714-a41d-3de6-91ff-6691a7926be1 | -5.24725 | -47.38578 | 2024-09-29 01:07:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 545a92ed-ffde-3163-93ee-7c07f827cb25 | -5.22235 | -48.53968 | 2024-09-29 01:07:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 454e69f5-d6d0-33d7-b058-5ac9adc52bc6 | -5.22154 | -48.1945 | 2024-09-29 01:07:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dc10858c-50d8-3fec-9e9c-4544cdc98b1e | -5.21891 | -48.88752 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81f5a592-ffb7-3f8a-a971-85e433df2193 | -5.213 | -48.97921 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| db319d4a-946f-35e2-a688-bfc3cc84cf4e | -5.09718 | -48.8814 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9948cddc-8754-3d84-a9ff-184f36869c81 | -5.08973 | -46.17669 | 2024-09-29 01:07:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 366c4954-4710-3dd6-bc09-6de654363128 | -4.92343 | -48.61888 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4faa8496-fcdf-37df-80b1-158e07b5e9b8 | -4.91393 | -48.62032 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ce4c3ae3-5aa1-31f8-a14c-8d83dd91da59 | -4.91246 | -48.61003 | 2024-09-29 01:07:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| da668a6a-85f6-3eb3-815a-8b2ff9f9fc81 | -4.84496 | -50.93724 | 2024-09-29 01:07:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README14.md)
