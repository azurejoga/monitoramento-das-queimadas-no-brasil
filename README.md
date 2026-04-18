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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 277143b3-ac20-3715-9a6f-09aa5eba69b5 | -21.19479 | -48.6069 | 2026-04-18 00:13:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 251eb8c4-f852-3cc2-8332-e801b76c0e14 | -21.03172 | -48.55016 | 2026-04-18 00:13:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| de56643e-b1ac-37a1-ac4b-f3df2cc1cc2c | -21.19609 | -48.61708 | 2026-04-18 00:13:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8a5e5823-e53b-38f5-8509-1f6e153f6eee | -21.04008 | -48.5533 | 2026-04-18 00:13:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 9acbbefa-d7db-33f7-b565-401e9bb5d450 | -21.70488 | -48.43245 | 2026-04-18 00:13:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7332b10c-12eb-3b0a-ba51-b77d1ab6e3cd | -22.87347 | -47.17938 | 2026-04-18 00:13:00 | TERRA_M-M | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a75012cd-d048-37cd-b69f-a10b2ce2b394 | -23.65191 | -48.00538 | 2026-04-18 00:13:00 | TERRA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2cd12b3b-798a-32e3-b1ca-15ee5d0d03d8 | -18.07372 | -46.36882 | 2026-04-18 00:16:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1825016b-b6c9-364d-8d87-61e514764a22 | -20.16185 | -46.72772 | 2026-04-18 00:16:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 503dfd10-0e7d-37fd-936d-fda860f98d93 | -17.57384 | -46.61153 | 2026-04-18 00:16:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 998afea1-23c7-3068-996e-94f1af1b1522 | -20.63005 | -51.70774 | 2026-04-18 00:16:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 302921af-f0f6-3f4c-ba12-68daa847ae84 | -18.02167 | -51.03592 | 2026-04-18 00:16:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 46205872-0b5a-3421-94d3-31cc28781771 | -17.57247 | -46.60205 | 2026-04-18 00:16:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00cc7c80-373b-343b-8eb5-811220c929d7 | -20.16054 | -46.71837 | 2026-04-18 00:16:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| aae21add-646c-3e53-a737-129dadc3e60e | -19.38915 | -52.985 | 2026-04-18 00:16:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b6aab88b-a548-3d31-a287-56df00f96bbb | -18.0751 | -46.37832 | 2026-04-18 00:16:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 796299a4-4891-30bd-82fd-b97a16dc743e | -18.02019 | -51.02382 | 2026-04-18 00:16:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7881e078-2fa8-31e2-8c47-b9f0e6d235d2 | -19.37721 | -52.98624 | 2026-04-18 00:16:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b44a9def-a132-340f-884f-be1471691144 | -12.27965 | -44.61832 | 2026-04-18 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6996ad34-092b-303c-986b-a856ae25b104 | -12.69224 | -45.29248 | 2026-04-18 00:18:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 793761bd-8aa7-3664-b8b9-c21e4518e40e | -10.403 | -44.9392 | 2026-04-18 00:18:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e0d0023c-8179-360a-82f7-d6aeb865cf0e | -11.97228 | -43.84549 | 2026-04-18 00:18:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 24c79dad-49ff-3514-bb4d-ef3815a20604 | 2.743 | -61.3568 | 2026-04-18 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4d121214-5a94-3ba6-a6c9-b639f1ef61e6 | 2.743 | -61.3568 | 2026-04-18 01:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9746d264-f5d9-3040-8083-a1aff22ec1d0 | -21.1955 | -48.605 | 2026-04-18 01:10:00 | GOES-19 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| d1589ffa-62cc-3f6c-9429-7ada7b3f869d | 2.743 | -61.3568 | 2026-04-18 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 714e2476-26e7-31f5-8f2b-8416c62b4043 | 2.7247 | -61.3571 | 2026-04-18 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 4b299316-790a-3e1b-9370-25c16e291b9f | 2.743 | -61.3568 | 2026-04-18 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 29f99d39-b219-31eb-87b0-8b108cf5372d | -21.1955 | -48.605 | 2026-04-18 01:40:00 | GOES-19 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| c98c8b69-f3eb-342d-a557-525fd73da0bf | -5.53428 | -35.51733 | 2026-04-18 03:47:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f99f2417-db36-3cc3-a96e-4377d779174e | -9.13944 | -40.99812 | 2026-04-18 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df09d602-468b-3965-a1df-26b136b2997c | -11.78254 | -43.66305 | 2026-04-18 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bd23387-7a0c-3ab7-8dd4-a680a6393b5b | -10.46635 | -38.61863 | 2026-04-18 03:49:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f8cad81-2244-327b-8741-5b979123a904 | -11.54615 | -37.81078 | 2026-04-18 03:49:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae1ed72a-d969-3bcc-8362-5023b7c8f497 | -10.46358 | -38.61453 | 2026-04-18 03:49:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11d70e75-5575-313f-be1d-424a2f0f1ec0 | -8.10159 | -43.15485 | 2026-04-18 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29ecb051-8593-3241-b35f-b9b3a6f5973a | -10.46301 | -38.61809 | 2026-04-18 03:49:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a082335a-b5c0-3d30-9ead-09f48396e801 | -10.46969 | -38.61916 | 2026-04-18 03:49:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bdc50ce0-5f9b-3302-82a8-bb888f3e2f0d | -9.1373 | -40.99959 | 2026-04-18 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc021a91-5958-394c-9b9b-17db02eaabc6 | -11.54284 | -37.81025 | 2026-04-18 03:49:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b98cc4e8-dc21-312d-b3de-6062285e7177 | -9.13868 | -41.00257 | 2026-04-18 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a591dd3d-f7c1-3def-b799-29d3160e9b24 | -10.46692 | -38.61507 | 2026-04-18 03:49:00 | NOAA-21 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2263901-ead9-3474-a99b-42eacaabcbf4 | -10.14275 | -39.99465 | 2026-04-18 03:49:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bed4f09a-28c5-3f78-924d-ca48ebf51d55 | -11.19073 | -43.56395 | 2026-04-18 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ca15813-a8ab-3dba-8338-b9011ff7dc2b | -10.47696 | -37.42698 | 2026-04-18 03:49:00 | NOAA-21 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd741646-649a-33db-ba72-7231fa51c3b9 | -7.39064 | -43.21451 | 2026-04-18 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ded93ce-e5ef-3069-a0b7-b1816b297139 | -11.9771 | -43.842 | 2026-04-18 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddfa72d2-7562-3c51-babe-29146341e18e | -20.05226 | -40.71558 | 2026-04-18 03:51:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c28bf537-3e01-3b85-ba53-a3f44c7fd85e | -19.36117 | -40.65118 | 2026-04-18 03:51:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3038e07a-644d-39da-81b3-4f9fe26e4ac8 | -15.91785 | -44.79048 | 2026-04-18 03:51:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2083e9fe-7576-3de2-a426-8ad57bb391ee | -18.07239 | -46.37307 | 2026-04-18 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eca236d1-f109-3111-afe4-1d4029ab912b | -13.68184 | -44.2924 | 2026-04-18 03:51:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4453b828-7eec-308b-8029-5516bca2a7e6 | -18.104 | -40.3435 | 2026-04-18 03:51:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcf7f69d-4957-31b4-81ec-2dd178970cab | -17.57716 | -46.60658 | 2026-04-18 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2516af1d-dc92-3158-a54b-dce026d377f8 | -18.07684 | -46.37414 | 2026-04-18 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac93aa17-b237-3b2b-ad53-8431fe629bc2 | -19.5963 | -40.07529 | 2026-04-18 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 767730e9-ed24-32eb-a3f1-5d8aafcc0136 | -19.35782 | -40.65062 | 2026-04-18 03:51:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1b0a589-6a4a-33fc-9fcb-cfea8e607903 | -17.21875 | -39.68831 | 2026-04-18 03:51:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8fe7d0fa-7830-32fd-b5e2-410b75517e8c | -13.44157 | -43.85337 | 2026-04-18 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5baadc7-5934-33b1-8482-428084abc80c | -20.10584 | -40.18694 | 2026-04-18 03:51:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd24c91a-905a-30fd-82f5-acd11258440c | -17.31013 | -39.45526 | 2026-04-18 03:51:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c87b83e5-6932-323d-907d-84c53afbcfcf | -17.93157 | -42.98504 | 2026-04-18 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ca1286cc-3e57-36e8-8ec3-b5d16d275e2c | -23.56281 | -47.50865 | 2026-04-18 03:53:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 823f3c66-172c-351a-8076-985c73475b9c | -21.03535 | -48.55155 | 2026-04-18 03:53:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f5b18b8-a672-3b09-b523-7c95d11e2b34 | -20.62455 | -51.7095 | 2026-04-18 03:53:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37befa4d-cfc3-3b21-b899-04dcc9b0e692 | -22.96411 | -52.69841 | 2026-04-18 03:53:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6602f0e8-65aa-3d8c-9cb5-78dfcd15516b | -23.56181 | -47.5106 | 2026-04-18 03:53:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e0bced7-ef73-32c0-b1a5-e95db657a97c | -20.63042 | -51.71119 | 2026-04-18 03:53:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c99f41d-3f96-36d7-b5ad-90244a1d5475 | -22.32028 | -48.24033 | 2026-04-18 03:53:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33465337-5eeb-30e9-8efa-241259a981ff | -21.04019 | -48.55273 | 2026-04-18 03:53:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0bf2dfa5-aaa2-3719-b3d9-8ab0ed8c95f9 | -22.87249 | -47.17626 | 2026-04-18 03:53:00 | NOAA-21 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f402b2de-b106-35c8-80b7-2bb9c1c6ae9c | -22.95055 | -42.98003 | 2026-04-18 03:53:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d5d1acd5-9561-3385-8d80-87ef49f5fdef | -21.23249 | -48.79821 | 2026-04-18 03:53:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 97cc8cda-8ca0-3dc6-8845-9dcaf44642c5 | -22.96867 | -52.69957 | 2026-04-18 03:53:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b2b70155-7d6e-3327-8343-7c529fffae31 | -22.32601 | -48.23621 | 2026-04-18 03:53:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd149bac-e48c-33a2-8c40-aa91b50caa6e | -21.71322 | -48.43073 | 2026-04-18 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3f78330-0427-3917-8654-17e8ffe5f9d6 | -20.63358 | -51.69736 | 2026-04-18 03:53:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8de9833-f0b0-3928-9596-76d543b6fe6d | -21.03719 | -48.5563 | 2026-04-18 03:53:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7c26a8ba-2ae6-396b-8337-b1acfdf79ecd | -21.19405 | -48.6078 | 2026-04-18 03:53:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| ee272881-cd4f-3c53-badf-79e572395126 | -20.63147 | -51.70658 | 2026-04-18 03:53:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf97d590-a86e-3697-af3e-cabbe446912a | -22.96274 | -52.69782 | 2026-04-18 03:53:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5908613-8036-3d85-b7b8-db5ac0b36553 | -21.71434 | -48.42525 | 2026-04-18 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2341d072-277f-38ce-88d7-8588184a4354 | -21.71353 | -48.42694 | 2026-04-18 03:53:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b58b2063-a4e1-3306-b923-8a28ccea1a3a | -20.63462 | -51.69278 | 2026-04-18 03:53:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fd8f4df-4569-32c0-a399-5bff88f87065 | -22.87708 | -42.39495 | 2026-04-18 03:53:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb4f3ce8-7c7b-317b-ad3f-9c9839644b86 | -22.32137 | -48.23514 | 2026-04-18 03:53:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d97b578a-4f6b-3594-89c5-3418e40260df | -20.1569 | -46.71397 | 2026-04-18 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd9a4036-2938-3f6d-a4d5-ea2682cbf3cc | -20.16476 | -46.7207 | 2026-04-18 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4567f4f2-7afc-3a7b-b676-4c28de8d8611 | -22.3232 | -48.23801 | 2026-04-18 03:53:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 381199e7-cf6a-3a03-ad39-2e99c02fc085 | -20.16129 | -46.71498 | 2026-04-18 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f08ca9a3-dea5-3223-9af8-25d565a48ff4 | -21.03839 | -48.55045 | 2026-04-18 03:53:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a01c9b88-52d5-3162-89a3-368cd711707f | -20.16384 | -46.72542 | 2026-04-18 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be6f444d-52dc-39a5-bcd9-29d4eea5b917 | -19.97756 | -44.85655 | 2026-04-18 03:53:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfa46769-691c-3c0b-8bf7-fc70cad99050 | -20.6256 | -51.7049 | 2026-04-18 03:53:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbaeda0a-e925-3977-82c9-6a79b6b5ae9b | -20.86783 | -43.3021 | 2026-04-18 03:53:00 | NOAA-21 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b2e092b-62b9-3466-a085-80ea92917da0 | -28.06323 | -48.67426 | 2026-04-18 03:55:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e1607a46-b7ae-3384-965b-cd3dcb494fef | -28.69318 | -50.17061 | 2026-04-18 03:55:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fdd62a9d-31ee-3166-89f6-79a8c1576b57 | -28.06414 | -48.66991 | 2026-04-18 03:55:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd07c39d-e772-36d8-b4f6-7baba3356ed8 | -9.13699 | -40.99966 | 2026-04-18 04:21:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e82a6318-e5ab-3806-b1e6-61097bb770de | -8.10152 | -43.15464 | 2026-04-18 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README2.md)
