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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 383e67d8-f33b-3427-aeb6-aa0021c370b9 | -7.5728 | -55.15387 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de81d85-0ce1-3829-bf86-da3db5608d1a | -7.57225 | -55.15734 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72b70379-32a2-3caa-b718-b65ee1187172 | -7.5717 | -55.16081 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fda05100-962e-3abd-892d-3f9cd215494a | -7.57114 | -55.16431 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02fced92-bda2-3ce6-884c-c03dc0110a08 | -7.57058 | -55.16783 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c6c8281-a84a-3b66-8887-5d4026f835aa | -7.57002 | -55.17136 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a646fab-fe63-32e3-b5a1-d3a12f7e8a98 | -7.56838 | -55.16031 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 024be641-df28-3ef2-9750-7ddee1cea47b | -7.56782 | -55.1638 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b680a90b-ea7c-33bd-99cb-5a15bbd53384 | -7.56727 | -55.16732 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd58154a-d2f6-372e-97ae-4ebbb045ceb9 | -7.56671 | -55.17084 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 616757b6-e4e1-31c7-8c74-609102b1c1af | -7.5645 | -55.1633 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9ab98abd-b096-3507-b1c6-0ffcd63df4ee | -7.56395 | -55.16681 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 270df07b-93b1-303d-a124-a9982e36d177 | -7.56234 | -55.0914 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc098d33-8ce0-3d08-b1ac-6c12de9fa503 | -7.56121 | -55.11984 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 949494fc-610e-3513-8fef-09bc77a8f300 | -7.56011 | -55.12681 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9bd26a-fbfb-39a8-b357-3e74b035e277 | -7.55957 | -55.08741 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3122fba-5ca4-3485-9794-492125044ad8 | -7.55954 | -55.15177 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01a69a05-24fd-3a8f-96a8-b12f9a5fde4d | -7.55902 | -55.09088 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ae7fdd2-a7e2-3e0c-801a-69a6965e5834 | -7.55898 | -55.15526 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fc09c47-9d23-39e8-9518-2c210aff6ba3 | -7.55846 | -55.11581 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5736287a-798b-3f59-a8cd-785162d5b523 | -7.5579 | -55.11931 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 85324b88-337d-3dfe-ab32-b520baa610b6 | -7.55735 | -55.1228 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a4acebf-1cfb-307e-946b-ab53cc5b8a99 | -7.55679 | -55.12628 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c52846a-2e22-355e-86b1-1adafafbcff8 | -7.55623 | -55.15123 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e458bc4-82b7-3a4c-8345-01200b931d1e | -7.55567 | -55.15473 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b680ead1-5e67-3ae3-97b4-4617f0f8c365 | -7.55511 | -55.15823 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2413b99f-3444-3eed-a177-4d7bec4d3451 | -7.55459 | -55.11879 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf8e8938-6371-39ff-bda6-0607868db4ed | -7.55402 | -55.14373 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8a28600-a326-3ba8-aa75-9be61d414dc2 | -7.55347 | -55.14722 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15457e42-bc15-35cc-8ddd-df95d5cee4d3 | -7.55291 | -55.15071 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3e55d3c-a683-3f84-a4c0-bd69a480d281 | -7.5524 | -55.08984 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbb38718-42cd-32b5-845c-4c8005574585 | -7.55236 | -55.15421 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bded9f14-648c-3bb7-ac70-95e4f3aa5d1c | -7.55182 | -55.13623 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 225d1b46-c52e-36f5-ab19-1e876bbc304b | -7.55126 | -55.13972 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc7234d0-328d-316b-b3d4-13f867270d93 | -7.55071 | -55.14321 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edcbab12-f893-396c-ba4c-3d08513eae84 | -7.54904 | -55.15369 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f4fd33a-af2d-3026-a9b5-04ae3af177e7 | -7.54795 | -55.13919 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fcbbf63-5aea-3a07-b5bb-6ed6a570073a | -7.54243 | -55.13116 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7bef91a-bee8-3540-8d3d-12ff80803905 | -7.53967 | -55.12715 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 151efec4-adb7-36ae-878c-6afbea89170f | -7.53911 | -55.13064 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60a81199-d7c4-35a9-a9f8-ceed91d9f3f4 | -7.53636 | -55.12663 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bacc5d3-bb2c-3e98-9102-9f46603f5058 | -7.5336 | -55.1226 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab05045a-89a0-3f6e-8779-a889eee839a4 | -7.53304 | -55.12609 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d49eb9be-8be4-3213-b21e-4a0f3496253c | -7.49243 | -55.16631 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85a35978-3a79-3a89-a1b7-3bf686097a38 | -7.47861 | -55.18921 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98dc33d4-bcb3-33ca-9311-35dd489246fd | -7.47529 | -55.18867 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08ad144a-1448-3697-bf98-3cbcdcdea6db | -7.44941 | -54.94522 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b058b95-a51c-3dbf-9ce2-1e538b12d150 | -7.40506 | -55.20255 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c55f645-2de3-3f7a-9ce1-efd69e308045 | -7.4045 | -55.20603 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d03d145-b076-3d6e-96fb-5ea69bc10de9 | -7.38843 | -54.89986 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52a70957-cfbc-3bd3-8750-b9d748354116 | -7.38518 | -55.1134 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072990ad-07cb-3227-b79a-13fc46a64704 | -7.38462 | -55.11689 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 725e2b1a-d81a-3416-af3d-64d6b4e97ecb | -7.38241 | -55.10938 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6725e3c-d505-3aa5-bc8d-413d28e134c8 | -7.3197 | -54.92395 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03925dd0-b4d9-3d7a-b243-5a16a829d457 | -7.31142 | -54.91196 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f30d5d31-86ad-3248-8527-947b53e9cbc1 | -7.30811 | -54.91144 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e7ce080-08b0-33a2-a8bf-5c619d88e413 | -7.30756 | -54.91492 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4daaeb7-f722-3b7f-85e4-876003359cce | -7.30701 | -54.91839 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69f8ecd0-8362-3c66-829d-ea828af7db84 | -7.3048 | -54.91092 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b8a7879-9b45-30c3-897b-cdf0d80aaf91 | -7.30425 | -54.9144 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdb5780d-5f40-3398-9827-c378c6ff008e | -7.30315 | -54.92135 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b520c4c4-84e3-380f-a705-33c6d4f29c1b | -7.30095 | -54.91388 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32b28519-225a-3442-8873-e9f12347660e | -7.18104 | -55.02678 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75befb5a-a53e-31cd-a6e8-539b9f66afc8 | -7.17827 | -55.02278 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74e1ae9d-b265-3071-9923-71bcc90edb14 | -7.17772 | -55.02626 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 234a0520-788c-3381-a908-94c120c887e7 | -7.17717 | -55.02974 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30be8511-c115-386e-98de-dd9c7bcddf9e | -7.17662 | -55.03323 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 876aca6f-de0c-3282-9c6f-d31a0739f36e | -7.17607 | -55.03672 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcc180ed-3608-3ed8-b8ba-99cb6a5d4428 | -7.17552 | -55.04021 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aca6e33a-09ed-3fcd-9dce-78e44f914886 | -7.17386 | -55.05069 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77d7784e-dd87-3dde-ab9b-004e756721f2 | -7.17386 | -55.02922 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d94ceda-4f10-3e72-9fe4-345ae83b5631 | -7.17331 | -55.03271 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a22cd475-a6d2-3593-828d-bfff25231a19 | -7.17275 | -55.0362 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adba9fb3-20f7-33b2-95bc-8ba893b335b0 | -7.1722 | -55.03969 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b4ca61-f2eb-37b3-8107-892e178ff3ba | -7.65963 | -54.99343 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2a3256e-06ce-3e5c-9bc4-a0e4d59429f9 | -7.61975 | -55.17925 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1c05dfb-37d1-3a60-9dfa-db0e78d9f2d9 | -7.61644 | -55.17873 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24ed489c-3163-3f6a-9a45-2edd2f7e3d87 | -7.61257 | -55.1602 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bfbd03b-5d7f-37e0-959b-cc42233b056b | -7.60925 | -55.15968 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb2be38f-a1f4-3dd3-a2ed-ea37bda3dd57 | -7.60207 | -55.16213 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4116ded3-8f87-3e97-b5ac-c4e5e10f53ce | -7.60152 | -55.16563 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad4ae1bf-7fa1-309c-a508-731f3b3a9542 | -7.59931 | -55.1796 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2705abad-4275-3ee7-b460-7b66a0e7a113 | -7.59876 | -55.16159 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee974e14-b047-3ef2-b279-26d662cf4fd8 | -7.59875 | -55.18309 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b4c2363-82c0-381a-a23a-6df07ee02402 | -7.5982 | -55.18658 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3a2adb5-9c2f-3dd3-b3b6-77663e674661 | -7.5982 | -55.1651 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7de95911-2c7a-3f6f-9842-ab3fb2e3bfa1 | -7.59765 | -55.19008 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfdf115f-0f9c-3256-97ed-c0eb0bdef607 | -7.59765 | -55.16859 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3344ae3a-4ead-3718-9071-255c4e36e318 | -7.59654 | -55.17559 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 859ca609-86e0-3406-a662-812f3900cdd7 | -7.59599 | -55.17908 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8eb0201-f1d9-3667-a15f-69f52e0a2ff8 | -7.59545 | -55.16105 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 320e644e-b3b7-3ac9-af5f-ef8f7ebca7e4 | -7.59544 | -55.18257 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe5ef71-4263-3559-9b45-f52dbbe53903 | -7.59489 | -55.18607 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e8901a2-8226-3093-8f93-8d1b945b173a | -7.59434 | -55.16806 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc5816d-601a-3abf-9f0b-88142db4d160 | -7.59378 | -55.17157 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3558eb9c-ba65-3e7e-91c3-8cf7853b4bd3 | -7.59323 | -55.17506 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1aeb5e5-8406-3f19-b1cd-e664b56fc4dd | -7.59212 | -55.18204 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27ae2543-dde0-3861-b190-90115647ee91 | -7.59047 | -55.17104 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 134757e3-159c-3204-be1a-dcc6f3501349 | -7.59046 | -55.19252 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 823b89b7-25ab-3958-9cd1-afd2cdedfba1 | -7.58881 | -55.18152 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README102.md)
