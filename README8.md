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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c638abf8-6790-3de9-afd8-8e014e5bb2e9 | -2.6017 | -48.199699 | 2024-11-11 00:51:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffcc3ec-dae0-3288-81ff-99e014937ca6 | -3.3549 | -51.679199 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d580c5-35ef-36a7-8341-1ffbc02ef409 | -2.4556 | -53.700001 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a8fdb78-da02-3165-86cf-71f7a7db60ff | -3.6952 | -54.3951 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86e63cc6-19ae-3697-9b98-f610329499b5 | -2.4267 | -53.8895 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6aecae5-a347-35b7-9b93-a8312025fda2 | -2.633 | -49.889 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18ee02a-a1eb-3408-95d8-6d8f89a98586 | -2.5401 | -47.3176 | 2024-11-11 00:51:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8372b3cb-ef2b-387f-a6a3-afa0465936f7 | -2.8938 | -54.176201 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af5d6f0-567a-3e0d-b530-e508fc1a1c27 | -3.1159 | -54.473598 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34a0c1e1-124b-3d5a-92be-091168c66674 | -3.637 | -52.325901 | 2024-11-11 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3688f7bb-4ca7-335b-a526-5012527d8e8f | -2.8712 | -49.447399 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe66f43d-6a68-3859-91c0-8cd94d82c0fc | -3.3093 | -50.494301 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b90d7fc-9942-3688-81c3-ca83ffc7271f | -3.0281 | -50.975498 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfc82f3-5b4e-3c48-a344-82a52a4fba8d | -2.064 | -53.294201 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b32b1a3-b51a-39f3-ad52-9966fb797b5f | -3.6627 | -54.660999 | 2024-11-11 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29ce6d23-bd25-356e-9fa8-47646cd28cdf | -2.0603 | -53.4132 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab922b2-432b-391a-9f96-6b5b0f69f572 | -2.7366 | -49.3564 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa39a558-bd30-323c-809d-1be4dee3d4e5 | -3.8957 | -52.239399 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c8771d-cae7-3500-8166-3abf699f7ac7 | -2.992 | -45.260799 | 2024-11-11 00:51:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4bad314-eb30-32e1-92d3-6f04833ce92d | -3.5065 | -53.789501 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d68135c0-7f0b-39cc-b790-532adbe8737e | -1.3927 | -52.074902 | 2024-11-11 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7688983-0d76-38d0-813a-43fcc2794b56 | -3.6929 | -50.636299 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ffb54b-42d4-309f-b372-93bf345400b1 | -2.2795 | -50.681599 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc93d3cc-da1d-3cdf-aa42-57a3fd6e9c60 | -2.4842 | -52.561199 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed750587-41bc-32bf-a30b-299b39c960f3 | -2.3087 | -53.823799 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f303844-efd4-34e7-9173-e3d6fcae4007 | -4.1167 | -49.1241 | 2024-11-11 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 838f0efe-1c11-3a0b-83e6-71d1a9818ea0 | -2.3089 | -50.674999 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c31ca5-2a34-33f9-9567-264db25713e3 | -4.0824 | -43.934299 | 2024-11-11 00:51:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f0266c2-70fe-3209-894c-ef6d596bac9c | -3.1068 | -53.708199 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac4d69f-5133-3625-ba7c-a4153857254b | -2.9042 | -49.367298 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0edb93b9-ba47-3144-88ad-214108ebcaf7 | -2.8107 | -51.6007 | 2024-11-11 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474ebbc9-10e5-37c2-8d21-b93823d71933 | -2.7482 | -49.3619 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 024aac1b-7d18-3bcd-9869-0cfad34f4706 | -3.8673 | -51.979801 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30d0d959-33d8-3a0c-9079-b1b33330e26d | -2.4036 | -46.515701 | 2024-11-11 00:51:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db914320-5fc7-39c3-8b04-bbe9367e08fe | -1.5142 | -52.1549 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9094408b-05f1-399f-9089-fe16726010a4 | -3.0797 | -49.367901 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f45ce5a-8455-39e8-9c33-77c628c9422e | -3.5257 | -49.9571 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fdb619e-e480-3cfa-be1f-bbf42ba97055 | 0.1711 | -51.104 | 2024-11-11 00:51:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 72d5affc-2f21-33c9-84a3-6642e3a9aeab | -3.1411 | -50.435799 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88518e26-e23f-3ab4-991a-fe24941a704a | -15.3008 | -56.4981 | 2024-11-11 00:51:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 505933b8-fcfd-3b99-8dfb-80758bf2d407 | -1.5127 | -52.148102 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3b9ec2-7c47-3cff-9c69-e1becd615fd4 | -2.8123 | -52.959099 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6523a4-0914-306b-a429-591c43545c19 | -1.7557 | -53.749599 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 655678e9-e4cc-3af0-8c11-75e523b8e2bd | -2.9326 | -54.120098 | 2024-11-11 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a83a0a2-178c-3376-b7b2-c4f773c488a3 | -1.0231 | -48.858002 | 2024-11-11 00:51:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 375207f5-b958-3dba-8994-4693ed80083e | -3.0887 | -53.266602 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa46a8f2-fc8a-3793-b734-cceef40a874a | -3.2372 | -50.181702 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a009525-1423-3e97-af7d-28ba28769c87 | -2.3187 | -50.672798 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb922bc-f134-3c2b-9e54-2b13c5c37306 | -3.9448 | -46.414799 | 2024-11-11 00:51:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c640fc9-8176-36a5-aabb-351576485e55 | -3.1884 | -50.2831 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7eed37f-a7e1-32a9-b569-feb3a5c98f17 | -2.345 | -50.562698 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ede463a7-a823-3b71-ae6f-a94fc7d17e7b | -2.7544 | -49.344299 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eed95bca-b12a-3da4-aa32-eccb1a613bf5 | -2.7018 | -49.339901 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d79a31a2-191c-395f-b44b-7a2f6d30b5aa | -3.0918 | -53.3256 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4061159e-e290-340b-8504-921d67acbcf8 | -1.1752 | -53.916199 | 2024-11-11 00:51:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcd00870-6741-3105-a9e1-45ca43c5b5df | -3.139 | -54.484901 | 2024-11-11 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2265408b-cb01-33c5-abd3-591317b7ed12 | -3.2276 | -50.2742 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 740f2637-9a2e-31a7-b1e7-250b91b84993 | -3.0813 | -51.0723 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50c2176-0b7f-3bd2-8f49-60ad21e40932 | -3.025 | -50.961601 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff354336-8c67-3075-9138-edaa660b99c5 | -17.6394 | -57.529499 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1f6b003-ff01-357b-b53c-ddd31cd62a2c | -17.610201 | -57.534901 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6414a64e-6cc1-3fc8-805d-22ebf52de297 | -2.1915 | -48.385399 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11eb3c01-6501-376c-831e-1fcb57b1fabb | -1.6576 | -52.644798 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e86ef5-2c1b-37ac-9591-67b84086b154 | -3.2391 | -50.5028 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36ae69cf-95ec-3b65-8329-140a63b75a06 | -0.32 | -51.581799 | 2024-11-11 00:51:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 46a57610-062b-3175-94ea-54e8a943c865 | -2.9767 | -46.983101 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73f1f0da-5808-329d-b48f-fdeefb2aa168 | -1.6228 | -52.537899 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eacc170c-193c-3bf9-a84b-04d7577c012d | -3.309 | -50.1353 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae6773d6-dc1e-36d5-b50d-cfbefa97d09c | -2.3038 | -48.469299 | 2024-11-11 00:51:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a5954b-6110-3e48-9c6e-8fb893db8aac | -3.5142 | -49.952 | 2024-11-11 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc4eb75-477c-3221-9360-5d9e6f3abac8 | -17.6164 | -57.513599 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8251d3c-b490-3cb5-9be3-aa5e30e86153 | -2.6762 | -51.823898 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9adb447e-44ec-300d-8018-a6216e51cc4e | -2.9238 | -49.362801 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 603c390c-ca4e-3b9a-a495-bd32b1e74b6b | -2.8753 | -46.6395 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dedda5f-8a5a-3b5a-9526-b83b102bae00 | -2.788 | -49.222 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53318bec-cb22-302a-ad19-da45810af2b2 | -1.5381 | -52.213799 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2a2d36-df94-3a9c-8719-f4a0e879c1b2 | -2.8322 | -49.145699 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd875567-f4b1-3e75-bac0-12b1deac0ad6 | -2.3967 | -49.848598 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47796c32-0bbf-33a0-b469-b2d676d27b38 | -3.0297 | -50.982399 | 2024-11-11 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa6a0a7-d16f-393c-b811-b96d23b0667a | -17.6005 | -57.536701 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2927b600-8f1b-38df-81a1-08fad8e49506 | -2.5666 | -47.342899 | 2024-11-11 00:51:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed51c7e-430c-3ecb-8302-176542545a38 | -2.7313 | -54.140999 | 2024-11-11 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 995755fd-e837-339d-bc93-358e54e31aef | -2.3835 | -49.835899 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b5157b-182a-307e-bd33-9122ac00e919 | -1.5111 | -52.1413 | 2024-11-11 00:51:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da20ac4e-7458-388b-97b9-e4d4e2e1f169 | -2.9263 | -49.507198 | 2024-11-11 00:51:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76e395d-8b07-3dad-b29b-ba2c91aa4a19 | -2.5786 | -47.350498 | 2024-11-11 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4c56d4-e4bd-3ff8-a923-d158cbb5a282 | -3.2606 | -53.7048 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e20e564-c15c-32d9-903e-de5a27b44c26 | -3.8977 | -52.2029 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 101efc5f-9291-3dbd-8e03-5ba09dbd184b | -2.4469 | -52.218102 | 2024-11-11 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb7ea5d-76e6-3fb8-9b3a-49345e678fad | -3.8941 | -51.9165 | 2024-11-11 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 150e1b19-7198-3262-b5bf-06c3aadd54c1 | -17.6026 | -57.436199 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02476eba-abf1-36a2-8cda-75ad8e08bc09 | -2.758 | -49.359699 | 2024-11-11 00:51:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f054595-41c2-3bb2-912a-d80a077bb400 | -2.8362 | -46.648499 | 2024-11-11 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4963aecb-bab4-36f0-8980-1f05d33f8fd4 | -1.2209 | -55.784199 | 2024-11-11 00:51:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac31fcb-28f9-381f-94b2-4715fa858465 | -3.2704 | -53.702702 | 2024-11-11 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a0ef725-40c2-354b-a50d-b99823196981 | -17.612301 | -57.434399 | 2024-11-11 00:51:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d26e252-8d0b-36bb-99bd-fafa2993034e | -2.6901 | -49.868301 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938fa146-6999-33f1-a123-61a9ba1f21d1 | -2.4232 | -49.873901 | 2024-11-11 00:51:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d022922-ee85-38a6-aedd-cc1089a3eecd | -3.2365 | -53.055801 | 2024-11-11 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f89ddb7d-053b-3b50-bd7a-91dab61ccbd7 | -1.3257 | -47.7187 | 2024-11-11 00:51:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
