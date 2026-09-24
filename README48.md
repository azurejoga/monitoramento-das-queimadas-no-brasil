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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1342380-5707-3bd7-8dd7-93dd465e8d90 | -3.41902 | -54.00919 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54daf752-dfa4-3324-b7e0-8c3d53e33152 | -2.92103 | -48.10577 | 2026-09-24 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2a4569-5786-3f01-93c0-0f9e1e8cf0e2 | -6.04217 | -53.27225 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 581c7cd7-4f50-3627-a317-e9faf9ff26bf | -5.1114 | -43.74313 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fde11ee-dd60-3d24-966d-dc2ea48062d0 | -6.04281 | -53.26848 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e93392d7-7d25-3a99-bf1a-2dd970883e37 | -7.02996 | -44.6542 | 2026-09-24 04:44:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c60bee0-b50a-370b-bb67-cac032411999 | -5.79017 | -49.18574 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 841f44e1-fb9b-3817-bad9-fe89673d88a8 | -6.78667 | -48.68296 | 2026-09-24 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 78521f61-fe8f-36de-9c9c-150935a7015a | -4.75771 | -42.73572 | 2026-09-24 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96bb14c6-07fa-3f8e-9897-c7dfc2ed530a | -2.8819 | -54.08684 | 2026-09-24 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66deaadd-11cf-3750-85b8-b3d6dc6e98fc | -4.05921 | -49.0701 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7f1fc6e-af57-3630-a682-bf8809589cbe | -6.61781 | -47.63774 | 2026-09-24 04:44:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e236c94-cc53-300d-846c-e45d167f25e4 | -7.67575 | -45.48315 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6732b4f9-88ca-3437-8bd5-12a5340738a9 | -2.89584 | -54.08912 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d25fbf9-b29c-345f-b7fa-bb7c386612b9 | -3.21366 | -53.40886 | 2026-09-24 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7343b455-c6b1-37dc-b265-5c374a371509 | -6.51608 | -52.82768 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a46f194e-e6f2-3411-92d7-5613feeabc17 | -7.00128 | -48.63057 | 2026-09-24 04:44:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 027766a4-4aae-317c-87c1-a4f37d3ca493 | -4.66216 | -54.47412 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8146b2ea-cf6f-3a06-b794-874a901075b5 | -1.82261 | -55.33687 | 2026-09-24 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c862487b-b0a0-3477-ba51-2739c14faf95 | -7.403 | -44.76918 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95fdcc43-78c3-3f74-8bbd-4789a46c2652 | -2.56083 | -54.7298 | 2026-09-24 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb08e208-ea96-3f13-bd2d-3e0230f0e91d | 1.5054 | -56.01599 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f501fa1a-514a-39f7-b6a2-2fa26bab9622 | -6.2707 | -43.26869 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d8e0ee2-677b-3def-9572-46fd10e5c64f | -2.64462 | -54.68995 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 4e599c17-d63b-34d7-a79b-e2a9aa5feb14 | -5.57485 | -42.30384 | 2026-09-24 04:44:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3099d4a2-20a9-33a1-b653-59448414c8bf | -5.81589 | -47.76733 | 2026-09-24 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da15f0f1-a530-384a-a4fd-6623f4b9edff | -7.19221 | -47.47107 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4856e952-0bcd-336e-9272-844b1ac5b8f7 | -2.92529 | -48.73989 | 2026-09-24 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 544c9033-dbab-303a-b611-0bfcbd4fc165 | -3.18325 | -48.02442 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b6bccef-45f3-3e23-a8fb-74e07177e4fc | -1.02694 | -53.73459 | 2026-09-24 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e837b91-7395-3494-81a0-15cf2deaef5e | -5.83676 | -53.84782 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ace40b8-12e0-3624-8b97-8fab14430c85 | -0.50803 | -49.15088 | 2026-09-24 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea590e02-4517-399a-ab1c-8877d57fdbdd | -6.6717 | -50.947 | 2026-09-24 04:44:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7a7a4b8-ddd9-394d-9719-14f9d925df88 | -6.60145 | -51.68217 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a97eb9cc-44dc-31d2-8556-9da178d94c97 | -3.15815 | -54.60496 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9c0a5fc1-0a82-358d-82bc-3539dc2376d8 | -5.77658 | -45.0971 | 2026-09-24 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e318df14-4193-3773-9ae0-eb32432aff9e | -3.97004 | -47.20494 | 2026-09-24 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b126faa5-c956-3f39-866d-72e78885184a | -7.3887 | -44.81449 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60383982-0629-32c9-94c1-9c767694e22b | -10.42186 | -49.36716 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c0dd6f-e13c-3c71-8151-e375410a5602 | -7.31058 | -50.06232 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b36687d-1183-3696-ac6a-61486f9cdacd | -6.63435 | -59.93223 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01da1358-5c08-3be5-ae44-949b8538898a | -11.43036 | -47.40441 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60739be7-6bcc-3002-b157-1c489d7d2c7b | -8.08602 | -54.76673 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93f5e545-47c9-304b-91bc-59300e8d9822 | -11.47941 | -47.33512 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f03f4932-c122-3fa2-b3d9-b422eb1940a3 | -14.62265 | -50.6027 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0431e3d5-518e-3217-917d-9f08608e4556 | -8.73077 | -47.60474 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7043c467-8906-3a62-a589-8fbd46505368 | -10.11733 | -50.20579 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2263ab15-d705-328c-9078-79fea65e7757 | -15.24709 | -43.2653 | 2026-09-24 04:46:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1774ce55-25cf-3850-a4d4-197da4969380 | -12.02123 | -47.80288 | 2026-09-24 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6efda51-1e82-35ce-ba17-48f810aadcff | -8.27475 | -54.76411 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 985490a3-01e7-3252-b7b7-e42079b5690c | -6.67625 | -58.58139 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d824062-6a04-3528-9ed1-d0a84466d4cd | -11.59226 | -58.51191 | 2026-09-24 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae23be34-a08f-3604-bf81-2306fe665b9b | -12.42015 | -46.9511 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6b7effd-45d3-3faf-9e98-ce055608e54e | -7.4266 | -49.86612 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 459c5fce-f025-33df-a722-c6116535c162 | -10.14421 | -45.54138 | 2026-09-24 04:46:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6945cf1-a881-3dca-904c-d2bf9526f5b1 | -12.28744 | -46.39441 | 2026-09-24 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9008cb4d-e1b2-3f83-a9e5-de82bbf7adfd | -8.29719 | -50.84702 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15eed232-6a1f-3fb0-a265-44af002c1e92 | -6.10306 | -59.8853 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4dc4803-4e3f-3b89-ba51-d85c12e972f8 | -6.34992 | -57.77314 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 744a40d2-85c1-36f0-bc3f-a7966da2868e | -11.40541 | -47.36216 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12561327-1e7d-3ac8-a14f-ab45ca8da992 | -6.23607 | -60.03122 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82300c2c-c7af-3bd1-a360-e43756e1e4d5 | -11.79364 | -50.0387 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5a14398-eba3-3e43-af64-df90bce55520 | -12.01114 | -50.31495 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10779e43-abbd-351c-a0a9-cc4148dec2ee | -11.35173 | -43.36974 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3c8b726-2ff5-34b9-97f0-663a1d172a44 | -7.88176 | -61.1757 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b3f6f1a-a1b1-301c-97bd-d5fcfd58988b | -10.61563 | -54.0056 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c65ca3f9-e4a9-33c5-a9e5-ff07339c815c | -10.89317 | -51.52097 | 2026-09-24 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01247dfc-1a25-3a59-96ff-99f98fb30e81 | -7.89534 | -61.17794 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d721ad83-1c3d-37a2-9b6e-ea796843df73 | -12.15281 | -50.7491 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c5b26d1-bf6e-3873-8139-5e52340de26d | -10.65971 | -42.61676 | 2026-09-24 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f29bea03-b020-3cc7-8a27-1c563039fe14 | -6.87991 | -55.56091 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a732da5-48cc-3e49-a848-e3d06e6de05c | -10.62227 | -53.98877 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39af430d-e251-31c1-a710-c6cfdbed14ed | -11.96241 | -50.75932 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7afcfd40-a2b1-3309-8275-341880c819ac | -10.43094 | -46.25771 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 671ddce8-3acf-3e23-9965-38287f5c9454 | -8.90279 | -46.81462 | 2026-09-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5fcd6fb-1674-37d9-9e88-bae44c7f8c9c | -11.42355 | -47.40336 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a9dcf56f-eaff-3518-9a8f-8dd147af85ac | -10.13991 | -50.21708 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20dac4cf-1b7a-3246-baf6-bb3d00dab92b | -10.41233 | -49.35085 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 75749184-7a76-3662-825c-4d559f7880da | -10.08778 | -46.00007 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2aeb3623-31e4-300a-b21a-e0d8c6963c19 | -10.10894 | -50.19308 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0b60dfd-22fc-38a3-a71a-971f1e7066e1 | -10.61156 | -54.00488 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e55b8e54-a9d1-315e-a9c4-a1cd0ec8d544 | -6.44359 | -59.95488 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 37e036b5-991d-3775-9503-0f4cc6e90ae9 | -10.07952 | -46.00693 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f485f640-8338-36fe-9357-599c73c6810e | -12.38237 | -46.96511 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c8867e-8c8d-338b-8ef3-30a3e15b3591 | -8.75338 | -45.88067 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2168ca89-8075-3988-8e36-dbbe0a740ec9 | -12.41622 | -46.96154 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3e48a269-57e4-3d58-acd1-f7c2ff086b5a | -8.27323 | -54.77281 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 807cf6a6-2e0b-3b94-aba9-340ac4227ad3 | -8.4577 | -51.48221 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4408f12-f5af-3bcc-85ec-070662a45238 | -9.96534 | -50.26044 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 355ea8ba-c294-32ed-9dfc-01e84bedcf9e | -11.39344 | -47.37207 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c45a893b-1caf-3042-97c1-4b2459e4c01c | -6.8838 | -55.56691 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41536de7-d97e-30af-a73a-5693bc4bb285 | -11.51086 | -51.49884 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 446f2f52-28eb-3a35-9dae-366422d4cd22 | -8.82129 | -45.93009 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3b6ffce-a2c7-3c0f-b6ea-0b490fd9b792 | -9.15121 | -49.96237 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db64cf34-547b-35ed-bd13-ab13fa431c1b | -10.97474 | -54.09254 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ff3aa21-c771-34ad-918a-7f40fb1ba056 | -10.08007 | -46.05212 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 95a9ebe0-bc3c-3f9a-82d4-77f6494aec63 | -10.08032 | -46.00842 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| d37586f6-b613-3310-81b3-dcf4e561ff35 | -11.13079 | -48.3111 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0262ec27-7ab3-3df6-88a0-12c8b8d08a5e | -11.98304 | -44.94518 | 2026-09-24 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97097852-65e3-3dc7-bfd7-6eb5f92919ad | -5.59225 | -60.20535 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README49.md)
