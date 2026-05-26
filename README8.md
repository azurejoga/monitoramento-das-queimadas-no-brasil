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
| 7503f92b-0888-348c-afa4-829e3b009cab | -5.79023 | -45.12981 | 2026-05-26 04:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23e029d6-8ce9-3efb-8a56-206356989c77 | -10.88209 | -51.21323 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 770c76a9-aa6e-359b-980b-173f6ef0e76a | -8.878 | -51.84084 | 2026-05-26 04:29:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| adee0f3a-615c-3c99-b292-bac11c6cf320 | -9.30049 | -45.49525 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 477973ed-1829-3a2f-b05d-613424c462ea | -9.36163 | -45.46762 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72e24728-3f50-3694-8ebc-3b065d417f3b | -11.78904 | -46.47499 | 2026-05-26 04:29:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6d2ec62-a2ac-3488-8245-25a98e0d804c | -7.13956 | -44.06681 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15ddaa5e-aa4b-3fb1-92fa-c02c8f14e98b | -7.35487 | -46.2151 | 2026-05-26 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b080be7-b7d8-3761-aeb8-2bf0fccc2acb | -10.60322 | -44.32426 | 2026-05-26 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e9ecef87-7324-3c71-93dc-a842598689fc | -7.01371 | -44.99165 | 2026-05-26 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92081843-5726-3d41-8a06-0da844b4bf5f | -11.21445 | -53.82719 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05d67903-5952-39f4-88f6-031ae861fe93 | -9.21984 | -47.54173 | 2026-05-26 04:29:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bb4a128-d235-322d-9d2f-f7b93ce4c657 | -9.365 | -45.46814 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a6f95ee-c782-3f11-aa9e-b52c92377721 | -8.62351 | -45.02581 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b840955f-338e-3ee6-9232-9124fade637d | -7.14652 | -44.0678 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b0a1cb6-6547-3dc8-a20e-54e4e43738ca | -7.01203 | -45.00243 | 2026-05-26 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a740129-66b3-3907-9db7-6b59aba3daf2 | -8.71504 | -47.91392 | 2026-05-26 04:29:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ce59ae9-3fb7-3f7e-b3e1-bd8812fa259d | -12.14118 | -43.58341 | 2026-05-26 04:29:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ae2d2c5-47f2-39ff-8866-01e258353ef9 | -12.23255 | -48.09927 | 2026-05-26 04:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1691d369-b5b0-3dd5-9f8c-ee2946c41775 | -6.5198 | -55.06016 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed6810d7-964c-3e0e-8a37-03445f704201 | -11.61489 | -47.90395 | 2026-05-26 04:29:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5b4a9b8-4fae-32d1-bcd0-9c3700d57bd2 | -7.59753 | -46.46352 | 2026-05-26 04:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3faee77-661a-37ff-a510-9e29f2820d49 | -12.04144 | -47.3349 | 2026-05-26 04:29:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f83ecb51-c424-3e31-972a-c538f571ee56 | -8.97535 | -47.98216 | 2026-05-26 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcb11847-2c5e-3844-a61c-d7d15a03c984 | -11.81227 | -52.51552 | 2026-05-26 04:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315af343-5122-39d1-8a81-e0412c0eb1a8 | -7.13667 | -44.06245 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e05328b1-8d18-3f5c-a504-fde7ab3fe867 | -7.13726 | -44.05862 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc4ff463-fb9b-3eec-b2f0-dec50c518037 | -9.90889 | -44.35168 | 2026-05-26 04:29:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f493457f-9390-39c6-86b6-88fe8077a79e | -7.01034 | -44.99114 | 2026-05-26 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84ce9e8b-e765-30b4-bf27-ebe38fb7e310 | -8.62294 | -45.0295 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 655148d9-d985-364d-b5ea-8bee708b2dcd | -11.35416 | -52.9576 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 742d02e4-83a5-3eda-9b4e-8d1139c5f5a0 | -11.21439 | -53.82474 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f486511c-5b5e-3bb2-9f27-d3c7cacf8d11 | -6.51924 | -55.06333 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af59a965-83c3-37b4-8b19-b39efe6fd1d6 | -7.01315 | -44.99525 | 2026-05-26 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30de9bfb-e9ca-3474-b920-0013e45175be | -9.30159 | -48.58557 | 2026-05-26 04:29:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1028743-0d68-36c4-876b-e8ff611145c3 | -10.13959 | -52.13364 | 2026-05-26 04:29:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cc9cb2e-1698-3aaa-84fc-b91db5792634 | -8.72174 | -47.91501 | 2026-05-26 04:29:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b0a547e-7f36-3393-a4a3-081c60c9d089 | -7.1355 | -44.0701 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eda30edf-1a41-3db7-97c3-e4b69359f53f | -8.98205 | -47.98324 | 2026-05-26 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70551ef2-0ef4-3267-950c-8fe34c285928 | -11.36312 | -52.9553 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 3cacab1a-326c-31d0-b58b-451010c65915 | -9.44658 | -47.29138 | 2026-05-26 04:29:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a36bbfeb-f43f-38d3-b318-e4a7cad0dc39 | -11.17758 | -55.91299 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0a94f410-e679-327e-bfb6-85d855e31fca | -9.3577 | -45.47073 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2065a37a-a0fc-3999-8b74-ac2c4b042fdf | -7.14015 | -44.06298 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ed45cac-ccdf-3bcb-9438-ff30d98f8feb | -11.17611 | -46.83535 | 2026-05-26 04:29:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2ed4dbe-e3be-3479-aeb3-7d7f8300bf99 | -9.34984 | -45.47694 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8b1e65a-fe9d-3b56-9be2-99ea7d803243 | -11.35897 | -52.95454 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 9e2d32e7-0c4b-31db-85ba-a5289f91e60e | -9.02767 | -44.25353 | 2026-05-26 04:29:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c991a30-afbf-3365-9a10-9bddb8774cf9 | -11.17816 | -55.90998 | 2026-05-26 04:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7d857adf-3fe5-3029-88fb-d03e54d092da | -11.21885 | -53.82801 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3febd64b-59d5-3ed6-bdd9-95c884a87e4c | -9.36444 | -45.47177 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 109350e8-8d47-34d8-b66b-476f73021423 | -10.84727 | -53.75426 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c120aca-565d-3673-89de-1fa30d3bf7d7 | -9.29431 | -45.49059 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f00627b9-ada0-3c06-afa8-03b00adf5139 | -10.63238 | -48.33252 | 2026-05-26 04:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6fc616a-be8e-33c7-956b-c95034876628 | -10.60698 | -44.31911 | 2026-05-26 04:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9169e4e-8593-38de-b693-33ab9a73e061 | -8.70718 | -54.99792 | 2026-05-26 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e805e9d1-96e5-3f4d-aef7-6c2b05999928 | -11.36246 | -52.95912 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 622a937e-477a-342c-b9a2-3ad558d3ce61 | -12.23293 | -46.6071 | 2026-05-26 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e85b7ce1-6716-3e53-9eee-3deee1ca0995 | -9.49211 | -48.66145 | 2026-05-26 04:29:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35bb9771-262c-345c-84a3-c61d3164d455 | -12.04639 | -45.27655 | 2026-05-26 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddeea12d-738f-3578-9918-760c0aa5eeb3 | -11.21799 | -53.82991 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa831221-2897-3334-845e-26f67f98795b | -8.9787 | -47.9827 | 2026-05-26 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7400fb58-5023-390c-9922-8761a7c59378 | -9.37286 | -45.46189 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ce699f1-7d3c-317e-aaf7-f4b1d2b2bef1 | -7.01259 | -44.99884 | 2026-05-26 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d4e1f6d-07a6-3481-9d4e-93dc453c92a4 | -10.47646 | -48.90895 | 2026-05-26 04:29:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed852434-2ce3-34a3-8080-5e2e877cd3dd | -8.61615 | -45.02843 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a498626e-07c2-3c09-993f-b3955268de40 | -12.67317 | -43.09571 | 2026-05-26 04:29:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ffc06d2d-2ca5-3aa9-bf98-c58919cb843c | -9.53499 | -48.24536 | 2026-05-26 04:29:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52ea073a-212a-3e3b-92ae-78813910cefd | -8.44139 | -49.70912 | 2026-05-26 04:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2edebad-8595-3473-bcce-73b92ff9026e | -7.6433 | -45.30182 | 2026-05-26 04:29:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3b5fd4d-61b1-33cb-aa60-64ff6a10f14a | -8.71839 | -47.91446 | 2026-05-26 04:29:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27379b3c-ea2e-3c0b-a925-243edd1ac9d1 | -8.55642 | -45.98018 | 2026-05-26 04:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c23b10f-dd85-3fb0-bf56-0868c999cf7a | -9.29768 | -45.49112 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2187449e-3d8c-3676-9fff-e1035d8b8d8b | -9.30386 | -45.49577 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2c8a75b-0997-3981-9aea-2e299f76440e | -9.33492 | -40.21405 | 2026-05-26 04:29:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4e5bc98-482e-33b4-a6d2-7e3825619407 | -7.13897 | -44.07063 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe8a3c01-88ed-37f0-b32a-5decab5c7d2c | -12.04985 | -45.27708 | 2026-05-26 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660ff8d4-ddf2-3c47-97e2-584e9b142dd8 | -10.9187 | -54.11419 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43a2c849-edb3-3785-891e-37ac33db42d4 | -10.66094 | -49.72377 | 2026-05-26 04:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ad5105e-5dd0-3039-bf32-f11904df5e77 | -11.21521 | -53.82284 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 254b9b2f-aaac-303e-9c17-dcad58259086 | -8.97812 | -47.98628 | 2026-05-26 04:29:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c2e12c5-3e72-3fb4-ad68-9c32d625432b | -10.63295 | -48.32892 | 2026-05-26 04:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82f4f8b0-47c7-3317-b3af-40e7ac838a6a | -8.87479 | -46.93456 | 2026-05-26 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5890312b-2de4-3e71-b293-25198b258b1c | -9.3504 | -45.47331 | 2026-05-26 04:29:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 429dec1f-0bf2-3d77-bc41-d8bc9a123a8b | -9.34006 | -40.21018 | 2026-05-26 04:29:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ea8f53b-2536-333c-8efd-b9f61b4b907c | -11.27425 | -53.97321 | 2026-05-26 04:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d838d4d4-e675-3672-9675-6824223ac2ea | -10.87316 | -53.73677 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8c9f560-eb73-3af7-8e5b-c26f871b2e99 | -10.50525 | -48.92523 | 2026-05-26 04:29:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 577f21c8-736d-375f-a456-ec4ad9edf893 | -6.76168 | -46.5285 | 2026-05-26 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37884dcc-b532-3aa0-a355-f9d334f13550 | -11.36378 | -52.95151 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 318fe6b8-ed17-351f-8fad-be9f9e2db5f6 | -7.13608 | -44.06628 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0781ddd1-5d03-387d-bcf6-ecda1a3dc539 | -10.87755 | -51.21716 | 2026-05-26 04:29:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c859d5c0-2761-3d64-ba1d-c59e21527932 | -10.63572 | -48.33308 | 2026-05-26 04:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7362ad-5637-3d5a-97af-a71b07d7446b | -11.2188 | -53.82554 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0c989a4-450b-325d-abab-a8dfe369ed3c | -9.45665 | -47.82298 | 2026-05-26 04:29:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9744af6-ad24-3edf-b10d-fd8cc67e1965 | -10.91786 | -54.11887 | 2026-05-26 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afc4f47f-72fa-3946-a9c7-4d67029fa617 | -12.03813 | -47.33435 | 2026-05-26 04:29:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f15a7b87-885d-33d1-9da2-baf8fd6677bd | -8.61671 | -45.02475 | 2026-05-26 04:29:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9e4fd5e-d7da-3b04-a081-ae55e94351cd | -11.35964 | -52.95075 | 2026-05-26 04:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a9a80b3b-f0de-311d-9c67-05a95eed2ab3 | -12.04697 | -45.27269 | 2026-05-26 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
