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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78a981d3-d9a4-39be-bc90-65db66f0ee74 | -11.4828 | -58.5159 | 2026-08-31 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 90586973-2578-38f9-b0bc-089e1018967b | -11.3611 | -45.2185 | 2026-08-31 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 328.6 |
| 0a534e7f-283e-3b50-820b-1a9871e114dd | -5.2548 | -55.8907 | 2026-08-31 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 24b8a723-99a8-38a2-bf39-4b7d92a64d03 | -5.2362 | -55.9112 | 2026-08-31 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 8fe29c4e-203e-330e-8c41-089b3227cf0a | -7.9236 | -44.2558 | 2026-08-31 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| fa146760-b365-3998-83bf-0f1320d2598d | -5.2546 | -55.9303 | 2026-08-31 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| efb1f394-38b3-3744-a5dc-0c7615184eb4 | -1.6042 | -54.415 | 2026-08-31 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c32758b9-31a1-3d83-96c7-ef905b783563 | -6.77 | -55.6445 | 2026-08-31 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 46e0de5d-5905-3b12-a78b-18c94e973087 | -11.3615 | -45.1955 | 2026-08-31 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 2e2889b9-a343-36d8-a465-9f5de8534c49 | -11.3798 | -45.2389 | 2026-08-31 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c08ae1a0-cc3f-3e08-a452-f5f0981ac18b | -5.2362 | -55.9112 | 2026-08-31 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| f4b22d2d-2a0c-329d-b466-7a4d4539f3eb | -6.6035 | -58.6166 | 2026-08-31 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 421e4ddf-0ea6-3041-816a-0b28f4d9b583 | -7.3302 | -60.589 | 2026-08-31 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b0eeee01-e9a0-3faf-aa1e-b423ba0bf190 | -7.9236 | -44.2558 | 2026-08-31 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5b668194-6a31-3653-ba2e-0f43395f2c67 | -10.8253 | -45.3152 | 2026-08-31 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d54dcd25-4618-3357-9405-0c45a09318ed | -6.77 | -55.6445 | 2026-08-31 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| ebff8bce-b9ae-3303-bae1-e1fc8b6c765e | -7.9425 | -44.2538 | 2026-08-31 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 46b4a127-f25b-3ea8-a5af-af11aef3d91a | -11.3611 | -45.2185 | 2026-08-31 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ef8665a6-1cf0-3554-9a20-63f382852e80 | -15.4231 | -52.7049 | 2026-08-31 02:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6ee1cba0-ddb6-30b9-9bbe-138b9263621f | -6.6036 | -58.5972 | 2026-08-31 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 64ac03f9-f787-346c-bf66-3900a935bf11 | -5.2547 | -55.9105 | 2026-08-31 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 216.6 |
| efeb6004-0d61-3ee8-99ae-7dab6a549193 | -18.2904 | -52.6818 | 2026-08-31 02:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ead51d21-87a6-3d6e-ae30-796a80e10735 | -11.4828 | -58.5159 | 2026-08-31 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d5464faf-30d8-3e3f-9790-d2e48fe659a6 | -11.3615 | -45.1955 | 2026-08-31 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 667b4b38-2a90-336e-99c1-30f62daa5364 | -5.2363 | -55.8914 | 2026-08-31 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 086175ce-2c31-380e-991f-be5a97401eec | -5.2548 | -55.8907 | 2026-08-31 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| f73b2787-3de3-395b-ab0c-5d9c501e7d51 | -5.2546 | -55.9303 | 2026-08-31 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d419bfcb-c8de-3cc4-a2da-11a5bae8f22c | -13.3831 | -41.3311 | 2026-08-31 02:40:00 | GOES-19 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 43.2 |
| 4aec06b7-dec0-3fde-92ea-2c2c1d5d827a | -11.3615 | -45.1955 | 2026-08-31 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4076ce82-6840-377c-bf88-2fdac5ce4dd0 | -6.6035 | -58.6166 | 2026-08-31 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9f6391d4-58cd-3f4d-b59e-3f22a692b0b6 | -15.4231 | -52.7049 | 2026-08-31 02:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f4ed2a83-d9b6-3ea2-ac28-3730ca85d95a | -1.5859 | -54.4153 | 2026-08-31 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d015d599-043d-32aa-bac9-8cb77f821ac9 | -1.5859 | -54.3953 | 2026-08-31 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| df42019a-b133-39bf-b497-2f636ca81ff9 | -6.77 | -55.6445 | 2026-08-31 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 92431091-6f5f-393f-bddb-af6067b386ef | -7.9236 | -44.2558 | 2026-08-31 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 746a230c-bbfe-3c64-9625-2e0a4add04b4 | -1.6042 | -54.395 | 2026-08-31 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5a3ed87a-148c-314d-a670-e4371fa45cf7 | -10.746 | -50.6386 | 2026-08-31 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c36d59e3-3101-35f7-b7bf-b17bed970539 | -6.1294 | -57.6833 | 2026-08-31 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 8fe952df-8177-39d7-a525-438c3bd3e7d2 | -5.2547 | -55.9105 | 2026-08-31 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 259.7 |
| 508ff288-80af-3664-8830-add5bb18acec | -5.2548 | -55.8907 | 2026-08-31 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| ae0d4495-b675-3257-9bb4-e6097cee8467 | -5.2363 | -55.8914 | 2026-08-31 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7a639cca-1bf9-33db-b5ca-3ebff370fde0 | -5.2546 | -55.9303 | 2026-08-31 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| cbd3f22f-d7ae-3c15-a09e-f94ae945a3f3 | -6.1295 | -57.6637 | 2026-08-31 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 0b5da337-3f2c-30bc-acc4-f4adfd26366a | -11.3611 | -45.2185 | 2026-08-31 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 8289e4be-03b6-3dd7-90a6-f9908ffabeac | -6.6036 | -58.5972 | 2026-08-31 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 7adcdc4d-df79-3faa-9b7d-b8e671c0d2f8 | -5.2362 | -55.9112 | 2026-08-31 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 60140119-c355-3688-8335-2fb3ff1f33c3 | -1.6042 | -54.415 | 2026-08-31 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| cd864349-9eb3-3456-ad95-5fffd2e928d4 | -6.1295 | -57.6637 | 2026-08-31 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eeb1a0c3-7daa-3668-8505-40029e7b8018 | -6.1294 | -57.6833 | 2026-08-31 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c1f21eca-5922-3eb0-9af5-cac36aa613c3 | -5.2547 | -55.9105 | 2026-08-31 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 251.5 |
| ce37ada2-98d0-31fc-9252-d2ddd29cf6a5 | -1.6042 | -54.415 | 2026-08-31 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8bffc797-b3ed-3911-89a3-ba87672fe6c8 | -5.2546 | -55.9303 | 2026-08-31 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f2bd8923-060c-39c6-b5dd-67e09d7ebaf1 | -1.6042 | -54.395 | 2026-08-31 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0e3cf800-8ee3-3fad-aeae-e9603871e96f | -6.77 | -55.6445 | 2026-08-31 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 366e0755-5b84-3b8f-b1c8-b2ab140ca3c2 | -6.1111 | -57.6645 | 2026-08-31 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 274f347f-3953-38ea-8763-7a1e0e767c78 | -13.9474 | -54.4179 | 2026-08-31 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5e678986-31fc-39f0-8835-bdcfdd87ceeb | -11.5017 | -58.5145 | 2026-08-31 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 50d120e3-9e76-32fa-8818-7436f9993ac6 | -6.7702 | -55.6246 | 2026-08-31 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 4a3de9ca-cdbe-318a-bb93-b1d7f3a3411a | -5.2362 | -55.9112 | 2026-08-31 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2160b2d6-157e-341e-8b76-c02f7b44c814 | -7.9425 | -44.2538 | 2026-08-31 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4e3b2f7a-072e-3f82-a59d-53fdfd9f710a | -6.622 | -58.5965 | 2026-08-31 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1a0f8a58-55b7-3b5b-a4a4-6d88b3b38cce | -6.1109 | -57.684 | 2026-08-31 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f8292226-3760-3a5a-8e1c-7b8bbea480ee | -1.5859 | -54.4153 | 2026-08-31 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 0f43a76c-0af1-3349-82a5-3560aabfd3c5 | -5.2548 | -55.8907 | 2026-08-31 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 6b9c6dd8-f37d-304c-bf67-0e867c24b512 | -18.2904 | -52.6818 | 2026-08-31 03:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 613b51ce-faf0-3a05-a069-2dc4d7524cb7 | -1.5859 | -54.3953 | 2026-08-31 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 8102de8e-4482-3c36-bbf9-b4234fb00b61 | -6.6035 | -58.6166 | 2026-08-31 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 521c0961-6bea-3f49-8326-07e29d3b5bcc | -7.9239 | -44.2327 | 2026-08-31 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 83b7863a-33c7-34e3-bdd4-fb66ffb73f0c | -6.6036 | -58.5972 | 2026-08-31 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 96d72e9d-3055-3838-abc7-bdba070664d0 | -7.9236 | -44.2558 | 2026-08-31 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 1eb04f47-e94f-3ff2-b3af-f8450278a8bd | -6.1109 | -57.684 | 2026-08-31 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d8fa409a-3e00-320d-9ed1-75f7012388c2 | -5.2546 | -55.9303 | 2026-08-31 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 391ec379-5552-3bfa-89d8-eb7fecbc6f11 | -6.1295 | -57.6637 | 2026-08-31 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a51a26ab-792d-3ac8-ba65-19ba36f8b0a5 | -6.1111 | -57.6645 | 2026-08-31 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7e2b2850-45e7-3f1e-ba3f-9bc1e27a666f | -20.3703 | -47.4481 | 2026-08-31 03:10:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 2d9fdedc-ae0f-3862-a431-22a9e0978ed7 | -1.5859 | -54.3953 | 2026-08-31 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f2ba8e7f-40df-361b-a55a-4e588d78f9f7 | -6.6036 | -58.5972 | 2026-08-31 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 57e13b07-22a5-3179-90f1-4b0929383553 | -7.9236 | -44.2558 | 2026-08-31 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f1527014-73db-3bb1-96cb-f5eb60b8d79e | -18.2904 | -52.6818 | 2026-08-31 03:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 450ecc16-db64-3252-a3fe-ea680e3a9213 | -7.9425 | -44.2538 | 2026-08-31 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b8f745f8-fa14-3552-a8a5-c9ed94cb375b | -5.2547 | -55.9105 | 2026-08-31 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 232.0 |
| 7452ce00-c520-3a9e-8f9a-a367391a53fa | -5.2548 | -55.8907 | 2026-08-31 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| a9671df6-d995-3c23-b9e5-ea029f365eed | -6.1294 | -57.6833 | 2026-08-31 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 45d6239f-6dd2-3326-8c81-8a9e7debf077 | -6.622 | -58.5965 | 2026-08-31 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a011d910-d192-37d3-8450-1b64e1057c7f | -7.9239 | -44.2327 | 2026-08-31 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 984c86bb-5be6-3419-ba67-37cc185606ba | -15.4231 | -52.7049 | 2026-08-31 03:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1686b602-09d0-39bd-87dd-7245e78a6d2f | -1.6042 | -54.415 | 2026-08-31 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| db0ad6ce-6cff-3788-a665-2964602d85e1 | -6.77 | -55.6445 | 2026-08-31 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 86f76dda-63d9-32e8-89f4-1dc194b3afb5 | -1.6042 | -54.395 | 2026-08-31 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 676bdada-c4ee-34a6-b5cb-b32f19cf859d | -5.2362 | -55.9112 | 2026-08-31 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7b90416e-0071-36fa-a8fc-9ca312acf9f2 | -6.6035 | -58.6166 | 2026-08-31 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 0ba0aea2-5911-3769-83e9-b2caad015113 | -6.7702 | -55.6246 | 2026-08-31 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| dba0157b-7fcf-3e54-81ed-f922516181a0 | -5.2363 | -55.8914 | 2026-08-31 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3b337b2c-080c-3f68-b349-2bc8f92bee53 | -1.5859 | -54.4153 | 2026-08-31 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3aceee99-3177-3d56-bfd3-55d0d829d369 | -9.00247 | -39.88197 | 2026-08-31 03:17:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b6221d92-09ce-3cde-b51c-d0a476dab0c5 | -9.00173 | -39.88591 | 2026-08-31 03:17:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4cee1cd9-6f2d-375c-b561-9e47c757a38c | -9.00743 | -39.88691 | 2026-08-31 03:17:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0bbd1d26-8b27-3645-a183-382ee593d43d | -6.33785 | -38.93603 | 2026-08-31 03:17:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93696506-1e91-3e65-bb94-61282d4394b9 | -6.33853 | -38.93218 | 2026-08-31 03:17:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97addf5d-fd6d-3355-b433-f3c993343d56 | -7.1094 | -42.76387 | 2026-08-31 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
