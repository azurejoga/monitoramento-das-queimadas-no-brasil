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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea08198-17a2-3964-b0f9-39a385db9fbc | 1.121 | -60.5034 | 2026-02-10 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| fb251ddf-ea48-3ab4-adb9-1bd4e95bcf90 | 0.9569 | -60.5233 | 2026-02-10 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a691abe0-6674-33b8-adc3-c6f86772e0bc | -5.4513 | -38.383701 | 2026-02-10 00:13:00 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e3d178a-4c58-30b0-9e49-e117984a1474 | -5.4535 | -38.393002 | 2026-02-10 00:13:00 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 027f82e2-afe9-33f1-b37c-b74c2c3a7a3f | 0.7928 | -60.6756 | 2026-02-10 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 9e4b3049-d60a-3859-a0bf-d65667db1f6d | 1.121 | -60.5224 | 2026-02-10 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3ae2a012-8a3a-3e6f-b609-07d02a750155 | 0.9569 | -60.5233 | 2026-02-10 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 320722a3-6f8c-31e4-a910-b5f4af85b4a3 | 1.121 | -60.5034 | 2026-02-10 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 94651a92-fecc-32e1-a8b6-686f6b6fe99d | -9.8349 | -36.2499 | 2026-02-10 00:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 64d72969-caf4-3e7f-a5c4-73109a7f6344 | 1.121 | -60.5034 | 2026-02-10 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 9681b59b-89f2-3487-9027-0b4c89950aff | 1.121 | -60.5224 | 2026-02-10 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 778a1860-640b-3077-ba63-37916da29af0 | 0.7928 | -60.6756 | 2026-02-10 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e32ce19b-10cb-3a11-a7d0-3e52bb4339f7 | -18.97603 | -52.92348 | 2026-02-10 00:43:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e42f3130-d9ec-3d06-9ddb-e8c353c22562 | -19.39514 | -55.11439 | 2026-02-10 00:43:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6193e1a0-26e2-3dec-a711-e6e5d83c17e4 | -19.39383 | -55.10405 | 2026-02-10 00:43:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3c6c8778-8961-3568-9b76-3848df7719c9 | -18.97733 | -52.93277 | 2026-02-10 00:43:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c05286a0-70a5-38d2-8c68-6fcf1d2c80a3 | -16.44568 | -58.17215 | 2026-02-10 00:45:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ef1c8147-a134-3927-a803-76b7e1dcaf27 | -7.56803 | -53.47514 | 2026-02-10 00:47:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec6bf779-fd80-3e3c-835c-f1a0461a43a2 | 1.11931 | -60.5197 | 2026-02-10 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bf7a3d8e-775f-3dc9-8a3e-6605333c0dfa | 0.67527 | -59.81282 | 2026-02-10 00:49:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a6c45e87-286a-32a8-9579-12c71eb3217c | -1.8228 | -54.49124 | 2026-02-10 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6d6fd435-2886-3e91-91ad-eb67f666df7d | 0.78151 | -60.66478 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fdf229e8-3bc4-3721-a3fd-86d9f32a5685 | 0.78123 | -60.67091 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| cae18ee4-80e8-37ba-a264-b1e9dd139197 | 1.11078 | -59.19596 | 2026-02-10 00:49:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd3e4d59-d1ed-3c63-a8d7-7a981749ae59 | 0.96542 | -60.5208 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b6b87bf9-0df6-3010-abc1-49117be62b90 | 0.95546 | -60.51939 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 37.3 |
| cd3d3388-79b9-3240-ae5e-76f4c174dd8f | 0.77984 | -60.67648 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e1cc4c9e-8102-3edf-8643-14e4729806e8 | 0.79159 | -60.6662 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6c90126c-1c5a-3e7a-94cd-a886276affe7 | 0.95388 | -60.53078 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4ab28706-5a61-3dbf-9119-85431e19369a | 0.96384 | -60.5322 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7e58804a-629e-3068-8319-40ab10fbff02 | 0.78993 | -60.67789 | 2026-02-10 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 58e1303e-b0ec-31aa-a26a-0500714fbdfa | 0.9569 | -60.5233 | 2026-02-10 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9c359d6e-e5b8-3a17-ab0c-176bd947e785 | 1.121 | -60.5224 | 2026-02-10 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| bfe60c76-bcb7-3218-9f74-df64373b1f28 | 1.121 | -60.5034 | 2026-02-10 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 7940de8b-5f9f-359f-9e14-6b534e7fb977 | 1.1028 | -60.5035 | 2026-02-10 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9fbda7a0-8df2-3c96-9f5d-cf180ebce00c | 3.25258 | -60.41782 | 2026-02-10 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6b7a1936-a0dc-33a8-97de-9af2b0720a49 | 3.69679 | -60.97074 | 2026-02-10 00:52:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1731b4d5-1c5c-38ce-b16e-722f8f6e20b3 | 3.69516 | -60.98193 | 2026-02-10 00:52:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9a58a3e-9c33-3cc5-a5d1-5221bb00a6d7 | 3.58391 | -60.75117 | 2026-02-10 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0b49d9c8-8c48-36a6-be7b-420330d6ddd7 | 4.39256 | -60.69144 | 2026-02-10 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0c07dc93-59e3-3493-9905-30e1b1e2dd26 | 3.22696 | -60.81018 | 2026-02-10 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c29b1cf5-07ea-3976-8717-8147db9e14a4 | 4.32173 | -61.18193 | 2026-02-10 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6073f6a0-a0f5-3138-9b8a-9e3c48c7c91f | 3.79175 | -60.58503 | 2026-02-10 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8ea79637-a25f-3c51-b23b-40556bad22c1 | -10.0265 | -36.2969 | 2026-02-10 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 87.9 |
| e06cbda7-6256-3bea-9ac9-2bf7007cd59d | 0.7928 | -60.6756 | 2026-02-10 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6c2de6bb-bf5c-3df9-ad6d-2467fc2df5de | 0.9569 | -60.5233 | 2026-02-10 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b6ceef50-0bd0-38dd-92c9-4d0394aa617a | 0.9569 | -60.5233 | 2026-02-10 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d6af9594-9a64-3c97-91d5-5da9cf48aea9 | 1.121 | -60.5224 | 2026-02-10 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bb8e68e4-1863-3e1a-8f0b-1f6cc3ed4f0d | 1.121 | -60.5034 | 2026-02-10 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c0417493-8aae-34fb-a19c-8081990b8430 | -9.8547 | -36.2195 | 2026-02-10 01:20:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 139.7 |
| eaf778ec-65f2-3c2a-be0d-abbdabb7bf8e | 1.121 | -60.5034 | 2026-02-10 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 54a1f1bd-9049-33f4-938e-4769e242b1d3 | 1.121 | -60.5224 | 2026-02-10 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 30169c87-1111-3581-b25b-91986ee7c0ad | -9.8542 | -36.2465 | 2026-02-10 01:20:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 166.5 |
| 9480f723-b060-3b95-a91b-f0659d22bcc6 | 1.1028 | -60.5035 | 2026-02-10 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 47e17492-5c31-304f-8dce-91282ee5a8ac | 1.121 | -60.5224 | 2026-02-10 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| eb9eceda-390f-37dc-b981-3df1757a04eb | 0.9569 | -60.5233 | 2026-02-10 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a41296f5-2c95-3a76-b298-e5f4b6ae6997 | -10.2111 | -36.7201 | 2026-02-10 01:30:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 8f87464b-6268-3a2d-8f2a-651a6fa074a1 | -10.2116 | -36.6933 | 2026-02-10 01:30:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 84.9 |
| f215c952-f3d3-33fe-9d74-31b1e62f3d86 | 1.121 | -60.5034 | 2026-02-10 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 570b7d4c-0553-37f6-9a6e-f39a0e1f6303 | 1.121 | -60.5034 | 2026-02-10 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.5 |
| fc70956c-f2a1-37c7-a15f-e8c2cde2d3b6 | 1.1028 | -60.5035 | 2026-02-10 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c56267de-9cf8-38ee-b86e-b4276f688ec4 | 1.121 | -60.5224 | 2026-02-10 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5056241f-2226-3bbf-84a6-5537bb2284ff | -17.6304 | -40.3434 | 2026-02-10 01:40:00 | GOES-19 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| ff9b850c-f784-3816-903d-35889e797ef7 | 1.121 | -60.5034 | 2026-02-10 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 2d6dad06-b50b-3305-8e48-1f061bfc0cc9 | 1.121 | -60.5224 | 2026-02-10 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b8123ec7-4f77-3c3d-8757-d52eff9b16f2 | 1.1028 | -60.5035 | 2026-02-10 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9271fa38-bb1d-3015-8138-22dd1ff353ee | 1.121 | -60.5224 | 2026-02-10 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 7f8ad837-6425-379f-8a93-4f38cc956db5 | 1.121 | -60.5034 | 2026-02-10 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.8 |
| e2b7f648-58b5-3e39-a24f-8cffc446c569 | 1.121 | -60.5224 | 2026-02-10 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f584fe0e-480d-313e-9f94-5d2d47b90b96 | 1.121 | -60.5034 | 2026-02-10 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.2 |
| d5faf82f-6df9-3ace-a903-7dc333704101 | 1.1028 | -60.5035 | 2026-02-10 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 570b422e-76d6-3d5c-a413-d4deec034330 | 1.121 | -60.5224 | 2026-02-10 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 94d777ff-4057-3135-9722-5440a1905949 | 1.121 | -60.5034 | 2026-02-10 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e262d16d-df48-33cc-9972-596dcfe11fcd | 1.121 | -60.5034 | 2026-02-10 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 5ae3892b-3426-3021-8a94-14b43d87476d | 1.121 | -60.5224 | 2026-02-10 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 571dd804-3eaa-3863-a75a-603ffca77654 | -7.73183 | -35.1993 | 2026-02-10 03:06:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ca3c1827-a11a-3eaf-b330-2f0f8e884e80 | -16.29399 | -40.7793 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 22ce0f4d-fe08-3823-85e6-a7f30d9d9f7a | -16.28678 | -40.77612 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 204ae305-199e-3a89-9513-e3c0d8b4b085 | -16.28756 | -40.77805 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4ded5596-c942-3565-8688-5b4c97493238 | -17.61049 | -40.34967 | 2026-02-10 03:08:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b0abbc60-8598-3b99-a4d9-e57ada73b8f4 | -17.60941 | -40.35456 | 2026-02-10 03:08:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cd3270a5-2fb4-3764-8584-5c06a5afa522 | -16.2946 | -40.77098 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 470735e3-480a-3729-9e6a-cc5c403da15a | -12.67866 | -38.80305 | 2026-02-10 03:08:00 | NOAA-21 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d962c789-0d53-3bf1-ac94-9bb738d07722 | -12.67958 | -38.79863 | 2026-02-10 03:08:00 | NOAA-21 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a074ee8-7485-35c8-b3cd-0541f44d37bd | -16.29541 | -40.77296 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 9802b70d-19fb-35be-a75d-20b636fb67e4 | -16.289 | -40.77164 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8d83761b-005b-3c12-8777-1178b67d281e | -17.61549 | -40.35595 | 2026-02-10 03:08:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 27d323a9-a1bf-39fe-bbd8-337349125815 | -16.2932 | -40.77742 | 2026-02-10 03:08:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 0adb76cf-2e6a-3902-b94b-a77200be140f | 1.121 | -60.5034 | 2026-02-10 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| df940944-9249-3f1f-9948-5ce0fc72f39d | 1.121 | -60.5034 | 2026-02-10 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2683a12f-169a-332c-aa83-77f482fc34f2 | -17.6102 | -40.3489 | 2026-02-10 03:20:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 947ae2df-a0a2-3354-88f9-325381440a28 | 0.9569 | -60.5233 | 2026-02-10 03:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a075dd88-d222-3883-a5c3-48377d00ae34 | -4.54974 | -38.42026 | 2026-02-10 03:34:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fcc6db83-7c0e-352a-b9c7-a7e1a1f23fbe | -7.78256 | -37.56913 | 2026-02-10 03:36:00 | NPP-375D | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3d6fe604-043a-3965-ad2e-73d36d9ea270 | -7.77849 | -37.56845 | 2026-02-10 03:36:00 | NPP-375D | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 36a1f4c5-4cd8-3473-a331-e9118b91b82f | -7.86353 | -35.007 | 2026-02-10 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab21c2cf-7d85-3958-a40b-fd1dba20ab03 | -10.25836 | -36.41853 | 2026-02-10 03:36:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e855251-df2c-31cb-a72e-8fe9e72b45d8 | -12.68241 | -38.80327 | 2026-02-10 03:38:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09ef53a4-a2c6-39b7-b28e-20ef3c2cd009 | -17.61566 | -40.35329 | 2026-02-10 03:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b01ebbcd-7abe-35db-8c84-cda7480adb6d | -12.31483 | -37.9177 | 2026-02-10 03:38:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
