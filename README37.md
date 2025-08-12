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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a346035-0025-3a23-a01b-c6b3da1fc60f | -13.03991 | -56.84536 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e442112-82e5-355a-aba7-060dd0b2f0e7 | -10.62145 | -65.01006 | 2025-08-12 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 017815a6-f12c-3c2d-8808-b53dec616a12 | -13.06952 | -56.84935 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b09c44e5-7b4e-311b-aacf-d971ea0ab0a5 | -13.06537 | -56.84358 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b819f4a-df3e-3bdb-9a86-5a51ac19d7af | -13.04048 | -56.84039 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b706530-b65f-3109-b990-40106027bf22 | -10.04654 | -64.89707 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8a04f5-7c31-39c7-a72b-77c86bc33759 | -13.06478 | -56.84872 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc3722cc-0a84-3193-aa95-5202c3d3f41e | -11.6483 | -61.64668 | 2025-08-12 05:50:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 145c6927-9fe7-3ee2-897d-8464974ce8b3 | -12.36388 | -59.84673 | 2025-08-12 05:50:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9315ab5c-3410-33c5-b47d-a5eb97d5fda3 | -10.47409 | -61.32597 | 2025-08-12 05:50:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32ff5358-ccdc-3ca4-8c04-d0bf54e696d4 | -8.9401 | -60.7288 | 2025-08-12 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 5e1075ee-b78b-30ad-bdc6-ff6a01856e24 | -16.2961 | -52.9016 | 2025-08-12 06:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 03e6d198-92a5-3fab-9c36-4e8f5a87f1cb | -12.555 | -47.0034 | 2025-08-12 06:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e6a4f5af-cd1a-3856-a0c4-27427fed78e1 | -16.3153 | -52.9201 | 2025-08-12 06:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 6494de04-4fc0-3b45-8bf4-3aebb0f66be5 | -16.3157 | -52.8988 | 2025-08-12 06:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 4e257c91-9603-3ee0-9f50-b25e3591fb1a | -6.5856 | -44.564 | 2025-08-12 06:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| afe3dabf-e544-3351-b677-abd6cb5fea06 | -8.5211 | -43.3063 | 2025-08-12 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9859f04f-988e-3d72-823d-d1b88d73f60f | -3.9684 | -47.8901 | 2025-08-12 06:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ffc7abcc-fb84-3257-bd59-790e2e1f50f9 | -16.2957 | -52.923 | 2025-08-12 06:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b7d3cf85-aa2b-3e7b-8b0b-b72422d8897e | -17.6549 | -46.6757 | 2025-08-12 06:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 84fa5ca2-b879-3602-81a9-618f7c297036 | -6.5856 | -44.564 | 2025-08-12 06:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| cfb09129-f6f1-37b0-9e61-ab197cb178b9 | -12.555 | -47.0034 | 2025-08-12 06:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6570cd7d-6ea2-3d6f-bf3e-e51563b06ad0 | -3.9684 | -47.8901 | 2025-08-12 06:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e77dc9cb-9dc1-3325-ac85-cac8226cc94d | -16.2957 | -52.923 | 2025-08-12 06:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 590cbae6-b793-346d-afb2-9915123d0f09 | -3.9686 | -47.8684 | 2025-08-12 06:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d3e86d0f-7670-376b-b657-fe0112cef94a | -16.3153 | -52.9201 | 2025-08-12 06:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 78871be7-411b-3fb4-b667-9d4cfa692599 | -16.3157 | -52.8988 | 2025-08-12 06:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5000b6c5-b084-383b-bbb2-273074f39101 | -16.2961 | -52.9016 | 2025-08-12 06:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c0ddeb5a-a998-32f3-9a8e-8e462180f9c1 | -7.1299 | -60.1182 | 2025-08-12 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7f85c191-7df1-31ab-b2b1-0fa73f601f85 | -17.6549 | -46.6757 | 2025-08-12 06:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 16bd4c00-98b1-3ef3-ba00-eea33d60d16b | -16.3157 | -52.8988 | 2025-08-12 06:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 16aa3d91-0132-3f80-9975-71be95251bbf | -16.2957 | -52.923 | 2025-08-12 06:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 15cb5675-e297-39cf-b008-6dc50c3377d0 | -6.5856 | -44.564 | 2025-08-12 06:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bd2b7248-8c19-3007-b7de-927a3d66ba66 | -16.2961 | -52.9016 | 2025-08-12 06:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 66690144-06fe-3a08-8257-7c05a988d8aa | -12.555 | -47.0034 | 2025-08-12 06:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 43b5b217-50a3-3a28-9afd-bc97047bc1e9 | -7.1299 | -60.1182 | 2025-08-12 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| dd7ec0c2-2e2b-3f38-a177-ae63949227ae | -17.6549 | -46.6757 | 2025-08-12 06:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 722cc215-7172-3d55-81ed-57fa8bfec9a5 | -3.9684 | -47.8901 | 2025-08-12 06:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a2f5c2c4-6e7a-3d49-ab27-666505f0aa6b | -16.3153 | -52.9201 | 2025-08-12 06:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f5bf3ea9-e035-39fe-b3d6-99994017486b | -3.9686 | -47.8684 | 2025-08-12 06:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1c43f7ab-02d7-3c81-ac66-5d2aeaf82e23 | -6.5856 | -44.564 | 2025-08-12 06:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3b23bf1e-a0c0-32ca-9359-3f1a925fa412 | -12.555 | -47.0034 | 2025-08-12 06:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| beb9b1fb-187c-3f64-93e0-c230d0c5a430 | -16.2957 | -52.923 | 2025-08-12 06:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 3dd4430a-2f9d-3e66-8dd8-13a66442cd27 | -16.3157 | -52.8988 | 2025-08-12 06:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| fdb02b81-ef6a-3a80-b9aa-b88a123b0cb4 | -3.9684 | -47.8901 | 2025-08-12 06:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| cf7758fd-5e8e-3079-bc23-159ba1aaec86 | -17.6549 | -46.6757 | 2025-08-12 06:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b7eeafc1-cc65-3f47-93fd-fe11471a6751 | -7.1483 | -60.1174 | 2025-08-12 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1741bd64-b845-3984-b4d6-4d7c46c8f5e9 | -16.2961 | -52.9016 | 2025-08-12 06:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1523c049-9afd-39d4-97b0-cca2f6cbe34b | -16.3153 | -52.9201 | 2025-08-12 06:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f77405d6-c6b0-3753-9c62-2e1b93ddbcf7 | -3.9686 | -47.8684 | 2025-08-12 06:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1d5033fb-924e-3139-ab4f-326f2a5ab65c | -8.9401 | -60.7288 | 2025-08-12 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 542cbb3a-82d5-37ae-8efe-b566a2236ee8 | -7.1299 | -60.1182 | 2025-08-12 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| fb16e86b-613d-3eb0-9d7d-12462a9363d2 | -12.5546 | -47.026 | 2025-08-12 06:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fa48e2a0-2cba-39e0-a7b5-395e0c5238cd | -12.555 | -47.0034 | 2025-08-12 06:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a4b9c3e8-ded8-38aa-b04a-f397b05a3517 | -16.2961 | -52.9016 | 2025-08-12 06:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 25f093c4-be9b-3222-83b9-ebd8217c75eb | -16.3157 | -52.8988 | 2025-08-12 06:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 167aada7-af9a-3022-937a-1e321489f9ad | -7.1299 | -60.1182 | 2025-08-12 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| bd8f1ee2-78e7-30cf-bed9-aee6e34fb23f | -3.9686 | -47.8684 | 2025-08-12 06:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 264ed325-753a-3ed2-9d35-746ced582152 | -16.3153 | -52.9201 | 2025-08-12 06:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| f4a3ffb3-2977-3f2d-b1a3-def6f162e96a | -3.9684 | -47.8901 | 2025-08-12 06:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 22d3320b-2998-309f-86a4-3bb8a4bbba93 | -6.5856 | -44.564 | 2025-08-12 06:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e2cd1ccd-c8fa-38dc-9c10-ae55dcdd7c7c | -17.6549 | -46.6757 | 2025-08-12 06:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 61f07a7e-818f-30c6-b89c-b816f85cf39e | -7.48485 | -68.34231 | 2025-08-12 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adba2d1c-fab2-383c-b18b-ab33f930316d | -7.48549 | -68.33733 | 2025-08-12 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08367e68-813c-3292-873b-d3c2e2b26be9 | -8.9489 | -68.50383 | 2025-08-12 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a1befa1-9f7a-3263-af43-202918d2e364 | -8.96255 | -68.80089 | 2025-08-12 06:40:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8923d789-edeb-3d89-b4ed-1555bce89e7f | -8.96167 | -68.79588 | 2025-08-12 06:40:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dea9d0b8-ecb9-351d-a91c-848ca4b258ec | -8.95523 | -68.50471 | 2025-08-12 06:40:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aee905a0-7817-3f09-ab6c-590fecd46ef8 | -8.96107 | -68.80085 | 2025-08-12 06:40:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c65ccbf9-cb95-3ba1-bb14-ca2a1580b6d6 | -16.2961 | -52.9016 | 2025-08-12 06:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| af3d1d51-4c2f-3b07-9f0b-ed753c95da4e | -16.3157 | -52.8988 | 2025-08-12 06:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 795f85fe-44fc-33ba-a4a2-77f066b9ff50 | -16.2957 | -52.923 | 2025-08-12 06:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 57950bc3-afe9-33a9-aa09-c7c18d8a2e97 | -12.555 | -47.0034 | 2025-08-12 06:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 84f4edaa-b800-326f-a73d-160475a7a371 | -12.5546 | -47.026 | 2025-08-12 06:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 4119248a-15ad-3668-82ed-4e4c3144d704 | -16.3153 | -52.9201 | 2025-08-12 06:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 4a15e34c-6579-3624-b564-1f5fe5884b21 | -3.9686 | -47.8684 | 2025-08-12 06:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fc93b5ee-c338-33d8-9a4a-751318a58fd2 | -7.1299 | -60.1182 | 2025-08-12 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 257981b9-b17d-3f0b-983b-c530d499cf2d | -6.5856 | -44.564 | 2025-08-12 06:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 84b76a3d-7da9-35f1-9b6c-3654e274a11a | -3.9684 | -47.8901 | 2025-08-12 06:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 9b5ba2f8-38ac-340d-9815-070b7fa686cb | -12.5546 | -47.026 | 2025-08-12 07:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f1cdbf32-b75f-3d3e-8b6a-535e06307894 | -7.1299 | -60.1182 | 2025-08-12 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a0194242-032f-3fb8-9445-878af5522e63 | -7.1483 | -60.1174 | 2025-08-12 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 2244c287-a33e-304d-a71b-864c4d97df88 | -12.555 | -47.0034 | 2025-08-12 07:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9c2ce6d3-2000-3d76-8f14-162f9dee9900 | -16.2957 | -52.923 | 2025-08-12 07:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1b41f484-933b-368c-b648-5c152e381899 | -16.2961 | -52.9016 | 2025-08-12 07:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 73b76cda-4d7d-3268-9c21-878580c4219d | -16.3153 | -52.9201 | 2025-08-12 07:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 012e9144-ecd2-3295-9cdb-12acdd7ff129 | -16.3157 | -52.8988 | 2025-08-12 07:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 55c9b73b-f3e9-3e1b-9b37-238c7f8289a8 | -6.5856 | -44.564 | 2025-08-12 07:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4447fcbc-3ebd-3e7c-a052-72c8153e533a | -3.9686 | -47.8684 | 2025-08-12 07:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f74f78e3-ec2d-38a9-8453-97bc847a5cb0 | -3.9684 | -47.8901 | 2025-08-12 07:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 24f40e87-6617-3424-b4c0-d120ab200046 | -17.6549 | -46.6757 | 2025-08-12 07:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 45ba667c-3af7-37db-9537-d8aeb8e2b9c8 | -7.1299 | -60.1182 | 2025-08-12 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 619ff37d-e769-362c-b0bf-b4962118b5f2 | -16.3157 | -52.8988 | 2025-08-12 07:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2c782a9e-409f-31c7-9f6e-fa79f95b4099 | -16.2961 | -52.9016 | 2025-08-12 07:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| d8a5ccea-bf24-310c-8f0c-60708a9a713a | -3.9686 | -47.8684 | 2025-08-12 07:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d15242c8-8c45-3a2b-af09-d669b86355c7 | -12.5546 | -47.026 | 2025-08-12 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| eee196c8-e778-36f9-bf73-27c08b2b7e02 | -12.555 | -47.0034 | 2025-08-12 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| aad1203d-0e48-36a6-9d7e-46eb754c16a7 | -6.5856 | -44.564 | 2025-08-12 07:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fda1d751-a132-3b2a-a513-cfa4a68fe115 | -3.9684 | -47.8901 | 2025-08-12 07:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 6b0638f8-844a-397d-94cf-5df622d4bda0 | -16.3153 | -52.9201 | 2025-08-12 07:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |


[Clique aqui para ver as próximas entradas](README38.md)
