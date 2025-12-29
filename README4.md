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
| 86250cd7-d6dd-3c67-9fc2-c264de8a1c74 | -9.7258 | -45.09809 | 2025-12-29 04:01:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c1ec6c8-104f-3032-8b4d-adb1cc67530c | -8.53549 | -35.75166 | 2025-12-29 04:01:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea5cb2a6-fbe5-3b02-9861-9f4e0ec4941d | -5.28893 | -45.83068 | 2025-12-29 04:01:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57a955d3-7979-3609-b420-554fe597a992 | -5.98143 | -44.59297 | 2025-12-29 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cfa4f117-7e0b-39f9-a290-d3dbc47aacea | -5.98535 | -44.59365 | 2025-12-29 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3193d3f3-64ff-302b-bdf3-cefc7a97dd68 | -7.36344 | -35.20848 | 2025-12-29 04:01:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce21234c-bb6c-3cfe-a4fd-251c07f3986b | -4.26707 | -40.85967 | 2025-12-29 04:01:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bdbed319-56a1-32ba-8641-1512a9ab1710 | -2.77263 | -42.56853 | 2025-12-29 04:01:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02e230c1-907c-3409-8f19-ee6d2819fd6c | -3.21266 | -43.45929 | 2025-12-29 04:01:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ce0f039d-3732-32df-830a-8d8a052a19f2 | -1.9949 | -47.98444 | 2025-12-29 04:01:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a548772a-0663-31c6-9e2e-65d84da0769a | -5.28462 | -45.83003 | 2025-12-29 04:01:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95d182dc-4c7e-3e92-871a-d4f32a5b9092 | -5.91478 | -38.72798 | 2025-12-29 04:01:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0563138-d9b2-37d5-a30c-63c1b353c082 | -6.51758 | -41.27954 | 2025-12-29 04:01:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6abdc1b5-9210-3af5-9e0a-62b085360930 | -5.33263 | -36.83974 | 2025-12-29 04:01:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 075daabe-3a11-300b-a882-9878bb0ff2ee | -2.45135 | -47.78864 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad1c1d65-4f61-326c-84ef-fc8c4073e5cd | -3.84979 | -41.93629 | 2025-12-29 04:01:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8037ea5f-95e0-3634-8d63-17a777157f7d | -3.34409 | -42.15716 | 2025-12-29 04:01:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 358e7b2d-f5df-3906-bcda-5490c9ea8db4 | -6.93375 | -42.45736 | 2025-12-29 04:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6cdc9c6-07de-329b-9cb1-18bcafc06346 | -3.62853 | -42.21135 | 2025-12-29 04:01:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ab12cdef-e0eb-3019-aad0-bcad01fb6e3a | -7.15346 | -35.08285 | 2025-12-29 04:01:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e17a01f6-fae0-3824-83d5-b7b4bbb208d3 | -3.90551 | -42.5601 | 2025-12-29 04:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 69cbb7dc-4aa7-30d5-829f-68a98670d7c1 | -5.57198 | -45.3674 | 2025-12-29 04:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60321c10-fd35-31fe-9222-540d5781ecfb | -5.57005 | -45.3672 | 2025-12-29 04:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb4fa7fb-b034-302b-bbca-fefce0a3f033 | -3.89833 | -42.55894 | 2025-12-29 04:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a7e254c-b05a-3478-adac-0662f815a935 | -7.47564 | -35.265 | 2025-12-29 04:01:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ae744e04-9f3c-3a40-9ab4-e7c50a6a8a03 | -2.45035 | -47.79488 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26db7328-16f7-35d7-af5e-60aff6d10750 | -2.41339 | -44.90511 | 2025-12-29 04:01:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52fe714c-1aaf-3e40-a4fc-d62f890f7667 | -2.45187 | -47.78545 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9d45cf8-fc2f-394d-9ff0-609f578a8de5 | -1.99438 | -47.98767 | 2025-12-29 04:01:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30bebc69-8cf2-337e-956e-5c08c108ac61 | -8.26829 | -35.27078 | 2025-12-29 04:01:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 031a61c3-78fb-3064-af97-31aa360704d8 | -5.97751 | -44.59232 | 2025-12-29 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e85c9bc-0fbf-3ba6-82f1-89fac914fe50 | -6.00106 | -43.45091 | 2025-12-29 04:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c3088f7-eec6-36d9-acee-1be37040f9a7 | -5.33261 | -37.05494 | 2025-12-29 04:01:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d176b89-6abf-369e-82f5-ad789e6a5a89 | -2.86828 | -45.51051 | 2025-12-29 04:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a01b003-90eb-3ddb-a14b-470a17f16cb5 | -5.33615 | -37.05549 | 2025-12-29 04:01:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c4618d7e-d4d1-319d-91e1-2b9c2b4043f1 | -10.17511 | -39.05202 | 2025-12-29 04:01:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0eb90b86-1182-359b-9a2b-324a226a591c | -5.41671 | -36.88008 | 2025-12-29 04:01:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aff7978c-5aab-394a-be55-e3ebdda3fc3a | -3.21191 | -43.46393 | 2025-12-29 04:01:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fc526255-f7c8-32f8-94fd-520f36673e11 | -2.44673 | -47.78457 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50809357-d5aa-3b11-888b-7f91708c3eaa | -5.53507 | -46.45264 | 2025-12-29 04:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe3c3abd-04f3-369c-a0b0-1a1c719e44d9 | -5.37941 | -36.82159 | 2025-12-29 04:01:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2bd59b0a-cfa3-362f-817e-b019a5024b9d | -5.85781 | -40.34527 | 2025-12-29 04:01:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3dbcd9d0-73d6-3633-ba81-42209cd5b4ff | -3.911 | -40.884 | 2025-12-29 04:01:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1986f4e0-2184-3427-982a-6c6ebbe81b22 | -2.4447 | -47.79705 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 064b26ff-df45-38a5-b739-616a113501cb | -5.28394 | -45.83405 | 2025-12-29 04:01:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01d283a4-a8b0-3fe4-844b-25edda6e612f | -6.00015 | -43.45267 | 2025-12-29 04:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a274be77-95e7-3cc2-84ec-644f1973a683 | -3.85106 | -41.93562 | 2025-12-29 04:01:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 786f7e4c-db4c-336e-953d-a700cd1e3fe9 | -2.4452 | -47.79396 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26ab8daf-0108-339e-b08c-f1d4f4504ec3 | -3.90192 | -42.55952 | 2025-12-29 04:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 710437b7-e5ac-3365-81e8-6de33007a254 | -2.51946 | -45.76907 | 2025-12-29 04:01:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56cb0af7-556e-3860-9474-721ac63cbe3c | -7.40717 | -35.13837 | 2025-12-29 04:01:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 02d9976e-5b8d-36da-b7a2-e77a7380d1e0 | -10.17512 | -39.05259 | 2025-12-29 04:01:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4f4e69f4-fd71-3652-944b-fd558d6c62d3 | -8.79628 | -36.95705 | 2025-12-29 04:01:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7921fa96-ec11-3287-b502-ee2f2342f095 | -4.60032 | -43.33793 | 2025-12-29 04:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9847291f-6cb7-3bd3-8540-51e3a43ff0e7 | -8.27235 | -35.27151 | 2025-12-29 04:01:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e714f13-4c03-369f-86c2-c7a0291415bb | -5.37354 | -46.28891 | 2025-12-29 04:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78cae93f-22d3-3a7d-9af9-55736b4dabe1 | -8.53617 | -35.74695 | 2025-12-29 04:01:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ccbc7821-8d25-34e3-8e05-5dc0f193652e | -3.90484 | -42.56422 | 2025-12-29 04:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 795da6e7-08cd-35ed-b4da-4c1f43345720 | -2.44621 | -47.78775 | 2025-12-29 04:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adde842e-c57e-3598-a320-518fd158dab6 | -5.99719 | -43.44785 | 2025-12-29 04:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80cfc192-b686-3b82-87d1-a2bc9df7f928 | -11.81926 | -42.5989 | 2025-12-29 04:04:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a251644-0b00-364c-9173-4652c7140952 | -16.98166 | -40.70555 | 2025-12-29 04:04:00 | NOAA-20 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c0b36198-1b2d-3dc8-b5aa-9a3490c7c43d | -13.52208 | -43.51209 | 2025-12-29 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcb30dd9-4c8d-300b-819e-74fa4211b64c | -12.6576 | -46.7683 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c42cbed5-54b7-31d7-b343-dd1a0029da0e | -15.95576 | -42.20831 | 2025-12-29 04:04:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 97d5535e-9184-3b33-8f30-97a31cd2e831 | -12.39424 | -42.45027 | 2025-12-29 04:04:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| acf7c258-3487-36f6-a346-88b546909bd9 | -10.77709 | -44.41628 | 2025-12-29 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e8895dc-e933-31b1-a124-b2ea06e50750 | -13.65807 | -43.72962 | 2025-12-29 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62e2d8bc-5bb5-3e27-97c3-54fd76022dfa | -15.96388 | -43.28121 | 2025-12-29 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4670fc49-9e51-34cd-98c8-4f242363b3ba | -11.96206 | -44.20907 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37195806-6221-3cc1-af1a-68155860cd9a | -11.54332 | -46.30541 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de1dc123-75b3-3d93-8e8c-88946c7a12b5 | -11.55194 | -46.30335 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05fb08fc-bd94-38d4-b9ce-ee1696dadb18 | -11.20865 | -41.08858 | 2025-12-29 04:04:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 46ff6ae1-a152-3616-b2a2-d72e8c9af88c | -13.70596 | -45.51666 | 2025-12-29 04:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef3e749d-797f-3004-9b11-faa9c434fad2 | -11.54732 | -46.30615 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e556633a-428c-3fdb-a288-87e4ca81d519 | -15.96329 | -43.28484 | 2025-12-29 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 697577b6-31df-3dbb-b032-ad3246486a76 | -12.66165 | -46.76903 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9792509a-ef93-3a4e-b5b9-0080deda1d25 | -11.55591 | -46.30428 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1abb97c-69b0-30ef-b067-592287dd4f1b | -13.47437 | -44.0113 | 2025-12-29 04:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e8a2fed3-e718-3b0e-a3e0-cf1f59baefd3 | -10.78072 | -44.41692 | 2025-12-29 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd8be87c-a6b0-31c1-9c09-992948bb5e74 | -15.96722 | -43.2818 | 2025-12-29 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2cf31c52-9a8c-33ab-a9f5-aab3c26432ce | -14.50006 | -52.56305 | 2025-12-29 04:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76dd540e-d9f0-330b-8366-0affc4747004 | -11.96138 | -44.21317 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 669a72c6-71bd-3330-9c93-602015d5485b | -10.61273 | -44.87924 | 2025-12-29 04:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff164128-319b-3054-a627-51cd4cfb2271 | -11.54394 | -46.30187 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aae498e-11a1-378d-a738-a984fc1c2c72 | -11.21196 | -41.08912 | 2025-12-29 04:04:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e843473f-3d88-3f4f-b5cd-8eda56fa2ccc | -10.55363 | -44.31873 | 2025-12-29 04:04:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac1a073e-85cf-38ab-a267-61c30564eb6d | -11.5467 | -46.30969 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec4216b1-ec9c-3d4f-9b03-be53e5db24b9 | -13.52548 | -43.51268 | 2025-12-29 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14631746-cd79-3583-9013-0423846fe4d0 | -11.75565 | -44.59513 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff7bf1bf-67f8-3bed-ab22-0bd29d59c9d0 | -15.49127 | -39.00454 | 2025-12-29 04:04:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5bfc5fd-f402-3233-bb23-e393d6f27a0d | -13.82039 | -44.18166 | 2025-12-29 04:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54976e58-29a3-3c5d-987e-c62bf9467095 | -13.65464 | -43.72902 | 2025-12-29 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5e2bd93-6441-3ef1-84d1-739e9d9894a8 | -11.9666 | -44.15952 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7f4476b-bd69-3f06-b650-cdce0dc7e7e4 | -11.5507 | -46.31045 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 464bef45-b17d-3556-ab40-cccde7bd997d | -15.49031 | -39.0013 | 2025-12-29 04:04:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 71bd88a7-bf2a-3c37-8c0d-9c8dec69a2fc | -11.5427 | -46.30896 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19ab4f47-4e40-32b5-b0ff-a3b44d1cad48 | -11.55132 | -46.3069 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef746701-d5f0-3660-8a4b-1d527b6f0142 | -12.47001 | -43.55067 | 2025-12-29 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ece612b-c737-36fb-8b32-7586c1ebbe5c | -11.55008 | -46.31399 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)
