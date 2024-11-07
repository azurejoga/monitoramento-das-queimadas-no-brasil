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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614cf8cc-faf5-3145-8848-8e2dd836e8ed | -4.35057 | -48.62513 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 340fcf51-5fe4-3d90-8dad-64b0cc49896e | -1.39835 | -52.19957 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dca711a-5860-3588-8cff-750627110b8d | -1.14946 | -53.73602 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a219f92c-db5b-3d69-9f7f-10dd294c779c | -1.23199 | -54.5397 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28b9d58d-dbac-3f4a-b7da-ce4b3248dff3 | -4.68605 | -46.38843 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7689f071-e018-3bad-b912-c431107c0f8b | -2.81784 | -52.95284 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ebf6e514-98bc-3b51-8450-4a3917b370a3 | -3.52251 | -50.3445 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b98cf90b-539a-33b2-8acf-733b6e897531 | -3.03386 | -51.09522 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eba47ca-2016-3ef7-8862-564da8e5bec2 | -2.76474 | -53.22452 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cd3e9ac-22c7-37ba-86d7-26faf361d93b | -2.81717 | -52.9572 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8f3bc575-122a-3e1b-8876-0d9acf1b92b7 | -2.81042 | -52.95168 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8810e26-7be2-3cda-b2fd-e189b7605cd8 | -1.46271 | -52.33496 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7304697-ac5c-3113-97a1-39166422e480 | -1.28399 | -54.13519 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3120d697-6f38-35d9-a901-7843e9a9d139 | -1.19418 | -53.51726 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d51cd96a-f9fd-337b-9987-5c0b57df95a4 | -2.15619 | -53.64669 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43205308-8380-316e-8e3f-6af2af0201e5 | -2.80034 | -51.49063 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27df3cd3-7531-3679-ad45-3ad41da10e0c | -2.81588 | -52.91613 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d89b8dbb-59ef-30f9-89f4-0c9847594359 | -0.36467 | -51.42309 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5e4c9ed-f109-31db-8db9-2a264ceb1611 | -3.15106 | -50.20401 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed7c988d-9e22-3bd6-bc7c-5d389e62c8bf | -1.68013 | -55.18069 | 2024-11-07 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5784e3af-8832-3cc2-b710-82f1e5fb5ea6 | -3.20707 | -57.06461 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5194cc4-85ed-3246-835a-fbf8dc38a813 | -2.04758 | -52.08407 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f6354154-01d0-3332-bff6-585a8733b8d1 | -3.01726 | -53.43626 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04dd588b-3827-3ee1-9ed6-cab3bc07ae55 | -3.6419 | -51.79433 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86783074-bce0-367b-8a40-a616ce896bf1 | -3.66715 | -52.34129 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acdabcc8-e272-36b1-9181-30985e6134b8 | -1.42064 | -54.50159 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc7a8ac1-b7b6-30ab-ba5c-ab7d02d54a61 | -1.08324 | -53.64653 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6294617-6bfc-38d5-8d37-042e765a007e | -8.02569 | -49.63683 | 2024-11-07 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed256b91-35e4-30ed-b7b0-5c8684c43306 | -5.37143 | -46.26342 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dcd6a0d-5436-3ea7-bdf1-a8d602dc0545 | -5.98427 | -45.36393 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 173fa45a-c654-3f8b-9bd2-03bf41dbc1f4 | -9.9185 | -48.56577 | 2024-11-07 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b6a34f4-0af7-3dd5-8bc6-be014fac71ce | -5.98996 | -45.37006 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f9fe770d-d0e1-332b-868c-8afb7259109d | -6.5049 | -44.67858 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fcfa8d8-736f-3511-9a92-0bc35faa280e | -10.72927 | -49.52958 | 2024-11-07 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d801e6e3-9271-328d-ade6-a329a539459e | -5.6174 | -45.92926 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 828c3722-2178-31a0-871a-37afd439241d | -5.53577 | -48.70704 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 031d6673-c0c9-35cd-89fc-3f4b15ac2886 | -5.53108 | -48.7031 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6b8023c-5ad9-3adc-8916-691387a713c4 | -10.72886 | -49.53277 | 2024-11-07 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9df0c107-219c-3a7c-9c5e-d1d789b19588 | -10.0315 | -44.74651 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcfa587b-5d7a-3ae5-9af5-2ffcc5b46ece | -9.91777 | -48.57103 | 2024-11-07 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03cb71e7-b3e2-3e2c-a1eb-fa2a4f044d0d | -6.50419 | -44.68417 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6ac6062-a868-393b-81f4-db90ed3cd826 | -5.98485 | -45.37134 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b7438a8a-4233-3a84-aa1c-6bfb98aa07eb | -5.70854 | -45.95222 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4852f07b-d43e-3d75-b16d-2cad8e2d9ae7 | -10.00846 | -48.83928 | 2024-11-07 05:12:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62e194d3-5b6d-3e80-9c5d-f393476a7107 | -5.95988 | -46.30686 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2794f102-8fd9-354d-b7c0-f58c2932c3fb | -10.03304 | -44.73326 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 061147fc-307b-3bcc-9afd-be6051b23f3b | -5.52856 | -48.70173 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d958db9-a841-3f44-9578-130d1e016246 | -6.07932 | -44.72187 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 04f4ad46-b9b6-3307-8bd8-51344aa6d626 | -5.70922 | -45.94742 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72994c8d-935d-37ae-9dfc-a93cc1a48df7 | -10.73287 | -49.82714 | 2024-11-07 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d7169e0-8e80-381a-85f4-49b2769bd608 | -6.49744 | -44.6833 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3c7cf3e-d986-30ab-89ee-9f57935d6272 | -6.54018 | -44.4572 | 2024-11-07 05:12:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 841c7689-c56c-349a-ab2a-46813fc8e161 | -5.5886 | -45.20932 | 2024-11-07 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b985266a-b44a-3499-a1aa-b7e2b51430aa | -6.04262 | -46.60681 | 2024-11-07 05:12:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6305943-088b-3b48-9d52-c7d39731a7c9 | -10.73246 | -49.83022 | 2024-11-07 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f5b13ac-24ee-3650-bfc8-bd7dfd5dccb1 | -4.99238 | -49.89296 | 2024-11-07 05:12:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fdd273e-b5b9-3107-a5a5-d34344ce4911 | -5.59458 | -45.20531 | 2024-11-07 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7057761-032d-30a3-8a11-e9076c418112 | -5.5315 | -48.70001 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6607435f-0569-3e60-8cd5-644293c6d3ec | -6.49068 | -44.68264 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ba05fb8-d9a1-3cf6-95c0-8d6207ac357e | -5.97986 | -45.35955 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e02e0223-0f26-3918-9fe8-50b392e8760b | -5.98577 | -45.35301 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 632ac41e-ef2e-383c-85b3-6e27546eb485 | -8.38296 | -49.63992 | 2024-11-07 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8d89c29-2909-3fae-8889-f884e7f0de77 | -5.59383 | -45.2106 | 2024-11-07 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50cf745e-81e1-3351-885b-9dbb5b5acc50 | -10.01149 | -48.84152 | 2024-11-07 05:12:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34b2e319-34c2-3c41-b373-47bf532fa243 | -7.90705 | -52.42266 | 2024-11-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d81809-5002-35b3-98f6-78b9c9964e5c | -5.97915 | -45.36495 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| da13f6f5-107e-3055-8b99-bcea93f4faae | -5.70829 | -45.95213 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d84cc0e1-26ae-38b5-bf07-8fb4125abf06 | -5.70278 | -45.94631 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66040cdf-b0b0-364a-bf63-2965ff59eddb | -5.70373 | -45.94175 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5382e9f2-01bc-3eac-9eea-f0fd0738f5d4 | -5.70894 | -45.94731 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b72a809-3e3a-3078-8196-a30f7402a5fc | -7.90602 | -46.6931 | 2024-11-07 05:12:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0eeedd8f-a1cf-34f6-b791-69cee66be881 | -10.7354 | -49.82987 | 2024-11-07 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c180f894-799a-3cdb-a2c1-eaa02a89c491 | -10.04008 | -44.73387 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ac38523-c11b-3ae6-a14e-080aeeb00165 | -6.077 | -44.71693 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 242b800b-fce1-3b0a-84e1-908500c4d90f | -6.04631 | -46.60806 | 2024-11-07 05:12:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 93c2fa54-cbed-36da-b350-9410f7016387 | -5.98502 | -45.3585 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 7ba2c9b5-ab78-3381-927d-4b2bc9fd6f1e | -5.98698 | -45.35508 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| b25410c0-36c9-3cf5-8d16-849d4ca91c3a | -5.34185 | -46.19732 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d61aa2ac-cb42-32ab-b5cf-3615588ef1ae | -10.07458 | -50.81564 | 2024-11-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e7e428-9ec7-3546-9161-4cd6dc9870a1 | -5.97787 | -45.36289 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5513374b-c255-34d5-aa58-eb38baf33b42 | -5.98556 | -45.36598 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 562114ba-3733-3bf6-bf90-cd4b614177bb | -7.90542 | -46.69771 | 2024-11-07 05:12:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f51a42f5-3144-3719-9a47-a4ed2ad05f87 | -10.04085 | -44.72721 | 2024-11-07 05:12:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3339db4-750b-3478-9c14-14b7355feeff | -9.91824 | -48.56742 | 2024-11-07 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fd13d33-d98a-3050-9b1d-32feed272922 | -8.02608 | -49.63397 | 2024-11-07 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4121cafa-d84b-3d03-90fe-3c58675110ff | -10.07932 | -50.81635 | 2024-11-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65a3d190-e58f-3544-b8c5-0f9a5bca5ba4 | -6.50842 | -44.68104 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba007e75-adac-370a-853b-b5b921899265 | -5.61674 | -45.93414 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1897c849-3ebf-38bc-85b8-24573bd030cf | -8.38336 | -49.63698 | 2024-11-07 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1924f6af-d5a6-3b70-b05f-52bb6e06ef48 | -8.02646 | -49.63112 | 2024-11-07 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 187e4a75-2402-31d7-9c5b-48ef505c24fc | -10.67985 | -49.45575 | 2024-11-07 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9524c588-1053-3470-bd94-8f35b3caa506 | -6.48995 | -44.68836 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6ad0b05-ce51-34b2-8774-a09394e08a33 | -5.59506 | -45.21017 | 2024-11-07 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 536ab12e-7d97-3c56-a40c-a7ecbd6003ce | -5.53065 | -48.7062 | 2024-11-07 05:12:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e236093-0946-34ed-9874-1a24b3bd78ac | -6.48391 | -44.68195 | 2024-11-07 05:12:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75831cd7-0c25-38c0-b8d2-287c9a043f1d | -5.70307 | -45.94644 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e7521dd-7760-3839-a948-0dc165b44219 | -5.98353 | -45.36928 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 565c7161-5107-3686-b916-7311068bb147 | -5.37806 | -46.2598 | 2024-11-07 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b57f0376-4b4e-3da4-892d-d42b30c88510 | -5.99071 | -45.36464 | 2024-11-07 05:12:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 1f77de4b-af8b-3d3f-bf34-fd14c03691de | -9.91731 | -48.57461 | 2024-11-07 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README52.md)
