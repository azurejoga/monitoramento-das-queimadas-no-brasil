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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e99b83b-cb67-347f-8258-ac9e28bc8142 | -8.1014 | -42.36215 | 2025-08-18 04:46:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 251e0e34-9232-3c4a-ad39-cf6a2dc96f41 | -6.55106 | -43.02055 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ad5c34c-c3c4-3f6c-bff3-4342d74bf943 | -7.51725 | -45.46473 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91a8c972-b277-3e6e-b0b9-8b053903cb71 | -9.94404 | -52.16438 | 2025-08-18 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 705f2aa1-667c-33a0-8b0b-83af411b9893 | -6.90226 | -39.55118 | 2025-08-18 04:46:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 70483644-bb96-3b06-a27e-3facd4010b8b | -7.54818 | -45.43179 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd4fb10b-5777-31d2-a35d-e2fbc0866886 | -6.41199 | -42.50181 | 2025-08-18 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28919dbc-0d04-33fd-8e7a-c38a6e772c4d | -8.03635 | -47.68402 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0bdec94-ed6d-396b-b42f-63d6df20e5ad | -11.66854 | -46.87729 | 2025-08-18 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea002728-292b-3085-a5b5-dc0d12645d20 | -6.73174 | -50.95926 | 2025-08-18 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b156f795-6d22-3ae5-82ca-6f00835fb36c | -6.18847 | -53.51868 | 2025-08-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91ddf8fa-84c0-3ed9-99b1-d350b22ded30 | -6.55189 | -43.01479 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc8708b6-1c1e-3efc-80cc-99796aaafdfb | -11.01944 | -51.78854 | 2025-08-18 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 092b900a-bdb6-3ee5-90d3-3ccf341fdba1 | -6.40648 | -42.50349 | 2025-08-18 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1d1a10b-4530-391b-aae4-a7d5d45c636f | -6.5523 | -44.47374 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5d1ee5e1-cb73-32d3-a867-5cc42d9333af | -5.5019 | -49.2183 | 2025-08-18 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eba3db64-b711-353f-9ca6-146b3188af19 | -7.01162 | -44.27905 | 2025-08-18 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f3a5d7d-b263-39e8-a20f-7a5e369cd41f | -8.79475 | -52.07567 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 470f99fa-b9f8-3b8c-bee5-8133992df9dd | -5.97951 | -44.12416 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e6b17cf5-fa25-33e8-b25a-9a0e03e62ff3 | -8.75113 | -46.68219 | 2025-08-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bae68624-fc80-3fc3-b094-3d70c7581e8d | -6.8026 | -44.72813 | 2025-08-18 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83995380-7bc9-32fd-81e2-e5fa1db2f60b | -6.55162 | -44.47839 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6920c3fe-5d08-359d-bf98-3f71c1dba1ca | -6.56137 | -44.47496 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17710960-fc27-3012-a2a8-e7900da3b3ef | -8.97457 | -60.49619 | 2025-08-18 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd1a1556-a599-348c-9177-36c4b31e3b66 | -8.20054 | -47.33464 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9dc3af3-d674-3254-9fb8-0dd4c6938820 | -6.56847 | -44.46817 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f84df8d2-04ce-3765-9a36-d44a364ebbcc | -5.97645 | -53.54935 | 2025-08-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c0ece5-7693-3dd4-bbb6-80a02ed0a989 | -6.56658 | -44.47094 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d60d71a-8b4c-3ac3-8929-51e16191c703 | -9.5202 | -60.53139 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3397feba-437c-3868-bffc-11e3ff805f4c | -9.51113 | -60.52341 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b21ec597-6218-3d07-8925-622f27c0343f | -7.20289 | -43.97462 | 2025-08-18 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9378ffa2-6d60-31db-906e-3069fdaac0f1 | -11.80206 | -44.93949 | 2025-08-18 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccf830fb-4913-385a-8fc8-73e55c025c27 | -9.49204 | -40.37403 | 2025-08-18 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a18ca6ed-2e88-32e6-9d0e-37400fe971fc | -6.43102 | -44.77913 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5efecec-da13-3aaa-86bd-a89a47586899 | -5.75945 | -46.67105 | 2025-08-18 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f83d14a-1982-3e6f-bfe7-64e016a44d17 | -6.56393 | -44.46752 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0ba7c0b-f927-3c1e-bfde-00619d687d82 | -9.5213 | -60.52528 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d26cce52-fda4-3f6e-bfe2-6b0340c95b0b | -7.55678 | -45.4331 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e5cfefb-b2ae-3cc0-9c53-a7ed075dde6e | -6.55728 | -43.01389 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fce9e823-aa54-3909-96de-9f3fb8fc3439 | -6.55683 | -44.47439 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b8889cf-271d-3b9c-a2ed-7fce4cd08196 | -7.13944 | -44.19356 | 2025-08-18 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33919a54-f22e-3dc9-bacd-332256d3c25b | -6.88388 | -44.65622 | 2025-08-18 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abeda73c-32ed-3947-8ef5-59f4b3eef380 | -9.1808 | -49.66571 | 2025-08-18 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d16f4a1-30a2-3569-b111-9234d38c8796 | -6.90514 | -39.55257 | 2025-08-18 04:46:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 010c2e5b-6e76-37bb-a179-0f159753ab1b | -8.79776 | -52.0798 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc643847-0940-3118-b760-ab17f27c3a5c | -10.86064 | -48.46871 | 2025-08-18 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25738112-192b-3888-81a4-75ec778b0812 | -8.22156 | -47.29884 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3045e393-e311-3a5a-be6b-c2d25106e7f8 | -11.90988 | -46.75066 | 2025-08-18 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5922460-2fc1-3c6a-9b72-3874f81c2e2b | -6.14582 | -42.7039 | 2025-08-18 04:46:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebe71a48-9ccc-352d-88a5-93cfaca9e2b4 | -10.86281 | -48.46671 | 2025-08-18 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b4a3aa8-cd81-3b1c-a892-30ce1fe5152c | -6.43221 | -44.77071 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 02977a3d-799d-3b9b-bdac-fb234ef50fde | -6.43041 | -44.78347 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d81da28-5115-3b35-9d15-31aab1ed4d58 | -7.08204 | -44.94271 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e65a8f03-299c-36f6-ac70-1e83dee3f118 | -8.79421 | -52.07915 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d85d464e-283c-37a6-bb7a-7b4085b7f0a2 | -10.85843 | -48.47071 | 2025-08-18 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9ba3b38-80ab-3c7a-a172-959941629087 | -6.5569 | -43.01551 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a16572e-9b48-3304-9094-c81c2375b596 | -7.02091 | -44.28007 | 2025-08-18 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddbc340a-ca62-349b-857d-254a7f45c496 | -8.19599 | -47.33886 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a653456-c958-36ed-9a7a-3dedf098d3e9 | -6.43484 | -44.78413 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d436157e-bcc7-3913-9240-c64a6ddd4bf8 | -8.79585 | -52.06871 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 976fc397-2185-3a8c-b346-4542a205f5e2 | -8.78372 | -49.99788 | 2025-08-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fdb378a-15d0-30ff-8cbb-c327ab21fd17 | -9.8748 | -44.69419 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7c130d3-ffb1-3500-87fd-816ff305dd74 | -8.82199 | -52.05511 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bf2a457-3855-3ccf-b690-d86f9f8ee74b | -8.81484 | -52.05752 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 372dec9b-e62e-374a-b005-1bfe3ba5133f | -5.55528 | -51.3712 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a13b7c6-5f54-3a89-811c-a75fc62c82c5 | -6.55226 | -43.01318 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d9cdd67-2278-3f3a-8a75-7eac97050be0 | -9.71839 | -47.9057 | 2025-08-18 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0967738f-5039-311e-a957-b02c1a465e62 | -6.19194 | -53.51924 | 2025-08-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18650a39-a136-3c3f-9fd1-699d3bf6bcdc | -6.11234 | -46.67097 | 2025-08-18 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a65a881-bf01-39a1-ac22-cf738b03b9df | -7.56908 | -45.43923 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cae5ded6-b877-3811-95b1-bf0a977c55b5 | -6.03213 | -44.34217 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5089826d-0ded-319b-bc9b-b0196782005e | -4.65905 | -49.67922 | 2025-08-18 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b152674b-89d6-3cc8-a8f4-9b19e33cce61 | -11.00271 | -45.65374 | 2025-08-18 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eecca974-7833-3794-96b0-65c1dac37b51 | -6.43603 | -44.77566 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6c1e7dff-87d1-3001-b1aa-11e504191918 | -8.8159 | -52.0292 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eedc9eb0-9695-3862-b4ee-eb316d56dd8b | -4.78466 | -45.324 | 2025-08-18 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e36a1c0b-8c3c-328c-8222-7b9001cc5ce2 | -8.04078 | -47.68005 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52f74b4f-0d5f-351e-84c1-4865e3418637 | -6.15136 | -42.70147 | 2025-08-18 04:46:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b094372-fdd0-3933-bec2-0c2fd9aa7ba7 | -7.07763 | -44.94205 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0caf34a8-6b9d-3fe1-bace-fd084ef1174a | -9.51168 | -60.52037 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c59b424-dad0-3690-b792-1b401599c507 | -6.55109 | -43.02185 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43c773bc-1a43-32ac-8abc-35e146983bf1 | -8.19914 | -47.34409 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9378f4a9-dbea-350a-be77-e272fb77494c | -6.55904 | -41.81784 | 2025-08-18 04:46:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c6633cd-f329-35f6-a409-5c62a71863b2 | -8.79639 | -52.06523 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dc289a6-e674-3f79-a03f-d84afc20c10e | -8.20197 | -47.32496 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 751913b8-3de5-3ae2-923f-c66bb3ad8d71 | -7.57338 | -45.43988 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59068d3f-ff81-327d-9d4f-9813d8998ae3 | -8.50236 | -44.73487 | 2025-08-18 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9265e976-5832-37cb-a15e-8b23908e6acc | -7.2036 | -43.9695 | 2025-08-18 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6a3c2e4-2d5f-3b2d-82b8-559e78230a16 | -7.38514 | -44.28284 | 2025-08-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c137b78-1c8f-3995-b1aa-ea27e8fe3a6b | -9.87289 | -44.69013 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6346eca5-30da-3666-8904-de4e5704b340 | -9.84401 | -50.14937 | 2025-08-18 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1a998c0-82d2-362d-8dbd-1a417860117a | -5.79299 | -43.8826 | 2025-08-18 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 170c45da-c70d-3654-98e9-ddb8e66d1798 | -5.79429 | -43.8854 | 2025-08-18 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6712fb9-3111-3692-b40a-c4c52a51dce1 | -9.18023 | -49.66951 | 2025-08-18 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78b357bb-51ce-395b-8220-be65d8150b86 | -6.55811 | -44.47626 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 468a9da3-e0f3-3ea6-aca5-583e78c88aee | -8.0377 | -47.67494 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92de179d-f11a-333f-be7d-4510182a5276 | -8.03703 | -47.67948 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55606763-1788-3109-a466-261ca930d6b4 | -6.36746 | -43.30755 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 45e1375d-9a38-3dbb-b5fd-232dffb46780 | -5.98439 | -44.12182 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0b4bbfc2-7bfd-3fae-802a-d4aa0d5fdcde | -6.43544 | -44.77989 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |


[Clique aqui para ver as próximas entradas](README19.md)
