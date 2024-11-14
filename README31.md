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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6d2a5bd-7f0b-37b5-80a4-737a39d1c488 | -2.62957 | -46.52719 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39709ca8-c4ca-3fee-b487-f8cdaedf8f71 | -3.62605 | -48.93029 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5960c1c5-5859-3f3f-b2ea-b0afa052306e | -3.49495 | -50.8401 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e64eb70-db24-3a66-a217-c9aae5c4cd38 | -4.2708 | -48.19467 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff34c2c-a984-32f1-94c8-07a62d9a0ff5 | -2.89863 | -51.68457 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c45feca-85e0-31b5-9d1d-02b7cdbbc5b6 | -1.39298 | -51.11678 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccc1de96-150a-3774-a76c-e73e5eb2316f | -4.30087 | -48.0661 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eee0179-1a31-32b5-b0d5-73a507657d8e | -2.87441 | -51.7922 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f64b13d3-ed67-3238-848c-a84fcd3bc2aa | -3.16368 | -48.36126 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad20ccdd-4e69-3ade-97ab-99be8bfde7de | -1.02979 | -48.84671 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d9aceb-3055-3e96-a7fe-6eff884bb160 | -1.56849 | -52.25021 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76fc7686-fb77-3111-9b2e-7e2b9762c875 | -2.3599 | -48.5211 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cced208-cf6a-323b-8864-45413b6b31c9 | -2.09473 | -46.35455 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9973b16-aa29-330f-b3b0-dd8cd4a2cb00 | -2.268 | -50.6702 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b60efe11-ccf4-3692-ae99-3907ee85f950 | -1.38783 | -51.104 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb6647f6-84e9-306b-baa3-a43184039c1c | -3.30152 | -51.59117 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 16a906df-1c18-3bef-a5ca-63978f9a9a61 | -3.11904 | -51.28127 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13f6c58c-30fb-32f9-88ad-39eec631759f | -5.07305 | -45.5119 | 2024-11-14 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba272244-5e00-3cc8-92e6-32c523c2c732 | -1.40314 | -52.38979 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1156b9e-c656-339e-a8b9-5fe6089fd8a8 | -1.4895 | -51.11964 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c2e200-56cb-3d46-9c04-6253d837b87b | -2.3168 | -48.46858 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6c95dd9-e7ec-38de-8bd8-1feadb430083 | -3.05187 | -45.52243 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20c11e7f-c91f-34a6-bc39-16b5b8e175d6 | -3.56908 | -45.14969 | 2024-11-14 04:40:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbbe6eda-c677-366d-a410-9b678c30a0cb | -4.13333 | -46.93905 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f6117c-14ab-3fc1-8a99-6464a06c56ed | -1.61273 | -52.2345 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c9d67b-bcc9-31de-9781-981dd9d263a7 | -2.64777 | -45.79725 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b839045b-c473-3a92-911f-67e9fa746344 | -1.88296 | -52.44408 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55bdf117-43b6-3d18-9adf-fc6dd61bb677 | -3.04761 | -50.33974 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b05ac456-7a14-344b-b924-5838b8b1ecc7 | -2.104 | -48.37181 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 590551c9-8e12-3803-94d5-1707ca3e0160 | -2.81996 | -46.6562 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b16b511-eac8-3cc0-9e23-519c8029fa80 | -4.15131 | -46.24747 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ac32de42-9700-3348-b683-53e3b212c8df | -4.02994 | -44.68276 | 2024-11-14 04:40:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6e9072c-6270-3ff0-aa24-e4e47f6b6f20 | -1.22977 | -51.78402 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1f8ee8d-4ae5-3e80-ac25-33f58c718566 | -2.75182 | -51.62605 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5584214-cf70-3823-8bf8-87c6e77b8921 | -2.64614 | -46.16605 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eba863e-85ec-32d8-9e54-0fee5b7c165c | -4.27901 | -46.90581 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc5bb5b-7010-393a-86c7-fdb3bde86175 | -5.08583 | -45.98417 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f49740c2-b407-3b82-826a-437a1c3a2bb7 | -4.39874 | -49.77488 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b5b4b5a-06cc-3efc-b332-b14ca268e6d0 | -4.48676 | -44.341 | 2024-11-14 04:40:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4fbbb2d-b7ea-37b1-886f-bc00cfce42c4 | -1.21294 | -51.77282 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c783fd86-f827-3efe-aa00-a387fdc7073d | -2.14111 | -47.16736 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63977721-8b38-3ddf-be19-403beb2600ec | -5.19273 | -44.36085 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b630632-1172-34bf-a563-f65a65701004 | -4.58656 | -46.62621 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c53ffde3-6d14-30a2-b570-f19fd04dede2 | -4.73935 | -44.10421 | 2024-11-14 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0c72818-182d-3d70-93cc-0964cb3343a8 | -2.90118 | -46.85588 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cda4a5c8-6ce4-3874-aad4-f3eef1e81944 | -3.0745 | -50.98818 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 951c3bc5-4e35-3303-8cbf-720dd5590fe8 | -1.79928 | -52.16619 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77041e8f-5023-3278-a5ad-2f36117d4e55 | -1.14669 | -48.77388 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e295af0e-97da-3602-b694-a2b6eca652f6 | -2.72909 | -51.74574 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8a8cf62-8509-3b13-9c06-56b61f81e60d | -2.70537 | -51.87125 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e62822d-f71b-3df2-8ebd-e19438904d92 | -2.21614 | -48.37218 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67bced29-4005-38c0-b7e8-5e84063c7dde | -4.11798 | -49.071 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0046a02-2727-3b34-93f3-e847b1ded7a8 | -2.95527 | -48.01634 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4324094-8b5c-323e-922e-a341882528f3 | -4.28591 | -48.22926 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 528c225d-394b-3b26-bb36-0760153ef36b | -5.19778 | -44.3545 | 2024-11-14 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3b0b121-612b-3e0d-ba23-067379307bc8 | -0.95193 | -51.64147 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 339b6ddb-bf53-33da-98a8-e3e27f3e152a | -2.37534 | -48.5305 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55582b12-3549-3d9f-b1b5-aa240fb963fa | -2.96102 | -48.70308 | 2024-11-14 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4e6c5a0-13a6-3931-88f4-0893c452909f | -3.13481 | -48.08652 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d5422e1-bc5a-3147-baed-8f9ffb280fd1 | -3.73946 | -50.44384 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9aa7d7d0-5219-371b-826c-ef16229aa97e | -3.77839 | -51.33101 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86088eda-ab43-3add-95bf-cf7649040686 | -2.27272 | -45.35039 | 2024-11-14 04:40:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8052d3a6-d004-3e28-ad93-46ea4e9675d6 | -3.97293 | -46.70486 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a52cb12-6d92-34e2-8008-c5b31c4a4ea3 | -1.80296 | -52.16674 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1e09b505-3d25-38fa-956b-4f68d1464ed3 | -2.92665 | -48.06895 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7782ba9-dc6d-3275-a398-8b3ccea836e0 | -2.67199 | -46.81772 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33eaa4c6-c1fd-3e9c-83bf-f7b2e9aaa965 | -2.43767 | -48.93759 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaae898f-aa5f-38d8-b89d-b916affab30c | -4.52222 | -46.47574 | 2024-11-14 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2330feb2-5ee9-30f6-85cb-ceb00bd8ce9e | -4.53088 | -48.64502 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9e2cf326-e3f0-30ab-8a02-3b71f54c3c1c | -3.12014 | -45.98104 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daef08b5-2787-3bf6-a9f4-dd4c9b1af57d | -1.40607 | -52.3876 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0df0976-751c-3952-97f1-13d0de4f2aa9 | -1.70802 | -47.90076 | 2024-11-14 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3e128fb-16d1-3205-94df-65836557e717 | -2.11255 | -46.53167 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3497f8d-9146-31fc-afe1-f1bc6818c1c9 | -3.11657 | -45.98051 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13aa9017-312a-3e10-a584-23b560f75db8 | -2.22891 | -48.39877 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 114fe073-94c2-32d4-8d6b-5752b5888c4e | -1.40302 | -52.38251 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5fe0139-f2e1-3e24-b606-5b8d95e328e9 | -4.16554 | -46.24973 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4256a70d-e6c9-3f9a-bab8-82021b3a3ea7 | -4.30265 | -48.09888 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70ec61ae-6bf7-3c75-a05d-0b4892819d3d | -4.3316 | -48.72341 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58b771e7-98dc-39e6-95d6-c58aedd38a2e | -3.03304 | -48.08519 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2c95a17-4043-3ca9-82da-a7643a45ef4e | -3.94658 | -48.99104 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4f9bc1b-6357-3a93-920f-62ede9a5e7ee | -2.24821 | -48.38767 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 751014a2-5899-3a29-9aca-9632aba5dff1 | -3.01766 | -47.96504 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5dc3466-3846-31af-9ebf-ca6d04d0fe1b | -1.6434 | -53.27152 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b459dfe9-aaaf-3c6e-938d-91754fea67b7 | -4.33994 | -45.81699 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 465399dc-3e57-3968-b922-d1e9b3d01a9b | -4.05159 | -47.22128 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3e2d7d7-a716-345a-8ad3-247c20fa724d | -4.3726 | -48.08421 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1a2bf783-455f-3788-9d33-d16d99381e36 | -2.42068 | -46.2647 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05a433c0-29cc-30ac-b926-1fee1dcaf45d | -4.77582 | -45.73152 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed02f991-ba2b-3368-8690-d431e5544a12 | -2.19417 | -48.38287 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba003360-9f37-35fe-96f8-9ca4240a0cd7 | -3.81748 | -51.26326 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 667f9f85-5c57-3d32-a98d-33f3f3528056 | -1.44688 | -47.78566 | 2024-11-14 04:40:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26b58781-b304-3492-8ab7-aa8d32df6524 | -2.63027 | -46.1757 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da52ad70-0638-3ba5-910f-7924ff2df4da | -3.99704 | -46.40469 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4adee53-302f-3ec6-9335-f158a3558ae4 | -2.25942 | -48.31546 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78aecadd-d229-391f-ba46-0f00e8c8fd10 | -4.34456 | -46.54766 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ae76c29-6cd3-30d3-899f-1cee408c49e2 | -3.40333 | -50.30746 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72be9555-8f6d-33e3-b475-3fe45c07440c | -2.43771 | -49.21916 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9a27a3-771a-3cec-b991-06e4a0b394a7 | -3.80846 | -47.79836 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a66f36d0-332e-317e-8b2b-e4c12410b52f | -4.27206 | -48.23068 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README32.md)
