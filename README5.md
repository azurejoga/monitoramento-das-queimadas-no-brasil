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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8174a2f8-dc75-390a-bfb2-5be0ba9ea8e2 | -9.22197 | -48.59823 | 2025-07-10 00:43:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6259108-4eda-3ec4-89e7-49c160e42d86 | -9.30506 | -44.85073 | 2025-07-10 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 625e8fa4-e921-3efc-a131-f06f7fb4c19c | -7.7091 | -45.78011 | 2025-07-10 00:43:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a6938e2a-0ab7-30ca-83d0-9f9b7dd6325b | -11.46392 | -45.09585 | 2025-07-10 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9ae2f6c8-4b1f-3ca2-93d7-617066752c0a | -12.09779 | -44.73945 | 2025-07-10 00:43:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8a0360ff-40e4-380b-9f2e-b35987f8d11f | -10.96465 | -49.25734 | 2025-07-10 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60f5c6a0-e55b-3e54-bf08-8e612cb807a5 | -10.57084 | -49.1533 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| ee74c887-ec14-3aa2-90ea-c9b76c9d99bf | -7.23718 | -43.07727 | 2025-07-10 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.8 |
| 3b90534a-cecc-30ae-80b0-ea031fdb4381 | -11.36645 | -48.70853 | 2025-07-10 00:43:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e58657c3-8dbd-398c-86fc-0cbcce8eb6a9 | -10.66085 | -49.46296 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 340.6 |
| e278ef15-4324-3315-97cc-6607e68e9bb9 | -11.8318 | -48.22044 | 2025-07-10 00:43:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3a4e7315-c2f1-32ae-8b9e-db4868524907 | -5.23062 | -45.22232 | 2025-07-10 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a021ab3d-d0cd-37b2-a2d4-c2971b8406dd | -5.35537 | -45.27996 | 2025-07-10 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| cdb97904-f086-3fcb-b41e-92f331f1c5f8 | -4.22599 | -47.20278 | 2025-07-10 00:45:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 93928a43-522d-3ba8-a4b8-24cb0362fd20 | -5.03203 | -47.96733 | 2025-07-10 00:45:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c19f4925-91de-3ddf-b09a-088ec080a3ea | -5.07064 | -43.73026 | 2025-07-10 00:45:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 4bee0df9-fa25-370d-8ba0-f1272934e5be | -3.74633 | -47.12009 | 2025-07-10 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e865dfea-c960-38c5-b848-f5382d5eaf32 | -3.75417 | -47.12542 | 2025-07-10 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| d8188297-5781-372e-9ba2-353a34d79110 | -4.28748 | -48.18896 | 2025-07-10 00:45:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 396320ca-8bee-317c-b5ea-6c49029cbd53 | -5.41507 | -46.07554 | 2025-07-10 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7c3e5b31-4fd1-3d55-8075-176b250a3c4c | -5.5554 | -43.90485 | 2025-07-10 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 675daf96-ec9c-3557-84e9-44122cbdd09f | -3.74808 | -47.13259 | 2025-07-10 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2fa82ea1-1bea-3ebd-9fe8-8f193b9a7e53 | -5.35296 | -45.26379 | 2025-07-10 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| f60542d3-9c06-39be-8aca-b4a1061f418b | -4.22777 | -47.21493 | 2025-07-10 00:45:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a9e19043-933c-3ec1-ba23-b1cae4ed8102 | -3.75234 | -47.11295 | 2025-07-10 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 58c526d2-d6fb-3057-bc9e-3aa68c0cccb4 | -5.65183 | -46.58844 | 2025-07-10 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f237639-a31b-3d0c-86f0-69a92784f894 | -5.06606 | -43.72421 | 2025-07-10 00:45:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| a3afb6af-54f6-3873-bcdd-83b3c27cb7ab | -5.55281 | -43.89959 | 2025-07-10 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 826667de-450a-34e5-b791-69c4f5de0725 | -5.0674 | -43.7085 | 2025-07-10 00:45:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ceb1881a-e6a5-3ad7-b1b3-135d328de8ab | -3.74376 | -47.12687 | 2025-07-10 00:45:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8f3525f4-f2af-3308-833a-bf5898ca1ae6 | -6.6263 | -56.27658 | 2025-07-10 00:45:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0e7d2fff-e81f-3a5a-8d02-e5cdfad239be | -5.89482 | -45.58113 | 2025-07-10 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fd4de5d9-240a-32c7-8bb9-c970021ad1ab | -10.5776 | -49.1316 | 2025-07-10 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ea6ddbf4-83bc-35e5-a81b-fc736e08820d | -10.5773 | -49.1533 | 2025-07-10 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4130e18c-fd1f-3502-a0c0-faf3ef559b86 | -11.4584 | -45.1126 | 2025-07-10 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 81d12fe8-cc7d-3015-ad3b-e9a99ffac813 | -12.4433 | -43.7242 | 2025-07-10 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f6133b32-9451-3532-91a4-62c6dc79e002 | -12.424 | -43.7274 | 2025-07-10 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0204db20-615d-38a7-ba6c-326aa91ccb03 | -10.6678 | -49.4462 | 2025-07-10 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| cc88cbcc-a5eb-36c1-b4cd-fd0d4fe73402 | -3.75 | -47.1144 | 2025-07-10 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b93e0ebb-c4f9-36f0-881a-9aa486daa262 | -10.6486 | -49.47 | 2025-07-10 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a8389c05-4a12-39e9-95be-2778d0f54759 | -10.6675 | -49.4679 | 2025-07-10 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 32d09dd2-3520-3689-9ddb-da8306f8f766 | -10.6489 | -49.4483 | 2025-07-10 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 357c4c06-89c0-34c7-83d0-fc2dd67d087c | -10.6489 | -49.4483 | 2025-07-10 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3de231ac-e3d4-380d-8e72-c6335769ff4d | -10.6678 | -49.4462 | 2025-07-10 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 68d36344-9632-3f2c-b75a-0e0f172a2834 | -12.4433 | -43.7242 | 2025-07-10 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c5b34c92-37b6-3890-96a6-2787ec3d5b0d | -10.5776 | -49.1316 | 2025-07-10 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f62561b8-abd6-39d4-bd43-a334c55d785a | -10.6675 | -49.4679 | 2025-07-10 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 255.5 |
| fb3a2379-1eb0-3438-b6cb-be88cdb4ecd6 | -12.424 | -43.7274 | 2025-07-10 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8485f460-ef29-3da5-8c11-cb61c96fc8ce | -10.5773 | -49.1533 | 2025-07-10 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 562be6c2-52c9-3e13-a2d5-a3c9426f4ec0 | -10.6486 | -49.47 | 2025-07-10 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 45b1e5c8-6915-3b34-b070-909abc1d4d0e | -12.5828 | -48.8908 | 2025-07-10 01:04:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d59a070-f63c-3b1d-93d3-79d5dd09b81f | -12.5748 | -52.218498 | 2025-07-10 01:04:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf0790fe-2fd9-3a41-aac9-25678bc013ad | -12.5805 | -48.881199 | 2025-07-10 01:04:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b45bfa3d-ec90-3dda-bc98-c44c5011e436 | -17.789 | -52.437901 | 2025-07-10 01:04:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8442f0ee-cbbd-3f3d-b927-45afff6b2823 | -8.4936 | -43.265999 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c0b27e11-0e0d-370c-a428-2db201a6fd5c | -8.5031 | -43.2635 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4550f30a-ab10-3466-a724-29d9379ca8a0 | -9.2233 | -48.595299 | 2025-07-10 01:04:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd206b11-b3fb-398e-b434-936c3559a6a8 | -15.0338 | -57.187901 | 2025-07-10 01:04:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d514761c-8c00-3db5-b727-3276fb965269 | -10.6743 | -49.463402 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f03d31aa-d9b6-3f2b-b9c8-f4c94915bc5b | -7.4687 | -49.4063 | 2025-07-10 01:04:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf2b0f1e-0ac7-348f-8743-b116ff87275c | -12.4472 | -43.727501 | 2025-07-10 01:04:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1b58e53-0cf9-3c8e-a2b5-9145a372edcc | -22.250999 | -49.613998 | 2025-07-10 01:04:00 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b552fda-2950-378b-aa47-940291a48f65 | -18.040199 | -50.531601 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d9ebdb8e-f689-3db7-9c23-97800ad70c41 | -13.3419 | -52.913799 | 2025-07-10 01:04:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b613db54-aa0f-3cfc-835d-428aa2a1b898 | -10.6645 | -49.465801 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64ffb2f1-68b4-3b21-b47b-9782ab1988c8 | -11.3659 | -48.693199 | 2025-07-10 01:04:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08c880a6-f9e4-32f8-b7f3-511e4d7a7af1 | -10.588 | -49.150002 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95fafc9c-cec3-3a6d-a451-d80b5f55b2e7 | -8.5127 | -43.260899 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de5ab988-9fdc-343a-8e17-b9e68b24f7d9 | -10.5833 | -49.130402 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3282d80-5bcc-3868-889e-466425ae16b8 | -11.8804 | -58.7211 | 2025-07-10 01:04:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b96d36d-234e-3360-a970-bcb9ddb2b6db | -18.030399 | -50.534 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 33d590cf-25c6-30d9-a6c1-9c9bab8273b0 | -10.6623 | -49.456402 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98338275-95ce-3d6b-b3fc-58bf50e78a89 | -18.0368 | -50.5168 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2494d6eb-0b17-3133-903d-5d1ec9062e5b | -10.672 | -49.453999 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31153105-5ed9-3a1f-ab9b-a58bc3f3d102 | -11.8394 | -48.2206 | 2025-07-10 01:04:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acbb1236-52c4-3596-b1e1-72cc18f14830 | -8.5137 | -43.342999 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| adfa2776-7d2c-338f-8282-88f96b27cfb1 | -19.4569 | -48.546398 | 2025-07-10 01:04:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7a86d56-3f60-3a70-8115-0277ccf6f7a0 | -11.3781 | -48.700901 | 2025-07-10 01:04:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c11d45b-eee3-3d96-b75a-e41a4aed9d0b | -8.5233 | -43.3405 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3bdaf0e7-9b27-3dd1-98ba-9920b4425f78 | -22.2493 | -49.6064 | 2025-07-10 01:04:00 | METOP-C | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6f054cc9-d468-3098-8756-2aeac4e8d624 | -18.041901 | -50.539001 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1618ab17-890c-3079-836d-a2213453b3b6 | -12.5731 | -52.211399 | 2025-07-10 01:04:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9a6f9d6-d38a-3756-bf08-f960e3de83dd | -9.2135 | -48.597698 | 2025-07-10 01:04:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1affc49-7b73-30c7-9598-441dfc4c3f89 | -12.5633 | -52.213799 | 2025-07-10 01:04:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a56750b4-e98d-3bf2-a16e-1c9b2fc7990f | -7.0095 | -43.514099 | 2025-07-10 01:04:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c054a68-8b7f-39b4-9088-5e381f2ef994 | -8.507 | -43.317501 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44cde44a-ebf9-357c-b3f4-abffa83efd2d | -8.5195 | -43.286701 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aeb7197a-455b-3d81-a25d-fe31b88c551a | -10.6668 | -49.475101 | 2025-07-10 01:04:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3cf151-e225-3f93-b046-6453622314e2 | -11.8368 | -48.2099 | 2025-07-10 01:04:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2dd1b92e-bc0f-3bdd-a4be-8f26101d2336 | -11.8684 | -58.712002 | 2025-07-10 01:04:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44737e7f-a0ea-3c9b-9f11-17cec2019130 | -6.8676 | -42.806499 | 2025-07-10 01:04:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5058a79d-85bd-3ecb-bc66-e52c2b2e2353 | -19.454901 | -48.537998 | 2025-07-10 01:04:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e89a5e63-5eff-341e-94a0-f1ad02239f9c | -21.3596 | -48.622398 | 2025-07-10 01:04:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| be9ab1a5-223f-3641-a735-0c29b54899cb | -18.051701 | -50.536598 | 2025-07-10 01:04:00 | METOP-C | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1610de99-620b-3931-be81-c2d4c84c1e36 | -8.8671 | -47.943298 | 2025-07-10 01:04:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4fd54b5-9516-36ba-8df0-c6390dfafab2 | -11.8781 | -58.709999 | 2025-07-10 01:04:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38c99720-2214-3727-a6c1-22e324b9242c | -13.3451 | -52.927799 | 2025-07-10 01:04:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd14d207-5151-37ff-8e02-68dd52aa28d7 | -6.6328 | -56.281898 | 2025-07-10 01:04:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9573d4f0-2d6f-39ae-ae58-573f3ff3ff7a | -8.5262 | -43.312401 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc946a63-b63f-381d-b093-6d2941ac7eae | -8.5099 | -43.289299 | 2025-07-10 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README6.md)
