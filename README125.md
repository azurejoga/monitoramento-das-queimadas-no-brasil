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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c39edbb0-73c2-3b1e-9407-e05405c31a63 | 1.82435 | -55.52734 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 463586fa-fb2d-3dad-ac7e-a107d4e13cbd | 1.70323 | -55.59931 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b925e072-6669-3f7d-9fa9-3db3a17744d9 | -3.20545 | -50.55811 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae967bf4-04c9-342d-889a-1d1e6e6492c7 | -2.47098 | -56.09283 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e1bd5b8-532f-3da5-bad6-75ac615795e1 | -1.10895 | -54.17301 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f6fab64f-3014-3264-8485-21f2f9062119 | -2.73548 | -54.10569 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3d0cb53-1702-33ee-b9a5-1e9b8fa850c7 | -3.21761 | -42.96475 | 2026-10-09 05:01:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0472fbd6-e124-3de7-ac2d-b4d7f5c31285 | -1.44984 | -54.46938 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 201e97a8-7599-393c-a5ef-9ebbc56e5f26 | 0.78751 | -59.20094 | 2026-10-09 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01bcec4b-4143-30c3-b393-0ec2df260f61 | 1.78021 | -55.53429 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3be638c-dfcf-34f6-a147-39ca69e28ed0 | -3.35368 | -50.41587 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1c392aa-9c47-3866-a7f4-79efb436dee4 | -1.48294 | -54.51732 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 106fa8c0-b925-346f-bb2c-78b1ca280fd2 | 1.69276 | -55.61163 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71486aac-11ac-3a93-b9fc-a5dcd3d6e371 | -1.47096 | -54.75732 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 510fe6b9-a956-36a5-9d46-af32a75f493a | -2.7837 | -54.07372 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a54757e-a5ce-3a0e-b376-78dd733a2415 | -2.13568 | -54.47078 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34630633-cae6-3eb6-acb3-853a946a1047 | -3.17108 | -50.44656 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d963d240-90d6-3ee3-85a3-bb7557b58624 | 1.21896 | -59.97456 | 2026-10-09 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d343f41-ccee-34b7-a6f2-65b993164485 | -3.35417 | -50.47846 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0953df0b-3aae-3702-950c-0b9cd2bb63bc | -2.2666 | -48.06015 | 2026-10-09 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 999903a5-0a31-3c51-b8c9-ff4bc0071779 | -3.35425 | -50.41227 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d8d7fe5-e904-3271-8fa5-a5cd0eb1f791 | -2.73961 | -54.10237 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1f56eca-cb91-3f1b-82fc-d5b1d6281fa2 | -2.7345 | -51.54761 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b3b7008-77f4-3195-b45e-8e15717437f3 | -2.16701 | -53.66732 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbec4377-b70b-3cc7-8898-2b74517cdecf | -2.8308 | -54.13974 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab4f02df-288e-32a1-a981-6362c10f24d2 | -3.27011 | -50.39545 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d94d222-657b-3790-b5d5-95832533a13f | -2.76765 | -54.10688 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f62ce7b3-f72f-37d5-9a5e-5aba64489fca | -2.7365 | -54.12176 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf5efb0-f6ec-31ec-8e71-727fe404d27c | -2.33818 | -48.87271 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| afa95883-31f2-3798-be55-af9fec64daf6 | -3.17735 | -50.58291 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d82c2301-5539-33ab-a482-b047cfd122d9 | -3.18129 | -50.57988 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 175e9f1f-d051-3551-819f-8b9a67fe0525 | -2.73775 | -54.11399 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 387c289e-b60e-3326-8f5d-9a069f03b6b6 | -2.83682 | -49.5109 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0377e7c-778a-36d0-a717-8556d1afd606 | -3.3598 | -50.48669 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32d97c58-fdad-371b-bb56-d5aaf46dd4c3 | -1.41951 | -55.71674 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e238a6-f85e-34e9-ad5c-1e17c0c56e0d | -2.50914 | -56.15451 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ef7d4d9-ae80-39aa-9167-db30b5fd19b7 | 2.32851 | -50.8746 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e0ba4d5-3528-36e3-8d86-15fc03942ae3 | -3.35538 | -50.40506 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff81309b-ad05-382d-80f2-b50534adba8a | -2.94543 | -51.41102 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d928648-5853-32ac-89a6-30b35ddafba5 | -4.09066 | -45.90343 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b23166f1-5b94-3f4f-9550-1a728850d1e6 | -2.74063 | -54.11844 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d230017-14c5-31e4-981b-24cf5ec87994 | -1.41774 | -54.62162 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbeaf626-ae37-360d-a097-9a8b56a07faf | 1.69222 | -55.60814 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca88d82d-200c-3d1c-9b0a-01b3a624d154 | -3.27558 | -50.02411 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a184528b-8722-328d-a592-8cb225016b32 | -3.20994 | -50.55151 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5a4b748-8113-3071-a329-36b29704c2e2 | -3.352 | -50.40453 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3592012f-87e3-3489-9cc4-9c71c5f67f6a | -3.20095 | -50.5647 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df4a00c6-ebad-3af8-ba37-46a42ff31a8b | -3.16838 | -50.59609 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c609587-c816-3643-98ac-6b7d8ed58ca5 | -3.25909 | -50.39411 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d988c79a-4446-37d9-83bd-f11b396a8748 | -3.48174 | -50.0889 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a92ee30-b3f5-342c-9761-65d980565eba | -3.0935 | -51.37379 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ea4fdab-e1ac-3c56-b577-ddb787bee613 | -1.31908 | -55.44531 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 320c58f3-84a6-3b93-a26e-308c7df742ff | -2.32619 | -48.49322 | 2026-10-09 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b440e4c8-13ef-352a-9874-6a94935c40fe | -1.29185 | -55.71391 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fb2bad1-5575-3014-9fad-efec99d7cfe6 | -1.43407 | -55.25917 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cec53b6-1c57-35d8-bbf3-467ba0ad911c | -1.36249 | -48.48096 | 2026-10-09 05:01:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b149302-665b-3a84-ab7a-130f33dfc334 | -3.36261 | -50.4908 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a67ef9b-317b-3867-b74f-50331acea0d3 | -2.49957 | -56.18859 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa65318b-aaa4-36bb-941c-49749ddb46e8 | -2.74786 | -54.09574 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d135f42e-96ac-30cf-81f7-fa6087ae8a76 | -1.14909 | -54.22078 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80a00c82-3bb2-3582-bfe7-d02dcbc28c6c | -2.76415 | -54.10631 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c190d4ed-65bf-348a-9ffd-080acfb81a26 | -2.82987 | -49.50982 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa4447b6-f181-35fe-aa0f-380df1afae8c | -3.20175 | -50.83296 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73881d85-f16d-356b-a009-c916c43d863a | -1.10244 | -54.1678 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4029e780-34bf-3a53-bdfe-1ed262629493 | -3.48231 | -50.08522 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9ff459d-d5d2-3365-8e8e-7180f4ab63e0 | -2.82015 | -54.09435 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b303736-700d-3a41-a3ab-906a8fb0bf23 | 3.73108 | -51.64954 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33a1864e-9e0e-362b-b9b0-91b0c69beebd | -1.18393 | -54.17524 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b673a20-58ca-34e4-85bf-2cbafaa7031b | -2.50919 | -56.12934 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ece182ea-8d1b-395f-a0bc-dccf7532210b | -1.1073 | -54.16033 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c34645e1-6d1d-379b-8c98-ea6a7bd8fd4d | -3.20657 | -50.55098 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2849ab2b-edf0-3904-a71d-f0050ed997ad | -2.46787 | -56.08732 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69383173-8c02-3afd-95c2-1f47137e4361 | -3.35361 | -50.48204 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f22d2b0-d0c8-3cbc-8532-b5f158a91990 | -3.3694 | -50.47308 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 945ad1fc-ee0a-3bd4-99b3-9bb5b742ba04 | -2.50362 | -56.16369 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69eb590a-5254-3120-805e-d1e4cdfb5be9 | -3.25513 | -50.39719 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6944f50f-4ae6-36fa-80e9-8d8318ba48f1 | -3.34972 | -50.41894 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c981603-c4ba-39e1-9b69-fc83a7523f21 | -2.95611 | -51.49424 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46da13a3-ed97-3e38-afa1-e2244a1125da | -0.66866 | -50.76991 | 2026-10-09 05:01:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77d93342-b117-37d8-a2cb-d2c1423669b7 | -3.16657 | -50.45324 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c346ff93-7089-3323-bd17-3b6e67ee2ec0 | -3.28726 | -49.51159 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46917224-48d9-3912-91ee-2c736eabacbf | 2.41282 | -50.82597 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cebd3bb-5643-360e-b982-c6c791ce18fe | -3.36545 | -50.47288 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d2facf-6964-3afe-b5e0-0f8d47539f3d | -2.84732 | -54.12647 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46252f3-d6ef-3e41-af8b-f4c2ea4bf4c5 | -2.78422 | -51.67911 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247ac49a-b7b8-3c67-8277-367d4421692d | -2.51072 | -56.14471 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 007ec0ac-31ef-3276-9ff4-4e55ae5b74e3 | -1.3998 | -57.93369 | 2026-10-09 05:01:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0dff90f7-c9da-3684-b968-0ff4f6f35409 | -2.74312 | -54.10293 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3b783da-e3e6-3fad-b69d-b3601a1c8caf | -2.22333 | -58.11057 | 2026-10-09 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcf17704-c669-3dc9-9767-cddda5a71372 | -3.14486 | -51.62641 | 2026-10-09 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19c2652d-a668-36b7-9ba8-a9368393a760 | -2.8432 | -54.12978 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0536f96e-c568-3915-9acd-e94275b16d75 | -1.52772 | -54.566 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b8585d4-a94f-3ce0-b082-e9bb9bae7ca1 | 0.92861 | -50.2558 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c7cbcf0-dcad-3a44-a585-1bb116d5ec85 | -2.85247 | -54.13921 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e34c8930-c6de-3640-9c86-1c043ba0e617 | -1.29106 | -55.69393 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 565ca5c3-5265-3b5f-ac0c-002944ab3826 | -3.19645 | -50.5494 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31837fc7-487b-3266-b9d1-ec16a723d9c9 | -3.01087 | -51.01902 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd10ee88-718f-3139-8191-2d0e7fb5f96b | -2.95818 | -49.17294 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8132a893-6a29-3a7f-9a70-e8371f312c46 | -3.10686 | -51.03025 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 433e170e-efe2-3252-b206-9f849fe0540d | -4.35799 | -44.35716 | 2026-10-09 05:01:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README126.md)
