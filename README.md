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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49abb218-95fc-3e5e-8172-8d7884102cf0 | -9.3616 | -45.4516 | 2026-05-28 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 3a2ff050-e7b4-34d7-898b-38037b4205b7 | -9.3613 | -45.4744 | 2026-05-28 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5bc54a1f-0eb1-3a8b-a967-52a4b249e46b | -11.591 | -47.4496 | 2026-05-28 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 37ad8d7c-aedb-383f-b60e-663e8193022c | -9.3423 | -45.4765 | 2026-05-28 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4cbc5212-ea23-3c4f-b529-71920deb7f2e | -11.6101 | -47.4471 | 2026-05-28 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 52705277-04bf-361b-9b72-615dd9045c26 | -9.3427 | -45.4537 | 2026-05-28 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b389ddcd-0c56-3cc3-8129-f9d3bd22ecdb | -11.4724 | -52.9193 | 2026-05-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| a71e4758-7466-3c40-8f03-403b043fa2bd | -21.43019 | -47.06113 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c49e7a8f-7150-3bb4-bfc4-8c18d80fd136 | -20.91679 | -46.79407 | 2026-05-28 00:07:00 | TERRA_M-M | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b9d51bea-5511-3a2d-b3e5-2b427144c398 | -21.22513 | -48.72402 | 2026-05-28 00:07:00 | TERRA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 24951bdf-45e3-37e0-a377-e574d33c8379 | -20.91553 | -46.78462 | 2026-05-28 00:07:00 | TERRA_M-M | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3ac95a7e-fa72-3ff6-bd82-dd9e98d6169d | -21.54852 | -47.05093 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 17.7 |
| fb2f11ac-5047-32c1-b7bb-5785169b90a6 | -21.53885 | -47.04837 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8956fdef-da44-3991-9db3-7d7c0b701a2d | -21.42249 | -47.0723 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 96d6e973-6408-3f4a-b2f9-a87b26bf6331 | -21.4212 | -47.0625 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e45d0223-06f3-3c34-835f-c604d3d4970d | -21.54061 | -48.89668 | 2026-05-28 00:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 16916c2e-04fc-3500-9564-64ed2dcd6c8f | -21.43148 | -47.07094 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4032370b-7dc1-3438-b01b-390528646644 | -21.54202 | -48.90848 | 2026-05-28 00:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3b3cda7c-5c4a-38b0-8c26-6c2fc139dabf | -21.53755 | -47.03854 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f0fa4b9-06a7-3fa2-af2d-989a5970bd1c | -21.42377 | -47.08205 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2f8bf38-2a8d-340b-8005-875e2b80a429 | -21.54726 | -47.04112 | 2026-05-28 00:07:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 09e79e22-b439-3c39-8c78-ddc5274e8754 | -21.99458 | -48.34272 | 2026-05-28 00:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e02edda1-196c-3fdf-8b6f-19c30aeee7a2 | -21.99593 | -48.3539 | 2026-05-28 00:07:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 40b7c7fe-8bba-3a99-aed5-d43c37e94321 | -17.92485 | -51.34765 | 2026-05-28 00:07:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 200f22f6-51b8-32c4-a392-188f532d4627 | -17.92309 | -51.33258 | 2026-05-28 00:07:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3b760e9b-1c7c-3621-8d00-f9c7a4b7489e | -10.13214 | -52.40214 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 46889fa5-7ef7-3f70-855b-37bd8768953e | -11.29564 | -54.02902 | 2026-05-28 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 16777a08-cae7-3014-8ae3-330fc407cb24 | -7.35018 | -46.21405 | 2026-05-28 00:09:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d0da5157-91a9-3df5-85b2-d7793d6d8e9c | -11.58692 | -47.46266 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d51dc8f6-1ea3-3ca7-aff1-fb78909e435c | -10.65137 | -49.72576 | 2026-05-28 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc3ee425-0d4b-376c-966f-282cc6ed3d8f | -8.72927 | -48.33449 | 2026-05-28 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e124620f-53e5-3384-81fd-76727100c5b2 | -11.62968 | -56.8616 | 2026-05-28 00:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| befa3791-99b9-3713-a30f-f9613fd1f5f2 | -12.69471 | -44.79446 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1e91eb1d-e9b6-3afe-94ac-44ab70f53347 | -8.72804 | -48.32561 | 2026-05-28 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| fbb15aca-a6fc-367b-80ad-a95ea84f4707 | -9.33994 | -45.46973 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.5 |
| e5465228-9afa-3e40-aabe-5593c50a1ffb | -9.14464 | -51.29271 | 2026-05-28 00:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6e094d2a-df9e-3171-9789-8bc9c745994a | -11.99613 | -47.15932 | 2026-05-28 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9e7af6ad-371a-35f3-86b6-1307108d82d1 | -11.58564 | -47.45356 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| feae93d8-16c8-358a-88fa-7417eb5ad41a | -8.6803 | -48.30533 | 2026-05-28 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| a7f5daef-76f6-3961-b5ee-729f7b8de823 | -13.64722 | -55.29732 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 3984f9c1-424c-3704-a3af-219d8caef565 | -11.82705 | -48.20758 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 062126cd-5f1a-3854-9d78-f188afb58996 | -12.69304 | -44.78334 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4b37fc33-bd6b-3e73-93b1-faa08eb1ceee | -8.68153 | -48.31421 | 2026-05-28 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b93030a9-3d5c-3e6d-aafe-ffc1db018e59 | -9.7362 | -49.22055 | 2026-05-28 00:09:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6467c3a6-98b7-3f83-badf-aa8f6c45899c | -13.21692 | -54.51477 | 2026-05-28 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 3ff12b5b-45db-3121-a54e-35c82cc0300c | -12.55728 | -48.35653 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 51b71a5e-e090-31ab-824c-ce30d5f7fee0 | -11.59322 | -47.44324 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cc016148-8bad-3a95-8814-86c1ebc61e06 | -11.30092 | -54.04079 | 2026-05-28 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8d29baf1-e2ab-3372-9b5e-3ee957e5df21 | -9.29031 | -48.58826 | 2026-05-28 00:09:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 911fb2e2-e804-3c51-b1fc-3de935362e61 | -9.3892 | -48.4411 | 2026-05-28 00:09:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 10c29249-ffc2-3844-961d-4570537b0abd | -13.22772 | -54.49196 | 2026-05-28 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 16240308-4384-3ddb-b35e-fa6001727ac3 | -12.32824 | -47.89717 | 2026-05-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f8a76007-e54b-3966-9adc-1bdfa43f9638 | -9.74385 | -49.21024 | 2026-05-28 00:09:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 106b6ea2-6bc7-302e-9598-946ae6c10414 | -13.65418 | -55.31552 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| dec2696d-d292-3152-8082-07ac0817cd5b | -9.35086 | -45.46218 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 08f722c6-77bb-3a9e-8bd1-2ce47736cd65 | -13.6515 | -55.29033 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4a4c26af-3f7d-31e1-b5c6-f6f792d73246 | -11.46736 | -52.92032 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4252b150-932d-318b-be82-e9a61ad866f3 | -9.36065 | -45.46062 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c98e92f2-6443-300f-826c-883a76f10d45 | -14.39565 | -43.52123 | 2026-05-28 00:09:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9abe4347-445a-3a65-9ce6-7141be115df6 | -9.34275 | -45.47486 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 743c9e63-f2e8-38f8-9ddc-21e7221762d2 | -9.44142 | -48.88654 | 2026-05-28 00:09:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 25e2dd8a-e647-3983-9618-0dc19a30a163 | -11.60206 | -47.44192 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 577662ca-29e1-37c8-9289-3e535a8aa3bb | -11.47864 | -52.9189 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 418c7b7f-96a9-330e-b30e-6dcab2714100 | -9.34155 | -45.4809 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1f2ef0da-6553-3236-8a98-2f3a9a766993 | -9.75354 | -48.06849 | 2026-05-28 00:09:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 244eefa6-a507-3cbc-83ca-35bbd126a99c | -8.72046 | -48.33575 | 2026-05-28 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a27bc93c-57c3-3360-ab30-6d072da57f94 | -11.64262 | -52.85556 | 2026-05-28 00:09:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 15a9a1f8-bf4c-3dbd-87e6-4ee35cc10fa0 | -9.34107 | -45.4637 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d62cfd8-a7c0-3346-8300-20b3a25081c3 | -9.73497 | -49.2115 | 2026-05-28 00:09:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e29c5ae9-0959-3cd1-82af-9096143b1e5e | -8.68911 | -48.30406 | 2026-05-28 00:09:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7455fc24-4656-3c76-9810-50ecec1e1d5f | -11.59576 | -47.46137 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 15f8c41d-e413-34d0-bfae-a93b06f95994 | -6.5346 | -44.68882 | 2026-05-28 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fb504038-b406-37ac-921b-0d8bc6ecc2cd | -12.45927 | -46.52629 | 2026-05-28 00:09:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78a03c79-6bf4-3cb6-a236-826057659b05 | -10.14274 | -52.40072 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c5f313f9-a76f-3c3a-ae1e-8357192be5c9 | -14.78333 | -45.62865 | 2026-05-28 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7c1c575-8549-3ee5-9946-a31c65bac74d | -16.35375 | -47.35186 | 2026-05-28 00:09:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7c74771d-203e-3050-8c90-7d91a99c46cb | -13.21453 | -54.49339 | 2026-05-28 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e133ddb9-4e8d-39bc-9bcb-a909a7d639f9 | -9.14324 | -51.28182 | 2026-05-28 00:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 77d1f5e5-8717-3e69-898a-012ff1734b43 | -11.29879 | -54.02218 | 2026-05-28 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0322069b-386b-3c66-951b-9e70bd6b2cec | -7.009 | -45.00603 | 2026-05-28 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 427146fb-956e-33ff-9967-b2e42cafe789 | -9.36231 | -45.47182 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 760ecdd7-471c-385d-89c7-508d2d641923 | -6.54544 | -44.68731 | 2026-05-28 00:09:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 847045df-1b79-3679-a802-32c4ea0bcd03 | -8.40131 | -50.24775 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 33f58aa7-4dad-3342-9d11-bb2e515821a0 | -13.23014 | -54.51343 | 2026-05-28 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 7d9eccb7-978e-3d34-8c66-de9bddfd0628 | -7.0071 | -44.99319 | 2026-05-28 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ee62416e-1f64-310d-8c67-d6d8c0510a82 | -11.59448 | -47.45225 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| af376013-a9d0-321f-aaf4-d8c2448f083e | -9.44264 | -48.89546 | 2026-05-28 00:09:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| db63f072-77a3-350c-8502-fab49616a96b | -9.33021 | -50.45249 | 2026-05-28 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a549d3eb-d157-3457-9c72-1f792e94d433 | -11.60332 | -47.45093 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6187130f-15d9-3772-98a5-cbfc039dcdff | -13.20443 | -54.501 | 2026-05-28 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e28c35a7-d09b-3214-8bf9-b7fc80243b33 | -9.35253 | -45.47335 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2707182e-6c64-31e0-a001-614f7076ceb5 | -10.65265 | -49.73526 | 2026-05-28 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8eb9dbe6-6842-364c-a5a4-7961a0e4c030 | -11.82828 | -48.21655 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 63fcd1ad-150a-3773-b82a-b93886d4828f | -9.40072 | -48.4427 | 2026-05-28 00:09:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2046ced2-af54-333e-9308-fc00168a007c | -9.05243 | -46.30575 | 2026-05-28 00:09:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 950193a5-5d4d-3bb9-b12e-d5e3d95ba0e6 | -10.04092 | -48.68623 | 2026-05-28 00:09:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 885b23ae-ed3a-3f62-84f2-627d8158914b | -11.97134 | -47.38145 | 2026-05-28 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0657e0c5-e162-375a-9e4d-d76fe41bfbaa | -10.95189 | -44.17844 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f4fb8a21-05c0-31df-960b-d1c2b4a1cd40 | -10.47836 | -48.91313 | 2026-05-28 00:09:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 261d666d-0a22-3047-acfb-934f21e08f12 | -13.32114 | -43.73412 | 2026-05-28 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README2.md)
