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
| 1800d952-d818-3fa2-8549-73dc0f35e9da | -1.8058 | -54.4923 | 2026-01-29 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 163e907e-54de-3e3a-8a54-608df46c1f76 | -1.3125 | -53.2111 | 2026-01-29 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1b32e8ab-db19-36f2-b2ae-c47a0998e0ba | -1.3126 | -53.1909 | 2026-01-29 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dc8d0d57-8c32-3200-9e43-6c4b4010f082 | -1.8058 | -54.5122 | 2026-01-29 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 833fb4ee-c073-3ee5-8e81-246406fa091d | -1.3125 | -53.2111 | 2026-01-29 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 162373b6-8332-332c-932e-19cfac596dbd | -1.8058 | -54.5122 | 2026-01-29 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e22b09d7-a523-3acd-8fb0-1ac6e8eff5a9 | -1.8058 | -54.4923 | 2026-01-29 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cecbaa06-404c-3f80-ad21-5a04795c5b5d | -1.3126 | -53.1909 | 2026-01-29 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2d973a00-10fe-38c5-b881-cc213a14d69d | -1.8058 | -54.4923 | 2026-01-29 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d798e96d-bd36-341a-b9f6-605c5c38a5b6 | -1.8058 | -54.4923 | 2026-01-29 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4f33e740-d60b-3e3b-b15c-f6a904f7994c | -1.3125 | -53.2111 | 2026-01-29 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| ba5f684f-7e89-306a-9619-d39741022c99 | -1.3126 | -53.1909 | 2026-01-29 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5df24bcb-e045-3610-b5aa-a84c41e3683f | -1.3126 | -53.1909 | 2026-01-29 00:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 1fd985cb-075d-388e-8360-b329b5f59c3c | -1.3125 | -53.2111 | 2026-01-29 00:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| ee932131-5b08-3f7d-83d2-3e5a14d2fcfb | -1.8058 | -54.4923 | 2026-01-29 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 14b16d1c-824a-3cee-b98b-42a5d69dc7e3 | -1.3125 | -53.2111 | 2026-01-29 00:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ee5141b5-b47f-3ebb-b4f3-cec74e53178c | -1.8058 | -54.4923 | 2026-01-29 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 85265122-215f-33ea-b25e-e809d398198c | -1.3125 | -53.2111 | 2026-01-29 01:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 791c9539-2488-33fe-b3d0-c825daaa5f0b | -1.3126 | -53.1909 | 2026-01-29 01:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 729ed914-4ecb-389e-b1ed-bbfe3bbc496e | -1.8058 | -54.4923 | 2026-01-29 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 254bec33-6251-3f84-92aa-7d9f1680a0ea | -16.44296 | -57.27002 | 2026-01-29 01:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c874b231-1ad0-3fd7-ae8b-4f0d7b02eaf0 | -1.31243 | -53.20724 | 2026-01-29 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| e7c1062e-a593-369b-b634-d230dcb3d87b | -1.80484 | -54.50212 | 2026-01-29 01:09:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 73056a8b-216e-39d4-bfdc-3ce30afe9d99 | -1.31577 | -53.21214 | 2026-01-29 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 06e1b18b-9f9c-35f6-bef1-131b69edb9db | 1.49243 | -55.90902 | 2026-01-29 01:11:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2b32c939-5ab5-38c9-8b3e-c26e14faed49 | 4.2669 | -60.28917 | 2026-01-29 01:11:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 155b3919-6526-3e33-9b11-f6df3d6cae76 | 4.22376 | -60.7536 | 2026-01-29 01:11:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3858a78d-a5a2-3af4-baee-04e0e43deb17 | 3.92763 | -60.29161 | 2026-01-29 01:11:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1f548fc3-5fc6-3f97-b513-fb8c8a08afd9 | -1.3126 | -53.1909 | 2026-01-29 01:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| a5755124-28e6-3e46-8f50-e5516ba25036 | -1.8058 | -54.4923 | 2026-01-29 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c7bd80f8-54a3-3539-b45b-44ec98d58338 | -1.3126 | -53.1909 | 2026-01-29 01:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| bb3d4acf-47c4-3695-9292-11c42ebfb976 | -1.3125 | -53.2111 | 2026-01-29 01:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 7e3d056e-e8cf-348d-81ed-599184740ea4 | -1.8058 | -54.4923 | 2026-01-29 01:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8b0e927e-dedd-393c-8bf2-d196f291a168 | -1.3126 | -53.1909 | 2026-01-29 01:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a7ec42c4-323e-3f2b-8de2-a859a2642ef6 | -1.3126 | -53.1909 | 2026-01-29 01:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 78564f34-33a0-3ce1-9a33-d88b342a867c | -1.3126 | -53.1909 | 2026-01-29 02:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 6bdac904-5d39-36db-878e-504850bba4de | -1.3125 | -53.2111 | 2026-01-29 02:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| c72b889a-0771-3534-9bd7-0bb1440b4a4d | -1.3126 | -53.1909 | 2026-01-29 02:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| ccec2c1b-9623-3898-8308-92b02f0990f6 | -1.3126 | -53.1909 | 2026-01-29 02:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 34ce70f2-b115-3b9e-8348-5cc2c732f068 | -5.92566 | -35.84645 | 2026-01-29 03:29:00 | NOAA-21 | BARCELONA | RIO GRANDE DO NORTE | Brasil | 2401503 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9df776c2-8b89-3f0f-a46b-ed5b98f5c2ee | -7.4813 | -35.18288 | 2026-01-29 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6c93a519-a9aa-3e8d-9661-d011809739cd | -7.48153 | -35.18265 | 2026-01-29 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61e6efcb-9d36-384b-b77e-f27463e46f4b | -7.47777 | -35.18229 | 2026-01-29 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4f20c33e-d1bf-3f3e-a74e-0f962a49dd73 | -6.2332 | -35.63864 | 2026-01-29 03:29:00 | NOAA-21 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| acd88f5e-d252-38fa-8b38-b66c24a85a7c | -8.37399 | -36.56282 | 2026-01-29 03:32:00 | NOAA-21 | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3a03dd5-22ad-32bd-b9bf-60afc8356a8a | -8.59668 | -40.44723 | 2026-01-29 03:32:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7765f288-cb81-336d-9893-46dd80b89777 | -8.59186 | -40.44639 | 2026-01-29 03:32:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 50bff8c5-9849-3994-b9e5-9f5962158a98 | -8.38867 | -35.38606 | 2026-01-29 03:32:00 | NOAA-21 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b21660d-7527-3362-91a2-fd0dc84c946c | -10.00457 | -36.27069 | 2026-01-29 03:32:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6381a56e-205a-3f34-afbd-3215ffa4fafb | -15.84259 | -41.61391 | 2026-01-29 03:34:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dbc8090e-9051-37b3-b207-bf2690787c94 | -18.95516 | -39.95337 | 2026-01-29 03:34:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 35dd1aa9-188f-33ce-b88f-afc4b43f781b | -15.85057 | -43.50649 | 2026-01-29 03:34:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ebb09e2-d7ee-30a7-8669-08eee6a3cbea | -23.26768 | -51.20923 | 2026-01-29 03:36:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7126a2dc-0833-3bfc-b42d-1b4335c50856 | -22.84046 | -48.64804 | 2026-01-29 03:36:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20697ca5-79bf-3d94-9341-a24a8aeb63bd | -22.84794 | -48.64407 | 2026-01-29 03:36:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60ef3bee-82e6-3895-82c4-a4c50ed34d49 | -23.18639 | -50.77109 | 2026-01-29 03:36:00 | NOAA-21 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1a358549-37f9-3825-8d13-0987cd5e0997 | -22.84665 | -48.64933 | 2026-01-29 03:36:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b690f49f-8dc3-3019-b428-75b6c29e68f2 | -23.27009 | -51.20953 | 2026-01-29 03:36:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3a04044c-9aea-328a-8b7c-672643ea4c1c | -22.84778 | -48.65017 | 2026-01-29 03:36:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de0fbde7-afd8-31a6-a18c-9a175b78eb20 | -22.84161 | -48.64879 | 2026-01-29 03:36:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f905245-5739-30fd-9375-4856fb4dc137 | -22.84286 | -48.64352 | 2026-01-29 03:36:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 757fe69f-462c-31fe-8e67-b32473e0bdae | -23.18633 | -50.77072 | 2026-01-29 03:36:00 | NOAA-21 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6f1bad13-9947-3b5e-9a55-a4127ebeb3f2 | -29.68538 | -50.78595 | 2026-01-29 03:38:00 | NOAA-21 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b37e9643-f2e2-3181-bdf0-e142de0dda31 | -29.68757 | -50.78593 | 2026-01-29 03:38:00 | NOAA-21 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 691b96ea-9586-3b94-b8b9-ddd13c1c0db6 | -5.92715 | -35.84752 | 2026-01-29 03:59:00 | NPP-375D | BARCELONA | RIO GRANDE DO NORTE | Brasil | 2401503 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38adc01f-05ee-3a0d-aefe-a961afeb1901 | -7.48026 | -35.17801 | 2026-01-29 03:59:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 34816d9c-1cdb-3b29-9f9b-0fa162af46df | -5.53047 | -45.95916 | 2026-01-29 03:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaac1f1e-b049-32e0-b15d-f3ce032f0392 | -8.37015 | -36.5632 | 2026-01-29 03:59:00 | NPP-375D | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3009b729-f127-361c-9f97-8e2f62992924 | -7.51141 | -35.18607 | 2026-01-29 03:59:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 896bead5-76ed-39a3-94bd-e0ae199866b1 | -8.37365 | -36.56375 | 2026-01-29 03:59:00 | NPP-375D | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9721721-2e38-3656-8d23-ce38e014ffe0 | -2.53318 | -47.80155 | 2026-01-29 03:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5885ab9-62b9-3db1-a2dc-9011a3fb64f1 | -7.4796 | -35.18239 | 2026-01-29 03:59:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2eec017c-536a-3efd-973e-9af82cae65a4 | -8.17295 | -34.97924 | 2026-01-29 03:59:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5075f7c7-79db-398d-8dfd-b3e72b971d7c | -6.10095 | -45.85307 | 2026-01-29 03:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b56ed25e-7da7-3eee-8bad-2c821661ba80 | -7.51576 | -35.18226 | 2026-01-29 03:59:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 878b6df9-1815-3a0d-979e-e174d8cc1af3 | -7.51511 | -35.18664 | 2026-01-29 03:59:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 75c7ca1e-dd96-3627-8ce0-7ca62b8b7270 | -7.86544 | -39.09615 | 2026-01-29 03:59:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2646507-0795-3e10-92fc-da67c1c2b9c1 | -2.53891 | -47.80267 | 2026-01-29 03:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6280ce2d-ff99-390c-8f77-e64cf81b9fc9 | -2.53885 | -47.80239 | 2026-01-29 03:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abd0c942-7a6b-3b34-a09b-632e28147660 | -8.37106 | -36.56246 | 2026-01-29 03:59:00 | NPP-375D | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c3f23ae-b2fe-3515-a3f3-7b50ec69501e | -2.53312 | -47.80125 | 2026-01-29 03:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dff320fa-06b7-3d06-a878-70cb44d20d60 | -10.01922 | -36.25387 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6559c39c-49ca-3bb2-9c9d-ed2869006ea0 | -10.00652 | -36.26471 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| b100fdbf-3d23-3d45-a14d-23b297639207 | -10.00229 | -36.2683 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 252e1527-d72d-3412-8967-36e57ae49d66 | -8.67 | -38.45126 | 2026-01-29 04:01:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e83dde4-2f38-31c8-b576-01851d9b85db | -10.01249 | -36.27406 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b7e2e11-c79b-3003-a837-39c938e3548d | -10.0095 | -36.2694 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f8664e76-bece-3cf9-9bbf-a67c46108517 | -10.01012 | -36.26526 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 7bacf14e-a13d-38f6-b0bf-76fe1c1719f0 | -9.99209 | -36.26254 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae96e975-1ff6-36c5-a20c-31b68d2bbcf9 | -10.01796 | -36.26221 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ecd8c10-3513-3a23-80c2-7b1d2ca93aef | -10.01435 | -36.26166 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9b0be89-e243-3c7e-a378-3a7b419637c5 | -10.35537 | -36.74228 | 2026-01-29 04:01:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8305e51b-839d-3d2b-a212-f31e7cc47852 | -9.81225 | -38.10643 | 2026-01-29 04:01:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5dddd55-dd16-356a-b1d3-1ce110fa8a6a | -9.99694 | -36.25478 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 60d2f917-989d-3e3d-b507-69acd846b226 | -10.01075 | -36.26111 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 0abbca0f-ce80-3d2e-b9ca-063972e1784a | -10.0059 | -36.26884 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a69d7695-adcf-3203-aafe-2ab8307e239b | -9.9957 | -36.26308 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 49e5b412-4464-38e2-b468-629970611ef8 | -8.88624 | -36.72498 | 2026-01-29 04:01:00 | NPP-375D | PARANATAMA | PERNAMBUCO | Brasil | 2610301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a7378ba-87b2-36ec-87c0-8ce021853e4e | -10.01498 | -36.25749 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 12d38546-48b8-395b-9cbf-7bcb50415cdc | -10.01373 | -36.26581 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
