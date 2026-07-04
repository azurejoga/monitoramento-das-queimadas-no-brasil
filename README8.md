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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f97085e9-8625-3676-8a19-730b822957c6 | -6.42129 | -43.7205 | 2026-07-04 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70de3209-7a15-3bb2-9248-fa9b83f34701 | -4.39549 | -43.30886 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 452723c9-5690-3d1f-ad27-21a08b99fdb0 | -5.31192 | -43.56767 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ecfab340-21b0-3e9d-aa62-6ea233cc1293 | -5.14768 | -37.9097 | 2026-07-04 03:57:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51b9e69b-3ee9-3b90-9846-8cf9f9bdf67f | -3.41524 | -41.70505 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5fbd37ff-bf63-340c-a352-6af52fe5033d | -5.32076 | -43.56535 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb689466-524d-3618-a90d-d37527647964 | -4.01482 | -48.06324 | 2026-07-04 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11617ab4-8fcb-37e1-8705-2ff96c47e3fe | -3.51155 | -48.03776 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f71d8a57-5dcf-3d70-8ba4-14c4e2023e99 | -4.33591 | -48.9575 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4297784-4e61-32ff-95e2-a1d6e54e3933 | -2.94331 | -39.92442 | 2026-07-04 03:57:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c197057-a768-3359-8d53-49950d94deb5 | -3.42276 | -41.7063 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb3fd05a-7e08-321a-8984-b938e38ddcf1 | -3.41449 | -41.70961 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 50def795-4ae0-309e-99fc-9e22f1790c8e | -3.5129 | -48.0379 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 526d8c8b-5a37-39f2-8fad-98e1d4d96c86 | -5.31666 | -43.56462 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8200bebf-0a8a-38e3-b3db-ef17ffd92ead | -5.43364 | -44.65097 | 2026-07-04 03:57:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0da29458-e9d4-361e-a9d9-6c3771802042 | -5.80079 | -43.63691 | 2026-07-04 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0639466f-2579-3d3e-abb7-f25bbf421c85 | -4.39199 | -43.30453 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00d6abe3-1ea3-3c8c-b6cb-7d66d50b7fe2 | -3.41751 | -41.7148 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5cf7b7f9-496e-3be9-8a4a-a3d48906a157 | -4.39609 | -43.30518 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d98d2274-7399-35de-8cf7-9e865a741548 | -2.76778 | -48.56944 | 2026-07-04 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03ccb0f7-ed44-3481-be18-6a738e376c4f | -5.42232 | -45.29731 | 2026-07-04 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a360dbc-4d55-34ef-8970-fa36eb532a86 | -5.79669 | -43.63622 | 2026-07-04 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea984c01-6ef0-34bb-ad39-de71e951fc1a | -3.5064 | -48.04129 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3938e8cd-58ec-3586-8360-8be6498389c6 | -4.28754 | -48.35173 | 2026-07-04 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c8a95409-3b73-3f6b-87de-f29436dd8fd7 | -6.03417 | -42.99402 | 2026-07-04 03:57:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32b572d1-3959-395a-972c-080539acc82a | -3.42503 | -41.71605 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7224bfb3-bb1b-3687-adec-87c593511ef6 | -5.79196 | -43.63923 | 2026-07-04 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f2e674-1733-320e-9c11-6ac15bcc4ffe | -4.34786 | -47.76631 | 2026-07-04 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 37cc380f-07f5-3e41-bac2-b3d5947dadba | -3.51082 | -48.04217 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26af9aae-c604-38ac-a405-74abbddebc34 | -3.87094 | -42.97067 | 2026-07-04 03:57:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4058f66f-4665-34ca-823b-d4f07b556108 | -3.51213 | -48.04228 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17fefedd-daa6-3ab4-b7cc-edda1e695bf5 | -6.43011 | -43.71806 | 2026-07-04 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3923c24e-9de6-341b-bec6-918273853751 | -3.419 | -41.70567 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bebe6165-dad5-343f-819c-64dd956a3b45 | -5.41772 | -45.29644 | 2026-07-04 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 018631d0-e5ab-3fc1-9098-8fe152ce9abb | -6.42539 | -43.72111 | 2026-07-04 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2c2b4d3-3047-3bf7-b232-5ef747c81a8b | -4.1397 | -48.83871 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea08633a-b4ac-3151-b067-98a9660a736d | -3.42202 | -41.71085 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c01645a7-ed2a-3f95-8924-e84e098dcc7e | -3.51222 | -48.03378 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c5eaff8-f5d0-30c7-b119-8c4c2e6383f4 | -3.41826 | -41.71023 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 676c4b24-e817-3066-ab50-d59f3aaf022b | -4.2862 | -48.3595 | 2026-07-04 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 68818e61-b47d-3faf-9991-e7eb9f85c1ba | -3.42127 | -41.71543 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ceba2e22-3e0f-30e9-b31a-57bcae96ad26 | -6.42601 | -43.71747 | 2026-07-04 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba26d3b-c352-33c3-bb6a-b2879ec8f536 | -4.00906 | -48.06266 | 2026-07-04 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d43fd085-dc8b-319d-9546-1f72904dd6cf | -6.85868 | -38.35107 | 2026-07-04 03:57:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e92c4a6c-9e00-3109-8f02-2aab403d0670 | -4.34267 | -48.95422 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9c34b30-592c-3305-ae8c-9c37f435e78f | -6.85923 | -38.34761 | 2026-07-04 03:57:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abe7bc62-4f63-39d7-a44d-c93ed6d6a318 | -3.8744 | -42.97489 | 2026-07-04 03:57:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a150bb9-91f0-3121-9f88-b9afcee3f771 | -5.47077 | -45.42313 | 2026-07-04 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 732d573e-4e35-33f4-aa4a-2c60ffe4ab46 | -4.66413 | -43.22131 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8f966de-cfca-3bf1-bb29-b94748ad2fda | -2.76703 | -48.57395 | 2026-07-04 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce7b647a-2d37-3297-b681-8433f91e9755 | -4.66473 | -43.21775 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c178746-5953-354a-8d9c-ed28f6b061d4 | -5.80017 | -43.64059 | 2026-07-04 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b79562-0a45-387b-bf92-3973b17b7e55 | -5.46748 | -45.42498 | 2026-07-04 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 041aa0a8-0ec1-3f57-a79f-d398aa025e89 | -4.34294 | -47.76173 | 2026-07-04 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5ad04b9a-87e9-3ac8-87a6-7af5ed3337a6 | -5.59784 | -39.5426 | 2026-07-04 03:57:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 41bfec92-3455-3cf0-a04e-bab849f107e5 | -5.31255 | -43.56388 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30641740-95e5-3fa9-9664-41cc9ef5a3ce | -4.34022 | -48.9563 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57d21177-47b4-3f45-948b-d2a15923d76c | -4.14044 | -48.83436 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48adac3c-380d-3547-8b59-594d2cbce3c2 | -12.7553 | -44.5194 | 2026-07-04 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 46c33d89-30b0-33f3-a473-ac8e6a22cd3f | -13.2592 | -54.3489 | 2026-07-04 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 520d2570-2a9e-3a70-ab74-fe534a0f1f7e | -13.2401 | -54.351 | 2026-07-04 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 133cec58-6697-352c-8c44-0905dcae9da3 | -10.9401 | -43.0355 | 2026-07-04 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 671c42cc-bccf-388b-be94-ed917e5760a5 | -12.7548 | -44.5428 | 2026-07-04 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ce5f040d-a831-3b3d-9592-f7699b54a925 | -13.2404 | -54.3303 | 2026-07-04 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| bc234da1-b7d7-3da5-8ca9-b6162ad7d588 | -10.9205 | -43.0622 | 2026-07-04 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| a694e856-01ba-3b5c-a067-d8c6f0a202cf | -10.9397 | -43.0593 | 2026-07-04 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 9b656bc2-599c-3267-95e2-6148ea665a08 | -10.9209 | -43.0384 | 2026-07-04 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 928d9af2-ddb7-3928-9288-f4485e28df2c | -13.2595 | -54.3283 | 2026-07-04 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 277238a4-eb51-33c3-9347-c21f535171d5 | -11.45573 | -46.5843 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8809de8e-a916-311e-a888-214e5cc2b01d | -9.31188 | -47.63314 | 2026-07-04 04:00:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00d01dd3-9804-3057-9c4e-5b2017ca9d98 | -8.4417 | -51.56772 | 2026-07-04 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61c657b3-acfb-31d0-8b43-d0c3e29d2de9 | -9.5687 | -49.11194 | 2026-07-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ca89cfc-2f5b-311e-a6f8-e6b79dd8a93c | -12.75062 | -44.54437 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 8f476b7a-2607-3627-abdc-eb767ebd80d7 | -12.74761 | -44.53862 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 140cb66e-7171-32c8-a8d3-9e7877b2d331 | -7.00528 | -42.77826 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a546030c-f2eb-37d7-b6e9-256cb7cc66c5 | -11.45573 | -46.55908 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07338ac1-2873-3666-8667-c79d63b09bd6 | -9.56822 | -49.10836 | 2026-07-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bab67ee5-3064-3c44-bbc0-55de49b54c0b | -12.76618 | -44.54728 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd85feb6-9d41-3ea8-81c8-801649967a25 | -9.44547 | -40.32912 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7ccc313-8eb1-3d49-ae1e-e1014c7953ec | -12.74106 | -44.55307 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5176495c-b44c-3214-9294-55d58fa947d1 | -8.95731 | -40.72211 | 2026-07-04 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 79ae830b-a3c7-3521-8499-82d63d02a8cb | -12.74336 | -44.51712 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c48cee76-63d3-3bf7-afff-cc7108f51a64 | -12.74283 | -44.54295 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 30188380-0fe9-379c-8bcb-7942c4d13045 | -8.7615 | -47.40522 | 2026-07-04 04:00:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad437e63-341e-3584-bb46-a3087b7089e6 | -9.43716 | -40.31676 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 84b1e4e1-67ff-3348-af80-0c8ce1b0ef9a | -10.983 | -43.71016 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e73135b-b6db-3332-a50f-11dcd09ad68a | -10.93028 | -43.04411 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6acd896f-378c-32a3-bf96-57925909dde3 | -9.44489 | -40.3327 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c5183da-21c4-30e1-ab71-16665fbfb21b | -12.74974 | -44.54941 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0eb8baa-3924-3286-8666-435da02c3444 | -6.93132 | -43.71817 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d4632f3-81cb-3a3c-ab3f-f16a0a6e7c0f | -10.92219 | -43.0472 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a5867a44-f91a-3478-b7d3-2633e0e62c3a | -11.4521 | -46.5534 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc816e7c-37c8-33f1-96c6-4936a1c6ac25 | -12.76229 | -44.54654 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1d2df03a-b9a4-36ee-94a0-afbb8f00a9a7 | -12.9708 | -42.58481 | 2026-07-04 04:00:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8d9d010-0739-3d3d-bbb5-2a82aaa4f056 | -12.76015 | -44.5358 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f6340c8e-d884-334a-acb3-3f6ade6c0b0d | -7.0113 | -42.78901 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75ae4839-769a-3c7f-b2e0-dfe34528dda4 | -7.59787 | -45.70906 | 2026-07-04 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b856228f-986c-3d76-8558-0a0a2d7a3af9 | -6.93477 | -43.72247 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 778ca4fd-4c3f-3d95-ad0a-15dfe5fa4a01 | -12.74195 | -44.548 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c1859df-1054-3500-a538-143be5804bab | -9.5694 | -49.10818 | 2026-07-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README9.md)
