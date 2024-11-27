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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5bf4995-dc57-3c80-8d92-8245e94d7f55 | -3.31705 | -54.10082 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e7f5681-949a-388a-b099-2be604399517 | -3.52481 | -52.15368 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 208.3 |
| 48875af4-00d3-301d-9b8d-8ca6c1bae4b1 | -3.73683 | -54.27188 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eecaf018-6477-3512-92eb-f29a6f9788e0 | -3.37285 | -50.1067 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8c0e05a-67f9-3740-ba77-12c35cb8d93c | -3.04347 | -53.71873 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9d0790c-7701-3da2-a9dd-7cc817ba09da | -1.99063 | -53.30207 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 84172a20-1170-33c3-9b96-1441a5a9e140 | -2.60038 | -53.97564 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 74ea6f38-7ce3-3e9b-8736-b9fd468dfa1d | -2.80552 | -54.12834 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 655399f6-d0b7-3d1b-828f-682e66efb73c | -1.66515 | -52.42057 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 63537716-227c-3f0c-8f36-c1dc79ade776 | -2.90373 | -54.17379 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 69d725cd-63f8-37a6-91aa-553dd6d6e503 | -3.08273 | -54.1365 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a47429da-6e43-32af-ba89-d9d3738841b1 | -3.77334 | -52.40914 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| faf66cc1-3378-3699-a0e1-e3b3310bd8c2 | -3.50683 | -53.80575 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6a49c7cd-0d8f-397a-89f8-3b6e4dbc0b5c | -3.3296 | -53.72393 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d7dc9f43-d2e8-33ef-bfef-51e3bd6627e1 | -3.24005 | -53.41596 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a72e124d-3493-38f1-a873-d904b37f8ddb | -3.58543 | -53.64244 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d35f5a12-2abc-330e-b615-51fb8853cc9e | -3.28971 | -50.54071 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce40e5c1-08e5-30dc-baf0-ccebead7e7ea | -3.03986 | -54.02781 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| dc937bd0-b2c7-3b5a-9c86-7c57f3e0ef4f | -1.19445 | -51.76046 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d0467a86-1935-3211-91c9-968d6dfd527a | -3.46594 | -50.2517 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12567432-9856-3f1d-bebf-28ad7b4f8687 | -3.45026 | -50.30326 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fff34e92-7f07-3902-a5cf-089f7f9c73cd | -2.6915 | -45.66295 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| a684f174-b1d3-3303-8db9-654628e5dc36 | -1.47081 | -52.47861 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| adce6f9d-1b35-30a5-b2d1-1efc36549c17 | -3.60188 | -51.98089 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aced03c8-4146-34f0-ba5f-bffed51da34f | -2.73793 | -54.10714 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 49540b77-9790-37e0-8382-cfe88a689ddc | -2.54767 | -54.06306 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2780e474-371d-3e9b-b4c3-1bf962a7325b | -3.39709 | -54.28033 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ba9b322-d540-3a6a-b54f-067a9d46f2c7 | -2.02413 | -48.65914 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 88c09c67-dc8c-35b0-84e4-21ec7cfcc514 | -2.86821 | -54.25012 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e145207-9552-340e-8ab1-972de6b20151 | -1.68386 | -52.61879 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05e16061-83ee-3ac1-b2a9-47bbde8b5617 | -2.77314 | -52.90345 | 2024-11-27 01:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2a7793b6-8eee-3bfd-aa3c-b91c7cbcd8a0 | -1.70355 | -52.16922 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd77228a-c3cb-372e-ba7e-e6a882ff13d8 | -1.66241 | -52.53074 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12b6c68b-cc48-3543-8871-85be14ec7c98 | -1.95349 | -45.72366 | 2024-11-27 01:09:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| d048fdaa-f0f5-38f3-9158-2178e18d3a75 | -2.84267 | -46.84303 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fd4a9be8-1c84-3704-a9fb-8980ccb67d62 | -1.79201 | -52.7336 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9b7e9189-2340-361c-9e8e-ab8e5264f262 | -3.09689 | -53.24359 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 14c7f242-368c-390a-8cd2-cd5427711628 | -1.64008 | -52.64041 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 99017abf-6405-3691-8ce3-197913892a88 | -3.16331 | -48.42776 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 053772c9-4be8-3a00-a482-f5c8cf27b469 | -1.27031 | -52.23293 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 757abf76-1a3f-3944-91f0-d705362d6e1e | -3.17437 | -48.42614 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 2a7390aa-fead-3f52-bba9-72253c216ac2 | -1.63675 | -52.48588 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f9cf4e3b-e69d-3619-8d8d-9b2f91aebf75 | -2.23895 | -53.63268 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0fc23e0f-9085-3267-805c-cf651ca5e7e9 | -2.89405 | -54.1717 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f0105ff6-e3a7-38b3-ab2d-2a725ba02e9c | -3.34103 | -51.24012 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e35f0cb6-cc5f-35ca-a198-a3936235fce7 | -1.51892 | -52.62704 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8791423b-4004-34fa-bb19-add66599ac52 | -2.77437 | -52.91227 | 2024-11-27 01:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93e248ee-7867-374e-8655-05316b37c638 | -3.04908 | -48.50871 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 269.6 |
| 8b699901-ce6c-33b2-99f1-d053a9f4cc97 | -4.00997 | -50.3562 | 2024-11-27 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| baea54a4-93f1-3559-869c-6da65bfdee72 | -1.67145 | -52.46549 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19c36e86-bfb2-3592-a1ee-b21995be960d | -3.00948 | -45.47409 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1718f582-4c88-3f0d-b303-7cb0eb38b132 | -2.84056 | -53.98486 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4e3b39f5-e456-3c36-bd0d-2de5cd514d11 | -3.93681 | -47.97668 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 37ca557a-75e2-3ecc-9126-8fe4edb8a5e5 | -1.76773 | -53.62164 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 606d6d69-130f-356c-811f-853b96f640a5 | -1.0658 | -52.41952 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 58099a86-3129-3f41-a031-bd32c564ae1e | -3.52606 | -52.16264 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a67b17e0-87d2-32e0-af94-f61b0ed8b5a1 | -2.85532 | -46.84119 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 384843f0-067b-3b65-8875-058da12f8456 | -2.70072 | -51.98808 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0b598aad-5ea2-38b8-849b-50e13689f9c6 | -3.42154 | -50.4462 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e46f6a28-3ff6-30d5-ab3f-1c5cd4fc4dfc | -1.1874 | -53.8896 | 2024-11-27 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc19955a-c967-38b4-9551-b82b0427f602 | -1.15662 | -53.66893 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f95e12ae-8d93-30cf-89da-faa9d66fa222 | -2.73918 | -54.11622 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fb8b2af4-6fa0-3c02-af70-6e64941b689a | -3.82206 | -52.23904 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16561fc0-f4f1-3af1-8218-74bbfc0b14b1 | -3.71901 | -50.18117 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a05dba49-d06d-344c-b31a-5c03ed679957 | -3.10943 | -53.2688 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c9283634-d8dd-3de9-995f-1bbbbb0be940 | -1.78436 | -52.74372 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4f59fc52-670e-3122-a275-3439e8881b00 | -1.58363 | -52.23555 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1c66af17-6ada-3851-9dd4-950b32a192e8 | -2.82824 | -52.96127 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| afa7259d-eb7b-37a5-9bb8-7a673778e834 | -3.97629 | -48.09206 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 37172756-7a2e-3284-8c71-b901f119c078 | -2.84283 | -49.4045 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8e5ec4b7-1af2-3efd-b643-0284608d8231 | -4.21474 | -50.90637 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| dd4c30c7-e135-33c9-a496-da654d082e68 | -1.7166 | -52.72304 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1801318f-db87-3328-966b-08dcf5e80d91 | -4.12757 | -51.07277 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3f1dd5a-cab9-351d-a3a7-3993367da15e | -3.85042 | -51.38745 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6b7f0d4a-e42b-331d-a2fd-76461f070608 | -1.64817 | -52.50255 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6384a4f5-2a7a-3aed-93e3-d2ae6b7395a9 | -2.92252 | -53.9124 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0e7c79fc-1752-33e0-8003-8679b16d249f | -3.59287 | -50.35625 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| a348398c-fa51-3322-9f51-1972ac12992a | -2.69944 | -51.97896 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 16e046d3-7662-3673-9e35-2c257060a92d | -3.73736 | -54.07667 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a291f56c-1811-3017-829c-643e1e50d207 | -3.6759 | -52.04674 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61e36b35-d966-3f15-b528-d107f1b508a2 | -2.8914 | -51.38383 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 70806a8d-f720-3cef-bfcf-b0d9d81b1ca4 | -2.79679 | -54.06477 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4b1d2e25-67c3-3390-a710-4fdce88fa655 | -2.81455 | -46.82758 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2eef8c7e-20b9-367b-86a5-7164dc48b064 | -3.59735 | -50.3875 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f222954f-ed1e-392a-a81d-1e77f5bac048 | -1.48605 | -52.52222 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0518469b-c2cb-3b96-8177-ba7c04ec0c9f | -3.10093 | -50.3673 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9e0a74c5-0d9d-3a62-8d5e-4945420237d6 | -3.53498 | -52.16135 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5fd2845c-ab2b-3972-a35c-e9e1463b1991 | -3.50807 | -53.81483 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8c6c6931-9c8f-31de-bf20-bf854b96217a | -3.12494 | -53.10793 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 7909935e-575d-3722-8833-9d0610a9e040 | -1.6738 | -46.91027 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0380659c-f94c-3ed1-ad99-b85c66040dac | -3.04013 | -48.52433 | 2024-11-27 01:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 2e391c11-736b-3670-8648-5f7df8e512c7 | -3.24445 | -50.14861 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b358ea1a-1ab8-3489-8994-14d55df6866d | -2.1802 | -52.74468 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87252834-3e31-301a-9abf-291eb11dd800 | -3.96508 | -48.09358 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 06c1924e-3edc-35f1-bf8c-2261c776b836 | -3.22188 | -50.91683 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 36cd9348-2795-3297-8324-1fd165591e7c | -1.62564 | -52.26959 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eb31ab3f-8b88-3f3d-80a9-83e90966d457 | -2.60497 | -54.21217 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25832885-221b-3e91-ad4b-834d22eba781 | -3.49788 | -53.80699 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 85751a8b-9e8f-3b22-8172-b8b89f3a5480 | -4.14478 | -50.41886 | 2024-11-27 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d578ac13-f565-3475-bc13-844fbc1a1b3c | -4.19321 | -50.6894 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README15.md)
