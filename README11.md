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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11adbaf5-7ae1-3586-ae7c-b38992a0328c | -2.9564 | -54.103001 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a0995ff-77fa-3469-a349-b1ef6f3e0e88 | -2.8784 | -54.120098 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dea9603-3be5-37ad-a31b-349d66318b28 | -5.1882 | -45.491699 | 2026-10-04 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e7b454-b6b1-338c-bd38-f89d519d79fc | -5.7393 | -45.154301 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4b2902f-0f30-30f2-800e-821cbd8a7086 | 3.4262 | -51.302898 | 2026-10-04 00:31:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8b044e51-3067-32a6-9457-e7d969b02ae2 | -7.7513 | -49.195999 | 2026-10-04 00:31:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a071b9d6-982e-342e-8277-db0e964503b6 | -4.8082 | -49.282001 | 2026-10-04 00:31:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021d3f28-7086-3762-a71e-6b791245f810 | -1.4857 | -49.439899 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc3b29df-8beb-3498-8182-afb91b0212f3 | -2.901 | -54.1292 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7482238d-b0fc-3464-a407-503e7064db12 | -6.9008 | -43.678001 | 2026-10-04 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bede25eb-f2e6-3a00-a4d2-a4cb6e18cc18 | -5.5282 | -44.956799 | 2026-10-04 00:31:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07198180-8631-39e9-ab32-3904c4f5a69c | -2.8071 | -54.121498 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0225ff75-c4fe-3c46-936c-63aca3c6c981 | -5.7359 | -45.139801 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fcc82d6-ce24-31d9-855a-000845d3afb7 | -2.9844 | -51.0443 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 256e83fc-b773-34c5-b5bb-459e14055514 | -2.8845 | -54.146999 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5ed6e98-d4e7-38ce-be3b-e3951bb7c91a | -1.4154 | -49.267799 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e3adbc6-b6af-3c25-8309-9b0943a25723 | -2.5749 | -51.868301 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25f97b6f-f994-3770-9b6b-871fcd5e5dc4 | -3.1269 | -53.722599 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3036147-4162-38b7-ba64-1e3bc65c4af8 | -7.8932 | -45.320099 | 2026-10-04 00:31:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 05ddc95d-df89-32ed-860e-0c97c1e82664 | -4.267 | -46.3717 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c2213f7-44a0-37f2-9a08-fc5a407b1855 | -3.7021 | -50.670601 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 759bd530-031f-384d-88be-c2c8c3e60fa7 | -14.5695 | -52.8857 | 2026-10-04 00:31:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4971cf08-cc43-3fb2-a0c3-d5c125a571b1 | -2.9662 | -54.100899 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90a780ae-3845-3395-87e2-9111fe301114 | -2.0257 | -46.941101 | 2026-10-04 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e205de62-3293-39f2-a1bb-463ad9180e2e | -6.1862 | -52.8004 | 2026-10-04 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55590a5a-fd81-3a52-9e4a-49b1dc8ae635 | -2.7913 | -54.096901 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181c23a1-aff2-37b7-976e-35e9a5cb46bc | -2.8579 | -49.627102 | 2026-10-04 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4e88eb-1272-34b0-b344-91e4e37f9e87 | -3.7002 | -50.662102 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd90f2a-f75d-3841-8ebd-b57be15b1955 | -1.1654 | -49.256401 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2659bbce-f464-35c2-bcc5-3144438c1688 | -4.2923 | -50.278198 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ad3f09-2684-3e37-8160-4540ba470f71 | -3.3551 | -43.384399 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3596d7ef-9cbe-36aa-9daf-6356335e3c90 | 3.428 | -51.2953 | 2026-10-04 00:31:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e84c6e6b-1b59-363c-96d2-18c8c28fcd68 | -0.3596 | -52.074799 | 2026-10-04 00:31:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e50dd7d0-5d57-3b76-b04f-453905ca33c5 | -4.2019 | -53.4492 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cccbe1d3-44e3-3d8b-97ac-d61751949904 | -5.582 | -49.016399 | 2026-10-04 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72690434-2b3a-3581-aabe-624621f02966 | -3.1171 | -53.724701 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69755939-18e9-368f-88b9-572eadfa7e91 | -3.1033 | -53.754501 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72c85729-979e-3895-87e4-c3d57ad4b6a0 | -4.927 | -45.7006 | 2026-10-04 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8e72de2-7375-3b88-a33f-66088c382e9f | -7.2801 | -49.249199 | 2026-10-04 00:31:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68b6da22-aa8e-38e5-8d8a-576c8e107c96 | -4.8099 | -49.2896 | 2026-10-04 00:31:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2f3b470-81f9-39c7-b655-a009196117e9 | -3.1644 | -54.0718 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15384781-82e1-35e8-9153-c763ec1b8e93 | -15.2449 | -40.5368 | 2026-10-04 00:31:00 | METOP-C | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1684b253-c823-34ee-964a-6c7b847a20a2 | -4.1916 | -44.2701 | 2026-10-04 00:31:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67793d53-168a-34af-9da7-73850dd89408 | -3.3628 | -43.373001 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5dbf45c-5a0d-3e80-b129-40849687c92b | -4.3757 | -44.395699 | 2026-10-04 00:31:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 219e19e1-18ed-37f4-8ba9-d3e393646d2f | 1.9174 | -55.7658 | 2026-10-04 00:31:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f049b845-0530-3d5c-ae0b-b38956284037 | -14.5663 | -52.868801 | 2026-10-04 00:31:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fba38167-26c5-3bbc-9d12-40ad90526039 | -2.8717 | -54.135601 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb290b8-d52d-33b6-9840-7185568b6392 | -7.4773 | -47.6059 | 2026-10-04 00:31:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22f4343a-a3a4-39c9-a714-81614d35530a | -2.8004 | -54.1371 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ac326f-9bb4-3e98-8c62-5f201b95f83f | -2.6707 | -54.4245 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9480deda-e17e-36c4-bee4-d14655e013a0 | -4.4583 | -50.970402 | 2026-10-04 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c57e03e-4dc0-31e1-8e39-815b02aad0c9 | -1.8118 | -47.849998 | 2026-10-04 00:31:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344758e7-c8f4-3a8a-8962-43c9fa5948dd | -2.9632 | -54.087399 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 069c9350-f80a-3f15-8533-227fb540c884 | -3.1832 | -54.110298 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 888ab64d-263a-3982-bf6f-a228da408de5 | -0.4651 | -52.041698 | 2026-10-04 00:31:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 622b7225-0270-3322-afa5-bea603e93e92 | -3.2758 | -53.838902 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebcb94c-5892-3d0b-8037-4b74fe5ea9a3 | -3.7841 | -44.380199 | 2026-10-04 00:31:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d44c9cca-24bb-3e2c-8221-c4afb065b62e | -3.71 | -50.659901 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278226d0-4921-3446-9bd0-6ada655a9bf2 | -3.4611 | -50.106201 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cdb90d7-794a-31ec-9e1f-3ddab2778718 | -4.4886 | -45.545399 | 2026-10-04 00:31:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61e261fd-6bb0-3857-be02-5a4e7876fc9c | -2.94 | -54.120701 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072745b8-3f1c-31c1-80b5-491875e5c0b1 | 3.3746 | -51.347599 | 2026-10-04 00:31:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2fd32be5-045d-31f6-9ca6-c747d6ab6088 | -6.9027 | -43.686001 | 2026-10-04 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27030ecf-6c95-3596-81c7-b3bb38f2e166 | -5.5427 | -49.756199 | 2026-10-04 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01abfc7-d9ac-3909-a20c-f5612fd2e289 | -3.8171 | -51.5457 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e8dbd3-3c01-385b-8b29-45b999a70b4a | -2.9967 | -53.872501 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3407a4-5ab3-358b-9e9c-6a80e0f39a01 | 1.9209 | -55.751099 | 2026-10-04 00:31:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7699b2c2-710c-3ee9-bdd3-9b5a6a58d594 | -2.7981 | -54.081402 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 715fa24f-6890-3a7b-a223-6db1d1014d8f | -2.2072 | -53.687698 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ef5c04-76ad-3478-840a-1aa03b120542 | -3.0903 | -51.103298 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67e67260-dab2-3a18-a999-5f807c5bbd4c | -4.1097 | -49.0625 | 2026-10-04 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 417fb787-f2dc-3b22-ab16-b62d58a21ece | -1.6426 | -48.325199 | 2026-10-04 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175ef040-3e5e-3133-ac7a-00626b104910 | -1.5005 | -49.459301 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b255a99b-704c-3e77-94a1-fe5fc0e78359 | -2.8989 | -49.400398 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c74d432-9e4b-3fbc-9799-162b3cc75782 | -1.6086 | -55.020302 | 2026-10-04 00:31:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 732c3f9a-4a3c-32b3-95fc-e3b9148cc27a | -5.5514 | -44.216599 | 2026-10-04 00:31:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0655c65e-416d-3372-8d02-5f11c2d102ad | -3.0424 | -54.212502 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9a5e5d-2651-3fdb-b3cb-cd7ada25eac5 | -2.9168 | -54.154099 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d232f57-a8fd-37fa-b242-55f51078939b | -5.6244 | -50.028999 | 2026-10-04 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da6b3d3-d039-308f-a028-74b7827aec63 | -4.5152 | -45.883099 | 2026-10-04 00:31:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4b5bd3e-3655-3f8b-80c4-721ce1bda896 | -6.0666 | -47.292702 | 2026-10-04 00:31:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2c54998-6c3c-3c54-a3bd-d7a85e509cc1 | -4.2867 | -50.253601 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74cef0d7-eafa-3751-917d-4f0c49191cd2 | -7.7531 | -49.203999 | 2026-10-04 00:31:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f1737484-b555-3748-beeb-0e070175921c | -3.0617 | -49.527199 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c23354-3f67-38fe-80f1-3eaf50f776a6 | -3.1228 | -53.750198 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e84e8978-5594-3d2c-b8f6-6ce806b9489d | -3.2729 | -53.825901 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4cbce0-a3a9-3ec9-a077-87586dc4715a | -3.124 | -53.7099 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbbbb66-de56-32ed-a1d7-15d9e70f1aad | -5.5495 | -44.208801 | 2026-10-04 00:31:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1b3c523-6f73-301a-8924-86b6745fefb4 | -2.9729 | -54.0853 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1a9ab0-09c3-37af-a595-a305c57be27b | -5.9987 | -53.533401 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36fc4bfe-e320-3eb8-8a9c-7bd9297be969 | -6.7123 | -45.9706 | 2026-10-04 00:31:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3481fdc-9b20-32b9-9902-e62ec413c41a | -2.8011 | -54.0947 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0e4df25-26d9-30b6-b8ec-73f180e010fb | -12.9773 | -41.1712 | 2026-10-04 00:31:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6506e9b7-47a3-3b01-abfb-9f93a8da765c | -3.8726 | -49.696499 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d83f6d41-0e09-3eb3-8085-df4507dc7003 | -2.8441 | -51.2873 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42c94cf1-6c7d-3168-b804-6545cef8296c | -4.5544 | -47.487301 | 2026-10-04 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9865f864-4cda-38c4-af52-85d1a53bfc7e | -4.2637 | -50.744801 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a13a729-51e0-3b55-addd-8e62aa043767 | -3.1297 | -53.735298 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1b063e-751e-3f25-aa68-557e100b5e3f | -3.6983 | -50.653702 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
