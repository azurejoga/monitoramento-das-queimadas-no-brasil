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
| b74c5a77-cace-3408-a916-2beca970a6e6 | -16.78133 | -42.56397 | 2025-07-26 03:40:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16a90626-c063-317d-859b-6c7e5ff176df | -17.88991 | -40.45998 | 2025-07-26 03:40:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e5b3a25c-8449-33b7-aa7c-869dc8908dd0 | -15.76191 | -47.7751 | 2025-07-26 03:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c470613-4f42-3449-8a44-0b5e5e81d9df | -15.16573 | -49.58305 | 2025-07-26 03:40:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 099588a6-dc9f-3912-a943-9b7ae375a06b | -17.88872 | -40.46208 | 2025-07-26 03:40:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08e950ff-691d-3936-8f84-8220b9f995b0 | -17.87339 | -39.66147 | 2025-07-26 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f6dc57d-c8ee-337e-b53f-05db6b3d94b2 | -19.01341 | -46.13003 | 2025-07-26 03:40:00 | NOAA-21 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba799e9f-32f4-3f30-ae4e-a1b380a21a8d | -20.64321 | -42.90645 | 2025-07-26 03:40:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| df5f23f2-cbcb-3988-928e-068c589b2296 | -30.12168 | -52.08007 | 2025-07-26 03:45:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 48765170-0a7e-3593-a061-7494bcd6dcdf | -7.2408 | -43.0664 | 2025-07-26 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| e533808c-e7d1-389b-a500-a024e76b6a7a | -18.2442 | -44.7767 | 2025-07-26 04:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6f73ad0d-2abe-3688-91ef-983c79356da6 | -6.70249 | -43.06062 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 775e04fa-2c6a-3670-891f-c41678e10277 | -7.74233 | -40.25122 | 2025-07-26 04:02:00 | NPP-375D | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bcfbb9bb-68f8-335f-b7b6-4cfd3161015c | -6.70609 | -43.06126 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7692ec6-ee5f-3672-af46-0b00d35156ff | -7.24163 | -43.07911 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 01db3f4b-2c21-35da-b46f-a20f2ce25161 | -4.30876 | -48.10151 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0baa5c00-e67f-3acd-bda7-a8c683369514 | -6.11941 | -43.15496 | 2025-07-26 04:02:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4c412f2-7868-3435-9302-a8690503f468 | -7.24123 | -43.07204 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 2f8dfa8d-2050-379e-8e98-d7d57962e851 | -3.58173 | -47.52689 | 2025-07-26 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e3af219-a4a0-3f05-856e-8b1deff9ee56 | -6.21126 | -44.80964 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 959b091f-8109-3045-92cd-19f2c682ada2 | -4.76114 | -38.48372 | 2025-07-26 04:02:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8f350212-072c-3f40-82c6-130120baaf75 | -2.99139 | -49.32158 | 2025-07-26 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b400822c-3993-33bc-b7a6-bdbb6f8d8659 | -6.56147 | -41.49577 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da1e1db6-bb05-3b2e-9ade-d91a2091d083 | -6.47554 | -43.48616 | 2025-07-26 04:02:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34b9e8ad-e75a-3752-9461-200c6778a85b | -7.07948 | -44.0466 | 2025-07-26 04:02:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbe36b52-3af7-319a-8a9b-de3c1d2ab0e5 | -4.06925 | -42.53857 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 52eecdc3-ca6b-384b-81d3-f78c1c984a70 | -4.03567 | -42.51603 | 2025-07-26 04:02:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 766dc1c8-e97a-3c4f-9b96-ef0025959fa2 | -4.96601 | -43.21883 | 2025-07-26 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7c936d9-371f-37f0-8f2f-2bb837be0307 | -3.38722 | -47.48681 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf45bc18-e69d-306c-b582-a3294a3dc85c | -6.5603 | -41.50306 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b840feef-a07b-3d69-95eb-c21480528846 | -6.78316 | -44.10355 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8f419eb-dc0e-33e1-98fc-1cfd8ed7b398 | -4.06333 | -42.52906 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1a17a03-bf2c-35ae-b059-ea63e30cfca5 | -6.23082 | -43.72936 | 2025-07-26 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ebf9265-6482-3750-b44d-d8f5424a9696 | -4.96229 | -43.21822 | 2025-07-26 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72723fc5-c610-3042-8753-2953ee084043 | -6.88666 | -43.11952 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26a79120-e7e3-3ab4-91c3-db6f41fe6d9c | -6.93433 | -42.80296 | 2025-07-26 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 478f40f6-344f-3cb3-a54c-f5cdf8da772f | -3.82574 | -41.55828 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21966209-6dff-3975-ba9e-3a32d589e15d | -5.18538 | -44.9584 | 2025-07-26 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 829328d2-de6c-3f91-afe3-c7f7bfa4261f | -6.88214 | -43.10173 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 826c097e-3956-3349-9268-38b09781843c | -6.55971 | -41.50671 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 794606eb-aef2-3793-af79-810887b519a9 | -6.76647 | -43.69307 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd7a6764-a1bd-3dab-bfd5-ab3bd3d4dee8 | -3.75415 | -49.0532 | 2025-07-26 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64d0e6db-c6e2-30ea-886f-09cc1ba44c87 | -6.33182 | -44.09518 | 2025-07-26 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de453d97-f95d-3500-9c66-cbb59c1341d1 | -7.23896 | -43.06326 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 27d6e2b1-11d9-3827-bda1-f35cea04ac33 | -6.90606 | -44.30202 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e81d6c-8b3e-3de3-94fd-04a581cd6212 | -6.65362 | -43.08408 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21271ca5-a0d8-3721-a723-cb210888ce4a | -3.82265 | -41.57739 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5f244d0-d0a1-3925-b93a-f900990b6438 | -6.42315 | -45.08316 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c27a0231-4086-3717-aa59-d222a9232338 | -3.99458 | -43.22661 | 2025-07-26 04:02:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f80ee811-9e89-3e4b-aa19-91aca0d6ad0e | -6.93014 | -42.80628 | 2025-07-26 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f310b21-a16a-3a27-a74d-a1d5a199e514 | -5.6657 | -51.35772 | 2025-07-26 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a23a7c-70ab-3341-a4fc-15856edc4e9f | -3.39226 | -47.48772 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f00f6431-80d0-3c47-8545-3f1a3e54d1d1 | -6.93238 | -42.81504 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 699ac7ef-593a-3953-a944-5f565b3d44c4 | -6.86438 | -43.68505 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e82306e-01a7-3bdb-afbe-846a90bea3f6 | -2.90552 | -48.25157 | 2025-07-26 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b9c63eaf-535c-372e-8395-44cdefa02282 | -7.03988 | -40.41034 | 2025-07-26 04:02:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8097d07a-c5e0-3e8e-bd83-c86f31b6002b | -3.43136 | -39.04633 | 2025-07-26 04:02:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a95be87d-de22-31e6-a89a-81deea3cf5b4 | -6.87704 | -43.67789 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca8ac29c-ec5e-3e16-8794-84368f839e94 | -7.28473 | -43.08615 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c230c5b-5abe-303d-9e08-5836685c96c9 | -6.56428 | -41.49995 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5922cabf-ee1c-3d81-8885-7522104144d8 | -6.65839 | -43.05487 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d185188e-96d8-3441-bc49-90c71d0946bc | -5.74596 | -43.97506 | 2025-07-26 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ffb2378-4285-31ab-8c25-2fad15bd188b | -7.79138 | -37.60009 | 2025-07-26 04:02:00 | NPP-375D | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7673e889-aae7-3c5d-a7ed-6db690c7f2af | -4.07297 | -42.54206 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 041de79a-7171-3377-a540-3ff55d1bcdc3 | -6.7054 | -43.06541 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc281941-4ee5-3d8b-92f6-00dd9f217d93 | -4.30771 | -48.10778 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4973c26b-8d44-3691-9e76-996945b0a048 | -6.86737 | -43.69011 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa943cb8-5f0c-3855-9fd6-c64c02424fe0 | -7.50228 | -37.36787 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 929d9648-9ff4-3a88-8f70-8042da01c079 | -4.06496 | -42.54218 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4c7fde21-2b02-36c7-b22a-d9f10b0012a7 | -7.24453 | -43.08382 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 052e8638-9943-3f6d-bb18-fb83f619afff | -3.05303 | -47.38124 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a13f6bc-e2d5-3cf7-8333-58e99f9030dd | -2.9109 | -48.25243 | 2025-07-26 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4a7aad9d-0788-3c5a-9559-e0b2f2ca5a61 | -7.23582 | -43.06971 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 26226e52-53de-34b3-8e05-65ab2e16748a | -6.5631 | -41.50725 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 65529144-091a-3cee-9732-51361beb7486 | -3.38621 | -47.49274 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9c2a1db3-01b2-3dff-a256-b42dc33f99a6 | -5.99039 | -45.73217 | 2025-07-26 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dabebbd-89b4-3e03-a16a-7580af810296 | -6.56088 | -41.49941 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02c32c8f-4169-3583-90d2-e5e20c25b10f | -6.41748 | -41.15137 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fedfeb0a-f09d-32f9-ab01-d98d3133d055 | -6.15799 | -42.60088 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d1dcf83e-82a7-323c-92cf-87493ca126ed | -4.32343 | -48.39175 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1db83d1c-3b13-3faf-ae49-5ecd451fde8e | -6.87405 | -43.67284 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 837c71ad-4924-3004-b296-4ba0a9f4ac53 | -7.05142 | -43.7943 | 2025-07-26 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ae96aa1-de41-3630-8c0c-ac3a95a18b03 | -6.87331 | -43.67731 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f98b5def-3c92-3152-a963-ee475d56ddfb | -6.0703 | -43.64974 | 2025-07-26 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11cdfa69-029e-3593-901e-17f76e170d39 | -6.70105 | -43.06623 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a9ccf6d-83d1-3767-92bd-96d15debd642 | -4.0393 | -42.51662 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| df625678-ff93-3cea-abb8-72072a4cd6ee | -5.47451 | -41.78195 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2354a498-6c8b-3e2e-ae3d-7605950bb8e8 | -7.09722 | -44.38301 | 2025-07-26 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17fd3045-45d6-31c9-9658-dc8e703437f2 | -3.99081 | -43.22603 | 2025-07-26 04:02:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 768b4ffd-069a-329c-8b1a-65e0757947b2 | -4.61707 | -43.32006 | 2025-07-26 04:02:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8831b96-645b-31dd-989e-d9989bbcc6a2 | -5.98609 | -45.73151 | 2025-07-26 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edc98b95-9397-3ced-88c4-511761f5f663 | -6.90685 | -44.29721 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abcab153-bc7e-3d94-8d57-f93ebeaef652 | -7.24189 | -43.06795 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7892e543-b323-3b73-9be0-2d2bd922759c | -4.06859 | -42.54276 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 462a1774-0e78-396d-8c29-353d71b437f3 | -6.52485 | -44.5957 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a834655f-2800-3704-8efc-544b20c8b4be | -6.15154 | -42.59574 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d80d628a-06d4-3937-b36d-f6752548987a | -3.39176 | -47.49065 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 808d3390-5d8d-38ec-b38e-d71046fccfad | -6.52878 | -44.59651 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae25c1e5-661c-37fe-b4a0-09ff0bd87472 | -7.23764 | -43.07145 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 49f91efb-5571-3126-9655-a73b70e26ac7 | -6.72215 | -37.12498 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
