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
| 3d0ba4fc-cd27-3c6d-b016-dfa54c5bc8fc | -11.30791 | -51.40928 | 2026-06-24 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5425d85-d4e4-3451-b18a-2371d15c26ee | -9.92295 | -53.4579 | 2026-06-24 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be43f2d9-1b0e-3d7e-8f65-8b2fbf94503e | -10.69941 | -49.61032 | 2026-06-24 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 180f714f-deab-3372-a7fc-cdd0c3b57644 | -10.39185 | -56.71896 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9545a3a2-8767-31ce-b14e-0a4d22ee1aee | -12.82845 | -44.35625 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70161a5a-5491-3ee1-bd96-0497bec71b5b | -12.83974 | -44.3676 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b6cc547f-35be-359a-8878-4d568a17804d | -9.94337 | -53.45664 | 2026-06-24 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac322381-93a6-3790-b0c7-f06cf42f0232 | -12.87498 | -44.37054 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 092fbc74-d2d1-315d-bb0a-bc2f1a9b130a | -11.79055 | -57.35732 | 2026-06-24 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4948c66-b70f-3e41-8f0b-1ed9cc0a0db8 | -10.90418 | -54.1269 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ef9224-0e6a-3a9f-8886-a13550d98b39 | -11.48332 | -46.74035 | 2026-06-24 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71142371-33a8-3fb1-a87f-9b22f4e6fe52 | -11.51554 | -56.12348 | 2026-06-24 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5092dd7-0cab-3a93-898a-9a6c9fb06b31 | -11.30454 | -43.3308 | 2026-06-24 05:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb31c7c3-b7aa-3670-8d62-491ab34e27be | -11.37303 | -55.8106 | 2026-06-24 05:10:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fe34385-cd6c-3ffd-91c3-1b4ed11bef0e | -12.46776 | -57.18864 | 2026-06-24 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b580a75-4ba0-32bd-a827-c2271c7e34a4 | -13.0666 | -53.3615 | 2026-06-24 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e831a68c-ffa8-3a8a-9f0a-cdfa114804d9 | -13.85227 | -47.04168 | 2026-06-24 05:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ace7a91-44b4-3375-be64-287f7d44ee9b | -10.38789 | -56.72201 | 2026-06-24 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bfd634d-e2e5-3b62-86df-8d88f10dfb9b | -11.30486 | -54.71656 | 2026-06-24 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f14c116e-02b7-3fb0-8fb6-f53d63230810 | -9.79148 | -56.95407 | 2026-06-24 05:10:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25aa27b1-d9dc-3df3-9c47-3a900f359ee6 | -12.72948 | -49.08969 | 2026-06-24 05:10:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32e40c20-e578-31b1-9ca0-56d05e061511 | -12.78746 | -44.43958 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02e0033c-402e-3847-90c1-7d4a1b076d56 | -11.54411 | -48.26667 | 2026-06-24 05:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a96eccd4-1233-3ee5-9611-58fb70867c08 | -11.111 | -54.14359 | 2026-06-24 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73578cf1-ea3b-3303-9a0d-05a389b0d8ba | -10.53888 | -53.73703 | 2026-06-24 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 589fff05-a69d-3cd9-a49d-9c03a47e75d2 | -13.77296 | -53.07439 | 2026-06-24 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf9f06a5-7381-3151-b39e-fa3982891ebe | -12.77962 | -44.45343 | 2026-06-24 05:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a020b04-c542-3d4d-bd14-4e38f9535e22 | -11.51107 | -56.13002 | 2026-06-24 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf29acdf-7b61-3190-be1f-9398d6fba527 | -12.8552 | -44.3389 | 2026-06-24 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 99c0d22d-1d8e-3208-b5c0-054d518fc7ae | -12.8359 | -44.3422 | 2026-06-24 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 37cc7598-8ec2-36a5-aa6d-fa10256230ca | -13.0635 | -53.3546 | 2026-06-24 05:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1cdd2488-6d54-349b-a380-774d3ecade0b | -12.8548 | -44.3625 | 2026-06-24 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 260.2 |
| 5ee1c83a-baa1-37bd-b40e-e2ced0d26bb6 | -12.8354 | -44.3657 | 2026-06-24 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 364.4 |
| 89d07f04-c85d-37b7-8a84-9eaca2b6d91c | -3.50959 | -48.04092 | 2026-06-24 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e08f91b-fec9-3e03-ba3a-f958cac92344 | -6.84543 | -47.90609 | 2026-06-24 05:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46d24c61-8779-3508-8dd0-d4ecb96310f1 | -6.84617 | -47.90059 | 2026-06-24 05:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3feacb7c-e8be-3186-81e1-bc77facb0cbf | -3.5103 | -48.03608 | 2026-06-24 05:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90d8c162-7d6c-387c-a7e5-fc9779525a8b | -2.73763 | -58.18869 | 2026-06-24 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a205f43-2489-3f14-93dc-51c697072ba5 | -10.15771 | -56.62336 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 514dad5e-75ab-3b43-a1dc-fe85d36e1975 | -11.30519 | -54.71547 | 2026-06-24 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38e05ea6-f982-3e21-b40b-29df9d6047ba | -7.91256 | -48.28825 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a2da10c-f48a-3bb0-9802-98e6c8849e25 | -10.16019 | -56.63429 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f907b70-dce1-3d1e-b75f-281ecf917c76 | -11.27959 | -55.79559 | 2026-06-24 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0044d00f-797e-349f-9861-9746c27d24e7 | -10.5403 | -53.73498 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56ca09a7-d78d-3368-b63a-3fcba50dd5ac | -10.90193 | -54.13147 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b715688-2197-3ff6-9f2d-50d2553ee2f3 | -10.38442 | -58.51801 | 2026-06-24 05:27:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a509b65-a142-3a7c-b8ca-cde328e0a3fa | -9.18361 | -58.07249 | 2026-06-24 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f5ecfe-fe32-3ab6-bf85-4a5050ad9ae3 | -10.11253 | -47.55761 | 2026-06-24 05:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cf9a674-8d60-3081-8b4a-664e8cc98ebb | -13.77159 | -53.07498 | 2026-06-24 05:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9c9a067-fa2f-35ae-9584-58c6c7781414 | -10.90261 | -54.12632 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0846c376-a209-3739-8c2a-964de6e469f3 | -11.27674 | -55.79328 | 2026-06-24 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75d81756-590f-320c-9e8f-50cb46cfb41b | -13.06077 | -53.35466 | 2026-06-24 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7ff844b1-a3c1-3902-ac69-3b50d6f75704 | -10.39146 | -56.72517 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d48d818a-017d-3a20-a0ee-e94fc18f580e | -12.54666 | -54.60226 | 2026-06-24 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60f74b7e-35d8-3a3d-918c-41a1cd3ec11f | -10.11341 | -47.55041 | 2026-06-24 05:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7f64400-884e-33c2-bfab-dbad24c163d1 | -10.39075 | -56.72211 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1d99a885-2c85-3367-b100-40b483938152 | -10.10867 | -47.55827 | 2026-06-24 05:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6c12529-501a-3b67-89a2-c8de78a4c6d8 | -10.39146 | -56.71702 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67a8caa8-01c3-3255-b1b1-4ba38b33b017 | -13.77691 | -53.07565 | 2026-06-24 05:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54c69d03-3f05-314c-bbf4-cbfa0e8fd0db | -10.10949 | -47.55116 | 2026-06-24 05:27:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 247416bb-1f91-368c-b8ab-6c404926f032 | -13.06594 | -53.35537 | 2026-06-24 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c499743-6de3-3348-a77e-f32d17cad180 | -9.3688 | -50.53485 | 2026-06-24 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66a782d1-2f32-353d-8aed-29a4171aa669 | -7.92275 | -48.29201 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0dbd9c14-a983-35de-b581-d899f06d7a7c | -13.06555 | -53.35847 | 2026-06-24 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a52a8286-baee-3109-98e9-0f367b61be36 | -14.53977 | -49.10413 | 2026-06-24 05:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3e573c9-1117-33f7-bb0c-0379fae30a6c | -7.91609 | -48.291 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bd99b4ac-1b42-314a-bd5e-c36ec4569e2c | -7.91843 | -48.29517 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 87796d8a-5a70-3082-b680-26ad91c0cae5 | -7.91175 | -48.2943 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b58f165-713b-3978-bef7-d79ee0183123 | -11.51395 | -56.13049 | 2026-06-24 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25729440-3d04-3955-ad3c-84f8975dc85f | -10.16243 | -56.61879 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3212706a-ad2c-3646-8e0b-0001e0b97b3f | -13.07111 | -53.35606 | 2026-06-24 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e185ca-668a-39bf-af8d-acc3170ea3c3 | -10.76776 | -54.10917 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81c0465c-93f2-358d-918e-dc6ab94b4856 | -10.81951 | -58.02069 | 2026-06-24 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cab38c0-90ec-38f6-9c92-d3551ba8fcdc | -10.27459 | -60.54496 | 2026-06-24 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f4c2b16-aa77-3503-adf5-7d12417a5b40 | -10.5778 | -57.32053 | 2026-06-24 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85627490-92f5-309a-ba36-2f37b409cdf9 | -9.18424 | -58.06831 | 2026-06-24 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059be626-033f-36de-a4ac-a815032f8c5a | -8.68738 | -47.85367 | 2026-06-24 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 32559ede-6580-31fb-9ef4-2275f6a6a65d | -10.28181 | -60.54245 | 2026-06-24 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94258ffb-850d-390c-b2b3-c980273334f6 | -9.17828 | -58.05877 | 2026-06-24 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20a48b5f-0093-3dea-bc3b-92cb2347fe0b | -10.27848 | -60.54193 | 2026-06-24 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3740228-52c9-330a-98be-7b452eaccf13 | -11.88781 | -55.13839 | 2026-06-24 05:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0ac68a0-cbbe-3efa-be8a-6b76ec4bc59e | -10.38895 | -56.7146 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ada45822-c4a5-378d-a365-d0e37ff47250 | -10.38821 | -56.71968 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 863b0aa0-53ed-3adf-8136-88a670d8a4a6 | -11.51503 | -56.12269 | 2026-06-24 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f54c001b-b92e-39c2-a115-2b7b5ecb59f1 | -9.92396 | -53.45919 | 2026-06-24 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d244faa-2469-3211-bbe4-352beffe20bd | -10.57848 | -57.31578 | 2026-06-24 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98df917e-99a4-3dc1-93d7-5b9c5c5747cc | -10.906 | -54.13726 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8aed4a7a-9a3f-307b-821f-17284eeab41e | -8.68005 | -47.85311 | 2026-06-24 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb7012cf-0189-3ff3-ae80-80b6fc55bdf5 | -8.68042 | -47.85309 | 2026-06-24 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79fc2e15-25ef-3b60-8cef-85b5616f452c | -11.27731 | -55.78921 | 2026-06-24 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f06f110-c203-3157-98f7-3d36ed487a3a | -10.90668 | -54.13214 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8be5036c-00d1-36d7-945b-d426a390eec7 | -7.91922 | -48.28929 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46c61e73-1b29-3096-84a6-b7b968ae7f75 | -11.51085 | -56.12207 | 2026-06-24 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63ef10b9-63bf-3e25-b5cc-4321401a2efe | -10.76838 | -54.11168 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 321ca303-20f6-32a9-a52f-5e72ad1950ab | -8.12788 | -47.88837 | 2026-06-24 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a939ce60-a2b3-38b3-9503-6d5e091be762 | -12.21928 | -57.28562 | 2026-06-24 05:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2db75b70-3508-3ee5-92d9-f0b9e31814e6 | -9.8029 | -48.92039 | 2026-06-24 05:27:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3b4cca3-d0d0-3739-bbb2-b0cd750103f0 | -11.30453 | -54.72029 | 2026-06-24 05:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9037e7b-2772-337e-b67d-3b44496f5d14 | -11.28042 | -55.79799 | 2026-06-24 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5edfe55-d5d7-3411-ac33-f5b0a3c0fff3 | -10.16093 | -56.62914 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
