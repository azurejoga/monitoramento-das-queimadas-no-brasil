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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77be82a7-eef7-3aa9-87b2-2dcb9c355af0 | -8.6118 | -48.027 | 2026-07-01 01:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 014606de-c682-3200-912c-8c877efad635 | -7.7156 | -45.9388 | 2026-07-01 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 33a076b5-7ac8-31f8-842f-847ed262f416 | -16.368 | -56.6514 | 2026-07-01 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 583d3d51-e6fa-3c6a-842c-062cf11cc07b | -9.6037 | -56.9276 | 2026-07-01 01:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6eb498ee-1e0d-32ae-90b1-f58903f0e205 | -8.6121 | -48.0051 | 2026-07-01 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ad50f100-4062-3089-b9da-705a51339cd9 | -10.6596 | -54.5372 | 2026-07-01 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8f8d36b5-9f9c-3570-a981-b23b5e4acae1 | -10.7654 | -53.5451 | 2026-07-01 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2f8f19b9-f965-3c6f-b999-f453912e29cf | -10.7843 | -53.5434 | 2026-07-01 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 825fdd34-91c9-3309-ba40-d4d09f79c17a | -10.439 | -49.5789 | 2026-07-01 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 90643efc-555f-32b2-9d65-d062c3c379bc | -16.3485 | -56.6537 | 2026-07-01 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 496a26b9-b62b-32fb-988d-7f7d80cfcd73 | -11.6286 | -59.0169 | 2026-07-01 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7b526c97-6b63-3b72-b6a1-2302fd9ef827 | -12.4094 | -58.4063 | 2026-07-01 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f7465c93-b3a7-3588-9865-da4816e24ef1 | -8.593 | -48.0288 | 2026-07-01 01:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 834f40b2-972f-35fe-9745-2e9942c3127c | -10.6784 | -54.5356 | 2026-07-01 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 21ea3bdd-329d-3262-8ece-65215ab4f3d9 | -11.84504 | -56.94556 | 2026-07-01 01:00:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bd09a1fd-0ac3-3258-b276-c1d671105f7b | -12.41158 | -58.39144 | 2026-07-01 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e468871c-2f43-3283-908f-d510253394cb | -12.42322 | -58.40142 | 2026-07-01 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 03bb1006-8f9f-33de-9085-c5341ceb42f9 | -12.22495 | -56.57378 | 2026-07-01 01:00:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 7f4f6995-bac9-3cda-9998-e6d53523cc5a | -11.43001 | -56.05019 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 280.6 |
| 9f191d48-5a3a-3937-aa63-d59e8ddb1410 | -11.78535 | -57.0002 | 2026-07-01 01:00:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5d4be11b-3182-3a6e-80ba-08bf85a44fe9 | -11.44038 | -56.07812 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 76036124-5d27-3531-8023-8fddbbab1b84 | -11.83392 | -56.94731 | 2026-07-01 01:00:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 535a77c6-12bc-3bb3-91da-e4380170ce26 | -11.43879 | -55.9165 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 9bd62ce4-0cbc-3345-aa3f-e5fac927581a | -12.80422 | -54.85821 | 2026-07-01 01:00:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1f981b28-6941-3504-b0be-66456853ba57 | -11.43493 | -55.92274 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 48320f3f-b321-3200-97d6-a88d1498d980 | -12.42151 | -58.38996 | 2026-07-01 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| c2dced93-6f50-3157-8f47-c94c558a7a16 | -12.22251 | -56.55825 | 2026-07-01 01:00:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 770558ed-c5ac-3e05-a0d9-b3f955ab0806 | -12.79137 | -54.86049 | 2026-07-01 01:00:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 43cdb7b0-2dbd-31b0-a23e-8211b7b17c24 | -11.9013 | -57.38589 | 2026-07-01 01:00:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 694f88b9-7db4-3fcb-af4d-9f2cb944cc67 | -11.4354 | -56.08465 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5a7a918d-5413-365f-bda2-aaa1a06485dd | -11.43271 | -56.06744 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1292.1 |
| f369bbb5-66a0-30b4-bd6f-5bae8520f734 | -12.41331 | -58.40297 | 2026-07-01 01:00:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| eec36cce-7838-3c09-a566-8b881ad96289 | -13.65791 | -60.6269 | 2026-07-01 01:00:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 53a132c8-49de-300d-ae9e-2e3fab7e2c3a | -11.43758 | -56.06102 | 2026-07-01 01:00:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 5dc57e0b-64d0-3be8-924b-9f801af03402 | -12.21114 | -56.56009 | 2026-07-01 01:00:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6db61a02-a2f6-3c05-8c0b-ec84258fe3bf | -10.76739 | -53.54446 | 2026-07-01 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 15eee7b2-1538-3053-a669-3e62bb22e366 | -9.02879 | -59.53604 | 2026-07-01 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8aa7fb07-5828-3027-b724-d11921a1e340 | -10.28184 | -60.53755 | 2026-07-01 01:02:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42fc9d8b-6ad3-3779-87f8-00d6403f6aa7 | -9.69074 | -56.1053 | 2026-07-01 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1301df9f-2d33-3310-add2-79e594955ed8 | -10.85771 | -56.66734 | 2026-07-01 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d77e507e-1bcf-32fb-b351-667d475f331b | -11.63678 | -59.02504 | 2026-07-01 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 7cdc5e04-a3e6-3a2b-8413-13d5b7201794 | -10.67636 | -54.55537 | 2026-07-01 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 8ea3abd7-4879-3853-9e48-cdf6ecc64d90 | -10.07429 | -60.49923 | 2026-07-01 01:02:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c2ec31c-37f4-37ba-90f6-90f5f16d9f9b | -9.68792 | -56.08703 | 2026-07-01 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 612e154e-bf8b-37bb-97b9-a51d046ceb1b | -11.62715 | -59.02656 | 2026-07-01 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 7c36f890-3c65-3554-9c34-85d704e36899 | -11.42345 | -56.08678 | 2026-07-01 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 86fbd5c6-d65a-393f-acdc-0aac14021b00 | -10.68617 | -54.52934 | 2026-07-01 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| d9e57bd4-5343-3a1e-a8ab-d62bba46706b | -10.12631 | -52.09607 | 2026-07-01 01:02:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 2c353cc6-e101-3ba6-b8e5-4a775846f0c8 | -9.5967 | -56.92434 | 2026-07-01 01:02:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e56cbc5c-a7b5-3093-9e0c-6a867189592f | -10.76796 | -53.55098 | 2026-07-01 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 3bb9ec91-c5ab-3915-bf3f-3f741252b2ba | -11.42071 | -56.06939 | 2026-07-01 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 581.1 |
| 2d519732-e4c2-3b51-854d-9aa439ffc01b | -9.69298 | -56.09843 | 2026-07-01 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 003a423a-06c4-3224-840d-2fe0d0349331 | -9.60828 | -56.92244 | 2026-07-01 01:02:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7fbb08fd-f217-314c-b9fd-ba5ba0121ac0 | -11.04764 | -56.92719 | 2026-07-01 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 4e971e25-3546-39b8-b8d9-3d8264381793 | -9.17041 | -58.06612 | 2026-07-01 01:02:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 87ac9fa4-feee-3867-977b-934281487430 | -9.17602 | -58.07305 | 2026-07-01 01:02:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c3aa32f7-154a-3b8d-ac58-7a0de9e088d6 | -7.62442 | -56.74577 | 2026-07-01 01:02:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2fd101c2-cd64-32b7-bc9f-1253c28706a8 | -10.66652 | -54.53822 | 2026-07-01 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 45127e4f-581d-3972-8a07-2ae5378d9520 | -10.11404 | -52.09113 | 2026-07-01 01:02:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 6c1e9f74-37aa-34b2-aa5d-3dcb0b5c7723 | -9.17396 | -58.05966 | 2026-07-01 01:02:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8acdb1be-95c3-3c16-b946-dd1b7bc078f1 | -11.62554 | -59.01582 | 2026-07-01 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fc3362ea-246b-36c8-8791-c9276d6661d2 | -11.62303 | -59.02253 | 2026-07-01 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 273df681-e4e9-3e3e-9534-f7e5e6bf11f3 | -10.85522 | -56.65134 | 2026-07-01 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 2dbe57f1-331b-3e10-9bac-41c0b4a5be04 | -10.67242 | -54.53162 | 2026-07-01 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e9b6e80e-5fe2-32e0-8278-2aaa861f40d4 | -9.61074 | -56.93836 | 2026-07-01 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| cf420102-2761-3300-ba0a-00547f14d15b | -11.62146 | -59.01173 | 2026-07-01 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c4610475-8e7a-3bc2-bff6-4f112e9ec47d | -11.41798 | -56.05207 | 2026-07-01 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 204.3 |
| 01cbe426-7f36-3dea-b4e8-2a0af2f67910 | -9.02507 | -59.53138 | 2026-07-01 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ee6010db-d0ad-3a32-bae5-dfaaeb893014 | -9.02661 | -59.54221 | 2026-07-01 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| acd38443-05c8-3697-b46f-2c39e72ff0b5 | -10.08341 | -60.49788 | 2026-07-01 01:02:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 327e9869-fa23-3e76-acfe-465d0bf62631 | -11.63518 | -59.01432 | 2026-07-01 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2591a0a9-b417-306e-9d53-1553583051f4 | -10.13074 | -52.0882 | 2026-07-01 01:02:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 10ab166b-f397-3e6c-b71a-9e5a0c5e001f | -11.6286 | -59.0169 | 2026-07-01 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 979f5ecc-4ed2-3329-a3c7-2febc4da400f | -5.8058 | -43.7975 | 2026-07-01 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c0143497-9b0a-36b6-ba97-30600145bbd9 | -10.1237 | -52.0905 | 2026-07-01 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 13980e6f-077e-3251-873f-f808fa3214fe | -7.7156 | -45.9388 | 2026-07-01 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 78f02206-5b42-31c3-8d94-ce9816055154 | -12.4096 | -58.3865 | 2026-07-01 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 87232b28-4b19-30b6-9d45-39ff551c0431 | -10.7654 | -53.5451 | 2026-07-01 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1ebc4e99-8efd-388b-aeb9-b870cb356b0e | -12.4094 | -58.4063 | 2026-07-01 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| f7a998dd-807f-3ae8-ba86-75f7c15d7f14 | -9.6037 | -56.9276 | 2026-07-01 01:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 0bb9b44d-2b58-3732-ba07-6326dfde58ab | -8.1251 | -47.8968 | 2026-07-01 01:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| afabfa7e-610d-3f1e-9b40-d6c2135c7f29 | -10.6784 | -54.5356 | 2026-07-01 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6b1ca97e-8583-3360-a4e1-f6acc34f5138 | -10.7843 | -53.5434 | 2026-07-01 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4d426d37-0255-3e0e-ad1c-b79e59f1dfa2 | -3.5043 | -48.039 | 2026-07-01 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f37bd5d3-e1b1-37ba-824f-6ebc94b6784b | -16.368 | -56.6514 | 2026-07-01 01:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| d53fcefd-b808-3d87-9e1f-cf9fc494d4b6 | -12.4285 | -58.385 | 2026-07-01 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e35679e9-5b08-3563-942c-57a3b254bca3 | -8.1254 | -47.8749 | 2026-07-01 01:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 30bd1ebd-e2ea-31e0-bde8-2d015112ca74 | -11.5337 | -47.4571 | 2026-07-01 01:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5bcea93b-1313-30eb-91dc-e7bae0aef157 | -11.5528 | -47.4546 | 2026-07-01 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 7e17d4f3-671a-3d95-9432-c4439ef70f88 | -8.6121 | -48.0051 | 2026-07-01 01:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 7c1fa499-fcde-3bb9-9702-8b23dd2765e3 | -8.5933 | -48.0069 | 2026-07-01 01:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f5997dbf-f39a-3a31-982b-cf98c55970b8 | -9.6852 | -56.091599 | 2026-07-01 01:11:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cca67f8-6451-3be6-9892-969c06f38ab4 | -16.3526 | -56.654301 | 2026-07-01 01:11:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d182d00-37c0-3462-b39c-77de22d851ee | -11.8368 | -56.9347 | 2026-07-01 01:11:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57607f11-2087-30fe-acc0-1f3363c7a14a | -11.4287 | -56.0485 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 996b8bec-5f36-3a7b-8e7e-6b040a5cf432 | -11.6225 | -59.014301 | 2026-07-01 01:11:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b66c8e4-d39d-3c63-a37a-2eba02a63929 | -11.4358 | -55.913399 | 2026-07-01 01:11:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd740904-7ef9-336a-ae32-f3bc71367ffc | -16.365299 | -56.663601 | 2026-07-01 01:11:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86c366d4-543c-388b-8246-970fdbab9ace | -12.4156 | -58.404099 | 2026-07-01 01:11:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ddb2719-2327-36a0-b68e-50d91875bbf5 | -21.092899 | -57.4561 | 2026-07-01 01:11:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
