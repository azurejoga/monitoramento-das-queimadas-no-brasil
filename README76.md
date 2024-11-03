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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fa61462-1e98-3702-82e5-ee7493619e19 | -3.43618 | -49.27838 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b3df235-da76-3837-be26-801bc1f1aa4a | -3.43066 | -49.28278 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fbebfa32-6f26-30c9-8bcf-684ade955968 | -3.42092 | -50.22056 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2359250f-772d-39a7-8499-3d73053368f1 | -3.37587 | -50.25572 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a846d7f3-7756-374b-aa68-4ca05ff471ce | -3.3538 | -49.88031 | 2024-11-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a912184d-3e5d-3643-af96-1a517ae1381e | -3.30445 | -50.34099 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c02a25d-3b6e-31d8-b718-3a3e9e9bf583 | -3.30382 | -50.3453 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b89a0d4-3e6e-3fe4-869c-1ee04f49188f | -3.30106 | -50.25092 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a96e7e-94c9-3b42-93af-77caf5f79417 | -3.30041 | -50.34251 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0945c407-5cb8-3269-853b-04c3ce20cde0 | -3.30005 | -50.34035 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ad7b6a-f9ab-30d7-8194-016658d59284 | -3.30002 | -50.24852 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df95b758-0522-3bfe-a1fd-b21ce15e1026 | -3.29974 | -50.34678 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd25dff2-a7fe-3759-bb53-83e288754a8d | -3.29667 | -50.33763 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ac63233-bcf0-3644-84d5-63fba4e77566 | -3.29664 | -50.25027 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6ff83ea-386f-313d-a1f1-2d8925a9ca2e | -3.29565 | -50.33973 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4233a373-7427-35d2-b1f9-c6a0d94b01d3 | -3.27634 | -50.14532 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 579eb08b-15fa-3c0f-9269-2eaeffcc3c21 | -3.25051 | -50.25626 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d61fe862-ce25-3749-b19a-efd3f23c9da0 | -3.20507 | -50.22751 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3022550-0881-3e71-9159-facaea4e62af | -3.20192 | -50.22356 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93f2b27a-61bf-3bb9-a57e-799b2aedbe10 | -3.20127 | -50.22254 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a3b70f7-cfa7-3741-b10a-c616e3be5b16 | -2.97258 | -50.31442 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f87d2ed4-82f7-32b2-8954-3cb4083f1718 | -2.97252 | -50.31702 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e23347f8-11a7-3a2d-a40b-2ce33e886a06 | -2.96875 | -50.31218 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb70db26-726b-3a2c-9e6f-845a551fc9f3 | -2.96511 | -50.30473 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c42d9172-6ec7-3795-8665-df54982c92e4 | -2.94412 | -50.23657 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0711581-4b7d-33ec-9a74-91e62ab11bc0 | -2.94347 | -50.24082 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 379a26de-0e7f-38c5-9f9d-97ae86927c53 | -2.94282 | -50.24507 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9100dbdb-f0da-3108-9865-e16e76949540 | -2.94218 | -50.24929 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 079e18e1-5e25-390f-a138-8b725cc40888 | -2.94154 | -50.2535 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 299dc67f-48b2-3dc7-a721-f4c09c5b0091 | -2.94089 | -50.25773 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e975f4f4-a3e3-318d-aed6-7d9af31192c8 | -2.94025 | -50.26197 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| affeca9e-cf2a-384c-acb4-e11a924ca31c | -2.93972 | -50.2359 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5525ddbe-a212-3395-a4f2-87c8136b23aa | -2.93907 | -50.24015 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7b2be071-9494-321c-8853-5f79d35fb42f | -2.93842 | -50.24441 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| dc5d8c8d-30e4-316a-af7b-cfb63bcecb46 | -2.93778 | -50.24863 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d49901dd-a0c3-3fef-8c4a-e43afce64cc9 | -2.93714 | -50.25283 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c4e34d56-adaa-3a78-9b68-46137d5aa345 | -2.9365 | -50.25705 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 8aca9b35-ac4c-3c35-90ed-ef3d391503e0 | -2.93585 | -50.26129 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4674d20a-315a-3ae0-858a-2488959780cc | -2.93532 | -50.2352 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3be23711-79e0-3afd-bf61-1e20dfbabd42 | -2.93521 | -50.26554 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f9a615fa-475b-3f55-8535-3afcd41e21e2 | -2.93467 | -50.23947 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 92bba686-0303-3607-8f94-74d9104d73f2 | -2.93402 | -50.24373 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3be28398-1825-3d30-b813-c99db117de60 | -2.93338 | -50.24797 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e2502cee-f9e9-38dc-b486-8342f98eb59e | -2.93274 | -50.25219 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 65fc9f55-92b8-3c6c-a548-9db37c067542 | -2.9321 | -50.25641 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 36aa53b5-d19f-346d-bbee-a5f439147a04 | -2.93146 | -50.26062 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b6946604-38fb-309c-9db2-a575df359cf2 | -2.93092 | -50.2345 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6decf89b-7007-3b0f-9423-4f434371417b | -2.93082 | -50.26485 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f864e637-c31f-321d-b19c-2f410ce4f40f | -2.93027 | -50.23878 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7fe90864-d628-395a-ace1-2b075d7dcbb8 | -2.92963 | -50.24305 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01150aee-141e-30cd-b1d9-d62c109c7aa1 | -2.92898 | -50.24731 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79359d07-ed71-330e-acff-3f9415592f67 | -2.92834 | -50.25154 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 598e8783-00d9-3ac5-8b96-cf9146bba3bf | -2.92523 | -50.24234 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d302bd18-410b-3f45-9b61-1992b715d61e | -2.92459 | -50.24661 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ad81ab7-e057-3089-a9bc-1427e28b126e | -2.89609 | -50.46426 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8158a936-8c6a-3a1d-8813-d643d802bd9f | -2.89237 | -50.45958 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f191c10-4235-3f92-917e-5e10ea7f012b | -2.89175 | -50.46365 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| edebe374-1ab3-3e77-a4d6-fb48e33a5b4b | -2.89113 | -50.46772 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 415a29b2-c795-3b7f-902a-59cf86cf6cbd | -2.88803 | -50.45898 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5ed42082-12b6-3067-9874-3d3317044dde | -2.88741 | -50.46306 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c8410c0-9c1c-3831-87f9-99128d862e1d | -2.8868 | -50.46707 | 2024-11-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| edc6a6e4-9057-33c2-9ce0-6d5249375742 | -2.67553 | -49.82539 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44e39e6d-13ab-36ce-8d22-60ec77f474f5 | -2.67485 | -49.82986 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2f8d7fb-a009-33f2-badc-ee72dc73d29e | -2.60936 | -49.79471 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5015167a-7b58-38e3-9bf2-c30f3195e3e9 | -2.60484 | -49.79406 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c5ea038-d9bf-3b79-8afc-e6b1d4b25a3d | -2.59963 | -49.79789 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8410b33-6f04-39f0-8525-1690d7b3679f | -2.57707 | -49.79441 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e220f785-368a-3975-89ea-8d22f320f94e | -2.56598 | -49.80657 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7877f9b2-448f-3449-9d0c-cb3defa55196 | -2.56012 | -49.81482 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 23032d32-7667-339f-bfd8-43557c090865 | -2.55944 | -49.81931 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4fbf54dd-6585-3df5-98b7-90e7eef4f2df | -2.55562 | -49.81411 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 60c74b00-d6f3-3b58-b3a3-44b57228c455 | -2.48028 | -49.84632 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc216f3e-ef9b-3b0e-af50-0dadfc320c8a | -2.47509 | -49.85017 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34f7485f-662a-3730-ad13-334c0bc78900 | -2.43511 | -49.78007 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57c1170c-878c-3dbb-9f12-989775ca2879 | -2.43445 | -49.78451 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe8f70b3-5370-3ccd-8501-ec2374d846f6 | -2.43061 | -49.77936 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2d23a8a-c809-33fc-97b1-985a3d633d24 | -2.4261 | -49.77864 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97d4ecff-ed20-353f-8e81-0b1d98c2d4c8 | -2.42544 | -49.78311 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6df5225-fcc6-3533-baa1-ee8ce8255d8d | -2.40821 | -50.01936 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1289464d-eaaa-370e-9df1-1dd5f1a26688 | -2.40443 | -50.01435 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1373b6-459c-30bf-8d3a-47c1e28a5668 | -2.40378 | -50.01868 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af8eaea7-259f-3f87-b3f5-a36b03611aa9 | -2.24947 | -49.82827 | 2024-11-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0be9c9a6-3d8b-3363-9001-b0bd957fa536 | -2.23051 | -50.27491 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca592515-754c-320e-a479-ed70bc2fbb67 | -2.22969 | -50.27549 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4c2fc62-d17f-34ca-9a24-5258932f1cfc | -2.22617 | -50.27425 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f823ac74-066a-3677-8328-c467edef8465 | -2.22555 | -50.27837 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3b77e55-c2ec-30ac-8e9a-1ff53319bbaa | -2.22535 | -50.27484 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4298a3-b68b-3a92-9a8b-038ab027ffc3 | -2.2247 | -50.27895 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 650cafeb-96c5-33bd-b2de-da9a70c4d3fb | -2.22121 | -50.2777 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20bf1e1f-ef75-32aa-903a-c07074cc90e7 | -2.22036 | -50.27829 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 648b3ca2-a7c7-379b-a0fd-abc52c96c37e | -2.54678 | -49.29022 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4f4b2051-86be-3d09-8ca9-0a149873e7af | -2.54604 | -49.29511 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ce3f9bc1-981b-32f2-b884-d2731589b125 | -2.54262 | -49.2546 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea81f45e-5260-3865-a006-5a0210f971aa | -2.54211 | -49.28953 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cde9bf9e-553a-3266-a0c1-0940d7ac2574 | -2.54189 | -49.25946 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62b3949b-2102-394b-9391-59bee6d5e46b | -2.54137 | -49.2944 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7164d4d5-fffe-3f74-bf05-7a90b0766f79 | -2.53793 | -49.25392 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8271979-fef0-3a4d-8268-b868edca9e32 | -2.53743 | -49.28884 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb3cdbfc-8af6-3e48-8b35-28b782c80b4b | -2.5372 | -49.25876 | 2024-11-03 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 996c64b6-583f-3d61-8859-78a9a95abb03 | -2.53325 | -49.25321 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README77.md)
