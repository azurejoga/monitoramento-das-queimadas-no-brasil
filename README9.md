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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d681c7cb-dce2-3e7a-9d86-a93fd69aef01 | -2.887 | -54.008801 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 819dec62-bb7e-35eb-a044-aa6ab4dfcfce | -2.7864 | -55.355202 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50df07df-e0b9-3b9a-8e95-68cf97bfb0c3 | -3.5134 | -53.817902 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee6ce229-0246-350b-bb5a-e4ccad71f648 | -6.81 | -46.763401 | 2024-12-03 00:37:00 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 568c4814-4979-3c62-a41c-cfd11dbbacc6 | -3.2219 | -53.619099 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ff1e09-a673-3c30-a916-56e62bcde818 | -3.3756 | -50.689999 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 668d5a6a-8a73-3fdd-aada-95689a32efe2 | -5.8 | -46.456799 | 2024-12-03 00:37:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7513ce-77aa-33de-8b96-36e7ddd43bb2 | -2.2585 | -53.594501 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6a8e23-3295-3dd5-9d94-485670c5a076 | -2.8674 | -54.0131 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0459046e-be67-344c-9c77-87e95bb22a4c | -3.7528 | -48.1493 | 2024-12-03 00:37:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5483ac95-685b-3772-b4e6-a9e44d41a4d4 | -3.8478 | -46.516499 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6a4e165-cf69-3023-85ec-0a44cdcee42c | -2.8111 | -53.028099 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc006cc9-d33d-3bba-aa7d-e7e9ec265f63 | -10.6464 | -44.4753 | 2024-12-03 00:37:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b91ec5f-c357-3dcf-973e-848ca9e06303 | -3.2882 | -53.271999 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7ff261a-ca12-3aa8-a66c-eba238c11a57 | -2.8658 | -54.005901 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8064ed8-d095-348d-8cd7-5903e64d7a5c | -2.5624 | -53.388199 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81bbc081-1801-3df3-b369-85c98c9b28b8 | -3.6373 | -55.483398 | 2024-12-03 00:37:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 089d0784-ee71-3697-bd6c-04fa8b4e2e20 | -1.7938 | -46.657398 | 2024-12-03 00:37:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e0ce85-9d13-3763-8c08-2d50e6d01a44 | -2.9519 | -51.778 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62ca81b8-e4d2-3dcc-818c-e286e854ce75 | -10.9044 | -48.5266 | 2024-12-03 00:37:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9509fd7b-b348-3eb6-8140-5700fc7622d2 | -3.8452 | -46.505199 | 2024-12-03 00:37:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82f51fcc-b552-3404-9975-11bb1970325a | -3.7586 | -52.659901 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a807aea-8789-3e85-8c51-249413124aaa | -2.5557 | -53.404301 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38c2f6b7-336f-3a71-9c3d-717e6685dff6 | -2.8915 | -51.784302 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467d97d3-b0e0-3e7b-a789-606787715255 | -2.3528 | -53.922501 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 336998f3-8578-3eea-9f23-44296ed1d682 | -3.4791 | -53.802799 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b418ab-e85e-3f21-8eee-b36c42f44e7b | -2.8542 | -54.046501 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deae8801-9b6d-3b58-b44b-690509449e31 | -2.2699 | -53.5993 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748c57ab-03c9-3c06-9f78-f7258da0bb68 | -4.3914 | -49.764301 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa206325-556f-38c3-b725-3d8d8578494e | -2.8525 | -54.0392 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32be187c-30d7-3581-826c-c735d2b9e00d | -1.7007 | -52.763699 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0717e5ae-65e9-3adb-ac46-4c2ffaafb18b | -2.7413 | -54.0942 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27bc7536-6d6c-377a-b986-ba689455e184 | -2.8101 | -54.033298 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9c443ac-9ff3-3c17-8c41-1748e73f2610 | -4.0818 | -47.345402 | 2024-12-03 00:37:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b32c98d-ce42-3080-b25a-b44570363fda | -3.586 | -53.038399 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb46ee3-7fa5-39ee-8eff-fffa0367d199 | -1.0676 | -53.384399 | 2024-12-03 00:37:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29afb2de-e49a-390a-bb8d-94a8e3af65d1 | -5.1046 | -43.195702 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9617a7e3-5f96-3bc3-9276-694e93ed79e3 | -2.7931 | -53.039299 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d1a0b2-0e74-364c-8db6-dda89f0387a6 | -6.6769 | -46.373699 | 2024-12-03 00:37:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc1e23ce-d13e-36c6-99b2-5de08d168656 | -3.3997 | -50.252201 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840867a4-fddd-3477-a422-5eece9e25cc1 | -3.3757 | -51.008801 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924a8294-64d9-3e9a-8822-9740a61502ec | -3.0423 | -54.058498 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 426d274f-7739-3000-8da5-f1f4b8a4b5dd | -2.347 | -45.719501 | 2024-12-03 00:37:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c87e0d89-1643-3cf9-b87f-06adb13f6a6c | -2.8989 | -53.052101 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5317c1-2610-38a5-b690-d789e1607f67 | -2.384 | -53.8783 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f664a988-63ae-380a-ac36-cd48973bd897 | -3.5554 | -50.3932 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf4cc00d-8560-36c0-b9b6-a59ab84160ec | -2.8493 | -54.0704 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a95412-5092-3699-aaba-4356e3dd7411 | -3.0373 | -54.0826 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf0f3e8-2615-3649-a55b-22fa95204187 | -3.1139 | -53.091702 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1436fed-1ff5-3a2d-8b74-24257915c6a6 | -2.8166 | -54.062401 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba8da124-0281-3220-bded-80c1779da293 | -3.2462 | -53.6362 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66353a04-55e7-3f7c-8ec7-140cd0313c75 | -3.7396 | -52.254902 | 2024-12-03 00:37:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa09cc33-acea-39ba-875f-0e73ae319820 | -4.1654 | -48.196602 | 2024-12-03 00:37:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1249434-d283-3f94-95c1-063e92fa6ded | -2.1496 | -50.692501 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dfa0560-a3cf-3ef6-9881-bba569519874 | -2.4364 | -53.606899 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f6cc083-8670-346d-a2e8-c69e1b48e1dc | -3.9206 | -52.372398 | 2024-12-03 00:37:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a847391e-6c07-3d2d-b71c-373d4afe60b4 | -3.8992 | -53.425301 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 146ae1e8-4997-3152-afa3-006d06d04136 | -1.7433 | -52.632801 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b102e2a1-9193-33be-88b1-56535f34be6c | -3.0291 | -53.4025 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd3b440-c8f4-38b9-a0fa-77b4f8eb39ba | -3.1728 | -53.629902 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 398a94b6-25f6-3377-85f0-15eecb31702e | -3.0849 | -53.3755 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a86d4e41-d73c-319b-a5a1-f89c6fdd9569 | -3.8108 | -49.84 | 2024-12-03 00:37:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 757dba18-d75a-30ed-bfa8-53bece72dcc2 | -3.2235 | -53.626301 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d9abab-fdf8-3d37-b70e-b27fb1535015 | -3.0877 | -53.250401 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 963c49dc-d518-375f-926f-e351c08a08df | -3.2611 | -53.610401 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bad47ac1-6dda-3507-896f-ffb6b52d9a79 | -4.1874 | -50.679401 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0f012a7-6f33-3aff-9fd7-43cedfb1c62d | -1.9013 | -52.876701 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdd8befd-ff55-3f21-b7e8-4cd2f47e7fbf | -3.0275 | -54.176899 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96c4313f-fa70-3ec6-a321-f8b57d8365ac | -3.3497 | -51.2122 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43bd54e3-31ad-311c-9df0-7bd51ba291d7 | -3.0861 | -53.243401 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb81707-96f3-3452-b8c2-baefc01da37e | -3.3773 | -51.015701 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1be771-b779-3e86-b1bf-effa05a84fc2 | -2.2164 | -53.773701 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfdf4e08-141e-3f58-a2e0-6ae097218ed0 | -3.282 | -53.244099 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126d4ac7-425e-303a-84a7-ac93a87f83e0 | -4.5185 | -45.7351 | 2024-12-03 00:37:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41217a80-5dc2-3a92-9e39-17c6cc774180 | -2.7946 | -53.0462 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e27827dd-cc94-34ef-8811-b50c1af9246c | -3.182 | -51.154701 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8a920ac-4e0f-3479-bdd4-1e8a5e2d5311 | -2.4734 | -54.0014 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bebae22-3794-3c83-b9bb-716c437bb274 | -3.4501 | -41.978001 | 2024-12-03 00:37:00 | METOP-B | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e963c73d-c9a8-3b30-953d-b6d3afee32b3 | -2.8256 | -53.0466 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba954b9-82ab-32af-b243-e4388fd8015a | -3.1356 | -54.245998 | 2024-12-03 00:37:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de17d995-7d43-3c01-a3b8-6a336fb3e8ab | -6.1707 | -43.401798 | 2024-12-03 00:37:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70ba0575-3750-3d50-9fa4-c9619bfccac5 | -4.0473 | -50.561901 | 2024-12-03 00:37:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 045b0dee-a68e-3658-8547-f57e206dffb9 | -2.8251 | -52.586399 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e29998a3-1cfa-3f9b-8d1a-8798588c3c7a | -1.7506 | -52.8027 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54361e4f-03fd-3ccb-a92c-c5537e83bdc8 | -2.2684 | -53.5923 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d9efc1-c52f-302c-af7a-d4ab6cd19cbc | -3.4798 | -50.241901 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e4edf4-704c-3380-9334-220aa1dc762e | -1.7463 | -52.6464 | 2024-12-03 00:37:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dce9d996-6da0-38ca-aa47-3cc825ae0337 | -2.4392 | -53.986198 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb1729e-dc99-35cf-8418-8abab7e1bdf9 | -3.2599 | -53.329601 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c585c897-97f7-3b64-ab95-c8fbaa1ea139 | -2.8995 | -51.363499 | 2024-12-03 00:37:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2d37c2-daa4-3965-ad20-589cf871b533 | -2.8075 | -53.0578 | 2024-12-03 00:37:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af3c2c8f-47d1-3ee6-ab34-47ee2675401f | -3.5483 | -50.180302 | 2024-12-03 00:37:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 643bf697-33fd-358a-947b-84af40b8f919 | -3.0295 | -53.8638 | 2024-12-03 00:37:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ccb98f-43bd-3ec6-9cf7-78d185e6a278 | -4.072 | -47.347698 | 2024-12-03 00:37:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae328605-c60c-36d0-ae44-735f360be2c6 | -2.7462 | -54.1619 | 2024-12-03 00:37:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776b082f-146a-3aa9-82fc-59d20129ace7 | -4.1633 | -48.589401 | 2024-12-03 00:37:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f404ef-10ab-38f1-9c19-c2c82f76a16b | -2.2454 | -46.034 | 2024-12-03 00:37:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1897bbca-3d04-376d-8e30-8805901df9fa | -5.1002 | -43.177502 | 2024-12-03 00:37:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7540699f-8992-3570-873c-454c02e94d08 | -2.8706 | -54.027599 | 2024-12-03 00:37:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9134d08-0740-32b3-9c22-577a69a01712 | -3.0593 | -52.756901 | 2024-12-03 00:37:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
