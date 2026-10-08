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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cf236cd-b86b-3069-b02f-b8f49a55166a | -3.0321 | -54.084099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab9ebd89-c503-3095-bced-0a95a46640f4 | -6.2267 | -52.850899 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba945b44-f5f7-3fba-a22c-9bab972541f4 | -3.0994 | -54.973999 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ec351a-1db2-32f8-9272-e1d3eaf3ed28 | -2.9437 | -54.103901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00aebe6b-0268-3d7b-a671-44fa37885dca | -9.4655 | -64.300102 | 2026-10-08 00:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac17b6f7-eb2b-3859-b4f6-89a1888b5d8e | -3.072 | -54.169399 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1124ebc8-21e6-3f66-92bc-1109f2aecfec | -3.1631 | -50.602299 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4358ef4-21d0-3de5-97c5-02f57d21c057 | -4.7598 | -55.666599 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57e3530-e593-32d9-ae12-a4e539b38862 | -5.7009 | -53.485901 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53eccf25-6b2b-39fd-9a5f-83a8fb3dab49 | -14.9197 | -48.106499 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6193691e-e8da-3658-8cd2-c34286cb1898 | -3.5146 | -54.667099 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8150783b-2a51-37cc-b327-680e5c98f459 | -6.2005 | -52.8717 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd9fe72-342a-30d4-b68d-8fa72f30ebed | 1.7548 | -55.572899 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c58d6c9-4926-3f5b-99b8-cd1193f4c507 | -3.1799 | -58.639999 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64af2201-98b6-38a7-b6c0-049b9370c90b | -3.0496 | -53.9347 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14d49a54-7d63-3f50-9934-05e31128d7ae | -3.542 | -59.484901 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee72913-b75d-3fbf-b0b6-84b1ad065b71 | -2.9763 | -54.111099 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e12021-0b87-3bb4-a6c4-f162879b99f5 | -3.169 | -50.449501 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08088af4-f82a-3528-8b0e-11f7befae1c2 | -3.3001 | -54.038799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c81625-7df1-3613-87e0-212c37c13d8d | -6.9933 | -59.098499 | 2026-10-08 00:26:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec2c2fe-5110-3642-942b-17083bea85f0 | -2.9334 | -54.149601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86969f5b-a222-3417-8839-9c9a73786a15 | -3.5296 | -54.6423 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4db966f4-2bde-39ff-8c3a-20fd7ee3520d | -3.5781 | -54.6745 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea1c40c9-d91b-381b-9f0e-ba4b69ed182a | -3.2899 | -54.084499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3931dd79-bba2-3745-b3aa-fdbf91411de3 | -2.9818 | -54.044498 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e11ad6e-0df6-38da-8300-6a6702afe6a2 | -2.895 | -54.071098 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3ffe77-004b-397a-9ffd-f682f30853bd | -3.0242 | -54.0495 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95db4446-1410-3e1c-b797-d4f8578a055e | -4.7468 | -55.6548 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ea2827-e4bb-38ff-a7b8-0b8e56453305 | -7.8423 | -49.277599 | 2026-10-08 00:26:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e175e0ea-8fe1-3834-acc7-4e48400418dc | -3.8251 | -55.770699 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6afa088e-ddd9-3944-bb3f-d1334aa069f8 | -3.1792 | -50.538399 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38dbc5c8-9ce6-3031-9bc0-6f2de91b0714 | -8.2117 | -46.320801 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb38948-394c-31c4-9e91-240f228a27a9 | -3.3112 | -59.462101 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f60272a8-c3d7-380a-bfe2-dc823d3f7ec7 | -2.159 | -59.2229 | 2026-10-08 00:26:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31a68ee1-5830-356a-b3b0-7f3f2f554c48 | -6.3425 | -43.348999 | 2026-10-08 00:26:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23e80bf3-fb77-3deb-abac-309e43a47433 | -11.1024 | -44.005001 | 2026-10-08 00:26:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28587428-9e0c-3560-9a4c-c1854aa4e95d | -3.0516 | -53.897701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e786a288-9dbb-30e5-a717-db9426c27eed | -4.1408 | -54.0173 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8153ce-1cfd-3caa-9610-e4d3152994e8 | -3.0176 | -54.065601 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8870d81b-3766-3e19-8ef1-f4b13f644934 | -3.1566 | -54.7253 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d033a1f-32da-3035-86fc-5b0810fa2f4e | -2.7922 | -54.0723 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2db58160-15b5-3584-a9eb-9d6d320fe2f8 | -3.2774 | -54.029301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8786a90-1d57-341f-bd64-a5431bade7d2 | -5.0473 | -49.756401 | 2026-10-08 00:26:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29015104-c967-3ccc-bdb7-b7772be3096d | -6.5121 | -55.397301 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5087e59f-dbd8-39f4-bdb4-8f7c23f43093 | -4.928 | -55.865799 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2890d6dd-5d95-3e1c-b261-ed921acf11f0 | -6.3935 | -52.723099 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b9fa3a-c746-3d17-ab42-b960f73a40ed | -5.8284 | -52.057301 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc42302-e3ed-33e2-8bbc-0ffe3274957b | -2.4941 | -58.055199 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8df65b97-6d8f-3d91-996b-25dfa57d60b8 | -2.875 | -54.119202 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd9788a-d58c-381e-b333-8927aae68059 | -2.8942 | -54.158401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57ef4e8a-a352-39b5-8f80-db3f05487276 | -5.2403 | -56.112 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39398fbc-5479-3055-aba9-feb11252d1dd | -3.1097 | -54.153702 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b7f4ade-856d-3d3b-b1f6-b74b6fec9562 | -4.1081 | -54.010201 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad92019-ba0d-35d1-9b7f-3a2cf3880a3c | -3.0385 | -54.522499 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9834c17e-0518-3605-b89e-6734870d1951 | 4.0929 | -60.559799 | 2026-10-08 00:26:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d23c7e04-f4a0-38a3-b834-211b9e273f47 | -3.0949 | -53.770699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e9195f-d0e9-306e-9cdc-d18dd3e42057 | -2.8585 | -54.137402 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11a7f4e3-6102-3336-bbd1-4284350a8e72 | -6.0407 | -53.211601 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77101e21-a971-36ff-aeac-43f1ec0f11e9 | -13.297 | -48.672501 | 2026-10-08 00:26:00 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99915e90-c3bb-3e76-b62c-005b89eb5aba | -3.5993 | -54.676899 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74af6bab-f90f-323b-83ab-212dc69f8b91 | -6.1482 | -52.868599 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b16565f7-0851-369d-b6d3-9ac27c58b618 | 2.121 | -50.828999 | 2026-10-08 00:26:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d8182095-cb6b-3b93-a4b4-261577a1d4a8 | -5.3025 | -60.083099 | 2026-10-08 00:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1302d6-ef0e-3243-8a14-f3514b9ca69c | -3.0226 | -54.042599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dcd7324-fbce-38ff-87ec-8b26ffd1fa4f | -14.2241 | -48.527599 | 2026-10-08 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 58ab4381-a5a3-345b-88d9-41b5c4c0af7e | -4.5427 | -54.975399 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0b4ce16-ecab-30ff-9ae4-c8e5217e630f | -3.4364 | -56.931198 | 2026-10-08 00:26:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f48829f9-d943-3beb-9298-8b4c31106130 | 1.7532 | -55.5797 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58bbc108-a28c-3fc8-a8fc-5f66444d0b20 | -2.5114 | -56.251598 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94af55d1-4c27-3796-b50f-bd4897a3fcc8 | -2.4992 | -56.1516 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ff29af-5869-3c19-9f99-a32f9aaa82ea | -3.2538 | -54.653599 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f782d96-ce1e-3d49-bd99-772a82553650 | -5.9559 | -55.3507 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d0e68b7-301c-3a5e-8eab-116134d817a2 | -8.2035 | -46.370998 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 352d8034-cad1-34af-a099-ce9e276fe1bc | -3.525 | -54.621899 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6fe3ce-6b5a-308a-abec-683f92819c6e | -3.0316 | -53.945999 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1143b69-f235-314a-aa8c-56281ea833ef | -2.919 | -54.1311 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6753f35b-40c4-3bb4-912c-9194d2fbcf4c | -4.2942 | -50.7714 | 2026-10-08 00:26:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd36f37a-ad52-3d65-89bf-4be450499c29 | -2.4639 | -56.086399 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9f47b8b-bc70-3d94-aaf2-7b567f93b127 | -10.8864 | -49.1395 | 2026-10-08 00:26:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4621b20c-9338-3b8f-9df9-2be9f0c5de07 | -7.2236 | -44.287701 | 2026-10-08 00:26:00 | METOP-B | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b3d7752-dd06-3b8a-86a5-688d68c4153f | -16.754601 | -53.375301 | 2026-10-08 00:26:00 | METOP-B | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e030a1f3-2857-3b1e-a4ee-919d4f6a5e56 | -2.8197 | -54.102501 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a3f8f3-77cc-399f-ae95-0ad904739f01 | -3.7142 | -54.2281 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de851500-bcf4-3df6-bcd2-beb2d87f88ec | -6.141 | -53.063499 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b16989f-d367-332d-ad1d-4e7edae16a01 | -3.4289 | -59.5303 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3daa7238-74a1-3015-bb4f-b00330b042fe | -5.6692 | -46.357101 | 2026-10-08 00:26:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb0b4b6d-b7fa-3a3b-8c1c-ce43ad4d9a06 | -5.6941 | -53.5019 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddec8ae2-bfca-3f45-90c1-913ba8e71584 | -3.1609 | -50.5928 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f1947c7-a13a-38f4-9e25-5a79e7560d08 | -3.5214 | -54.651299 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d90cc62a-9e92-3985-be11-0406fd61e9c8 | -6.2349 | -52.841599 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b50ba959-db66-3195-b696-b4e1dbecda4f | -3.0927 | -58.017899 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3463e283-66e2-3129-a8c8-be109fabb3aa | -6.2527 | -52.874802 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b4647ba-bde6-3a91-802d-d7f352bb4908 | -3.3036 | -54.008999 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c53e6c9-f0ff-3fc9-82cf-f7fd2fb60c95 | -5.2448 | -50.9142 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9333f956-03ae-3e02-993d-52adc4f3a3c7 | -7.3936 | -55.194901 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a1fff6-e08c-3db4-ba82-4ec065163df2 | -5.2428 | -50.905602 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec77ad29-e45c-390c-a03f-ea99b283395f | -3.0591 | -54.157799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a274ba-fafa-393e-9c21-6094c8b56806 | -3.2809 | -53.999401 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 321f3f58-0b5f-398a-a2f2-6a8322f67c5e | -6.1359 | -47.955299 | 2026-10-08 00:26:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ade69792-1482-3ff8-835c-ed7f874539b6 | -3.4941 | -59.2686 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
