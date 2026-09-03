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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0822007-65d7-3722-828c-373acc386ceb | -7.50959 | -60.77589 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71b1d7df-76c3-3495-b6dd-eea63269eae5 | -9.21914 | -59.75939 | 2026-09-03 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5cad675-e4e3-3ace-8f39-1745dc4fd31e | -9.363 | -68.04463 | 2026-09-03 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef2ce407-8ca6-36e8-ae23-836fccac602a | -8.43925 | -54.69939 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf3fd705-7e06-35f0-80ec-1dd023e65c26 | -8.71832 | -70.68511 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 586847fb-a399-3f9e-a19b-0d9bfd1fcd49 | -9.04603 | -65.74343 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffca553f-5956-32b8-81fd-78a9647544fd | -9.03218 | -65.72342 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afb7e2bc-949f-3bff-9f5e-2e1f09155e30 | -8.61375 | -62.55513 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 75da84f2-d05c-345a-9b55-1018379e185c | -9.71324 | -65.00752 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb7eeb2-6147-3b42-9da6-50b873cf72a5 | -7.50509 | -60.77879 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05958a57-b87e-3087-942f-ce06e3bfe865 | -7.1975 | -60.66222 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0636dd1-7e65-347b-9adc-b774cb30c570 | -8.46421 | -54.64999 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1aabfb8a-ab2f-3c23-899b-92cb9cb6480e | -6.9557 | -59.78782 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95dca76c-efd5-359a-9e90-6ab06c2ba9b5 | -7.67262 | -62.5457 | 2026-09-03 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75ab67ab-149c-3fc3-9b1f-cfd9df5dc047 | -8.46968 | -54.65583 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de3702c4-25f1-3ddc-9d20-9e828a72275c | -8.46482 | -54.64522 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| af948a23-6573-346f-80c9-0a93c11d87fd | -9.04549 | -65.74691 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2e52045-65b2-30d9-b9ef-1c1cd8ca87b4 | -8.46721 | -54.67498 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6ff24de0-4b07-3b7a-92f9-8856e1bd7037 | -9.05095 | -65.73351 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af0c3e45-049f-3e4f-aefb-d8305b967578 | -7.53876 | -60.71593 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50c7a3c8-bff3-3365-8481-c985b2b1c2fc | -10.33604 | -68.00005 | 2026-09-03 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48d8c90a-78dc-3bc3-b41d-cd9590dce892 | -7.35876 | -60.60764 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60304157-47f4-3888-84d1-061afe37af27 | -6.94626 | -58.98304 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a1f917f-19d8-3b45-8cfa-e038d31d9a7b | -7.805 | -61.11679 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b8eb2d6-f3ce-3828-84b6-e1dc197d0c8a | -9.02109 | -65.44287 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c572eb3-0c2e-37d8-81b2-effb4f9d601b | -8.43316 | -54.69857 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1e4163d-dcbc-33be-96d1-13bd20986703 | -8.78966 | -71.28456 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d57bbf66-a2a9-3ce4-92b3-2cfab8436c6a | -10.279 | -60.53595 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01f179a2-7d15-3c4f-b8ae-e59cdd1153e9 | -10.30227 | -68.8594 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce680e4f-f17c-3ba5-a844-6a69417b10c3 | -7.20547 | -60.6637 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eaa73a5-2ba9-31c8-8b59-32d94ef6f513 | -8.6101 | -62.55457 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7a6b2907-18ee-3e79-90b7-a6637e3cc899 | -7.53424 | -60.71885 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3979c2f4-55ff-3f28-829e-91b9552f8d4b | -7.69565 | -67.12364 | 2026-09-03 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06e8c9d4-edf9-37bb-b257-0cba3fe183c9 | -7.29365 | -60.71644 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65cbc478-d911-319f-9c0d-1815e6bffcb9 | -8.48027 | -70.6147 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2c5f6b6-2fa6-334a-9e0c-ca4fe67ad248 | -7.50909 | -60.77937 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 799cd8f1-ac2f-398f-ab5e-c8379b5989e7 | -8.62346 | -62.56533 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6cb8b15-87f2-3069-b608-14752a941737 | -7.2526 | -59.52344 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d2b3aa4-edce-38e9-9689-414f5c6e4c35 | -8.45626 | -54.66348 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad5e6ce4-4aa1-3515-aa88-4e40c55ecbe7 | -8.44099 | -54.68575 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6142d5de-8fe8-3ec3-bae8-5e676c72b9e3 | -9.46976 | -66.57848 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43245209-6b9f-38ab-9d5a-36caefff666a | -7.21445 | -60.68639 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add8ee33-6fd6-386d-8fcd-37a4b57002b3 | -9.02772 | -65.44391 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc05bfcb-01c1-35c4-bfdb-f894a5af1d99 | -8.48619 | -70.43614 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65ae5fb6-6a60-3c62-a656-9f6ce185c223 | -7.5707 | -61.21082 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fed4b2a-b38b-305d-9f00-2966fa472ae3 | -8.92024 | -70.58549 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 427f91ad-50bd-385f-839c-2f90c40ff923 | -9.10043 | -65.50179 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 950e37ae-3475-3550-8cfa-bf9fec6ce835 | -7.84941 | -71.75073 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77464905-9b83-3727-a6e8-acc0c45d2155 | -8.42647 | -54.70237 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4272629c-30ef-3cc8-bf29-197dc8d13a6c | -14.14423 | -58.87577 | 2026-09-03 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3c73561-7afd-3a48-bbe1-364b69f36b36 | -14.14407 | -58.87558 | 2026-09-03 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9193d060-e786-38a5-a09b-14980fc447b5 | -9.83209 | -59.47686 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebe5de57-5327-3c9f-9a38-ce186ad17aa4 | -7.21495 | -60.68295 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d70a178-4837-3df6-bf7d-fdf729f5f069 | -8.46176 | -54.66904 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0975057-eb92-3671-87ec-d325e9f6cb39 | -9.0867 | -65.37046 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43347e7f-5d9f-352c-af57-afd01758565f | -9.71708 | -66.3032 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fddff29e-ea3f-3c72-b9df-1ada558fe947 | -9.03833 | -65.74935 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aca4447-c7d8-37a4-a46c-a6e10df45047 | -8.9556 | -69.4258 | 2026-09-03 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d067d19-044a-3b59-8c88-7ec3c452ef7f | -8.99347 | -65.44572 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 266a07ff-1934-3249-9062-8419ace96103 | -7.36786 | -60.60184 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 356a9b59-f17c-39c2-8d2b-9ce944279377 | -9.44507 | -67.42281 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 002dc0a9-093f-3e59-ab0c-61ae1015c8a4 | -8.60948 | -62.55887 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2d904b7e-c141-32f6-9913-15b7fee3c6c9 | -7.53825 | -60.71944 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2ba2c83-052f-35e8-acd4-d5a5478e3c16 | -8.43257 | -54.70317 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91874588-5f87-3b48-9813-ff115b5e5ca3 | -8.68489 | -66.53072 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04234b8b-83b6-32c0-8a37-5cc2c6f6b377 | -9.53106 | -68.56354 | 2026-09-03 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9857a5b9-d59a-3edc-8405-45fa42b61740 | -7.20994 | -60.68924 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50a19a48-5e02-32e6-85ea-4578e43573f1 | -7.56297 | -61.34418 | 2026-09-03 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71ceca37-f7b2-3e4e-8ad8-deeb2f16bec6 | -9.47308 | -66.57901 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84df68a9-58bd-3d61-9167-9009c7cc2dc2 | -8.8524 | -70.63027 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de866280-e0e1-3867-8edc-99f446998437 | -8.45749 | -54.65385 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f6a9f68-8862-3552-8821-729df7b72ef9 | -7.85368 | -71.75144 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d22a94-a28b-33d8-85f9-b5a60411e481 | -9.03664 | -65.7384 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3240dfd0-a6b0-329e-8ad6-82668d5b8e52 | -7.29474 | -60.62332 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e7a42db-2f0f-3232-8880-77e3d2f0dba1 | -7.29816 | -60.71354 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5fb47cf-dd74-33dd-98a1-e2a669d824cc | -8.91417 | -68.80278 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67398711-5dee-30f1-8765-3c516766dd91 | -8.60707 | -62.54971 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d16b24ea-1f30-3365-bd50-8623b999b9e1 | -6.95073 | -58.98371 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb94e3d3-82c5-3024-bf15-1e2414d5070c | -8.46045 | -54.6792 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf154b8f-966a-3f62-9186-0a7a54877eec | -7.54175 | -60.72355 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f763e47b-c19a-33bb-9ff7-99dd2251bb0e | -8.84942 | -70.62247 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fa75d58-c130-3d3a-b936-bdd4e6aa934f | -9.44171 | -67.42226 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23d168e4-519d-32bb-bae8-7e08cd73705d | -9.1032 | -65.50581 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 763552b2-cf04-37b0-9d91-7b0a4710be9d | -8.60645 | -62.55401 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99268e4d-a67b-3e73-a036-2bcbf50fdf8a | -9.70471 | -57.88817 | 2026-09-03 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ed0b1fd-a81c-3431-b83c-8ed53cc2c8a4 | -7.02463 | -62.98848 | 2026-09-03 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 891eb6e2-3ab8-3979-9c80-29dba84e65ed | -8.59297 | -67.17493 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f61d482-369d-3f2e-ad89-e8ce1ba71c08 | -8.45811 | -54.64904 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f130fb41-1ae0-37b1-89e9-a3a222bd78d3 | -9.62228 | -54.31043 | 2026-09-03 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50c7207d-10d0-334f-9c3f-44a93ee3bab6 | -8.06387 | -70.57625 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8366a72f-2b22-3f10-8bf1-de6cf9af1fdc | -9.04049 | -65.73544 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0eef098-9d72-3deb-8832-e36ffc847fd3 | -8.47029 | -54.65107 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3daa278-94d6-3fc3-95ad-d4425d277bf8 | -9.02386 | -65.44688 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e49fdecf-6d4d-3496-8e2b-e02a8d3127dd | -7.36547 | -60.59726 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1cc1c2d-8a35-3c43-8c98-b5de5825078a | -9.0438 | -65.73595 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 407218c5-d84c-32c6-a6af-2286e5ed36a7 | -8.47091 | -54.64627 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0e0bd15-4461-392b-a906-339034445754 | -7.36433 | -60.59779 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 423bf803-04d7-32db-bb32-ab3fd1dea686 | -9.62864 | -54.3111 | 2026-09-03 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891ff76b-a7a7-3af8-8be4-fe72143b8aa3 | -7.28267 | -60.65032 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 540e4230-2a5d-30ca-9318-5e8df42b5a95 | -7.29715 | -60.7205 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README48.md)
