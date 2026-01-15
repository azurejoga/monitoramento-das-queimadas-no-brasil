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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d72fbd3-4933-3040-9d77-bff37137240f | -7.23818 | -43.05818 | 2026-01-15 03:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4e2eda02-7d93-3f26-bac8-3fe04cd3ecc2 | -4.36333 | -37.90343 | 2026-01-15 03:21:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 38e20287-82ed-36ef-ade4-0a056716b40b | -7.22407 | -39.95354 | 2026-01-15 03:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5311a6c8-7449-3769-af65-68d3ba1ce589 | -12.50263 | -43.67956 | 2026-01-15 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f134943-f341-3bea-9fe1-450a9a27e933 | -10.20941 | -36.23156 | 2026-01-15 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 50b1a4f8-7525-378b-b5a0-7bb3d7381eb2 | -10.21304 | -36.23675 | 2026-01-15 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a677b069-2df2-34ad-8494-2fb100a040b3 | -12.51481 | -43.6888 | 2026-01-15 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a02f256-a261-369f-b863-dea9375869c3 | -10.21381 | -36.23241 | 2026-01-15 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1b7dbec7-b962-3ed6-a635-0d91bc1e5bf8 | -10.67293 | -39.19219 | 2026-01-15 03:23:00 | NPP-375D | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f62e96af-da3a-313b-88e4-072933efb31f | -12.50938 | -43.68108 | 2026-01-15 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ea6c4b1-6a88-3912-a898-1851d597c4d8 | -10.20864 | -36.23591 | 2026-01-15 03:23:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 560b7936-1d5d-3499-8ad2-d6a1965e9dcd | -14.406 | -44.58514 | 2026-01-15 03:25:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f80499c7-d3db-3d87-ac0d-ad1ba839578b | -27.78017 | -50.52412 | 2026-01-15 03:27:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 14a2b49a-3058-3603-8cdb-b2fc6ccf0dcc | -27.77796 | -50.53178 | 2026-01-15 03:27:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 48bc31f5-9d54-3c49-8c58-611445c1ab9d | -4.3718 | -37.9175 | 2026-01-15 03:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 7436a4dc-9564-37ee-8efe-76cc0f0d42a3 | -4.372 | -37.8918 | 2026-01-15 03:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 96.8 |
| fd3fed45-a715-334c-9f81-cbef42773267 | -2.98787 | -39.9672 | 2026-01-15 03:42:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df75c56c-4cb2-3d86-b9dc-4e6d901e8517 | -4.37163 | -37.90708 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb51ba8d-a059-3ae1-b022-0717ba4c537f | -4.12591 | -38.204 | 2026-01-15 03:42:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 331bf854-a7a6-3c5c-b801-31e4ed38c7a8 | -4.36935 | -37.89827 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e52463d0-9d4a-325d-b82f-83db58d2de61 | -5.02046 | -37.54072 | 2026-01-15 03:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a94b8612-4533-31a7-b975-a7540a1e0105 | -3.2301 | -41.80449 | 2026-01-15 03:42:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 689c0ba9-0a96-3cf2-9936-8d7753be1e72 | -2.98848 | -39.96349 | 2026-01-15 03:42:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 340fc374-7556-3f47-9af8-e1d0a36c4062 | -4.37014 | -37.90517 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7dda7d7-3c1d-315e-bcfe-8bb11b45bfb6 | -3.81078 | -38.6581 | 2026-01-15 03:42:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7db891ab-71db-359f-8516-b631a9bcb4bb | -4.36804 | -37.90649 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2321c720-5795-3949-a99a-be11150fdec5 | -4.37081 | -37.90107 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0a7748b-ffbb-3b0f-b5bd-6f915b318dcb | -4.37228 | -37.90296 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51df26b1-c0b9-3608-9716-3bf2b7c8f2a8 | -5.07494 | -37.29226 | 2026-01-15 03:42:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e715a261-f7c9-38c2-954d-25cec214da2d | -5.446 | -35.61108 | 2026-01-15 03:42:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a57e212-f638-3cc5-944f-c1cdab305da9 | -5.01632 | -37.54406 | 2026-01-15 03:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6da590f1-bb4f-3f59-b4e2-431ebda5dbfe | -4.36738 | -37.91061 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aab378f4-681a-3f09-ae5b-23eb81ed51b1 | -5.44931 | -35.61161 | 2026-01-15 03:42:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d4ffbd52-a676-3b90-9595-9e47f3ca0d14 | -3.28457 | -39.26134 | 2026-01-15 03:42:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c8e952e-e326-338e-ab2f-b51c7f9bc7cd | -2.74864 | -44.64309 | 2026-01-15 03:42:00 | NOAA-20 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22629440-60bd-3c5f-b2a5-186b459dd2b9 | -4.36576 | -37.8977 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7cc0b54-1e99-3d93-b442-93e85db78f07 | -5.01695 | -37.54015 | 2026-01-15 03:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 59dca45a-b053-3002-a034-d1a82c90f314 | -4.37149 | -37.89696 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 506518bd-5b06-3d0e-a107-20d3859be083 | -3.23946 | -41.80595 | 2026-01-15 03:42:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e1d4b225-df30-334e-917e-12f06460a7b2 | -4.37359 | -37.89474 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1246ede3-dd5e-3583-81d7-b4e31f6c816b | -4.37522 | -37.90766 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a7b4063-5c78-3325-9c7b-dd0255f1504d | -3.28368 | -39.26369 | 2026-01-15 03:42:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b4dd9f2-3bbc-3c40-a4ce-4118e5b15e65 | -4.37097 | -37.9112 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0cf84796-e508-3290-8d7b-283a6e9979f7 | -3.23478 | -41.80523 | 2026-01-15 03:42:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e1c578af-9384-392f-bc89-c371badcfb68 | -5.45866 | -35.55272 | 2026-01-15 03:42:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8cb7b83-9765-384f-8d72-bb4ca3111a10 | -4.3651 | -37.90181 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57e94862-a868-33f1-919b-80b9a066193e | -4.37 | -37.89417 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e06a3b84-9bd6-3119-87a6-6e437ed1a799 | -4.37508 | -37.89754 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fcbe871-c194-35ea-8433-33a659c9b25a | -4.37456 | -37.91178 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee0e19dc-41cf-3e07-9381-5f7ef3f0df29 | -4.37652 | -37.89944 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ee9fc5c-634e-3743-8d39-22baf808c0a4 | -4.36946 | -37.90929 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddd278d1-7c6b-3bbf-8ce6-38ea8fdb22e7 | -4.36379 | -37.91003 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dac4d51d-e7e7-3206-9255-9bcc3feed77a | -3.31339 | -41.86726 | 2026-01-15 03:42:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2970def6-4791-3879-896e-b0e3bfbf6ebd | -3.44858 | -38.99539 | 2026-01-15 03:42:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8cf56301-73dd-3c56-bbb4-21fba29c8684 | -4.3744 | -37.90165 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 374ef681-2b70-3946-a1cf-a444c07b7f21 | -4.37373 | -37.90575 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48303f38-5c97-313f-9de7-b1a62bf60bc5 | -5.60661 | -35.58323 | 2026-01-15 03:42:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9e448ca-0e94-3b79-bb98-e98ca0168553 | -4.37587 | -37.90355 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d57fc8c8-7f9b-3c9e-8fa3-1f9e30d0a6f4 | -4.37293 | -37.89885 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a38b4b0-0700-3206-81d8-c3546e9d15ac | -5.01983 | -37.54462 | 2026-01-15 03:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| faaec245-f413-3196-8578-4219f227f6ab | -4.36869 | -37.90237 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e92bfa03-3736-394c-a21a-acb8a56c10c4 | -4.36444 | -37.90592 | 2026-01-15 03:42:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 73628e90-9e83-3639-9f77-49064bb89474 | -11.86122 | -37.60205 | 2026-01-15 03:44:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| db33ba05-efca-37d4-84ed-b490819d1bd1 | -5.26277 | -44.73316 | 2026-01-15 03:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 936ce77d-6472-396f-9629-d29c64431cdf | -10.7697 | -45.01948 | 2026-01-15 03:44:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88a3d238-0110-345a-bab1-b330a3f65543 | -9.83287 | -36.99128 | 2026-01-15 03:44:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b73dfead-0276-390d-a400-bbe156043401 | -8.55911 | -40.37695 | 2026-01-15 03:44:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fbfd6d3b-3a54-3126-9a7b-e56d710531c4 | -12.39042 | -38.88696 | 2026-01-15 03:44:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e2131855-9a8d-3856-a52c-dc6d2bc24175 | -8.39607 | -44.05606 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d2b5308-d273-33ce-9d97-f87fbb3ec173 | -5.50924 | -41.22907 | 2026-01-15 03:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8015aeef-7360-3a9a-b33d-c7fafaf13b26 | -10.15735 | -42.20786 | 2026-01-15 03:44:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b49aeec4-d5be-3f7a-9336-de6b4f82ed57 | -8.15654 | -43.18679 | 2026-01-15 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ba30233-5b12-3fc6-88d0-bf60094ebd64 | -5.01519 | -41.87356 | 2026-01-15 03:44:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 943d6a39-174d-3012-aa73-fc51cdccb55f | -11.86515 | -37.59903 | 2026-01-15 03:44:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 550430a0-fa2c-3930-b09c-e812e642a023 | -11.2957 | -37.90605 | 2026-01-15 03:44:00 | NOAA-20 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4df2158f-d940-3e01-bda7-1a2e598f5389 | -9.00847 | -39.85786 | 2026-01-15 03:44:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26a49fb4-531a-397c-b196-65a4c2d7c291 | -7.68191 | -43.72754 | 2026-01-15 03:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7398577-29bb-304e-af66-f89540d4d046 | -10.59256 | -44.97868 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b519f4b9-e7d3-3c90-884e-9c92ccbc6e36 | -7.04965 | -43.95211 | 2026-01-15 03:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e74aa70-fe10-385e-9eb9-f9bcde91ea53 | -8.39658 | -44.05317 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51a376aa-dc30-36d1-a731-002d1624a306 | -7.50636 | -38.8184 | 2026-01-15 03:44:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fc8b83f-f6b0-3c8c-b187-a576a3a84541 | -7.2451 | -43.05129 | 2026-01-15 03:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 453acf96-fe31-32b5-af39-23f5f8ba6ada | -10.5937 | -44.97254 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 688177fa-e396-32a1-a4cc-cfd9d7751533 | -7.22283 | -39.9507 | 2026-01-15 03:44:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1983f44f-6e21-366d-b57b-db4e7ca09dcc | -12.66775 | -38.57063 | 2026-01-15 03:44:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 12618f04-6424-3099-8cf5-43b648c75c0e | -7.04911 | -43.9551 | 2026-01-15 03:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 195016ef-da22-319d-be3b-b935ea8b9f05 | -5.52617 | -37.79598 | 2026-01-15 03:44:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9b69e1e-1f5b-30d8-8f88-ba43e51ea5ce | -10.27561 | -36.57919 | 2026-01-15 03:44:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a1be8876-90a2-3aa1-8df3-f77542a15576 | -7.04558 | -43.95596 | 2026-01-15 03:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c54fb4f8-8adb-340a-9558-d5fd25d54a45 | -8.39555 | -44.05896 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 161893a9-1ad1-38cb-9ec3-95aa75d3c215 | -10.34297 | -44.82851 | 2026-01-15 03:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83446bbd-9240-325e-9945-67a20bd864b2 | -5.5297 | -37.79656 | 2026-01-15 03:44:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6bd53e66-c8fe-3016-91a1-b01d166edbba | -5.89603 | -42.55069 | 2026-01-15 03:44:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 26eccff6-d371-3a76-bca0-619f2d0df7fc | -8.15596 | -43.18503 | 2026-01-15 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b267105c-a23d-3e5c-9249-f32c247a1615 | -10.48207 | -44.93342 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae53e9f4-2319-3d7a-bc12-21f385fa089f | -8.42274 | -44.02238 | 2026-01-15 03:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa3541e3-24dc-37bf-ae84-a7d8ad5ba429 | -10.59313 | -44.97561 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d14ce4ae-4e7d-3a84-ba7b-f3f2397ae6a6 | -12.31346 | -38.97405 | 2026-01-15 03:44:00 | NOAA-20 | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe9f3a6b-7375-3c99-8ec2-c6155b7e4776 | -9.38907 | -36.89732 | 2026-01-15 03:44:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 536b244e-83f7-35fe-bf10-98a20a84e584 | -10.34572 | -44.83063 | 2026-01-15 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
