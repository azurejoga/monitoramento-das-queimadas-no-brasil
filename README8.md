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
| 8c29e7ac-e07a-322a-b6b2-a503e8c32b27 | -7.46344 | -45.56038 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28069690-9cba-3ec8-a69c-abe7db3e2b4c | -8.39749 | -47.14215 | 2025-06-23 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f6289338-97af-3181-a213-cfab265ec82c | -8.71648 | -48.01213 | 2025-06-23 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f9f0e60-42d8-328f-a69c-881e60ab52a7 | -7.8733 | -47.8818 | 2025-06-23 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86e94a1b-05c5-383b-b164-3083f620bc81 | -10.06467 | -49.66156 | 2025-06-23 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1808cf11-1611-3eec-9f7f-63dd4448ec4d | -8.65523 | -49.56161 | 2025-06-23 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2a8d1a6-54a3-33bc-a5b1-6bd116c8f114 | -7.44236 | -45.55713 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62f43c69-a2d4-3745-9266-5bf2f8f41662 | -8.0667 | -43.12027 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f4764493-57a9-320b-80ae-f8d82afe61e1 | -8.06873 | -43.10557 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f30483be-416d-349b-85f9-97f831c42230 | -5.70155 | -44.246 | 2025-06-23 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e798c37b-598d-3798-8bea-5eddc754d4f2 | -7.95084 | -46.04416 | 2025-06-23 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dce6d1f9-f26b-3b77-9a67-637df8078eff | -8.3782 | -47.43966 | 2025-06-23 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf41a57-5651-32ce-84e3-5f9a28979094 | -8.0671 | -43.11733 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| be617ae5-26a3-3b12-a8e4-d7826b2844dd | -8.6518 | -49.5611 | 2025-06-23 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91390c2f-87b5-3813-b065-983e7c74931e | -8.06832 | -43.10851 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 53605b38-b794-3b18-a6c1-26fb7a237bf3 | -10.03771 | -48.6801 | 2025-06-23 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fc745a7-a974-33e7-9f1c-aaa8c228109d | -7.44345 | -45.54938 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b4d72ee-d097-3ff8-b8a5-dfc5e39eb130 | -7.4508 | -45.5584 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20271e54-4e25-3367-aef1-9d0ebf8d7cca | -7.44006 | -45.54126 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 521a1a0a-fb8c-3211-907b-5300050a5184 | -7.44712 | -45.55391 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc294963-52b0-3d91-af2f-199743d022eb | -7.44254 | -45.55362 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 186f9958-c29d-3897-9ffa-e83677fc7374 | -9.4189 | -48.41829 | 2025-06-23 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c26b86f5-f6ac-3c73-adcf-9edb10962ca7 | -7.44791 | -45.54652 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e56adef-dda0-3573-a9a5-9fab62a42fdc | -5.69893 | -44.24834 | 2025-06-23 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8241b52f-378e-389c-8e6e-332f95c357bd | -7.44676 | -45.55425 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb967fd4-b26a-317e-ba0d-7b0e0bfa3ef2 | -8.09826 | -43.15146 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be9bf622-6263-3064-ada9-0c2a6f457be3 | -7.44767 | -45.55004 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e04bc9c9-e11a-3133-9a6a-5b79b4fb37f6 | -8.10839 | -43.14792 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 01679f29-66e8-3f8c-a384-c3f25ea42c20 | -7.44658 | -45.55776 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59513ca2-5385-3b8e-bb2f-0880e4fb94d8 | -8.48466 | -47.50541 | 2025-06-23 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fa6efa6-b172-3cdf-9291-3705a813ac5f | -7.45025 | -45.56227 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 385d716c-ba77-3fce-a5ec-f8d3708efb42 | -9.0865 | -49.62622 | 2025-06-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 278679d1-3851-3586-a106-e0b1db91a88d | -5.11015 | -43.14716 | 2025-06-23 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6882feb1-06b6-368f-8f73-4ea97972c237 | -7.46821 | -45.55709 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4eea89a-1ff3-3a15-8ff1-14925305511d | -8.11884 | -43.14642 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cab70ebd-fa3e-3be8-8356-3fe637cbd5dd | -7.44983 | -45.56258 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96edd61e-97ce-3dc1-b9be-1fc98cb43830 | -10.06813 | -49.66209 | 2025-06-23 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3af1fd0-d279-345a-bb40-f2a72b9c32f4 | -9.41953 | -48.41401 | 2025-06-23 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| df41e56d-3754-3c37-b536-60a37d615511 | -7.30789 | -43.21288 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3614b54d-db11-3ba3-b83a-49f5115f8275 | -7.30867 | -43.20732 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 506d3baa-fc09-30f3-a75b-08fecd6adbfc | -10.06121 | -49.66103 | 2025-06-23 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9ae2f35-295c-333d-9461-e0a3bf594f54 | -7.45041 | -45.55872 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33415830-704c-383c-b859-b12a6b777f09 | -5.42212 | -45.11034 | 2025-06-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 874389a5-60b8-3663-8593-05b9337b9c85 | -10.14823 | -48.98761 | 2025-06-23 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9abf37b-2d3e-307a-bb84-28bc74e03c24 | -8.48776 | -47.51068 | 2025-06-23 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bec2da88-1e2e-3808-9c34-b17016ede599 | -8.06791 | -43.11146 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a0df656e-a6fd-3c3e-ae25-9e343e1992fa | -8.10955 | -43.14413 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bb79453f-2a94-3bb3-8f23-9978af46f7b2 | -7.31283 | -43.21361 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3337fa59-7331-3c7f-909f-f468ce643b67 | -10.1524 | -48.98407 | 2025-06-23 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31db5b0-7bd2-3dfc-9cb2-37e094e61b56 | -8.06166 | -43.11956 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0d9fcbbf-cb10-3b45-b25e-368e5b43f78c | -8.06913 | -43.1026 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f2e86b8d-8452-324a-86fa-66445a0b7f27 | -7.34966 | -45.33425 | 2025-06-23 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d13382b2-5713-38d0-bad7-52bf81bdd128 | -7.31777 | -43.21439 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84bea0a3-4d71-3998-a223-dc4ab18eb007 | -8.09364 | -43.14785 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a48d699f-5b03-3f6d-9166-fc0660a233cd | -10.05776 | -49.66051 | 2025-06-23 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ac9f7c5-acda-3c37-a06e-6cf912aec1ad | -8.06287 | -43.11076 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 77cb1b72-aa3d-3ba7-b86e-faaa7a2a318f | -5.57183 | -45.20967 | 2025-06-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1acb4fff-18bd-3990-858f-e634da1ce087 | -9.14996 | -48.97101 | 2025-06-23 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed2e03e3-12d7-366a-aefe-c5caab4b3306 | -7.31362 | -43.20802 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 841a258a-b059-3851-bc88-5a9ee5701ccb | -8.10914 | -43.14704 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 86f23498-3d41-39aa-a737-8601efb5415d | -8.11342 | -43.14864 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7030b1b6-3e3e-31e9-a5ea-60c623a3dad3 | -8.10878 | -43.14499 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fc4930ef-11e2-337c-b08c-4c7f3896bec0 | -9.41527 | -48.41776 | 2025-06-23 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e1c594b-6eb0-32f1-9c80-67beb258554b | -10.45147 | -47.02224 | 2025-06-23 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| deeba2f8-1af6-37fe-ae35-657e10ac3b3d | -5.10534 | -43.14648 | 2025-06-23 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 571ad756-301d-3965-81af-a27b008cc565 | -8.39997 | -47.14123 | 2025-06-23 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec520146-ff0b-367b-812d-5ba69872125d | -5.49495 | -43.98411 | 2025-06-23 04:44:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 694aabc8-c772-3e18-a62d-917531874ba7 | -5.49564 | -43.97948 | 2025-06-23 04:44:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11bf7e1e-9ff0-3e17-adee-2af233dddd15 | -7.29695 | -47.84048 | 2025-06-23 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ba083b8-2d89-35cb-ab1d-f3b2945b6808 | -7.44821 | -45.54617 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4e2e3f9-627f-3863-b5bc-c93404e7c386 | -8.3961 | -47.1407 | 2025-06-23 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 21a7899f-21e6-3cf6-affe-387f42bd3c21 | -9.9105 | -52.44226 | 2025-06-23 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c859156-ae52-31cb-9ee2-0ffdaff12ffe | -7.35877 | -47.75123 | 2025-06-23 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a98f9f97-b4e8-3ded-96d5-71dd2ab9d7e5 | -10.44747 | -47.02171 | 2025-06-23 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a81ee762-44d0-3618-9954-d0a8b7318ad5 | -7.31204 | -43.21924 | 2025-06-23 04:44:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3fa6efb-8cf0-3b77-9963-9b13660f1e41 | -7.44312 | -45.54973 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6b04935-096c-3c38-bf91-6dfa886668a1 | -8.40383 | -47.14176 | 2025-06-23 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3197cf85-50b3-3df4-9166-0d53674a40ca | -7.94672 | -46.04362 | 2025-06-23 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a42c7f6a-fcd3-3ceb-a703-54769f3f973a | -7.64204 | -49.54706 | 2025-06-23 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acf0a8d0-ebc4-3175-bfce-10e59bff72d8 | -8.06126 | -43.12249 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1447c7e0-88e8-3e6b-9d8f-f549e28a3d67 | -8.0663 | -43.12318 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 47becdc4-64b2-3322-878e-c3baf4d35738 | -7.46399 | -45.55651 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0b22a1b-c88f-3ca9-9f27-03ef0094d5ac | -7.44198 | -45.55746 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9bd9be8e-eb3d-3e97-a5d3-ac05c5e333b0 | -8.06207 | -43.11663 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f6cb6b8f-c80f-3dd0-b8c7-54a5e88d9cf8 | -8.09867 | -43.14855 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b567a66f-a62d-3972-b34b-480d6f65fafd | -7.46876 | -45.55324 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a78e9b6e-904d-336e-a3f0-3a68c7fa57a5 | -8.11458 | -43.14482 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d769f218-542e-3e57-8b07-61f73417f333 | -7.46454 | -45.55265 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9e682a2-7fe5-314a-8f14-3bac5ee873e8 | -8.09323 | -43.15076 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02403ad7-e8e2-3b42-8e76-494c24cd5314 | -7.4429 | -45.55327 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a60522bb-3b9f-3b1a-bde4-44469f0ab00d | -7.44619 | -45.55808 | 2025-06-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f2e103f-8684-3f85-9f3a-397c24895f26 | -8.06751 | -43.1144 | 2025-06-23 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e893587b-6486-3749-88fe-4dbdec623412 | -15.51704 | -56.03377 | 2025-06-23 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f693ec-410f-3268-92ad-34b79f57f2fe | -16.21234 | -49.97657 | 2025-06-23 04:46:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e907817-7e68-3fbb-bc46-a000e49dae0c | -10.86928 | -53.76188 | 2025-06-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 889a3982-1e69-3b14-9343-29b2db9f87e5 | -13.66314 | -43.66452 | 2025-06-23 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c47a9c26-80d4-3228-8cab-87f9cef7fc52 | -10.94991 | -48.22411 | 2025-06-23 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb06cf5e-ed66-39bb-aeee-a96dd039187f | -13.26703 | -46.81956 | 2025-06-23 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39e165dd-e044-384f-95cb-6b18ea37b0ef | -11.6181 | -58.28136 | 2025-06-23 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ee7919-f3db-3e50-a088-693fbcb41aa1 | -10.50807 | -53.58598 | 2025-06-23 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README9.md)
