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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38a75d53-e00a-3bd6-a614-a4e0cf44a4cb | -3.55717 | -52.05392 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8431a356-e1d4-3474-85b6-34fc3c0b9517 | -3.53352 | -52.13634 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f9abbdd-aa05-3915-b49a-0963283b2472 | 0.82056 | -51.85019 | 2024-10-10 04:42:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f1452df-9356-37f2-b3c9-5516d867eb13 | -0.38345 | -52.05215 | 2024-10-10 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc421ab7-266c-3718-b656-e7e7fd839be3 | -0.38284 | -52.05599 | 2024-10-10 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cab1bf2d-c1b4-3380-a1e7-b9b79d7b101c | -0.38182 | -52.05333 | 2024-10-10 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8341b9da-15fc-31fb-9a30-8e2b5ef0a664 | -1.84256 | -52.07466 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c39f219f-05af-3eeb-9a4d-0852e9120d80 | -1.72029 | -52.50635 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d2897ad-a3c7-3187-8994-83c6e1e2eb57 | -1.71966 | -52.51025 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 731b37db-b65f-3a74-811b-5d12eb2ce2f6 | -1.71937 | -52.50675 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 807d588d-7ca5-3602-b996-20b02dc8e15a | -1.71876 | -52.51066 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82941c29-db70-3871-aef2-e768cd8ece2f | -1.71841 | -52.51806 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fc2043a-cb02-3097-9b49-8b5aa43e141a | -1.71815 | -52.51456 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c314f6dc-b7bd-3e4f-bc8a-2075a6a257f5 | -1.71754 | -52.51847 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4deffc0-2b65-3b78-afcb-5d52cc2113c0 | -1.67959 | -52.12648 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 803d0834-eb7e-3519-8796-d881b23705ed | -1.67613 | -52.12593 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf1fc4f3-0d97-31ce-bc34-ea6dcd9834c8 | -1.66039 | -52.14352 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41f73760-c764-3ee5-a3c9-dde8522c05b1 | -1.6533 | -53.33998 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9587e680-fb80-310d-8ff4-1b3881b5e48a | -1.64964 | -53.33939 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c0304c9-eb86-31b4-b25d-faa81179720b | -1.53741 | -52.95512 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14d6ea26-5b1d-31da-aa41-718696ba9cf3 | -1.53447 | -52.95041 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21ee71e9-aa67-33b0-8ac2-eb0cc9331523 | -1.53382 | -52.95454 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6f9fd32-2963-37a3-a106-9b95deca955b | -1.53088 | -52.94983 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6c0fbb3-fbfc-3e13-ba2c-8e34373334bd | -1.53023 | -52.95396 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e2b2d8f-c16a-31b6-b12c-ce4aec07d342 | -2.07475 | -52.02551 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f5aff54-e19b-31b5-b49f-41e5d608d122 | -2.07416 | -52.02924 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea8685d9-463e-3dd6-b922-c74aec83e5ab | -1.94933 | -52.06397 | 2024-10-10 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99849d3c-8388-39d7-9c29-53c59fcd589b | -3.62805 | -52.28997 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7264a0c8-2bcc-3a4f-8280-ea31589041d7 | -3.5115 | -53.01492 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0b2202f-ec5f-378d-b313-ca27c9847bc5 | -3.49986 | -53.45262 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 342ccdc8-03fc-3a65-8129-d0faa21cd6b7 | -3.49399 | -52.80506 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03d75429-17af-337e-b705-2586f99abeec | -3.4905 | -52.8045 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0896d42-c72a-3b41-9021-caa2f4c7854a | -3.47819 | -53.28922 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93fea882-a503-3935-a250-d3ef0a37ca24 | -3.4496 | -52.81387 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b202e30-1b26-307a-bc84-6301ae227e7a | -3.44898 | -52.81778 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 317115b1-7fa1-34d9-bfc4-08cbfd2bbb10 | -3.4461 | -52.81335 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdeb2704-caef-3e18-b91b-d59f37186d04 | -3.04354 | -53.04351 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685dace0-5c3d-3455-86f6-76670d72da76 | -3.03999 | -53.04295 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8710881a-8a23-3d7c-82bb-9e42a73c7303 | -3.03645 | -53.04239 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94264b7b-1852-317e-84a6-933c1c4dea30 | -2.95581 | -53.04619 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f765c7f2-ed74-3fc9-95aa-d4a78c6c81b1 | -2.8582 | -52.90956 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e04240d-60af-39ce-b4ca-ac26a17b155d | -2.85756 | -52.91349 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73564648-9e10-3bed-a981-3d0336cf9068 | -2.85518 | -52.90606 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 116d4a9f-499b-3e27-8a6d-971b2421bb41 | -2.85467 | -52.909 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 84886957-b9cd-3a7a-bc7d-1e3fff926e56 | -2.85456 | -52.91 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ff30ab6-e9dc-338a-931c-27c5a9903cb4 | -2.85164 | -52.90552 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5771b360-f808-3c67-a43a-b1248b50925c | -2.85113 | -52.90846 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 39e3a80f-9b1c-308a-b58d-505d26f4f22c | -2.85103 | -52.90945 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed0f048b-df17-3b02-a261-111d1d07a462 | -2.8505 | -52.91239 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d462666-be78-35f6-8703-4e0773111240 | -2.85041 | -52.91338 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89b09034-08fa-3f52-b8a9-58df1f158e1d | -2.84959 | -52.94172 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 239ef7ae-7ed2-3753-aa7a-b0eaf54370c4 | -2.84955 | -52.94065 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| da46e78a-4551-3d26-8a65-131aecf5b24c | -2.84749 | -52.90891 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b67e0d58-8551-334e-99bb-f55182ca41b7 | -2.84687 | -52.91284 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cea7259-0077-3d5b-af51-682e7a0326c1 | -2.84668 | -52.93713 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 17f40851-240a-3302-ac9c-59f367b6c3c9 | -2.84666 | -52.93609 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 21110d04-2ef9-3cc1-83af-a86f3b9b58da | -2.84605 | -52.94116 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 56766f93-2769-3565-b5ca-25fce8337e1b | -2.84601 | -52.9401 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6154b291-9c34-33c5-aacf-0326baac61cc | -2.84535 | -52.94413 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32e5f62f-ab98-38e1-9fbb-4aba54cedfb1 | -2.84396 | -52.90834 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b61716d8-013b-34d4-9ee3-edfd5fcf3023 | -2.84378 | -53.31799 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3dd707d-1449-3dde-8269-e61d66cfb033 | -2.84334 | -52.91226 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 702c8a67-0e47-3fc4-84db-0d0c012a4626 | -2.84314 | -52.93658 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eb6b1011-1079-39f5-aa4d-63117eef5019 | -2.84312 | -53.32213 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 542a4788-2a75-3c4d-b25f-a5a7135da928 | -2.84252 | -52.94059 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ad49be29-4339-3fc6-8c47-a7a7cfe60ac3 | -2.84083 | -52.97203 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e71ff3e-3c5b-3412-8a7b-354d5c1e29f5 | -2.84041 | -52.97718 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d0720bf-c2b0-393f-bf23-b952fd891b82 | -2.84018 | -52.97606 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bef1f4b5-e44d-3a7d-b4c2-6b3c24bb3b6b | -2.84017 | -53.31741 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6146e5da-c896-3379-b285-f5695715612a | -2.83951 | -53.32156 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1fcc1b6e-a201-3b5c-999d-7667ebe031e2 | -2.83749 | -52.97263 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86ab2f17-ce56-36d5-ae89-2c133fe972a2 | -2.83686 | -52.97663 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cc544ff-8d7d-39e1-a3ae-0fd4b3a077d2 | -2.83623 | -52.98068 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfbda256-4cbe-3ff1-9721-61b89f0d05f5 | -2.83395 | -52.97208 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0dab693-f47f-357f-8de7-1b32850be910 | -2.83332 | -52.97609 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e88e68ea-776e-30f8-922f-259cc8ec0b0a | -2.76949 | -52.96623 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f5b43df-ab4c-3cdc-945c-367c5efe8cd3 | -2.68572 | -53.34969 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d913f50-2005-30f9-b690-7c6a2bb36111 | -2.68278 | -53.34496 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 27b44361-cfb6-30ca-a6ae-a9cf8c409d3d | -2.6821 | -53.34912 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1598c419-dbd7-3fb5-98fd-a0b79ac3c063 | -2.68143 | -53.35328 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24a4c694-7cc5-3429-be25-0adfa264b2e0 | -2.67984 | -53.34023 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8dde3abc-1bbb-3c5f-9f5e-6ba94d5b3eb9 | -2.67916 | -53.34438 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e4a1e058-d920-38e0-a148-4406e44910f3 | -2.67911 | -53.33689 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4990fbe6-8d73-3a30-86b1-0c840ce04f09 | -2.67849 | -53.34855 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1111f8e9-98d0-3180-87fe-a32cebd3dc47 | -2.67846 | -53.34106 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7677e644-b5d5-3f4c-a639-02aed31b4215 | -2.67781 | -53.35271 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed7a069c-d2cc-33d3-a713-1700c7f9a466 | -2.67781 | -53.34522 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 74ece509-7cb5-36cf-8817-debbd82397e7 | -2.67716 | -53.34939 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 183ad382-cad9-3a96-9a0d-82c03027226b | -2.6765 | -53.35356 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 24c5eb38-4eb8-31dc-b693-9486cee9a0bf | -2.67623 | -53.33966 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 92bd513d-f6b6-319c-a7fc-75ec9d9c29fe | -2.67555 | -53.34381 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 62014c18-f80f-3936-97c3-89ca0f773558 | -2.6755 | -53.33632 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ecf33689-bec6-3e7d-a68f-87ed17b0c74f | -2.67487 | -53.34797 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| a425ad30-6535-322f-8471-7c2d311f45f3 | -2.67484 | -53.34048 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4e120df6-f450-38eb-90bc-418c4d2afa51 | -2.6742 | -53.35214 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| be3e04d8-cb61-3047-ad5c-c9597b7fdba4 | -2.67419 | -53.34465 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 7767887a-a2d7-38ad-a6d4-3ce7d4402a21 | -2.67352 | -53.35631 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 2fdb7521-5b1b-3fcf-8c48-5eeec368025f | -2.67289 | -53.35299 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 3c49bc86-2fb6-37cd-80fb-290a4aac8d90 | -2.67261 | -53.33908 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9dba7de0-3c23-3f2e-8b2b-d7d291d252d1 | -2.67194 | -53.34325 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |


[Clique aqui para ver as próximas entradas](README93.md)
