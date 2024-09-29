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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b245115-b750-36db-8374-71a51c8a9cad | -15.93494 | -59.55974 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ec74c0e-bc4e-3cd2-98f8-7ba34c0dbd87 | -15.93453 | -59.55594 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9612682-276e-35a4-b587-8483f93b1363 | -15.931 | -59.55896 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2adcb0-9f3f-3404-9319-6d50d9162ea3 | -15.9306 | -59.55519 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddf16078-8fc7-35e2-949b-77f9b63ac450 | -15.92964 | -59.5604 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da52201-0a6a-3b8a-96c5-66839c4e0ebe | -15.92707 | -59.55819 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1890529b-a84f-3f1d-a841-8ade5ab88309 | -15.92667 | -59.55443 | 2024-09-29 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2bc89fe1-1d3d-3d8d-8b27-91916f03a210 | -11.52745 | -60.16218 | 2024-09-29 04:51:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b7adb69-0b4b-362e-b768-fb3f29d35e1a | -11.52668 | -60.16648 | 2024-09-29 04:51:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00641a1a-c59e-368e-8bfb-001c1ac9f144 | -11.52304 | -60.16142 | 2024-09-29 04:51:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61b34d7c-32b8-3701-85ab-71b8941ef32d | -11.52225 | -60.16577 | 2024-09-29 04:51:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61f0bb94-d341-3e62-9ea5-25887efcde7d | -11.51862 | -60.16072 | 2024-09-29 04:51:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1386db00-8887-3902-ab6a-62fe714a8e3b | -13.70761 | -60.69809 | 2024-09-29 04:51:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 579cd37c-178e-3693-9a6d-b5f09ee0e900 | -13.68729 | -60.68504 | 2024-09-29 04:51:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 689f4e09-4f6a-3fea-acb0-992a191cc2e4 | -9.97584 | -62.25364 | 2024-09-29 04:51:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 72483c56-bda8-30fc-a066-c266400b130a | -9.97064 | -62.25266 | 2024-09-29 04:51:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbdc9098-e2eb-3b8e-80e2-11ed7fe10840 | -12.04125 | -62.95658 | 2024-09-29 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92fd26bc-eb8c-3d8f-a0d4-305bb3b95368 | -12.99452 | -62.70286 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 553ffbc2-8a06-3fb2-8502-7cac661b2d83 | -12.99004 | -62.69876 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ee1f811-2e4c-3976-a685-9ad635f13ea0 | -12.98946 | -62.70181 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c5b1d87-064a-3475-8b54-fa00dc977f0d | -12.98887 | -62.70485 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0656e0-4c52-3239-94e2-31b8b79d3e0a | -12.98828 | -62.70792 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4237a7e8-5bf9-324d-a5b1-862cd017a379 | -12.98497 | -62.69772 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 582db9cb-4513-35bc-826c-526acfad7922 | -12.9838 | -62.70381 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 99e2d180-bc5d-3428-a1a5-dab90129fd0b | -12.98321 | -62.70688 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34a6395f-c452-3b46-a6b8-9169a59b5140 | -12.98261 | -62.70995 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b08db4f-af50-3faf-9a75-30ec4d68e85a | -12.97813 | -62.70584 | 2024-09-29 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08fca0ba-0e89-3157-b0d9-b6cb1f5cf7af | -12.87133 | -62.72504 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b21da23-ba97-36e5-a8ae-a912ebeee557 | -12.86536 | -62.75594 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 906585e2-8c91-3944-877e-773c2e670a18 | -12.86477 | -62.75903 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92b6dd9e-53a7-34b4-9d95-1e3f07e6a998 | -12.86417 | -62.76213 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f3f8fb8-bf21-36f0-bb0c-e81f514228a6 | -12.86297 | -62.76833 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da7d8aeb-0e11-3f2b-8a98-cc4556b33140 | -12.86237 | -62.77143 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a0bb752-346c-3e82-9131-8dc193200a4a | -12.86146 | -62.74871 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5df63c69-0f45-3f46-9347-e4c5948e313e | -12.86086 | -62.75181 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51eeca86-fb6e-3c6c-bf81-fa8d58b5ea25 | -12.86026 | -62.75491 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e15b2069-d624-3da6-bb3d-720cdf3e6e8b | -12.85726 | -62.77039 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc0caa8a-9d24-3945-b8b2-f4c3bbca07b9 | -12.78902 | -62.61609 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b0d8871-8d72-34c1-a320-be016c3ca84f | -12.78844 | -62.61913 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67454579-4248-3394-9f36-c35af32fe847 | -12.78455 | -62.61202 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0372a3e-3db2-3bf4-a493-96e421a2023a | -12.78396 | -62.61506 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b145fcd-42cf-3591-92d7-7f5a9ef42bba | -12.78338 | -62.6181 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6640e11d-f335-37eb-a00a-f7a2dd27fe3e | -12.77949 | -62.61098 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe30b5df-d329-3a60-9921-6c5e3adf7ecb | -12.7789 | -62.61403 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 714ec5f4-8fd9-3c9e-ab74-06e1fea9eeeb | -12.77714 | -62.76065 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4163c00-6b9b-3507-b6a0-accc25a916c5 | -12.77654 | -62.76377 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61409fff-9667-3669-ab5d-45c118efd884 | -12.77595 | -62.76688 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c5cf2a8-6efc-3499-8712-40dcf216fa1e | -12.77384 | -62.61297 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ae46b79-8c5b-3da5-bf28-d76756bf9c63 | -12.77325 | -62.61602 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9015e77d-be37-3116-b2d3-a044eeb9019b | -12.76879 | -62.6119 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62f8cadf-9dfd-35a9-ac89-6a9e1977745b | -12.7682 | -62.61495 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a0b3a6c-12bb-3f79-b5ad-24e0322e7ccf | -12.75519 | -62.79184 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fdd72d6-8de7-36ce-828d-04102f3ef01c | -12.65462 | -63.11841 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 164b2570-da31-3e3b-b45c-402898f476c8 | -11.64142 | -64.09476 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33bb849b-210c-3304-8424-66e1fbad13de | -11.6057 | -63.90442 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56622afd-554f-314f-bc32-c06c11ffed53 | -11.60494 | -63.90838 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2dd6e8a-24c6-3a73-ba35-25447b9bd099 | -11.60418 | -63.91232 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4c8f065-dcf3-3c89-81a3-79455286bd14 | -11.60162 | -63.8953 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13950783-7ef8-3b30-a0e4-8f787cd6a884 | -11.60086 | -63.89924 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea1ed18e-f86c-344b-b974-8a76ff61d6a3 | -11.60009 | -63.90318 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 723ac7e7-7a46-35e7-af77-a94d5e6f7eb5 | -11.59674 | -63.89031 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecc6c3a8-4aa7-3f7f-9b2c-c35896f89f75 | -11.59599 | -63.89419 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bfdb1009-51c0-37b0-96f4-170fe8f4e899 | -11.59526 | -63.71857 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1abb23fa-9def-33cc-bb44-c3df7de09ea4 | -11.59449 | -63.72252 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf5ec3c5-173d-3cc7-bac3-9d689c2d9339 | -11.59361 | -63.72703 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79c43577-4ff8-3de0-8ac5-44f55da66e5e | -11.59191 | -63.88514 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57d23393-2e8c-3a57-92bd-78ca27661458 | -11.59115 | -63.88906 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33ae08b8-cf32-31c7-b0b9-febae1b90947 | -11.59112 | -63.7102 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a83f3063-e5bd-341c-83cc-70ff9fce0cec | -11.58816 | -63.72533 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26bcd87c-0825-3c72-b242-57076d69868e | -11.58633 | -63.70522 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60c30ff3-bcfa-3e81-bc28-bdeb4bba72af | -11.5863 | -63.88396 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e6472d2-81c9-3a22-a51d-d01a185240b3 | -11.58067 | -63.88292 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef3f6f22-b5b4-3c0c-80e4-3ca94bd26c0f | -11.57823 | -63.74657 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3d819127-b9c6-3280-b8e6-e4a775c1c907 | -11.57737 | -63.75093 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b6987236-b5bf-39b9-8c01-5de66eafc718 | -11.57647 | -63.75555 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f9942f3d-8255-3f4e-9a74-d1a9539cb1bb | -11.56999 | -63.70746 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 243f6054-5cf9-3aef-b0c4-eb1721d978d6 | -11.56939 | -63.88094 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a768e214-1299-376d-a687-57bc69243c4b | -11.56887 | -63.70595 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a55bf5be-d61b-338a-af58-3002641dc564 | -11.56864 | -63.88476 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cfbba01-55fa-3062-852e-07c82f7eef90 | -11.56376 | -63.70987 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 024144ba-0a67-3541-8efa-bab0f4a9cd96 | -11.563 | -63.88375 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6416a7d1-def3-3237-af67-b09dccd5c05c | -11.56261 | -63.70843 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8442a673-4de3-3539-98b1-2bf7b8b72294 | -11.56197 | -63.71165 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c6c7bb1-07d0-3da0-b243-91b81da325b7 | -11.55802 | -63.70976 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d549158-5a61-320d-bbb5-472492190832 | -11.54463 | -63.88807 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf3fecd9-2e9e-3894-9c26-11ca2b55fd32 | -11.54388 | -63.89186 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f90df731-8269-3aea-af0a-25155a8908f6 | -10.95397 | -63.59092 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49f339de-9a27-323f-9c3b-0f71f7c36e6c | -10.95341 | -63.59374 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 270590bf-21ce-3966-94ba-e098dfeda493 | -10.95281 | -63.59686 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 785449e6-4086-337a-afa4-9806d5160923 | -10.95212 | -63.60038 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51ab18a2-7037-3342-8950-739a3f3a3a7a | -10.94939 | -63.59403 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a411fb2-7cd8-358f-a78b-596e6e07dc89 | -10.9488 | -63.59715 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 226ccd0b-9f05-3cbe-a0c4-8bd4340b7423 | -10.94822 | -63.60024 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9a4a0e4b-828c-3d42-a2ea-9cfaec115c7f | -10.94749 | -63.59446 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 537b6bf0-6335-305e-801b-7676b696ee50 | -10.94689 | -63.59751 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 087b738e-ac41-35e3-83f6-40ca7ca75ef6 | -10.94633 | -63.60041 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 855d6e5a-e14f-3e17-b9fd-3209268a4470 | -12.32962 | -63.72062 | 2024-09-29 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e67df23f-4968-3e6c-b330-e447a11949d5 | -12.32951 | -63.71982 | 2024-09-29 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6959c4cd-f8f8-396d-8fcb-6374edb77e3f | -12.32892 | -63.7243 | 2024-09-29 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8609d4e-3652-36a8-8716-b64f979489f0 | -12.32878 | -63.72349 | 2024-09-29 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README62.md)
