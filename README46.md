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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a15ee4bc-6ddd-3d1e-be5f-8584e6c661cb | -19.56429 | -56.66439 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c35b1fd5-9587-3f3e-a6af-7d71060c5b87 | -19.56368 | -56.66809 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cf285058-50a5-3e52-87b4-e710bc35ea38 | -19.56308 | -56.6718 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| afee5dbb-50a4-3aff-a58c-68f87d2429db | -19.56248 | -56.67551 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 24c58ad7-efb3-3b44-af50-ccd030fb217c | -19.56096 | -56.66378 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| df3e2c52-863b-302b-9552-2ddd3f3e036c | -19.56035 | -56.6675 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b977253e-d4b9-3794-80cf-e240f8354c7d | -19.55975 | -56.6712 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bfb7b4b0-645d-3650-b482-5076448e9d94 | -19.55914 | -56.67491 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9b249b2e-a260-3573-800f-7469fb29712a | -19.55854 | -56.67862 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 41e1476f-8581-3f54-adfc-22ab289c12bb | -19.55793 | -56.68233 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d9cfa10d-4281-3bc3-8604-258e011fb7cd | -19.55762 | -56.66319 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c97d9df7-f992-3d88-aa71-da0ef0a2c6c1 | -19.55733 | -56.68604 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 43c9aee1-f578-39f3-beaf-60beb4bfc8b8 | -19.55702 | -56.6669 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 16cb3540-0cf0-377d-83ff-0ffff17272d7 | -19.55642 | -56.6706 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c11124df-7712-3575-b8de-3e5ac74026ff | -19.55581 | -56.67431 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c0556e44-c868-3511-8df2-7fbe04469cef | -19.55551 | -56.69717 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23a685a9-8cce-371f-a371-b650b62fdf02 | -19.5552 | -56.67802 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 847c85aa-7380-3a5c-80e7-8f47c8bb9bae | -19.5546 | -56.68173 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 475ceb80-5768-3ab0-9c82-e8d8efb1d3bb | -19.55429 | -56.66259 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6f868f4f-e443-3542-bcc9-ce0546324644 | -19.55399 | -56.68544 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c395fc41-00b6-3651-9245-2b667c5f3afd | -19.55369 | -56.66629 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| daed43ae-9452-312b-9056-100e7cacbe1b | -19.55339 | -56.68915 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1258dbc2-038f-3bed-939e-038d58eeeec7 | -19.55308 | -56.67 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 672fc04b-5073-3835-98d2-c0f365e7516f | -19.55278 | -56.69286 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e1a656af-e89b-36cc-955e-7915d719930f | -19.55248 | -56.67371 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 083c9a84-01e7-3df2-a560-49c89a6470b0 | -19.55218 | -56.69658 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 04c6cc85-72cc-3a86-9860-27b0116ac5a1 | -19.55187 | -56.67742 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 895a5d3b-be7c-3e95-93a4-b7d4856c2b53 | -19.55126 | -56.68113 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 100cee54-7845-39b4-b724-d1f80a9a477d | -19.55096 | -56.66199 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e426b6d3-bb5f-3111-ba9c-5cce49da1911 | -19.55066 | -56.68484 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 0140ed84-e001-3c4a-b63d-04d60a83f504 | -19.55036 | -56.6657 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3035219e-039f-3c55-b041-1dd398b6b9eb | -19.55005 | -56.68855 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 799cf0ea-ff12-3746-80a4-fe5302ca05fa | -19.54975 | -56.6694 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 45e4c3ef-975e-333c-8e11-a105d675ca93 | -19.54945 | -56.69226 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 24edc275-04b0-3ef8-b41b-1f0b626cb733 | -19.54914 | -56.67311 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 84e4af88-91b1-3211-9ea1-1be21b7abf5e | -19.54884 | -56.69598 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 85dd4d27-edef-3565-b497-ec0efcd4e4eb | -19.54854 | -56.67682 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 583cdbf3-0f13-323c-b491-322f45122f03 | -19.54793 | -56.68053 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| bc9649fc-f538-31da-a2d4-2beadbb8c936 | -19.54733 | -56.68424 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| aa9b73ad-a77a-3bf2-b8cd-b4854b2e282b | -19.54702 | -56.6651 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a2c45596-a142-3ed9-8c29-bc42fd231260 | -19.54672 | -56.68795 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 3acb3c22-d41f-3abc-a3b4-e1527ac274b7 | -19.54642 | -56.6688 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 8a8c657c-b485-3bd5-b4dc-f2b2e0300a32 | -19.54611 | -56.69166 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 351c669a-4c68-3bdb-8b5b-437f495ad590 | -19.54581 | -56.67252 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 535a8d33-fa1a-3d78-9f41-14904355d14f | -19.54551 | -56.69537 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| d677d13c-a4c4-3eab-b3a0-572566bc91ab | -19.5452 | -56.67622 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 04579dea-1396-3a6c-b735-5f287d9dbe0e | -19.5446 | -56.67993 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| f64081cd-d9c0-318e-8cb6-944eaaa5a09e | -19.54399 | -56.68364 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 4d44f4c1-9f8a-347d-ac58-1c8936d909f5 | -19.54369 | -56.6645 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 312c5546-5781-3711-9e2a-7908b7d27156 | -19.54339 | -56.68735 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| e65e10a2-8c46-38f1-b790-214d03af8135 | -19.54309 | -56.66821 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 3fb91c80-2140-399a-9515-edb4201b3d77 | -19.54278 | -56.69106 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 3d6f21d5-f088-359b-b093-0e7a6a38af1a | -19.54248 | -56.67191 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 60f588c1-64d7-36bb-acad-ad95c06c6a0c | -19.54217 | -56.69477 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| a830c9d3-d29b-3535-93a6-9064ea354ac0 | -19.54187 | -56.67562 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 59d58a21-b0f2-3eff-b38a-0728368acacb | -19.54127 | -56.67933 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8d86486b-6fb1-3fb6-a113-5f0bbe641dbf | -19.54036 | -56.66389 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 363cb142-c6aa-30c5-9bb1-8d72804cf1e3 | -19.53975 | -56.6676 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| c84b1bd1-cb42-3999-b788-b35adff7e749 | -19.53944 | -56.69046 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 2ec4191d-6174-3a5f-98a5-8937918dabb2 | -19.53915 | -56.67131 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 4d5e315c-c283-32d5-ac50-9993ff834c09 | -19.53854 | -56.67503 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 99f33ec4-e849-3730-afd5-628897ca6405 | -19.53793 | -56.67873 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9e0a008c-68a7-3028-813e-c0c32f1dd5ac | -19.53732 | -56.68244 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b7ebe844-a477-3b98-b1ef-35ff47243d0b | -19.53703 | -56.6633 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 5c830d9b-89b6-3524-abd2-c4837270deb7 | -19.53642 | -56.66701 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 9a049910-d1b5-3bd1-a517-0f90b873f00e | -19.53581 | -56.67072 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| d0e7f079-6221-3a45-8839-1c53c829b128 | -19.53521 | -56.67442 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a4c07cca-fe62-3fda-8122-4251d4e8da92 | -19.5346 | -56.67813 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b4248bec-b923-3e12-8cf1-0710980cbd9f | -19.53428 | -56.6633 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 29745dc2-00e9-3bfb-8aaa-00f574ff8800 | -19.53399 | -56.68184 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 35f4e9fe-7cf3-30e4-9504-10687cc7d675 | -19.53368 | -56.66701 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2940350a-a9a2-3029-878e-965647ca6e22 | -19.53308 | -56.67073 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d653083b-02c6-3f5b-9ffa-8d31076c3f75 | -19.53248 | -56.67444 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bab606a3-8438-377f-8135-849745b995dd | -19.53188 | -56.67815 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d5bfb8e0-97f9-3a0f-b2a9-a28fdfe4a29e | -19.53128 | -56.68187 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4044be92-19e6-375d-bf45-193c4c6b1fa0 | -19.53095 | -56.6627 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b3ad04da-e3e9-3a3c-9b7a-5ce6802b6289 | -19.53035 | -56.66641 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c4d21f21-c04c-39e5-b3ff-979334690e4e | -19.52975 | -56.67012 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d1190588-04c8-3749-8ca9-356cc0175457 | -19.52914 | -56.67384 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9d281c73-f332-30e1-9242-79434e146376 | -19.52761 | -56.6621 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 87d949fe-3614-3c82-a69e-603263848c45 | -19.52701 | -56.66581 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| af3c977e-dbe4-32ca-abef-9e9cb45a87ce | -19.52641 | -56.66952 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 20955185-706c-300b-89fe-e0af010710f4 | -19.56548 | -56.61501 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fb87fed2-ac5f-31c6-98e3-e49317238aa2 | -19.5649 | -56.66068 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6f434054-c7c0-38bd-91fd-789f55200012 | -19.56215 | -56.61442 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fbdff0b5-5f72-3ddf-bcbf-8a360b41ea9e | -19.56156 | -56.66008 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 997f4f32-0b74-3e10-a7e2-668892b1bcd5 | -19.56155 | -56.61812 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| af65f6be-30d3-3841-b3da-bfe937d8f996 | -19.55884 | -56.65577 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b662d4a6-eb8b-39bd-8cad-940c3507cac0 | -19.55823 | -56.65948 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e27bdda6-a653-3ccd-8d9d-25b6e718b83f | -19.55822 | -56.61752 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 104807cc-3584-335e-adf2-d54f903bab01 | -19.55732 | -56.64405 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7253b31a-dcf4-3e30-9437-38ea8eb19bb5 | -19.55672 | -56.64775 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d9af85e8-4dfe-33d1-8753-40400be66830 | -19.55611 | -56.65146 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 85c41d18-099f-3589-a25c-ef4888e6489e | -19.5549 | -56.65888 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a1473485-09be-3d14-b559-4c56abaeca6d | -19.55489 | -56.61692 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cb22dfe9-f79c-3881-aedd-c4f6253163e0 | -19.55459 | -56.63974 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 56709d98-6bb1-3054-9eb0-e3dd959a1591 | -19.55399 | -56.64345 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 836b9a75-de94-3081-bdb8-f02a8e3e4d4a | -19.55276 | -56.60892 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b4dd87a0-eb61-3703-bff4-ebe4eed0dbc1 | -19.55216 | -56.61263 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| eb27f80e-4173-3487-9151-fe1da8d9a926 | -19.55157 | -56.65828 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README47.md)
