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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d948b5b9-ae0f-3d4e-9ed4-0892613c129f | -8.49446 | -48.64345 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 366e8243-43ac-32d2-80c1-42619ffc6e53 | -8.4939 | -48.64704 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c3483162-ae04-3bb4-b0a7-6fdd7b865f17 | -8.49334 | -48.65062 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fd8f44fd-929f-3462-b5d7-776de77d7fd8 | -8.49221 | -48.63575 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4229bb3b-8170-3943-8832-73501b46ba51 | -8.49166 | -48.63934 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 97b2bbdd-80d4-3435-83c4-6baee3d6e2a8 | -8.4911 | -48.64293 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 86a682c9-8a5f-3571-9650-01844ff89b84 | -8.49054 | -48.64651 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0006656a-0b0d-3491-b54c-ec3af3e07d4e | -8.48715 | -55.16917 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f65aae27-e6a2-3de6-b518-ac33546ffa52 | -8.48428 | -55.16106 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea950d51-4172-3616-bc7d-a8247b61512b | -8.48365 | -55.16476 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93aa523d-073d-3507-bc56-b8bcb1621e78 | -8.48302 | -55.16844 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 534fb455-1129-3310-a3df-5b442ac3510e | -8.44465 | -55.24314 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 303c95bb-f2d9-3d91-b8b6-b4749dc4f249 | -8.43375 | -50.04276 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36c4b97-fff9-3654-a31d-9eb35b037066 | -8.38455 | -49.66686 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fc17c52-c584-30a8-a589-68fd7dbd8586 | -8.37783 | -49.62292 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15c058ca-2d2d-3db4-96cf-2c10daf44acb | -8.33896 | -49.65983 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 617ff510-9b3e-3208-b4ad-ddf3edd5c913 | -8.32687 | -48.01258 | 2024-10-09 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547c0d65-52d3-3d70-8283-04ba2911f293 | -8.32373 | -55.11832 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1766a100-72c5-3457-b88b-f2961dbe1b8f | -8.30366 | -49.23215 | 2024-10-09 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 908ad960-2fdb-3370-90af-85b430079168 | -8.30312 | -49.23565 | 2024-10-09 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec725a3a-2987-3b55-a283-97fb3415fb01 | -8.30259 | -55.10791 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 07492b20-273a-3692-b652-8152cd6a2fff | -8.30196 | -55.11164 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ea8246e7-53d4-3eb2-91d1-b3e94abb7a28 | -8.30105 | -49.23187 | 2024-10-09 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1f1c24d-52d5-3857-b9f3-da9489b2a587 | -8.29783 | -55.11089 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 09026d3e-d47d-33a5-ba0c-210ded6a8d29 | -8.2443 | -46.28406 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5cac70f8-ef15-3802-91d5-7320adb28959 | -8.24366 | -46.28839 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bb7eee1-1df6-3870-91a1-26e7ef5d2bae | -8.24303 | -46.2927 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9280a99b-1073-3cdd-a223-b8b935278e10 | -8.24063 | -46.28347 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| affef5fb-0ff1-319a-842a-bacc7dcfa41b | -8.23999 | -46.2878 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf1c89fd-3dda-3386-beda-6848b3d62e58 | -8.2219 | -54.89357 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b472fddf-3e77-3372-85f9-06c5b06e49c8 | -8.2213 | -54.89718 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebe6146-4e34-3774-b477-3d9b926fc6b1 | -8.17887 | -55.04863 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3dbc409-d718-3229-8469-9357cfb7e254 | -8.17823 | -55.05239 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b00735-d4d3-3475-94e1-7b83d31b63f6 | -8.13929 | -49.37857 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92b1b9d0-ec00-3cea-aa08-7b54cf3737f7 | -8.13586 | -55.17599 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d29a1c43-7b99-3c84-aede-167d1ef91bd4 | -8.13387 | -55.31356 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1ad3fdf-9284-3562-b5e0-de4d0048d293 | -8.12862 | -49.09742 | 2024-10-09 04:38:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e83384e-9a39-30df-9ac4-73426b5c8e1b | -8.11011 | -54.86686 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e57e2bc2-54bf-3179-8322-b76a2e6f37ba | -8.10604 | -54.86612 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 095fac64-b800-3faa-b507-d45e99728942 | -8.07339 | -49.66807 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ea3b67f-71e5-3c31-a47a-4b713913a972 | -8.07076 | -54.77845 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 596cd10a-5f61-3d10-b67c-60b0fc9ec09e | -8.07061 | -49.66406 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cdebc6c-6b14-3374-9bd2-c542a72b5def | -8.07006 | -49.66755 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b98ae7f0-f8af-3f8e-9937-4c803f2c3753 | -8.06729 | -49.66354 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83694ddf-2267-3b73-8162-1df58857df52 | -8.06674 | -49.66702 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5924de13-3320-3e21-af79-04c23cd1db41 | -8.06547 | -54.78492 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f2085d-7195-3354-a4d1-7f1194b6e6b3 | -8.05437 | -54.8982 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eca0e90-d64e-39f1-acd2-f3972372b49f | -8.0369 | -49.70512 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59a51625-e4b9-3fb1-9a8e-26ff437fcbc2 | -7.97871 | -54.8295 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64d0de91-6259-3837-9ee3-a8eb4ba51dd4 | -7.97463 | -54.8288 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f06ee3a0-b34a-32c7-9c6e-55fcd5607ae4 | -7.97401 | -54.83245 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2872129c-27d6-3b48-af6f-1b213e7a417a | -7.96931 | -54.83541 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c545efb-f80a-32a2-b2f8-5bc1f7592b5b | -7.96586 | -54.83109 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46ff8dd8-2b94-3260-9925-b14d8fde02c5 | -7.95665 | -54.76278 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5ccd1e-825a-3f05-a897-a2b91656174e | -7.95604 | -54.76635 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26e44c4-c8c2-3809-b2bc-962b0a6f2356 | -7.95542 | -54.76991 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08e6380a-fdfd-396f-a628-89b7558f5d39 | -7.95383 | -54.75495 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d36217d-0569-31a6-b03c-a29435af06c8 | -7.9526 | -54.76207 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51f0b52b-ab22-34fc-b8cb-dc55ae7dbeac | -7.95198 | -54.76564 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 644c8dc1-de22-3b8d-b2dc-61172fbf044d | -7.95031 | -45.90342 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72ca9775-d12e-326b-9ac2-b0eccc5edac9 | -7.94967 | -45.90102 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0fa5c3d-dca9-33eb-95e8-9b64694b393b | -7.93351 | -49.86671 | 2024-10-09 04:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1499c133-47cf-31ea-819a-452d673f3393 | -7.9074 | -49.25958 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0280bb9-5837-308a-a2f3-9e499e856984 | -7.86226 | -54.90429 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55948d10-3e80-32d9-88d3-08323b8be939 | -7.85615 | -49.65126 | 2024-10-09 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9fa311f-9004-3315-a84e-f3c4c4c92633 | -7.84995 | -54.90217 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fbd9aee-5110-36e0-9c7c-e26757a93457 | -7.76393 | -47.04657 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0da5b4ba-6473-3026-887c-ff40ab0cf079 | -7.76102 | -47.04207 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de555a1-5491-33a8-97b9-9298c350567c | -7.73929 | -46.58108 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 548cf3ac-8007-3fba-964f-9bb1b140d2a3 | -7.73819 | -46.58257 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a32354f-dd6b-3f7c-923a-33edec46a442 | -7.72405 | -46.73361 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e04978de-0589-36ea-82f3-4982f08cfb7f | -7.68035 | -47.3124 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50f4892a-cf12-3b19-8482-d15a49e64ac2 | -7.67687 | -47.31186 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94fbdaff-72fe-33ed-9109-92263b3f9b19 | -7.67629 | -47.3157 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3a51b37-9347-3d70-80e9-effcee1b58ce | -7.67339 | -47.31132 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04148543-cbea-32f8-9d2b-c780240d5043 | -7.67281 | -47.31516 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e9c463b-3e26-33f6-9764-94c62406ad59 | -7.58438 | -46.64043 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 611da4f4-2d37-30b9-b2e5-c3d1d564332d | -7.56482 | -49.84435 | 2024-10-09 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19da6503-bfb8-3c5a-9943-a19b3ea4b377 | -7.50869 | -46.8765 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1b4e989-dd6b-3573-9393-b6b875add294 | -7.5047 | -46.60007 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75d5c9a5-c4b9-3f24-b9d8-230ab3e8ab58 | -7.50408 | -46.60411 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddf97cb2-b2ec-3336-8c25-eab6bad53cdb | -7.48637 | -46.6722 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3474dc1b-aead-3fe6-b825-fde371f2be7e | -7.48504 | -47.58627 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 873cefe9-7b34-3bac-8613-33bda9ca18b2 | -7.48447 | -47.59 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d112060c-41b6-3fa7-a118-58b4aed7772d | -7.48342 | -46.66761 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15e593b1-8083-32ad-9f65-638dcbbce1d8 | -7.4828 | -46.67165 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c883d2-2c43-3024-b29b-76df44ce1aaa | -7.48218 | -46.6757 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6976e6c-23a8-3ec1-89e4-3445d2087f4e | -7.4816 | -47.58574 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c34422b-041d-30fd-a30c-0a244d947e05 | -7.46058 | -47.54472 | 2024-10-09 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c61efc01-cec9-38ee-afdf-732de5704cae | -7.4522 | -49.46609 | 2024-10-09 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd33d1ff-d533-3b09-a349-aa11b2ac18fc | -7.4382 | -49.68478 | 2024-10-09 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4563c5d4-8f0d-34fe-adbe-2f44fa810386 | -7.43487 | -49.68425 | 2024-10-09 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beac42eb-7c3d-3341-a2aa-0f8bcf8f1d80 | -7.43254 | -48.35973 | 2024-10-09 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 741d7b62-c7f1-301e-ae28-23f1c3be069e | -7.42968 | -46.6847 | 2024-10-09 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f1f3aa3-4aaa-3b6a-9217-6edad4193849 | -7.41416 | -47.86814 | 2024-10-09 04:38:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee30a823-b6bf-3217-9bd1-8abc383ff8eb | -7.36805 | -46.07968 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d189b2b2-9a18-3557-b26d-fbc9cb85f373 | -7.35132 | -47.11043 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b013e018-2fa7-334d-9909-f9f1ea785be5 | -7.31426 | -47.37955 | 2024-10-09 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2afb7ce-9356-3822-b413-4d1aede35258 | -7.30689 | -44.97652 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b44f21dc-15ed-3f99-9616-0881b42084dd | -7.30614 | -44.98151 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README118.md)
