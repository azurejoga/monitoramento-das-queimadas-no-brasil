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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aeb5441-9c96-30b9-ac91-0130114c79c9 | -1.2534 | -55.88083 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 493e3b85-97ff-3fba-a354-a8bd54ec6518 | -2.93875 | -58.32179 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00ed46be-c712-3808-a4d6-34d82b1409be | -9.48178 | -68.94812 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b56aa8e3-59b8-3af7-85d1-c0fab7e8e62e | -8.63126 | -66.99803 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 67c74a47-7422-3235-af81-842ae2ecd495 | -1.7886 | -66.55038 | 2026-10-05 17:37:00 | NOAA-20 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 220ba2e4-6d71-35a8-be1c-c5b9ad602f52 | -2.54296 | -65.86996 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| e50a81d4-704f-3802-a644-04878a49fd79 | -9.38676 | -68.32787 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cad74597-bac7-3fed-b930-2b1a5ea76543 | -5.66166 | -49.21881 | 2026-10-05 17:37:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69d87807-3625-3000-adbf-743ef0e8167c | -1.9657 | -56.69907 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1e096abb-fd01-32e7-a838-a1913ae2686a | -7.12167 | -55.72689 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8d64f085-5d3d-3860-9326-9e8f68857a85 | -9.91407 | -65.01832 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8a3d5272-119e-312e-bce5-d8caebf73adf | -2.01116 | -66.31654 | 2026-10-05 17:37:00 | NOAA-20 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4229f406-3a7c-3f19-9008-506ff08bac2d | -9.10049 | -67.75093 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e33f3636-f9f1-307c-9805-e7ffc64a38f5 | -9.47982 | -67.06709 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| beaf41b5-adf4-3565-88e7-3197982389c0 | -9.23844 | -65.57828 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 85c4099c-f6f7-36e1-8922-d9edd47086d6 | -8.59134 | -66.80855 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac2350a3-6d33-3dec-981b-6f15e26996ea | -0.71869 | -57.96758 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2994d94-e192-3258-9807-9cc742add07c | -9.44017 | -67.09893 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eaba5473-184a-3661-9778-ee0b8487f205 | -1.22437 | -56.20609 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b4bb9d9-fbbe-3d60-8436-7edd8e1ecb9b | -8.52022 | -67.00539 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 87f1c1cf-640c-3e99-a069-5e468408a605 | -8.6006 | -66.8073 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c38cafbc-661a-34ba-bcf5-873154af988a | -3.08654 | -69.20081 | 2026-10-05 17:37:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5f2907af-9cfc-3881-9959-a0d9d4a532db | 4.20763 | -60.71324 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 05bb895a-2339-3ad3-907f-7e0cebe649bb | -9.10807 | -67.69203 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f836d889-1ba1-3d64-93cb-454565891af4 | -7.23036 | -55.19843 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 59baaca5-930e-363f-97ca-5801f77ca139 | -9.14314 | -68.99014 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24af8844-f573-3b4f-ae46-a9d3cd15e6b5 | -8.92334 | -68.74931 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9ce16768-997e-3cdc-b67d-a00ebd001d78 | -0.73975 | -57.98221 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 469163c5-34d5-3081-9f52-49210cefc32e | -9.54914 | -68.5481 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4865a07-abe3-3c8f-910e-aa1c4f0d364d | -1.67127 | -55.06124 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e4bbccf-0a63-3349-948c-28e340bf85ea | 4.26671 | -60.34258 | 2026-10-05 17:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f667cf6-99ee-38c2-b825-3dcdf575f5f0 | -10.27424 | -68.07988 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8402cac9-7d84-3c1d-95fa-b3afe4d4fa89 | -3.32802 | -62.60719 | 2026-10-05 17:37:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1dea0b12-43b1-3483-ba37-1c6e5ba8fcf7 | -10.17659 | -69.33492 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3ef96d55-7235-3ef6-818c-9bfd63c9d1f2 | -1.61539 | -55.10421 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 09955a3a-77a8-3936-854c-2664809110bb | 1.79063 | -55.54449 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 78bd7791-316a-3592-b7bf-07c2e7bd3d3d | 3.5739 | -61.33897 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6057084d-81e1-34ee-b36b-59b84a7cace7 | -2.76626 | -57.66437 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 7b112d5a-c687-3ad7-ba8b-a80e020f4931 | -8.62723 | -67.0036 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 675d8232-a4b3-3073-8b42-2d98d84e374d | 1.17387 | -50.76848 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8753d1f0-1244-3a3f-9729-ffa45435523a | -2.89576 | -58.16097 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 328016e1-c1da-3d21-bb75-d59030520815 | -9.2753 | -68.37479 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8efdc097-72ad-378e-b7f9-0e49435ee374 | -9.12632 | -68.29553 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0230e5e2-9d2d-376c-8d21-f18be24a1475 | -9.07756 | -72.20322 | 2026-10-05 17:37:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f178ef16-2b2b-3b1d-b363-2616b50bad7c | -1.73635 | -55.34803 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0bf1e68f-4222-37e1-917d-5f513b31c929 | -9.01851 | -67.74796 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2d8a9eec-ed2c-3665-9cff-bd9875d783f5 | -2.55486 | -65.86818 | 2026-10-05 17:37:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 3a8da8b8-e62f-3a77-bbdd-8bd11b8ea712 | -7.32557 | -55.75495 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3cee30c8-9ca2-30a9-a7c5-23dc056edbd0 | -8.85915 | -66.78989 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2e57872e-cb2e-3792-8a9e-87b5df87fa5d | -10.6629 | -69.11688 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ea109cf-24f7-3bfd-98eb-e40b4293d133 | -9.56548 | -67.80032 | 2026-10-05 17:37:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d1c9228-6766-3995-a058-6a2e52226c30 | 3.42417 | -51.32075 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 946c741c-ce5b-3151-8280-29fbc286b74a | -10.40403 | -67.8297 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6596ab55-7cba-3247-87b9-d42f6f49300a | -9.1273 | -64.38006 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 957f94fe-9557-3979-8c13-ca101f9fc548 | -9.10804 | -65.35835 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bd9b4fa6-348a-3eec-b7cd-511c45b14590 | -8.6016 | -67.13527 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c397d3a3-985c-325f-848a-cd4b59992dad | -8.8392 | -67.38639 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b2506da-a3b1-3513-a657-47438c0d8336 | -9.14946 | -68.2324 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b29119de-e7ed-35aa-8164-c88a3cf2481c | -3.08618 | -69.20206 | 2026-10-05 17:37:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| afe66e34-b005-3203-baaa-8ff601e6b011 | -1.72668 | -55.36127 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 4e39d393-685b-32a2-859d-847aa15633fe | -9.40289 | -65.88601 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 60b0c059-b56e-3070-b377-eefb4916fcad | -2.60421 | -57.55981 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b045e72-9da7-3353-a55a-7a10944f1abc | -3.6668 | -69.43759 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19f7d6a8-3c58-3637-b7ed-afdde5b464ff | 0.31492 | -50.99619 | 2026-10-05 17:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf584916-482c-3ed8-af8f-740ea492a5b3 | -1.6211 | -55.11201 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d82625ea-cd1e-349e-9f34-cdb8f9b67e85 | -9.13595 | -64.38407 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a50b68f-3157-3101-b64d-2a71da1ffa6a | -10.40397 | -68.55802 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1766c3bb-4fee-31fb-8acc-d2804e4b0465 | -9.10039 | -67.75416 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e3e989fb-91a7-3950-b630-d7e1ffadaf8e | -10.26306 | -67.99285 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 400509d3-c26d-3cdd-9c0f-9a2ba67ad01a | -9.05967 | -66.09685 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5673517d-cf4c-36ad-81dd-a078a2f8091d | -0.73455 | -57.97857 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9a6c8ccc-f70e-3817-b062-7cf3b02fa9b6 | -1.62882 | -55.13236 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c5f7baa6-4c07-3375-992a-88249f53afd5 | 1.9847 | -60.61178 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 64bec30c-26bc-3131-9588-efa83174ae9e | -3.62088 | -64.34294 | 2026-10-05 17:37:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57748b92-493a-3939-87a3-6d6622749d99 | 1.45572 | -55.65417 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 93a4b597-c5b9-36e8-876a-30eada555d66 | -8.79518 | -69.2438 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 17f743e2-76f0-33b4-901f-0f86ba256d18 | -1.62815 | -55.12819 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 25a95a26-3d30-3e0e-8aaa-292c190afe0b | -7.22949 | -55.19327 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ce954425-1204-3522-a2d1-f4a76b1f4f9c | -8.84072 | -67.38835 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a87ceccf-ed64-3608-8c38-2d790468ef42 | -2.95562 | -59.16071 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f498b2bb-2acf-3e90-bf33-8445da09f47c | -9.1214 | -67.8345 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6ddf3a2a-b851-3c5a-b589-2b8674a4870a | -10.06427 | -68.23312 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c35fb44e-e734-38ad-8096-4ee704924159 | -8.64473 | -67.02663 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 79f6cf1c-defd-3865-9b87-87f2d329a984 | -9.88284 | -64.17709 | 2026-10-05 17:37:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fc3b648a-0adf-3e51-bcac-69f71a7f8a0a | 3.95202 | -59.85933 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| abb43c94-f9df-3633-8d45-8b1fc9f45e02 | 3.52782 | -51.51083 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e84f49b-d791-3cee-93e9-2f5304fd32fd | -8.83031 | -67.38428 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b7d90538-2c41-3b51-81a9-dff9c26458c5 | -8.91918 | -68.74971 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d3dcab63-44cb-3164-ab56-e53f733e95d8 | -9.04928 | -72.33341 | 2026-10-05 17:37:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b160c36-5393-33df-99b7-fc1950ed0889 | -9.39962 | -65.89519 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 35636052-ea5b-3535-905c-91e1b6e1440e | -8.99946 | -65.69299 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60bfe16c-f08e-3629-b028-738c9ff00467 | 1.88349 | -55.73958 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 505360e5-4105-31ae-bb5a-da706fa0c380 | -9.41421 | -68.86494 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c0d73d29-9de3-39c7-963d-ec7551fc1638 | -9.33967 | -64.71131 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 886fd5d7-b9bc-37fc-a678-bb74d67e4260 | 1.98415 | -60.61538 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f0f7b14f-4cf8-3f36-a879-44a80c10a5a2 | -10.46789 | -68.67503 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a0301f5-141a-31cb-8d83-783376966a63 | -9.07804 | -66.09883 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 674a5e5d-fd93-39d5-8d62-e93cd6517f59 | -9.08188 | -66.09382 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 058ea605-6454-3b2c-8ecb-4a4cd9795430 | -9.13611 | -67.75195 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 956e224e-2e49-3476-9d3d-b05fbccab2ce | -2.66566 | -57.28108 | 2026-10-05 17:37:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |


[Clique aqui para ver as próximas entradas](README155.md)
