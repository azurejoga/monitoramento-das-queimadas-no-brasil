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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e52036ee-2119-37a0-867a-d1b4673d8ae9 | -1.74779 | -52.3423 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91baf8fb-8f8d-365a-af42-da7d47b1e3a0 | -1.68786 | -52.73764 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3982515-8dec-3cda-ba7a-b5bd251f1b90 | -1.68708 | -52.74247 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d031770e-16b9-31ca-8a4f-b4b4ae38a554 | -1.68399 | -52.73704 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9634d286-db9b-374b-8ea7-bb460203e136 | -1.66162 | -52.667 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d10a98a4-6091-3917-81a4-fe93c21aa14b | -1.65777 | -52.66641 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0e45cd0-b7f0-3cee-bc7c-9fab2a1969ca | -1.65391 | -52.66581 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84182dd2-6f3a-30f0-9835-64691e5b1e8f | -1.61659 | -53.33118 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4e62548-bbcf-3df0-9b2d-794ecba8f6cd | -1.59618 | -53.18856 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad5f8e36-270e-3c56-b882-762e6be0591c | -1.59563 | -53.19205 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d154f7a6-6601-3350-8c36-f54bb809ffad | -1.59451 | -53.1886 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9341b474-af76-38d7-8279-11e84956908d | -1.59394 | -53.19209 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1aaf8d22-484c-3bc8-bd61-597f7543169f | -1.59165 | -53.19138 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e90bc84-06f1-3008-bd04-9257c1b504b4 | -1.58819 | -53.18738 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbf0d8ca-fbb5-3cdc-88d1-c99f56ad1ab2 | -1.58767 | -53.19075 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94e5c586-5ecc-3550-909b-4afcd14351fa | -1.58714 | -53.19409 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cffa68e9-4445-3945-982f-a8cbdf08e600 | -1.58474 | -53.18337 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4f58da8-5c13-343a-a910-59d949e29c8d | -1.44837 | -52.84978 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdc35c68-fd9c-337b-b600-e1325523f55d | -1.0834 | -53.1677 | 2024-10-29 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cb30809-6224-3705-9ca1-64a3f1389cc3 | -2.99993 | -53.43313 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e9a8a828-60f1-3440-aa9f-3d809f1d238e | -2.99908 | -53.43834 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0c5f43ca-cd06-3abf-94c2-018bc0a258ad | -2.99512 | -53.43766 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 102f25a2-2f73-3518-973f-c600dd88dc1f | -2.99224 | -52.90971 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4deba73-9c3a-32ee-a739-5b4b4672d785 | -2.98348 | -53.26292 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48bab4eb-b90d-3481-9a97-b2a4413460b1 | -2.98269 | -53.26796 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dccfa78-c1c3-306d-b7ec-d8551045b094 | -2.97877 | -53.26729 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314034bd-a19d-30cf-80ec-e8e54acf7ddd | -2.97485 | -53.26662 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d8c484e-8fe5-37d0-a8a1-cadefa55b84c | -2.97404 | -53.27168 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be3dead8-4da3-371b-ae10-1ec612a32e5b | -2.97375 | -53.34554 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32603c02-24b8-3e1e-a436-8dd270b58341 | -2.97093 | -53.26594 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 189fd0f6-202f-3963-a664-c30308fd86eb | -2.94655 | -52.56598 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2ee0eed-2be1-35d5-b3e1-e65d813867a6 | -2.94278 | -52.56542 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cc09939-b1fa-3e09-b8d8-ba2426d19f1a | -2.88956 | -53.04425 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 336d6fad-a19d-3a1f-b0ef-b47c558817fa | -2.86975 | -53.346 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb9429e3-12fe-3f34-ab96-65ce3a11d112 | -2.86961 | -53.34278 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8065c2ab-6fdc-3a31-a9ee-5fb5da88d78d | -2.86892 | -53.35126 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| efa24ed3-67e5-3ed1-b2f6-0f7dcf0a11aa | -2.86877 | -53.34788 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b2838c16-1d05-3563-b97c-7edc20201358 | -2.8682 | -53.3302 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1454192e-5614-340d-82aa-db0abe3de8d2 | -2.86817 | -53.327 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5af250dc-8471-381e-a597-91e3509cd267 | -2.86789 | -53.35318 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8cb167f2-d075-3e3b-814f-59f745c1a8e6 | -2.8674 | -53.33521 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40155b76-cbc1-376a-9648-89cd8a5e81b3 | -2.86734 | -53.33204 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f47fa69-ca77-3f74-9903-c998543eaf4e | -2.86661 | -53.34021 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2528361-3cff-3ee5-894f-07520b93ef22 | -2.86651 | -53.33704 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d1c72cf-32ab-3547-96c3-63d72a10e917 | -2.86582 | -53.34525 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40817e10-3520-3d51-8237-ce7df6f45023 | -2.86568 | -53.34204 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3afefc5f-e873-3c73-8640-ed92a37a999e | -2.86498 | -53.35053 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c27cb899-18f6-3eae-95f6-fb4b60eb751f | -2.86484 | -53.34713 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 35e355ec-bc86-3e38-9813-f671ec342721 | -2.86427 | -53.32944 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4304d350-6478-3c01-8041-c576ae63e4ad | -2.86415 | -53.3558 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f909459-21c7-3e0d-a021-25a7a314be8c | -2.86395 | -53.35246 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 231ef57d-187e-356e-80ec-289e9afbed26 | -2.86348 | -53.33444 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c957561-519f-3f42-b36c-e2efd98552ed | -2.86188 | -53.34451 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 303e57cd-3805-3e64-a3a9-9445cf0d6f35 | -2.86104 | -53.34981 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b65d7b10-2536-30e4-8d5c-363b3b24a79f | -2.8602 | -53.35514 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 355eef69-aab8-3e97-b0f7-45a9fe46248d | -2.85954 | -53.33376 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b8ab7c9-e50b-3237-a24d-0260f6be8f6c | -2.85793 | -53.34386 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f70ad3a-3ce7-365f-8631-1d44c55adfe2 | -2.85398 | -53.34322 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02ed67d0-179b-38a1-b60f-b976df5336c7 | -2.85245 | -53.32742 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb9682a6-fdcd-3662-848e-bd7c9a79145b | -2.85003 | -53.34263 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a340e87-e622-350c-ae19-405a05cf4a5c | -2.8485 | -53.32681 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 430a77b1-6088-36ed-9306-ee4f498acacc | -2.84769 | -53.33186 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 286ea272-663b-3e2c-bb62-e016ce7539cb | -2.84525 | -53.3472 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 500e9e8b-be1c-3621-a20b-3c86b1c1a93b | -2.84455 | -53.32619 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fa5d316-8b3f-314e-b1c1-f1fbd6fea050 | -2.84212 | -53.3414 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5189559b-6c1a-36e1-8c64-6102ec43de1b | -2.8413 | -53.34654 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa88fc02-7270-30f0-8dfa-b1471b747ee3 | -2.84031 | -52.55078 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 148743c4-4317-370d-a3d3-f15ae67b35e5 | -2.78903 | -52.48672 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c658a6d9-9d4f-3f31-a2c8-2c136fafa6c8 | -2.78841 | -52.48391 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb6f72c1-89a2-3204-8eb5-30734334e96b | -2.69596 | -52.43716 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372a957e-b996-3fe6-90a4-7f4493beeb22 | -2.69457 | -52.43871 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1acee973-dd38-35ae-9e2c-b55b70b28868 | -3.22455 | -52.18895 | 2024-10-29 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96c493c8-6346-35b6-abbc-183fca5753dd | -3.22431 | -52.60453 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f4a1272-b8f8-3d12-991c-400ebb485ef5 | -3.22355 | -52.60917 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d59a8250-cf2d-33bf-b870-3c078baa6dab | -3.21582 | -53.36851 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d79186d2-6cbd-33af-81b8-8f3f57fc87e8 | -3.20687 | -53.39835 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7c343fc-efee-3eee-95cc-970307238b89 | -3.20605 | -53.40336 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1abc0609-f967-30c9-a682-1782bd0f5b36 | -3.18657 | -52.88306 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1228479b-bdc4-354b-9adc-0aa901ed836a | -3.18275 | -52.88247 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aa5064f-fcf8-391f-a559-efd975660a47 | -3.18079 | -53.16238 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b61caa-4d6c-3839-93d9-7fcbc3bc8e24 | -3.10552 | -53.0526 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d3f0f5d-0f1a-3f0b-8292-d946854a0ea1 | -3.10474 | -53.05751 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91746d6d-98ef-3319-81cb-da6d95d18072 | -3.05771 | -53.25111 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b01dfa27-09bb-3543-8333-8e0eacccdcd3 | -3.053 | -53.25546 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19276ec9-1c32-3001-b6bc-f518cee0738d | -3.04825 | -53.25994 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6444df0a-2638-3037-9adb-284571b71ca2 | -3.04061 | -53.03728 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e863b47-1b87-32ff-bc86-6206dcc8b062 | -3.03946 | -53.03469 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8240c011-9ddb-31ad-8bd9-6028b9d83c7e | -3.0382 | -52.35053 | 2024-10-29 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6559965-10ba-3d85-9b9c-5999f4c0a08f | -2.76125 | -52.06 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d21b9ab8-6899-3cd2-8b93-46ff1cf0df6e | -2.7576 | -52.06079 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cecd85d-eb16-3901-adf0-625a33397daf | -2.75759 | -52.05943 | 2024-10-29 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b66abac-95b0-3dd5-8d32-16e3c3902307 | -3.43676 | -52.48391 | 2024-10-29 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7a4a5de-4e0e-3505-a919-c1fa827abc56 | -3.41618 | -52.83307 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a67552a-57aa-3061-8804-c7fe2b02fdcf | -3.41541 | -52.83777 | 2024-10-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c70403c3-c3d8-3018-93d4-8b4aee50233d | -2.15451 | -52.83504 | 2024-10-29 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fcae740-dfd4-3bdf-9a7c-887e589c1167 | -1.75392 | -54.44545 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 265efc3a-7186-3878-a5c7-ab96551403f8 | -1.74959 | -54.44482 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e0f6a8-e53f-33c6-afdf-de13c9d42cea | -1.71675 | -54.70271 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 076e8349-8a09-3b30-8e7b-f854761503b4 | -1.71368 | -54.52854 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb347769-3c1d-38c7-b30c-94970989b902 | -1.713 | -54.53273 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README52.md)
