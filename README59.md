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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcb43967-9b0e-3d64-845f-8fe213bafdb1 | -12.57501 | -57.80128 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1f0ab00c-4720-35ae-85a6-8f835807c8b9 | -2.66123 | -54.08764 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31130996-4d46-34d8-8ed1-37faafbd8725 | -3.21391 | -53.12613 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24585242-46c7-3319-b3fd-29ef5b940ef9 | -1.7489 | -52.78605 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad2896d0-2d67-36c0-a2c6-d27c31d037cb | -3.10377 | -53.23175 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bf7983c-8f33-3aff-a868-0e7ff0f6aef4 | -3.85224 | -46.52297 | 2024-12-03 05:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a45704bd-4c89-37ec-931a-82a8161dc15c | -3.12191 | -53.979 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f057169-d33c-30ba-840f-e8e7db8f151d | -3.26464 | -53.62424 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9909dd28-98ef-3344-8c3a-a29f275c7ef2 | -2.7559 | -55.3404 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9f1e269-4c67-37c8-88d5-9aa50ad36c9d | -3.2582 | -53.63669 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68851cb1-e638-3570-a1c9-dd65b0ee505a | -2.77955 | -55.36943 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4265f04-3bab-377b-9970-cc2919978a1d | -7.66032 | -61.50467 | 2024-12-03 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34718c2f-8174-3579-a776-169c6ee531bf | -2.33074 | -53.81018 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d89cd91d-8637-3840-8dec-6be5275a565b | -2.86407 | -53.32575 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe0501a-6bcc-3659-a336-586d1ef71cca | -2.23559 | -53.69582 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e77ce5d3-abf0-3956-ae3d-8f89a099efbc | -3.1822 | -54.33406 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 435ef179-f810-35b9-93bc-d73530348111 | -2.80126 | -53.06043 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31a490d9-192a-3d33-b389-49c7af360fe4 | -3.25489 | -53.65838 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a368f2e7-9d45-3f43-bfe5-ac1d3f6c4fc1 | -2.45748 | -53.71788 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b1dd664-c249-304a-a4af-ad02b9c94947 | -2.66992 | -57.05439 | 2024-12-03 05:25:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a15d9482-8c3f-3af6-8a45-4fee5a3c37d2 | -2.96878 | -53.88229 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07f235ef-92fd-340b-b8bd-090f3e9fbe74 | -3.26555 | -53.64391 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f94987d2-847b-3fb4-af7e-cf201ea4a296 | -1.74627 | -52.649 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a269ed0-cf1b-351f-a8f9-94dcd1773412 | -1.61847 | -52.68544 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 118c696b-8a82-3e0f-9b03-f4a1daa5cac2 | -2.4666 | -54.11199 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77ba180f-a8fe-35dd-b60e-0f350e03439f | -2.78578 | -55.35506 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78f0b15-7e39-3e51-b1c0-2737aa5b7290 | -2.7627 | -54.13121 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 291b0755-0ba7-3d54-84ef-d69d019a35f2 | -2.81329 | -53.04312 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c2beef36-dd75-36d7-a73c-f64d523a6006 | -3.05766 | -54.50187 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d66090c8-e4ad-395e-ac93-03770171bd04 | -3.35085 | -51.21218 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22d68dee-619e-3871-b51e-43fe1a8acbf2 | -3.35038 | -51.21538 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84f81e6b-5c1f-3d5e-a9a5-3b8711ed010e | -2.89191 | -54.16112 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 897f0220-799c-3728-8e07-8b1dd01154d0 | -3.28764 | -53.70926 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19de7022-7695-37de-a135-fbe8825ca008 | -1.702 | -52.60498 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71fc0f86-bf63-3c50-babd-b03fa6963e8b | -3.07027 | -53.26889 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7329c745-4b5f-34a5-b5e3-272279dacba6 | -2.80656 | -53.05648 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83f8dc00-d709-30f3-a351-b54284ef20b3 | -2.81571 | -53.05791 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 203ca309-90cd-32f1-999e-fa3ca6d6e8da | -1.46824 | -52.68468 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16ada5fb-531d-3071-80c5-d5a05deb2326 | -1.76048 | -52.80232 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13faf0b9-c0ea-32fa-9e74-c0477d66a7c3 | -2.84373 | -54.11053 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a93c4f2-ce2e-313f-969e-250487ec1e64 | -10.44276 | -59.43587 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b64dd7-cf4b-3566-9e8e-0f6ddc2fe520 | -2.78959 | -55.35703 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a96b0fb-3a6f-3a18-9c75-5cb00b2bb6b7 | -3.2613 | -53.64606 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18986a62-520d-3f59-833f-0127174ec089 | -2.07975 | -53.47575 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66029e88-acff-3ef6-8d9d-c8cfbd27f66a | -1.70743 | -52.62315 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebbd6aa-9e2c-3320-83cd-7f7561e03531 | -4.16773 | -48.59735 | 2024-12-03 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 617a567e-d345-3ce0-bf20-aaf5ceb9b4aa | -2.80948 | -54.04786 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c91d6869-cc02-33e1-ba57-f6273fbafd83 | -1.69919 | -52.64657 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d2291d9-8b22-3fb8-ba0f-ea9771954f3a | -1.69207 | -52.63063 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3131d0-d74f-3127-81cc-569475f3a559 | -1.11176 | -54.18682 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949a3f3c-fb9d-3caf-804f-a0ba5ecb2638 | -1.94663 | -53.34255 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43f1c762-5dd8-3a90-9e98-3faa7bb7dca2 | -2.9824 | -53.88026 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e2b8d4e-d10f-3fe9-b677-f5b52992aaa0 | -2.37964 | -53.66465 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16a312fc-1f72-3665-aeaa-75cd13cb2ebc | -1.71245 | -52.44593 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c522de7-ebc6-3007-85f3-4590ffb8df30 | -3.41982 | -54.0243 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd29fbc3-495a-3550-9d75-c9b7b4005226 | -3.08102 | -53.91457 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d4b82b8-78db-3ca8-ba01-7cd5ae0daf5f | -1.27603 | -54.54941 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b457b7ea-6e01-3c02-9477-644b4aeaccda | -2.7726 | -54.11983 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70b73141-cdd6-32e5-9ad3-8f79c90c9d7f | -2.66066 | -54.08596 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43986482-7e13-3c51-917a-82de468ea76e | -3.31325 | -53.36643 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 334c4b2c-b6c9-36f1-b8d0-90db3fdd1d5f | -1.36449 | -53.64569 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 458093f9-81b7-3fcc-852d-5f5923610ca7 | -1.4718 | -52.78662 | 2024-12-03 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cfb1590-00ef-386c-b662-379e0c8a59af | -10.45518 | -58.68082 | 2024-12-03 05:25:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53e5d3b8-277b-3889-8412-2190cb744c9e | -2.47085 | -54.11262 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ef56ad2-0701-3f72-904a-c593a54b4b07 | -1.78695 | -52.74988 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6782774d-6ab2-3c2f-b11b-7018b3758919 | -2.79042 | -51.71714 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee39e07e-fa81-3235-83bb-f70c1f4e7f6e | -10.45936 | -58.67723 | 2024-12-03 05:25:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9142aaa2-5904-35e3-9b84-c81928919ee3 | -3.07606 | -53.91805 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3f05fb0-57f0-38a3-a904-25597efa55b2 | -3.25243 | -54.21233 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b765601-b746-3d54-b22a-6aa45ebb2af1 | -1.69897 | -52.6243 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb45bae6-d5d3-3390-9e7c-6b137d087efa | -2.6731 | -52.45444 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef5ed10d-1b48-38ab-985e-0c876b0c45ca | -2.7864 | -55.35148 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 030cd146-179a-3042-9218-eac4d9bfe22d | -10.05256 | -59.1131 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 021e5caa-4bac-340d-b959-7a6d82804f53 | -12.56979 | -57.81052 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ecfe1bbf-dd7e-3cb6-828f-c347ecd58466 | -3.25931 | -53.65906 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f4839b35-178f-3892-a2ff-1e9ecdf45899 | -3.3456 | -51.21136 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdbdd240-e88e-3c61-8600-5e780f409e9f | -2.64261 | -54.20868 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a363107-6a6b-3c4f-9395-c7464c170df8 | -10.05548 | -59.11755 | 2024-12-03 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f6f9d6a-a56a-3ee5-9d9e-d2395b3ff9f8 | -3.2467 | -53.6527 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5722143b-1b5f-3303-b993-95d76fa41bfb | -1.52208 | -59.99443 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20a37439-3512-3fc7-95b7-9187d1a73c2b | -3.2633 | -53.63301 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7163de4-c63c-3335-b389-8073fbb8862a | -2.80871 | -53.0424 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b6037948-c6e8-3a1e-aefc-694e0a20b24e | -2.64226 | -54.21009 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b93e184f-8d75-3262-8f9a-f84b4e89036c | -2.45202 | -53.66557 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32ff816b-fb29-3f06-a30f-baaea684d972 | -3.37364 | -50.70322 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a35eb5c-8f1e-3558-a4ec-24d628aa4e79 | -3.08083 | -53.382 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 063077e0-e88d-3aad-8288-3d1a36284bce | -3.26492 | -53.64829 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b335c089-95d4-3831-86a0-d15106305347 | -2.44513 | -54.0284 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b834e09b-cd4b-39b1-895b-fb10528ad3a0 | -2.83702 | -54.09724 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0328c61-d5af-371d-b508-f2a65ca0c97a | -3.07473 | -51.26707 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da162285-3f19-35b1-9d9e-c74da633b166 | -3.26745 | -53.63083 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f151594-76b1-3164-b95c-42653d3815d6 | -2.67389 | -52.45155 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65d3f794-e680-3300-a104-9865f16f64c6 | -12.57047 | -57.80563 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c8ff7ba-d132-3c41-8c3f-d4b8808a7ace | -10.45876 | -58.68137 | 2024-12-03 05:25:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba3ce997-405e-3d70-a870-186a2569f700 | -2.44027 | -54.03168 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1119fd2-3569-3f43-88ad-42949b1d0461 | -12.71077 | -58.20994 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78caa8bd-c5bd-3715-9e57-d6f8ac6313cc | -8.192 | -62.82613 | 2024-12-03 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6038fd34-124c-32b5-aa35-b7baf6e24a5a | -1.61492 | -54.24438 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a05b5a6-0df6-3dde-82fe-71a0c76f474d | -2.78894 | -55.36059 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09505556-c993-329b-b2fb-edd0743002d0 | -2.35632 | -53.93025 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README60.md)
