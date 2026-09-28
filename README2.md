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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da828b75-05ba-34c5-8f3e-9330b0cfb3a3 | -10.2067 | -49.9898 | 2026-09-28 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9966c54b-a813-342d-9b1e-577db467d8aa | -9.9266 | -60.7171 | 2026-09-28 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b5e3a2a6-982d-32ef-a870-f58e4a2dc8ff | -20.1966 | -48.5773 | 2026-09-28 00:20:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c021a16d-81dc-3f93-879b-705beea82d0c | -6.6872 | -45.6456 | 2026-09-28 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 3467daf8-b015-3621-88df-afa92d63bf88 | -10.4043 | -53.8236 | 2026-09-28 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 382a82d2-bdb8-357d-a4b8-cfcd818d557d | -11.4616 | -44.9276 | 2026-09-28 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f781a806-4cba-3bdb-a114-f8eae68203fa | -3.1472 | -54.0648 | 2026-09-28 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| dd9e0647-a69e-311a-81d2-c8b5c2620d1d | -10.4232 | -53.8219 | 2026-09-28 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4e9e49f3-597f-3e2d-8069-a3fc6b1d9897 | -12.1925 | -50.3904 | 2026-09-28 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 010d673b-b642-3e14-8738-4afebab78e00 | -2.998 | -54.7492 | 2026-09-28 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| b6f40bc0-2670-3131-9f28-f39cb6f982a3 | -11.7173 | -44.5422 | 2026-09-28 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6db0c5b4-04ce-3205-983a-d4f8243f6e56 | -3.1471 | -54.1049 | 2026-09-28 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 72c4acdc-855d-3bd2-afa0-811a657dd659 | -11.0962 | -51.3231 | 2026-09-28 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 55b03c48-e8e2-3955-a78f-b3da891f763e | -3.1471 | -54.0849 | 2026-09-28 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| d4fef4c2-e966-3575-814d-6e21570a3fbb | -3.2137 | -51.0384 | 2026-09-28 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 39adee61-6c5e-3de4-96a7-34efe531524e | -6.7059 | -45.6441 | 2026-09-28 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 97d069c8-d807-3647-9208-e9bf7c253275 | -2.7766 | -49.4977 | 2026-09-28 00:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| c0a976cb-51af-3187-931c-f680a90a73f0 | -11.1152 | -51.3211 | 2026-09-28 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 05a7d5e0-5f68-3ff0-b688-e4f82ed9831f | -8.2288 | -45.4829 | 2026-09-28 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ae894f4e-53d5-3d5c-a674-f20e895b421c | -11.4429 | -44.9072 | 2026-09-28 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 069c6df1-3cbc-34fd-8538-888c6e5e84af | -11.4425 | -44.9303 | 2026-09-28 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 7ce073db-01f9-366f-a3ac-3707252b1e3b | -5.7376 | -47.3804 | 2026-09-28 00:20:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ffcf3218-c4b5-3f06-af31-6283721e1693 | -12.1928 | -50.3689 | 2026-09-28 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a2014e16-ee08-3dae-b67f-d630ea38b03e | -6.5977 | -47.1667 | 2026-09-28 00:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 894b9ae6-54fe-32fb-9ea2-46e334c727f5 | -12.6267 | -47.2851 | 2026-09-28 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a25b77c5-4c7c-3ec7-9006-10c2ba7ce8b7 | -9.9973 | -50.1393 | 2026-09-28 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b51c8c3f-8f2a-3d00-9001-3c1d99f20cd8 | -11.3436 | -54.1086 | 2026-09-28 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 54297250-5347-3e98-a928-be727c0807ff | -2.7767 | -49.4765 | 2026-09-28 00:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 4793efeb-5623-3cd6-b4a4-f54e81879f91 | -11.0959 | -51.3443 | 2026-09-28 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ca3ab015-3aef-301d-94ad-f5cec19f116b | -2.7242 | -54.1953 | 2026-09-28 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 39e0d890-faa2-368b-9547-fc4f00811483 | -10.2065 | -50.0113 | 2026-09-28 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5c6d666c-bf66-373a-8343-411ab0354b9f | -3.1953 | -51.039 | 2026-09-28 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| bf48cdd2-3f32-3498-b203-d734e7de3eb1 | -11.6981 | -44.545 | 2026-09-28 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cce237c9-fc0f-32aa-b1b6-db3d51767633 | -11.3735 | -43.4209 | 2026-09-28 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0c9fa245-2650-3e86-bed7-fb07a36bb7f5 | -11.0962 | -51.3231 | 2026-09-28 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fb52f9d4-bca1-3cc1-903a-5a4a06c94933 | -3.2137 | -51.0384 | 2026-09-28 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 15acbf47-a13b-316f-bdef-1cf775e93fa7 | -6.7059 | -45.6441 | 2026-09-28 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 72c57e7b-123a-3206-8be3-879f7102fbb1 | -6.6872 | -45.6456 | 2026-09-28 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 335.5 |
| e5a1bea7-9340-3c36-8c22-5c25aa5592eb | -8.2288 | -45.4829 | 2026-09-28 00:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a29ba6a6-eb3c-376e-8851-23207d4c9a8c | -10.4043 | -53.8236 | 2026-09-28 00:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| abf83d1d-4048-3061-ac4e-5ff16bab16e6 | -7.8626 | -61.1787 | 2026-09-28 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 448ebd3b-bdb8-3cb6-a6e7-372d2ef6c6a3 | -6.687 | -45.6682 | 2026-09-28 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 181869b2-6dd8-3103-872c-fba78942ae52 | -6.5977 | -47.1667 | 2026-09-28 00:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 48c0d934-752c-3db8-a658-d2ef8806a8a7 | -2.9082 | -54.1108 | 2026-09-28 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a5598425-a820-37ac-b2bd-8679efaec509 | -6.6874 | -45.6231 | 2026-09-28 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4388d7e0-e2a9-332c-86e9-a3113af6dbc1 | -8.0373 | -54.8926 | 2026-09-28 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e980e2ec-64fd-3b6e-ab87-7491ee6576ff | -2.7767 | -49.4765 | 2026-09-28 00:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 55b2fdcb-51c4-3c81-8cab-d99a2a905cc1 | -11.4425 | -44.9303 | 2026-09-28 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| ac9a0c2c-6af3-35d6-b2dd-74e75422f81c | -11.4429 | -44.9072 | 2026-09-28 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0d5e1348-8d6e-3739-a80c-f02d781a8691 | -3.1953 | -51.039 | 2026-09-28 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 47e57cdd-8685-3825-999b-4c1469b28e5d | -2.7766 | -49.4977 | 2026-09-28 00:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 18af5606-0924-3e89-b979-a8aca7763b13 | -9.9266 | -60.7171 | 2026-09-28 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b3f89c7b-dcc6-3975-87c9-a1987f8494f6 | -10.4232 | -53.8219 | 2026-09-28 00:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 233be80b-8b07-3d59-b154-96148fcdf878 | -2.998 | -54.7492 | 2026-09-28 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b5504a5d-d8d9-3084-ae1e-1807a80c38b8 | -6.7057 | -45.6667 | 2026-09-28 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9e0889e8-a627-3322-a077-d37cf33502a9 | -12.6293 | -47.315102 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8dcd22db-4cc8-3695-8281-7ad06e93d3c4 | -6.6636 | -55.113998 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb1276e6-627d-368f-81c5-2a5f11278571 | -1.8234 | -55.319199 | 2026-09-28 00:33:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26e41df-d1e8-3b53-841c-c4e2bd315e29 | -14.5128 | -48.310799 | 2026-09-28 00:33:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d1c227a-f7a7-34a6-9dba-2a737aa9053b | -10.9519 | -49.605801 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5135d31-5fbd-30f5-b55d-98470ab00dd7 | -2.7227 | -54.198299 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f915df92-72ec-3b22-81df-8be1cee58bc4 | -9.9718 | -50.168098 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51052de4-20ef-3538-998f-109d7b6607dd | -6.6522 | -55.109299 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad4c7049-b12c-33d3-b3ec-f6b6a4071120 | -3.3541 | -50.4655 | 2026-09-28 00:33:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e47f0aa-0a67-39e9-97f5-9ffc7698bd13 | -9.9792 | -50.155499 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe0c2f6-921d-3ada-8296-6ae9c066a73b | -11.3803 | -43.460602 | 2026-09-28 00:33:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb78c78-3f5e-3a04-85d2-222374d7b2be | -11.4349 | -44.914299 | 2026-09-28 00:33:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a1e992f-63dd-346c-a6a4-00c39bec47f0 | -11.1091 | -51.346001 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8169730d-be33-399d-b908-d2a9050583af | -11.3827 | -43.430901 | 2026-09-28 00:33:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efccedde-1561-3524-8d3c-c23578b92cab | -9.984 | -50.132702 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d48ed3d-5523-3823-8e72-0e226bf49df8 | 1.6739 | -55.939201 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3886f0a7-dee9-3bb4-af50-e89a8673f060 | -15.1534 | -43.633801 | 2026-09-28 00:33:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 5e900dea-79bb-3c37-9342-a9009cde1423 | -13.3453 | -51.322701 | 2026-09-28 00:33:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 686c720e-318f-3154-abf2-d12361b0089e | -8.2836 | -54.711102 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a360059c-9d1f-307a-9655-342aa9e2ef74 | -6.6967 | -45.680099 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c370993d-7930-3017-8730-9d438b251610 | -22.4583 | -48.597198 | 2026-09-28 00:33:00 | METOP-B | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e789b744-25a9-3614-b072-35a83944cf30 | -2.7834 | -57.695099 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0feaf95-fbc3-38b8-846b-f90d37d08ef3 | -28.752701 | -55.5975 | 2026-09-28 00:33:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| db02616d-53ec-3b24-b515-68cbf663fbb3 | -20.195499 | -48.584202 | 2026-09-28 00:33:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bfa6d980-4850-3254-909b-19268210b32e | -1.7691 | -53.7672 | 2026-09-28 00:33:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baf1c04d-282e-3ea2-b8ca-0709d2f43360 | -7.6756 | -54.848999 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f37281da-4ab8-3ff5-a345-76f452899f0c | -11.0648 | -49.474899 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea1aae13-75be-3284-9b2e-e9ab203cc586 | -2.8641 | -49.644299 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e67bbb7a-c977-38b2-9c2c-360d2a65887c | -10.1109 | -50.188099 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 245ea50c-c512-3536-acc6-e9e43d0d23d5 | -12.1573 | -50.3643 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83e3e29c-95b8-37dd-aa70-1b8dcfe1640a | -12.1933 | -50.384998 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd4141a9-9c76-36ac-8109-a63eeef07111 | -12.7263 | -47.289501 | 2026-09-28 00:33:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1da4a2b8-f6b8-306b-a127-3b01135ee3e1 | -10.4099 | -53.811798 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a39fca30-e168-34b0-ab85-ac839373f824 | -6.2731 | -55.4837 | 2026-09-28 00:33:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c15f39a-d01b-314e-99d7-7a4bd85774ba | -6.7044 | -45.6292 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7990b941-5a19-3acb-b040-0a88d9288b7e | -13.694 | -48.809601 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f46df41a-5548-3511-aa03-5669b064acac | -12.7299 | -47.303699 | 2026-09-28 00:33:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d040cf6c-45ae-33cc-9a84-ef3f004f8452 | -10.8243 | -57.215099 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3334f72f-7a56-3d92-b2e7-a8544c7b2547 | -13.5823 | -51.452702 | 2026-09-28 00:33:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78e016c8-bb92-35c3-a217-92ab9e89ebff | -12.8685 | -44.793499 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e31af6c3-4b89-3f3c-8fc0-be99765da5da | -20.1933 | -48.574799 | 2026-09-28 00:33:00 | METOP-B | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 20f6355c-21b5-38b9-8dc6-25c2d7ac31ef | -10.208 | -49.990398 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8652f9e-5f3a-32b6-a3ed-7cef5f753dd4 | -6.6852 | -45.634102 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d421d75-83da-35f2-add0-a2689b43c82d | -11.1815 | -44.772499 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25d1c8b4-9866-3d51-972f-3817610b018f | -14.5225 | -48.308201 | 2026-09-28 00:33:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
