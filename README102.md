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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c56ca41d-c8d7-3b3e-aed2-52d284aeacc1 | -2.90192 | -50.71173 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0fc40e82-e739-35cc-8463-a9e6e060633b | -2.90118 | -50.71646 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ca36030b-8ec2-3bf1-947e-2027a9394749 | -2.90107 | -50.70926 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7d44359-b00f-37ff-bf9b-1dc42cf05d74 | -2.90044 | -50.7212 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 44980308-2f6b-3660-b510-9c9615bc5d78 | -2.90037 | -50.714 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5a281f6e-20a7-32ae-887a-172c4407e750 | -2.89966 | -50.71875 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 71c2ed23-d45d-30b6-9784-199c8ca57c39 | -2.89895 | -50.7235 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb579823-8ccf-3de0-af3d-c5b58a75091a | -2.89883 | -50.70641 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f936eac-0541-3b40-8ede-57a933d5b89a | -2.89809 | -50.71114 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e63defbc-c972-3068-9f8e-ed862b5cc1f8 | -2.89795 | -50.70393 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82a7c902-ff4d-3a6e-b4dd-33219aefd897 | -2.89735 | -50.71588 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| b1ea0456-849c-3c5e-b995-9a188134b518 | -2.89724 | -50.70867 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29d24b52-829f-31fb-8ce7-bd47bcb998eb | -2.89661 | -50.7206 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ae16f004-0138-3532-ac16-5fca886db29e | -2.89653 | -50.71342 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 39434beb-2d9a-3adc-96c8-c5b44420da4c | -2.89587 | -50.72533 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3269f2dd-c8bc-31b8-b00c-e72e877e3363 | -2.89583 | -50.71815 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| bfaa7efb-14d3-3f03-88ea-c5e161c3e803 | -2.89512 | -50.72289 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7854941d-46d4-30fd-8e4f-eebbdcbb59f0 | -2.89499 | -50.70582 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 707a5569-4956-3937-90fe-89579d7fcb5e | -2.89426 | -50.71055 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ab08b5a-2a53-30d7-9b20-9a0e76e79504 | -2.89411 | -50.70333 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8688703-db90-32e1-93f9-468f6cc08301 | -2.89352 | -50.71528 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 3f6e39cb-662d-3eff-8f55-d3d995a90730 | -2.89341 | -50.70808 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a23d7df1-48ea-36ce-951e-9e5cf4a97ca8 | -2.89278 | -50.72001 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 3400504d-d24b-33cf-8f9c-8e2059a9b86c | -2.8927 | -50.71283 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 075198d4-6c3d-319a-8710-2859d46bcff1 | -2.89205 | -50.72474 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f895a6dd-13dc-36f6-afe0-1007b1d4d561 | -2.892 | -50.71756 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b4884bfd-a4d1-392a-a435-1030b2e0d45c | -2.89129 | -50.7223 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9e83a3b-5119-368e-91d6-1be7b42ccf9f | -2.89116 | -50.70522 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d77f39b6-ba3e-38d7-84a0-b58ae25c9143 | -2.89042 | -50.70996 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4eb12867-470c-32dc-906a-4006d2fa03f3 | -2.88969 | -50.7147 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f1befbb2-e70f-3186-a193-e06b0a170ef4 | -2.88895 | -50.71942 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f793d0a0-f746-319e-aa00-2db2d77efc71 | -2.88733 | -50.70463 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bb5e2851-3193-3ab0-ac31-9d6b9d7aa93a | -2.88675 | -50.73361 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbd9a7db-61ac-3b7b-a45e-7f93b386dc7d | -2.88659 | -50.70938 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1688b01a-2a56-39a5-97b1-283bbdc626b9 | -2.88586 | -50.71411 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| a7ca03e1-78e3-3d87-8db1-423e4d241dd1 | -2.88513 | -50.71883 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 05204fa9-aa56-3e0b-bd21-74ca43a73f32 | -2.87983 | -50.72768 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7db39ccf-5f6b-3f6f-9e55-cbe8799d666f | -2.8791 | -50.73241 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6feb7f12-a812-398f-a0b0-9f13e5cd9512 | -2.8782 | -50.71294 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 72bc8818-8a2d-3ba1-8b9a-3f3b16d56432 | -2.87673 | -50.72238 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 057b2b5c-d017-3cbd-bcc9-ee6dab397793 | -2.87071 | -50.73598 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 908d30db-b536-3448-8e0d-22288e2a9641 | -2.86689 | -50.73539 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 40097b1d-cd1c-3b73-8d64-7e18b333d0b3 | -2.86525 | -50.72062 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 241.6 |
| 6ba4d303-2f3a-3a23-98a4-a1b155d7d9c1 | -2.86452 | -50.72533 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 241.6 |
| 23e04f59-1d42-3429-b59a-51816c1700e0 | -2.86288 | -50.71056 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 40f55806-90b5-36c1-8d35-01eaffe964af | -2.86142 | -50.72004 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 241.6 |
| 5ebf20e0-4fab-3640-aca7-6fcebdb7c079 | -2.85924 | -50.73419 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d36e9319-db27-3139-9612-a0e86cc99e9d | -2.85905 | -50.70997 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 785ceb7a-f4af-3bad-bbdb-48c3fe168c75 | -2.85542 | -50.73359 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b4b16221-ac05-3277-bb85-ff9d3f37d9cb | -2.85522 | -50.70937 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f18b01b0-7492-3562-ba59-47bb2c8beee9 | -2.85449 | -50.71411 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 360cadd4-fd2a-37de-a287-2f0774f8506d | -2.85377 | -50.71883 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 46b201b8-cd1e-32dd-bd2d-2c1442e966d0 | -2.85232 | -50.72827 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a3c92d1a-910b-3b4c-b943-c0d68d33ad2d | -2.8516 | -50.73299 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f64efbcb-6082-3780-8255-8b4b04299008 | -2.84922 | -50.72298 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| da27e7f0-52f8-3f3e-b016-d08aefbd2969 | -2.8485 | -50.72768 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 27a8f648-b410-3e03-bcb3-3392e56cc453 | -2.84684 | -50.71292 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90a84130-3dd6-329a-b607-7c92973a411f | -2.84611 | -50.71766 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d44c674f-426f-3f59-9f62-48671e5ee5b0 | -2.84539 | -50.72239 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7150086f-115a-3e64-b66c-1a00f6b49301 | -4.15497 | -51.05413 | 2024-10-01 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56dcd515-fd3e-3438-b930-d2ac373a13eb | -4.15228 | -51.0512 | 2024-10-01 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93d8c160-f3cf-3797-8880-76d1c3d289fb | -4.15114 | -51.05361 | 2024-10-01 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e831244-5ea0-31dc-9305-4a70a6e8948d | -4.09895 | -51.11931 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25bcec5c-2590-374a-a1cc-adef4afd32ce | -4.09825 | -51.12397 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97be45c6-12b9-3db1-8e4f-8dfb396faf91 | -4.09445 | -51.12336 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f76e1577-88fa-315a-98d6-3ee5f7a65b5f | -4.09375 | -51.12796 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 808c5d36-d6f3-3610-8c01-dc73e94159b1 | -4.09066 | -51.12274 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6fc4255-163b-3d7d-ac1a-6db4f4223fdf | -3.80396 | -51.4053 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca2bf5e1-41e7-3e14-8680-e3e2082b7eb7 | -3.30091 | -53.6997 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc4b234e-cdb6-30ff-aeea-a05db4eb859d | -3.297 | -53.70274 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc679f9-9570-39a3-a021-c51839e0c222 | -3.24189 | -52.79416 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fa6e914-02d0-39e5-b513-6f080130ebf8 | -3.08121 | -53.06473 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5718134f-e191-31ef-a1bd-f08f9d46de09 | -3.08077 | -53.06524 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7416e752-0397-3b39-932e-f251dacb60a9 | -3.08064 | -53.06847 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f562b172-a7c4-3461-80a9-e6f6d7024181 | -3.08019 | -53.06897 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f208b1ec-0fc6-327f-bd72-2836778db4da | -3.07736 | -53.06473 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f72c419-944b-3b63-86e7-39edf510213b | -2.85636 | -53.31574 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85baae18-2e74-3c00-9b0a-6d147a36621f | -2.8558 | -53.31936 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbefce23-4d8a-38bc-824b-49e17cef98e6 | -2.85468 | -53.3266 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce28c904-4e0c-3613-9b00-79c164534b53 | -2.85298 | -53.31522 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7a1e17-f29c-3d23-9201-17774c6ad41c | -2.76087 | -53.22992 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b5dedb7-6927-3930-82d8-6350d6fadce3 | -2.85242 | -53.31884 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6ee9ff4-e20c-3a1d-b682-0c79233443e3 | -2.8496 | -53.31469 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b9c75c8-f015-374c-bfcb-117dae0b0ecc | -2.84904 | -53.31831 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c99a224e-e5e5-3565-bee8-475bed175b43 | -3.7611 | -52.35734 | 2024-10-01 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce54a680-6c5f-3387-9a49-9a5b3deeb82b | -13.04 | -51.23 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de8f813b-14ab-3b56-ba4d-71d72df43367 | -13.04 | -51.28 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 202d096a-8442-370a-a211-1d42f64752f9 | -13.01 | -51.16 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3884495a-bcbb-323a-9e25-a76dc15019bd | -13.01 | -51.21 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10e71cf0-268c-32c2-87e3-0a349a3550c2 | -13.01 | -51.27 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 683ff9cf-3416-3ec3-88c2-2fd94120d72d | -13.01 | -51.33 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f85dae97-ce52-3fb5-b3a8-978e67269823 | -13.04 | -51.17 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9935dfb-16c6-3b4e-bfc6-4d918dd40777 | -12.98 | -51.26 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ccb7d4f-a50e-3da2-9ee3-1547c961f91f | -12.98 | -51.32 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc03589f-3f04-344d-9a90-ea0a9a475fa1 | -12.98 | -51.2 | 2024-10-01 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15e46070-0686-3297-aa4e-0302bdf58e1e | -2.88 | -50.73 | 2024-10-01 05:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d513e4-4106-37f4-a02f-2a0b5ade1e7f | -2.85 | -50.72 | 2024-10-01 05:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f85a9a-92b3-3cd4-a776-18b95e8b8052 | -11.91495 | -55.91532 | 2024-10-01 05:06:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fab9be0-6d31-3403-a651-083ce63fd53e | -13.28163 | -56.15557 | 2024-10-01 05:06:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 193b6cab-3acc-3955-bed0-1cf752db5f26 | -13.28108 | -56.15919 | 2024-10-01 05:06:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README103.md)
