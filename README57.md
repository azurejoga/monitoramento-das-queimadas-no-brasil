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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08705f42-b694-35ab-b915-1ed609355fa7 | -3.31475 | -53.85189 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c07f346-dead-300d-87bf-a7f7ff2edd32 | -2.87846 | -54.15489 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4591441-eeb5-366c-8d78-76b8d26368ab | -2.9541 | -54.14251 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdf86457-d7e9-36f1-9bc0-5f38ade03d19 | -3.47904 | -55.42728 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1104e0b9-7cd2-38c4-87c0-8d35bbec8571 | -2.87769 | -54.13095 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95b03d95-25dd-37cd-9923-d1d0a44ac04c | -2.89703 | -54.11775 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9123eeea-327b-38da-b1e4-44c6ddb99297 | -2.78101 | -54.11236 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 324e8a49-239a-3165-9fb4-a56fdbebef63 | -1.51232 | -54.8108 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80acdfe6-1006-327e-880c-b00dd6c5d00e | -3.38407 | -59.42989 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb034db-86d8-3309-87ef-bcbaadf1142a | -2.99705 | -54.11491 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d24640ac-61b4-38fb-b064-41246daf4f28 | -3.77157 | -55.56451 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62f5331e-c40e-32e9-90ee-78a310377a58 | -3.07321 | -54.24244 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8536bce7-e016-3ac1-9855-af76d9fd6f6b | -2.78152 | -57.67001 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08b96c76-bb2c-3daf-aa86-0da4e2e02708 | -8.3488 | -62.83461 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa874295-18f3-3927-8a65-0a1bdaa8f8c6 | 1.00207 | -50.95087 | 2026-10-06 05:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1f2807f-5d18-3ac7-91a5-848f66fcc067 | -2.99952 | -54.12751 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f169e347-973f-325f-a7f6-4dd89f8b2dfc | -3.1112 | -53.76776 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1021a245-18b8-3fa5-b4cc-331f51f5fa33 | -3.10811 | -53.75868 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1ced0604-a0b2-30d9-aebe-a4a662ec739e | -2.95959 | -54.10688 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a9fbc4-e152-396a-99eb-795cb4ac9c6f | -3.05015 | -54.22288 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fc7bac6-7d41-31d9-99ec-70626fce3e32 | -2.9487 | -54.14799 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b79aa90-a4ac-371e-bb35-4c3fb49d1b80 | 3.06138 | -60.60127 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 353eb0de-52cb-31fa-bf04-fa65d72b2476 | -1.75993 | -54.94879 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fdd66d5-a30f-3439-92d2-e8a83131aa22 | -3.69218 | -55.96188 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7eb8b7a-23f8-3568-9641-5a14b77b649c | -2.94696 | -54.15992 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 956c5857-b58d-3d02-8954-878c9b7de097 | -2.89874 | -54.07722 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29dae39d-f0c0-3364-a232-61a5c2a915f5 | -2.94863 | -54.14985 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 669e0519-7ec0-3b1a-97b9-8010578e8bab | -2.78426 | -51.66668 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3323b1df-b564-3a01-88ac-f8ebb718eac0 | -3.11793 | -53.7581 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08016c35-0403-3305-9150-ad68efc57734 | -3.16814 | -50.44308 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d28a246-8d44-33c4-b28b-4150772cf3d1 | -3.50011 | -49.90049 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ea8aafb-6c99-39ea-8708-a568c7bea349 | -2.98253 | -54.12472 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| afa56d08-009d-3ebf-a1f2-9c63f7780d4a | -1.05466 | -53.59116 | 2026-10-06 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a66b744-2ffa-308a-a853-600e5d54a299 | -3.07524 | -54.17006 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e1ce1de-0b54-3cb7-b399-49a9e23d14ca | -3.05353 | -54.22884 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13aa14a0-1882-3a84-a97f-61c218bb4150 | 1.98629 | -60.61744 | 2026-10-06 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76ceed5e-b3ca-370e-a24c-e132310394cc | -3.3293 | -59.47438 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b7425cc-0ec1-3a29-af43-cf7c15b5113e | -3.05188 | -54.21105 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba4bbad8-0d41-3bc1-b411-dad5ad7237e7 | -3.28223 | -54.17421 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3c06465-c04a-34c2-8af8-c5f372e3e17e | -8.76816 | -61.38489 | 2026-10-06 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 586be76e-bb0f-3ce5-8434-e8c01f11250c | -2.99068 | -54.04013 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4695c1df-7d1d-321c-8a4d-6daa9634379f | -3.68283 | -55.94616 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83b4e3d3-fbdc-315c-86be-10af6d55d139 | -3.47436 | -55.43165 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b43ccad-31ba-36b9-ba1a-8f6f0ca6526d | -3.07948 | -54.1707 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a224c111-b19a-3601-a884-a646cc09b862 | -2.06315 | -56.87142 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 572f3c21-709f-34ca-b025-401897f76ad9 | 1.71942 | -55.64177 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bcd1fe7-f92a-325b-9ee4-c099583afc41 | 2.00978 | -61.08775 | 2026-10-06 05:23:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23b5f699-f95c-32b3-987a-ec7040fdd1e8 | -1.61674 | -55.12241 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d90d9d1-f20d-342f-a327-fee4c8ad2ca4 | -3.84066 | -50.31318 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84abc3c5-2502-3c73-b365-f21db9409c63 | -2.90667 | -54.0825 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01d272f3-bb09-3f1f-9309-6148a752ae28 | -3.06365 | -54.24868 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6824fc1e-057a-317a-9663-245822f9bdc8 | -3.06249 | -54.16816 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e882b270-ac3a-3e9a-89ef-c1ea0ac07e76 | -3.10747 | -53.76289 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fbdfbc2a-434f-3b59-8c72-4bc59ca6ca2e | -3.68594 | -55.95146 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3ff593c1-6410-33e5-850f-558043a2344b | -2.32545 | -57.98753 | 2026-10-06 05:23:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ece8b066-5ff1-3510-8ca1-ed1e42acbe80 | 0.43936 | -60.53417 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96931c5c-7ba6-3e69-8c1d-83f9aacf0e79 | -3.04388 | -54.23535 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03694b79-866d-39f1-8b75-2a4cb73a6bdc | 2.2661 | -50.8242 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54798f9a-6072-36f1-884c-d4ec8fe8487c | -3.16274 | -50.60098 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5610adc3-a3e1-3c58-a9e2-5b026810de7f | -8.34262 | -62.82987 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf618129-d1ea-3994-bd24-82b25ef05f2d | -3.05825 | -54.1675 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2c86f50-fb4e-3553-8814-bc862444b54e | -2.7944 | -54.13873 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c88a9fc-f291-3ac0-ae1b-32096b32c092 | -1.62801 | -55.13106 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6633f94-fb3b-3b40-9460-67805d9a4a99 | -2.99101 | -57.20052 | 2026-10-06 05:23:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b780def-69d9-32eb-bd5f-b94dd6b23bea | -3.0928 | -54.16873 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c654fded-19ed-3616-983e-c544618df1e4 | 2.45948 | -50.8405 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 37ceb5c3-50ba-3fb2-adca-e97933b0ae52 | -3.05113 | -54.21638 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb7f3566-e1c1-3e14-b189-27b44567ac75 | 3.08702 | -60.56331 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b4dd48e-3a24-3821-948a-8896ca5a3402 | -3.49981 | -54.62838 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8e06895-912a-380a-bd7d-a583e9c15483 | -2.78323 | -57.68191 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8267b138-f586-3c8a-9143-2434bcaf3721 | -2.87607 | -54.17093 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48e8b680-2b16-39ea-99f7-a49db09503a0 | -3.06266 | -54.16969 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b6067cf-864e-39e9-9b01-f9509ec2a009 | 1.98572 | -60.6138 | 2026-10-06 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 360cf232-dcd8-3c16-b2e2-aa38657f5419 | -3.84695 | -50.32028 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c1f4c52-c4dc-3c5e-8bf7-41bf50c03c03 | 1.80178 | -55.54418 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6410183-0d3a-3a50-a2f0-7f56d9252bbe | -4.14467 | -54.02811 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdbe03e8-e819-3deb-a218-bb8216c3fed6 | -3.50564 | -54.61788 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb56de6-52ab-30e7-8761-5b62d0f36081 | -8.85897 | -62.83396 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b2bc1bd-60a3-3c18-9885-07f224427688 | -3.0427 | -54.24305 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e452935-d99d-3e55-8e86-1c9c24279a76 | -3.10129 | -54.17008 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a615b323-9e80-3288-a05b-d1038967b469 | -2.95237 | -54.15258 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f63ce7aa-f529-3805-8688-8fdc8d64da90 | -2.80288 | -54.13999 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1351ff67-920c-367b-b933-dd5a5ee0f218 | -3.07569 | -54.25482 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 07f59058-c1ac-3c28-96d1-b90c7af1f369 | -2.13197 | -56.70216 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f1cd4c33-b1dc-34ed-8be6-021238a3c753 | -3.16647 | -50.60268 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34476f29-3af6-3adc-97a5-310608b2e99a | -3.53754 | -58.59349 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 437393c3-4428-396e-a2c5-a5e349a66287 | -2.88193 | -54.13161 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6a69339-7ce3-32d1-8aa6-33038a5487f0 | -3.05943 | -54.24795 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31d3aa6c-5a25-39ab-b365-0aca9cee8047 | -3.71976 | -57.14766 | 2026-10-06 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27080905-73bd-366e-a1f1-170d352cc852 | 3.12572 | -60.56501 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d0ecc3-8fc9-30de-916e-20a3afb37dfc | -2.88252 | -54.12766 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dc02939-ca66-3970-9540-c672bdb3c28f | -3.13225 | -53.72127 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4ee937e-3c72-3ef4-a846-b24a8929d371 | -2.57319 | -57.79306 | 2026-10-06 05:23:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fdf4bfe-1414-3cda-98ef-52884719d1f1 | -3.09694 | -53.74395 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5b4f70ba-d016-326a-87e5-0745499984c1 | -3.06086 | -54.15315 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 186447c7-0a3a-31bc-a1f4-2ad4e1ba7604 | -3.12091 | -53.70427 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50202a34-12ae-38f6-9728-64607126b891 | -2.99892 | -54.13148 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3485849c-dab3-33ab-8acc-004b86b3bacb | 2.51507 | -60.99691 | 2026-10-06 05:23:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d3c9205-0d75-3dff-ab21-dc01ee46ed24 | -3.16263 | -50.44233 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3020f5a2-9d4b-33d1-8602-14dc2a29327b | -3.11184 | -53.76356 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README58.md)
