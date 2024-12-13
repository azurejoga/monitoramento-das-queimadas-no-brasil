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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865874db-61de-3163-9424-2096daea1529 | -13.05881 | -52.03746 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ca65cf0-49f9-3ef3-9fab-b43d08d4a55f | -11.43984 | -55.92141 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe8f973-85e4-364e-8512-c251e43a93ca | -11.43452 | -55.92074 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0036c611-58d5-3c77-bf63-2f0be58cfa7b | -11.44409 | -55.92227 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df015f6e-568f-3d41-99f8-329ed15aa07a | -8.29898 | -54.86111 | 2024-12-13 05:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f87c908f-8832-3d27-8ee5-f144a58048c4 | -11.20836 | -53.81768 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 93c1f924-b26f-3c55-93e5-f9dbe5051782 | -11.43917 | -55.91831 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ec5de2f-de8e-339c-9bf8-07e432faca50 | -11.43877 | -55.92162 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b015e02-5446-3974-a792-80ba869a58f6 | -13.06548 | -52.03978 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d152b39b-d158-3245-ac9b-1563e838df4b | -13.05859 | -52.03885 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c032c812-5d5d-3bc5-87c7-0628c3c30dfe | -11.44558 | -55.91872 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2070fca6-c9b0-38e8-add7-460b80cc1834 | -11.44516 | -55.92204 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4414d82a-6c8e-3b01-9004-b10b74fa39cb | -12.90528 | -55.04779 | 2024-12-13 05:37:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adff9433-e910-339f-a169-8bf8a0d08474 | -13.07308 | -52.03427 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5d23591e-7273-370f-8f0e-f375220975bb | -11.20724 | -53.82715 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 216e45ae-4dcd-3718-bf0e-4b2bf90b3745 | -11.44449 | -55.91895 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bb194a5-ee2f-32a1-9628-47fe1f93e8e4 | -11.20175 | -53.82144 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8a500bdf-4aab-371c-936f-8a340083c1db | -11.4239 | -55.91935 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddd6d85d-1dec-3ea3-b361-ae21e318f058 | -13.07327 | -52.03287 | 2024-12-13 05:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c44bae0c-1f07-3fad-a46b-c5b406eb9d58 | -11.21275 | -53.83272 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 25e2c1a4-e0e9-3fb2-a3f0-9e20ec58a8a2 | -11.43346 | -55.92093 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45bf4a40-359b-35c5-9ff4-e07ee114a405 | -11.20065 | -53.83088 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 72ff1ceb-d2d2-3a71-bdd5-4c0640b970e5 | -11.20615 | -53.83648 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6d189cf6-f5f4-3769-b18b-12e9c1cfdc66 | -8.29352 | -54.86032 | 2024-12-13 05:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56d04f09-4402-340d-b69a-f2021d0d09da | -11.42921 | -55.92003 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38619a39-1252-379e-b07f-bc3a8cd3b987 | -11.44026 | -55.91809 | 2024-12-13 05:37:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 569e6854-a8a5-3fdb-89ba-be9a798614a8 | -11.19954 | -53.84031 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 941853b4-1fa8-3df8-b3ff-b9e09882be74 | -11.2001 | -53.83559 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18f9e92b-f143-35b4-9c47-608c9156c459 | -11.2012 | -53.82617 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| b23d908b-dbb1-385a-831b-b6836a4c5c05 | -11.20231 | -53.81671 | 2024-12-13 05:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0e678366-4170-3ba7-9e18-7f21e4ab8b1c | -5.211 | -43.2833 | 2024-12-13 05:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 875a9eca-6fe6-3578-a95e-6e30615a686f | -5.2108 | -43.3067 | 2024-12-13 05:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d815ff37-a9ac-35cf-a691-813d65c8cede | -13.66091 | -55.24806 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7195a353-c34a-3e32-9f67-25209c0d583c | -13.65566 | -55.24336 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2f9e7f7-46c5-3a85-93e8-c4ede3c635aa | -13.70021 | -54.75801 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3543e0f7-1593-3e6c-85e6-8d2bf726aa0d | -13.68891 | -54.75221 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d991a844-3cd8-3c9c-b64a-07980c69f903 | -13.69276 | -54.75776 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3dc2846-0a24-3033-b6be-5d8b9b7a607c | -13.69379 | -54.76188 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ea026ff-d28c-315f-b778-725aaabb90de | -13.66323 | -55.24547 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6653b5e6-6315-3dea-b28a-70a8500219d4 | -13.54172 | -55.38155 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 320ec8c4-8a3a-3fa9-a387-80e11b510c9d | -13.69969 | -54.76258 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef875487-832f-3742-a8f4-2a4489e3ded4 | -13.70359 | -54.76826 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f123a66b-ae51-3551-9f5c-1129a55e48b0 | -13.69228 | -54.76229 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92ac01bb-2b69-35da-a38f-701b5cd94462 | -13.69482 | -54.75281 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a48df569-f2af-35ed-bb94-953248f472b9 | -13.68839 | -54.75671 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 563a88b0-63ad-3b88-8851-2391f142bf2f | -13.66137 | -55.24413 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d92fc93-2fce-382f-b2ac-9f503c94c341 | -13.69431 | -54.75735 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbe20c5c-7ab3-3124-ad44-9e937629401f | -13.68942 | -54.74768 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9783d16-49ef-3afa-bff1-e94bf0c63190 | -13.65751 | -55.24472 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90d1960a-fed6-3300-87b5-a803de304f49 | -13.69917 | -54.7671 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37470adf-9b09-3f84-aa88-fd4189d19053 | -13.69324 | -54.75322 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 643c8d07-97bc-3ab8-a33a-c2314a0a6dbc | -13.54693 | -55.3863 | 2024-12-13 05:40:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b6bff0e-cca9-3f3b-8c4f-7a0d8d7016a9 | -13.69769 | -54.76752 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e2fb102-eaf5-3a66-9fa8-e5be881b1e44 | -13.70408 | -54.76372 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f23f64b7-2741-3e4a-a529-01f92f15993f | -13.69818 | -54.76301 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53395f2b-94d5-31ef-8feb-e14f33abfa2f | -13.69867 | -54.75845 | 2024-12-13 05:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d1e1f4c-34fe-3bde-91eb-5b3e0540e0c9 | -5.2108 | -43.3067 | 2024-12-13 05:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9dab3b92-3ab8-3684-9ccd-61f814df05eb | -13.0644 | -52.0326 | 2024-12-13 05:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bf82962e-63d9-39e6-b5d3-97eb7ce1de15 | -11.1962 | -53.8142 | 2024-12-13 05:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 752646d6-2030-3f29-ab6c-6be99b376d61 | -5.211 | -43.2833 | 2024-12-13 05:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6cedb246-8aa8-358e-b12c-5dc386de1793 | -11.2148 | -53.833 | 2024-12-13 05:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 747eb9fd-cfe5-36ff-b8f1-d344816f206b | -11.1959 | -53.8348 | 2024-12-13 05:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4a95a6a6-0977-3a53-a97a-b5513c57dd11 | -11.2151 | -53.8125 | 2024-12-13 05:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 85f9f120-5fbc-32ac-a2a1-664a2dbd16ca | 3.19642 | -60.29376 | 2024-12-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43f67697-434d-3cd7-b68f-43e03bfe9f7e | 3.20041 | -60.28767 | 2024-12-13 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eeb51c80-4fa6-330a-94e3-9cbe176da313 | -11.2151 | -53.8125 | 2024-12-13 06:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bc44aa53-db1f-3037-a9c7-a0eb0c5eabe3 | -6.9161 | -43.4952 | 2024-12-13 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 2f6e893a-ce53-3747-8b88-fff66114c057 | -6.9158 | -43.5185 | 2024-12-13 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 439897a8-f433-3ba8-a6e2-426938508dd6 | -6.9349 | -43.4934 | 2024-12-13 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| a7b2dfe2-3b81-30ca-905f-0e80c67036ed | -5.211 | -43.2833 | 2024-12-13 06:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 82950309-6cf7-3f4f-8501-36b33552dee8 | -11.2148 | -53.833 | 2024-12-13 06:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5ea156c3-8f03-37fb-939c-573631534522 | -11.1962 | -53.8142 | 2024-12-13 06:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 22d7e76c-217a-3d83-a0dd-190a48331da5 | -6.9163 | -43.4718 | 2024-12-13 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 93eda62f-81c2-3f91-877a-df0d42332041 | -2.1173 | -54.6472 | 2024-12-13 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 4fc34a10-0cb9-31e3-86c3-72c793d22d0e | -6.9346 | -43.5168 | 2024-12-13 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 844cae17-9713-30c1-b658-a1e27e0fcbc3 | -11.1959 | -53.8348 | 2024-12-13 06:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 18617694-dbdf-3ddb-9f4d-d9067411fffa | -6.9346 | -43.5168 | 2024-12-13 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4e90c8a8-41be-328f-be9f-9462a3d02acc | -11.1962 | -53.8142 | 2024-12-13 06:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 49570fec-8872-3b28-b309-92a51b613b9c | -11.2148 | -53.833 | 2024-12-13 06:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ef7aacfc-e08e-3d66-aae6-02ddd32192a5 | -6.9349 | -43.4934 | 2024-12-13 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3f926e1b-80a5-3e14-9a20-dd79380bbc71 | -11.1959 | -53.8348 | 2024-12-13 06:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5682ec44-6958-355d-8aa4-006483b1c08f | -6.9158 | -43.5185 | 2024-12-13 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 9c4588e1-5db4-3f52-a0ae-e95bc6853de1 | -11.2151 | -53.8125 | 2024-12-13 06:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 11d7e54c-d827-30a2-a0a1-6c598328ca0c | -6.9161 | -43.4952 | 2024-12-13 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4e28901c-8fde-3f46-aef9-2e4449ac28d3 | -6.9344 | -43.5401 | 2024-12-13 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| bd8799a3-f709-3e4f-b0de-cb6367c71f21 | -6.9158 | -43.5185 | 2024-12-13 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| da6994de-88f7-342e-ab22-6669c5d13a4d | -6.9156 | -43.5418 | 2024-12-13 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1eef1f5a-48db-3e37-89e8-93ee89c91e89 | -6.9346 | -43.5168 | 2024-12-13 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ed183a8e-8886-31f5-94b4-9ad660380d0d | -6.9156 | -43.5418 | 2024-12-13 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 8af41575-b16b-34e6-a3d0-1163d24f44dd | -6.9346 | -43.5168 | 2024-12-13 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 09198fe4-f407-3deb-8fc8-357db0ea9a18 | -6.9158 | -43.5185 | 2024-12-13 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| fc2e9b95-f16e-3135-a074-213c399f8f5d | -6.9344 | -43.5401 | 2024-12-13 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d5097ab1-a552-3ae7-81f6-ae207704b272 | -6.9349 | -43.4934 | 2024-12-13 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 85afb8cd-98a1-33e6-ba58-7a7ab347a65f | -6.9158 | -43.5185 | 2024-12-13 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f5ab1974-149f-3621-bfb3-49b087cf0bcc | -6.9161 | -43.4952 | 2024-12-13 06:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 08354a85-283c-3290-ae5a-afa6e92ea42f | -6.9346 | -43.5168 | 2024-12-13 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 58c69fc3-ee07-3ca5-a91c-25607224ca7a | -6.9161 | -43.4952 | 2024-12-13 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0466d846-7022-300a-b1ae-29f246a8122f | -6.9158 | -43.5185 | 2024-12-13 06:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 74389124-06a6-3f56-8d24-e12ee6042f4b | -5.8198 | -40.3642 | 2024-12-13 11:40:00 | GOES-16 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 3f60f717-7b72-37cc-8d82-2a1c7095cd5e | -5.8198 | -40.3642 | 2024-12-13 11:50:00 | GOES-16 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 78.4 |


[Clique aqui para ver as próximas entradas](README33.md)
