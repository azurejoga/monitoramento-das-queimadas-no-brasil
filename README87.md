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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d047f6-078b-3ba1-ba0d-006457504edd | -3.7587 | -49.80745 | 2024-12-01 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56e4af19-db37-3d89-84fd-e4cb9c14ddd8 | -3.99766 | -44.75666 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 53cee24e-66f7-301d-86b9-d5bd535ebccd | -1.96569 | -54.13176 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81841f3d-2426-314c-a6b8-807aee826e05 | -2.56355 | -53.9597 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a51d510a-d684-396d-9eb5-780da2e0bff3 | -3.31542 | -53.86893 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae020f96-987b-3d79-b7b0-0c8d0dcf7073 | -2.97518 | -53.86834 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152304b8-4b4b-3328-a96b-60abdfee2afb | -2.25651 | -53.62754 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c049ba2e-db2d-33b7-b1b4-58e427854206 | -3.48916 | -54.03097 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b12b4fee-322e-31c5-bb63-be5aaea7eda2 | -3.11758 | -53.27456 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 228fe0fa-f935-317b-8a9c-de8e8b7ecb3f | -1.5057 | -52.57162 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 578ef256-9443-35a6-a637-8e3df04ce685 | -2.63455 | -46.88386 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3eb982f-a4c2-3855-a540-f9171970d5ac | -3.0651 | -53.22439 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e599e8da-5ddc-3df0-b085-7b6140ea6e33 | -3.06456 | -53.69014 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f36ca38-29a3-312a-bf82-ba41a067d5fe | -1.57548 | -53.83458 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e6ca8eb-855d-37da-ae09-689039d0adfb | -3.21668 | -54.22479 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b7e7777-4125-378b-ba4f-5f0b483b0101 | -1.54116 | -55.94378 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db86d52a-dc89-3c90-aecd-7f647f04ccea | -2.79677 | -54.13195 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24dc1e28-6eed-39ad-8fed-67838dc70867 | -2.96089 | -53.72844 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 414a20e5-fb06-36d4-8121-20f5250a5cbd | -3.81607 | -52.08655 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3d8ac4a3-7217-3601-aca5-5430f20e3283 | -1.76017 | -55.65323 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c379edd1-062d-3603-96bd-ad506dcf549c | -1.9379 | -53.4429 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04c8185c-1956-3478-9c0a-c2a88f00ff97 | -3.31188 | -53.8684 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0850b5a4-ce59-3162-927e-74a3bac512aa | -2.82717 | -52.59094 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 014d643d-79a3-3c7c-942b-cbcd61286ad1 | -2.12632 | -50.63487 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a507ef5-2558-30bf-b5b3-15a54e8c616c | -3.05857 | -54.05223 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796be182-5c0d-30e8-9617-229d4db0e5a7 | -3.30884 | -53.86483 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe6243ab-13f8-3a06-8ac9-75a7e0b2f389 | -3.1705 | -53.63535 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbaa99ff-28b5-3b87-ac97-17f08cf58283 | -3.3815 | -49.85807 | 2024-12-01 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb74f5fc-cc63-3195-bca9-89ed326bc960 | -1.75135 | -52.65432 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ef64212-0e66-3d94-9578-6e1b54694659 | -2.91343 | -51.72123 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0aa89c9-a169-3cc7-bd02-11865f158f68 | -3.54027 | -50.18333 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2b0c16b-46c3-3b39-9922-113933040250 | -2.83753 | -54.09901 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c034633-877e-3d23-b991-5d308c58f647 | -2.60474 | -54.28123 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d7c7452-8695-314c-9a64-40a53017674c | -3.58006 | -54.52224 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4801e17-3161-3d25-b40e-09917389a08e | -4.10501 | -50.98512 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1353a1a6-48d5-3f6f-8252-0c6260db375f | -6.29004 | -43.85668 | 2024-12-01 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec3bd7e-2eb2-3e00-b2dc-ba3a299f9f5b | -2.4154 | -54.00783 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72212712-6efc-3f70-937c-55352b729f9f | -2.44113 | -54.14053 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdc23cba-e89a-3179-b63b-ef1f8faa040e | -2.86398 | -53.98321 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c885422-109c-35a2-a67d-9dbc40d06e8e | -1.57488 | -53.83839 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9266807e-52a4-310d-b56f-d4bdbda357e7 | -1.44278 | -55.2305 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3703cfbf-9b24-3b69-82e0-8846caeb521d | -2.55421 | -54.33908 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a0ec9e1-310b-3ebc-b47b-2d396285abba | -3.11194 | -53.99203 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e73ebd1-3510-3489-aab7-b09c656d17fe | -2.77556 | -55.35032 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dad0cbd-d8f3-3ef0-ac01-edb7270da4c5 | -3.00753 | -53.21155 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5959cc2a-cfff-3bb1-91ae-79cad6500ff6 | -3.50559 | -53.78646 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03d33f51-569e-3980-8076-cd611c90521c | -4.07086 | -48.8031 | 2024-12-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbdd69fc-3eea-3d3b-a6d1-98375e58a2b9 | -2.85215 | -54.06052 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52bcbefa-6d8e-3815-bd35-6f68ee942ad8 | -3.99021 | -47.91651 | 2024-12-01 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d56eda0e-a4db-399f-9bb6-981af25486fc | -3.0898 | -53.71489 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62974c4a-bb16-36c3-8524-29a9ff117c75 | -1.70495 | -52.43965 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac39334a-b2b5-3c6d-8663-62d73c9f1972 | -1.26673 | -54.55041 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5689f5a7-43ed-3c58-8f97-3c3ab05b40c1 | -4.04073 | -46.93303 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e763e1af-0a77-3405-863a-4dc1365de3f5 | -3.25402 | -53.28534 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a2635d-31e1-3b3d-a33b-e5e403eaf84c | -2.58848 | -53.98327 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffc22534-8f27-3418-9502-8654c8fdf5e6 | -2.63479 | -54.22387 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2068cbdc-ccb3-362c-b008-2ee6213274c5 | -3.41984 | -50.18291 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6fd9a5b5-5065-3b9e-bd85-234593f9234e | -3.4912 | -53.80892 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16ffc61-8ec9-3408-938b-c5aa58bf845a | -2.79695 | -53.04808 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 980a8001-f810-310f-9cf0-ac9d8abeb32c | -2.88898 | -54.00691 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bfedd81-61b0-3856-8be3-70e496ea5362 | -3.7246 | -51.10448 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2478393-7bbb-3cc7-94d1-a1aff677d3ed | -1.98251 | -52.89658 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43937f16-6eac-3ac8-a247-5da8d03ddd7b | -3.3398 | -53.28842 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64025982-2a50-39be-9cbf-09391774e41b | -3.25272 | -53.29368 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2789e52-cc50-306e-b322-71242a68444a | -3.26133 | -53.6321 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fd3dd2c8-9c9f-304b-b7fc-3e057b702f43 | -4.44546 | -45.36692 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd626cc3-6e78-3485-ad7e-0e4cb50a1384 | -4.07792 | -54.56101 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94e9f20d-e95c-3cae-a358-235fcbc8fb1f | -1.49352 | -52.64979 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a60e1ed9-7734-397f-bac5-6a924ebbc2eb | -1.67095 | -52.49979 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed85f80e-29f1-3872-8304-bdc6e67531ee | -1.72222 | -52.6231 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 96f94a1a-2e8b-3e55-a44f-fd924169019a | -2.81801 | -54.48861 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96594395-7f5b-3c0b-a00b-87d4ecafd6bb | -4.55304 | -43.30237 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1acc1c69-512e-3ae9-b437-837069f2f7d5 | -1.69734 | -52.63715 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14892b40-207a-30e2-a8f8-56401bdab1c5 | -3.30858 | -50.50376 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8bb35be-4b02-3764-abeb-b4055409a4b2 | -1.99021 | -53.28814 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46c25001-5ed4-36d5-b181-886d45af670e | -2.96212 | -53.72049 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f65e016-c48f-345d-b0de-6cd9a03a412f | -1.64321 | -53.86771 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c52a2147-985f-3035-a2a6-a1b82d3d2c58 | -2.46139 | -53.96384 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5920537f-3d92-316a-859f-fce664e1eeaa | -2.43787 | -53.62524 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08c4b32c-8ec2-3a49-a2e1-c0689d2c0edb | -1.55714 | -53.51766 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02fa2e90-fefb-32d1-9bd2-4ede1680ad70 | -4.11155 | -54.41051 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5635ea55-99f5-32ca-b34c-6f97dd7ada07 | -4.55207 | -43.3091 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 1fb4b5e9-e720-32bb-bbd5-bd21ad923580 | -3.3213 | -54.18094 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e71ce859-8f27-3213-9d9f-d0718efba586 | -4.53478 | -45.70278 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70e7aa3a-d12e-3827-8073-2eca28a4d246 | -3.09076 | -50.35973 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b458193d-5f51-369d-8ab0-57920407bbc3 | -3.71141 | -51.07212 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8b74948-0940-31ed-997b-6daf3ddd45cc | -1.62163 | -53.89203 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a300e76-15e0-36cd-b90a-ee0e161d19bc | -1.82093 | -60.06626 | 2024-12-01 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8ec198-fb73-35d5-84c5-668ee1bc166f | -2.90176 | -54.01679 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 662966b8-7445-32ba-90e7-2c7adc66b2cd | -2.9298 | -51.4495 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67d7f352-bc21-3dcf-add4-cf456a2a6474 | -3.3452 | -50.74734 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82f69e06-442a-3a1e-8d9f-b4213b2f4cd6 | -1.71852 | -52.62253 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d2a35ec8-5b10-3a09-8f0c-567232be6bb6 | -3.48977 | -54.02704 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8aa144c-9d0a-38c9-bdf8-384d6565180b | -2.60674 | -51.81305 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40f75458-6f61-3224-8b30-7aaa5189bba0 | -4.55054 | -45.72341 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10dd192f-6058-38eb-8b4c-71675b0a5d04 | -1.32879 | -55.847 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef28bb4a-ac1b-3362-a406-8c65c1f6cd69 | -3.33617 | -53.28785 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4588d973-7531-33a8-a5d6-8d9b2214cef3 | -3.14252 | -45.36725 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecd32bff-740e-3614-9c90-f8cc0fb82032 | -2.62558 | -54.21477 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae911f7f-aa33-37f3-9f48-3a0b3556a506 | -3.1634 | -53.24279 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README88.md)
