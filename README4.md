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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68608ba0-7cf1-30ab-95a6-3e0d91ce4960 | -12.4498 | -43.3911 | 2026-08-28 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 418e6c82-d344-3370-8cb1-f166b87d83a6 | -11.6583 | -50.4746 | 2026-08-28 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8f56c5dc-d39c-3c5b-9aef-53226d07ac94 | -7.2471 | -45.8685 | 2026-08-28 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 694.1 |
| 411d4a41-10bb-3a33-8faa-81d5be502e11 | -12.5187 | -43.8063 | 2026-08-28 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ed90674d-15c0-32d3-b38f-215372c7c065 | -7.2657 | -45.8893 | 2026-08-28 01:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| be93cc0a-6d96-3e12-9427-b2cdbf46438c | -12.4494 | -43.415 | 2026-08-28 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| dfeaa469-ba75-3133-a136-4dd266c6e2c5 | -7.2474 | -45.846 | 2026-08-28 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 349.0 |
| 273a19b9-5222-3d1e-a195-28fdf29080e0 | -7.2469 | -45.891 | 2026-08-28 01:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 024effa3-8d33-35ee-95e3-0986c785611b | -10.4082 | -61.23 | 2026-08-28 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c9ba1097-0148-3bd8-a049-ed5142a88159 | -4.8397 | -45.3926 | 2026-08-28 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 86b3e549-3bdf-3ac5-814c-79b3ae567784 | -9.621 | -55.1266 | 2026-08-28 01:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c5c32995-c132-3638-83e9-8e970de9813d | -28.66455 | -49.90516 | 2026-08-28 01:00:00 | TERRA_M-M | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 43.8 |
| d0474ad9-fdd1-36a9-ab69-ac2ed3124a8c | -22.08849 | -55.97726 | 2026-08-28 01:02:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c1197e03-4ca5-3bef-b474-c293debe2a29 | -22.0918 | -55.99606 | 2026-08-28 01:02:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8e374669-e5a4-39c7-b9b4-b28b5380b845 | -22.04499 | -56.08119 | 2026-08-28 01:02:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7312d0fd-652a-3d6e-a199-c63094172434 | -22.05217 | -56.08505 | 2026-08-28 01:02:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dd1485c1-5438-38ae-93e0-103c601433d9 | -12.91033 | -59.89441 | 2026-08-28 01:05:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 27d2fb53-5d3e-3e2b-b832-d334bbda7165 | -11.2198 | -54.004 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 740877c0-e4a5-3a43-a8ad-ae3ba69e53c0 | -10.76635 | -54.04119 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 702a860e-7af6-3472-8bce-cb0c6646b40a | -12.22022 | -61.83906 | 2026-08-28 01:05:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2fd75391-8f8f-3e27-8bdb-2b0240365c2e | -11.72351 | -54.56458 | 2026-08-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1dd884d9-59a2-3320-bc45-f19591f13b30 | -11.27892 | -54.03503 | 2026-08-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 36844067-6b91-391d-b7a4-150b727e6325 | -16.15307 | -58.59443 | 2026-08-28 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| c4e76d2e-f8bf-3911-af66-86b0b5780548 | -10.74895 | -54.0443 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| beb4ab78-b98f-301d-a283-a9a02a4e32f5 | -11.72812 | -54.53304 | 2026-08-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 15e7d845-2a53-380d-a1bf-c30f0de955f9 | -11.2358 | -54.0078 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 8d6c7b5b-3c37-3a62-b931-d30938b60497 | -11.23701 | -54.00045 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 32fbb3e8-ca58-319a-9480-d199279a0235 | -16.15549 | -58.60947 | 2026-08-28 01:05:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| ac2939b0-c521-3841-83d5-7616b920cc40 | -11.27738 | -54.0421 | 2026-08-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 100ff7c2-695b-3bff-b5ac-5e41f3aaae8f | -10.74818 | -54.05139 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 435c99a6-54ae-39bf-88e0-0861c7e4b408 | -21.04268 | -57.85199 | 2026-08-28 01:05:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 216657d0-986b-3677-90ce-a79601fb163f | -11.71696 | -54.52815 | 2026-08-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d7ef4942-bce1-3e09-9fd5-ca6095724404 | -21.04569 | -57.84552 | 2026-08-28 01:05:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 424bdb16-a67c-394b-900e-ea3ab5529746 | -11.2186 | -54.01139 | 2026-08-28 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| f17670e9-5699-3e0a-baf7-22b60774bc7b | -21.04035 | -57.8377 | 2026-08-28 01:05:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| a411a3cc-6a26-3955-8c35-29b498c6b65e | -10.18742 | -67.35646 | 2026-08-28 01:07:00 | TERRA_M-M | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f8fe5556-d955-3109-9744-a9bff011707b | -10.38752 | -61.2251 | 2026-08-28 01:07:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 90a3de14-02c9-34eb-b8bd-5269b9823562 | -8.99415 | -65.43993 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f989fdec-b3e2-38a1-8c8e-e35aca2dc66b | -10.3893 | -61.23721 | 2026-08-28 01:07:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 9d0eb2b2-d2cd-306a-8edf-400f1882de59 | -6.00402 | -57.83682 | 2026-08-28 01:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5d121876-b1c3-352d-afa2-aa945caacf3b | -7.46367 | -65.18392 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d21f084d-d23a-39d3-afdc-a0f217b1caf4 | -10.50317 | -64.49578 | 2026-08-28 01:07:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f879e12e-4f71-3501-9702-9a2223c66f74 | -10.5044 | -64.50468 | 2026-08-28 01:07:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| a35163ae-2a5f-3507-aa15-eb90561e0ae9 | -8.6575 | -62.84676 | 2026-08-28 01:07:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7f624d6a-6234-355c-b8a5-bf13e3ff7146 | -7.60769 | -61.34362 | 2026-08-28 01:07:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9394b953-50c8-3335-8e72-1e1ca3127f4c | -9.61658 | -55.14093 | 2026-08-28 01:07:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5cb7d9f7-1dc8-3bea-b81f-5ea7cba4169b | -9.54125 | -66.77837 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a410781c-a92c-3274-831a-b9d14a764941 | -8.98533 | -65.44118 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| fe3c1855-3dda-334e-b73e-1958a481f33e | -8.87829 | -66.90811 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4ca24ab4-4ca1-32ed-b8bf-1bf8d72b588c | -9.62239 | -55.13306 | 2026-08-28 01:07:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f4ea5a16-069f-3f3c-bdcb-e804444a11b3 | -9.27782 | -68.77991 | 2026-08-28 01:07:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e4cd35f7-195e-31b8-898d-3e44be483f0d | -6.76136 | -55.67903 | 2026-08-28 01:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 63f5c08e-519f-3d26-875a-016748280a02 | -10.35224 | -64.45997 | 2026-08-28 01:07:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f179086-2942-3b73-b9ca-e297cfe5cbaf | -8.99536 | -65.44884 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7fd8d430-16e2-3ad8-b42d-ff256cb9ca71 | -6.81325 | -59.45913 | 2026-08-28 01:07:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7e601766-871f-3dd1-974d-c10ef9fa5db3 | -9.00175 | -65.42979 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8f0050ff-d180-30d7-b3d4-c5fc7e48bb83 | -7.58095 | -61.30817 | 2026-08-28 01:07:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 2a07832c-26cb-3cf6-b28c-7a2c3f4ed3e7 | -8.64392 | -66.53464 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 801cda9c-40fb-3fb4-baee-0f6ea80e7362 | -6.52939 | -55.25842 | 2026-08-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7f0554a4-c9e4-37b2-82d4-4497ab09866f | -8.58401 | -54.76442 | 2026-08-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 8c6e234e-8f34-35b7-b62a-424c8391737a | -9.20687 | -65.79651 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 78fcaacd-b1b4-3bc2-85bd-7649195d8360 | -9.00296 | -65.43869 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 39d6c31f-4611-323b-ba4c-a590b739cff5 | -9.53997 | -66.76859 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 09bdc6af-6e54-3abb-b007-a76ba144ce07 | -7.51184 | -61.39018 | 2026-08-28 01:07:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1592334a-86c0-3275-b2bb-f4634ca58ec4 | -6.16002 | -57.77988 | 2026-08-28 01:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6d83b268-85f8-3936-9e96-f6ef235b0004 | -9.16635 | -66.03342 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9c4cff4d-d483-34ef-971e-aacdb8facd91 | -8.87699 | -66.89841 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 30959a88-aa00-341a-9d9d-0d10ec8e3ce1 | -8.59939 | -70.22073 | 2026-08-28 01:07:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 30.2 |
| c150f7fa-6f3a-3432-be1c-424fc9c21e15 | -8.60207 | -70.22608 | 2026-08-28 01:07:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 847581c5-f396-33cb-8763-92686dd91fe5 | -10.50563 | -64.51359 | 2026-08-28 01:07:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 6bdea899-0f75-3776-b3be-13516d883cbf | -6.00108 | -57.84389 | 2026-08-28 01:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 2bfac427-ce55-30ce-ac0f-ceb0995b5563 | -10.39107 | -61.24921 | 2026-08-28 01:07:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 6768dd82-b83d-342e-9fbe-2fe5907ac8e4 | -6.53126 | -55.25114 | 2026-08-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7f210b6b-2580-3850-87e5-8d913ce429ab | -9.84845 | -65.01297 | 2026-08-28 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 098caaeb-5200-34bc-9efb-b431cf2fc8b4 | -7.58288 | -61.32109 | 2026-08-28 01:07:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 319e2a1c-1323-30c6-b5a2-fb129dab961b | -9.61063 | -55.1052 | 2026-08-28 01:07:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 98a7b24b-944e-397b-a324-2702bed7306e | -6.164 | -57.80562 | 2026-08-28 01:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 3d710196-5ad9-3b3e-9288-a229504137ca | -8.63614 | -66.54526 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fc0c6a97-5964-3521-842d-8e33f93b0cca | -9.84967 | -65.02185 | 2026-08-28 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3866d0db-ba9c-3422-b4a4-2b63f6681aea | -9.85847 | -65.0206 | 2026-08-28 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd289d34-1bf6-3826-8073-6245650aa2a9 | -8.59061 | -54.80501 | 2026-08-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 63fdd0e1-363c-3515-bc5a-c33cd07f2448 | -7.58481 | -61.33395 | 2026-08-28 01:07:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 36986f31-785b-35fd-bec4-0298a0d9e8f5 | -6.75601 | -55.71037 | 2026-08-28 01:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| cc58315c-e32d-34c1-91a2-01104b980e4d | -8.5858 | -54.75911 | 2026-08-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 4c817b99-8ef7-3d70-81f0-3a553526ae31 | -6.74987 | -55.67372 | 2026-08-28 01:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 887a8826-e85b-3c19-bc6d-b15c9fb1d00d | -8.63488 | -66.53589 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 40f5b259-5ac1-30eb-b009-6570c854acee | -8.98654 | -65.45008 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98946aae-26a7-327d-bb2d-48ac93bce5fc | -8.60983 | -54.79688 | 2026-08-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9d9d4bce-6263-3957-9d7e-930d3c70af8b | -8.60003 | -70.2104 | 2026-08-28 01:07:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c8643d6e-75df-3729-b68e-a92c72acc266 | -8.59747 | -70.20506 | 2026-08-28 01:07:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 15947f89-b23b-3834-b4db-fec4526ea09f | -8.99293 | -65.43105 | 2026-08-28 01:07:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b87d4211-3299-320b-a2b3-11f6773843c6 | -8.5927 | -54.79982 | 2026-08-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 403.9 |
| 2fa8ac08-7c6e-365a-b80d-320acc0b2ca4 | -3.45901 | -59.52063 | 2026-08-28 01:07:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4277f4da-0ba3-34ee-a484-ab7796e22c5d | 2.02035 | -61.47248 | 2026-08-28 01:09:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f839d577-4730-33ff-9a7d-f922c52558cb | -7.2469 | -45.891 | 2026-08-28 01:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5ac4fae6-7f84-3aa1-99c2-1e26e7dbc2f5 | -10.4981 | -64.5005 | 2026-08-28 01:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1bb44524-d211-32b7-aff1-7d8a46cb9336 | -11.7354 | -54.5431 | 2026-08-28 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ed2a7f82-7515-3f65-9476-f2768a48b3a4 | -8.5783 | -54.7768 | 2026-08-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 5199b3d2-ab5a-3aac-a2b2-7f0154cffac5 | -14.1645 | -52.8269 | 2026-08-28 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| d19a1a20-2984-32aa-af16-4adbcbe4b939 | -7.2474 | -45.846 | 2026-08-28 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 464.0 |


[Clique aqui para ver as próximas entradas](README5.md)
