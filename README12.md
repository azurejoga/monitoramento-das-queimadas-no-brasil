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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b99c3f89-76e1-39e1-87d4-05580b856862 | -17.21799 | -44.82613 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27d2a206-d71f-3980-af28-d950bfb485f6 | -19.08708 | -40.1394 | 2025-08-05 03:51:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c98679c1-1239-3f0e-946a-d9d70c1c4ebd | -18.85236 | -40.45903 | 2025-08-05 03:51:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 64524fe0-5b40-3217-89c8-cb216b029cd6 | -17.22145 | -44.83025 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3337f8ab-fb7d-3f7c-8921-957062e91355 | -17.3409 | -39.58791 | 2025-08-05 03:51:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ddb5e771-750c-3e9b-a3ff-e88dca6c7ef2 | -16.0791 | -43.62753 | 2025-08-05 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91ec2fde-1380-3748-9d12-7c8fcbd621ea | -16.08206 | -43.63315 | 2025-08-05 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 462831ce-fb4f-3a6a-87a4-da10545d5322 | -17.36378 | -46.08671 | 2025-08-05 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3727a131-030a-37aa-91de-2fad1efd63f4 | -15.38743 | -40.84142 | 2025-08-05 03:51:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec45f89b-7a4c-36b6-a460-8d5e5a3f10fe | -17.22215 | -44.82653 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11ad0ac7-f4ea-3a89-bc72-41aa8e6035c5 | -20.22463 | -43.80317 | 2025-08-05 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7fede3f2-8e87-3d71-a20e-1b27292d545c | -17.21259 | -44.83281 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 0218ead8-f899-3555-a2b0-625b073b7ed5 | -17.21741 | -44.82948 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1b35e196-666b-30bb-888a-7f34db29d304 | -17.2207 | -44.83439 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a1f0beb1-0c3a-395b-aa01-2481cdfa8c48 | -21.16632 | -44.53846 | 2025-08-05 03:51:00 | NOAA-21 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| af1f1740-072f-3fae-b00a-4d4e5c723581 | -15.65075 | -41.24958 | 2025-08-05 03:51:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42cc7e8a-9cb0-31c1-bc3f-c041b18732f4 | -19.99486 | -45.76839 | 2025-08-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11c625e8-0785-33b8-9db2-c659f7a1f1b3 | -21.35291 | -42.66383 | 2025-08-05 03:51:00 | NOAA-21 | CATAGUASES | MINAS GERAIS | Brasil | 3115300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 967f8307-df06-35cc-b6ca-98ab5edba7ad | -17.21192 | -44.83654 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6790fef2-6daf-3cf7-8f2b-870a9541f758 | -18.85568 | -40.45962 | 2025-08-05 03:51:00 | NOAA-21 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1dac1b4e-9036-3360-8224-b8a596897bec | -17.21732 | -44.82987 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d9fa9747-1572-3963-b773-0ae7187e45ce | -17.2181 | -44.82575 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64ee0a9d-4dc7-3923-8428-1be1df0ab2b3 | -17.21664 | -44.8336 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 050e11a5-84e6-332b-a18f-9e4dba788264 | -17.20922 | -44.82828 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| de8a5f5b-8601-339a-a0db-0c3d48049925 | -17.2188 | -44.82203 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16292aa5-71e4-3098-a46a-4c753e8c6a6b | -17.72003 | -42.95759 | 2025-08-05 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25b548ae-6a06-3909-810b-9c74257efb17 | -20.06387 | -43.71108 | 2025-08-05 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d9d9946c-2d33-3660-9a77-595b50c15261 | -17.22137 | -44.83065 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 12f1120c-7fa9-375a-9e34-7455ff66fae7 | -17.22204 | -44.82692 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8126e432-6341-3534-b6a7-5b81ccc1561b | -17.20855 | -44.83201 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 6d06a9ac-ef92-367e-a247-f9d9834a7110 | -18.74607 | -43.92365 | 2025-08-05 03:51:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4c90f52-36de-360f-8334-b92f0771ffe3 | -18.77618 | -47.61987 | 2025-08-05 03:51:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebdda132-ef28-3d42-911e-e3bbde9d19c7 | -17.37635 | -44.99255 | 2025-08-05 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddf071f1-fd72-3ba5-b989-b9dc91501e07 | -17.21671 | -44.8332 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 39d47cc0-78e8-3320-80ee-3a0cbbdb0be7 | -17.21601 | -44.83693 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56e59a0d-dd7c-307e-9ead-06d5c0a6007f | -15.35707 | -41.85682 | 2025-08-05 03:51:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95f90c4c-e926-3bad-987c-22a38f3f916a | -17.21597 | -44.83734 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2da719ad-005f-37f8-888e-42d8b4fcc925 | -21.92358 | -46.08027 | 2025-08-05 03:53:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0f11100-02f3-39bc-91eb-29efb33186b2 | -21.93234 | -46.07823 | 2025-08-05 03:53:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| babc6494-5502-3e69-ae8f-7275e45b6c40 | -21.92832 | -46.07739 | 2025-08-05 03:53:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7de3ad9-ab99-3709-a3d6-d0a3cc92fb86 | -17.2256 | -44.817 | 2025-08-05 04:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 22fc469e-b67c-313f-b5a8-2f1347834834 | -17.2056 | -44.8214 | 2025-08-05 04:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 35609dd7-8205-301f-b2de-b04e24a37a9f | -13.0914 | -56.9114 | 2025-08-05 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 45db3502-744a-366c-b9ef-f42e0b7de76a | -13.0538 | -56.8746 | 2025-08-05 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bb8a8cc7-79bb-38df-9575-5729a2ceba98 | -8.9478 | -46.7354 | 2025-08-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 24cb6a20-60aa-3685-bf3b-10121654d82f | -13.0723 | -56.9131 | 2025-08-05 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d4ff5a80-2ca1-302e-a7a7-e4fb49db71a1 | -8.9227 | -60.5568 | 2025-08-05 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 77288b6a-e6b1-3ac0-af7b-4e273b092910 | -13.0723 | -56.9131 | 2025-08-05 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 34f105aa-84bb-3652-a620-b78a44c5175b | -13.0538 | -56.8746 | 2025-08-05 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fcdd3386-0625-3396-9d09-76cc21c94c8d | -8.9478 | -46.7354 | 2025-08-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| dcf3ff90-4daa-3035-9569-83f7ed6538cf | -13.0914 | -56.9114 | 2025-08-05 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 833574e0-3905-3974-8c91-c6fe37c62579 | -13.0726 | -56.893 | 2025-08-05 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a43645f8-2206-3ef9-a2d6-bb8e6dde2a76 | -4.02862 | -48.05845 | 2025-08-05 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee940b8-f4ba-3d68-8740-60bdd366f03a | -2.49411 | -47.56797 | 2025-08-05 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fdfd392-8e0e-3882-bde3-e6c3e5d9e97e | -4.3894 | -41.91594 | 2025-08-05 04:14:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d07f47c8-06de-342e-856c-625f9e1bd1fb | -3.01982 | -46.9086 | 2025-08-05 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b868c12-d55d-3415-8bd0-ab9d0f2f0e65 | -4.02736 | -48.066 | 2025-08-05 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af7150c-7bc8-3586-b436-709461b5ebb6 | -3.47627 | -43.2454 | 2025-08-05 04:14:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0195818d-55ea-3df6-a6c9-90ba492d70de | -4.06343 | -46.93553 | 2025-08-05 04:14:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 779c6fc8-db9d-30aa-bf49-627d0eefa10c | -5.48529 | -42.15781 | 2025-08-05 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9921c70-f4ec-34fc-b2e4-0b2396b2daac | -5.48474 | -42.1613 | 2025-08-05 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 540d44bf-bb5a-3653-a938-89db88314a7a | -2.90716 | -40.13331 | 2025-08-05 04:14:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f5a89cd3-869b-364a-a48e-730d71d2b1ec | -4.35595 | -46.55918 | 2025-08-05 04:14:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b5da3cb-81c0-302b-bb82-25342f91503f | -2.98439 | -54.50402 | 2025-08-05 04:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e82189-aaa4-3a40-9e92-305b032528ec | -4.028 | -48.06217 | 2025-08-05 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7addb020-c3a1-31b4-843b-03db36867530 | -4.0238 | -48.06151 | 2025-08-05 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9975f3cd-bc34-3079-bb62-77c571d7bb88 | -3.78278 | -41.68536 | 2025-08-05 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ae3792a-3f58-3818-94b4-eae77003f18a | -3.47571 | -43.24891 | 2025-08-05 04:14:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c196838-f881-340e-8216-551e41d39924 | -3.47906 | -43.24943 | 2025-08-05 04:14:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d66c7c91-d8d9-3c2a-ae9e-8b5a5cebdf7e | -5.48141 | -42.16079 | 2025-08-05 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 568b624b-e633-363c-b1a0-462e0aec75c6 | -3.2101 | -41.84165 | 2025-08-05 04:14:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6dda0b6-f894-3f42-9ddf-e6cb8e9a4ef7 | -3.42057 | -43.1649 | 2025-08-05 04:14:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0451aedf-d153-30c6-bd89-61e4abee8019 | -3.78611 | -41.68589 | 2025-08-05 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9fa8f45a-20d1-352c-b412-1ac4a15806c6 | -4.77522 | -45.33676 | 2025-08-05 04:14:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b0f26f7a-0f72-3fbe-8ee7-9ad04158e77e | -3.01902 | -46.91361 | 2025-08-05 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e038da96-8cb0-3e1b-af02-c4088b8c290c | -5.13923 | -36.36857 | 2025-08-05 04:14:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0eae6d22-8d23-36f3-905c-6571829d36a4 | -5.10751 | -42.92178 | 2025-08-05 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e86f31af-6904-35da-b4b1-eb6cf2791551 | -3.11223 | -47.50315 | 2025-08-05 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f612feb8-8342-39bc-abd4-38ae4c70a78b | -3.57207 | -49.50632 | 2025-08-05 04:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d92caf64-d70c-31b7-a6d8-550b429811ca | -5.13986 | -36.36425 | 2025-08-05 04:14:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8815dee6-91d4-3b08-b974-28118153b5e6 | -4.12929 | -38.18649 | 2025-08-05 04:14:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c62e06ea-3bac-3556-99ef-6814e912d874 | -4.91567 | -37.48703 | 2025-08-05 04:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a94132d-6d23-3b88-ae9f-92c6279bda04 | -3.21234 | -41.84909 | 2025-08-05 04:14:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 419db68d-af3b-3a97-bba0-2d02f030ff38 | -2.89482 | -40.02005 | 2025-08-05 04:14:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 78fecb89-076e-33f7-a37d-8e5079c33933 | -3.77944 | -41.68484 | 2025-08-05 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 65abb6c8-81e8-3a7f-8775-3b84b33181b8 | -2.4935 | -47.57169 | 2025-08-05 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df4f9ff6-18de-3c4a-af32-accf29ef3aec | -4.77586 | -45.33278 | 2025-08-05 04:14:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c1d86be-07e7-3cf3-9b01-915c8a315921 | -2.98525 | -54.49897 | 2025-08-05 04:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40d077cb-787f-302a-8235-d376c17c0a89 | -2.92951 | -40.19442 | 2025-08-05 04:14:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 590c36f1-ccaa-3393-bd05-2e91fed2c02d | -3.01832 | -46.91036 | 2025-08-05 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d96062a-044c-3de6-af90-7dae243cbfc5 | -3.56906 | -49.50732 | 2025-08-05 04:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17f79a2b-195f-321f-a1f1-e437e619ff05 | -7.39027 | -44.64758 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aee7b795-eda4-33d0-ae0a-8c12b9a6b5e2 | -11.9121 | -44.954 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dd37e78-bb42-3f61-b2de-9953d80058e6 | -8.9384 | -46.7409 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 840dc286-9043-3652-958c-e395b7750bcb | -8.00532 | -43.21719 | 2025-08-05 04:17:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| cd8093a6-e648-30bb-ba57-8eb01baa09ca | -11.7456 | -45.0038 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea08579-18a5-3188-98f0-166cbf58f82b | -7.368 | -43.75759 | 2025-08-05 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca823f82-e77c-3ee2-ab41-5853107f54eb | -8.23271 | -45.05464 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d35b430b-044d-3b98-9e1c-a26861918913 | -11.76798 | -44.97084 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b8752ec-3e20-3220-af33-c04b0e3ba609 | -8.38689 | -45.78899 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
