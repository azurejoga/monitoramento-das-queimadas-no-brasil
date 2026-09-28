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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be2640cc-a027-30af-97f8-ffa8b223f1ed | -6.94266 | -41.60445 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f274429-9465-38fa-ba41-0dd6bf6fb986 | -3.9417 | -42.55394 | 2026-09-28 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 204ceb60-cff6-3050-8e51-f85289510e8b | -5.8963 | -42.43749 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 25383a7e-e3f8-3cb1-8b05-0fce331f0e8a | -5.63391 | -43.72221 | 2026-09-28 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 777bae5b-0c40-3ef1-af89-2fc43afc1c23 | -6.30601 | -43.61037 | 2026-09-28 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 152c481a-b399-32aa-92bf-676edefd7442 | -6.94554 | -41.61357 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 26eeaf90-a30d-30b9-9978-881ea603c735 | -7.15934 | -39.31229 | 2026-09-28 03:47:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cdaab98d-d6c3-313e-83c1-27058463c067 | -6.94696 | -41.60532 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7fff3b26-aab6-3ff8-a4a1-5387bb0e3f92 | -5.89018 | -42.43424 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 60a78754-d185-3ad9-9697-7e6aeef9122e | -6.94483 | -41.61771 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e005959e-5748-3a18-8428-a9aecdc9c3e8 | -3.81956 | -44.09118 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd4632f1-2e04-372d-9eea-2f637979db9c | -3.42073 | -48.34325 | 2026-09-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cb81bb7b-0e28-31d2-9041-d17b23655b1e | -5.63847 | -43.72623 | 2026-09-28 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2723a902-f9e7-3464-a744-08cbece61605 | -6.14054 | -44.13339 | 2026-09-28 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 62b8af0c-1a68-3b9c-9c37-e037697212b5 | -5.7298 | -43.2814 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d97602cf-734d-384c-a3a6-5df17861fc8b | -6.13996 | -44.13663 | 2026-09-28 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d1d19c2-dc17-398d-bbf3-92038ed9814a | -5.63901 | -43.7231 | 2026-09-28 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17c9fabf-49b7-3fb8-911c-89abc244a369 | -9.97253 | -45.34179 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c3c3e37-76d9-3fa7-ad3b-cbacdb9c25cc | -9.76999 | -48.21229 | 2026-09-28 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba244f5c-df43-3295-9acc-8e49e6c95be5 | -7.70661 | -44.93573 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9aff7930-67e7-3ab1-b3d7-b8effd29e08a | -10.10579 | -43.94744 | 2026-09-28 03:49:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 176e2508-cd90-35a7-9667-d7414045fbff | -10.261 | -44.61925 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90c92f5a-3f84-3dd7-a2a8-27ac08c9d621 | -11.12816 | -50.06585 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34034ac7-3c1d-34ae-b2aa-1873dde29757 | -7.37847 | -42.11412 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9cf30b43-8131-3d79-af1b-0412a8748cae | -11.19538 | -44.80954 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| c4f98446-2068-35ff-ad3e-9cd3a6c7e8ad | -12.68355 | -45.02576 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1772214f-6398-3ec0-8df1-9162dcf8ccc5 | -11.54498 | -50.5221 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccdfcb38-6c4e-31f6-9da9-44bc382f8fda | -9.98327 | -50.14581 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed48c3e9-bf33-3d4c-babe-0b9f2c11e6a3 | -7.37536 | -42.13191 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 380626ab-c2ed-344f-81ab-3385f0966336 | -8.89417 | -46.19732 | 2026-09-28 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e17e1529-4a0b-3686-bfb6-d976b756146f | -11.43684 | -44.92466 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abe2ee5d-16c9-3f0a-91b2-465c7b4044f4 | -7.37925 | -42.10969 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 96f49136-5353-385e-8790-9ebb5e51a83b | -9.14082 | -47.9863 | 2026-09-28 03:49:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5416f385-4ef5-3138-8c11-adaedc65fec0 | -11.69027 | -44.52822 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62936d4c-24b5-3eb0-91d4-e1980639ef8c | -10.25654 | -44.61385 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e536d135-5984-3af9-96ae-605ecdeaa11e | -11.19952 | -47.71499 | 2026-09-28 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e47d07cf-bb50-3d11-acf2-76aed23d64de | -11.59482 | -44.13369 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6660d840-5f26-3884-a786-321e86e15ac2 | -12.69612 | -47.32616 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db5cb67d-1c4e-3196-a471-490325d580ea | -7.33503 | -42.0826 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8adc6f28-581d-33c6-88ab-9c8f3b8f1692 | -7.70841 | -44.93965 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b59ddbe7-fb21-3523-bc96-45e3ab4ac4d0 | -9.62439 | -43.96299 | 2026-09-28 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23ed1285-477d-3fe1-a28d-f31fb8743813 | -13.4507 | -46.31505 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63064e45-2043-31de-adf6-1d6d393f10e3 | -7.88971 | -45.44881 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9fa05cb-44a1-3565-bcb7-c74a4f2829c5 | -10.8878 | -50.69024 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9581264-9b01-34a2-8b96-f9e43f6d56b5 | -9.97761 | -50.17345 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e85eccb1-b595-3373-987e-2d0e5c0e247d | -11.16962 | -45.13593 | 2026-09-28 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bd3511c-de4b-3519-9ad7-65f246b1b321 | -8.95702 | -44.16593 | 2026-09-28 03:49:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 66e8c70b-6d9f-3b66-ae2a-2598b27084cf | -11.19346 | -44.81905 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bccb4a31-9ed5-32a1-ad09-d3257c0b4e19 | -11.19539 | -44.80901 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 88efbdd6-6149-3966-a0ea-0a3cb9c55282 | -7.70945 | -39.35157 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 107e85f3-4b71-32df-ad44-5196bb68770a | -12.87691 | -44.79513 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 849e8971-e5e3-36e8-9a56-ff83f2a228a8 | -10.92195 | -50.70542 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b2fd58a6-e812-3bdc-a90f-abcfa5136c78 | -11.18256 | -44.79513 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| edc673c5-9643-3de3-a79e-5f384f405c9f | -8.3703 | -45.46206 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae973324-b427-3fee-927b-08aa5433e6b1 | -10.21122 | -50.00699 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0cc2fde9-5f25-35e2-9ecb-043995d31ee2 | -12.63692 | -47.31964 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 342cd1cb-1fbf-3d2b-b050-6c3cb911f824 | -11.18407 | -44.81491 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| f41de385-679a-3f6b-bce7-17654b77e902 | -13.10299 | -47.42518 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bde19ae5-c02c-3ff0-9226-33f4257ad391 | -9.17336 | -45.78526 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc67bacc-2162-352b-8c5c-9d25f49bb42a | -10.20426 | -50.0055 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 887e953a-0e01-37fa-bcdc-7c8f55f440e7 | -13.46593 | -48.59757 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| db7a4a76-d76c-3507-9b62-9af898547b97 | -8.22957 | -45.48452 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab51f861-015b-3d9e-8808-8adce103387e | -12.71 | -47.28661 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc7c4489-ec24-3b50-8b4f-89598743980d | -12.65622 | -47.31787 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fee8ed0c-9b30-3791-8d7c-c4db75bd3e10 | -7.07337 | -41.73497 | 2026-09-28 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43ef0d4d-3e49-38a5-9e31-4005616a66d2 | -8.36946 | -45.46313 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 592b2c04-cd81-3552-b9c0-48bf0d820d09 | -11.66982 | -43.52277 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fdf7246-8251-3b72-94f0-7cac75e97ea1 | -7.38002 | -42.10526 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6e953cb-1a59-37f0-9cf8-9d2fc83f95e0 | -9.16824 | -45.78331 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3767d15-42f3-38b8-911c-bd27a4092c71 | -11.37049 | -43.43027 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a60d7139-20d4-3c98-a038-6da4d4589951 | -8.24367 | -45.40697 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 334c5404-a9c1-3fdd-82dc-7670e6ea210a | -12.31348 | -46.40966 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7909cfe-d53f-3ae6-b42e-5f07641b5dfd | -10.25114 | -44.61657 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1b2e55f-6cb6-3da4-b26b-22b26d765129 | -11.21051 | -44.78319 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 983333a7-58e9-3f96-9060-4b01e6bcc69a | -7.26754 | -45.34404 | 2026-09-28 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dba4162b-1e0f-324b-86d1-860645b176f7 | -12.69044 | -47.32491 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b666e564-81b9-3317-96f6-609ac57e84ec | -13.45991 | -48.59599 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11b64be8-ae29-3aac-9e40-346342160975 | -9.82526 | -45.26361 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24e7baa3-7c4e-3323-b2a9-8920871cb832 | -11.44235 | -44.92286 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8c52ba-2333-3c7d-abb5-909a3c73898f | -12.67737 | -45.02497 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c719bd3f-962b-36b6-96fa-e8334bdedaa3 | -6.59355 | -47.16681 | 2026-09-28 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc903938-8960-3ca0-a5ec-dea4aff6dc24 | -11.1904 | -44.80855 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| ccb883ae-b2af-31c8-bd83-949f2dd11155 | -10.88348 | -43.68932 | 2026-09-28 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b8b63d6a-a888-313c-ae26-70fe28073375 | -10.70593 | -44.44075 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0002f77b-2ec3-3da2-ae4f-ed2b6b47f83b | -10.21399 | -49.99353 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 310a0823-8eab-3634-a40f-c911058d5ff7 | -8.65618 | -45.41918 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 563846c1-8a6c-31da-971f-064c94c47acf | -10.9352 | -50.67799 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54947a20-f36b-3c11-a524-6c377ade03be | -7.30456 | -44.59906 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0a9f10b-31f7-3e61-b028-6035a7430c0f | -10.94232 | -50.67959 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c7fa7b3-5fe4-3787-b31d-8e0a96ec2bdb | -10.37551 | -44.97617 | 2026-09-28 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d16f4f3d-fba0-30ad-9a06-64bee63607f9 | -11.37926 | -43.40805 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11eb3cf8-7cae-32b4-81d9-ac94f90e4f73 | -13.56668 | -46.35971 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6b1d4e2-e7e1-3384-8e34-9801c044b388 | -7.28466 | -44.31272 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdde63e8-67c1-35d5-88c3-329f2ee0e89d | -11.37954 | -43.43198 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8e1c9b7-d19d-319a-a304-6acb89b79279 | -11.18852 | -44.8188 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f06d912c-5def-3d7a-b092-f220d8fc6682 | -11.44954 | -44.93976 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29ff1cd0-e5d2-3e92-8103-87cb50e14e87 | -9.82398 | -45.27071 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd222e9e-69ae-33d6-aea9-ab34fe962437 | -9.6038 | -46.85487 | 2026-09-28 03:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db07ca22-dbce-386e-9acd-b69b9bca3494 | -8.24499 | -44.83331 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aba06eff-5281-3e3b-8d1c-5a911968b27d | -11.1295 | -50.05929 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README18.md)
