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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e78edde-f788-3374-9f25-9602af34dfe2 | -2.13446 | -50.99471 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9cfa879-9a5f-3275-8506-9067298dc7e4 | -2.13095 | -50.99417 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5a06ef-f089-3868-8083-d1f08490157b | -2.90205 | -50.74509 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3977ebdb-3585-31fb-aa18-fab38fdf6360 | -2.89932 | -50.71765 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db1f26b1-f077-3e3a-946d-247961ec0220 | -2.8992 | -50.74078 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e0c4de2-4053-3d6b-8438-83b9847a02af | -2.8986 | -50.74455 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d14463df-3fca-3ca0-86e3-ad3076c995d4 | -2.89767 | -50.70582 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7adc859a-c457-3572-8002-111057d04ab9 | -2.89588 | -50.71711 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94e49886-196e-307b-a1f8-90a8fc42dea5 | -2.89243 | -50.71656 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d48c39b8-60f2-3880-a02e-71caa404cacc | -2.89077 | -50.70473 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8d20fde-641b-39f5-a006-fd54c34c7055 | -2.88958 | -50.71226 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 556118fc-64d3-3d53-9d42-6c567c2984ad | -2.88614 | -50.71171 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6229dbd4-7fb1-3ca1-a775-2bb0a6e38eaa | -2.88269 | -50.71117 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36a7ccb2-5084-3b13-af35-03d63344ec8d | -2.8761 | -50.75261 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56a04175-8a39-3f95-91c4-fabfa0b4f121 | -2.86305 | -50.7235 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45c6e021-595e-33c7-95c9-10ad5ab288e2 | -2.86081 | -50.71543 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45e66b43-e974-3572-b7b7-47455fe2f409 | -2.86021 | -50.71919 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a814822f-cc37-308e-9189-8de148f2e170 | -2.8596 | -50.72295 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 072d977f-4213-39fb-ae32-dbe6e8ffac5a | -2.85736 | -50.71489 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3f0ebb5-1282-3056-87fd-be0b93408b05 | -2.37516 | -50.50694 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fcd89eb-7ca5-36b3-9246-1dbb8ed28385 | -2.58514 | -51.82508 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33c40815-55d6-395c-89ff-5cdd4e65268f | -2.58476 | -51.92091 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22af5a1c-97c5-3e17-8062-b0d406770ca4 | -2.5815 | -51.82453 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf22a3ea-2fa7-35de-876d-1ba5c40b0111 | -3.29233 | -50.75826 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a2df12e-9272-323c-9664-98d802bc0fe1 | -3.28889 | -50.75772 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad65add-8a9c-37c3-9bed-cc24ea6800de | -3.28473 | -50.69575 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e058dbcc-ac39-340f-a7cc-2bc8df4bc0bc | -3.23507 | -50.83433 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e196114-c05a-3e0d-b09b-2f2e0977803b | -3.23448 | -50.83812 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48ebe6c2-8076-3526-b507-b4abb3d469ec | -3.23162 | -50.83377 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe865415-561a-352f-9f3e-734d73ba606a | -3.22758 | -50.83699 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a9ebf016-efae-3c2b-8aff-5694952ebf94 | -3.22472 | -50.83268 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ae3d8d2-4083-3f83-8518-bdb63b391628 | -3.14973 | -51.30737 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0388b9b9-1beb-32b7-855a-57d11cc3e08d | -3.14291 | -51.28202 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c6f8f47-df37-32a6-a050-84e5761ba9cc | -3.36995 | -51.5156 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 506b1058-8b92-3390-8e9b-8b24e44fba82 | -3.36641 | -51.51502 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 614122d0-3979-30aa-8dce-882fd9bd1efd | -3.30752 | -51.65994 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e307bf3b-e360-3001-9a85-375f96ea5abb | -3.65922 | -50.72263 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 162efbfe-bea3-3ab7-9f2b-c07508fb68d3 | -3.49463 | -50.80869 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3570f271-57b8-3af8-9a2d-8f922f15cbc6 | -3.49402 | -50.81245 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b06c7c1-6a3d-3740-b68e-7688cf3d71c4 | -3.49179 | -50.80439 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95962758-9498-3a76-a8fe-b68348da1980 | -3.49118 | -50.80815 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e888937f-2212-326d-a1e3-0f5c7071e133 | -3.48702 | -51.19061 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 518a95a5-81a5-34b0-a34e-f6a0e6906841 | -3.44482 | -50.65958 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49171c71-0425-33ee-8cff-fbb058f03682 | -3.44423 | -50.66329 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d882f854-f91d-3f32-9633-ae0737c5bc44 | -3.44365 | -50.667 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c5bfa87-5b3d-3951-b6ab-60394fe7c634 | -3.44081 | -50.66274 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b6f0dd7-0d0d-30da-befb-968a9de5b66c | -3.44022 | -50.66645 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c982b455-6efd-337b-80d9-bc014b9bc8f6 | -3.43739 | -50.6622 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 251f73a3-b0e4-3b62-bfb4-aaca60269ea9 | -3.4368 | -50.6659 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17bce42e-49e0-33be-9919-0903577d0457 | -3.43337 | -50.66536 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae201377-eca4-3b24-a334-c82dd1fced0e | -3.43278 | -50.66908 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b6204b9-e44e-3056-ba54-5d56c3add00b | -3.42995 | -50.66481 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e49d1ec2-6b22-3198-ae80-3f8e3575a411 | -3.39809 | -50.97589 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6a11492f-a604-3eef-bf77-c17b5874a703 | -3.29293 | -50.75451 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c965aeef-da49-3fe3-9df6-0f9ad1aa2f3f | -3.29173 | -50.76202 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ba68a7-7c8d-3072-a6e2-55b6907fed1f | -3.28949 | -50.75396 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c43f16b5-c417-3710-a177-89a5d3f4578b | -3.23103 | -50.83755 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c12c2a8-3591-3653-998f-b39ba732c647 | -3.22817 | -50.83323 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e1b7d2b-3b4e-395e-bd02-24742c9596ec | -3.15035 | -51.30344 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 315afe26-2518-38a5-854b-362a98880534 | -2.89992 | -50.71389 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 38208efd-465d-3c9f-b4bc-0d46fbc987e8 | -2.89873 | -50.72141 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa57ca2e-b520-396b-b3b0-9bfe47553174 | -2.898 | -50.74832 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5879be21-1117-3699-a7ac-55c62a58a472 | -2.89707 | -50.70959 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d3f74c54-27d0-3a92-aa80-3120209120a4 | -2.89647 | -50.71334 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ae9c7363-a0bc-3779-b067-6c3df999d918 | -2.89422 | -50.70528 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6675f61a-684d-3bc8-8534-336f7f8b3908 | -2.89362 | -50.70904 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e795d9e2-0120-3885-9a20-3f3ec927123a | -2.89303 | -50.7128 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8c849d6a-9896-3ab2-8fd9-b4f0d116968d | -2.89018 | -50.7085 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| eb10082b-d11a-3278-aa69-b511346882cc | -2.88898 | -50.71602 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f49214b3-ef40-346d-9136-a0de7ef55edb | -2.88673 | -50.70795 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 731bbfdd-0999-3744-bb5f-a1f44332bf89 | -2.88329 | -50.70741 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a73fc5e-609d-3eb8-b8f5-7cf4209bc8a1 | -2.88209 | -50.71493 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85a7c152-6bf6-31aa-bad5-bda0beb29be8 | -2.87924 | -50.71062 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0701c01-a3ce-388c-8ab8-067d42a42d57 | -2.87264 | -50.75206 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e315b87-33fd-39f4-8039-9e53cbfb9020 | -2.86141 | -50.71167 | 2024-10-05 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b88e8931-5a05-321b-9647-4bd345d0002b | -3.88904 | -52.17133 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c4e59b-359f-35e3-83e5-1f30aeae5655 | -3.85583 | -51.93802 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3b9ceea-d4f9-3f76-b9d7-b196f5e4d17c | -3.8529 | -51.93328 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c44c4249-db0b-35da-a464-16c21956aac3 | -3.85223 | -51.93745 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8dd2b60-a3fb-3d6c-905d-ef4d0ace1e69 | -3.76868 | -52.24625 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b45a0f69-ea6a-3640-b925-f3d362d6c02f | -3.7593 | -52.25788 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bbb554c-5349-3575-874f-bee44cc2389b | -3.6177 | -51.90638 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13a5a9ab-4c5a-36c9-89a7-188965c14f5e | -3.6163 | -51.90764 | 2024-10-05 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c18b2674-a653-3d8a-93fe-4c7c749f047f | -3.73515 | -51.36271 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d92b734d-752b-3b42-8ec7-8465658910ac | -3.6841 | -51.16049 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0974ba-d1f2-38f3-9486-5759eeba3b70 | -3.68061 | -51.15994 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e795911-291a-3d0a-9b09-6aa0b843fb83 | -4.63632 | -50.97335 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d33f2a7-4ecb-3987-a048-6b1f03f4670a | -4.05637 | -51.1153 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40057426-6eb6-39f3-9ebc-18afb31ec72f | -4.05291 | -51.11472 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e949751-2fca-3e68-a04e-a8c897668285 | -4.04611 | -51.09042 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be3810d6-fd65-3e95-8734-916a5b125c61 | -4.04551 | -51.09426 | 2024-10-05 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cdcf465-ba19-3e31-ae92-b88d372de44e | -3.85494 | -51.36133 | 2024-10-05 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40820b41-530e-3deb-955a-2605987f06fa | -1.65618 | -52.12968 | 2024-10-05 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90ceeaab-4e3f-3471-af3b-b942c2d1d466 | -3.54443 | -53.02466 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88738d03-df7d-3652-a3c6-2ea57de34a16 | -3.54292 | -53.02211 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1c9a762-1c68-3d55-ad48-f92319673979 | -3.54135 | -53.01917 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f77f24-6af5-37d7-83d1-cd796ba4f048 | -3.54058 | -53.02403 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddef5d32-fd5c-3f52-bd06-de703a112db7 | -3.48075 | -52.83511 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8488508-43ea-3654-88cc-fb91ba964fa8 | -3.45294 | -52.79483 | 2024-10-05 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 764758f0-ce2a-31f6-8d9b-f69864522564 | -3.429 | -52.19172 | 2024-10-05 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README94.md)
