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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c079771e-0581-331d-99df-06e1538415d0 | -10.9815 | -45.0874 | 2026-05-03 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a1b8790b-a2f2-31ed-a870-a1cdc83f52af | -17.9665 | -52.9924 | 2026-05-03 02:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| af6849f3-1543-3613-9d49-bd62c6a612bc | -13.2186 | -54.5182 | 2026-05-03 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 06fe5799-e802-3f5e-be08-9ae964aee57f | -13.1995 | -54.5202 | 2026-05-03 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b4a69509-ffc6-372e-9484-54b6f9acbe5a | -13.2183 | -54.5388 | 2026-05-03 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 66586146-4e42-3c00-b930-86c9a20c9ac4 | -13.218 | -54.5594 | 2026-05-03 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 056212f1-7b63-3e8c-ac78-c169d03784af | -17.9466 | -52.9955 | 2026-05-03 02:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2b6759ba-168d-3481-ba0e-75a4efde565e | -13.218 | -54.5594 | 2026-05-03 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 42420142-7563-35dd-8613-46cc873eb880 | -12.37 | -50.0242 | 2026-05-03 02:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9e499152-31db-3aa2-98b0-dbb4997ad6ef | -13.1992 | -54.5408 | 2026-05-03 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1c5bc89f-26eb-3f69-84fe-b67f75a85a68 | -13.2186 | -54.5182 | 2026-05-03 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e18e4aca-b82b-35f0-9d2e-9971bb82679c | -13.2183 | -54.5388 | 2026-05-03 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 8c55b3a1-cd21-3970-b5aa-99830eee51c0 | -17.9665 | -52.9924 | 2026-05-03 02:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| abb6a105-b244-3b79-a3e9-0e934d00a0f6 | -10.9815 | -45.0874 | 2026-05-03 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f70b60c8-1305-3a63-956c-4a3372120bac | -13.1995 | -54.5202 | 2026-05-03 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f0252447-9f85-3a24-94dc-abe65e33d09b | -13.1992 | -54.5408 | 2026-05-03 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 10e1cf45-4fbe-337b-b1bd-8a33d7ea8a27 | -12.37 | -50.0242 | 2026-05-03 02:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 18b0cf37-7330-35b1-909a-f3026e2fe005 | -13.1995 | -54.5202 | 2026-05-03 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| ab18b309-7485-33f3-a782-8fc8c9eaaf75 | -13.2183 | -54.5388 | 2026-05-03 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 71175c2e-47b2-318b-9104-b474c8fa138c | -13.218 | -54.5594 | 2026-05-03 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7f05dd77-7a47-3bfd-a4da-74bb7a9f3ed5 | -12.37 | -50.0242 | 2026-05-03 02:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7eee7d27-b379-3263-baff-43a55aaeb19f | -13.2183 | -54.5388 | 2026-05-03 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 4c288617-75cd-350b-846c-15b562297c49 | -17.9471 | -52.9739 | 2026-05-03 02:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 43aeb061-fcda-346b-bdeb-f698307b3277 | -13.218 | -54.5594 | 2026-05-03 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 206c593e-28a1-314e-b607-6b4692a0b07b | -13.1992 | -54.5408 | 2026-05-03 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d49ca1c9-d084-3445-9241-ef444a3fc51b | -13.1995 | -54.5202 | 2026-05-03 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 1d9c5aaf-e10d-3abc-b888-d84b059bca04 | -13.1992 | -54.5408 | 2026-05-03 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 81024add-f758-3a72-8811-b0d8ae9d902c | -13.218 | -54.5594 | 2026-05-03 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 8e3d1c82-4803-3090-a61d-0703653700c3 | -12.37 | -50.0242 | 2026-05-03 02:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| aed6cb80-d75c-3588-abd9-044afb5afec9 | -13.2183 | -54.5388 | 2026-05-03 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| c5031c4c-3d67-3862-a887-8b9edbca8181 | -13.2183 | -54.5388 | 2026-05-03 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f64cff76-571d-311f-a66c-169ed5fc2f5f | -12.37 | -50.0242 | 2026-05-03 03:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0f880dfd-bb64-3e47-bb6d-066b0a4bdfd0 | -13.218 | -54.5594 | 2026-05-03 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 4a8a5554-bd40-3704-b221-2e4b2c780903 | -13.1992 | -54.5408 | 2026-05-03 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cec633e0-2b80-3918-bfdc-e46d59b2d48d | -13.218 | -54.5594 | 2026-05-03 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 5d61f4bf-9ac6-3730-93c4-c0450d91e296 | -13.2183 | -54.5388 | 2026-05-03 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 856237a4-e468-32aa-9665-93e5696e2780 | -13.1992 | -54.5408 | 2026-05-03 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 55a733e6-5e83-3bdb-8019-cf996cabaa62 | -12.37 | -50.0242 | 2026-05-03 03:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f4708483-f98b-3b13-b20c-be2c3eddb995 | -9.85737 | -36.41024 | 2026-05-03 03:19:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2666b3ce-8d91-32af-94bd-76f13fad0405 | -9.85585 | -36.41175 | 2026-05-03 03:19:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 79e59b0b-842b-3496-9aee-ae6ba7dcf958 | -9.85666 | -36.40717 | 2026-05-03 03:19:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 10c6c976-a3e0-3ae8-b622-1be9184f4209 | -12.37 | -50.0242 | 2026-05-03 03:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 121bbb90-94f1-3c40-8b98-cb28d2a56db2 | -13.1995 | -54.5202 | 2026-05-03 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| a16d9603-45be-3ed5-b8e3-184d4cee04eb | -13.2183 | -54.5388 | 2026-05-03 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0b9c5740-83e1-3feb-ac7a-cd117431fffc | -13.1992 | -54.5408 | 2026-05-03 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a0e5f0f7-8a83-3fef-8f6c-a4aa85db83d5 | -10.5746 | -44.3336 | 2026-05-03 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| fce50249-8a90-39c6-90e0-6816dfeb61c8 | -17.47058 | -42.30388 | 2026-05-03 03:21:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49e8ba8b-5ebe-3658-ad7e-5dd16665fd97 | -11.88479 | -43.81467 | 2026-05-03 03:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47ee542c-2ff9-30f6-bfb5-d13993223a58 | -20.19402 | -46.46525 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c02c567-d9de-3752-a639-e6c27e7c3b5c | -20.18732 | -46.45757 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c474b521-74c7-32ea-a0ff-57ef5ee8fd30 | -20.18702 | -46.46397 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 08223110-7431-3656-975c-5936b08c6454 | -20.18851 | -46.45789 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b6b3729-ddb1-3878-acdd-4277585a4c7f | -20.18581 | -46.46358 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1b70850-7644-3fac-a37a-976066ff35e6 | -20.1944 | -46.45853 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1d87830-844b-3339-993b-747d417f584c | -20.19283 | -46.46475 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5fc1313-6990-327e-8922-d0aea2a5eb5d | -20.18124 | -46.45778 | 2026-05-03 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85e006a6-804b-3628-ab6e-5cae687215e0 | -13.1992 | -54.5408 | 2026-05-03 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 5e46f6df-746b-3994-8e75-ca14ad3c8325 | -13.2183 | -54.5388 | 2026-05-03 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 55268dba-0a98-332f-8cf4-0b6492446629 | -12.37 | -50.0242 | 2026-05-03 03:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f7d4f19e-d382-385a-ab39-6b9ef8459b1c | -12.3508 | -50.0266 | 2026-05-03 03:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8f003c0f-8951-3e24-aacc-2327f92b3742 | -12.37 | -50.0242 | 2026-05-03 03:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 09bffad9-0e67-3fe8-9f2e-adfea2c4b48a | -13.1992 | -54.5408 | 2026-05-03 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| ad73779e-fb77-3d47-9129-007003d4160d | -13.2183 | -54.5388 | 2026-05-03 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 311c7c60-f45b-361c-9382-5ebd804843f4 | -10.9815 | -45.0874 | 2026-05-03 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| feb1de03-71fa-31c0-a3b2-6dff20e860d2 | -13.1992 | -54.5408 | 2026-05-03 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 39a34325-6801-3918-a698-5c15cd1a7bfd | -13.2183 | -54.5388 | 2026-05-03 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7a8dedd7-6ba0-3f82-9945-6f54e41db033 | -12.37 | -50.0242 | 2026-05-03 03:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 875c71f9-c322-39b7-a18e-2ff8078eee35 | -13.1995 | -54.5202 | 2026-05-03 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 9ef64340-4f3f-3892-b8ea-bee00de66ad3 | -13.2186 | -54.5182 | 2026-05-03 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| c9c2da63-0855-335a-809e-d54efd344df3 | -13.1992 | -54.5408 | 2026-05-03 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d15a6d37-32fd-397a-9c30-32a723c67846 | -13.2183 | -54.5388 | 2026-05-03 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| cc8e5a2d-e164-302c-bc64-c85395167fee | -12.3508 | -50.0266 | 2026-05-03 04:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6d8ffd51-2abb-38c8-8483-c9d54cd8d6ee | -9.48997 | -43.04275 | 2026-05-03 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24261db5-41ca-3b00-94dd-95a0d10b2aad | -8.32972 | -45.35637 | 2026-05-03 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e223993-1e0b-32a3-8fe7-bcf5b605a6bc | -6.51758 | -43.33482 | 2026-05-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a4c94c8-6e35-35a3-884d-6a34e1759bc8 | -8.25901 | -43.92904 | 2026-05-03 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 388d38fc-caa8-3be4-8f86-10fb3beaf9b1 | -9.64151 | -43.11798 | 2026-05-03 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b7f8865f-850b-3c9a-9fc2-c562146e4f6d | -8.33341 | -45.35686 | 2026-05-03 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b05b03bd-8fd3-3d68-ae1b-c451c3dcb1a3 | -13.2183 | -54.5388 | 2026-05-03 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7ca8deee-4c6d-343a-b9ff-f3e04da661c9 | -12.37 | -50.0242 | 2026-05-03 04:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 84f57385-ca6a-37d4-b828-19d94752621e | -13.1992 | -54.5408 | 2026-05-03 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| dfd14a43-b57e-3f9b-a35e-05aee2f80d7e | -9.56553 | -50.67908 | 2026-05-03 04:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86053e7e-97d3-39ae-977a-f23710c91cc0 | -11.64324 | -52.56118 | 2026-05-03 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7274cd4b-606d-3e30-b6a5-f5bd4ae7eada | -13.19776 | -54.54142 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a9471963-c7a4-3e85-aac7-3283860f07a0 | -13.20893 | -54.54874 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5825e253-591e-3b0d-8fb0-2fb8911a6494 | -14.05534 | -53.40211 | 2026-05-03 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b960f95f-856e-3442-854d-0e6753b2b03e | -10.63969 | -48.00987 | 2026-05-03 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 01161f65-4e21-3835-bf49-18786032e910 | -12.27992 | -44.63259 | 2026-05-03 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e80a5dc5-a8ce-388d-aa7e-edbb71776b6f | -13.20482 | -54.53782 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad4382ef-9dd8-3596-83a8-805b8b55d4f4 | -9.67916 | -43.79323 | 2026-05-03 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 92f215ce-5ced-3640-a924-74540f649443 | -13.22971 | -54.54345 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a229d415-cae0-3b0d-a0fa-53ab80046ae1 | -11.64252 | -52.56488 | 2026-05-03 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5920541-bc42-3957-8277-f18cf56b07f6 | -13.22996 | -54.5386 | 2026-05-03 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f841f1b2-ea89-32fc-b9b1-81f9a1155d47 | -12.46417 | -44.29684 | 2026-05-03 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99f2be4d-0795-36d9-913f-4bbc35c7e789 | -12.37665 | -50.01841 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c169d45a-649c-3087-93c3-dadb35cc13eb | -10.98166 | -45.08665 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e111ff78-a5bc-3553-9a8b-6749bb217ac8 | -12.28053 | -44.62884 | 2026-05-03 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2c09e400-33e4-3b85-865b-1a36203c653c | -10.98033 | -45.0946 | 2026-05-03 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c6c97f61-0ed4-3b73-9f3d-59a2d8c2d74b | -12.35552 | -50.02962 | 2026-05-03 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e20c6056-2811-38fb-9c5d-52de6265f720 | -11.89166 | -43.8148 | 2026-05-03 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
