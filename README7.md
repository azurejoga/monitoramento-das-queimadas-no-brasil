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
| 47070a6a-0a4e-3fcc-a5ea-b2a11fdc140c | -3.0975 | -53.248299 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e060c55-7d2c-3848-9bfe-63873abe111f | -1.6187 | -52.674599 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 784d1740-b49e-3a5a-9c12-9f90091d43f5 | -3.3481 | -51.205299 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b417d909-972f-3eb6-958d-7e3e8636733a | -1.7417 | -52.625999 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b76c1ec-a191-30bb-a95c-d13b7eec65ac | -2.8885 | -54.153599 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0e5c028-7c7b-392d-a702-0c54e045c643 | -3.106 | -54.021599 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5acea77-135a-3743-81a0-7da99009f531 | -2.8509 | -54.032001 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 457df77f-f82f-393c-abee-993e02d311a8 | -2.8787 | -54.109798 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e751962f-d62e-3b13-94eb-866878e84f90 | -2.6399 | -54.192902 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36ad118b-0ad0-3aff-86f4-7e56bd12d5a0 | -3.4045 | -50.228001 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5c4276-83ee-3403-8b85-0026a649e6c8 | -3.5449 | -50.1656 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43dd320a-f476-3caf-893f-0a6b05360b23 | -2.6415 | -54.200199 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2445531a-d918-33ca-844b-cab6d0845a2e | -1.9428 | -53.335701 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8f4995-a88c-3241-abfd-c9c830503f70 | -2.3407 | -45.692501 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6dbe2e2-dce8-3251-948e-51331bdcabc1 | -3.0374 | -54.036701 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d962360-7dd4-3a4d-b9c5-5d4ba70b5952 | -2.1887 | -53.558601 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41868adc-58e7-3324-90ca-8eecdbb6eebd | -1.3453 | -51.3727 | 2024-12-03 00:37:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 792726d2-bfcc-3127-b088-4fae4d72e482 | -1.6978 | -52.6143 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67a89ef-0a7a-3e86-9395-e6e7a36000a6 | -3.9221 | -52.379299 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b489536-5ed3-379c-8afe-e7531af0f16c | -3.0323 | -49.364399 | 2024-12-03 00:37:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7567195-be1d-305f-b549-dc407c7013c0 | -3.6475 | -51.116501 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd92a2f-69ee-30f3-b910-9f214208d9eb | -1.7258 | -52.600899 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7e47c1-25e9-32eb-b4db-4fe17f173f6b | -3.5112 | -46.1758 | 2024-12-03 00:37:00 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc78cc84-a101-3b0d-9e98-7d8f9baec3ac | -3.1833 | -54.3214 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3474728-c500-3dcc-a5e3-86a357a7c6e3 | -2.047 | -51.1945 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ba82018-0d41-3ece-a6fa-8d6c09da1068 | -0.827 | -48.723999 | 2024-12-03 00:37:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e09898-3ccf-3818-86b4-674c30c0b0cb | -1.1069 | -54.107498 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70bf122d-542e-3394-9bc8-90b4542898ac | -1.7429 | -52.7686 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde6ab13-d153-38ed-89f3-0904cdcc003f | -1.2417 | -54.523701 | 2024-12-03 00:37:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7a9cd9-479f-3579-8253-9b7d29299b2d | -2.4357 | -54.0172 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53248b13-d389-3b1f-b9a7-aa1fd18bbf17 | -3.8774 | -52.317501 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9241d58-7d78-32cb-80f3-cfb06ad831ad | -1.0816 | -53.446301 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6095870a-92e1-3a64-85b3-14155c94246b | -2.8756 | -54.003799 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d321cbb7-da29-3069-bcea-85e592be7fe3 | -3.5181 | -46.161499 | 2024-12-03 00:37:00 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1d16cb-7dde-3275-bdb5-a88aa805fb73 | -1.08 | -53.4394 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62a6b175-17a6-3a72-adc2-7ecfc597cae9 | -4.2551 | -50.841499 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72aba2a6-7e8b-37a4-9e61-33ecea188354 | -2.8297 | -54.028999 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c11952af-9434-3763-b39a-9533ad7083ce | -3.1233 | -50.2603 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a01782-cce0-3c36-9702-abfbd424041d | -3.2789 | -50.310101 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a77cee9-60f1-3252-9ea5-037683c940bc | -2.8446 | -45.388302 | 2024-12-03 00:37:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7701d9df-6243-3796-876c-ce99c079ddb9 | -2.4776 | -45.574902 | 2024-12-03 00:37:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a50dccc6-a35e-3e20-85ab-413a6a530e84 | -1.6932 | -52.593899 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 391c30c2-b4ae-3647-9d72-e2c76042318c | -3.0718 | -53.9151 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2cb1f2-ea06-3be4-a4e0-a82f5c426284 | -2.8044 | -53.043999 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e12f75-a64f-397b-a664-cf9cc5059334 | -3.2806 | -50.317402 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77bbeefb-5fca-3547-a354-b5f2cdb0ce37 | -3.1175 | -53.9809 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98f2f9ff-7917-36c4-b7aa-4b7a8a1f6871 | -2.2617 | -53.608601 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14918ca7-8550-3d7b-b2c3-6b345fab2efa | -3.393 | -50.2229 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6281de-e668-36e2-b0a1-f33566ef8992 | -4.5616 | -45.090199 | 2024-12-03 00:37:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a7e81a3-ed9c-3d2d-a635-aaade26c9ea8 | -1.9457 | -51.202202 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 610d162b-e68e-36d3-abf9-76d41d7a0e24 | -2.279 | -46.356602 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 937a2225-0695-38ce-af77-441d437908b4 | -2.2268 | -53.682598 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47312206-f364-3f97-aa57-895a499c8ccd | -3.7507 | -52.395699 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7b2c05-079c-3e89-873b-55f1951e0a99 | -1.7402 | -52.619202 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbefa08a-b0d3-34b6-bedf-330d6aa79247 | -1.8197 | -55.263901 | 2024-12-03 00:37:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c29f09a-30bb-3266-82bb-f92617d4d417 | -2.7578 | -55.318802 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb39149-3b0d-3b57-92f0-da5f00e53532 | -2.7596 | -55.3269 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de2b3df7-b105-362c-8482-565079be7878 | -3.2115 | -53.113701 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a96bd8d-b096-3bd3-894d-8f50ba3758ac | -1.3406 | -54.9632 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a50b382-a097-38ef-96ec-fefa40e2d66d | -4.0372 | -54.2285 | 2024-12-03 00:37:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a41ad19-0ff8-3225-bc84-2de266699fc0 | -2.4424 | -54.000599 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf3a5b5d-c41a-3382-96ad-ef27c821a633 | -3.2838 | -50.785099 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7867ff23-c180-35f4-a599-2971d12a4630 | -2.8281 | -54.021801 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a60edee6-c7c9-3df1-8fd3-4a9eb925f337 | -3.7601 | -52.0714 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b41bd5b1-188e-3aba-a416-cdb957e6a453 | -3.1143 | -53.9664 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb6dab7-b745-376e-9c4d-89a088428cbc | -3.1109 | -54.0434 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 160b86c7-953f-3cb5-a949-3fc7f99419d0 | -2.6684 | -46.618698 | 2024-12-03 00:37:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de807e05-f665-3f94-b26c-e852cfe624b6 | -2.8127 | -53.034901 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e14a56-23aa-3a21-a530-63093d8a420e | -2.361 | -53.9133 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b08fbe8e-9be8-34a0-b3cc-468d90a006bb | -2.564 | -53.395199 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f84de4c-a784-3aa2-9998-e11049037963 | -1.3658 | -51.964802 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6030940-253e-3492-a86c-74a804b7a0c6 | -2.6557 | -44.974899 | 2024-12-03 00:37:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99394630-0d2e-379d-8299-5de2800f55a5 | -1.9049 | -52.847301 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5e7410a-ea73-3c99-8bc7-f4be96706ede | -4.7271 | -45.094601 | 2024-12-03 00:37:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c92ecbad-121e-3aaa-b1d6-133b776d6137 | -1.7414 | -52.761799 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4253f1-9fde-3373-8064-35d79a6ba2bb | -3.0913 | -54.001999 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fba86d9-bb81-3f4b-90ff-be2d24d6f291 | -2.646 | -44.9771 | 2024-12-03 00:37:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5661ed23-7b5d-30a0-a775-e413211d365f | -3.6628 | -50.185398 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 060ac241-4b46-3ee1-9618-0b52dcb6f841 | -3.3367 | -51.2005 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34544a67-572c-30f9-8583-21bc3fa92057 | -1.4443 | -54.829201 | 2024-12-03 00:37:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4650b0c-fe34-3911-aeb9-7a1c1baf1699 | -3.4361 | -45.854198 | 2024-12-03 00:37:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b306e60-a899-392b-9a47-d32217393dd3 | -4.0115 | -49.9519 | 2024-12-03 00:37:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00415db2-d36c-3fe0-b5db-0945ce45dd81 | -3.2283 | -51.723801 | 2024-12-03 00:37:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e07ad73-c02e-3f75-a0d0-9cc9429f3155 | -2.6689 | -52.442101 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37bb7667-8864-3920-a2c1-37127a642c2d | -4.2665 | -50.846298 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8a12fb-8101-3002-9203-2fd124918f95 | -4.0253 | -46.925499 | 2024-12-03 00:37:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba4092f0-6e28-36c1-8946-2dda2cf983c2 | -2.3536 | -45.703701 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03a4566c-55ce-38b2-b8fb-dbcb13fe87a2 | -3.3351 | -51.193501 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e68a79f-c948-3669-970b-9270116c0f1f | -3.0684 | -54.037498 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9283ab-cd75-3098-b90c-ce4b036be155 | -1.9527 | -53.333599 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6a769e7-bb09-32a1-b1ee-e7cceb8c354a | -1.9028 | -52.883499 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4281b935-0991-3e69-a01f-6f48d67f1b28 | -5.805 | -46.478199 | 2024-12-03 00:37:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d3dbf9e-f0b8-3ae8-8ee3-072999872152 | -1.1669 | -53.412998 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9910bbe-104b-3178-8caf-ba0e47f31e08 | -1.7874 | -52.737301 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31dde1fa-995a-3f92-87f7-cf2b0efe1111 | -6.0154 | -46.234402 | 2024-12-03 00:37:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0733a5e5-ed72-3c26-b734-9c4681785f78 | -5.8148 | -46.475899 | 2024-12-03 00:37:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0b780e0-8e87-39a9-8986-afc55d8c5903 | -3.1919 | -45.293098 | 2024-12-03 00:37:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92dd36c9-8e81-3513-93d1-06702270af61 | -3.2529 | -53.619801 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f344a0ad-2843-34ea-ac28-e9e65509d957 | -3.2478 | -53.643299 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a7554c-aa06-31d2-9fe8-71d2a2409855 | -2.8623 | -54.036999 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
