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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 980c1d26-8a8a-3ff9-b1c5-fb1ca8e7af13 | -9.17639 | -62.2958 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3395bce-2f65-3b9b-ab38-4ce51631766a | -9.17411 | -61.57894 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 890d3206-a807-3284-9b88-b4e2324ce735 | -9.17095 | -61.57926 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c6e75ab-558e-30d8-8190-8f0a4b63fe43 | -9.17043 | -61.57832 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27606199-4908-3f84-86d6-05faf97acaf0 | -9.16826 | -61.56892 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ea0917b9-c471-343b-bb83-29a87740cbad | -9.168 | -61.57422 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b3e926dc-3db5-3314-9396-21e7ab7e5fea | -9.16751 | -61.5733 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 874dea60-a4fc-313e-a282-45b0a8062b61 | -9.16728 | -61.57862 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2e98aec-815e-3e42-9b57-a2b6424af383 | -9.16504 | -61.56922 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 47c2c5c5-df85-3a79-ae01-09c5814702a2 | -9.16459 | -61.56831 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7abd4084-2e9b-3965-be79-a6a717f1fcc4 | -9.16433 | -61.5736 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 87fb86fd-9780-3e00-b70e-41b7afa0fef0 | -9.18021 | -62.29644 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64ea1797-15b1-3a1e-bd4a-8efb4e76fdef | -9.17167 | -61.57485 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 12f64865-c3d7-3df8-b66b-636f67488267 | -9.17118 | -61.57393 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab98dd12-b570-3cad-915d-b47c6563d25d | -9.16872 | -61.56984 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| be3e25db-b1fd-33ec-9406-3d03b442d3a4 | -9.16677 | -61.57769 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f517e10-ad83-387e-9f0e-fc75e5c07a9d | -9.16384 | -61.57268 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e229c974-c1a8-3ac3-a674-0cf14d698be4 | -9.16309 | -61.57706 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87542b97-26a1-3e0e-9ba7-2ffcb5f3acfe | -9.0935 | -61.13747 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b395a745-d545-375d-92a3-699fd0793056 | -9.09059 | -61.13271 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e02109-5a32-3d3d-9a06-ac3ac2bb0900 | -9.08138 | -61.39212 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 087a39fa-b3d6-36b3-8244-4b5ffdb79cc7 | -8.74321 | -61.05661 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f94563-bb26-3aca-9ccc-3ff84c1e3ca8 | -8.99704 | -62.41911 | 2024-10-06 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1911847-5dc2-3d58-8476-f9c0fde8a4a0 | -8.84342 | -61.49257 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d0519d1-ecc2-33b9-9dc5-b44f3e9e75b6 | -8.83974 | -61.49195 | 2024-10-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f1e7045-c8c8-3107-8722-43d843b623ac | -8.37601 | -61.54798 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfd1650e-2b78-373b-bf1a-006895538967 | -8.37303 | -61.54295 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13d63e68-4003-39be-a46c-9d4e715e45d2 | -8.3723 | -61.54739 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9030f50-2941-3282-91be-1a51243621b8 | -8.22727 | -61.2202 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35d5aed2-e4bd-3b20-809e-7a2144b1afe9 | -8.22657 | -61.2245 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c61464c4-7ebd-3389-86b3-dcaa1334cffc | -8.22503 | -61.21099 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe11d7c7-3f0b-33f1-827d-9d07402a6500 | -8.22433 | -61.21529 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e310d88e-3cde-3c24-91e8-5c2f52994b96 | -8.22362 | -61.21959 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca5341b-1fc4-3b37-8ecf-e450981be682 | -8.22291 | -61.2239 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88f208c3-312b-3bcd-9558-1a2ad591fa99 | -8.22279 | -61.20181 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7098bed9-8494-34be-a580-46671ee86d86 | -8.22209 | -61.2061 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8751841-1233-3556-b322-1ed7a1ee8a8b | -8.22138 | -61.21039 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe409c3a-d41b-3237-bf14-61b4bf87ad37 | -8.22068 | -61.21468 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| affce2c8-b39d-3b2f-9f20-81f6f09d4133 | -8.21914 | -61.20121 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a37aff6-1758-3cb0-85ec-c6fc2f2ef0a2 | -8.21844 | -61.2055 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad9a193e-4ac1-3286-87a6-6ccd75e02509 | -8.21774 | -61.20979 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0079d553-9f28-3e48-92f5-d50f2dc56903 | -8.2155 | -61.20062 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a296801-8e74-3588-9b08-95eb725b1fce | -8.21479 | -61.2049 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 343c8027-cc34-3834-960a-8fdd24df9a9a | -8.21409 | -61.20919 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe2128a8-be05-3bb1-b302-fc1a1f36e705 | -8.21185 | -61.20002 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31e6d6a1-ac7c-3a62-86db-010ff6ba3069 | -8.21115 | -61.20431 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a649e2d-c0d1-399a-8d49-ed7bde1b5256 | -8.21044 | -61.20859 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7f73f38-d6e2-36d0-b48f-c948430c047a | -8.20821 | -61.19942 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aceb5010-7904-318b-9c44-0e474d76db77 | -8.2075 | -61.20372 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b04c035d-4a81-364a-9372-d81975f89acf | -8.14713 | -61.27326 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af876bec-82f7-3cd2-a332-b03d7d1f5b58 | -8.13174 | -61.34241 | 2024-10-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b7a834a-7a94-3e79-960c-60f998552113 | -8.09441 | -61.27508 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 330f05f2-1285-3dc0-b9d1-fb14a6622c44 | -9.69929 | -62.17266 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 970b41f1-6c25-3db7-b031-9d432118681c | -9.69552 | -62.17199 | 2024-10-06 05:12:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83469a94-bc92-338c-97c2-9638ece23b63 | -10.93664 | -62.56279 | 2024-10-06 05:12:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aefe348e-993d-318c-887d-a241ad8d3f5c | -6.4468 | -62.86512 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd3ac33-dfd0-376d-9d78-3191bee7cf41 | -6.44513 | -62.86446 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 303c74be-40c5-3e4c-908c-2ca1c14aca97 | -6.44447 | -62.86828 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd2982ff-0939-3d66-93d8-7f41b9c10e81 | -6.44265 | -62.86448 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 716aefdb-755d-3716-a7a2-32e99676d5e9 | -6.44203 | -62.86827 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce6bff4c-58cc-3320-9e4d-964ba0b0a03b | -6.25786 | -62.46429 | 2024-10-06 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a2ad0c-9bd6-3be6-8699-83f2e929a5aa | -7.52433 | -63.26268 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2962216-699d-3c4f-af4e-8d43d13b857b | -7.5043 | -63.35498 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03f9f97c-f420-3e88-a27e-d942db7da158 | -7.50364 | -63.35889 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8943548-df11-3999-b3f2-6d5d64effa62 | -7.47887 | -63.79025 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 260d136d-d065-33a6-8aa8-174cca7bf97b | -6.985 | -62.91258 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08eebb4d-1f7d-39c1-b80e-c8a34b259956 | -6.98229 | -62.91136 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42922aea-2da5-38c7-b37b-3a01e1fee9ca | -6.98167 | -62.91508 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbccb860-3149-3a51-996c-86443628e17e | -6.98106 | -62.91881 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36fed701-26d4-367e-84de-0c28fca3569d | -6.98089 | -62.9119 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f01e68f9-4304-37eb-86d6-e1605b355b5a | -6.98025 | -62.91561 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 030f7b01-2d09-3f5b-b425-a0265a15d191 | -6.9796 | -62.91933 | 2024-10-06 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 237c6deb-ffd6-3269-96ee-34cc42523c2e | -8.78953 | -63.22673 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6feae11d-3c5d-3fbc-b11f-9c4b955fc12e | -8.77622 | -64.14948 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89b430a5-1efb-3013-a413-6c1d06f507ba | -8.58161 | -63.09665 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a50aad1-b9fd-33df-b5d7-823667e8e930 | -8.50407 | -64.01862 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e202ad1-07ca-3a59-a562-548c574455b3 | -8.49184 | -64.06385 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c7b1afd-979e-3cbf-a537-76d89140c5a0 | -8.48751 | -64.0631 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4d1f3ad-2c78-3996-b46e-fdb9df7c2b55 | -8.48317 | -64.06236 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 195b6395-3c7c-3abd-8e07-b2e45c58af0c | -8.33427 | -64.01089 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bdb0305-45d1-3da9-82d6-e47afba4a6e6 | -8.3328 | -64.01926 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b0aaf72-c8af-3c63-b5aa-7599969db5ce | -8.32177 | -64.02283 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b72f022c-e385-31ef-9104-c3573859189a | -8.31906 | -64.02122 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dee189dd-6f89-31e1-919c-bd57055e69d6 | -8.31833 | -64.02539 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dee1cc95-d965-3825-8402-589f7abdb80c | -8.31743 | -64.02208 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9bac8823-589d-34b0-b14a-91d9162baeb5 | -8.31672 | -64.02628 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4581f1af-2ca8-3d34-930f-78eacd94ab7f | -8.31473 | -64.02046 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e261b81-cc34-3ff6-97b6-61301472129e | -8.31399 | -64.02465 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| efa208f6-d1c6-333e-b6b4-7a10cbe57d36 | -8.3131 | -64.02132 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47b05ef4-7697-3367-b308-86cb8cd5444c | -8.31239 | -64.02552 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c5a2723-b524-33b3-8b9e-90b9e2fe4f29 | -8.26538 | -64.03911 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57df1ddd-f913-3cd3-b75e-e546d0eb1eca | -9.31346 | -63.2469 | 2024-10-06 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ef4f51b-8484-3383-ae0b-bd3c93e02f06 | -8.83217 | -63.02945 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c425ce-335b-3ad4-9b9d-1cdfcc321944 | -8.78545 | -63.22603 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8d0609a-9b0d-30d3-82f4-df9528906c29 | -8.58232 | -63.09395 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9dcf0d4-8df7-345d-b1e9-50b41b152bda | -8.58169 | -63.09757 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e63d2797-c750-3e8a-bd9d-9401c8bb71bd | -8.57755 | -63.09597 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd7efab2-cd43-3905-a703-54a6dc34eaf7 | -9.37991 | -63.70774 | 2024-10-06 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b297c9e-ebdb-302e-b283-7fa74ea6e798 | -9.63557 | -63.14888 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1062c40a-f359-3c96-98f6-1a83518f7d2f | -9.61518 | -64.05234 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README112.md)
