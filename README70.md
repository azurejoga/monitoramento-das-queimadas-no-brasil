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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65ad2ba4-c106-387a-bed2-d1e43efe580a | -2.9114 | -54.11655 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a4d0443-0230-36f3-a5e8-94b72420861d | -2.91079 | -54.12041 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4438901-1ec6-3ea9-b2e3-c362c0a84bb5 | -2.91019 | -54.12426 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22d71ce6-bb11-3f00-a6da-c7e71ef7aa21 | -2.90959 | -54.1281 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aafcce1c-5b7e-3372-9ab7-e88fccdb9697 | -2.90851 | -54.11216 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe90b527-5375-3983-b950-7ca31b579d5b | -2.9079 | -54.11602 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 62fdb7b2-330a-3f6b-9807-554671fe1af0 | -2.9073 | -54.11988 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9abc4984-8997-3eba-8eaa-99bd9a5cbe11 | -2.9067 | -54.12372 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ed8ab09-4173-3acb-92b0-58c95c5e2e13 | -2.9061 | -54.12757 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1dfe6b4a-e794-3022-ab55-348bdba1a413 | -2.90562 | -54.10777 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d261ee-46ca-3faa-9fb6-d624b01ea2b7 | -2.9055 | -54.1314 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35c5d58e-1b91-3d1c-aa91-90ec000db2c8 | -2.90501 | -54.11163 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ec49ce6-24d4-3fb1-a4be-d989f654a265 | -2.90441 | -54.11548 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e2cf4ef-2fcf-3b90-b5f4-f6ce811183d5 | -2.90381 | -54.11934 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8dd953d9-800e-3365-a2e0-28c9c1bb265d | -2.90321 | -54.12319 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 067f9d90-3d68-36a7-be1c-e1b3450bf343 | -2.90261 | -54.12703 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1357f90-1634-3cc9-9018-13d1fe23d3d4 | -2.90212 | -54.10723 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61ab0e2d-1860-3684-891a-7f6f86bbdcae | -2.90152 | -54.11109 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2c9c7d4-015e-3a45-a9b9-1e959330f8e4 | -2.90092 | -54.11495 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a19e851-de39-3b79-9b9c-0e61b3ab1bf4 | -2.90031 | -54.1188 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c8b7dc6-96b7-37b5-93fb-06694f7c2029 | -2.89971 | -54.12265 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f083e31b-57dc-3437-9402-809199b44dd5 | -2.89923 | -54.10285 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d8f95ef-b264-3cc5-9e8f-95e0de3edcce | -2.89911 | -54.12649 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f809859f-958a-34aa-84d8-581e258de725 | -2.89863 | -54.1067 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7acea293-becb-361d-9e91-9df183474126 | -2.89852 | -54.13032 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d54ad8a0-43d5-3ceb-8bc3-176e08a9500f | -2.89802 | -54.11056 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 35b935f2-aed6-3f8c-9ac5-bb85eca62c80 | -2.89742 | -54.11441 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe24d3d4-f0c6-3c57-9bfd-ae3e1b1e1ccf | -2.89682 | -54.11827 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 173e24c1-c19e-38b5-84aa-655193502c51 | -2.89622 | -54.12211 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 923f7578-951a-3608-b745-b39c249998fa | -2.89562 | -54.12595 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba2a00c0-308e-3aad-86e3-2b3b0c4f86f8 | -2.89513 | -54.10617 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d284e677-f1b0-304b-bd5a-f0179076efe1 | -2.89502 | -54.12978 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aeb6c4b-1d0a-3466-9dc5-c0e61fb5cbf8 | -2.89453 | -54.11003 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f598001-f74f-3a2b-9d16-4019ea5ae5e4 | -2.89393 | -54.11388 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e18f6cc4-0f09-3ca6-acd6-21acb0e57e3f | -2.89333 | -54.11773 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7051fa8e-13f0-383d-b941-0492114eb4cd | -2.89273 | -54.12157 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2f77867-adf8-385b-a276-2392f3d59080 | -2.89213 | -54.12542 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 617106c0-8c09-3e20-99f2-8f214f7edc98 | -2.89164 | -54.10563 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ce1c93-7d78-3cf4-994c-8f58e11a6942 | -2.89104 | -54.10949 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 231de5e9-3499-3fc7-8270-190157141922 | -2.89044 | -54.11334 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56858dc0-0d6d-32d8-be67-943df5e89c36 | -2.88984 | -54.1172 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 109b93d6-51ce-3f5b-a4cc-59049dc8d221 | -2.88754 | -54.10896 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aef8c481-d1ee-3a4d-89b7-a0c984f75e38 | -2.88694 | -54.1128 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3d0ee2c7-077f-3ba1-b92b-15b707a8e9b7 | -2.88634 | -54.11666 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db73ad0a-6782-3320-9e03-165ed41ade05 | -2.88465 | -54.10456 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fbcaf65-39fe-30f3-a16e-0a5ff4b570dc | -2.88405 | -54.10842 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d606ff1-862b-3360-a694-ae9e95bac374 | -2.88345 | -54.11227 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e190935-faee-3d17-aed7-d529ced7a073 | -2.88285 | -54.11612 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92f3638a-5954-34c4-8334-8b10d492c23d | -2.88115 | -54.10402 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e7d3b6d-7723-3505-ad77-00354e4ad286 | -2.88055 | -54.10787 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edfdf457-fcda-37b9-863f-1c8a0723d11d | -2.87996 | -54.11172 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ad62e0b-8917-3042-907c-712840ca2d99 | -2.87766 | -54.10347 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fe32384-5cf6-3e8f-8c59-7c7ac021b9a4 | -2.87706 | -54.10733 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc44f75c-4701-3fdf-a97b-6e333ecda7f9 | -2.87646 | -54.11118 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d57d4590-121c-3a1b-ba98-33a8b939fe19 | -2.87357 | -54.10678 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e17d3f28-db03-32c2-aebd-6564a8ccf210 | -2.83405 | -54.06119 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74b43628-ec0f-33c8-8e9e-ff74d67aec9d | -2.83301 | -54.06197 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88a7735c-d6e2-39b2-8153-f72b81296fa9 | -2.82815 | -54.09283 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72ce8794-dbf5-32be-97ed-b619e656d62e | -2.82583 | -54.09155 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a552db2-a0d1-3f7b-8368-cd8632d031a5 | -2.82465 | -54.09229 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12e90ed4-4b43-3912-804f-0ac59e853ce8 | -2.77864 | -54.08913 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8af512ff-7c6f-3f07-8a6a-36aaef84cf28 | -2.77804 | -54.09297 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 186b81e7-b2a8-33a7-8832-9497d945763e | -3.45615 | -53.92766 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d98774e7-4d0a-3c83-b52e-9cd711a82a46 | -3.41539 | -54.52427 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aad6ac7-7b28-3e18-b95f-5cdb960c36b0 | -3.41193 | -54.52375 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee62c596-b501-31c9-b11d-be545cce2aa6 | -3.41015 | -54.52024 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eec14db-7bcf-3aed-aaa0-f4567fa623a0 | -3.38699 | -54.55518 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8131d90-2c17-3cde-8760-ab055b1a46e6 | -3.38627 | -54.60482 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 833fc414-257d-31dd-8e5c-2b94d00eddd4 | -3.38355 | -54.55464 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 331c3e39-29f4-34ba-8369-dbb71e1917b1 | -3.38296 | -54.55842 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4dea209-ac48-3dd1-8d8f-0e4ef7642cb0 | -3.3801 | -54.5541 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fb16e51-fd6a-3d89-a75d-71b90f812660 | -3.34774 | -54.64847 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ffc2e7c-1261-3050-b9f8-9c87507709b6 | -3.23949 | -53.76609 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c0e2fc2-52ac-3ffe-9045-8387cb9e7876 | -3.23888 | -53.77006 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6470165-a87a-3778-9948-1fb8cd7704c0 | -3.23593 | -53.76556 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f073f02-2fbd-3c6e-b22e-2d948fdc9b5c | -3.23532 | -53.76954 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a812dc52-936d-339c-a193-99060571177e | -3.23236 | -53.76505 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be82a0ea-512a-31d6-99f4-a8d47c5e70bd | -3.23175 | -53.76904 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83504e54-6e20-3a22-b695-1f5d142d84bc | -3.16246 | -53.75527 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b1cdc1a-ce6a-3864-8ca1-fde36032f0c0 | -3.15828 | -53.75872 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddb2cfc9-7a59-37b5-9349-32c4c2d22004 | -3.13789 | -54.0981 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccefc018-31e3-3224-848c-9c556ce435dd | -3.13499 | -54.09369 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5b1b806-3a11-3049-83af-4d21a56992a7 | -3.13209 | -54.08927 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad387285-3816-3fa0-b0c5-e58dceef6a99 | -2.713 | -53.9331 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b65464bc-792f-3bdb-b3f6-53b36807cf9a | -2.67011 | -53.95451 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddddd1a-f1cf-3413-acda-eed7677e65f7 | -2.66719 | -53.95018 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c1cd60-09a2-363b-8bc0-e21f6a9685ac | -2.66659 | -53.95401 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed276f0e-d3d4-3643-a31a-61d7a8ddbbcb | -2.66308 | -53.95352 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cad91321-01df-3e87-acaf-68ee08e73dd8 | -2.65956 | -53.95302 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 642d723a-8fd2-366e-80aa-3d3fb3e1b66f | -2.58321 | -54.00111 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c282eacf-a86b-36f1-a067-a8978eae3a2f | -2.57911 | -54.00443 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9adff8e4-2798-3310-a212-d0a3bb548b58 | -2.57066 | -54.0816 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ca5d36-f430-3624-bbb8-65a44d46bfbf | -2.57006 | -54.0854 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c2d901-ed23-3d2e-81d9-752ef7a7093c | -2.56717 | -54.08104 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e060ab-8025-3a8c-9593-566dff9fee36 | -2.42526 | -53.97741 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd81d810-95e9-3a64-90ea-c2482f8c5778 | -2.42466 | -53.98125 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4fc4607-e7a3-31ca-a806-0eeb8b051282 | -2.41244 | -53.96754 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f355712f-bcd9-3091-b2d4-d9d8dda5b4b9 | -2.41201 | -53.96432 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6948962-2e31-349d-b66f-791de67e72a0 | -2.4114 | -53.96818 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 917da828-5da5-3ce1-b51b-fa8107b8ed7b | -2.40807 | -53.94384 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
