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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3579c88b-0652-3da9-be23-e0a504084ecb | -23.55235 | -45.61204 | 2025-08-03 04:32:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 05f39496-e2b0-3f4a-b935-dcdab8abe18d | -23.83831 | -52.95245 | 2025-08-03 04:32:00 | NOAA-21 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af26c765-3f40-35f1-8cec-9d34c29e4419 | -25.35482 | -52.16479 | 2025-08-03 04:32:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 46fc1679-a94b-3418-a762-ee6f0aa1545e | -26.78134 | -52.21257 | 2025-08-03 04:32:00 | NOAA-21 | FAXINAL DOS GUEDES | SANTA CATARINA | Brasil | 4205308 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a05a93c-a6cb-3d03-859f-62ba5a7518a1 | -25.80494 | -52.58167 | 2025-08-03 04:32:00 | NOAA-21 | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4a657773-4353-3ee3-b9db-d372a1c7e6e2 | -22.90715 | -49.69281 | 2025-08-03 04:32:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bddb7424-36cf-39c6-bf6d-0b02a97f6cf6 | -23.98575 | -51.3123 | 2025-08-03 04:32:00 | NOAA-21 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 76c706fb-d07e-3309-81f8-f5e6a8557fba | -27.182 | -53.41446 | 2025-08-03 04:32:00 | NOAA-21 | VICENTE DUTRA | RIO GRANDE DO SUL | Brasil | 4323101 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7730a43c-ac8e-31fb-9d14-3666635d0a4c | -8.0132 | -43.1278 | 2025-08-03 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 58cd99e7-3bf1-30dd-8634-711ef3343f02 | -8.0126 | -43.1749 | 2025-08-03 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 272.8 |
| 997c7132-1573-32bf-8e37-ba4a06a0ce88 | -7.994 | -43.1534 | 2025-08-03 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 203.8 |
| e8542352-cd12-379e-8203-1a33cef835ec | -8.0123 | -43.1984 | 2025-08-03 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| ebf37ba7-e596-37e4-aa93-e534ef08e9b8 | -4.5497 | -44.2047 | 2025-08-03 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d7633b81-5146-3ba4-8d60-1f922fee730c | -8.0129 | -43.1513 | 2025-08-03 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 461.3 |
| 98fb7e9a-11dd-3c21-bf87-0fd7749275f2 | -7.9937 | -43.1769 | 2025-08-03 04:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 166.8 |
| e603902b-1941-3594-9052-8d18766f4be0 | -8.0129 | -43.1513 | 2025-08-03 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 372.1 |
| 0a6248fa-a055-3012-85ce-873948c6643b | -4.5497 | -44.2047 | 2025-08-03 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e3cb7515-7337-3e42-8fe7-4c9837501ce3 | -7.9937 | -43.1769 | 2025-08-03 04:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 167.5 |
| 6b5a9bb4-ed88-35f9-b11d-a11ae4e15b52 | -7.994 | -43.1534 | 2025-08-03 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 179.0 |
| d54f0213-db04-3b4f-905f-0f56c8fae9f7 | -6.6329 | -59.9649 | 2025-08-03 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 55e47325-7b5f-34e8-a64f-35fe355df4e1 | -8.0126 | -43.1749 | 2025-08-03 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 266.7 |
| e75ec891-b77f-34e6-acdb-992f60c119b4 | -6.6144 | -59.9656 | 2025-08-03 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 18caf7d9-a466-35b7-8fb0-742cfe594ba9 | -8.0132 | -43.1278 | 2025-08-03 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 6c459bb2-0db9-3360-a88f-3b5aa31e06f9 | -4.31303 | -48.10018 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25b13209-ef68-3092-8c1d-aba5c45ca539 | -4.06253 | -46.93624 | 2025-08-03 04:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16e53e7c-8173-3397-91d0-71bdcaaf446f | -2.90703 | -52.54938 | 2025-08-03 04:51:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b867352-edfa-3577-ac54-1a4b5538ca26 | -2.92331 | -48.675 | 2025-08-03 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f1b537b-5248-3fe5-8932-686fff735cc8 | -5.92019 | -50.00586 | 2025-08-03 04:51:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 780644ef-3e22-3aa8-99ef-ff943f190d8a | -6.5172 | -42.80319 | 2025-08-03 04:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ebbd6f36-9dce-39d3-b111-65727488b58e | -1.60157 | -49.92569 | 2025-08-03 04:51:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4fc0cfb-f966-3630-a40d-ee2ccb83ee3c | -6.49855 | -42.8146 | 2025-08-03 04:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ca8d10c-2a12-323d-894e-84ef7362dbd6 | -6.5305 | -44.53316 | 2025-08-03 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e41b95ae-39b8-3194-835d-4ef5ad2fa08f | -4.56088 | -44.20529 | 2025-08-03 04:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 0bdb7d8d-6ef6-33c3-a336-b6a9141f613e | -6.67849 | -44.35165 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b76b66da-9b1f-3f6d-921b-e1d50a454d3a | -0.7478 | -51.09209 | 2025-08-03 04:51:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c8c35b8-179a-3b51-b7d7-31ea2a52ed1c | -1.40399 | -54.125 | 2025-08-03 04:51:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ecb3159-0797-3634-b613-dec2cd3cb79f | -3.58159 | -47.51291 | 2025-08-03 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49681517-158e-37bf-a5ef-2f7898e32cb0 | -2.90654 | -54.15766 | 2025-08-03 04:51:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1de3c890-06dd-34c4-892c-4b6fdb0bb0ca | -2.28876 | -47.87117 | 2025-08-03 04:51:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 891cfa76-a384-302b-888a-cb9c107ba1af | -6.68485 | -44.34328 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b8ed747-499a-3b0d-8e00-f796f0e80ea6 | -4.31234 | -48.10477 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9ac04cda-6a57-3798-b251-9542f9e92dcd | -4.30591 | -48.10174 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ef77f4d-0a76-30cf-9d0f-038f874aa23a | -4.85579 | -45.74681 | 2025-08-03 04:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 537882c5-f746-32de-943f-5bf5fc48b971 | -6.85991 | -44.28789 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8e6f49a-b5f1-3e6f-8f06-586b42e39af6 | -4.55892 | -44.2081 | 2025-08-03 04:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5eec5923-81fa-34dd-bc5f-5f55dcce5a58 | -4.85647 | -45.74228 | 2025-08-03 04:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a1e1704-5d02-38d7-81c9-e4b740fb17c9 | -4.3097 | -48.1023 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c698f80a-704d-38d2-a522-f4ebf3edd024 | -4.10497 | -48.20349 | 2025-08-03 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e3d96ce-3af2-3f03-a541-efec6a8a1b32 | -4.55973 | -44.20273 | 2025-08-03 04:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 4c31dc27-0025-3665-b357-fc5eb86d42b2 | -5.59358 | -51.12711 | 2025-08-03 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f248ba8-872a-384e-a5eb-ba7dd8704167 | -3.4362 | -48.95604 | 2025-08-03 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 162d79a2-0e09-34d5-9672-36f3445cfb11 | -6.67943 | -44.34513 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf6911d3-ff62-31bc-8339-508c7bfffd5c | -6.20469 | -46.3444 | 2025-08-03 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2736ace-9237-35fd-ab4c-4190b8e9f14a | -4.30924 | -48.09961 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 220c208f-1d53-3555-ae59-b13fb28864dc | -4.0268 | -48.05928 | 2025-08-03 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab6ae2fb-8376-3e06-8ddf-66d5e0417bdd | -2.58713 | -51.92019 | 2025-08-03 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a3b172-ac2c-3c42-9094-bdac504f8247 | -6.52276 | -42.80418 | 2025-08-03 04:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0a76337-23b8-3302-8329-f9271ead4798 | -3.6624 | -50.95271 | 2025-08-03 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5008a6af-8d8c-3b4e-b463-4438c9f7ec19 | -4.30856 | -48.1042 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 29028a78-d880-34de-af53-23470d3ca5ca | -3.48393 | -51.1897 | 2025-08-03 04:51:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f14eb2ad-fc41-34e6-b8ba-bed2ee6c3b68 | -3.28174 | -48.8176 | 2025-08-03 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8729fbfa-dd1d-3595-bb1e-ccaf873312e9 | -4.55399 | -44.20736 | 2025-08-03 04:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4c40269a-5c06-387b-91e0-dd1230a4ada5 | -6.86033 | -44.28491 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df082ee7-d668-37e1-8542-f6a1fb5daa4d | -4.0261 | -48.06392 | 2025-08-03 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7cc4177-4daa-3815-93c0-84679149b1da | -3.96391 | -49.43924 | 2025-08-03 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94dff992-31ee-3c09-9fe9-d8901fbf84a7 | -3.79049 | -40.99779 | 2025-08-03 04:51:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbd7ef79-295c-388f-8b23-bfee0a152995 | -6.68186 | -44.36397 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62397619-8449-375e-8a5c-71ffd4214648 | -5.94792 | -50.08112 | 2025-08-03 04:51:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11bc7a5b-8a4a-316f-ac0b-2416378b32c7 | -2.80891 | -49.00948 | 2025-08-03 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7e67525-9df9-37f0-a624-c14fe750c64d | -3.05235 | -54.53409 | 2025-08-03 04:51:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0e23598-801a-3646-88ec-2fd8e6a9f9df | -6.20844 | -46.34933 | 2025-08-03 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f345f7a5-6ff3-3356-997f-f30c9f067dc1 | -6.49805 | -42.81822 | 2025-08-03 04:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3aa8ac0-5f4b-3f58-b323-4ce8bfeeaa76 | -3.66294 | -50.9492 | 2025-08-03 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b624b309-99b2-32b2-8c2c-10a061d753cb | -6.67723 | -44.3604 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6dff8bb-c2c6-3ff2-9f8c-227b17fee13c | -6.20408 | -46.34865 | 2025-08-03 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84bfd67a-9763-3fab-9fe8-2ca78f03512e | -2.99468 | -49.32182 | 2025-08-03 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0da8818d-0eed-3b8d-a141-856d7f7fe477 | -4.31278 | -48.10744 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3813f53e-4519-3945-960d-2eb95ed08374 | -6.67684 | -44.36313 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbd08249-964e-3fe9-9cfd-319d92b8d1e2 | -2.58658 | -51.92363 | 2025-08-03 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bcb3473-46d0-38c2-bcfb-cdf3fabd1b20 | -4.30899 | -48.10688 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a2ec3f14-7db5-3381-9e09-d79dc17a703e | -6.67804 | -44.35481 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23d770c9-71aa-3508-8019-9e7976e8a717 | -4.77179 | -45.33836 | 2025-08-03 04:51:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93cea479-10f8-30b7-af47-941ef6884557 | -4.56466 | -44.20351 | 2025-08-03 04:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12c3cce1-e3f8-37b5-a41f-7b9e7769ec6d | -3.37971 | -46.93078 | 2025-08-03 04:51:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d823d569-9351-3485-b31b-ff79926f8010 | -6.68523 | -44.34063 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7b75688-7561-363d-ab32-203ef1cf009e | -6.52886 | -42.80133 | 2025-08-03 04:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0bdc0e23-bd2a-3f6b-a1a1-3bf90727a270 | -6.67763 | -44.35763 | 2025-08-03 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40bd64cb-5a63-30c2-8351-cad04bcb3db0 | -4.31349 | -48.10287 | 2025-08-03 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 62ed1281-2d82-35a1-875d-3508fe1ffec2 | -2.91004 | -54.15821 | 2025-08-03 04:51:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13b8132e-8b69-32b2-b8f8-b8c249aced6c | -4.56167 | -44.19975 | 2025-08-03 04:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f7a1e7a3-dd37-3f8f-999e-7521cd1a2c5e | -3.78984 | -41.00227 | 2025-08-03 04:51:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc57079d-8892-30f9-bcae-4bd41ecaedb9 | -4.06297 | -46.93677 | 2025-08-03 04:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ba28640-4fd2-335c-ab9a-778a57b27565 | -4.77636 | -45.3391 | 2025-08-03 04:51:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 724eed7d-5b29-3acb-950e-2bc08e167dd7 | -6.7268 | -59.18349 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e13a659-9578-3974-ae9c-a4e28be8d0ff | -7.96851 | -45.10617 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a292fa78-8c82-3a27-bb53-1bf0baf09ef7 | -7.9997 | -43.18264 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 76635702-869a-3587-855c-58bde235fa95 | -10.4734 | -46.95284 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2217d0b-b319-3715-8a6e-d5af907fccf1 | -12.64196 | -44.51939 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7764e87-5ad4-3d8f-aa97-3d057cae31c3 | -6.81567 | -59.26989 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed2e9e95-786e-3006-a1b8-bf0fb2709b93 | -6.61441 | -59.9587 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README22.md)
