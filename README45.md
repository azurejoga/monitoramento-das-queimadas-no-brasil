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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0892343c-6624-337b-8ce5-281b72a59634 | -3.9393 | -55.51785 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fc0a0b3c-c1f3-3d0d-a7e9-0b63cd913b5e | -3.2762 | -54.00782 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c666e802-7943-3cbf-882a-3cdc38ef2075 | -3.04463 | -54.22861 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3d36035-d741-30cb-9a66-9333c4876ffb | -6.08609 | -53.47968 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff9030e-1cd2-387b-943d-385bd04aaddc | -6.17998 | -52.93262 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d21f4c9a-ae0d-389c-93bd-1bc5f7bf6fc7 | -3.7112 | -50.64445 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 893eaafb-cc24-3553-b799-226802831844 | -2.89936 | -54.0827 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa802e36-9e78-34ff-8d14-2f494714b7e3 | -2.77605 | -45.5138 | 2026-10-05 04:57:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 029705ed-9dd0-3e3b-9abc-1d37ace5bc39 | -3.04402 | -54.2324 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7593f58-c860-3a89-b0fa-5d8f8f68aae0 | -2.80954 | -54.09616 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c750975-a04a-34af-9b0a-95c66bbda72f | -6.20189 | -52.7945 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75bcbe29-a090-3342-a51e-2ad0484776ac | -2.8939 | -54.11641 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d3dc5f1-ce91-3500-b3b0-3d8163182e4a | -6.61463 | -52.99829 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d5c4ff6-77ce-3965-bd7d-f930ee09fc5c | -4.82197 | -49.8797 | 2026-10-05 04:57:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d87b496d-fde5-3152-a285-5b3a7fe1cd11 | -3.80254 | -47.49001 | 2026-10-05 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e5abfd-eacb-338c-8fa6-672eb65c7dd0 | -2.88457 | -54.13036 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e2e7fa2-7a4c-3017-bc8a-3e00e496ff85 | -2.2212 | -53.71978 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6630537e-8b69-3839-8a69-c10e58801dc2 | -2.78482 | -54.0961 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb8f8732-c8b1-3d4f-8bb7-0609be859a6d | -3.10453 | -53.74396 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b8ff3ddb-e159-3cf8-ade1-3a682e369d06 | -3.31458 | -53.8555 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2ef3fa-ef2a-3ec8-9898-be698df59a4b | -5.80702 | -52.75598 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb14256b-924c-3da6-a714-db5856911095 | -7.23054 | -55.19224 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfc812bf-9517-3c33-8ccb-7c1e4e06c291 | -7.51311 | -54.98663 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e15f55d6-e242-3841-9323-f5ae5293624c | -7.49762 | -54.99553 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a3ed42-0027-3fb2-9659-8cf1ff9f1df7 | -4.28475 | -50.26901 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96aedaf4-9d5c-3426-abb1-5b538e716ead | -2.3689 | -55.27064 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcc6d3ea-4323-34ef-892c-501fa0359efc | -2.94435 | -54.13219 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a82e94-975a-3670-a037-d68f115a150b | -2.82374 | -54.11769 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c09ef24-5c15-319b-9866-2708d82cdcd0 | -3.06505 | -54.38015 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f339b114-07af-3d45-9c6d-f9bda65f9fa4 | -3.88519 | -55.80789 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea8ce75d-e568-33a4-8de8-c1316604c14d | -3.02366 | -54.18273 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49846fad-685d-338f-9ed8-35d0e218a700 | -7.49822 | -54.9918 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc2c0696-25d0-3d32-999a-b66bd60d6668 | -6.00879 | -53.5172 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8bf789d0-ed34-35f3-99ee-d50c84518ce3 | -3.05622 | -54.39055 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c23dca-a773-3670-81d0-51c221c6349c | -2.91538 | -53.94021 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d8b9e9a-33d9-368f-b206-bf6fe4957618 | -2.89207 | -54.1277 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d370a7e7-b2a3-39af-ada1-37f8d7e96f12 | -3.29815 | -53.84914 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1c7329-63f3-3290-b875-ea086ea6e1bb | -3.22375 | -53.87528 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1d8f28d2-9267-31f9-8c65-7623ef0609fc | -3.05154 | -54.22971 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cc96ba18-03d9-3cbd-87b3-37bb3122405b | -3.05034 | -54.39388 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c52bded-8e5d-35a4-8c25-8626febc315d | -3.10289 | -53.7325 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2cbcba1-fbd9-3760-9455-02563122ac7f | -3.31293 | -53.84399 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02766915-efc0-3f4b-935e-6d7bc8f159a3 | -2.81014 | -54.0924 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86341dbf-67fe-3f16-832d-9dee626761bc | -3.47198 | -50.09016 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41c48f0-51a5-3dd6-a396-8341c551bfa4 | -6.80741 | -55.29533 | 2026-10-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5d25d2-332d-31b7-8ba3-848b35be184c | -4.28861 | -50.7883 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74cd9122-d376-328a-a822-45099c894aeb | -8.53401 | -54.59558 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b5f6af1-c1aa-3269-a7fc-334ae8a40d3a | -2.90846 | -54.09184 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 65d7b878-3e18-38b2-a9ba-10f0ac8d0230 | -6.20716 | -45.40558 | 2026-10-05 04:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 051d4fc5-7699-3777-aa59-59883e42f19a | -6.91036 | -43.68479 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7810338-3716-3e08-a65c-5c63a7f2e5b3 | -1.24989 | -55.87877 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d8a045c-20cf-3975-a3bd-cda2e07f4fa7 | -3.01488 | -53.88784 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86e090e9-cbb6-3c42-82bb-4c2e8956ecfb | -3.30671 | -53.83925 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93ec3a36-3847-3637-9a48-3a467ff4e534 | -3.28408 | -53.8282 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f6f8b9-04b5-33b3-82b2-be39a3c8b1c3 | -3.07493 | -54.17163 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a238dd26-8a4c-318d-a701-ae9456446278 | -4.44395 | -54.9679 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4da6a897-5626-3ef7-a096-9af03b3a0f33 | -3.12499 | -53.72481 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 611edae5-e545-3061-bb54-3dbe448f4632 | -4.29286 | -54.80142 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fae83f8-c44f-3619-aa7d-9067de4c3248 | -3.07174 | -49.52736 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 344d5ae1-794d-39bf-81b1-d6dc49a82ab7 | -2.9034 | -54.07951 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 776e0351-be15-3b02-989b-8759651f3bd7 | -4.11027 | -50.80503 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5a697c9-b600-3d17-87f8-de74c828cbc7 | -3.04868 | -54.22538 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1e224dfc-8e48-3b4b-be9d-a49d79da9854 | -3.46443 | -54.5988 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 38117d9b-68c8-3728-90e0-b337963928f9 | -7.50164 | -54.99236 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a756f73-8ebb-38ee-86ed-349cb1f6103a | -3.28454 | -53.847 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c60c10e6-d555-3394-838c-42b0eb9a5ef5 | -3.65242 | -55.32166 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc48ade7-184e-3f4a-9a1c-969cff3f28da | -2.59707 | -48.95173 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3336f5f7-dfe2-3ca9-a310-4998ef8466e2 | -2.80754 | -54.13054 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26e1e0c7-0580-37d8-83f1-4b36bb94fa72 | -1.46446 | -54.78652 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf1575ba-af67-373f-8331-b994c28732f6 | -6.70877 | -45.55582 | 2026-10-05 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b852a288-324e-3383-aa75-d3bc10e5705e | -6.31854 | -52.93634 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4931c7a-2098-340e-ba03-779a7e93a355 | -3.46796 | -50.09336 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 574ee410-55a1-3c47-bb02-3effb503d10f | -3.27368 | -50.01425 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a62a59a-35e3-369b-8789-b1fdd5a5dd4f | -8.6716 | -54.5442 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 64027b72-b1d7-39f0-a84e-b789ecee78b3 | -2.80865 | -49.8715 | 2026-10-05 04:57:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcfba8c9-c332-30f5-8cd0-0ee42b1196fa | -3.90408 | -49.71345 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26d80035-b2e2-3b96-9e08-dc1f3be2ade3 | -3.71231 | -50.65943 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab219e08-186b-349c-9ddc-0e5266d77b1e | -3.5086 | -54.61374 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a28eec0a-4b4f-3c16-b1c6-afa43676197b | -7.72761 | -45.46434 | 2026-10-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0f7a82-517b-3f1c-bc4a-46cf98b62fa6 | -6.18605 | -52.93711 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9eb8655-3cc7-3e51-91fe-4d14dc4c8654 | -7.22931 | -55.19984 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f458212-0943-3b73-89d2-9fcbebe0e4ed | -6.20303 | -52.83009 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1636c1e5-4a88-3e81-868e-a68bb150e339 | -3.28232 | -50.40841 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84feccbb-41f5-3286-bad3-d45b5ddd4187 | -2.78421 | -54.09986 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01028600-c478-3adb-843b-1752d49b2d90 | -2.53742 | -58.03674 | 2026-10-05 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 140d591e-eb5a-3c45-b021-ea6457ea9cf7 | -2.16318 | -53.66583 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d1b22f1-d063-3687-8e94-db6936bbdea4 | -8.53123 | -54.59143 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e50488-0b6d-3cda-b13c-d8d7466f5652 | -2.24014 | -51.91598 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a700a23-c85c-307c-9c72-7889a6180e23 | -2.27085 | -48.74541 | 2026-10-05 04:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cdcb762-4bd3-3d4e-8113-c0692bd8df05 | -2.57732 | -51.86732 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5ab0a3c-2311-33b2-a8e0-14dd7c73420c | -3.56007 | -50.28912 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b233f4f4-3567-3726-bd20-e628839c017b | -2.9188 | -53.94075 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9de3370b-0bcf-383d-9834-bfb71c233837 | -3.07345 | -49.53957 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d95e3e-2730-373f-9c1d-9dd6964f2f1c | -5.9937 | -53.6334 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d47967a0-197e-3a0e-bd01-9d643768363a | -2.98926 | -51.0457 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 339f6585-1a30-3997-bf33-24e9e1007062 | -2.83687 | -54.21285 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10d2e48d-e742-358a-8d64-73cb223195cd | -3.11307 | -53.73412 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bf09c2a-25fc-3d09-9a0c-dddf835606f6 | -6.17668 | -52.9321 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0f2860d-3bb3-3083-8681-6d14019386ef | -8.67217 | -54.54062 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9103700-8722-3bdb-8376-0bf7435f460b | -3.84034 | -55.96766 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
