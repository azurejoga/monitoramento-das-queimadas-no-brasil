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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03271059-c671-35fa-9769-c22fe3cf3516 | -12.9091 | -62.415501 | 2024-10-05 01:09:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78a7ed07-a542-30f2-9f16-86c3e9c3be7f | -12.9118 | -62.429001 | 2024-10-05 01:09:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aad9aee8-e534-3cfd-92fa-be67277a6a51 | -12.9145 | -62.4426 | 2024-10-05 01:09:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39687b0f-2cfe-3a97-b075-18e08298c5b4 | -12.8799 | -62.421398 | 2024-10-05 01:09:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7e608c0-1826-32ad-8256-7f6992b2bddd | -12.8825 | -62.434898 | 2024-10-05 01:09:16 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73dcd1db-7e46-3ba3-a618-ef455f6554ab | -11.102 | -54.212299 | 2024-10-05 01:09:16 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96c55a90-1c63-32ed-ae77-6d75323779eb | -11.1037 | -54.2197 | 2024-10-05 01:09:16 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47f67285-c7e0-354b-9461-7f48a07e07ee | -11.1054 | -54.2272 | 2024-10-05 01:09:16 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d447972-996b-3ff3-80be-15dcdd132b4a | -11.1071 | -54.234699 | 2024-10-05 01:09:16 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67becf2c-67d9-334f-87cc-e7afc9a45d7c | -11.0922 | -54.2146 | 2024-10-05 01:09:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b287624-8df0-3e2c-84e0-bef7a979f6ad | -11.0939 | -54.222 | 2024-10-05 01:09:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34afad04-359d-3019-a909-489700a4b438 | -11.0956 | -54.2295 | 2024-10-05 01:09:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e28dcf46-0d42-31a2-b5a9-66a3b3b2da10 | -11.0284 | -53.9828 | 2024-10-05 01:09:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddc3652f-b793-3e5a-a3c6-8b2a39a6e7e5 | -11.0302 | -53.990398 | 2024-10-05 01:09:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0879b3e6-6ffc-39c1-b087-94edfb4de695 | -10.9715 | -54.004299 | 2024-10-05 01:09:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd717f7f-0b58-3def-a1dc-e577a3f47ce7 | -12.848 | -62.774601 | 2024-10-05 01:09:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd5a87d-2fed-3c53-a220-ed4229a76790 | -12.8508 | -62.788898 | 2024-10-05 01:09:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7fe007-ac53-31ad-8e7b-42383ecc4f71 | -10.9635 | -54.014198 | 2024-10-05 01:09:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| beaa91ab-85b1-3fc1-87e3-9c88f739473d | -10.996 | -54.244999 | 2024-10-05 01:09:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 539c1657-78cc-3588-ba6d-442484890c1a | -11.0746 | -54.768101 | 2024-10-05 01:09:19 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 247ebf95-38d0-3ab0-a187-ecae025b65a1 | -11.0762 | -54.775299 | 2024-10-05 01:09:19 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11737ca6-5878-36c3-b22c-bc6952769fcd | -11.4874 | -56.792198 | 2024-10-05 01:09:20 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56125b3b-9ec0-3849-9be5-744467a275bb | -12.7243 | -62.919201 | 2024-10-05 01:09:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 201ac806-6183-310d-bc12-487e012ed01e | -12.7146 | -62.9212 | 2024-10-05 01:09:20 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 375e3f86-1908-3dad-bc6c-65c96504e61e | -12.6429 | -63.072899 | 2024-10-05 01:09:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 372eb47e-480e-3b02-995d-225df96ad9c2 | -12.6459 | -63.087799 | 2024-10-05 01:09:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 273f5d80-706d-3b26-8afe-6b5b3137b2de | -12.6332 | -63.074902 | 2024-10-05 01:09:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12b6fee6-f990-395a-a6d2-b1cab8848e7a | -12.6361 | -63.089699 | 2024-10-05 01:09:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca4d79e8-1bc4-32f2-9cd6-34d4e6678c90 | -10.7174 | -54.199799 | 2024-10-05 01:09:23 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0a48e4-e9e6-3dfa-9c0b-09dc0c77f2d7 | -11.4274 | -57.645 | 2024-10-05 01:09:24 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 715457de-4a97-313d-a9fc-b3e9c4a1a737 | -8.8503 | -48.320099 | 2024-10-05 01:09:30 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 581364af-b2d0-341f-a90d-5ac642f0bc81 | -10.3887 | -54.790298 | 2024-10-05 01:09:30 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65632ce5-8c07-3073-b935-d201dcac192a | -10.3904 | -54.7976 | 2024-10-05 01:09:30 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc7584b3-df6f-3a4c-8042-3055e8bfe028 | -10.392 | -54.804901 | 2024-10-05 01:09:30 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94c45844-635b-354d-9d57-4bc3e1dac67c | -9.5905 | -51.427399 | 2024-10-05 01:09:30 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8bb5e04-1aec-3b73-aec2-704a0949067f | -9.5931 | -51.438 | 2024-10-05 01:09:30 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236ddbcf-27e8-3f1b-897f-45a7eee12f36 | -10.3335 | -55.181499 | 2024-10-05 01:09:32 | METOP-B | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6de81b9-3e00-32b9-a4db-5aa2beb09a56 | -10.3721 | -55.625301 | 2024-10-05 01:09:33 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54dfcaab-3e52-3789-95a6-78990fcdb5e0 | -10.3737 | -55.632301 | 2024-10-05 01:09:33 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 254ca26c-4009-34a7-b3b2-34fa1194d3a3 | -8.9701 | -49.804401 | 2024-10-05 01:09:34 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc49eb6f-b03e-3a7a-ad5f-e309fa9d1966 | -11.9879 | -63.5033 | 2024-10-05 01:09:34 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6968fdda-add7-32cc-bce4-defca57cdbc4 | -11.2483 | -60.4599 | 2024-10-05 01:09:36 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cdf91b2a-216e-3eed-b475-fc9142b68937 | -11.2706 | -60.566601 | 2024-10-05 01:09:36 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5dbc71-ba65-3a5b-b6db-e35b9e5d8ed4 | -11.2726 | -60.576401 | 2024-10-05 01:09:36 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad808df-1f5b-3e82-9734-23e5b5e4d284 | -8.6405 | -49.092499 | 2024-10-05 01:09:36 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1ced2e8-2542-3476-8000-005a82d53b54 | -8.6444 | -49.108002 | 2024-10-05 01:09:36 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 543e133f-fdb1-3f85-b957-91d74a863271 | -11.2608 | -60.568699 | 2024-10-05 01:09:36 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b92d3228-d67d-3c8d-8f91-1d496d34c960 | -11.2628 | -60.5784 | 2024-10-05 01:09:36 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1022bb3d-f397-308e-ad94-7ef4b3fd2250 | -8.6308 | -49.094898 | 2024-10-05 01:09:37 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f23d939-4094-3e64-ab08-90a01a4d338f | -8.6347 | -49.110401 | 2024-10-05 01:09:37 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c46cd6e1-bba6-3d02-9805-85f0686d5844 | -8.7798 | -49.9534 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d952261-1d57-31e4-b610-86ed75016b4b | -8.7831 | -49.966999 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 602e7930-f76f-3358-905c-5e35675bed19 | -8.7667 | -49.9422 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e87a1efb-5d3b-318b-8196-92bffbd851fe | -8.7701 | -49.955799 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4e87d7e-b6ef-3444-ae4f-980a2002bbaa | -8.7734 | -49.969398 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5d18ed-79ef-35f0-9d8d-8bb7cf991d97 | -8.757 | -49.944599 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ada2dd1b-0049-3ca4-ae71-86367a5dd0f3 | -8.7604 | -49.958199 | 2024-10-05 01:09:38 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 011f11bd-36ba-3f90-91a7-9d25f1609a2a | -11.1912 | -61.266998 | 2024-10-05 01:09:40 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2de0070-ff24-32c5-89d4-2f08425d0252 | -10.129 | -56.7463 | 2024-10-05 01:09:41 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6392a48b-b24f-3f21-a89b-2da04dc9651f | -10.1305 | -56.753201 | 2024-10-05 01:09:41 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96e8864d-84a8-3b9a-a57f-670d046abd18 | -10.132 | -56.760201 | 2024-10-05 01:09:41 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb3b6d9d-41ca-3593-8745-c69709f44d86 | -9.0547 | -52.952999 | 2024-10-05 01:09:45 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76722bb4-2133-3faf-a92b-4198daea255d | -9.0568 | -52.9618 | 2024-10-05 01:09:45 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68601022-1f5f-34fb-bf65-3d28652a16b3 | -9.0491 | -52.9729 | 2024-10-05 01:09:45 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1225d0-3f17-3244-8071-91a15e2fa0bc | -9.7269 | -56.9753 | 2024-10-05 01:09:49 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42ab0264-e11f-3a01-86d2-40569b2cc227 | -7.7405 | -49.1996 | 2024-10-05 01:09:51 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 97c3310b-58e9-394c-ba28-4ed4dcdc6817 | -7.7443 | -49.215401 | 2024-10-05 01:09:51 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eef08b83-e565-328d-ad90-b45c4717d7c1 | -7.7308 | -49.202 | 2024-10-05 01:09:52 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c4790305-c4f7-32f7-a909-7bf249cf3a1d | -7.7346 | -49.2178 | 2024-10-05 01:09:52 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 64831c1f-d6c7-30d0-b96a-0ea11f687577 | -7.7211 | -49.204399 | 2024-10-05 01:09:52 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 060c4c9f-a504-3ccd-ab2b-ed14fccb8265 | -7.7249 | -49.2202 | 2024-10-05 01:09:52 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 561b5a97-e3e8-3cdc-99a3-7da8407fbdae | -8.8973 | -54.449501 | 2024-10-05 01:09:53 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 534ce196-d0ce-3ec2-a6e5-02951e62b902 | -7.772 | -50.2155 | 2024-10-05 01:09:55 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 483e1e93-98bc-359b-a42a-6f9cb947ce44 | -7.7753 | -50.229 | 2024-10-05 01:09:55 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5d8faa-bd3f-3901-bb76-c7377774c100 | -8.7036 | -54.818001 | 2024-10-05 01:09:57 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9f2254-57e7-3fb7-8675-110055330f78 | -8.5094 | -55.140499 | 2024-10-05 01:10:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a74bfb05-84db-39a0-8b19-f86cba6beb96 | -8.511 | -55.147701 | 2024-10-05 01:10:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41989a48-7be1-3407-a71b-451ed15e596e | -6.1487 | -45.408699 | 2024-10-05 01:10:02 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2378fda-e839-3a6d-92d3-46639c3a4372 | -6.1564 | -45.439301 | 2024-10-05 01:10:02 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 307a478d-e492-3351-b924-f180c61b7c92 | -9.4815 | -60.3783 | 2024-10-05 01:10:05 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76b5c1dd-b7a7-3481-bd7f-9963ba2c5a77 | -9.264 | -60.462601 | 2024-10-05 01:10:09 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab0c0a99-5542-3c95-8040-8a7c309073e8 | -9.2659 | -60.471699 | 2024-10-05 01:10:09 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2348a110-66c6-3c4f-84e5-b012ab3e922f | -9.2678 | -60.480801 | 2024-10-05 01:10:09 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1ad38f-e865-3980-a8cf-f44fc21ad8a8 | -7.9355 | -54.751701 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05031728-4386-36f3-a4ac-bea5268ee8a7 | -7.9372 | -54.759201 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5175bdb9-07d8-3174-b2e5-563ad10a9598 | -7.9026 | -54.743301 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be63f7e6-6a80-3214-b8b1-233101b3bd44 | -7.9044 | -54.7509 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a35c5922-acdd-38cf-ab76-ad205317aea3 | -7.8912 | -54.738098 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8adf7751-835b-3c83-a80b-428f90fd731f | -7.8929 | -54.745602 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 158e6a57-8556-39bb-adb7-be1bbb81113e | -7.8946 | -54.753201 | 2024-10-05 01:10:10 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf116bda-b80e-364d-be69-1921261b44a7 | -9.1679 | -60.492699 | 2024-10-05 01:10:10 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72196274-316c-3222-a486-77c18dbb0f79 | -9.1581 | -60.494801 | 2024-10-05 01:10:10 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 008fbebd-7e82-3634-9988-5d13a336f0cc | -7.8681 | -54.8619 | 2024-10-05 01:10:11 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0de75b84-bd19-3d58-98f4-f8ce2d38afdb | -7.8698 | -54.8694 | 2024-10-05 01:10:11 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4410f992-3f63-3e15-bae7-de793d3ff4e0 | -7.8715 | -54.8769 | 2024-10-05 01:10:11 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e84762b8-c3ee-30d7-a0ff-05e3c55c053a | -7.8732 | -54.8843 | 2024-10-05 01:10:11 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff752de-a87e-3b42-8963-924ecc5e19d8 | -9.1787 | -61.556499 | 2024-10-05 01:10:14 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 422a1fc7-9b79-3fc1-a899-161bf57c434d | -9.1689 | -61.558498 | 2024-10-05 01:10:14 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 552c4d3d-99b8-3db9-8a4d-01f4f0873467 | -9.0785 | -61.373001 | 2024-10-05 01:10:15 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7295e1cb-8bcc-3b2e-9bac-15853cd5d3c6 | -5.3574 | -46.403801 | 2024-10-05 01:10:19 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README21.md)
