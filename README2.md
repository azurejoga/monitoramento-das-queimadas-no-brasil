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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b29e6682-f969-36c6-bd89-359a47de6936 | -3.5813 | -41.660702 | 2025-11-30 00:03:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a72580aa-9bea-384d-b7c2-6d12024e9ffc | -8.0462 | -43.134899 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8acd9eac-ce7c-3409-993e-164167f97c2e | -2.8899 | -45.244801 | 2025-11-30 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f537aa2-cf6c-3494-8e28-dab3f477d1c7 | -3.0738 | -45.057999 | 2025-11-30 00:03:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8ffec6e-4f2f-38c6-9983-5e797dde98c1 | -2.8922 | -45.254902 | 2025-11-30 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc29066-884b-35d9-824d-ab0fcf94e55e | -5.5393 | -39.668098 | 2025-11-30 00:03:00 | METOP-C | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9e057364-5c45-30f7-af68-e6bb8dfe47d4 | -3.5394 | -43.293098 | 2025-11-30 00:03:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2afa1d08-4da1-3290-bad0-c82f416c819c | -8.0266 | -43.139099 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fd9cff2d-c080-35d1-9c52-7ec932f4dcc8 | -3.9453 | -45.833801 | 2025-11-30 00:03:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d921b8bb-2fbd-35d2-a0a1-610ecc01efcc | -7.8226 | -40.644798 | 2025-11-30 00:03:00 | METOP-C | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cb3c9c30-e1ca-313e-a560-91ace2e54f44 | -2.774 | -47.418701 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1632c4-332b-3a3e-9701-76c100dd704d | -2.5247 | -45.583099 | 2025-11-30 00:03:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1b5f4d-4593-3ed8-8a9d-a3aa313ebf21 | -4.3524 | -43.156799 | 2025-11-30 00:03:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba62ff3c-43a0-3397-8e85-b519b113da17 | -8.0423 | -43.1171 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5facd41-08a3-3ba9-a246-46c724ca2d44 | -2.8736 | -45.3549 | 2025-11-30 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40666070-19e2-3c74-abbe-b96b13190526 | -7.8325 | -40.642601 | 2025-11-30 00:03:00 | METOP-C | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 292d4454-9a0b-3e59-ae9c-df30898d548b | -3.348 | -45.547401 | 2025-11-30 00:03:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13b63d41-d02c-30e5-8a01-fe83b5c68787 | -2.7348 | -45.194599 | 2025-11-30 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2e2d6e2-7fb1-3760-917b-df598210aa51 | -3.9688 | -42.5056 | 2025-11-30 00:03:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82edac4b-099e-3b12-9c7c-a5b37a8a35ab | -2.5223 | -45.572701 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4ffa21-a400-3f0d-82cf-a64aac3948bf | -3.3004 | -45.380798 | 2025-11-30 00:03:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e348f601-cc3b-35a6-8c16-cfea11aa4921 | -3.5911 | -41.658501 | 2025-11-30 00:03:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d20bda10-057d-3090-a917-506335ed22c1 | -5.7333 | -39.84 | 2025-11-30 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ff386760-aea8-312f-a0eb-c294d5d34958 | -3.3674 | -43.807098 | 2025-11-30 00:03:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54333eda-fcd4-39ab-81dc-8199d92f89c3 | -5.7386 | -40.813801 | 2025-11-30 00:03:00 | METOP-C | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1a8e5e16-ed5c-3272-8e4b-093208820a37 | -4.4347 | -44.486599 | 2025-11-30 00:03:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| facf31b5-3d59-3610-8435-e23742e75950 | -2.6222 | -48.018101 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c721b76f-0418-3172-9eec-963c1cbbbbf3 | -5.7288 | -40.816002 | 2025-11-30 00:03:00 | METOP-C | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 606220db-6c74-3269-81d5-cf508e2ed353 | -2.6319 | -48.015999 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e92be4ef-b02a-3cf1-885f-e7dae128546c | -2.4022 | -45.631901 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf192b10-6f1d-3e61-b8ad-2b07ce8f083d | -4.4167 | -43.305401 | 2025-11-30 00:03:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c80c92bb-6203-3de8-90be-75f2b35f5335 | -5.7204 | -39.828499 | 2025-11-30 00:03:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7116800a-19fd-3b87-8ae1-b5d70fa2b45c | -3.1884 | -44.426601 | 2025-11-30 00:03:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf4a5bf-532d-32fd-a275-b14641bb704a | -2.8945 | -45.264999 | 2025-11-30 00:03:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c640c282-315b-33e5-8ab3-2e2fc42a3d81 | -3.869 | -42.519699 | 2025-11-30 00:03:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 75ea5d02-392d-3c85-844d-17c06e97f86b | -8.0344 | -43.128101 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2bcbf1d2-4d56-3b49-abcf-a551d0ef9254 | -2.515 | -45.5853 | 2025-11-30 00:03:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef9e934f-4da9-3020-a4ac-ca2df41414a6 | -4.2729 | -40.669498 | 2025-11-30 00:03:00 | METOP-C | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 59b034b0-893a-3fb0-970f-8b211d0f9048 | -3.4062 | -44.115898 | 2025-11-30 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 330bdc8d-32e5-39bd-bf42-553535b6453d | -3.6555 | -40.9007 | 2025-11-30 00:03:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e3d38890-d2aa-3814-9309-7c87c36dfe73 | -2.7495 | -45.0774 | 2025-11-30 00:03:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40cfe062-ed2f-3647-947e-e5890f89030f | -3.3027 | -45.391201 | 2025-11-30 00:03:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84f701b7-73c0-3497-b0b0-661a55b4bd5a | -8.0364 | -43.137001 | 2025-11-30 00:03:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e4127bcd-34c3-3742-a597-c12c1141b627 | -2.7371 | -45.204601 | 2025-11-30 00:03:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed8b970-25b1-318f-9a15-b91cbe8c7915 | -3.0716 | -45.048199 | 2025-11-30 00:03:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b42c6b1b-908e-34c0-89a6-006e619b2764 | -3.1496 | -43.162102 | 2025-11-30 00:03:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3289d7b7-69bc-3ee3-810f-6d42df116fb3 | -3.4042 | -44.106998 | 2025-11-30 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b74fa2a0-8143-3496-8cba-6d3541c554a0 | -2.9277 | -44.865601 | 2025-11-30 00:03:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9911407-b588-314f-acdd-78c4dc11bf2a | -2.4006 | -45.352001 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4c351c-1ac5-338e-91e5-cc10082f0159 | -2.2926 | -45.1469 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1eccb548-a584-35ff-a72c-c28749ec4a28 | -3.5257 | -43.870701 | 2025-11-30 00:03:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fbbfdda-2cdc-3a7a-b1b0-17506f22d72a | -5.737 | -40.8069 | 2025-11-30 00:03:00 | METOP-C | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 92e68b43-b42e-3838-adef-c41827ed16e9 | -3.3712 | -43.8241 | 2025-11-30 00:03:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2504b0-7114-368c-883a-6bf2319ef5f4 | -3.4668 | -44.384701 | 2025-11-30 00:03:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b24fd4e5-9fad-310e-88c4-73e2724a4ba9 | -5.7272 | -40.809101 | 2025-11-30 00:03:00 | METOP-C | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 33bde755-3a3b-3b0e-9231-d36d84df44f8 | -2.4029 | -45.362099 | 2025-11-30 00:03:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22c09447-aca7-3655-86c7-309ccab1055d | -3.6223 | -42.7491 | 2025-11-30 00:03:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca805065-4d2a-3915-991a-e0b5e908351d | -3.624 | -42.756699 | 2025-11-30 00:03:00 | METOP-C | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6e604a3-1fa8-3bd8-96d2-d643d8ab2466 | -3.5797 | -41.653599 | 2025-11-30 00:03:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f29dd056-2ef3-3d01-979a-42c295ed4e5b | -2.6257 | -48.033401 | 2025-11-30 00:03:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc552ab4-7a1f-3d9f-9867-96c3e8d42a9a | -2.527 | -45.593601 | 2025-11-30 00:03:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9df2d10-8348-3489-a32b-ee481884ffb9 | -2.6354 | -48.0313 | 2025-11-30 00:03:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4efa79e-319c-37f3-a0ac-f5ab016c2085 | -8.051 | -43.1237 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 306.6 |
| dcc456ca-8506-30e2-8c36-0023148349c0 | -2.4524 | -47.0726 | 2025-11-30 00:10:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 68dc93bf-d797-3f58-8e1c-23dc556a0c99 | -3.5945 | -41.6817 | 2025-11-30 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| ca37d4b5-271e-3028-96ef-43e5756d6f09 | -5.7306 | -39.8534 | 2025-11-30 00:10:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 842425a7-6a18-3547-a03a-e7c188559dc4 | -8.0318 | -43.1493 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| dac7a8eb-13c9-3ebc-80f3-91d6c167ace6 | -12.0195 | -49.2659 | 2025-11-30 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 812eaffd-a7fe-3b4b-aedd-fad9231edecf | -2.4523 | -47.0945 | 2025-11-30 00:10:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| bcbeb458-4a84-30fa-959e-97b93993f41d | -8.1633 | -43.2055 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 435038c7-c470-3ee1-bb83-04fd06364c17 | -8.0507 | -43.1472 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| fbe19f26-10a8-3e97-aeb9-61c76d1cc900 | -12.0004 | -49.2683 | 2025-11-30 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| aebe3b61-5621-3b61-a745-c4e54c1eaa14 | -23.6237 | -52.959 | 2025-11-30 00:10:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| 9c695625-bee2-36b6-a719-113cadb9ecd2 | -2.6322 | -48.542 | 2025-11-30 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 979f96b1-91b6-3ddb-a66b-43c6e827000f | -2.6507 | -48.5629 | 2025-11-30 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 04d3dde2-a645-3106-96b4-7ea97e32c971 | -8.0513 | -43.1001 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 86c8d589-af4d-3697-89ac-9fb790c34c16 | -8.0321 | -43.1257 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 224.7 |
| b82bdd7e-786e-3569-a4fd-5145c930fa29 | -2.6507 | -48.5414 | 2025-11-30 00:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 04deba8d-32e4-360b-82a6-4fc383a99e48 | -8.1822 | -43.2034 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 7e3be8c7-3622-353d-b142-b1dbd5c9b5a6 | -5.7309 | -39.8286 | 2025-11-30 00:10:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 86.1 |
| d927f289-6b9b-389e-8448-f06bd06cf313 | -3.5946 | -41.6577 | 2025-11-30 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| c4d5fe30-39bc-324f-9c8e-676e4c7530a9 | -8.0324 | -43.1022 | 2025-11-30 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 3badc2a8-9478-30dc-b8d8-bef4d046f9d8 | -3.5759 | -41.6587 | 2025-11-30 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 9e698546-97c9-3d58-9bac-9f83337543d3 | -7.5014 | -37.4242 | 2025-11-30 00:10:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 2b4d8bf7-8c86-3aba-9111-156e574c9901 | -2.532 | -45.5862 | 2025-11-30 00:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 476610ca-e459-39eb-adc5-cf0f9c00963a | -8.0507 | -43.1472 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 7dcf55e8-3e6a-3cf1-831a-c340c92e7a1b | -8.1633 | -43.2055 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 45252002-9d63-3b64-9da9-b7122cbdc833 | -8.0318 | -43.1493 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| f4d2d16e-3b33-33d4-b0da-1e6041dbb9f4 | -8.051 | -43.1237 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 284.0 |
| 2b62954d-f303-3ba9-a6b1-59d44ab290cc | -5.712 | -39.8302 | 2025-11-30 00:20:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 8cddacf0-8f3b-3a7a-a349-c7e3ee0247f9 | -19.8675 | -57.7808 | 2025-11-30 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| 664d82a3-1812-3a7b-a39c-21a584105e7f | -2.4204 | -45.6343 | 2025-11-30 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 5c218799-2bfa-3bc7-8a6a-7fa25634bd78 | -19.8477 | -57.7627 | 2025-11-30 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.3 |
| fdfcc191-2de3-3cf4-976e-ae97e1d621de | -8.0513 | -43.1001 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| b4e847b6-9b94-30be-9245-d741e78e4e00 | -3.5759 | -41.6587 | 2025-11-30 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 382e2e41-e50a-3af4-a787-cbbfb9e80cbd | -8.163 | -43.229 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 91480d4e-5779-3803-b1fc-d41407d12b7f | -2.4018 | -45.6349 | 2025-11-30 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| b50856bf-9497-36c1-bb34-94e7c3a7900d | -2.4523 | -47.0945 | 2025-11-30 00:20:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| ead61aa8-8559-319c-821c-ae37a349e255 | -2.6507 | -48.5414 | 2025-11-30 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 95b7ca39-78ec-3337-b40c-ec12a038eec5 | -8.1822 | -43.2034 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |


[Clique aqui para ver as próximas entradas](README3.md)
