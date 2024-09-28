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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 067dd7df-3ae6-310a-ae1a-503d41b86d8f | -6.6233 | -42.043499 | 2024-09-28 00:14:22 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01455c20-87d8-37a2-b5a4-6d3440e64d59 | -6.6249 | -42.050499 | 2024-09-28 00:14:22 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02c7699c-6696-3148-8f21-b52d8d895e56 | -6.6426 | -42.0835 | 2024-09-28 00:14:22 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3387253-3178-352f-a870-3d7ca1409a3c | -7.0563 | -43.921101 | 2024-09-28 00:14:22 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4010c2d8-244a-398b-9876-e38ac1442dbe | -7.048 | -43.930302 | 2024-09-28 00:14:22 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 967cd7b7-536b-3187-8ee7-f1d4097ef1e7 | -7.0258 | -43.876701 | 2024-09-28 00:14:22 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37ed5a85-a9b8-32c9-9540-ef8454cee00f | -8.2302 | -49.352798 | 2024-09-28 00:14:22 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cac70da8-fdbe-34db-83c6-372b2fcf7be5 | -8.233 | -49.366001 | 2024-09-28 00:14:22 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 268f5d1d-1632-3a30-a5fd-09181db72d26 | -8.2358 | -49.379299 | 2024-09-28 00:14:22 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e839b8ed-5757-325a-bac0-93293fcc8ca8 | -7.2697 | -44.929699 | 2024-09-28 00:14:22 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81b34e20-c447-35f4-91ce-1a9db1f74807 | -7.2746 | -44.9519 | 2024-09-28 00:14:22 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb646f6c-a517-3434-9c40-f964385ae506 | -7.2762 | -44.959202 | 2024-09-28 00:14:22 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a3afb85-3c24-3592-81bf-ac403c2c6213 | -7.4769 | -45.874699 | 2024-09-28 00:14:22 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32b533ec-ea12-3556-a39c-dfa49fa2aea1 | -8.2233 | -49.368 | 2024-09-28 00:14:22 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fae9bfbc-3cdb-37bb-ae41-1d912581e687 | -7.2664 | -44.961399 | 2024-09-28 00:14:22 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| debff764-e126-38c7-bb33-b45b9ce70490 | -6.8334 | -43.109501 | 2024-09-28 00:14:23 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 938b71bf-304e-3610-a7fd-aca7ccf224c5 | -6.8349 | -43.116402 | 2024-09-28 00:14:23 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa558060-9f98-3ad0-8363-98aff17abb14 | -6.6618 | -42.577 | 2024-09-28 00:14:23 | METOP-B | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0eca9e0e-65ac-3623-b457-6e10c9761d26 | -7.0607 | -44.1255 | 2024-09-28 00:14:23 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd8ce3a-c22c-3b1a-8f2e-5e0d30855d34 | -6.4587 | -41.954498 | 2024-09-28 00:14:24 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cfc1caae-3a0a-3491-9c30-75f720618032 | -7.2124 | -45.089901 | 2024-09-28 00:14:24 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f797a9d2-f599-38fe-a042-113ad1eed794 | -7.2141 | -45.097401 | 2024-09-28 00:14:24 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65d7f776-5e64-3481-8300-e7bf044f3194 | -8.0964 | -49.492001 | 2024-09-28 00:14:25 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30406e0c-9b10-3265-8e92-0298cd8aa620 | -8.0992 | -49.505402 | 2024-09-28 00:14:25 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84674ba3-1fe6-3a8e-b94f-92bd6a703e1b | -8.0894 | -49.5075 | 2024-09-28 00:14:25 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22606740-9a24-302a-80ed-9aabcba328fa | -6.7153 | -43.546799 | 2024-09-28 00:14:26 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cccd305-39d6-3b12-afa4-ce922b0710ba | -6.7168 | -43.553699 | 2024-09-28 00:14:26 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2a0ed49-a591-3612-9baf-8f9cf7488368 | -6.6895 | -43.523701 | 2024-09-28 00:14:26 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a2da050-92aa-3c53-87c6-443602fcb247 | -7.1415 | -45.421799 | 2024-09-28 00:14:26 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14b267a5-e122-3dc6-bcb2-7a4b3b083c4d | -7.1432 | -45.429501 | 2024-09-28 00:14:26 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 385429ae-e10b-3205-85b5-6a5c9ce1f93b | -7.286 | -46.129101 | 2024-09-28 00:14:26 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea7517e6-839e-38ea-a101-0a92b6f610f6 | -7.2878 | -46.137299 | 2024-09-28 00:14:26 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b21b14b0-c42a-39e7-a232-f395b03f428b | -6.4902 | -42.775002 | 2024-09-28 00:14:27 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72a13979-022b-3c98-a2bb-8d2a249b44d4 | -6.4917 | -42.781898 | 2024-09-28 00:14:27 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96d40005-ed6e-3165-a5f1-606f7d6d0c2e | -6.5542 | -43.150299 | 2024-09-28 00:14:27 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f44d55d-8b35-3730-b11a-015743d3738e | -6.6719 | -43.491501 | 2024-09-28 00:14:27 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2f555e-2cc9-3d51-8a49-4c1291c2134e | -6.5526 | -43.143501 | 2024-09-28 00:14:27 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a56e635-f026-3330-b0dc-0de708c2d2ab | -7.0185 | -45.329102 | 2024-09-28 00:14:28 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcd2789a-8558-34ec-9a34-a40ef76ec4a9 | -7.0201 | -45.3367 | 2024-09-28 00:14:28 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6ca8c80-806f-3955-892b-4d15b99f2614 | -7.0218 | -45.344299 | 2024-09-28 00:14:28 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 978f7e65-04f4-3fe7-a601-e9854e3074bb | -7.3103 | -46.665798 | 2024-09-28 00:14:28 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4c5b187-fbbe-3390-8774-76cd4805bff1 | -7.007 | -45.323799 | 2024-09-28 00:14:28 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9235cd4a-5793-30f6-87cb-b8abd1e03422 | -7.0087 | -45.331299 | 2024-09-28 00:14:28 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31d8aee7-dcf4-34c7-a64b-503a24605a22 | -7.4061 | -47.1563 | 2024-09-28 00:14:28 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acabbc63-4a72-34d2-a1eb-a9e159535a36 | -7.4082 | -47.165699 | 2024-09-28 00:14:28 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33a90a12-89bd-3e79-bd47-39eeceb6d51d | -7.4769 | -47.532501 | 2024-09-28 00:14:28 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbf678a-a033-3f92-8c3d-4ec66b175585 | -7.479 | -47.5424 | 2024-09-28 00:14:28 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c53fb1e7-753d-3bb9-85a3-0714fb4dae5f | -7.2659 | -46.602299 | 2024-09-28 00:14:28 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72dacc3f-f534-3e00-82bb-1269276521b0 | -6.3217 | -42.486198 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca689a5c-6765-37cc-afab-572a71cf5807 | -6.3103 | -42.481499 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2c323f5-bcbb-3941-b4ec-4436fba5055d | -6.4071 | -42.909302 | 2024-09-28 00:14:29 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| d3b30afc-1874-3f76-8a59-e39d0f57fbf5 | -6.4087 | -42.916199 | 2024-09-28 00:14:29 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 2dec0925-1819-3ce2-a8b4-61e20b273457 | -6.299 | -42.476799 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b99c01c-d21a-33fa-850e-452e4c2737e7 | -6.3005 | -42.4837 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e9b757f1-fa6d-3b2a-8d3d-be57ab64637e | -6.3021 | -42.490601 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6331ce87-978f-32ec-8743-091069a3a839 | -6.3256 | -42.594501 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9f03685-b6dd-3c99-b7c3-d98ddb9f988b | -6.3272 | -42.601501 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b131db49-6faf-325c-bb36-3070b8e2f239 | -6.3143 | -42.589802 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2a1c9c2b-b0c6-36c5-b21d-b9d5a274d5d1 | -6.3158 | -42.596699 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86c515d7-f663-397d-9730-80ace05c4ae2 | -6.2837 | -42.545799 | 2024-09-28 00:14:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| efcfceba-ad52-3457-bb4d-9c90b7b50be5 | -6.6268 | -43.841702 | 2024-09-28 00:14:29 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87fba76a-3349-3c87-8ce0-b4984b171a4f | -6.6283 | -43.848598 | 2024-09-28 00:14:29 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a755ad64-0b50-3bc4-ba3f-4f66af921be9 | -7.245 | -46.8372 | 2024-09-28 00:14:29 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0834008c-8461-3169-ba4d-d2b7ed02031a | -7.2469 | -46.8461 | 2024-09-28 00:14:29 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34fe5d01-924c-3324-bfaa-a3f96a7b3dd1 | -6.2723 | -42.541 | 2024-09-28 00:14:30 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 616436be-26d5-3ca5-949a-26d2fcb2850c | -6.2739 | -42.548 | 2024-09-28 00:14:30 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dec7c20c-6124-3233-9df3-cfbe7d3b3be3 | -6.2755 | -42.554901 | 2024-09-28 00:14:30 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70c7dc0e-a811-30bc-aa5e-955a5f315b5d | -6.6915 | -44.5481 | 2024-09-28 00:14:30 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26f1db02-8842-38d4-a9b3-48f74be889f5 | -6.5856 | -44.164501 | 2024-09-28 00:14:30 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1999120-5f97-3d32-80b0-391d33b06972 | -6.5872 | -44.171501 | 2024-09-28 00:14:30 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 837bcbda-840a-327c-9a17-0a1fbb6050c3 | -5.0626 | -37.712101 | 2024-09-28 00:14:31 | METOP-B | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| e756725f-7d32-3d41-b5cf-293ebabed7fc | -5.0654 | -37.7239 | 2024-09-28 00:14:31 | METOP-B | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f045f95-5ab2-393a-981c-c4ee586d9156 | -6.5743 | -44.159698 | 2024-09-28 00:14:31 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6da617b-a3b6-33f9-a968-9526e3ba70d3 | -6.5758 | -44.166698 | 2024-09-28 00:14:31 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b98acd59-0ddf-360d-b560-b57f42980a1b | -6.5774 | -44.173698 | 2024-09-28 00:14:31 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e72456e-e22f-3201-ac85-0131f51ec32e | -6.566 | -44.1689 | 2024-09-28 00:14:31 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5babaabe-3532-3244-9cb8-b76c16099f60 | -6.6433 | -44.701302 | 2024-09-28 00:14:31 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8785dbf4-eef6-373c-b574-3995af701383 | -6.6449 | -44.7085 | 2024-09-28 00:14:31 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| febc1aa7-6af2-3ff9-9f37-7522e499c8a0 | -6.3242 | -43.410599 | 2024-09-28 00:14:32 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6467522-3b99-38e6-8764-d0b6abc103f4 | -6.3128 | -43.4058 | 2024-09-28 00:14:32 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3d8fed0-dcd1-37f3-b771-f98f64d6a59d | -6.3144 | -43.412701 | 2024-09-28 00:14:32 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae8a757-e0c2-305e-b7c0-65865930c0c1 | -6.3159 | -43.419601 | 2024-09-28 00:14:32 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe32024-41d3-327c-9f3d-2e5fcde3a19b | -6.199 | -43.265701 | 2024-09-28 00:14:33 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c9b6bc5-bd43-33a6-886e-2ff42fe64b31 | -6.008 | -42.330002 | 2024-09-28 00:14:33 | METOP-B | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e52968f-7f7a-31da-aac4-2e049dc749c1 | -6.1755 | -43.436401 | 2024-09-28 00:14:34 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39be44d4-3d6b-38d0-9f8e-b0b2d5c2b4ad | -6.177 | -43.443298 | 2024-09-28 00:14:34 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea6780b2-e6f1-3846-9762-58d7482e537f | -6.2414 | -43.638 | 2024-09-28 00:14:34 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82b0a5fd-32ac-3e57-bbc5-04ce687bc8a5 | -6.1626 | -43.4249 | 2024-09-28 00:14:35 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8944876c-56d1-35bb-bcd8-db721c95a86c | -6.1642 | -43.431801 | 2024-09-28 00:14:35 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a6b14f4-5c56-3326-a830-542b7db48589 | -6.1657 | -43.438599 | 2024-09-28 00:14:35 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61fc6c1b-70f0-3541-8bab-a037a4dbd350 | -6.1672 | -43.445499 | 2024-09-28 00:14:35 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95a0cd82-0e40-3504-9897-296c38e056f8 | -6.7462 | -46.2892 | 2024-09-28 00:14:35 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65c024cf-a431-3e36-90c7-52d99cbe14de | -6.3914 | -44.771801 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7079e32d-7f02-3104-ac05-387c6d0091c1 | -6.5986 | -45.709801 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c3668e5-7906-333e-9c8b-4636889af4bd | -6.6003 | -45.717602 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7db0dbb0-949d-36b2-8729-c64d025b8dca | -6.602 | -45.7253 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0509908-523f-39c4-a2e6-d03af126be5f | -6.5871 | -45.704201 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc8a23a5-1039-3c66-8684-e4d9ea26f42a | -6.5888 | -45.711899 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd9f0867-8a02-3089-afd8-fc4fd8f3a8f9 | -6.5905 | -45.7197 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76a57bf9-0eca-3bb6-b9c2-dd5854239ac8 | -6.5922 | -45.727402 | 2024-09-28 00:14:36 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
