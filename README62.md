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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07cd659a-69b1-37db-a0cf-0726504ea2f5 | -2.85954 | -50.77026 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0a1b49e-e3f6-3352-93a3-d51e2c846c9e | -2.85922 | -50.78598 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0807763-cfae-3834-a7f9-c58b8ddd7a1c | -2.85854 | -50.77644 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ded41cb-4702-3b12-993d-8b416852dbfe | -2.85754 | -50.78263 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 064da960-1452-3e05-b7ec-0ebdf9deb889 | -2.85439 | -50.76944 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dd03ff6c-b74b-31a1-aff3-e31e175f54c1 | -2.8539 | -50.77251 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05423a7d-d508-3e75-b849-fa1b456561f3 | -2.8534 | -50.77559 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afaf2385-5cd7-36f9-a995-6aa37d955728 | -2.8529 | -50.77866 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c3b66d6-dfb2-3674-9698-11e98a45a4a0 | -2.8524 | -50.78175 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3735ad6-a922-3b14-8931-67299581be6c | -2.85042 | -50.79399 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88847a2d-d5c6-32b8-a99f-b53e75e56385 | -2.84944 | -50.80007 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e6bdbdd-6605-375a-848c-f47fd17e9789 | -2.84826 | -50.77475 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a351c95f-92d3-3e3c-9e23-5bb9a583a597 | -2.84676 | -50.78398 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0dfd754-13ba-3915-89f4-e34a8c61b3b8 | -2.84577 | -50.79011 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8b4ac71-a280-380c-92f5-7055979b7532 | -2.84527 | -50.79314 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42304064-8b67-3c59-a3c3-9fbea09a3752 | -2.84478 | -50.79619 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcb501a9-64f2-3912-b97c-0a150aacd7c1 | -2.84313 | -50.77387 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e906eed6-61b5-3a6d-b5a8-d3c0f753bba7 | -2.84213 | -50.78001 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31df2178-c83e-3f62-a322-b82e96c40fb8 | -2.84162 | -50.78311 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8a8279b-db03-3221-b7c2-294eaffdc545 | -2.84013 | -50.79228 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 305e4b7a-108b-3d33-acf6-5b0c0fbb0666 | -2.83964 | -50.7953 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ed38b2a-d66d-3e65-b92b-c1eea4fe2fee | -2.83914 | -50.79835 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d167c4d-22b2-3e61-b616-2296e52df556 | -2.83865 | -50.80141 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d86e0163-aebf-3aec-9309-271ff9ab0a52 | -2.83799 | -50.77297 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 82a67381-760e-3e5a-85d8-864ad64f7594 | -2.83749 | -50.77605 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72b814f8-d983-31b2-93e5-e21b15ba3349 | -2.83699 | -50.77914 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74bf3bee-0504-3f23-a763-23fe07789eb1 | -2.83648 | -50.78224 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76730c23-f82f-318e-bd0c-0f1c03ea9e25 | -2.83598 | -50.78532 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4e762f5-6cfc-309d-9f51-2436bc8ed576 | -2.83548 | -50.78839 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bf80438-a0ea-3b07-b170-9c5f4afa154a | -2.83399 | -50.79754 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9196ace-2973-3e35-8af0-3ff312825664 | -2.83349 | -50.80059 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b92776d5-6d24-33d5-a513-1c2ae40976a6 | -2.83235 | -50.77518 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aee64a22-acd8-3d8f-9949-254e9fbfeb85 | -2.83185 | -50.77826 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecfdc083-e8d7-33b3-9d20-c42a8206ec0e | -2.83135 | -50.78134 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3151cefb-5442-3047-87f2-e3ec4fcb3945 | -2.83085 | -50.7844 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 276f8c6c-9c3e-38fe-b8c6-2552061ed52d | -2.67932 | -51.71014 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 770979b3-31d0-3848-b251-35b18d1b866e | -2.67873 | -51.71375 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a8348ae-7019-399e-addc-dc4ddf875270 | -2.58095 | -51.9259 | 2024-10-01 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ea3c02-7139-3f8a-93cd-d9fa2b48fca8 | -2.87465 | -50.72588 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43cd0223-159b-31b9-9d4c-1f49b62caa9f | -2.87447 | -50.71029 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74652176-2b95-33a4-8289-43f39f326791 | -2.87414 | -50.72891 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3be0a67-a245-34ba-a247-9cc73cab895d | -2.87363 | -50.73192 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c889f9d6-720d-3b5c-9122-98b9115a5c36 | -2.8735 | -50.71635 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e140cb14-7390-364b-a7a8-eaeb8cdd01f8 | -2.87313 | -50.73492 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a014b640-87a8-3f64-827b-a598fa7500e2 | -2.87252 | -50.72244 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4962901f-8ed8-3020-801b-583d4c621502 | -2.87202 | -50.72549 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64b135b5-1a19-391d-9874-1ce696e3296b | -2.87159 | -50.7129 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fca5435-8314-36b2-9940-9a34e97306db | -2.87153 | -50.72853 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b15c389f-5005-3649-81de-c30d538c81b4 | -2.87108 | -50.71592 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfa5365a-bbee-3edd-9ff6-dfe2d50baea9 | -2.87105 | -50.73155 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 48bff2fc-edca-3942-af15-12ff758cc8d5 | -2.87056 | -50.73455 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f52f8bda-9a12-3f02-b522-00b1d9a8734d | -2.87056 | -50.71895 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c4d83d1-0a3f-32e0-9f24-04b4aeb891a2 | -2.86954 | -50.72503 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 835bfb73-48c5-395c-9924-dd20b59400ab | -2.86902 | -50.72807 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3bc157d-84a5-3526-a53a-db2dcf2ebc02 | -2.86851 | -50.73107 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d637d5d-78fc-398c-8f71-393ef7274efe | -2.86838 | -50.71549 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dda72eb-864b-3bd7-aea4-655a22b7a3e3 | -2.86801 | -50.73407 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 97d8fc34-8dbc-37de-903a-a40b27a151bd | -2.86691 | -50.72461 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec9c1254-f919-31c7-845d-28d9bbb6f22c | -2.86642 | -50.72766 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 64ce1c0e-3971-3cdd-950c-c62faa63e41c | -2.86593 | -50.73069 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a47aa71-c2da-39a3-9315-2680b5ed6eb3 | -2.86544 | -50.7337 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b573f12b-2d75-3fec-b2a2-8df27021ea90 | -2.86375 | -50.71161 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dbc127d-5e4b-3383-88b1-9dff9a5809e3 | -2.86326 | -50.71464 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a3a82fd-aae2-32a9-afe3-add672bfd077 | -2.86229 | -50.72068 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 616b235b-bfd2-34ef-b5ea-9b7dc6eaa234 | -2.86179 | -50.72373 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cec5f2ea-8ad8-3c84-aac9-0f74e33aed30 | -2.8613 | -50.72679 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3e8eaed-af18-3307-b5fa-9a232c2e03e5 | -2.8608 | -50.72984 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 926248b4-258a-3050-951f-6e1136694e28 | -2.86032 | -50.73285 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e84e33ee-30e7-3e8e-9637-a1ea86cbccb2 | -2.85815 | -50.71378 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18910320-12d4-33cf-a9b7-065768963653 | -2.85717 | -50.71985 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e0d62d7-2484-3fc5-9cd2-94ef2843150a | -2.85667 | -50.72289 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94c7a34c-82ac-3868-8ac4-ea8c65e93caf | -2.85618 | -50.72593 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46ec3022-28a7-3ccf-9782-8dc6e2d22e47 | -2.85568 | -50.72898 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 04bb1814-a89c-3f05-b615-deb60ffe6d77 | -2.85519 | -50.73201 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36de1fc7-38a9-362d-8b44-7dc56bb44048 | -2.8547 | -50.73504 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 520966dd-4350-30b4-b2c1-f1865cab8fa0 | -2.85056 | -50.72813 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aedc64e0-0439-3b39-a761-697698971e98 | -2.85007 | -50.73117 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4087499-de8e-303a-abfb-d9d2f8f2782d | -2.84958 | -50.73419 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be90f236-0beb-382d-a41e-739ca709b8aa | -2.91198 | -50.72273 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd854bbe-498a-39b3-ae9c-cc18793c4b8b | -2.91148 | -50.72576 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fde64d5d-9aa2-3a23-b575-de5e7458fd0d | -2.91098 | -50.72879 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a56a1a2-bbf7-3a0b-84ff-a21ca70de6a2 | -2.90687 | -50.72186 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44bfc798-fcea-3644-ae18-9b5a0e79c0a6 | -2.90637 | -50.7249 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ac4efd4e-4ade-32b1-a567-9d31092b3450 | -2.90586 | -50.72792 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dfd1a1ce-3004-399f-98ee-a22994469d7f | -2.90536 | -50.73095 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 28202541-12c5-3bc4-9c9f-b7fdfdb55a31 | -2.90486 | -50.73398 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 321ceffa-1ca1-3a87-8a3b-65943992586d | -2.90276 | -50.715 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4369213-9d3c-3ea9-a31c-3d5929e5ec20 | -2.90226 | -50.71801 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec382c36-81f1-3632-aac6-aaaa69497297 | -2.90125 | -50.72404 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2d4e9cb2-5943-3053-b90b-f7b3a011e3f0 | -2.90075 | -50.72707 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a5fc584-be96-36cf-b815-aeb4548b948b | -2.90024 | -50.7301 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd3fdbb7-a28f-3b9b-843a-e241b2a6d8cd | -2.89974 | -50.73313 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 316987de-adba-383e-b6c6-72192860fa49 | -2.89765 | -50.71415 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2f034db-34c8-3c9d-857f-565b68acee6c | -2.89715 | -50.71716 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e79879a2-a2da-30dc-86e7-d075424dcb7d | -2.89664 | -50.72019 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 77231282-58b6-3bee-967c-8022d54ca61d | -2.89614 | -50.72322 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 74595e41-53d7-3026-88d0-c2d5cc7d3282 | -2.89563 | -50.72623 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 40c0eb44-f74d-381c-9715-f3dbe0bf420b | -2.89513 | -50.72925 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 381fdaa5-b9fe-3d2d-a2cf-699de829217d | -2.89462 | -50.73228 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 423d2113-abfb-3840-b0f4-a6f427fc7db6 | -2.89411 | -50.73531 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |


[Clique aqui para ver as próximas entradas](README63.md)
