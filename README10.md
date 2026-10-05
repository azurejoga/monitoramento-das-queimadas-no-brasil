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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d52304a-e6b7-3c98-8d28-68f1e7164796 | -6.2159 | -52.8285 | 2026-10-05 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| d10ae4ca-c3cf-3870-a237-8c1770ba36ec | -3.9032 | -49.7137 | 2026-10-05 02:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6be4fa9b-dec6-35e2-885c-b112930c8a5b | -6.8952 | -43.6833 | 2026-10-05 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ee532587-7798-3367-92d8-0b73205c4a74 | -3.0549 | -54.1876 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d7e62ea2-769f-38a8-8dbb-ba22b7ebf395 | -3.0917 | -54.1666 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0e4c2c8d-d4ee-3637-8e61-b0a7ce7d80ed | -3.0733 | -54.1871 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 304addc7-8b9a-3e2c-bd69-3ab38ede8efb | -3.9859 | -55.8152 | 2026-10-05 02:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a6336834-f15f-3d7b-a211-52afc414577b | -3.0917 | -54.1867 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 9c9cb53e-ea6c-39f1-ac83-f33ad495e257 | -2.9448 | -54.1501 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 34bd559c-c7ce-39e9-9ca3-d2f3bf3ce940 | -6.1974 | -52.8295 | 2026-10-05 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 775768d7-c29c-3c85-b13b-1affdeec0db3 | -2.6859 | -49.0325 | 2026-10-05 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 77769435-d465-3cfa-85fc-7ed85b8451f7 | -6.0074 | -53.5325 | 2026-10-05 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a2d660f3-413b-3a2e-98dc-ce8fa9806e6d | -6.914 | -43.6816 | 2026-10-05 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1669f22f-5d75-363a-a27c-ac50ddd48fd4 | -3.0548 | -54.2277 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 47548146-1f75-3eef-9074-9c91c0d37022 | -6.0075 | -53.5122 | 2026-10-05 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| fca208e4-b188-33bb-a25d-208cc60a9f34 | -3.9217 | -49.713 | 2026-10-05 02:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e724917b-37aa-305f-9319-6f0edfecb1d0 | -5.9882 | -53.635 | 2026-10-05 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2795394f-936f-3298-933d-e02b427b2ad6 | 1.7304 | -55.6259 | 2026-10-05 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7f574457-5717-35cb-a408-bcf9a5af07b6 | -3.055 | -54.1675 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 2d93e0dc-a50f-3616-b8d9-ec0fccbdd1e9 | -3.0917 | -54.1867 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 7e29bbdf-44c2-3b49-9a37-6d91c4d316af | -2.6859 | -49.0325 | 2026-10-05 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| be98eae8-2f29-3c4c-bce4-8562979f3a11 | -6.0074 | -53.5325 | 2026-10-05 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 163c601f-d3eb-3dac-a98a-18c81372f492 | -6.2713 | -52.8665 | 2026-10-05 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a2edf99b-77f1-39c9-b39b-f1c8df64c02c | -6.914 | -43.6816 | 2026-10-05 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| db11f2ac-a000-3d66-bcfb-3eedd875d068 | -3.8447 | -50.3273 | 2026-10-05 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d6276a43-c98a-3f24-ac41-c1aeb3be8356 | -2.9448 | -54.1501 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 42a7f119-41be-3203-a303-9950bef2c692 | -3.0734 | -54.167 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 278.9 |
| dfb15c26-5d7a-3c20-98c3-65a40a038ca7 | -3.0001 | -54.1086 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| af779796-375c-3786-ac32-3d731db30e95 | -3.0548 | -54.2277 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| de92dc7e-e1b6-3a56-8730-c8a65c6ebd58 | -3.055 | -54.1675 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 780b4bda-1720-3060-88ee-5ae3e630f098 | -2.9817 | -54.1091 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 2889b87a-c585-3484-a89e-b8ea7850636f | -3.0733 | -54.1871 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 15b08ff3-12a3-3e95-a775-24068a4f2501 | -3.9217 | -49.713 | 2026-10-05 02:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2d29f06f-110e-3108-b38b-cf22e3e1049c | -6.2529 | -52.847 | 2026-10-05 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 28ed2f75-7196-3536-b536-4db2090e6773 | -6.0075 | -53.5122 | 2026-10-05 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ba68aa30-ba0e-38c8-b195-e599718fea9e | -7.4441 | -63.5777 | 2026-10-05 02:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6376bcff-5d2c-3136-9e9f-945a681b9b75 | 1.7487 | -55.6256 | 2026-10-05 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a56f831a-8f7d-3393-9316-8210b05ca5c7 | -8.4458 | -62.7131 | 2026-10-05 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a076464c-e28e-37ae-8f91-e7b41e0d1f9d | -2.9449 | -54.13 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 125fb103-f9c8-32f5-8d56-db69cb794e67 | -6.8952 | -43.6833 | 2026-10-05 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 537e8277-fee2-32fb-b612-71539dfce0a3 | 1.7303 | -55.6456 | 2026-10-05 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b8e02126-3d81-3e78-97c0-7384b8152515 | -8.4457 | -62.732 | 2026-10-05 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 2dfc9d3d-373e-3ebb-a51f-e2d3ff36f408 | -3.0734 | -54.147 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 92c46f2d-5918-36f3-af8d-008a94332c42 | -6.1974 | -52.8295 | 2026-10-05 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a77387c3-878a-3624-b5cc-62b3d96a6362 | -2.9632 | -54.1497 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a531a293-6b2d-309f-a2ad-ab29a702d421 | -3.8448 | -50.3063 | 2026-10-05 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c8f11a10-4ee7-3d5e-b10e-992271f365c1 | -5.9882 | -53.635 | 2026-10-05 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 198baff5-3958-3e69-aad2-899d1b36b627 | -6.2159 | -52.8285 | 2026-10-05 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| f2c589c6-5e2d-352c-9d3a-2624463eb0ae | -7.4442 | -63.5589 | 2026-10-05 02:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| c24fd714-9fc8-3f24-b913-3a1afd7eeefa | -2.9817 | -54.089 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 60f63dd2-3b25-3a1f-b99e-ef0fe65e4f32 | -8.4642 | -62.7313 | 2026-10-05 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a9b8adbe-67eb-3e64-8ccd-e77ea580fc87 | 1.8583 | -55.8216 | 2026-10-05 02:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cff1c068-232e-3f49-8694-693a3528f494 | 1.8583 | -55.8018 | 2026-10-05 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 59154547-0e39-352c-84a8-2e7cdeb56c81 | -3.0917 | -54.1666 | 2026-10-05 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 030e97c7-37f2-3eab-9530-6a5b93b737f1 | -7.4442 | -63.5589 | 2026-10-05 03:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| fcc55c31-5dfd-32ef-b6cd-dbb3016ec3c0 | -3.0001 | -54.1086 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 70d5ec86-97e1-385d-9ab7-034b42d42bc4 | -6.2529 | -52.847 | 2026-10-05 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| beffe8aa-c27b-3405-b3df-30fd83f590ce | -6.8952 | -43.6833 | 2026-10-05 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0d03d85c-2a03-3272-a605-127dd82bcf23 | -2.9632 | -54.1497 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a1e8e850-552c-372d-8ea3-f61c8e1ffb6b | -6.2159 | -52.8285 | 2026-10-05 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| c586e6e7-9614-37c6-b2e0-645250aa3145 | -6.2713 | -52.8665 | 2026-10-05 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 28d64537-0a94-3aa5-81e6-961f9340ef17 | 1.7303 | -55.6456 | 2026-10-05 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 78f675be-41b8-31bd-a8d4-96bb3875f5b2 | -2.9632 | -54.1296 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f607fb10-bb3d-3890-8f90-8789ef607c6c | -2.9817 | -54.1091 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| a28c7444-1c94-3629-81fb-e2c8dee60b29 | -6.2527 | -52.8675 | 2026-10-05 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fa533eb6-5688-36fe-bf8b-7ca26ad9f262 | -2.9448 | -54.1501 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e0cc4393-669b-3f46-b8e9-e58948f327d3 | -2.9449 | -54.13 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8d517654-db3e-36cf-b13a-4df8f4e0c214 | -3.0548 | -54.2277 | 2026-10-05 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| be947fa4-214a-345a-8d3f-228d08a3b915 | -8.4458 | -62.7131 | 2026-10-05 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 902364e4-03f1-36fb-95d2-36ca4622d5ca | -6.0075 | -53.5122 | 2026-10-05 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2bb71df2-b100-3d35-8201-dea81e919905 | -8.4457 | -62.732 | 2026-10-05 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 4231e8af-a9dc-3b70-8018-d965a4323334 | -2.6859 | -49.0325 | 2026-10-05 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 82ad5be9-4eb8-3b4e-896a-dc972c1e4420 | -6.914 | -43.6816 | 2026-10-05 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| a2f6f43e-377e-3d6b-9171-850dfb75cec0 | -2.9632 | -54.1497 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 712b941a-209c-305c-b763-28fbf0f12f31 | -3.055 | -54.1675 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 8ce175a1-1f81-377f-9d12-34d54a152866 | -2.9449 | -54.13 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| fc00b05a-d11b-31aa-ac4d-cb816822fa2f | -3.0734 | -54.147 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7a511dfe-e8f5-39de-829e-484a0b7f564b | -2.9817 | -54.1091 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 70af12ec-7fe1-36fe-bd0d-2faf8f4cc8e5 | -2.6859 | -49.0325 | 2026-10-05 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| af1d93c1-0750-39db-a9b5-326803d836f0 | -8.4642 | -62.7313 | 2026-10-05 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c2ad0cb3-836a-3004-9602-7201cdad2724 | -3.0001 | -54.1086 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5e7935cd-1470-3741-b2c0-52f0d2750d42 | -2.9448 | -54.1501 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| c98afacb-5783-3e74-b8cc-0b599e0773e9 | -3.0734 | -54.167 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 290.4 |
| 1ea17d34-9616-327a-933f-6e2d1aa2a0cd | -6.2159 | -52.8285 | 2026-10-05 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ed9566c6-781e-38c6-b58f-4134a0995469 | -3.4577 | -54.5977 | 2026-10-05 03:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f31928f4-d2cc-3019-b6e3-a9c478e2b6a1 | -7.4442 | -63.5589 | 2026-10-05 03:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 093feb77-a390-3f83-a979-fbd4adce007c | -12.1015 | -57.1583 | 2026-10-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bc12f4a3-c0cb-3794-a7c6-9f2f66331379 | -3.0917 | -54.1867 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 1a0569d1-6067-3ed5-866f-bae70394f9eb | -6.0075 | -53.5122 | 2026-10-05 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0516378f-157f-3330-aed1-bb56fc1f3b33 | -6.914 | -43.6816 | 2026-10-05 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 16fb4633-3e34-3019-9cd4-89e4f0094742 | -3.0548 | -54.2277 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 589ec1d8-29db-384e-ba54-cadda3ee766b | -6.8952 | -43.6833 | 2026-10-05 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3a5ec043-8d1c-3d9b-a6c3-0dddbe66a216 | -8.4458 | -62.7131 | 2026-10-05 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 407102e1-4d0c-389b-b8ed-89a87dd5c4ed | -3.0917 | -54.1666 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 20304070-698f-3eb8-bc96-2206ba8147ff | -2.9632 | -54.1296 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cba4dca9-890c-3ba1-9f40-8f2461234efe | -3.0733 | -54.1871 | 2026-10-05 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 78fc0e1c-da54-3def-a314-b2c849e46ec6 | -8.4457 | -62.732 | 2026-10-05 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 8970a4e7-1f1b-3e45-b015-d9e388dd467e | -6.0074 | -53.5325 | 2026-10-05 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b5c6b51f-aea6-39ef-afc3-00b6e9f1d9b5 | 1.7303 | -55.6456 | 2026-10-05 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c08bd38c-3ac3-344a-a3a8-6dac52eebdfa | -3.11 | -53.75 | 2026-10-05 03:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
