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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8404c6-ce29-37ac-8ee4-2afbce1b5419 | -6.42989 | -55.52528 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7943f7e9-1c21-3fb8-a80d-850ee313c9e5 | -9.66915 | -55.07455 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e735f1-51f8-3b1d-8dc7-55d2c01aa05a | -8.81192 | -50.08284 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f51de79c-c316-321d-9bb1-2610c6c7cd03 | -6.26493 | -53.34408 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 483743a9-6e33-3966-965b-6bded7dc1e7c | -8.60721 | -54.71352 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a73136c-72d7-3232-ab1c-2913bbec9e5d | -6.33941 | -55.88343 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba689469-d92f-37d5-a81a-c58092805e3a | -8.59126 | -54.77158 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c4563a8-5322-33d7-93ab-a0a99140326c | -5.87822 | -52.19014 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b1ca51-d5e1-35af-887c-8b548cb574ec | -7.38122 | -55.15034 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b593cb8-c38f-3cbc-9770-8704412cb1c0 | -6.12725 | -53.53502 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23251e7d-796a-3b8f-afd4-1f8a209f490c | -6.1601 | -57.7957 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4511444-fe5e-3958-952f-db9b7e961706 | -9.22721 | -51.54335 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5af2c76-1411-36c6-8bf6-8d18fcf70d5e | -6.27427 | -53.3536 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0292f80-9f74-383b-ba8b-6ef11b937ec7 | -9.42731 | -51.59615 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0d56de4-3ea0-3a32-9b59-af5f89e0f771 | -9.07539 | -53.04195 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 386b87f5-b6f0-39c8-9bcc-008d90b2d308 | -6.22021 | -53.47327 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efb7530d-9bc9-3ec6-8f0d-639885f80254 | -6.00014 | -57.8311 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff7c0ac-be69-3f6a-a00f-cd9f3159f7cc | -7.27387 | -49.85489 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cec79738-0fd4-334d-adc5-4e6e6d092243 | -9.96949 | -53.93726 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d0ace15a-9a1f-37e8-8881-d0b8acaf6e06 | -6.30575 | -53.57685 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca2bf187-c316-31e0-92ee-e55792399964 | -6.83757 | -55.61086 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a62837f9-b1bc-3c1e-91b3-fa5f8894c66c | -6.75988 | -55.69463 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c799f7b-3edd-3e89-abea-97410ab7db38 | -6.16352 | -57.79625 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d0d3118-4cd1-3370-83de-1c13a6fe7115 | -9.15952 | -49.97164 | 2026-08-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ba09ec3-8dc8-3ee5-adcd-60290c7212b6 | -6.16812 | -57.78943 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01a55c49-6c39-39cb-a945-705d37c21e66 | -7.50491 | -55.36145 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b56dd70d-f623-3092-80ed-daee7020af69 | -7.35936 | -55.16528 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3d4ec74-b657-3e4a-8117-1c71abab415c | -8.59297 | -54.76052 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7318f186-7b9b-3129-8ce0-751addf2fc74 | -10.07408 | -48.6641 | 2026-08-28 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c6ea2b8-0113-345d-bde8-40539003e168 | -6.25955 | -55.42002 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7216a4c8-8ace-3f7e-a579-a94391ff8033 | -6.83645 | -56.45568 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01d78686-59ab-394c-af32-afda7e83b692 | -4.61178 | -56.172 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b54e8c6-eb6f-3c24-adbe-08d4a376a6cf | -6.23809 | -55.40596 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8affe2e0-ce11-3b5d-a6e6-c4ffb8cc402b | -6.84003 | -59.9462 | 2026-08-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c21e80-0837-3d41-b3fd-ca783c6dc20d | -9.67537 | -55.07936 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de48c918-7b32-3378-a8cb-2edb94faf2df | -9.43685 | -51.58694 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 260e9950-f017-3832-9130-84386922a3a0 | -6.21653 | -53.59155 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2a372a-6057-36da-af9f-d73f964ed8be | -9.44397 | -51.71033 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7babdd80-7d43-342f-acd1-f055e8000c06 | -10.01471 | -46.41146 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34b171e7-f9cf-34e6-addf-1c970fdfce78 | -9.88211 | -49.71753 | 2026-08-28 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d327b32c-bde8-3361-aba7-cf91cb681086 | -6.51822 | -55.24298 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ea7ec02-84ae-3bbc-8a5f-a68fc76147be | -11.01754 | -45.06898 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c1abbf0-727a-3c6b-a52d-7b22f8b21376 | -8.77841 | -50.07086 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c25bcf48-f209-3a82-915d-0b75cbe18a11 | -8.07846 | -45.81165 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b868f87b-e0bc-3a0b-926c-1c7e486c6806 | -8.55781 | -54.71731 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f697eeb-a151-3e0b-a0a0-9eccd31deb2b | -6.27076 | -53.35307 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d5a4ea-5603-3d17-a571-1f0f75e5dc07 | -9.22025 | -51.5634 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c0a36ab-73ab-3585-8c6c-36b616427b75 | -8.59411 | -54.75314 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c26268d-fa58-3e93-9404-5e8f27043259 | -8.80749 | -50.08216 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b54537e3-12d9-3a1e-98df-6ce7477dfa4f | -5.50213 | -55.82854 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 49657419-884f-3798-bbd9-8565e2868a7a | -6.61945 | -43.73435 | 2026-08-28 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90e655fb-66f1-3e90-bec7-d487cf0a2256 | -8.59466 | -54.7721 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e46838b-290b-306d-87b2-a407774e4ee9 | -6.84089 | -55.61138 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3d01ece-de14-3225-b8bb-b42adb0d5dc0 | -4.84366 | -45.39566 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6da1cd80-da8e-3ced-97bb-1283432a7e72 | -9.21865 | -51.5456 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a544e08d-c67e-3215-bdfc-4e443ab3e3e2 | -6.57986 | -55.43522 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5954b6-e8f6-3e6c-b3a1-5c90c2660541 | -6.27497 | -53.32541 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fca28aae-b271-3447-9529-1d0c2ffc3941 | -8.58215 | -54.83046 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9589c2c-15fa-32ed-80da-070ac143e602 | -9.46356 | -51.71654 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04b063d6-c792-31aa-84bf-967dc70ad73c | -8.59694 | -54.75733 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2d6356-abef-3ed5-b33b-d551da0eba5b | -2.67081 | -54.76333 | 2026-08-28 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e2ccac6-99dc-3d6f-a22e-1de7858d6a3d | -6.27437 | -53.32936 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c1c817e-f92f-320f-9de3-35ceb026a6a8 | -7.92533 | -56.63729 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8096e67-30ce-390c-8a47-9408e6064a92 | -3.5352 | -48.18316 | 2026-08-28 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1169ea46-886b-3eb9-9a01-eb2ce2e3a5ee | -7.26638 | -49.84465 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b639d823-12cd-3cf0-8247-b5ee43b9b236 | -7.69806 | -55.36304 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bc79cd7-0e3f-3fda-bdda-98d265691f1f | -7.28281 | -49.94987 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d64820b-cad0-3949-afdb-850a944ca540 | -8.55497 | -54.71309 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07677f2a-843b-379a-9bfc-fec5dffd5e95 | -8.09541 | -45.81078 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe68e12f-514d-3d88-ab2e-080bc6b1a9ed | -6.32957 | -57.74641 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d235829c-b268-3ee8-a054-491646a3a2fe | -3.46271 | -59.51401 | 2026-08-28 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e37d1706-da04-333a-a742-7d8b0a74bd50 | -6.77753 | -55.69033 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fe5a1da-4664-3e9f-bd24-35c2d3ea0290 | -6.31859 | -54.7422 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f78b484d-ae76-395c-8207-e2076607692b | -6.62899 | -53.18399 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f10b65c-d172-30a6-bffc-86952180e507 | -3.35096 | -49.23744 | 2026-08-28 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cdd8607-16ba-39e5-8573-8a751e7d617f | -6.62483 | -53.18748 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f65b139f-71d7-3b6d-8114-61bff4ca363b | -9.46558 | -51.70253 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41d82bcf-7fb0-39b5-93fe-e8e54d709c44 | -6.84034 | -55.61486 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d575e6c-548f-3877-b53f-1f42b04601b3 | -8.60266 | -54.72039 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f49ed536-c8a9-31bf-9a9a-574a1257467e | -7.27003 | -49.85041 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83783e16-44fa-3bdb-895e-354ee9e564f1 | -8.8081 | -50.07779 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 750c68cb-5d9d-3b14-af59-5d741daeb57c | -6.77862 | -55.6834 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 178c7ef9-cd83-3734-b949-36ab3d7abdf3 | -6.17034 | -57.79737 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c6616a9-070d-3213-88ff-c32ad34f303b | -6.27442 | -53.13796 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 158d20d1-93f7-3e12-b9d8-59b0112933ba | -8.59918 | -54.78788 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f4c4baf-5e38-3ea6-a188-6fa2fcf1abc4 | -6.53043 | -55.25205 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6cef367-b0fe-3d44-a451-3e9e7bd50f76 | -6.50179 | -53.26034 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2acb45d-ba4f-3a50-a84b-d41fda1ebb2e | -10.00795 | -46.41818 | 2026-08-28 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 385e7c68-8632-36db-abbf-f0e0405ce52c | -9.46305 | -51.72005 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 628a6a0d-5b3a-3649-8e7f-5de444730a80 | -11.19627 | -51.24372 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f18e1309-fd84-3301-82c8-ace01e9ecf67 | -12.76781 | -44.26968 | 2026-08-28 05:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07765072-5d2e-3033-b0e2-95fdee10caa8 | -11.19536 | -51.24649 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66497a6e-3062-3e43-8104-d8221b3a7958 | -14.44155 | -54.05601 | 2026-08-28 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97423072-5b60-3f6e-9766-6ef469e8a583 | -13.61432 | -45.78142 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d18c1cb-7382-3a4d-83ac-e7f168ad8539 | -11.63881 | -46.74142 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b35c5ab3-0083-356c-9199-b02bf357d2a4 | -10.78699 | -54.00655 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eede9bf-641c-380b-ae89-c35072fdbe75 | -11.28207 | -54.02356 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 849d52ac-5616-32e3-b52b-9f10316baf0b | -11.21739 | -54.00242 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81c4c134-eb58-3bcd-bb43-07b314eb0e3d | -11.83104 | -47.21184 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17b8872f-af02-37a1-b8ef-9ce3ec04fb77 | -8.98637 | -65.43784 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
