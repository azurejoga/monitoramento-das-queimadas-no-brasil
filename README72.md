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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47074aaa-9639-37e8-bc00-598651461eef | -14.95938 | -47.59394 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99a1f8ef-8301-3736-a4bb-db56d9b70eb5 | -14.57547 | -49.1356 | 2025-09-06 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d26650a-954c-38d5-b87f-b484ea9c6b21 | -12.95676 | -54.78689 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff05a7c-9e5b-3148-a646-52994dedf255 | -12.96561 | -54.80259 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03ae9c94-bdc8-3d31-9c3a-38452fee11c6 | -12.48294 | -53.86705 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0357c97-fbf2-3258-b19a-33ffbff4ca86 | -12.99541 | -54.81511 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e06f480c-99a3-36e4-9276-270b8b2a6ebd | -12.96935 | -54.81046 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f40df40e-b8ab-38bf-9173-f8dc0e28d280 | -13.73703 | -46.91068 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bea83f3-c95f-3d8f-8a56-b4576a9e1e24 | -13.79837 | -52.743 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03c043a2-85f7-314c-a644-3598b27d9af9 | -10.4756 | -53.64387 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8d51a1b-18d4-36fd-b550-ebbbb99a3781 | -13.73318 | -46.91033 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7a3bec8-7b86-3cce-a3c7-eff8401fc1d5 | -12.73184 | -52.97456 | 2025-09-06 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a9f8a3f-7f9c-3b25-8796-095dd6190186 | -12.95848 | -54.78496 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3d22b3b-3a48-3348-adcf-a2906417e10b | -14.84402 | -48.18736 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ed3ff99-b889-3021-a4a8-9de89d9a2a11 | -10.13984 | -46.23664 | 2025-09-06 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbf2d22f-5964-3ff1-a1ff-002b1e7c70d9 | -15.72204 | -53.56945 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| feba7466-c03c-3c08-9bf3-9c36743ac4d0 | -17.71208 | -44.49429 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b50752a4-cdd5-34cd-a949-7bd259c1f9f6 | -13.24202 | -51.81353 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c72250f-9d25-3eb3-9030-f646fd95aea6 | -12.95971 | -54.79211 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b6fa80d-3de4-36c8-9dd4-64b37814f458 | -11.5893 | -47.74506 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c835edb6-1c82-326e-9ff6-ba0bb37c7ca2 | -9.69013 | -51.10318 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e8a70e8-12b3-3a10-b9a8-acadd9176f2f | -12.68805 | -44.96572 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73d6c672-8af8-391e-84cc-64a3515bf8af | -9.7425 | -51.05365 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e27bdf4d-e05d-3816-95b7-7f02a5d47ee6 | -11.90684 | -46.64587 | 2025-09-06 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407895a9-85e1-3a39-91ab-9a5ae9326844 | -12.9909 | -54.81897 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1ed09b5-5072-330a-bcf7-09414887c124 | -14.89925 | -49.4524 | 2025-09-06 04:40:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 523a30d6-e4df-3afb-bcd5-18022f0c8c4b | -13.00794 | -54.83146 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 129e008b-cfdd-3eb6-9ea7-c7599114fca6 | -13.00649 | -45.2196 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 721b78a0-e6c9-3779-9ee5-c656dc0a79b1 | -10.0258 | -48.3419 | 2025-09-06 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0936b732-c0aa-3c3c-93fe-ae67bf5c5c0a | -9.9852 | -51.63922 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e178da9b-42ee-37c8-980b-e9e9626b294b | -12.99699 | -54.80604 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67710193-4b56-3d8d-a8fe-baf56fae17c4 | -15.85739 | -52.30761 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab3144e4-a7fe-375b-9f1f-cde67d848e1c | -16.32473 | -52.96309 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6910781d-be3c-3687-a924-bd599dc1c743 | -15.57531 | -52.91044 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 831e7a05-6604-33ac-817b-42b0e9cb4f58 | -11.00581 | -47.15149 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce6dc4d9-fd4e-33b6-afd0-ba473a2f5212 | -13.59217 | -43.35691 | 2025-09-06 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f247f40c-8c45-31b5-9610-fdeb79b78ec5 | -11.32563 | -55.21786 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b329ad43-9c55-3e51-84f2-b9e2a631dc68 | -14.58994 | -48.0899 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e2e9511-846d-3a90-9590-79d3e471cba6 | -13.01088 | -54.83669 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f4dc8b9-0d0d-33ac-aa7a-8e3e9a3e2ecc | -13.92307 | -53.9987 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85b5a794-f064-316f-b1a4-b0fe0a6f4fe5 | -12.79373 | -48.16737 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63bb61f0-eb69-309a-898a-cd8bffd4c453 | -12.99406 | -54.80082 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf9e1a44-14a3-3ced-a06b-49e70ed50e4e | -15.07436 | -48.11594 | 2025-09-06 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cac90ec-95cd-35ef-9fd8-8dbfdeff8ab2 | -11.01552 | -45.93811 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1315d59a-dc46-3c21-bcd0-75094fef0cf4 | -12.96638 | -54.79803 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58f66757-5992-3284-abb4-2b19a4643fe5 | -15.57162 | -52.89087 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43abdbee-a92d-339a-8a49-fee370191c6e | -12.86494 | -47.99908 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06a56283-9e74-3655-9b91-a00ba82abd7a | -11.54578 | -47.31446 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f44082ff-5276-32c2-bdf0-d5c5a40ea418 | -14.5686 | -48.02624 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 867aa1b8-2bfe-3757-a7a4-86243101fd62 | -12.50788 | -53.85 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d4bdddf-5d1d-33f8-81f9-ef7b9c9ce10e | -15.13022 | -52.34726 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 96aadedd-af7a-36a7-bf3a-db45987d49dd | -12.96298 | -54.78114 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2ef8076-9a97-3472-b3dd-bed845b51a4d | -12.91317 | -48.01844 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d8b3da5-04bd-358c-9556-f9feaae5c728 | -10.76224 | -48.2803 | 2025-09-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60cdd349-3b37-3064-ac86-413a4c357c19 | -11.21006 | -55.02564 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbbac677-14b4-3533-8547-32f5780b3eb1 | -15.36274 | -46.41434 | 2025-09-06 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57973bf4-f6d6-300e-a5a3-4f2ee4be9be5 | -11.6272 | -52.22268 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c544f33-1f59-37d0-ab94-219417c4949b | -12.47934 | -53.84509 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b7a596-5452-3cb9-95df-00fb96e1794a | -15.29405 | -46.98751 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da9851e3-acbb-3bdd-8395-59deb9602298 | -11.86411 | -51.44721 | 2025-09-06 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b07ceddf-bf1a-30c2-8e48-17c0f525a147 | -13.88946 | -48.02843 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4797afad-d27d-3b2f-ac02-cc0ac15570bd | -16.33387 | -52.94945 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fac7d006-4b8a-37a5-8468-167935825c33 | -15.70518 | -53.58603 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba28a84a-651d-30c7-af51-4b43968165b8 | -10.227 | -50.5273 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c40aeec-dca6-3d22-b817-2955fb459acd | -14.34304 | -60.32901 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 387aa20d-74c9-3981-b8d9-4fb886cadc1b | -14.17714 | -53.06438 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45777e22-1d14-3e52-8ce5-f2e156f81c61 | -16.31582 | -52.94306 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b0b21ea-1782-37ef-b8cb-76eaf656e650 | -12.19115 | -53.90205 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5696063e-93d3-3a71-a7c5-ddaeb490617a | -10.22085 | -49.72278 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bd727d8-3a9c-337c-9465-3179974b4cee | -13.02209 | -48.063 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cbec587-784c-34bb-8638-348681bfb9c6 | -12.47579 | -53.86582 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45bff6b6-ee6a-3b1a-a235-c1b58293ee5e | -12.51285 | -53.84238 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6b83b1a-7ae5-3e63-8a59-1a3833a09a6d | -12.95583 | -54.81502 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be25ee26-ccd2-3eaa-9938-cfb46cff814e | -12.96266 | -54.79733 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b80256-5f25-3489-9286-9ae89e7f9a8b | -9.74026 | -51.06768 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1fa6445d-3862-37d4-a642-527f88255c3c | -14.58757 | -48.00173 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a887159-45ff-3646-979c-8703acb84ac5 | -12.99913 | -54.8158 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 197c3f51-d5fa-3845-82b8-4e41d0a8aefe | -13.00703 | -45.21566 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2463475-ee20-30e6-b864-0a560fd45db6 | -12.61863 | -56.98499 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 450aa914-634e-324f-95c3-f4548f9a86c3 | -12.96189 | -54.8019 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6da6cc23-5573-3c30-8b44-c127c6bd3e09 | -13.01382 | -54.84193 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d32224b-835b-3d4a-bc8c-0326c8cb636b | -12.95367 | -54.81232 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7d7afbe-1e6a-3054-863a-03d09e6717f9 | -11.013 | -45.92768 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af6ee9ba-8c7d-3801-b2ed-24461ce6c119 | -10.08481 | -48.09159 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c3213e0-c49f-310f-8993-75b4ad886412 | -10.06471 | -48.06052 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 145aca03-b8cd-3453-9f6e-4eca9deea381 | -9.72692 | -51.06562 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82d19a6d-6a18-3a8c-9886-b5907129b908 | -17.23593 | -46.71387 | 2025-09-06 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 794e4dfb-629a-33b5-be0c-b921c6494716 | -12.94321 | -46.56505 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6f9d0dc-99b5-398c-ba81-cc304315008f | -10.60077 | -44.3264 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d719011d-35e6-3cc5-af1e-a7affd78e5ee | -16.29492 | -45.6893 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87eb617e-ad98-3a46-a355-3dc51b69350f | -12.49094 | -48.09175 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7c74932-5bb6-31c4-af45-bed1c264ddae | -14.79845 | -48.11834 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80c19378-8288-3eaa-bc32-2414e8679d83 | -16.60213 | -48.95035 | 2025-09-06 04:40:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daf54406-e1cc-3d08-9b5a-9e8b9152dee9 | -12.51292 | -53.86367 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98c745ca-19f8-34c2-aaf0-63c3bf98e29d | -13.89006 | -48.02431 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddcc231c-a741-3de8-a0d5-b172c661d0df | -12.50928 | -53.84174 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76a8b640-40c7-3def-980f-2e0b10b5cc1c | -17.23998 | -46.71441 | 2025-09-06 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdaebb17-4a18-3999-83a9-a119a7eaa1de | -9.32378 | -55.22015 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0c332f6-e0d9-3813-bfe8-4f4cab7c3578 | -12.96084 | -54.77147 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba153dd4-d7a2-3226-be61-4db6c093374d | -9.21564 | -57.08624 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
