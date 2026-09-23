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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06602872-862a-3958-958a-b72cc9939227 | -3.5927 | -50.030102 | 2026-09-23 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 623c4dd8-4bf2-33e8-b8d2-c95fce3ce9bd | -3.1529 | -57.693001 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e24cc76-b56e-333c-b956-59e3e442e94a | -9.9504 | -48.473598 | 2026-09-23 00:58:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24c43c21-2772-3606-ac90-58334e2cc75a | -3.0113 | -54.184399 | 2026-09-23 00:58:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23281d0b-5a46-380c-91d1-9be3e59eba06 | -3.2596 | -53.9636 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffa64e0-1a21-3161-9535-74662ee6b989 | -2.9568 | -54.081902 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff69696-f4c0-3b54-bdb5-c48d4c9a6432 | -2.7421 | -51.550301 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5787b29-8d81-3912-a039-ea9201e41fba | -6.609 | -43.7393 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e84de06e-dba6-372f-94ef-2fe58fea3ca2 | -8.7788 | -45.6087 | 2026-09-23 00:58:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b71a26a9-aa8b-319a-bf1b-138d1212dd28 | -6.9306 | -46.5509 | 2026-09-23 00:58:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1a0f20-c236-33eb-b071-693f4df88edc | -11.13 | -51.0471 | 2026-09-23 00:58:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 241411b4-14bb-37ef-bb86-d97b4b75c9bb | -2.4608 | -57.9076 | 2026-09-23 00:58:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2db5a5c2-689e-3857-95c8-5a09ab6258f4 | -4.0526 | -56.304699 | 2026-09-23 00:58:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 678c1dca-383f-3c2f-8317-8a0cfdb8f2f2 | -12.7628 | -50.874699 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8afca9cd-8f60-30ff-bebb-ecc2176dadaa | -6.6329 | -59.921398 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 612088b1-3f51-3e03-ad21-43077a81b322 | -11.7063 | -50.949402 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7e5fc82-d37d-3741-ad80-af1e3de36511 | -11.1124 | -48.320202 | 2026-09-23 00:58:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e55bf7a-c34c-380b-9e6b-c6fafe4e98b1 | -3.6773 | -60.569401 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80f87136-b483-3c7c-bb5b-d791b3771e3e | -7.4217 | -49.8615 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3fd4b4d-5772-3231-8346-2025da517f2b | -5.0066 | -49.469101 | 2026-09-23 00:58:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb04660-ff85-36f9-9107-21c610dd3043 | -6.065 | -57.800999 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cdf1c49-24e7-3551-b123-393189da1589 | -7.4274 | -49.841801 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d78d896-d0ec-3c31-afbd-11e449ab50d5 | -6.6146 | -43.761501 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf83cc9f-660e-34d8-88db-8ef27ce100d2 | -11.3081 | -51.3694 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dadd0cae-a8a3-3bf3-adf1-a2c02b87d7db | -8.5834 | -54.617298 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95f9fc5c-5ee2-386b-844a-2ff02b9cd611 | -6.8884 | -55.320702 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825f4ce2-fbba-389b-9e1a-83d6c7ed2b96 | -13.8575 | -48.593201 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90a5e9cd-9639-3bc4-969a-22fcd9f0d51f | -5.3471 | -45.136101 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea38eb3b-a275-3ed5-a351-7673caebca3f | -10.2496 | -49.981201 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28f9bd0e-81d5-32da-816e-9aee41c449f3 | -6.6119 | -59.966099 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36a63475-e596-38d7-9c99-960b43eaf9db | -6.2882 | -57.742802 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4986b8f0-9b1c-3563-b0ba-d58c484a48e9 | -4.9816 | -56.953701 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c989ce10-3431-3a91-9106-743754269663 | -14.6314 | -45.647301 | 2026-09-23 00:58:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 625bfa7e-5389-3a62-9125-888e5f85eced | -7.5617 | -55.0187 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc52448-8063-3f70-a821-04aad4412a4e | -3.2466 | -53.952099 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4904ed94-433c-3d8c-8ab2-ee9df5fc6a4e | -8.8099 | -44.266998 | 2026-09-23 00:58:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f72a2b9-b715-341e-808f-be0dbe35e2c5 | -12.8526 | -50.861 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c69dbcc1-4bb0-3847-b4f9-6ecce361ca9a | -10.2629 | -50.212399 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2985fd66-c451-3997-8c16-23ce153b9cbe | -6.4181 | -59.967098 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23fefeb2-7de4-3541-b26a-302d0a801a75 | -10.2575 | -49.970798 | 2026-09-23 00:58:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f1d2b58-bbdb-38d9-9297-64216634e5e3 | -4.3054 | -49.120701 | 2026-09-23 00:58:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba0e95b6-e719-3ff1-99ad-61364b3ac02a | -8.4634 | -48.690498 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e0526ca4-29d7-30e7-b113-faab79207354 | -3.7763 | -60.737499 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca040a7-f5a0-30c3-875e-36482080fb43 | -10.0434 | -53.782799 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2b18212-57a2-3030-adb8-53095c90ee1e | -6.1274 | -57.758499 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39858661-3c35-34f1-b55a-f19881be6f36 | -4.3028 | -55.592201 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbc2c4e-a83c-3ebc-aa8d-529d6682cbbc | -4.3354 | -55.644798 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3768b64f-332e-3ea3-a6da-99d9321f04ae | -10.3786 | -54.406898 | 2026-09-23 00:58:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be536255-eb4c-3f4e-9487-4ecdbc994aca | -11.6914 | -50.929901 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae7da96-f80f-3081-bd8e-3c0cb69e0f9a | -2.7633 | -57.020199 | 2026-09-23 00:58:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd165f4f-3dd7-31f9-b07d-de4dbd78bbef | -12.7563 | -50.891499 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e700fb20-f82e-31c5-8669-f2eecae70fbf | -2.5644 | -57.5037 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20150aba-5aa5-395d-b3c1-052d1b09f742 | -14.6282 | -45.634998 | 2026-09-23 00:58:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a737d350-1519-3960-b587-5de5bc1dd992 | 1.5704 | -55.881802 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b5d221-1e36-3de5-b45d-fc2dffcd9e9f | -5.8133 | -57.730999 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aca19ba6-047a-397e-bde0-28d0a6988762 | -3.7446 | -58.856998 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86794bf9-7b00-34dd-9d40-45bdba86c9c8 | -12.1339 | -47.379002 | 2026-09-23 00:58:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb433d8-e2c8-3eb2-b848-a4375147299a | -12.7922 | -50.867802 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5568d506-950c-3238-91ee-6426560335c1 | -11.313 | -51.345699 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3220ffc9-4325-3798-88fd-65bc2787a92f | -11.5314 | -45.3447 | 2026-09-23 00:58:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2521c450-c477-3211-8cc4-b9736cd938fa | -12.477 | -47.008801 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6b0d08b-3e18-3716-ab0d-b00aad161ad7 | -5.6303 | -45.243 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48bff02e-9d05-3046-806c-ad595e96b996 | -5.7656 | -52.3503 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76d440ce-b49d-3517-a71b-da82a42180ce | -5.9234 | -59.901199 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78408730-6ad1-3c96-b7ae-fb6a83cfd97c | -11.2982 | -51.3265 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5718eacd-0637-30cc-9268-21750acdf877 | -6.739 | -59.421799 | 2026-09-23 00:58:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2ee6efb-873a-3b68-99d1-0a4355ab763f | -2.4195 | -58.2691 | 2026-09-23 00:58:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95adc5a9-d0df-3122-bf85-79532db57aa7 | -12.8411 | -50.856201 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99c75ed5-af91-3de0-91dd-7d24321fb2e0 | -6.8917 | -55.3353 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 967e1a76-a249-3b5e-9f18-cffcd383a7a3 | -9.5555 | -47.954102 | 2026-09-23 00:58:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7ebadcb-9fb8-307e-9836-eaf1834996fa | -3.4709 | -59.557098 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04f39793-1a6b-30db-8d01-176a770d5e07 | -7.0216 | -44.641102 | 2026-09-23 00:58:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b42fb370-a720-38b9-b976-f6af1ac9a1e9 | -6.2996 | -59.938999 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2698ecc-4e0a-3c27-a8a3-fd537cb64bc2 | -12.7874 | -50.8918 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7337d7c-a174-31d1-9f63-260d47493506 | -11.7832 | -50.969398 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78ae5e46-597f-3865-936e-ddd4e84c8ca8 | -6.063 | -57.791801 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e982ae26-9b2c-3026-962d-4a59c2b661ec | 2.7823 | -60.219898 | 2026-09-23 00:58:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4c343ed3-5271-3c37-b5a8-46c9d60259a3 | -10.6996 | -48.707802 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b198374-b6f9-3d78-9a87-bacebac65cdb | -8.8003 | -44.269501 | 2026-09-23 00:58:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 914a33c9-9aab-3383-b3e2-96027ea201e6 | -3.6339 | -58.912399 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a093d40-148b-33cb-b2ad-70d2d5cc939c | -2.9253 | -57.7785 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7123dc17-445f-3395-bc7f-e85b1818a169 | -4.2755 | -55.427101 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9332560-d576-3b49-8a02-31301e774ef0 | -3.1491 | -57.6763 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3ab2dc8-5429-3c42-8038-461765186aaf | -12.7908 | -50.9062 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e79478b4-85c7-30ec-ab7f-a78156a9d266 | -9.5429 | -45.365799 | 2026-09-23 00:58:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb81b1b6-2b4b-323b-a8fc-e88551566163 | -6.6762 | -55.064499 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdd5259f-46f2-30ec-bef2-429bc361f53a | -4.5116 | -54.970699 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa8924a4-8dbb-3842-865a-6dd9bb27a398 | -6.5997 | -51.323299 | 2026-09-23 00:58:00 | METOP-C | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14bd6781-09da-3555-b2f0-056b3011b40f | -8.1286 | -44.421501 | 2026-09-23 00:58:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79e75e7f-a261-3a2d-a04b-e68f7b16ffe8 | -5.8899 | -52.0415 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40f9fe89-609d-3a23-a5bc-059b60950c3d | -5.1939 | -50.0858 | 2026-09-23 00:58:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b4ee92-0570-34b8-a03c-fffe6a2d6b7d | -13.8688 | -48.554001 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a00d18a0-7993-3138-9309-d5d840a68334 | -8.2502 | -55.243301 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae0361e7-09e8-397b-aef2-d3973114ce3f | -3.5751 | -59.062 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99ec5476-d243-31e4-afb5-4befa46cd9e5 | -12.8104 | -50.9016 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f30452e0-ba6c-3490-a2e3-afa034c12d68 | -11.7275 | -50.774899 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4b0e2d-aaa1-3df2-b3ad-7871b92e2a10 | -4.5327 | -54.973202 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 944247e2-d59d-32d7-ae5d-0b9ce479ad1e | -7.6154 | -50.417301 | 2026-09-23 00:58:00 | METOP-C | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88e4a34-bf3d-388d-917a-42ee5d7e870f | -3.8756 | -52.254501 | 2026-09-23 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f78e57-7fc2-3e5c-baf7-ed099df270ee | -5.3467 | -45.1758 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README27.md)
