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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df177486-4399-3b3e-a4e7-c1d760305285 | -2.2445 | -48.3802 | 2024-11-11 04:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3c54ebf2-54aa-3c24-8fa3-fbeea37b7a5a | -2.2297 | -53.6824 | 2024-11-11 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f9b589da-0d13-3e4b-bf54-29c9a38df005 | -17.2737 | -57.488 | 2024-11-11 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 32a83968-2851-39dc-a207-a51136ad2fe6 | -2.2259 | -48.4021 | 2024-11-11 04:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 95b1dc14-ffc2-305c-bcc7-470c4d937032 | -2.2479 | -53.7627 | 2024-11-11 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 28e98ce0-5f3b-370d-9986-1fd3ca886678 | -3.0295 | -50.9815 | 2024-11-11 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 32d5654e-c020-3054-8384-623a910fc300 | -2.189 | -48.3815 | 2024-11-11 04:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9305dc95-02b7-3243-8dec-3d94ab19ca82 | -2.2298 | -53.6623 | 2024-11-11 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 67918570-8446-32f5-b115-98e3d55c6a71 | -2.2075 | -48.3811 | 2024-11-11 04:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ffe0ab86-a768-3234-8492-dae67d001f93 | -2.248 | -53.7224 | 2024-11-11 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d174e1fc-11e3-3340-af74-bbdf6b6190ff | -2.2663 | -53.7422 | 2024-11-11 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 76d2c6ab-a081-3665-99e1-12a9b75ef676 | -2.248 | -53.7426 | 2024-11-11 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| cb904b6c-f1ef-3874-9b8f-0e469c12a1d2 | -17.2936 | -57.4652 | 2024-11-11 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 5f3897f5-9244-3985-915b-32e5e6b9fe8e | -1.4057 | -52.3758 | 2024-11-11 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 30fddf0a-81e7-3002-aa33-53bfb7f259e5 | -2.2075 | -48.3811 | 2024-11-11 04:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e149b894-d65c-3d6b-b42f-192d6c5f7d7e | -2.7402 | -49.3502 | 2024-11-11 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 71703d61-79b3-3f6a-96f4-f55fb953b09e | -2.189 | -48.3815 | 2024-11-11 04:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 578de884-3847-34b7-91ad-04f9e853a663 | -2.226 | -48.3806 | 2024-11-11 04:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4cf91bff-52f2-379f-b4b0-b7e3f7c2ccd8 | -2.7588 | -49.3285 | 2024-11-11 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4ebbf185-fd58-3ce5-9d64-69834e807143 | -2.7587 | -49.3497 | 2024-11-11 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| ec9f78ca-8ac8-3d57-850d-942b4a8fe92f | -17.2737 | -57.488 | 2024-11-11 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 6f83c7f2-bc27-3b2b-b713-70f23a83a5cd | -1.4057 | -52.3758 | 2024-11-11 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| e7ed2b9f-599b-3488-bed9-d6be8e0d3224 | -2.2663 | -53.7422 | 2024-11-11 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d0291aff-da75-308e-b4da-13a799955ce3 | -17.2936 | -57.4652 | 2024-11-11 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| bcd47fb9-f04b-34a4-bee1-65a9d5b33a4e | -2.2259 | -48.4021 | 2024-11-11 04:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8702bb79-8ad1-39d5-8cfe-8bb67a503b04 | -2.2482 | -53.6619 | 2024-11-11 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 058127d7-859e-3b4f-9009-af74eb184025 | -17.2933 | -57.4857 | 2024-11-11 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.6 |
| fe502ceb-e39d-3890-81a4-a19b02c8fe72 | -2.2298 | -53.6623 | 2024-11-11 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 1a136ddc-ef61-3546-b1df-676f0cc6856c | -2.2297 | -53.6824 | 2024-11-11 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 327462c2-4d28-3391-89bf-48cefff1d8d9 | -2.248 | -53.7426 | 2024-11-11 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| bf8fb70d-2c1f-36ea-8257-bb30b4847e5e | -2.248 | -53.7224 | 2024-11-11 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7f99b06d-8ddc-3216-b5ba-b732d7468639 | -2.7772 | -49.3492 | 2024-11-11 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 1aa87679-7f4c-3d17-bd41-268cc37a72c6 | -2.2445 | -48.3802 | 2024-11-11 04:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fb4f7eaa-75ae-3447-a435-f29606bd309a | -2.7586 | -49.371 | 2024-11-11 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 942c3637-97f1-3676-811e-ce370aa8aa2a | -2.2663 | -53.7422 | 2024-11-11 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 76b767de-616f-3bae-91c8-7a2f81df5bee | -1.4057 | -52.3758 | 2024-11-11 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 69991cf8-d15a-3c24-991c-94c27c10140e | -2.2259 | -48.4021 | 2024-11-11 05:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8bf04c15-57ea-3393-beb2-66184bbd5565 | -2.7588 | -49.3285 | 2024-11-11 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bbefcc32-ab32-3a4e-83dd-95bb69cfbf53 | -2.248 | -53.7224 | 2024-11-11 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3cbeb631-849f-3e5e-81cc-3b539e2bb5a8 | -2.2298 | -53.6623 | 2024-11-11 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| c5039e1d-b5a5-327c-a997-58718547cfc5 | -2.2482 | -53.6619 | 2024-11-11 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| b0021f90-8d24-303d-b004-a49089fbd147 | -2.7587 | -49.3497 | 2024-11-11 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| b5351f92-d124-37f4-90dd-680ac675c3e8 | -2.248 | -53.7426 | 2024-11-11 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 7ac4332c-89bd-3c9a-b6be-1a55073b20d0 | -17.2933 | -57.4857 | 2024-11-11 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| d65f8784-b1ac-3ade-97e2-50bb24244ec2 | -16.0179 | -59.343 | 2024-11-11 05:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| bfcd8fd4-be66-306b-b5b3-b40ab2c8364f | -17.2936 | -57.4652 | 2024-11-11 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 90e2c8fb-8b38-3bb0-884d-44880a06eea8 | -2.2297 | -53.6824 | 2024-11-11 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| d1abd781-41ea-3ee8-9743-3b8145c09351 | -2.7402 | -49.3502 | 2024-11-11 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c9291932-9918-31f1-839d-2cad59da0e2c | -2.2075 | -48.3811 | 2024-11-11 05:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7a7ba667-5e1f-3061-ad8a-3f46256646d8 | -15.9985 | -59.3449 | 2024-11-11 05:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d3453519-8472-390d-809d-9063d6908127 | -3.0295 | -50.9815 | 2024-11-11 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f47176d6-1e70-33a6-b4ec-7b9673b20e3c | -2.226 | -48.3806 | 2024-11-11 05:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9e9765ed-a29e-331d-a5df-49ff9e16dfe8 | -2.189 | -48.3815 | 2024-11-11 05:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ec1a8db9-98dd-3c11-805b-faa85c0b1a72 | -15.9982 | -59.3649 | 2024-11-11 05:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 852e10b8-1762-31ba-b169-cf2e61b5b2d3 | -3.1458 | -54.4859 | 2024-11-11 05:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0235fed6-c92f-3c8d-8cac-de0b0d2f5dd8 | -2.2482 | -53.6619 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 23610980-5579-310b-993b-666759aeca2a | -2.248 | -53.7426 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 28471340-0465-3efa-a9c2-4c854ea1b786 | -2.2297 | -53.6824 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 7cada22b-5306-3490-8600-bc2ac6aec079 | -2.2298 | -53.6623 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 6f941f69-93d4-37fc-85be-6c2b7c44fbe4 | -2.2114 | -53.6626 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 89aa6614-edab-34d3-beab-2d67a0739cba | -2.189 | -48.3815 | 2024-11-11 05:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d7b1e8bd-7aa3-3ecc-8885-70d19a8f8826 | -2.2663 | -53.7422 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6e5431f1-515b-3316-9355-7756046b1d62 | -2.2114 | -53.6828 | 2024-11-11 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| fbb7e022-6baf-32bb-aeb7-d7b216ecf9e1 | -3.0295 | -50.9815 | 2024-11-11 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 15406c32-c9ad-3054-87ed-86e96d6db92a | -2.7587 | -49.3497 | 2024-11-11 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f9ee891c-bb49-3750-9ade-fe7630d2e42c | -2.23128 | -48.37772 | 2024-11-11 05:14:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bbbbd6d5-bb67-330e-903d-818978000109 | -1.84234 | -46.58247 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bcabfea8-83fa-3a41-a8f0-6f549f50df0c | -4.12604 | -43.58852 | 2024-11-11 05:14:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5f83764-679d-3ed1-8eb3-863108d59538 | -3.53069 | -45.70648 | 2024-11-11 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 714e8954-a738-3131-a341-82534dfcbe6d | -3.54076 | -43.55603 | 2024-11-11 05:14:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 39dab5c0-6e1e-3333-afe2-d07956c389d3 | -3.59562 | -44.54199 | 2024-11-11 05:14:00 | AQUA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5ed7e17-f529-33b1-be60-15d3631ae4ed | -3.11459 | -45.22211 | 2024-11-11 05:14:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8d8ae4fa-0f1e-31fb-8f8f-9bf0c0207deb | -2.23281 | -46.436 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bcfcb03d-153a-3111-a88a-aed6de14e27e | -2.09648 | -46.52362 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6560a512-c436-3a66-bd9a-3b291d9c92ab | -2.97965 | -46.98638 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2d5f7e82-e884-3c50-a79e-080d5988ce9e | -3.73674 | -44.52942 | 2024-11-11 05:14:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b826a560-da44-32f5-9a67-398f0346fdde | -2.92199 | -45.62904 | 2024-11-11 05:14:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c90e3af8-a98c-3b32-96a8-75d6415894b4 | -3.13855 | -45.96429 | 2024-11-11 05:14:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a80a3c9-1bc5-31dd-a6b2-38062515aed0 | -1.8427 | -46.57766 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f36d1b73-7dfa-38a9-9236-d17d2f0ee1b9 | -2.21882 | -53.65318 | 2024-11-11 05:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d949f8ae-a206-344e-8e35-2167958707c9 | -4.07203 | -43.94929 | 2024-11-11 05:14:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d1034708-9f36-3d08-946e-3739882e4a2f | -2.97892 | -46.99185 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 36643582-9421-3d15-8917-7036c9d964ac | -2.24122 | -53.73784 | 2024-11-11 05:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7168eae0-086c-37b9-82fb-6362168d094b | -2.98075 | -46.98017 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e8cdf39a-f27f-3928-b222-e6fa2fa26fdf | -2.4161 | -46.51634 | 2024-11-11 05:14:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 07728f18-9886-3697-8c8f-6c7392145741 | -3.61045 | -44.2624 | 2024-11-11 05:14:00 | AQUA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0dcc44b5-5e91-31f9-83a8-bf8612a20f7f | -3.59427 | -44.55095 | 2024-11-11 05:14:00 | AQUA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0c21c5d2-a6dc-31ad-a481-34927aa43c03 | -2.09817 | -46.51239 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89046da4-6dea-3443-922f-3d853d89c703 | -3.53944 | -43.56483 | 2024-11-11 05:14:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f978183b-443b-337d-ad54-6605759e051d | -2.99813 | -46.93473 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d8f8e7d4-f8ae-3ac9-add3-1b29d17a8122 | -2.18438 | -48.38052 | 2024-11-11 05:14:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5a68d2c1-9ef3-3d2d-b668-c135a877cac0 | -3.23809 | -45.37843 | 2024-11-11 05:14:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 456bdef1-c8e5-395e-b50e-9ca91f9e6729 | -2.21914 | -53.66079 | 2024-11-11 05:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0bc31cb3-ffb9-3a1b-8486-8ad7f47de315 | -3.59856 | -42.85127 | 2024-11-11 05:14:00 | AQUA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1dfdc91-12ef-3a16-a7a7-7c547d6b7077 | -2.70071 | -46.66799 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2298acba-536a-398d-a001-1febaa559038 | -2.22893 | -48.39283 | 2024-11-11 05:14:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 7634477a-7f02-36ab-863c-0d8efb495091 | -3.53216 | -45.69674 | 2024-11-11 05:14:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1af27193-655d-3cfa-9ec5-7e61e363e575 | -2.23278 | -46.44299 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 765f6950-9e6b-3052-9796-c1bd7bd3b0df | -2.18667 | -48.36543 | 2024-11-11 05:14:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| df7b1298-b603-30e5-aaac-e2214b9bec8d | -2.83555 | -46.64905 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README41.md)
