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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd198cac-db36-3eb1-ab13-f86032dc5acb | -3.05232 | -50.34331 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45033b99-cbd4-3df1-b8fc-cf29a728f316 | -2.15239 | -50.91264 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f64099b-22b2-3584-ae68-1cebc169c636 | -3.34573 | -48.96346 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| ccf4980b-5615-3dab-b848-f39e087c983c | -2.18647 | -53.69711 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5d13fe5-3b71-330d-84e1-9486f16148a3 | -3.61732 | -54.79425 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616e200b-203b-3bda-b099-da2e0154dd82 | -3.46358 | -53.82008 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67b477b8-4ad9-3419-8078-c2eec546587a | -3.65981 | -54.65389 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbda1f08-bd79-3982-a866-88464ec2fb4e | -3.25683 | -54.53371 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1a2ff4f-bddc-36e3-a63e-bd6ed4e3ced5 | -1.71002 | -46.14635 | 2024-11-13 04:57:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95ae10c7-3200-3bbd-9f5d-c7dbe2e584ff | -3.0627 | -51.3802 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13830dde-7ada-33f4-abcb-82feb4cf2204 | -2.56781 | -53.97905 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03983368-6fc5-38ee-b90c-3d6a318f78da | -0.28766 | -51.6709 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09b47d95-685b-36b1-bb19-e3b977338265 | -1.34569 | -51.43324 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed6815c-c510-364b-bfd8-52968c2ac7d8 | -1.474 | -52.26558 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a2111de-30c9-3bc4-bbd6-6b246152fbec | -3.17809 | -45.8089 | 2024-11-13 04:57:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a45add3d-4535-3cbf-8f98-fe05f9ca286e | -4.06016 | -55.79136 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a924633a-351a-31f2-ab65-f4e1a2c01235 | -2.90172 | -48.76353 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b10429a8-1cfe-3f0c-b8ee-c043552f923d | 0.81838 | -51.87123 | 2024-11-13 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 51f8a3ec-490e-3dbc-9a76-206ec2d5fcf5 | -2.82223 | -52.95889 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 852d7f0e-0a88-3bb3-8f1a-cbfbf61176de | -2.28151 | -53.52622 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff28d6e2-fd16-3c38-a969-47c1e712a72a | -2.76233 | -54.04101 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2af3534-dfcc-3e90-9b0a-e71f1f0143c6 | -4.04463 | -56.11058 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d229ed1-a37f-3152-9b71-cfb5be407eac | -3.09846 | -53.98082 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0f564de-5e3b-310e-9a8a-de6ec2999102 | -3.73216 | -54.43032 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15d8c66d-67f9-3523-b7a4-eac895abb48d | -3.04115 | -50.5706 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5e05e4c-1b09-3b7e-b586-5c0801ebae01 | -2.45329 | -53.929 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08696b9b-8538-3192-86d5-b7d952770386 | -2.56182 | -53.99575 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91487be6-b839-3692-bad2-04f2b18a6270 | -1.95369 | -53.31697 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9758d289-70be-3057-b0ed-81c567ebff87 | -2.62197 | -49.23448 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98f062f9-eba0-3448-8ec1-cc8e26c9c879 | -3.24353 | -50.58314 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89b8a7a7-d099-3755-b7c8-a2682e75cc77 | -3.10522 | -54.30761 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8201f9f8-d49a-36aa-a09e-6375f10dd8ee | -1.55419 | -51.85766 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21b6dee8-ff2c-30c9-8aa1-9f87b5c7b724 | -3.73163 | -54.43377 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4817d870-9302-36b0-9f2b-073d58e4f011 | -2.30727 | -49.08619 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92294c4b-db27-3f54-9b9c-0a0cca4cf15b | -4.02046 | -49.00716 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c51c5c7-46f6-3276-822c-5cd79383037a | -3.24871 | -50.3097 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a37564f2-a319-3308-8650-33c0f6424046 | -2.99217 | -51.339 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 419ada45-291c-36e5-b102-c94414a2405b | -5.05304 | -44.48084 | 2024-11-13 04:57:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdc2a5a2-6879-34b9-88a1-f60a1c983dfc | -2.44912 | -50.39527 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b3d71c-03bb-378f-8ce6-f9e456d4d728 | -2.92156 | -51.70419 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16b1e283-e3e9-3e81-b897-9fa1d057fb26 | -3.2835 | -53.66563 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5a82816-59b5-36dc-9ec9-5cb53a300e1b | -2.61207 | -48.25293 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d86782c-2807-3783-87ff-c820a75e4cc9 | -2.58224 | -51.92217 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8d259ac-22fc-36eb-96a2-eb43846f989a | -2.41172 | -48.63654 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6564ebd1-51ae-3105-9c2e-9804d3449caa | -3.36601 | -50.15401 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 528f6ad7-2d80-39f1-bd4a-d6b28da5a29d | -2.46314 | -48.82413 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc348f0d-6a16-3010-9cd0-a2ed5919ff04 | -2.56558 | -53.97166 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631d61c9-ff15-351d-90b9-2248a26047e1 | -1.64539 | -55.25338 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5e55b14-138e-3e41-906c-2b14cd314d96 | -1.40011 | -51.10714 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9d32742-1b6e-36a9-9ed0-914ac2adeae3 | -3.17053 | -50.4573 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6ca77dd-29ec-3af5-b9b9-981c70552392 | -0.38802 | -51.74795 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f94a965-292e-3e2b-9de0-7c31db2d3bb3 | -2.11283 | -50.69867 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 504faa31-a696-3a1a-ac6d-073b08ec0bc7 | -4.13333 | -46.6317 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b8cc04a-0d93-34e1-bf53-519c14bf74b9 | -3.08175 | -54.47821 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab2d606e-1c86-352b-9f98-3731ead7961c | -4.08994 | -49.14036 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7157ba11-b583-366d-8e55-cc2452da2c60 | -2.97193 | -53.87691 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cdcdcea-fad0-34e4-b624-892bd140a923 | -3.43978 | -50.30971 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7857b7a6-ced1-3483-805a-62babd88f419 | -3.34428 | -53.21037 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f70dec2-c9a4-3f33-b033-a9ad90a4a07f | -3.16755 | -50.45255 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e301ca9-1a7e-3944-bc22-bd73b21a7dc5 | -1.5748 | -53.73885 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e754e5c-bbbb-3216-a283-8be251917408 | -2.87421 | -49.43455 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765d7d17-0aab-389d-bc67-40f0af15da96 | -1.48037 | -52.09687 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fa88d05-916d-34d9-b19b-1927c0a5f5f0 | -3.17478 | -50.45365 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53631445-9519-3095-bc31-5665fc81c0f6 | -2.77118 | -54.04943 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecf9f15f-15d0-3b9c-a43a-e75d4e98cbbc | 1.06085 | -60.60816 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ea5fe201-4d3c-3aa5-b896-7c3c180e86e6 | -3.04708 | -54.8498 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9668be7-7eaa-3e69-a577-807647b6451e | -3.27353 | -48.7527 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d58513d-d831-3fb5-9ff6-6be1408e7ae9 | -4.28763 | -44.19406 | 2024-11-13 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 22b2ab33-9e83-388e-988c-2cf7355e0abf | -1.88603 | -54.20534 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4acb8358-1a10-3a5b-a82c-92f5021f604b | -0.91644 | -51.76003 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64adb63b-e33b-33d0-bed6-fad80476f60e | -3.57316 | -52.12381 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14ffb13f-a1b2-3e5d-a7cd-72789e350420 | -0.94957 | -52.40186 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30995ab9-39c8-394c-8bf9-d3c1aa6bb9af | -1.61857 | -52.23375 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5c5b074-5856-334f-9c71-68c162bab5f5 | -2.21403 | -50.7698 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dccf6699-ded1-3478-9dc2-bb9f54e57cad | -3.24506 | -50.30916 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c332f69f-7953-34d4-9425-4b578349c6b7 | -2.18424 | -53.68973 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23801ebd-c170-378d-ac78-86eeeec4f04e | -2.98346 | -51.34946 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a111dbae-3478-3f48-bb79-79a03c126141 | -3.06519 | -50.33229 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5836fcd3-3285-3659-8f29-bec7c988cf64 | -2.12528 | -50.68842 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d82e83ee-4cf5-31ca-b771-abea998d5bbb | -3.06046 | -50.3435 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d0089dd-b828-35ec-b581-e910acb7f7f4 | -1.5312 | -51.34746 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52c6a911-d3d9-31a9-9051-beb00642d125 | -2.98582 | -51.33413 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3fc3077-8a12-30ca-9d00-fb28ef173fe2 | -2.597 | -48.18683 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6b59fc-ebf6-3127-b8ac-4f9303222e2a | -2.7367 | -45.29703 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e10beba-4e0a-3c09-b7dd-dae07f795e32 | -3.69611 | -51.38703 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2884719-2627-3a37-9322-31f56d07e8ba | -3.69885 | -52.28324 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9eeb52f2-42d5-365a-baaa-4396204bc59c | -3.26499 | -50.42727 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e06da258-56aa-3c96-b821-187d3e865df8 | -2.24723 | -53.74579 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c8a2aea5-caf6-32ea-a5ec-7c4194436f16 | -2.93415 | -48.32228 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff23749-12ad-3f61-9170-766a0dba77d8 | -0.87227 | -51.95666 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5a66b15-49d2-364e-b018-e97fb97248e8 | -2.46929 | -48.44896 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d18ad6-e516-3150-abb3-a83113ad514c | -2.66227 | -48.65664 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a94fc29-4862-3769-bb7d-b9f8aaa6ab77 | -2.21035 | -53.74363 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa7de795-7d97-3d3d-a190-45efa95c2ed2 | -1.46185 | -55.23645 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f0d4676-45aa-369d-94c9-8ce61bbff251 | -3.61871 | -51.36848 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5761076-7854-3a27-87d2-900f51593dcc | -2.2004 | -53.73792 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebb7178e-cc5b-39fc-9c4c-71336985109e | -2.14485 | -46.40081 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abae526d-a637-385a-9ae2-6ae751b94d23 | -1.65548 | -52.54323 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c5193eb-988a-31e9-98e4-6b77546a6682 | -3.26447 | -48.75845 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 140f79d0-2de1-3843-950d-0171b5326a50 | -2.58337 | -51.93712 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
