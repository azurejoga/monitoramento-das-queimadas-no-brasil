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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 817d1a0d-9398-3d17-aee3-52e3fe0d1e02 | -3.1431 | -50.2464 | 2025-10-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b564142e-44a5-3baa-a4bb-3928247e896a | -10.4937 | -43.4552 | 2025-10-18 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3d09dbd5-5bfd-3a03-92e4-09ac7b78aebc | -3.8572 | -41.5719 | 2025-10-18 01:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 8d5677b5-0e95-3f6e-81fb-3d194afb9bd3 | -10.4945 | -43.4079 | 2025-10-18 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| b6ac67b1-9bbf-3851-84cf-ec98f8a9186a | -10.9564 | -45.4579 | 2025-10-18 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| d3dce932-542a-37aa-a752-359190f7b220 | -3.1616 | -50.2458 | 2025-10-18 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ac23dc01-ecf3-3e18-92cd-be2dd37c8cb9 | -10.9567 | -45.4349 | 2025-10-18 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 79f6110c-0e40-36bb-a63b-1394d694a696 | -4.4446 | -43.2164 | 2025-10-18 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c60a0de3-085f-3f4e-a4fa-c6fda24b90a4 | -10.9752 | -44.3244 | 2025-10-18 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 07baa5d0-616b-3f2d-abe0-d798820eb161 | -8.6029 | -40.2083 | 2025-10-18 01:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 79d89017-eebd-3856-9b03-9104682a3861 | -19.1114 | -57.5486 | 2025-10-18 01:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| f593326e-e9a6-3089-8576-89923477f760 | -4.4445 | -43.2397 | 2025-10-18 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| a06b9a01-eadb-33d4-b5cb-6f4578377d9f | -10.4941 | -43.4315 | 2025-10-18 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| b0c041a9-21f1-3880-80a8-188d5a83361e | -5.3105 | -44.8423 | 2025-10-18 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c13ca865-e456-3a30-8d7e-f28b91d600cf | -18.393 | -55.498 | 2025-10-18 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 813e4f93-054b-3632-8fdc-0bbdd69afe26 | -12.5947 | -52.8014 | 2025-10-18 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d0f15138-1b30-3c59-91d6-cfb4cd1efec8 | -11.6109 | -44.0678 | 2025-10-18 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4a9f3433-eaf6-3f00-aba8-2eee1787ea1d | -4.5267 | -44.8225 | 2025-10-18 01:40:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| eb27f681-878d-3ee4-811e-c8ff34c6e67e | -5.0029 | -46.0108 | 2025-10-18 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4e63860c-e2af-3294-a832-ca6646131c85 | -4.4633 | -43.2152 | 2025-10-18 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 7f0d5e5c-ac4a-38c0-8bb6-51659e20b740 | -12.6138 | -52.7993 | 2025-10-18 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d3f332ee-804b-391e-af23-0da3e42bcb38 | -12.5944 | -52.8223 | 2025-10-18 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8bbb6ff1-5c61-3326-b747-dabc293a07e3 | -5.0214 | -46.032 | 2025-10-18 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 10e02af0-3dc0-3ae9-b5a5-28139ff6eb5a | -12.398 | -47.2056 | 2025-10-18 01:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| fa78e573-619e-3fde-9eeb-c9f9aa53a471 | -10.1718 | -44.5264 | 2025-10-18 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3b8dfe5b-01dc-3b39-a2e3-8369f0aefbe6 | -19.0915 | -57.5512 | 2025-10-18 01:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| fcaae14e-b345-3ec8-a459-5c77b0081ab9 | -18.393 | -55.498 | 2025-10-18 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| aaa22151-207a-317f-a827-b59b84568985 | -4.4633 | -43.2152 | 2025-10-18 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| aaf077a9-3189-35d9-b990-d82e69df9663 | -4.4446 | -43.2164 | 2025-10-18 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 23ba02bd-e256-36fe-8536-89cef6fcb8ae | -10.9567 | -45.4349 | 2025-10-18 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2b3a50fb-1c94-3132-8a02-f1bd0185b59f | -12.5944 | -52.8223 | 2025-10-18 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5af52fc3-9c53-3a0c-bd71-4f8d7c2c4691 | -18.3735 | -55.4798 | 2025-10-18 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| adb4125e-db4e-3724-97ac-db783d339780 | -12.5947 | -52.8014 | 2025-10-18 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 0ff7c7db-eed7-3a3f-9d1d-063e068dd855 | -10.4937 | -43.4552 | 2025-10-18 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f9da500a-067f-3e6b-b3e2-6076ed178a33 | -10.4941 | -43.4315 | 2025-10-18 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 22265f28-4818-3322-b828-b7c1a16e596c | -3.1431 | -50.2464 | 2025-10-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f9434944-96d0-3e42-9ded-17b4b6ba3173 | -13.2296 | -43.9692 | 2025-10-18 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 8e4d054a-92d2-339a-9ef0-1d96bbe3ea76 | -4.5455 | -44.7987 | 2025-10-18 01:50:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ba31a8bc-bc79-3da3-ba67-21ecd00404b6 | -10.4945 | -43.4079 | 2025-10-18 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bd2b884a-cf81-3b33-95f9-ae7e47507366 | -10.1528 | -44.5289 | 2025-10-18 01:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| c2c6f89d-65db-37c6-a7a5-0631d6b8b21e | -19.1114 | -57.5486 | 2025-10-18 01:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 794e64ed-525a-31b7-aa5a-626329ef48a7 | -18.3938 | -55.4559 | 2025-10-18 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 2b95c96b-ce67-32fd-8def-bf0bdc1085fe | -17.8586 | -40.1002 | 2025-10-18 01:50:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 011871dc-41f5-3e61-905b-0588b094889c | -13.4663 | -43.7617 | 2025-10-18 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 6128b83f-bc43-321b-af08-5fd069d56c8b | -10.9564 | -45.4579 | 2025-10-18 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| bf78a234-4d5f-378b-bb6e-525163b648b5 | -11.6109 | -44.0678 | 2025-10-18 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 16405f98-65e9-3e36-96ef-2923f994614a | -4.5269 | -44.7998 | 2025-10-18 01:50:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 98030319-0b5a-3655-b538-b2e7f877d44a | -12.6138 | -52.7993 | 2025-10-18 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| bcb29d56-2b58-3877-96db-05e91c55b393 | -18.3934 | -55.477 | 2025-10-18 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 222.7 |
| 42c13395-3e4f-39de-be28-a7c22280edde | -5.0215 | -46.0097 | 2025-10-18 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b28dc66e-848b-3b94-b09a-c9926d642cc8 | -10.9755 | -45.4553 | 2025-10-18 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 89accf56-421a-387f-b718-4091cdc101b5 | -17.8789 | -40.0946 | 2025-10-18 01:50:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| d4833e9f-0ae9-3291-8d01-840d54f39ff3 | -10.5132 | -43.4289 | 2025-10-18 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0d095dea-ee8f-3493-a1d8-54d52feb0547 | -10.5128 | -43.4525 | 2025-10-18 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| bfb137d1-27c9-3b18-8804-bee24dc7e677 | -8.6032 | -40.1834 | 2025-10-18 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 170.9 |
| ab7c7c19-eac5-348e-acd6-962ca5aa4036 | -3.1616 | -50.2458 | 2025-10-18 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 7e723b7e-69dc-3e5c-b499-3ea4d233b755 | -4.4445 | -43.2397 | 2025-10-18 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 9accfb39-f178-3c06-a8ae-f53f5e83c68b | -12.6135 | -52.8202 | 2025-10-18 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| b697b66e-f254-36d4-8846-1a4472404ff8 | -18.4133 | -55.4741 | 2025-10-18 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| b301795c-34a8-330f-8208-adbf8fee39fa | -8.6029 | -40.2083 | 2025-10-18 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 98.4 |
| a40f636e-9edf-395a-acb6-f3e9367fa6de | -11.5917 | -44.0707 | 2025-10-18 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4050512a-f1b7-322d-a0dd-0ecde1a795a9 | -4.4632 | -43.2386 | 2025-10-18 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| aaf7954a-56d0-3aaa-a099-c9238d5163c3 | -8.6223 | -40.1809 | 2025-10-18 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 6f1809e8-45c1-3215-9141-f34def57a234 | -5.0214 | -46.032 | 2025-10-18 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 29c8cf5b-15bf-39eb-b025-496c75ba0e52 | -5.0215 | -46.0097 | 2025-10-18 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| ec466c28-2213-3d69-afe2-d24ccbf54689 | -11.204 | -47.8318 | 2025-10-18 02:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 980d403e-f3e1-3bdb-b7f3-f93999411182 | -6.5631 | -51.1126 | 2025-10-18 02:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 95939a58-f57e-3d4d-9602-a69c7152fb2d | -10.4941 | -43.4315 | 2025-10-18 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 39eca56e-1cb7-3254-ad2a-766d20c5eda1 | -5.0027 | -46.0331 | 2025-10-18 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ba86dde4-865d-3a80-add5-fbaa1bd7d323 | -4.4633 | -43.2152 | 2025-10-18 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c201c882-e831-344c-b101-845e0c5772f5 | -4.4445 | -43.2397 | 2025-10-18 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| e1129a83-b8b6-3ae4-9f43-760fea25208c | -4.4632 | -43.2386 | 2025-10-18 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 18a1dbc6-ea75-3bde-ac04-885398704033 | -12.5944 | -52.8223 | 2025-10-18 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e5c97b62-40b8-351d-9382-1cfe67896e16 | -5.0029 | -46.0108 | 2025-10-18 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e1b0acb0-612b-3717-8476-e97aebb3684e | -10.5128 | -43.4525 | 2025-10-18 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 70f1628c-27cb-3dbd-b40d-7d6c78facd4d | -8.6032 | -40.1834 | 2025-10-18 02:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 174.1 |
| e6beda69-8dd0-37a6-86fc-0f9b64ea8ea9 | -6.5261 | -44.8887 | 2025-10-18 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0643b3cb-e121-3ca8-a165-77744701f652 | -3.8572 | -41.5719 | 2025-10-18 02:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| eb37e1b3-bde2-32c2-a688-bc8c2fc6da9a | -11.6104 | -44.0913 | 2025-10-18 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 45655695-9d5e-329b-8945-e123dcd6a528 | -10.4937 | -43.4552 | 2025-10-18 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| fb7ce013-5f28-364b-b76d-4feacd4d44ef | -3.1431 | -50.2464 | 2025-10-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5a11c974-b737-3e72-acbd-bfabc2093621 | -3.1432 | -50.2254 | 2025-10-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 903beb65-159b-3e60-b350-eaab997fc2df | -12.5947 | -52.8014 | 2025-10-18 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 103888f6-8f66-3a25-8c3b-451cbba2f791 | -12.6135 | -52.8202 | 2025-10-18 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 5d849294-8cac-31a6-96ad-0b23aecbed50 | -10.1718 | -44.5264 | 2025-10-18 02:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ab3f8205-7b79-33a5-b982-d549e7a56341 | -4.5269 | -44.7998 | 2025-10-18 02:00:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1d58f745-f13d-3acb-94f6-01b8a6f1fae0 | -13.4663 | -43.7617 | 2025-10-18 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| a545f722-e61e-31de-8c0f-852b542e711c | -8.6029 | -40.2083 | 2025-10-18 02:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 136.7 |
| d9afc866-9e03-3dec-b100-49ede1fa2c0d | -6.5259 | -44.9114 | 2025-10-18 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3ec92fab-4df5-3472-93f8-eb101bd27f78 | -4.4446 | -43.2164 | 2025-10-18 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 10d30e56-7167-3f4a-8ed3-5faae682a2ee | -12.6138 | -52.7993 | 2025-10-18 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e149fb76-e586-3c6c-b57e-c354f1e242af | -12.0883 | -47.4053 | 2025-10-18 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 04dbcdbe-3945-301e-8710-9fc6afc1576c | -6.5071 | -44.913 | 2025-10-18 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 62fb440d-c557-3e97-9bf2-6b03138d425a | -10.1528 | -44.5289 | 2025-10-18 02:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4607dc30-d80f-3ded-91c5-71743be030c5 | -11.6109 | -44.0678 | 2025-10-18 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e8149522-78d9-34ff-8efc-14b13dc30715 | -4.5269 | -44.7998 | 2025-10-18 02:10:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| a829641f-e899-3e33-8e16-d4008c3ac1a9 | -4.4633 | -43.2152 | 2025-10-18 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 33668d48-05d6-369e-84b2-800c18e8dc27 | -3.1431 | -50.2464 | 2025-10-18 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7eeb4100-0706-3b87-9042-09321dbe51d7 | -4.4632 | -43.2386 | 2025-10-18 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 10bd2e6f-3bfe-31a2-a76f-07fb40c46bc7 | -12.6138 | -52.7993 | 2025-10-18 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README9.md)
