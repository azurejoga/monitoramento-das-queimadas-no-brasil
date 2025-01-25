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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30ff27fb-0064-3228-b3b3-221db3e9a91f | -20.6365 | -55.72994 | 2025-01-25 00:56:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 15a935c3-9797-33e0-a854-1180d2ac8a1c | -20.63992 | -55.69743 | 2025-01-25 00:56:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 7e90f99a-cfa4-30b1-bac3-fe8bbbb85763 | -20.64231 | -55.72281 | 2025-01-25 00:56:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 39.3 |
| bcebc958-4139-39d4-8119-a081a2ddaee9 | -20.62605 | -55.69822 | 2025-01-25 00:56:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 20d0b3f8-2e90-31c1-9806-32af19098af2 | -21.98546 | -42.14283 | 2025-01-25 00:56:00 | TERRA_M-M | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 44ff3c99-0f81-3faa-84c0-124bb1072c82 | -21.98231 | -42.12479 | 2025-01-25 00:56:00 | TERRA_M-M | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 57fd9ed3-fbb2-396a-833f-fdbba86676d5 | -20.62846 | -55.72403 | 2025-01-25 00:56:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ba542e29-6ae2-33d1-8c6f-e1caed0d4dcf | -20.63396 | -55.7048 | 2025-01-25 00:56:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c8850f5d-80c5-319f-9184-d809617d9a82 | -21.27123 | -50.65249 | 2025-01-25 00:56:00 | TERRA_M-M | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 769cccc3-8a9f-3b68-9709-55a9b8792b4b | -13.21762 | -50.46939 | 2025-01-25 00:58:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1fed7337-e896-3280-9c7c-5bc7df29de07 | -10.50488 | -42.42819 | 2025-01-25 00:58:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 29.9 |
| f5c3029e-eaf6-36bf-a3f9-f85a615da5b2 | -11.04984 | -45.38205 | 2025-01-25 00:58:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7328b865-e846-31ef-9aae-047575fa224b | -11.06094 | -45.3801 | 2025-01-25 00:58:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d36758b3-5e33-3ca6-aed4-69665ca408e9 | -15.253 | -60.2095 | 2025-01-25 01:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5f0f283c-2797-3e02-87cb-420074042d97 | -20.6334 | -55.713 | 2025-01-25 01:00:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 61.7 |
| de6e80a0-cfbf-3efd-9ce1-f142f52e27d5 | -15.2528 | -60.2293 | 2025-01-25 01:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 617a4844-1a3b-337e-87dd-f825f16cb653 | -20.6334 | -55.713 | 2025-01-25 01:10:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 89eb125b-5acb-32ff-98c2-5033c1fc4467 | -15.2723 | -60.2078 | 2025-01-25 01:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 1d93cca6-ab8c-3427-b5a9-67ee35984eef | -15.253 | -60.2095 | 2025-01-25 01:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 376f1f65-c03a-38b7-9c35-15d4b8a945c6 | -15.253 | -60.2095 | 2025-01-25 01:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 656192e3-98a7-3f68-a259-f0f602f4c963 | -17.8586 | -40.1002 | 2025-01-25 01:20:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 0153c5e4-55e0-375a-94b2-6f9bbb07632d | -15.2528 | -60.2293 | 2025-01-25 01:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| bb42b08a-9898-3a35-b19d-a83bcd1616c5 | -20.6334 | -55.713 | 2025-01-25 01:20:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 17babc14-01d0-37fe-9433-e9bfb6599b65 | -20.6334 | -55.713 | 2025-01-25 01:30:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 7f69b834-604e-3d37-8671-f6ed21c10810 | -20.638901 | -55.722301 | 2025-01-25 01:39:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7ffff90e-cb66-36fb-9539-8a7651069f64 | -20.636499 | -55.712601 | 2025-01-25 01:39:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1b83ac-766b-346c-8a36-c60fe63a0d2d | -21.083401 | -56.395199 | 2025-01-25 01:39:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 194f439e-8409-337b-85a3-ccb9c9fce6fa | -15.2598 | -60.213699 | 2025-01-25 01:39:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc3dc932-3ee8-3cf0-9bd5-39225215198f | -16.0723 | -59.528801 | 2025-01-25 01:39:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e99f864-8045-3979-be34-26cc94283923 | -9.267 | -60.323399 | 2025-01-25 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 705d7c53-cd1d-32e9-b987-61302227ad23 | -20.6341 | -55.702801 | 2025-01-25 01:39:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5d44a459-e3fe-3c65-8dbd-9a48bb214f75 | -20.6462 | -55.7099 | 2025-01-25 01:39:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 29acb4b3-ae48-3ce7-9413-ca3609c7f274 | -9.2634 | -60.307999 | 2025-01-25 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e283c3c-08f0-31f5-adbd-e0585d74cd8b | -9.2652 | -60.315701 | 2025-01-25 01:39:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 126465a3-c226-3162-af06-a1d24fcb75ad | -16.070601 | -59.5214 | 2025-01-25 01:39:00 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9085734b-5b12-3b80-bafc-a69250bfa247 | -20.6334 | -55.713 | 2025-01-25 01:40:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9c32f1ac-b6fa-30be-9d86-90f38b0e1039 | -20.6334 | -55.713 | 2025-01-25 01:50:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e3bb242b-807f-3d58-ab98-d1ded66cc8d2 | -20.6334 | -55.713 | 2025-01-25 02:10:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 1016ee91-ee1b-35fc-9647-81461f2f10d3 | -20.6334 | -55.713 | 2025-01-25 02:20:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 5453f963-ec74-32be-9816-eba9fc32d3cd | -15.253 | -60.2095 | 2025-01-25 02:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| ac9b2d0f-0a29-3dc8-b2cc-2512112efbf6 | -20.6334 | -55.713 | 2025-01-25 02:30:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 013959a5-a7f6-3ccd-ac71-6847f4da9d9b | -9.259 | -60.309 | 2025-01-25 02:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7b4be306-8575-31c8-9783-52d43c184aca | -15.2528 | -60.2293 | 2025-01-25 02:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| bcaead63-146d-3fcd-a43b-2238613ead0c | -15.253 | -60.2095 | 2025-01-25 02:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d2e34da1-1f53-3c4b-aae1-4448f11f7883 | -20.6334 | -55.713 | 2025-01-25 02:50:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5daa3cc2-f2e4-3629-9202-56426f6d8812 | -15.2528 | -60.2293 | 2025-01-25 02:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f180185f-3a07-3abf-83d4-260cbd7f4a2d | -15.253 | -60.2095 | 2025-01-25 02:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e284704e-b9de-37e5-8b23-1e23e2dba8f0 | -7.94134 | -35.23164 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5d6d1fde-1359-3efc-876c-a2a71c591c40 | -7.93468 | -35.23471 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 762f8484-9750-344e-8d7f-3e8bb8fe9a88 | -7.95994 | -35.20691 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9841873c-b4b6-3b3b-b3a6-e2943f361d9e | -8.46546 | -37.81543 | 2025-01-25 02:55:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0aa6c0e5-029e-3b36-b2ec-ecbc62f3c393 | -7.93784 | -35.2284 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 1af4cac1-ab0d-3e88-8360-3ba2e7f94f3e | -7.9355 | -35.23035 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| bae2ba2e-efe6-32b2-b9ba-ca7b9d545b44 | -8.46422 | -37.82178 | 2025-01-25 02:55:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 04fefb90-2502-38b7-8fa4-6a76079aa63f | -7.93705 | -35.23277 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| bca7185b-47d6-3579-b421-9d669578be85 | -7.94053 | -35.23595 | 2025-01-25 02:55:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1817a695-397a-33b5-839a-8b4b97cb27c7 | -10.62257 | -37.04335 | 2025-01-25 02:57:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 409e00ca-6cea-3f9c-8c4b-1e88e6a7e0a9 | -10.61994 | -37.04144 | 2025-01-25 02:57:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 122a0c59-dd7c-3a42-8edb-027a0c5aeab4 | -10.17324 | -36.50031 | 2025-01-25 02:57:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31e0d761-7281-3fc3-82a2-43addbd229d3 | -10.619 | -37.04629 | 2025-01-25 02:57:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b1275228-d836-3115-8ef8-a5693b2b33f6 | -10.17422 | -36.497 | 2025-01-25 02:57:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5185888-9e6d-3bc1-9798-14bef07d2793 | -15.2528 | -60.2293 | 2025-01-25 03:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| fd25aff4-7bfb-3c90-a29a-a9c0d4e16357 | -20.6334 | -55.713 | 2025-01-25 03:00:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ea87b823-8f97-35eb-8fc9-a624664108a3 | -15.253 | -60.2095 | 2025-01-25 03:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c1f116e9-6014-3897-9738-830057e82181 | -17.81955 | -40.16697 | 2025-01-25 03:00:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e18d5346-0696-35df-aa3c-483e0ad225d6 | -17.81774 | -40.15785 | 2025-01-25 03:00:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| a9df57bc-08c3-358c-bbb6-4fe5ec1a26c9 | -17.82091 | -40.16114 | 2025-01-25 03:00:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e71b8111-2c84-3085-89ae-a90b84ce411f | -17.82237 | -40.15488 | 2025-01-25 03:00:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 4231a514-a707-37fe-bd1a-b05954520d87 | -17.81636 | -40.16391 | 2025-01-25 03:00:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| a6e3d10a-6ec1-354b-bf20-147f43d3399e | -21.98253 | -42.13235 | 2025-01-25 03:02:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6d459b32-6d0d-327d-ba96-63c89c5cca9e | -21.98807 | -42.13907 | 2025-01-25 03:02:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a346b02-626d-3206-a633-e9c2f59aaef7 | -21.98239 | -42.13491 | 2025-01-25 03:02:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 25a81e28-4c72-331d-9b27-912c64d36a31 | -21.98122 | -42.13759 | 2025-01-25 03:02:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 45b0ba46-5e0e-3d2b-b4f6-88b42257e5b1 | -21.9759 | -42.132 | 2025-01-25 03:02:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d480d077-0c9d-31e9-ac80-1fbf42be784d | -15.253 | -60.2095 | 2025-01-25 03:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 180f604a-fbfd-336e-afdc-2c112ab73b29 | -15.2528 | -60.2293 | 2025-01-25 03:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| fcac594a-38a1-31fa-bf95-5e80c4b8605b | -15.253 | -60.2095 | 2025-01-25 03:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2addf924-3874-386a-b467-f9ace6222c3a | -15.2528 | -60.2293 | 2025-01-25 03:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| adc70021-82d3-36fd-8676-3c8820c29597 | -15.253 | -60.2095 | 2025-01-25 03:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 893a73ee-53e2-3816-a388-a847f23edb2e | -6.07307 | -35.40545 | 2025-01-25 03:46:00 | NOAA-21 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f871da9-48ee-39e9-b1aa-e6446486627f | -8.90931 | -36.39816 | 2025-01-25 03:46:00 | NOAA-21 | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e550f2f7-3e57-3a63-aa88-598805513c55 | -6.69252 | -36.15137 | 2025-01-25 03:46:00 | NOAA-21 | SOSSÊGO | PARAÍBA | Brasil | 2516151 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93f731af-4f68-3762-a220-d9ebe2a4c42f | -8.307 | -39.54658 | 2025-01-25 03:46:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 93c15b36-8b3b-3e04-a330-52cc60090176 | -8.47046 | -37.81751 | 2025-01-25 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4d3f9b26-5b31-32e7-b04b-e1d3ce1ce290 | -8.47101 | -37.81403 | 2025-01-25 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5ba13da6-5f04-36a5-8eef-b2f2d5441481 | -8.4635 | -37.81585 | 2025-01-25 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c64b849a-a2fc-376f-bfdf-0c5574eb4a9f | -8.46714 | -37.81699 | 2025-01-25 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| acd59659-a84c-3b8d-aa0a-950ccadb9245 | -6.97962 | -42.79224 | 2025-01-25 03:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6945efdc-46cf-345c-adc6-412647e72f9b | -8.4677 | -37.8135 | 2025-01-25 03:46:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 59299644-a471-304a-ba6f-d2f5fe0ca51f | -8.31048 | -39.54713 | 2025-01-25 03:46:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1bdcdf8-0588-36d0-ab43-4487376fe21f | -9.08953 | -37.66679 | 2025-01-25 03:49:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9440ebcf-d028-3e99-a7b4-fec9df179652 | -11.68941 | -38.2743 | 2025-01-25 03:49:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd94bda6-e1f0-39fe-913f-780288fe4393 | -12.21145 | -37.96005 | 2025-01-25 03:49:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b41e209b-9e2e-3644-ba43-28d15305801a | -4.44203 | -38.06218 | 2025-01-25 03:49:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| db121c13-49ba-359f-bc2a-ea09df91cbfd | -8.11743 | -43.13096 | 2025-01-25 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 0818455d-479e-3233-ac97-0f080e1c6e0c | -14.0639 | -43.71225 | 2025-01-25 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a6a0c59-f2b0-3f4f-b016-40fe259e358f | -5.04277 | -37.7739 | 2025-01-25 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2de10c2d-6152-3052-8b74-d9927ee1b8e8 | -9.34224 | -35.89854 | 2025-01-25 03:49:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 22f799b2-e871-32b6-b708-b1260a65b409 | -11.28155 | -38.5066 | 2025-01-25 03:49:00 | NOAA-21 | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a065728c-7ff3-39f4-9620-1c2584922482 | -9.88214 | -37.27801 | 2025-01-25 03:49:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
