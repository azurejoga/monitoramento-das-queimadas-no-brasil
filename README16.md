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
| c9aa3b6d-0054-3fba-b6a1-b2414880087d | -13.6975 | -50.941299 | 2024-10-01 00:51:20 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77134480-8d48-31a3-9bdc-82c7dc7e726d | -13.6991 | -50.948299 | 2024-10-01 00:51:20 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec93ca9e-cedb-3817-a36e-f9ec17ad2089 | -13.6293 | -51.0975 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba7e37c7-d533-34ec-a6b8-71366ff36e82 | -13.6309 | -51.104599 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24b28fa2-9515-3b97-8f4b-10682f4cd814 | -13.6164 | -51.085701 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 846dccd1-3d2d-3fbe-8c18-07a79db93fa4 | -13.6179 | -51.0928 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abc7b515-9fb8-34a4-8a07-79ab1d0d1bb9 | -13.6195 | -51.0998 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eca2dc91-29e4-3064-a2ea-f5414a84fb47 | -13.6304 | -51.148998 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d80f536-760b-36e9-b197-03fbf98035ed | -13.632 | -51.155998 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c6c3d21-37d6-3552-809f-c47e676f2eb0 | -13.6335 | -51.162998 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84821c8a-bbf7-3570-8eba-23f3669b261c | -13.6003 | -51.059898 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5094bbba-fac2-3cb5-9477-6446489885ab | -13.6019 | -51.067001 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad6e4f8e-2c80-3e88-a520-3cb520de05fb | -13.6222 | -51.158298 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbbd0603-99eb-3b0c-9f7d-d328dd79fbb0 | -13.6237 | -51.165298 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa312a29-5629-319a-a03c-27c923cf9173 | -13.6253 | -51.172298 | 2024-10-01 00:51:22 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29ed4357-a855-3860-9c31-5538f7d9f6a5 | -13.5752 | -51.132198 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe701881-d2d3-341b-94db-814f75bc5d30 | -13.5767 | -51.139198 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8085c4-d042-3572-9b3e-9bdb8fb7c41e | -13.5783 | -51.146198 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b3dc6d7-28a6-3c0c-8960-6def55ff523f | -13.5799 | -51.153301 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29e0cb08-b4f9-3027-938e-48f0e2750351 | -13.5814 | -51.160301 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d685c559-6fa0-3f1c-83a0-d4433fa1ac43 | -13.583 | -51.167301 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8607d504-92e7-3f18-b779-234a5ba6d87e | -12.9695 | -48.5219 | 2024-10-01 00:51:23 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20996e63-4452-3ee9-bbf9-6b11e893b8b5 | -12.9714 | -48.529999 | 2024-10-01 00:51:23 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3691b4bc-ae4a-3f36-9d1d-46f7ffee01ba | -13.5591 | -51.1064 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fdb5d883-ebfe-3535-b8ce-23f50f3adb9d | -13.5607 | -51.1134 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8da0e214-5681-3826-960e-b5087f0e3cd7 | -13.5623 | -51.120499 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 634d4bfc-27a3-3d0c-9ff0-3e831b11c65a | -13.5638 | -51.127499 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ded59f8-9162-33ab-a5a4-3fab33e44194 | -13.5654 | -51.134499 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fedf3b36-4d42-3f66-97a5-3e26a3f04ade | -13.5669 | -51.141499 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e28b4ea-5b00-3d86-808a-cc56e90cd647 | -13.5685 | -51.148499 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b85d817-2458-324e-8efb-87bcead0fce8 | -13.5701 | -51.155602 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 992c9105-ace8-32c8-bfa2-d11fc270e36c | -13.5716 | -51.162601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c0f1359-ff66-3033-aa92-6be6092325aa | -13.5732 | -51.169601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36894a0c-93d1-3411-be38-37e427e37702 | -13.5747 | -51.176601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21bc1331-94c5-3b22-bd2f-43045c7af506 | -13.5462 | -51.094601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8ad0df-7d35-3df8-92aa-31fb6891592c | -13.5478 | -51.101601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98bcb76a-2b16-38a4-8f9b-d56456eababa | -13.5493 | -51.108601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8589960-3ca6-3cf1-9893-31dc14d9eab2 | -13.5509 | -51.115601 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd17a619-164a-3a9f-8342-76c19b9fd594 | -13.5525 | -51.1227 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e49b2bdb-59b0-3755-94c7-781f851a1e4c | -13.554 | -51.1297 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2091390a-61b6-3193-be2b-a944f7003442 | -13.5571 | -51.1437 | 2024-10-01 00:51:23 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7d04484-d217-3fe7-b63c-e65ddf27116d | -13.2793 | -50.181 | 2024-10-01 00:51:24 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14acda02-e08e-39c6-a24a-e1e712748a03 | -13.2809 | -50.188202 | 2024-10-01 00:51:24 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec5e5cc-b97d-3e60-9c49-3476e0bce770 | -12.0723 | -44.975498 | 2024-10-01 00:51:24 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea4f81a4-e7bb-3aff-ba30-b12f86cf7de0 | -12.0755 | -44.9888 | 2024-10-01 00:51:24 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 595e3ace-3015-31ea-9051-fbb2cdbfb431 | -12.0626 | -44.978001 | 2024-10-01 00:51:24 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8314d7ad-8a38-3953-899e-80a08e596493 | -12.0658 | -44.991299 | 2024-10-01 00:51:24 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc31c5ce-acee-3ac3-8207-7abf7a5c4eb3 | -13.538 | -51.103901 | 2024-10-01 00:51:24 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 103bd43c-04f4-3b7c-8d33-2e9c79c8d944 | -13.5395 | -51.110901 | 2024-10-01 00:51:24 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a469b149-14d3-394a-8ea3-a3a5441fffc3 | -13.7836 | -52.409302 | 2024-10-01 00:51:24 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 93b8848e-0306-33a6-8b1e-26f83ae32e92 | -13.7851 | -52.4165 | 2024-10-01 00:51:24 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0aed1e49-d01f-38c9-a07e-f892ce3f9398 | -13.7867 | -52.423801 | 2024-10-01 00:51:24 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4726f39-0a0d-377f-84dd-f7a33ea1117c | -13.7738 | -52.411598 | 2024-10-01 00:51:24 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1a0755-9311-3392-8daf-e235657ebe46 | -13.7753 | -52.4188 | 2024-10-01 00:51:24 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51c43f53-e323-34c6-a3d0-59619a245dbf | -13.7769 | -52.426102 | 2024-10-01 00:51:24 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1418198d-6e41-3d18-b404-0506f7810c17 | -14.8794 | -57.980801 | 2024-10-01 00:51:25 | METOP-B | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9c0c900-a45b-3cad-b83b-41717d8b6908 | -12.4668 | -47.486198 | 2024-10-01 00:51:27 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db8d017c-b191-3089-a4ce-3b1465c146ab | -13.3223 | -51.338001 | 2024-10-01 00:51:28 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 338257f0-4755-336c-a5f6-542e55126ccb | -13.3239 | -51.345001 | 2024-10-01 00:51:28 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2ba754e-2cf0-39bd-b5b8-403ffea5b6f2 | -12.5186 | -47.966 | 2024-10-01 00:51:28 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8200caf8-c0c1-3e01-a493-6c4e6b6954ea | -13.2453 | -51.223 | 2024-10-01 00:51:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd1d644-747c-3225-b4fe-bb768d42482c | -13.2484 | -51.237099 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f30f98f8-70af-3a54-bf8a-cb5ba5432f4c | -13.2324 | -51.2113 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba4ded1e-fd72-3412-82c6-0d56274d57b1 | -13.2339 | -51.2183 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1836c63b-59ed-36be-a14b-1252fa408ab6 | -13.2355 | -51.2253 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83018552-92d9-3154-9e3f-43ded3efac5e | -13.2371 | -51.232399 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fdaf314-f4cd-38d6-9dd8-447d3d7e95fc | -13.221 | -51.206501 | 2024-10-01 00:51:29 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85537777-cb3c-34c6-bb01-62685e39c88f | -13.2226 | -51.2136 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5464e9e0-b07e-3601-a46f-c537ffc2194d | -13.2241 | -51.2206 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c75b92b-5fc9-3d29-adde-64da5fe98d23 | -13.2097 | -51.201801 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66204631-a668-3020-9e4e-54a0223c7b9f | -13.2112 | -51.208801 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| faa37fff-7135-3e76-a89c-60c489c3026f | -13.1999 | -51.203999 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d89fcb10-3980-3b3f-846b-fae74ef78455 | -13.2014 | -51.210999 | 2024-10-01 00:51:29 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3bb955-c93d-3877-82ca-982f5470f444 | -12.9761 | -51.263 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 413a0867-3900-36c0-b0d7-bd7f799467ad | -12.9777 | -51.27 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91e024bd-8ec5-3878-9bd2-14609016672e | -12.9792 | -51.277 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff374b7f-82ac-3fcc-b248-0db95b997ef1 | -12.9808 | -51.284 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 912def82-5d19-3a67-9453-144de6eba33e | -12.9824 | -51.291 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dfd8fb1-0dd7-3e27-adc4-9718b14bc6bb | -12.957 | -51.223202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f02036fe-90b8-3805-904a-e926ef5ca4ae | -12.9585 | -51.230202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| afdb985b-cc2e-3505-bb7d-e568bb005853 | -12.9601 | -51.237202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39df0676-996c-3a76-9b82-6ae87375d41d | -12.9616 | -51.244202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4065ad42-21cf-3fd5-9444-0737b94fa6cc | -12.9632 | -51.251202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5a99b52-a001-3b5d-adbc-f2faa47134c9 | -12.9648 | -51.258202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aafb8b01-3b53-31cd-a148-b2bd12db875f | -12.9663 | -51.265202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce165fa7-d22d-39d1-9c5e-436d033b0170 | -12.9679 | -51.272202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a371c3a-d758-3829-ba63-04ba89cca39b | -12.9694 | -51.279202 | 2024-10-01 00:51:33 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9951249f-f3be-3a9d-a8e0-9c8d73f9376c | -12.9596 | -51.281502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af2b217d-d1a7-3bda-a0c1-837e2c303a36 | -12.9612 | -51.288502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad068db3-f6d0-3507-a7d2-ecd1bdddc706 | -12.9628 | -51.295502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99acb179-d444-39ac-9427-4ec74be4cca2 | -12.9643 | -51.302502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bbfbc59-8840-3123-a5ae-54778917526e | -12.9659 | -51.309502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2b84a4-d617-355b-9633-3a3795178b7c | -12.9674 | -51.316502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 728174d0-1c3c-3183-8d4d-27e861f747b7 | -12.969 | -51.323502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d312bd94-d7f9-375e-9e2f-599de9a7855d | -12.9706 | -51.330502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9cac9390-1f2c-3e13-8536-93403d70bed8 | -12.9721 | -51.337502 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a56c483-9c45-39f2-bee6-8c597faea58f | -12.9737 | -51.344501 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dfd78915-1bc6-3d58-9584-3b4e9eaad3ab | -12.9752 | -51.351501 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e617ecb9-d603-31e2-8489-191d4f602449 | -12.9483 | -51.276798 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 27e47a53-cbc8-36a0-bc6c-579f910d6e8d | -12.9499 | -51.283798 | 2024-10-01 00:51:34 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
