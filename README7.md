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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 088b0d62-8c68-3993-8b0f-0de6e2f47d6f | -15.16463 | -56.46924 | 2024-12-31 05:25:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11686cd9-2a76-3025-874f-17c63dac1eee | -15.36857 | -59.8889 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99d9e5c8-4ff7-3704-8bfb-58ff0611551f | -15.16897 | -56.46991 | 2024-12-31 05:25:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d18c156-6a47-32af-8321-25c49ce6eb32 | -15.16028 | -56.46858 | 2024-12-31 05:25:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64c9bd97-d176-3dec-8aae-3c68c74e12ab | -17.74405 | -56.32375 | 2024-12-31 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1f6f8c8d-85c6-37df-aaa4-d2e06e160080 | -20.50408 | -55.80423 | 2024-12-31 05:27:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a800c43f-5d5d-3dce-8643-4c748bf8d18f | -22.11961 | -51.46183 | 2024-12-31 05:27:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 8056f050-91da-3b3f-845d-c38617df66b2 | -19.83067 | -57.47433 | 2024-12-31 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e8f5600b-943e-367a-aad9-0f36c42b964a | -19.83883 | -57.47987 | 2024-12-31 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bc52ffb1-6dcf-33f2-a5a1-fe0c4b7c0603 | -19.83502 | -57.47493 | 2024-12-31 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b6190153-89a1-3bdd-8b49-648d8341cff9 | -22.11916 | -51.46745 | 2024-12-31 05:27:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| b5f1f946-5614-3ef5-a2ce-92d55ffa40ad | -19.83936 | -57.47552 | 2024-12-31 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6d903193-23d5-38f5-93a0-2ab7739deece | -1.64857 | -45.8604 | 2024-12-31 05:33:00 | AQUA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| faab7a29-0513-3119-a703-45fac291a5eb | -1.25227 | -46.60105 | 2024-12-31 05:33:00 | AQUA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 417f1866-ff29-36b0-8c53-6a93efd4d5b4 | -1.64994 | -45.85119 | 2024-12-31 05:33:00 | AQUA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65931193-9fea-33d0-a445-1d67fde80890 | -1.27035 | -45.73368 | 2024-12-31 05:33:00 | AQUA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bcacd243-b111-364d-a9b6-7f83a138e91d | -6.95765 | -42.9958 | 2024-12-31 05:35:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 61a18880-a823-33d4-b932-c75fad54fae2 | -22.1136 | -51.46695 | 2024-12-31 05:40:00 | AQUA_M-M | ÁLVARES MACHADO | SÃO PAULO | Brasil | 3501301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| f4feb165-87a1-34b4-bad7-9bfdfe327a31 | -22.115 | -51.45744 | 2024-12-31 05:40:00 | AQUA_M-M | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| c94d0ac9-4c97-3f33-b7da-e56deb133f28 | 3.56923 | -60.21662 | 2024-12-31 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dce6a7f5-a5b1-31d4-9e9d-d195a18f96d3 | 3.47232 | -60.45955 | 2024-12-31 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a95952d-1a76-3a67-b80d-1cb508991ac4 | 3.26439 | -60.54034 | 2024-12-31 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db4241e0-3aa7-3347-9d25-1b2487ad09ac | 4.18436 | -60.61825 | 2024-12-31 05:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82ff4f46-a16c-3c43-b3d3-a10101846fc6 | 4.18737 | -60.61311 | 2024-12-31 05:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f836889f-c020-38fa-aa25-f0b518fa0890 | 3.62748 | -60.40786 | 2024-12-31 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4b25d21-d74d-30f6-b728-a8b6a90c8344 | 3.4769 | -60.46363 | 2024-12-31 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbfd46ca-f8bd-3d4d-b951-f8221a040190 | 3.57001 | -60.22146 | 2024-12-31 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6683d655-985e-3267-8fd0-72c302b55b4d | -9.9045 | -65.11803 | 2024-12-31 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9043a515-4537-3cae-8c6a-ad3710c310af | -9.47708 | -66.04032 | 2024-12-31 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 790f69c4-a7cd-3667-a57b-ce60e4c830cf | -9.47369 | -66.03981 | 2024-12-31 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5653b6fc-a8e2-39c6-9dad-0a3c9d655ad8 | -9.90067 | -66.81078 | 2024-12-31 05:48:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9e7290a-5140-3131-b6c3-4f80bd11da38 | -19.83734 | -57.48349 | 2024-12-31 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c30c869c-bdc2-3a22-a05b-1554dcfcfa9c | -15.37472 | -59.8862 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8df80d46-820e-302b-9d29-a6c688f3d93d | -15.36871 | -59.89208 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7b4114a-819f-3ed9-8161-c8c5129d3d71 | -19.83026 | -57.4765 | 2024-12-31 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3575e356-2779-3522-9a88-06a6225cba4a | -19.83668 | -57.47713 | 2024-12-31 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 77584ff1-57eb-396e-8f82-3c81a3680aed | -15.37489 | -59.88646 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8127fc9-5dd1-3854-8b45-679168cddc22 | -17.746 | -56.3223 | 2024-12-31 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 37779fba-7cf0-3e39-a39e-84d7b9d1cb4a | -20.50255 | -55.80783 | 2024-12-31 05:50:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8e1dc22-dd0b-3b59-8e28-43f785eb3bfa | -15.38049 | -59.88385 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab1c65fa-b3c0-351b-aabc-31c28ee2eadc | -15.38035 | -59.88358 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd8d436a-6ada-3d37-8624-21f8b086db60 | -19.8378 | -57.47799 | 2024-12-31 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 112a3eb1-5fe0-3dab-a75b-3f0a598b491c | -15.37525 | -59.88319 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26a84256-5fe2-33ca-9621-9833d1e3673c | -19.83619 | -57.48262 | 2024-12-31 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 15f0f96f-65ef-34fd-b3e1-7a8b09a4bac9 | -15.37995 | -59.88685 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4d3119e-e36b-3fc6-b431-705347403632 | -15.38086 | -59.88058 | 2024-12-31 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f77e5997-eced-3fb3-8dfb-8e3529f5d612 | -5.10873 | -37.02414 | 2024-12-31 11:34:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 54.4 |


