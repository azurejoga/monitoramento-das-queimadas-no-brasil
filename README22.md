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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfe5c8af-4c91-3d86-b284-6988ee2d8a26 | -21.85841 | -46.08216 | 2025-09-09 03:47:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cfea902b-2432-316d-a02b-5b7bce154391 | -22.21614 | -49.72763 | 2025-09-09 03:47:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15dc45f8-e03e-3d60-97c5-3cee65617598 | -19.57948 | -47.3968 | 2025-09-09 03:47:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a323b98c-0706-3176-a5cd-b6a2574ecf94 | -20.99374 | -49.31546 | 2025-09-09 03:47:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0764f553-aacc-306a-881c-56b1c56e2133 | -21.7229 | -46.23095 | 2025-09-09 03:47:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ad8eca79-9e44-3a37-af58-9396b3bbe194 | -19.90395 | -43.85537 | 2025-09-09 03:47:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ac441186-f441-3c03-9247-65f678e67db3 | -21.58147 | -50.35602 | 2025-09-09 03:47:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 8800fa45-3171-3536-82f0-9fb62c610166 | -21.00015 | -49.31305 | 2025-09-09 03:47:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f808c6d7-6ba1-3d17-bfa4-099c86e1497e | -21.23563 | -49.87894 | 2025-09-09 03:47:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5bb12c24-dfcd-32e5-a492-bcb26cfc33db | -20.08039 | -47.35573 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b5194be-aaa8-3cf0-8724-8d1e959e5ef0 | -20.59096 | -47.84548 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae5c928f-eac4-3b4e-9193-ed1cd58738a5 | -22.33365 | -49.02245 | 2025-09-09 03:47:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc5fe1a1-45d4-39b4-9ca9-3848cecb0646 | -18.8218 | -49.68901 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c76f90c6-b2e1-39ac-b055-010b57bf42cf | -23.12865 | -46.83226 | 2025-09-09 03:47:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1a2f74c0-e6ad-3b63-a0a2-43074c2cadec | -20.59611 | -47.84659 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0e50180-7bcf-307f-a619-b3dfb56105d4 | -23.49134 | -45.43856 | 2025-09-09 03:47:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 282948b8-46f9-3afe-97a1-ca9bbc01c7d2 | -21.43871 | -48.8658 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6614c836-6f0a-3833-9a2e-882f6cb341ea | -20.02985 | -48.53622 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7f9bf074-f826-35a9-bac7-53d7973207ee | -21.44119 | -48.85457 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 923bef99-fe13-37a3-b9ec-a4b8419b74e0 | -23.21824 | -46.60973 | 2025-09-09 03:47:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7573a13e-dbab-301c-9d0d-7378fffddcbd | -21.43826 | -48.8423 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| a7449bc5-6f65-3492-a130-0bbf0757985c | -18.81534 | -49.67834 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 178e5ce6-b245-3b24-b101-143be6ef87c0 | -23.71976 | -47.46422 | 2025-09-09 03:47:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4e237545-0267-3b62-a412-7920784b56bb | -21.43371 | -48.83734 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2734818-0dc7-3588-9f7e-bb78b24c7666 | -18.82716 | -49.68135 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 88c230a8-05a0-3b81-89f1-e632da9ceaa4 | -21.44817 | -48.84855 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e70eb45b-98c2-3560-b4a1-34a969bc5ece | -19.72464 | -43.91396 | 2025-09-09 03:47:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 810b4d28-c3c6-3367-bcc4-2de77bc5871f | -22.92389 | -49.16431 | 2025-09-09 03:47:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b22d7ee-6d4a-3843-9faf-eeade5110ad8 | -22.22339 | -49.72158 | 2025-09-09 03:47:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6f451cc6-d4c9-3c47-87e3-d3d8005e8e1c | -21.44898 | -48.8449 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 0a9c2d6d-6610-3f35-9baa-09f10b419d0d | -20.47156 | -43.95885 | 2025-09-09 03:47:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1ef3cbae-320a-39b9-ad79-41d0dfa70dce | -22.8945 | -43.58282 | 2025-09-09 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 459fcad7-efbf-3e13-9346-f02df496df52 | -21.4562 | -48.8222 | 2025-09-09 03:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f44fc4b6-78bb-371e-8fcb-17abab1704a1 | -17.6847 | -52.2615 | 2025-09-09 03:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 541a32ae-e3ba-3a52-949e-ef604e0159fe | -18.8375 | -49.6777 | 2025-09-09 03:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| f5b6d2c7-38a1-3010-ac3f-434d5f112cf8 | -10.0111 | -64.9151 | 2025-09-09 03:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fe4b1f8f-b0df-30ac-a02a-6c61fa86fb6b | -21.4555 | -48.8455 | 2025-09-09 03:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 99f93f23-54e2-3d6b-8495-e7a7f5d5d671 | -12.1988 | -53.9024 | 2025-09-09 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9eb0491d-e12e-3546-9273-2a089a734e86 | -18.8174 | -49.6816 | 2025-09-09 03:50:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 61624c8e-d260-3ccb-80e2-7fe90ab1d96f | -21.4348 | -48.8503 | 2025-09-09 03:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 142b9f4b-0077-327f-916c-830398cb011f | -22.665 | -51.3857 | 2025-09-09 03:50:00 | GOES-19 | TACIBA | SÃO PAULO | Brasil | 3552908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| c0b840ce-38b0-3f42-87ec-ce9967b1fffb | -12.1991 | -53.8817 | 2025-09-09 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 26dba920-9402-3d53-8295-019556606ead | -21.4355 | -48.827 | 2025-09-09 03:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 03cb7ffe-753e-3937-a048-c045aa02ead8 | -10.011 | -64.9339 | 2025-09-09 03:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 169efc82-5ced-357b-b3fa-64d9ffb88532 | -10.0111 | -64.9151 | 2025-09-09 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 19f5fd30-1811-302f-aab6-b621eab8afb3 | -21.4355 | -48.827 | 2025-09-09 04:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 53dfb357-a42b-32c3-ad9d-6d396987a612 | -21.4348 | -48.8503 | 2025-09-09 04:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 611c64dc-4279-3b43-8ca4-3e031744eecf | -12.1988 | -53.9024 | 2025-09-09 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 3e74abc7-b8b5-30c1-a1cc-401fb8f133ae | -18.8375 | -49.6777 | 2025-09-09 04:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| acce2a0b-23f7-3615-a452-cc813068b99d | -18.8174 | -49.6816 | 2025-09-09 04:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 566d6853-bae0-3ec3-b848-77365dad86a7 | -21.4562 | -48.8222 | 2025-09-09 04:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 128.2 |
| da1ca30b-89eb-36cb-82f2-ddbe7bca9ef7 | -21.4555 | -48.8455 | 2025-09-09 04:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 052876c6-9ab9-3e2e-9ab5-48145d6cd53a | -12.1991 | -53.8817 | 2025-09-09 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2244a286-c58b-37ca-97db-ed549eff891e | -17.6847 | -52.2615 | 2025-09-09 04:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 8a42b19f-0c0f-3978-b45e-d122f65e6bd5 | -10.0111 | -64.9151 | 2025-09-09 04:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5eddbbc5-6cec-3343-9620-ec8b04ef4968 | -10.0111 | -64.9151 | 2025-09-09 04:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8520f6b7-b2cc-3159-9886-648946494561 | -5.94308 | -44.89166 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7c612ec-3576-3b86-be4d-218a5dd1f7b0 | -3.79325 | -48.87301 | 2025-09-09 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047659df-1688-3dab-9077-db80695044b6 | -6.82127 | -44.9006 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 453ef742-3d56-3416-a75d-7b5a8242282e | -5.86067 | -45.29645 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9818f6-c0f8-3baa-a1e0-1e9810f659b8 | -5.30674 | -44.51197 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8c42bbf5-af67-33ae-965c-83ccb1775bbd | -6.83207 | -44.9024 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 439b976b-5c68-3de3-8990-bee978d421a4 | -5.42448 | -42.81471 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fc1c466-2d6c-3cd2-9f47-e729db5bc86f | -6.86752 | -45.60216 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d71fae-1905-34cb-a454-8fc48b8b656c | -5.69671 | -43.89106 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92afb768-2f67-34f2-9913-6a3047a90474 | -6.48136 | -41.76611 | 2025-09-09 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 89ce6479-e3fd-37e2-9439-3586709c9e4d | -6.58946 | -44.0099 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c2fe2793-5505-3174-aa7a-d498792d38ed | -5.42021 | -51.5401 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92a89044-d789-3e56-9882-62a85d38ac1f | -5.08208 | -42.42839 | 2025-09-09 04:32:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed7f2463-8a89-3cb8-9b99-90a14399772d | -6.29954 | -43.82128 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40150953-6c78-3556-b9f9-59449b87651d | -4.70022 | -55.67533 | 2025-09-09 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c507ac7-5361-3bcb-aaa6-a074ca402226 | -5.76337 | -45.52818 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b811be70-0699-3fb5-b658-8dd86a7b4505 | -4.97988 | -43.63443 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e822a17c-e4d2-312e-bb8d-5d4d7583f3b9 | -6.21246 | -45.57437 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9658c346-06b1-3ad3-a68a-7e11e17b14a1 | -4.11828 | -47.13021 | 2025-09-09 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edcc6843-6500-3e2b-b1a3-714bd3f951c3 | -6.49952 | -43.98896 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51ec7429-5e37-385c-88b6-4953c63b70bb | -5.67962 | -43.90238 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f7cf1e4-06f2-3fcf-bd53-b61b528e74cc | -5.72116 | -45.40755 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f6ae3e8-a4e8-3609-a38a-e76ad47d5cff | -6.20946 | -43.36336 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8189d68f-5f4c-3604-ae7a-58580817e6dc | -4.99333 | -56.25669 | 2025-09-09 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4409a72c-1679-3f4b-80a5-d9ca269e6634 | -6.25022 | -43.49799 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8047ef66-df73-3345-8cbe-d1aec1bef674 | -7.10618 | -43.89382 | 2025-09-09 04:32:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a871784-5ffd-37d8-a442-ba0dea4d4ad2 | -5.62017 | -44.37301 | 2025-09-09 04:32:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7d574fa2-0396-3cff-874b-2ab6b380e8a6 | -5.11384 | -43.77655 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0877cef4-df55-3bfb-a823-981c6a848530 | -5.86447 | -44.19275 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32ee0b02-cbc3-352a-8269-c26b9188cf3a | -7.1069 | -43.889 | 2025-09-09 04:32:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28092b61-9db8-3a19-b722-3e6c74f55510 | -5.67012 | -45.30928 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7b409d6-d042-36f8-b39f-d6cd3411574c | -5.28064 | -42.66618 | 2025-09-09 04:32:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 889c9792-df6c-3663-811a-691b7f114810 | -5.80947 | -44.83924 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a84da792-d14b-3f82-8704-6b0a5eb73df1 | -6.08671 | -43.35305 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8b367d0-f534-39f2-ac4b-716720330dd4 | -3.30755 | -48.71981 | 2025-09-09 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65429032-8f94-3574-b517-2009a3a0d034 | -6.55417 | -43.90753 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5d7e443-1952-395d-8823-711caf55fadd | -5.92576 | -45.95694 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cb5a8d6-ae58-3024-8ab7-4882357dafaf | -5.43395 | -43.423 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bc38e6b-fb55-3966-bd36-b80b0a2984d3 | -6.10566 | -44.13353 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 812f77c8-4518-3aaa-9c1a-f0c30f541e1b | -6.21593 | -45.57492 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc1cbf83-5a5e-3ffb-b5a5-7fde180ec4d8 | -6.95136 | -46.31491 | 2025-09-09 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c08d005-2c8e-3c95-b764-cb8e9edc99eb | -5.39723 | -43.2362 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3392a248-60f2-3529-8d00-9bfa9ee16bf3 | -4.53223 | -54.8451 | 2025-09-09 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d769363-c243-34d5-89e9-074ab821965c | -5.71176 | -43.89336 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README23.md)
