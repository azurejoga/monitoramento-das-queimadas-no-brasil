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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1e47b77-4ced-356c-b8f7-0b728d32bd88 | -9.10799 | -51.53373 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3878db52-c630-3ba8-834c-bae46f0365e7 | -9.10564 | -51.52452 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27efefd2-3f40-3ca9-b076-a0e13ed5596d | -9.10501 | -51.52884 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb3843ae-ad45-3923-adad-ada2aa33f82d | -9.10438 | -51.53313 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e330254-fa95-3e59-8132-91f0c20c591b | -9.10204 | -51.52389 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| baa4e1c2-7313-3e3c-b11d-73026ade2d45 | -9.10141 | -51.52819 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5a1a59b-aba5-3617-b037-b90933ef9e2f | -9.10079 | -51.53245 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8ed4fd4-5e76-34b0-8ff7-ce48af95db08 | -9.03674 | -51.53221 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e88a45e-b9bf-3b89-8b19-2c8d082eaa19 | -8.68975 | -51.70481 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73649aa4-64ce-36d2-a5fe-2571ddaf5dca | -8.68618 | -51.70432 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5054175-c451-30d8-9300-1e709a0d3648 | -8.37791 | -51.63947 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3461638b-f6d4-34f8-b209-017c6c151175 | -8.37726 | -51.64379 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34156658-fd6f-3ee1-a3c4-d0e053842bce | -8.37369 | -51.64326 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7aaaadb-e70d-3d7f-a0d4-11e9b6ba2ffa | -8.10798 | -51.12149 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a55e779-08b8-3b42-b962-bb852ed83b2f | -8.09523 | -51.10671 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df6ce458-9140-38b0-911e-08f12ef46b2e | -8.08673 | -51.11382 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9965b85-a714-342f-b258-3e229b81e671 | -8.08359 | -51.1352 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31219a5d-59e7-3137-9595-7350de24f18f | -8.08234 | -51.14372 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25a419d7-6378-3d14-b463-73066ea46c6e | -8.08172 | -51.14794 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2702a542-137e-316f-96e2-c3f95e795d3c | -8.07807 | -51.14742 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b1429b-a78b-3562-ac97-34769aa5d651 | -8.07757 | -51.12541 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71d2789b-4c46-3506-8082-8ace826421e8 | -8.07392 | -51.12487 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f46b66e7-363e-38df-b8a3-a4eda992ba62 | -8.06954 | -51.15487 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8a0ad54-799b-3d7c-941f-65565512f626 | -7.97519 | -51.21103 | 2024-10-04 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe0d41e0-7c92-340a-909b-042cc22197ab | -9.82402 | -51.9198 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e0bc38f-1e38-3fde-b138-233350532dd4 | -9.82342 | -51.92389 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13328a01-7c92-34a6-9398-a3c2db7abe7c | -9.82044 | -51.9193 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1ba34ee-f6a8-37c9-ab8f-cfc0936a37a0 | -9.81984 | -51.92339 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06be810b-470f-3777-b2d9-3edb17513ced | -9.81687 | -51.91877 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52373620-35ca-3e9e-aa93-defb5d383353 | -9.81627 | -51.92286 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61a7c1b4-45b1-336c-b2f7-e7b234935377 | -9.81105 | -51.80811 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed4d3c7f-66c7-3be0-b6cd-539b74c24493 | -9.81045 | -51.81229 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2ca8518-d2e3-356b-9c74-914a9d094238 | -9.80984 | -51.81644 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24eb02bc-3784-3894-a036-e39c47f60bd0 | -9.80914 | -51.8093 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 249b84dd-2060-339b-93de-36d1dedd276f | -9.80851 | -51.81347 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b5554f8-d44d-3f3b-a3cb-f477f004967b | -9.80789 | -51.8176 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 884fc5f9-6045-38d8-8dc8-f46eb4702bee | -9.80625 | -51.81594 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b5da019-8bed-3766-9f3c-e0aac53ae2bf | -9.7774 | -51.92281 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02364630-de97-3b2a-b430-415ddeac0a59 | -9.7768 | -51.92685 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78e2920a-8b76-322e-a8ee-0bc83754c24c | -9.77507 | -51.91402 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67e3d74f-9195-3ceb-82fa-d9f0561f647f | -9.77385 | -51.92218 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd5ddd45-ac14-3098-83e7-5199d18d2a43 | -9.77324 | -51.92626 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e279918-d2c2-3206-aca3-14fa12e6b5e2 | -9.772 | -51.93449 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2008796-000c-3279-bb7f-87ab09082b4e | -9.7715 | -51.9135 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c185f3a-167d-3608-8eeb-65d49a9716aa | -9.77139 | -51.93858 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ff8d804-189c-368e-8712-6ca3d6b5cc2e | -9.77029 | -51.92156 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c34a4b9-b622-3bcd-906e-03b7d0664d19 | -9.76793 | -51.91291 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ec1a46-02f3-3b90-8141-cbd780dc8197 | -9.76781 | -51.93807 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6450b6b-c514-33bd-8538-9bda08ad9832 | -9.76424 | -51.93758 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab876b47-ec7c-3c17-b63e-dc4ef80fd7de | -9.76377 | -51.91636 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d7a0657-7636-3809-b8d5-211c4a5d12be | -9.76067 | -51.93704 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 592923b1-f2d3-3f9b-b6ca-8decb593b8ca | -9.68271 | -51.38001 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca0ead83-2cea-34e2-b374-83e1a9d2005b | -9.67975 | -51.3487 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1a1ed87-ca71-3ef1-bb8a-8e325ce87dcb | -9.60483 | -51.45384 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86b511f1-9297-3e8f-84b0-e9f2e46351c8 | -9.60118 | -51.45334 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2f3828a-9cfc-3630-a18a-c8b1dd9505eb | -9.59628 | -51.46122 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e63d02a-afd0-34d5-8cc6-178441b0265e | -9.59567 | -51.46537 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 616b572c-aa7e-346d-bea2-6cfdfef0a474 | -9.91125 | -51.13812 | 2024-10-04 04:55:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 429aa970-3436-3007-8659-2becd44e0343 | -3.36868 | -51.21211 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6629314d-7575-394c-9ee9-4b5b1bddc2a0 | -3.54707 | -50.85622 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32d2c71a-4894-3f78-bc51-ba03734c5174 | -3.54646 | -50.86013 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90d90a89-780e-34b7-b96f-f82875e656d6 | -3.49686 | -50.80841 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7f017e00-6c99-307c-a4fc-b640441caf74 | -3.49394 | -50.80395 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f54a0f93-7557-3244-843e-592aac02bf08 | -3.49333 | -50.80788 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 80e69777-113a-333a-9eb5-1c121d6f4852 | -3.49273 | -50.81181 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c1a512e6-ef3e-3de1-a23e-c4b724edb6fe | -3.49042 | -50.8034 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81dced40-ca84-372b-a688-fe55bb3b5c96 | -3.48981 | -50.80733 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d556c5d3-2c28-3e8c-9379-b05b0662d3d7 | -3.48921 | -50.81127 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db482ac4-e02a-34fc-801d-ed47c1e33dd4 | -3.4876 | -51.19084 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fde9875-1a7f-35c8-9fcb-4fee8d1f5383 | -3.48629 | -50.80679 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d46c1597-00a6-38f7-b84e-162761f7a86c | -3.37214 | -51.21265 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df13558-44b6-32d7-9475-8649d160ae72 | -3.37155 | -51.21642 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14e4800c-fea5-31e5-b636-47c71deab870 | -3.37047 | -51.51437 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0128ce9d-a234-3496-949f-9bfdbb9fe4a0 | -3.36809 | -51.21589 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 932643db-dcd9-3c4d-927b-3c5fa6eb1b22 | -3.36705 | -51.51386 | 2024-10-04 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e030d1ac-4335-38c7-b49d-648d0497414a | -3.32622 | -50.78767 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3e8ce4f-1cec-322d-a272-ef147ce87a4e | -3.3198 | -50.78267 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 736ba86c-0bf7-3083-b0c5-03bec8cb0fba | -3.31919 | -50.78659 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eb65843-b501-327f-aeb6-959025decc1f | -3.31566 | -50.78607 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5be2c7f2-bd80-346a-8772-422c3930c278 | -3.29466 | -50.75881 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0046db17-da0d-3584-8c47-23e5cec437c6 | -3.29405 | -50.76274 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4295b25a-82ed-397a-9a3d-646f66210c25 | -3.29113 | -50.75827 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4dceff6-78e7-3322-bee0-b216987c8561 | -3.29053 | -50.7622 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c04ee2f-41c3-33d8-8f9e-2c50a21ae34f | -3.26576 | -50.94602 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02442fc0-d84e-3f13-9c9d-97ba8349746a | -3.25588 | -50.94053 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d207f932-a4c0-3451-b3ee-6f58a2e6ae6f | -3.25239 | -50.94 | 2024-10-04 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5604c533-cb17-315d-8aa6-f5bc4c2c00ca | -3.22408 | -50.79313 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c50a25-5464-3cab-ba24-b861ed628006 | -3.22347 | -50.79706 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a13d03e-1270-37b4-a46c-f33e1a3594ff | -3.22057 | -50.79259 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ecd65a-6125-3486-b72d-d7e816fd449c | -3.15867 | -50.8908 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a704cc3-62eb-30a3-a5dc-0199554bdd94 | -3.15808 | -50.89466 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 043fc077-9ac2-325a-95c9-0f2d5489410c | -3.15518 | -50.89026 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 926d8ec7-dbee-3a51-a25a-561d5b802721 | -3.15458 | -50.89412 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4b210ac-1c0e-34b2-97a4-9fcf7eb9b788 | -2.90128 | -50.75042 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16da6231-d793-31ab-b50b-5280c22929de | -2.89915 | -50.71804 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dee0a652-835a-38e7-b3ab-8b036cfbff9a | -2.89854 | -50.72196 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f145f40b-e97a-309f-9d94-0e017fc59e9a | -2.89777 | -50.74988 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97b9c46a-f91d-3ebc-a5cd-f2169ddc1416 | -2.89625 | -50.71359 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 072f7efd-cf34-3dce-a25c-afbf6eb46184 | -2.89564 | -50.71751 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91264de4-c2b6-3128-8b2f-77c41075acdf | -2.89273 | -50.71305 | 2024-10-04 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README147.md)
