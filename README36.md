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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dc7ed98-2e7b-36cc-832b-a6895fbfdcbd | -11.118 | -54.0268 | 2026-09-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 40a52001-6c8c-33fe-87a6-8387cb1d53ff | -3.7638 | -51.8076 | 2026-09-26 14:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 28985e5e-f8ea-3c6d-a5a5-0bfd19c5235b | -10.7115 | -60.7312 | 2026-09-26 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f3e95474-2f19-335b-99ba-d6c92bf63e17 | -12.0277 | -49.9583 | 2026-09-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 87605dbe-6119-3ec7-84b1-20aa499716de | 1.2794 | -50.851 | 2026-09-26 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 04ae222a-8cfd-3c04-b604-722ca8248dc7 | -13.5484 | -52.9227 | 2026-09-26 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 857e57de-c237-346a-ab6e-5da38a626114 | -12.9457 | -51.0695 | 2026-09-26 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| bff7db21-8718-3e0e-aab4-ee041f727e01 | -13.4016 | -51.3114 | 2026-09-26 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c18694c0-0716-3158-ae49-d423ec456ddd | -10.7114 | -60.7505 | 2026-09-26 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 72d2ec1c-bf50-306a-a833-0eb365fb256d | -6.2213 | -41.617 | 2026-09-26 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 195.7 |
| cd606557-848d-3eb7-b044-71bd4ea3e939 | -15.9265 | -56.2719 | 2026-09-26 14:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 06d16606-f810-3b4b-bba7-84c6b3da8a78 | -12.6075 | -51.9384 | 2026-09-26 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 361a7367-74ff-36c9-84ad-686c75ab675c | -12.0171 | -50.647 | 2026-09-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| bf55f3f7-19c2-3509-8ff4-2815a007fb0e | -14.7475 | -45.6191 | 2026-09-26 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 91bd1ca9-5b51-38a8-bb0d-8e9eac3b5feb | 1.5651 | -55.8844 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1d5271bc-aeab-38db-b211-684ab200d95f | -13.8154 | -51.834 | 2026-09-26 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 557f7699-48b4-3d29-8893-58634bac87c4 | 1.6382 | -55.982 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1edaba01-870e-3eaf-923c-551c07a1cf4c | -12.723 | -50.6475 | 2026-09-26 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 278.1 |
| 1b242ce6-b53b-32b0-ba4b-0e7217145e96 | -2.9579 | -50.3988 | 2026-09-26 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9592b85f-54cc-3863-8958-5a783cea8d26 | -11.9352 | -49.7752 | 2026-09-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| eba3baf4-6564-3b6b-9886-cdd6e8dcb4d4 | 1.5834 | -55.8645 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0cfc4ec2-57b9-37b0-aa4f-b1b1e812ed5b | -11.2113 | -54.1208 | 2026-09-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7d14d4cc-f860-3217-9e57-e0c065ca6b2f | -12.7226 | -50.669 | 2026-09-26 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 357f70aa-5bd4-34df-ac57-7df01cda2c7e | -12.9461 | -51.0481 | 2026-09-26 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b82fa204-547a-3472-8212-08fc44cb5428 | -6.2024 | -41.6187 | 2026-09-26 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 8ebca9b5-f000-369e-b845-1cf34aa20343 | -6.2587 | -41.6377 | 2026-09-26 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 9d65537b-77ea-3e9b-9fa8-8fb4c5bcc154 | -3.0202 | -44.4163 | 2026-09-26 14:50:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 39240e1c-b8e6-33d9-a694-a12cfd7ca323 | -6.2399 | -41.6394 | 2026-09-26 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| e61c4be9-e5ee-326b-b0af-07ac9dd040fe | 1.6383 | -55.9427 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| cf73aa8e-818c-316d-8ccb-b1a19b831acf | -14.747 | -45.6424 | 2026-09-26 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 860234fd-6c83-3417-8987-c3c9aa74210f | -12.0365 | -50.6233 | 2026-09-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d8c426d7-1467-37f6-80ce-241db6fde087 | -3.0389 | -44.3927 | 2026-09-26 14:50:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ad139b0d-acd5-36d4-95c5-38dbe9d422ac | 1.6017 | -55.9234 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 62214259-a23a-3a39-b10f-0770bd913720 | -11.0991 | -54.0285 | 2026-09-26 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 73759b1f-46c6-3cf9-b7b2-0dd2fdf70775 | -13.2404 | -51.7997 | 2026-09-26 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| fae5591b-80a0-3d85-be84-0299e2c14772 | -12.8059 | -54.0255 | 2026-09-26 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d551db01-5de5-36c9-a333-cad0a608fcea | 2.1083 | -50.8375 | 2026-09-26 14:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 30902476-ee8a-3d77-8df9-199be5edbf2c | 1.6015 | -56.0415 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ebaceb30-7b1a-33ee-9a5e-942fdc77cd6a | -14.748 | -45.5958 | 2026-09-26 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| e3989bab-23ca-3d5f-a248-20ecf848ee03 | 1.6199 | -55.9429 | 2026-09-26 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e2f44fff-d485-3207-9747-443e7536192a | -12.0556 | -50.6211 | 2026-09-26 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| b1a84e6d-d957-32b9-992b-482ea53b3b5b | -10.4234 | -53.8014 | 2026-09-26 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 1434bfb5-2a7f-32a2-8279-00fc6e3335cb | -14.7475 | -45.6191 | 2026-09-26 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 2c0a85af-c1c3-3753-ae72-212c06caae74 | -11.8665 | -50.5362 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 89febb3b-172e-349b-9599-79967d07e8ee | -12.8059 | -54.0255 | 2026-09-26 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 119fb90e-d8d1-30b1-9f12-a8e3bdce9763 | -11.9352 | -49.7752 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 46592dce-b87f-3c9e-8a80-dffc0ceb59b6 | -12.588 | -51.9617 | 2026-09-26 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d8822249-0d41-3fcd-8e9c-3cd46c433597 | -12.9457 | -51.0695 | 2026-09-26 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| e9a17628-f931-3024-b0fa-9cf0633f63ae | -12.6075 | -51.9384 | 2026-09-26 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 3a7d8d20-5a05-31be-8725-6363b97d944b | -13.7142 | -48.8172 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c359b48e-cfb3-399f-b0a5-baa37ab6cff8 | -11.8014 | -49.8129 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 99db5184-fe4f-3b65-9c62-6141a2d5c5db | 1.6565 | -55.9621 | 2026-09-26 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 02e1131a-ddd5-39be-9f49-8b028dbf3ab2 | -12.1027 | -50.0355 | 2026-09-26 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3b67c7d2-ec67-346d-a8bc-d824eab32fda | -13.7146 | -48.7951 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c8736f85-f389-3a2c-ba5a-d27d78cac6d6 | -10.7114 | -60.7505 | 2026-09-26 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 258a8fde-3307-3caf-b768-1c8477a2a708 | -10.7115 | -60.7312 | 2026-09-26 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| cdd79468-ff37-3807-a459-9b5f2aaed137 | -12.6608 | -50.9549 | 2026-09-26 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 94495afb-5b47-3b2f-aa83-41daf152da5a | -2.9579 | -50.3988 | 2026-09-26 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 4822838c-9c42-30ce-a4e7-7762240cf01a | -10.8532 | -54.0916 | 2026-09-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 748cbae5-0ae0-365c-b398-4840cd94f3eb | -3.4193 | -50.4264 | 2026-09-26 15:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1d6945d8-7964-3c80-991d-8b15d5a00610 | 1.2794 | -50.851 | 2026-09-26 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 8326ac8a-e360-3064-a8f7-da934d9d6d0e | 1.2978 | -50.8507 | 2026-09-26 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4cf9edff-d55c-3029-a8b0-8c42cb45c7b5 | 1.6015 | -56.0415 | 2026-09-26 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a76b587e-d0ec-3dfe-ad8a-60be6e566c5a | 1.6383 | -55.9427 | 2026-09-26 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 5c259b9c-8687-3d1c-a1dd-effceda75f2b | 2.1083 | -50.8375 | 2026-09-26 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 3a0a7e53-e79e-35d4-8a13-a5df4ac4d988 | 1.6382 | -55.9624 | 2026-09-26 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a73669a5-8b38-301f-93d9-34840526efd8 | -0.821 | -49.1304 | 2026-09-26 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 41756ce0-7c4d-3081-8731-b8dea175b171 | -12.0365 | -50.6233 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 0f4d6d01-b9e2-34ab-8026-1d20b3aaba8f | -11.1183 | -54.0062 | 2026-09-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d00f789a-512b-3322-b00a-05c857225872 | -15.9265 | -56.2719 | 2026-09-26 15:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 8fea94a8-d59b-3483-b6fc-2d3cd2c1dddd | -11.118 | -54.0268 | 2026-09-26 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 9013cf9c-e3a3-317a-829a-88d8a9e3e8a0 | 1.6015 | -56.0219 | 2026-09-26 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ad30df27-1de1-36ad-a85b-859ab8a8ac1f | -14.7671 | -45.6155 | 2026-09-26 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| b3e5c1b2-42db-3d5f-9aae-a67764347140 | 1.2794 | -50.8718 | 2026-09-26 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 78a6e384-9241-327c-b34e-8441b3f8aa35 | -12.0171 | -50.647 | 2026-09-26 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 17b99afa-e904-3776-937b-5b850132f4c3 | -14.748 | -45.5958 | 2026-09-26 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2952dcde-a638-35c1-8037-4a529de6ca73 | -2.9764 | -50.3773 | 2026-09-26 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9279bf59-a982-3554-87b8-e15dc71a8765 | -12.9461 | -51.0481 | 2026-09-26 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 6de24126-97f0-3cf9-b8d1-366ea259a384 | -15.6574 | -43.527 | 2026-09-26 15:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 132.0 |
| cda81fd9-4e58-33bc-ad56-b228f7da6036 | -13.7146 | -48.7951 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 21694e5c-85d8-3ab9-914e-cc9da06ffe66 | -11.4173 | -51.3948 | 2026-09-26 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1268ef54-2395-3dee-9eae-702c0a8d17c5 | 2.8913 | -60.275 | 2026-09-26 15:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 57b28e70-7496-36bb-a25f-08f22bf8665d | -0.8584 | -48.6606 | 2026-09-26 15:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 43a9da44-ae4c-3f8f-a3d0-3da0e4a0d7ed | -11.7697 | -50.6543 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| dd4874b8-386d-39a0-a74d-472014a76e6a | -12.9461 | -51.0481 | 2026-09-26 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 29dea57b-8dd9-3af8-8407-3348c109d478 | 1.5832 | -56.0221 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b7dab8d1-1d2b-3cac-ab07-254edabb945d | 1.6383 | -55.923 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 54d1f073-9d1a-3d0e-8604-0eea7f5c67a0 | 0.5983 | -50.7946 | 2026-09-26 15:10:00 | GOES-19 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 5c419815-09a0-3359-a23c-bf99b02ce420 | 2.1083 | -50.8375 | 2026-09-26 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 98.9 |
| a7801b66-f6df-3cc8-8ee1-1fec00092654 | -1.0791 | -49.2555 | 2026-09-26 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 80de9d79-2fb3-3f09-aded-6f0b498c9082 | 1.5831 | -56.0614 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a49a74de-bbc7-3281-b07b-9c232c8cc172 | -11.118 | -54.0268 | 2026-09-26 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b1eb8b24-9a07-3cb8-b63a-19deffb822db | -11.9352 | -49.7752 | 2026-09-26 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| d30dbaa1-215e-3384-b5c0-c6e6c6e3a875 | -12.723 | -50.6475 | 2026-09-26 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 9bae495c-d81d-38d0-b9b8-2ede0a7205f9 | -14.748 | -45.5958 | 2026-09-26 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 1fd0a666-0c73-3332-b1fb-f0ff7dd9fb14 | -12.2439 | -50.7699 | 2026-09-26 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4701b6c1-eb8c-3f1b-b3db-bf650e27d1b1 | -12.6075 | -51.9384 | 2026-09-26 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 8add9521-e2e1-39c6-8162-50096366f062 | -10.7115 | -60.7312 | 2026-09-26 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2d8557ae-9613-3840-b421-fdc2b40a81b4 | 1.6383 | -55.9427 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ae445cf4-81b0-3139-8c16-996ecee62f53 | 1.6018 | -55.8643 | 2026-09-26 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |


[Clique aqui para ver as próximas entradas](README37.md)
