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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8f2b9a4-e669-3036-ba80-ae90146aa715 | -7.71847 | -47.30312 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db4418a3-3051-3d41-aa4a-aed9ac188b40 | -6.7017 | -42.74793 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d1b2f522-0913-3e7d-ad86-207d62dab55b | -11.4323 | -44.96487 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95b8ed12-84f8-398d-9a96-45692643e501 | -11.70967 | -44.42051 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc2a2b91-4e86-37af-9deb-87e1c31f6c44 | -11.34924 | -45.01038 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58b2ec86-7d18-3431-8c6f-0434cad7f4ee | -7.78269 | -46.94409 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1a8d497-f08a-35a3-aee8-0290971e668c | -11.71359 | -44.42121 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7da74aec-f6f8-3957-be3b-0334c60c9e8f | -10.00142 | -46.70809 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cf9dfd1-8020-31f3-b85d-1dc15d7733f9 | -9.6942 | -48.93884 | 2025-09-27 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4602c445-1bf1-3e27-b37f-8c30a44e6a9f | -13.24187 | -40.945 | 2025-09-27 03:55:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f558eb7d-5b8c-3d8d-a3ec-e3c3904e4e6c | -9.99662 | -44.18107 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba0e2fc4-6841-3d3f-9259-2f4ae992613f | -10.11861 | -45.32945 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c4b136c-7f7d-31f3-b0ad-8c9efcc07268 | -11.40866 | -42.30384 | 2025-09-27 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| abff2847-3826-3531-bb07-99d1a4fbbf42 | -7.05543 | -46.41632 | 2025-09-27 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8283f650-b94f-3132-8424-1bafd4089a67 | -7.65068 | -43.82705 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ac6456a-4462-3215-8bba-ba63b8452346 | -10.24084 | -43.95149 | 2025-09-27 03:55:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94f699a9-5653-3d33-a3a3-35fcd876649e | -7.04408 | -43.03475 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e27914e8-fd05-3d5f-8089-7a7708846134 | -10.24032 | -50.25409 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce5ddcfc-a7f1-3c8f-9a11-1b2a4eb341a2 | -7.71791 | -47.30618 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84207586-b6a0-3abb-9df4-f5d3aaba0dda | -7.27719 | -42.97654 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43d8c78e-db83-384c-9a65-ecf284715493 | -6.54984 | -43.83562 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74b3c617-ca34-3f47-8909-af2e3c893e16 | -10.15726 | -42.42616 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fc682a6b-d287-30ed-8e08-348d0d19150a | -11.61172 | -45.42597 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00d2cda1-dfb5-33a1-9775-a25c0bd7af0f | -11.70576 | -44.46742 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6b0fa9a-6c32-3db1-b003-504a06450bed | -11.98916 | -46.61023 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e356a345-22fd-3b3f-8d31-f5df4cc99560 | -7.34694 | -42.09098 | 2025-09-27 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6022be3f-3b23-3800-8750-e5c08c5150d9 | -11.02369 | -44.64508 | 2025-09-27 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d3d5c7a-d615-323c-b676-d8cf2955c4d2 | -9.96422 | -43.60709 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a19f9213-96e5-344f-8b62-5b0bb5a0ca5f | -10.00234 | -44.17138 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c4615d6-04f1-33cf-ad51-6e593c097c8d | -11.43854 | -44.97728 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47bd9043-3dd5-3aa9-b148-40dcf72f43d9 | -12.6476 | -48.15389 | 2025-09-27 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a29c58be-55a5-3cb9-aa3a-f994c0bc3937 | -8.64976 | -44.01036 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c65c0033-2a8a-3537-a250-5930154f2025 | -9.9972 | -44.17759 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf29ddca-d0db-38e4-9568-94d6851fe8ca | -12.30278 | -44.35177 | 2025-09-27 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 76d92265-338d-3ac8-b006-f60629b9c2c3 | -11.29725 | -47.82166 | 2025-09-27 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cb81005-a903-393f-b683-628e28a6b7dd | -10.94289 | -44.30503 | 2025-09-27 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4011ba7f-2b09-3ff3-866b-1afa780f0705 | -6.53824 | -43.82932 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 286cfb05-1e06-31d9-8196-bc52037bd0f1 | -7.62889 | -43.80874 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 32a12239-af1d-30d9-8fca-ad29804ae817 | -11.9434 | -47.87164 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c289891e-36a3-37e2-b5a7-2ccf6ee09498 | -7.78317 | -46.94128 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1c6b8a9-b93a-3bcd-ade8-6086d2bb4d6e | -11.35399 | -45.00735 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baad1ef1-4baf-32c3-85b1-875f952a8600 | -8.65038 | -44.00676 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af28f817-1584-36a5-bbc6-8335e9618db0 | -11.44147 | -44.93667 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf1903b6-af70-3403-b851-dcbbb90e7490 | -11.37103 | -45.00653 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25be2fd3-1e01-37c0-a51f-f2af34631f69 | -6.54642 | -43.83082 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b2395d4-0cbe-3420-9ed5-79377a35b8ef | -12.31055 | -44.35306 | 2025-09-27 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f52eb7cf-736e-3e52-9231-880b2c2c66d6 | -6.70709 | -42.73908 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b5a6e1e-c8df-3b03-8e83-86dd9701e81c | -7.18842 | -41.70831 | 2025-09-27 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7cb7370-579e-39aa-a035-401e1ffa8d27 | -11.67703 | -44.30492 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98c7f7c7-b308-3df7-b4c6-194cbe90550c | -10.00456 | -44.17298 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e11a167-f04b-308e-8c46-59cca7471642 | -7.92224 | -43.30849 | 2025-09-27 03:55:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4c2a7bc-b612-3393-a231-12373eea4b23 | -11.97085 | -46.59951 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 296be782-82fc-34cc-b598-e0712c9483c1 | -12.85878 | -47.62336 | 2025-09-27 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed113a4f-dc7d-3f74-9abc-95864a03c2e1 | -12.36168 | -44.1493 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 312a8c56-a0bc-3a55-924c-074015407e45 | -7.77043 | -43.91447 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30a861d4-ea87-3ab8-b05d-737e81c966b2 | -10.79873 | -45.37023 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccc10e61-cef2-3cca-9bdc-11550abcc412 | -10.65153 | -47.27039 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1702426-5394-38f0-a9a0-44e3009c852a | -11.71705 | -44.40078 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 229a3ba1-fc3c-3f89-80f6-a465c5e9ba8f | -12.03052 | -47.0779 | 2025-09-27 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fe6c629-1065-3c0b-a5b5-cf45123926d9 | -11.43569 | -44.96951 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48718848-fdcd-3168-b733-5757cb325532 | -8.90944 | -46.09651 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8b830bd-5396-3bac-b8bc-ccde4f14042a | -6.49739 | -43.6467 | 2025-09-27 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd160c2d-48d2-3d98-921d-6fb5dd6bf261 | -11.36154 | -45.01254 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4db460d5-a5b0-35ef-8697-667d2a6e01d9 | -8.67351 | -43.99216 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4808a3cb-c050-35da-8a22-d5157a1aa1c7 | -7.81079 | -46.9635 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19eddca9-3d36-3498-b679-ea0a74e91839 | -6.61444 | -42.92924 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5e6ef9d-3304-3bc1-961b-ff8385bf761f | -8.66089 | -43.99362 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c27126c4-8133-3e96-86be-6dfd01f1e23e | -6.93092 | -44.64685 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20c9143c-82d8-3ddd-ba5c-ee165e1cb806 | -11.68477 | -44.44779 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d29962c-d4f3-3f49-a7fe-9f85beaecc35 | -9.98358 | -43.58572 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79153268-e6e4-35fd-b47f-a98c91a3ba2a | -11.43386 | -44.97996 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88da32b2-2714-3932-aaf6-4b6f0c3e2ea1 | -6.99699 | -42.39446 | 2025-09-27 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a77f7154-11d2-3315-9aa8-7eda74beb0e4 | -10.23443 | -50.25296 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12eacd77-fcb1-33e6-8513-f66b18d5b073 | -12.98879 | -49.4347 | 2025-09-27 03:55:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b3c43f7-4529-3718-a9bb-16532dcdd7f8 | -6.81265 | -44.47151 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d14249c2-5b30-3284-9a61-1d556bde1642 | -8.8227 | -46.26573 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bf5790c-d397-300c-bdb1-390c1d0a87c1 | -11.78822 | -44.87104 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48ea159d-14e5-3dea-8ef7-48a5cdb67e02 | -11.69176 | -44.45432 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d686cc50-8386-31f1-aa75-72f917e94064 | -7.60197 | -43.05758 | 2025-09-27 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54954705-8222-30bc-98f6-fcf6052caf74 | -10.18386 | -46.9326 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 30546532-5457-38ad-b225-f63b4a2f087e | -11.97251 | -47.91574 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3967733b-67bf-3959-870a-eff4145d4cfa | -12.29122 | -45.64823 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69746cb7-7b0d-3b8a-a8e5-525fb9da7d95 | -11.41936 | -43.5117 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a87d03c1-bb11-3ea7-bd1f-83543016e080 | -8.83137 | -46.21669 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23b0827f-9c7a-3782-bdfd-4edba360dca2 | -11.99644 | -46.62129 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a05b0a67-fdf9-3eba-8ad2-30859b2797a9 | -7.61614 | -43.83532 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab816548-2af0-3cb1-8f91-e6ffda0f2d79 | -7.27334 | -42.97592 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cbfc8b6-c1e9-3aee-9a41-d4e2c8976b79 | -7.80684 | -46.95699 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87131203-95f3-3ce0-8e24-38103aac9c43 | -11.36693 | -45.00579 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93b63c58-e869-33f8-83f8-438b00791951 | -11.38291 | -45.03568 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1526a07f-7a91-36ee-b909-61b7fab50ac4 | -11.68565 | -44.44266 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5840e866-80db-3bdb-b198-8d09c85ac1c3 | -10.10095 | -45.30438 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71187d40-ff90-3f50-8d88-364eaf477010 | -7.26609 | -42.98227 | 2025-09-27 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97d706d2-7547-35d8-8b44-91b8eb283ef7 | -8.8368 | -46.21302 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6f9918d-2b91-3b30-ae0b-a284ed5190a9 | -12.95092 | -48.90936 | 2025-09-27 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dec42022-0eb7-3970-b828-d52f1a917ec3 | -10.17903 | -46.93524 | 2025-09-27 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cf77c2c5-e0e6-3828-9ffd-2a29de690a2a | -12.10303 | -44.31563 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ef82565-acd9-3ec9-9f78-be0d7a929b7c | -13.32514 | -43.03615 | 2025-09-27 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 774dfffc-8c15-3c0b-9389-3a7f5dfcc905 | -10.49234 | -48.03752 | 2025-09-27 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91c4b408-421c-3839-825d-b41caac0199b | -12.83868 | -44.70405 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
