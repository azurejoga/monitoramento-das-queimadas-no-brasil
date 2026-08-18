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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b2058a3-3edb-3f74-b62f-5c8643fdf494 | -8.57243 | -54.72163 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 4819ef2b-0a79-3550-8d91-6aa374e62bd8 | -11.35608 | -46.38171 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92442267-95cf-39b8-8885-7780b06a0610 | -9.9895 | -53.95596 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b5ad6ae-8e4a-3937-ae86-871d5cca3e45 | -7.39159 | -55.48743 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c91c8fe-3054-3c99-8870-86b69c587455 | -7.60995 | -60.8292 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7e7996e-3c8e-3310-86e4-3d90eaca70d5 | -11.19554 | -54.82595 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6213d87a-e8fd-3b28-a111-ef9b947088b5 | -6.75406 | -59.15675 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01103ebc-65db-3c85-a037-d00f7c682f74 | -9.63393 | -49.64485 | 2026-08-18 04:57:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19543b1e-f8e0-35ac-a20b-16efec34d088 | -8.33117 | -46.48623 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b45d37b-e41f-3e4c-aeaf-9f7cb2f2fb28 | -9.13253 | -46.00968 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 729e62f5-5edf-3b24-9962-43a246275ec9 | -11.24726 | -54.82355 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4f68354-d52a-31c3-b1e6-5fb47ca94e0b | -8.56174 | -55.30947 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26c790b4-6126-37f9-b2ac-40c19fda045d | -8.90324 | -60.54954 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 034f10b7-c325-3411-819d-fede78a3536e | -10.54345 | -52.30406 | 2026-08-18 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e15c357-e814-3661-9487-918ea6262521 | -7.38048 | -55.48962 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b2c2158-7b4b-36c1-b065-a679320417c0 | -10.56573 | -51.97606 | 2026-08-18 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 224d0c64-a8cc-3aae-94c2-5e3b3b02cc52 | -9.06854 | -50.8491 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 568ee9ca-54e0-3ce4-a518-eefe13e7bc75 | -8.2148 | -55.02734 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49b61d98-d3d8-3da3-9f85-a6dbf2360704 | -8.36801 | -46.35436 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1166e32c-e845-3f0c-8cf6-016a604b57ca | -7.88335 | -63.7657 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d96746ab-c143-3f7a-a43d-6807de2c7d7c | -11.20336 | -54.81992 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 990b82eb-1c14-3356-ad39-49d8f64d8c31 | -8.58043 | -54.69335 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 744c66b8-88fd-3eea-8aec-65e433f21825 | -13.55856 | -51.69849 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 872645a0-ca7e-3503-822e-9369f760daee | -8.55155 | -47.37911 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8c166da-4fee-39c9-8102-d152b80b751c | -7.13022 | -59.64205 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bd7cfea-393c-3d52-a62f-1f2407140091 | -7.39288 | -55.47966 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd554bab-93e9-311d-95ed-1066d53941f5 | -8.0944 | -61.34954 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2702f205-a1ce-318b-958f-9688e8fb45b2 | -12.1428 | -48.26617 | 2026-08-18 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6c9b59a-8d47-38b8-910f-e51ee6dc9c6a | -10.11962 | -54.29002 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c928909-5c21-3e9c-8c7b-6515110cceee | -6.75697 | -59.16585 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 39119c4e-0994-38f1-8435-f8d2af1508a5 | -12.39716 | -54.96223 | 2026-08-18 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01a9c0fb-3064-3caf-8760-608a5b3cf785 | -10.27453 | -50.41612 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ea8ea34-4340-3441-bcec-3770a90970a8 | -11.20118 | -54.81227 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2c739ce-f012-3c84-9bc5-6a5581f55897 | -11.71653 | -54.63136 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b785b0ed-a7cb-3e0c-941e-223172767f3e | -8.57196 | -54.70304 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f79191b6-19ab-3138-be05-626fc5aa1e2a | -10.26852 | -50.40651 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51555e09-ce1a-36cf-bce2-efe6017d7ff9 | -7.13485 | -47.51046 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbdc80c7-856a-3e1c-9c89-82f00c78c0a4 | -7.78594 | -61.11523 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f139025f-43f9-311c-be9d-025d24844c20 | -11.52114 | -46.63393 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb70bd65-e5f4-3f27-9951-4e367a2de07b | -8.58136 | -54.73056 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d1684240-c8d7-335b-b907-a6c06ba05ab7 | -7.55845 | -55.5701 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 590bdea1-b385-34c1-98ee-fe5c0470a6cc | -11.12259 | -46.49132 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ed855d5-4643-3c68-a08e-7bda2bd27356 | -9.82209 | -47.2802 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57be50de-33f8-3ea2-9452-1189df227569 | -9.54704 | -56.79851 | 2026-08-18 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aedca32f-57de-36af-88fd-c033f1a0c860 | -14.22798 | -45.41043 | 2026-08-18 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 195eeb98-61e0-39fc-b059-5de59fadad3b | -8.89777 | -60.55358 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a50d002c-e3fe-31be-8260-370fd94b55cf | -6.74744 | -59.16551 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c444f2b-0c60-37b8-a761-176b914a58e1 | -9.18098 | -56.99057 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e5523fa-804d-3fb2-8c81-1fea3d26523c | -9.82919 | -55.15667 | 2026-08-18 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c606d23d-9740-3012-b027-c5309d04b00b | -8.64212 | -54.70716 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5949e495-ee87-3a9e-a6b8-5a7397a8a2ea | -6.83347 | -56.4531 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ff8e44a-a9ef-39c3-9e6f-f9881f4eb0b6 | -12.06037 | -58.04546 | 2026-08-18 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05f83841-f69c-319f-b40c-0b1eeae6a915 | -9.46528 | -51.61644 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a3c57d1-a9e6-3734-a2b4-965c0746b720 | -9.54966 | -56.80014 | 2026-08-18 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb5fa4b1-25ee-3b51-a4ae-0062842f4e0c | -9.07382 | -50.83804 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 098f5cb0-4e80-3be4-84e9-3c319b946b53 | -7.17158 | -43.12089 | 2026-08-18 04:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2f984adf-4c38-3d14-868d-bbd15a45ac70 | -8.90258 | -60.57228 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efef5e25-43b6-3e25-b40b-3839f1bb924d | -7.38811 | -55.48686 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bc425e9-f733-3b80-9a89-5eb1049a9cfc | -9.9383 | -53.63697 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e157dde-e7f8-3738-b02e-ac9054d01ffe | -8.59134 | -50.35024 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1fc4b7fb-735b-376e-b8e2-2f5122070b59 | -6.69501 | -58.94973 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f326ab4c-f760-366e-8e16-94b952891db9 | -7.55303 | -61.18037 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 001f9196-d864-3ed6-8939-efe63f5190a0 | -9.42314 | -60.406 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3070681e-c7cd-3d91-a6e9-61b2630e7189 | -7.0188 | -45.90429 | 2026-08-18 04:57:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3e789f3-e2c2-39de-b25a-c648034c7e7b | -6.84588 | -59.01352 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 93128e39-5435-3ac1-92c2-6d42ba5244fd | -11.71709 | -54.62782 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 483fc98d-d585-3e43-9b04-9b402d3acac5 | -9.49087 | -51.67739 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b3250b6-51a4-30a8-8447-b04e30153801 | -8.21167 | -55.02345 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b60d24-9521-3cf3-a4bf-180591211481 | -8.03369 | -55.14751 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5417f908-5e20-3901-adad-5631907b9818 | -11.71321 | -54.63081 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21978e18-aa85-3801-a24b-943ebc45a801 | -8.9489 | -60.58064 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc732fa7-1dc5-37af-8e7f-4b82cefdb4c7 | -9.1602 | -59.66999 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b94dde6d-9f72-30b9-b4b0-dded0c876282 | -8.5342 | -54.89431 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62908f1c-7ce7-35a8-a9c6-f88af105566e | -8.31756 | -46.48451 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4ceb0fa-bea1-3ef9-a93e-b7eb48895557 | -9.07151 | -50.82965 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a74c66-ec01-392c-97fc-4820a5efd06c | -6.82907 | -56.45684 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5021c4de-fc42-3153-b166-ccfc57e04228 | -13.5627 | -51.69497 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27433f01-489d-3de8-9ea7-f14de5d280f3 | -8.04184 | -54.02524 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71d9cf61-6a7b-393a-9698-339232a1b40b | -11.82189 | -56.60589 | 2026-08-18 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166950af-a06c-36c2-abbc-087193139add | -11.38738 | -46.4019 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0d3825-3a48-323f-9608-3ac6c2e73fb1 | -8.21979 | -55.03957 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b14535af-13eb-376f-a53c-93eaf223d116 | -9.16329 | -59.69828 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7c04b84-f980-3c96-887d-945232b05eb7 | -7.55203 | -61.18607 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe76db43-772a-3a0b-8e51-a62efde95054 | -12.71972 | -48.48796 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76212962-5fe0-36d2-a8d1-9464dda1a2b2 | -8.3227 | -46.48068 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94d87d8e-62af-3c4c-b286-67831d01651f | -11.82866 | -55.22124 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e01fa58e-bad4-3144-b62f-45a16147d0ea | -7.38746 | -55.49075 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c416539a-08da-32ad-b723-fe2acb5de666 | -11.19727 | -54.81528 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffbf5401-1873-3eea-a78f-fd849d70df5b | -8.58764 | -54.71303 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 932eb5ac-cb2f-3fe6-867d-7f35eac967fc | -8.95092 | -60.51581 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03b8d4c8-996e-31ca-af1b-f687379846d9 | -8.95034 | -60.54575 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb1ce032-4d08-3467-bb89-98e6a6eba417 | -7.24454 | -49.89051 | 2026-08-18 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35fdd328-79f2-3827-9386-7a5dc1ad5cf7 | -8.58868 | -54.71698 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4b35794-248b-3540-9562-4fbb40c37892 | -9.01048 | -60.50156 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0f952c83-41cf-351f-b047-e597b70e2553 | -6.10913 | -57.73891 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a0a70b4-d2fb-3605-a164-3d3dd511fcb6 | -10.27152 | -50.41132 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 217da125-4f5a-3de2-8b12-88fbd312fa4d | -8.94543 | -60.51986 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf60eae0-5ab1-3cec-aece-6e062764af9d | -8.21881 | -55.02422 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c844c5-caf2-38a6-9b47-fde5f5ad7898 | -9.79905 | -47.31464 | 2026-08-18 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61a779a4-c22e-37b9-8959-9dd226ec122b | -12.47113 | -54.18073 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)
