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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| febb2531-31e9-3a66-995b-0acfbd580b9d | -11.42113 | -46.40477 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faa66846-3a03-348d-b937-61f4b8fc7571 | -10.86142 | -49.11628 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b1b1a53-579b-3096-8748-34c132ceb3f6 | -16.83841 | -48.52796 | 2025-07-12 03:49:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73148334-29ce-35f6-9862-3e3b2d611f8d | -16.66386 | -50.62885 | 2025-07-12 03:49:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a25d78a2-9e46-347a-ae4f-9ca1340f5c8d | -10.66395 | -49.50754 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60bb0be7-588a-36d5-996d-f9ffcff067c7 | -13.11313 | -47.30343 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b02b0651-5d87-3999-ad15-435daf588f6a | -12.41011 | -45.35167 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed9ef0a3-8d12-3433-9fa7-32084b4bcaf7 | -10.84441 | -49.10789 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 160f3195-7455-3240-a310-275932e5e5ba | -12.41832 | -45.35833 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e903a552-3f68-3f57-9f3b-b91d63246409 | -10.6659 | -49.49765 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e11ce524-ba5a-3f17-89b4-01bcc9df74c0 | -12.41861 | -43.49381 | 2025-07-12 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c849039-42de-3976-b2aa-7868ba2dedee | -13.12121 | -47.28936 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 228aeae6-f209-355e-be9d-e76a034a3bd1 | -11.94357 | -49.30069 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 566854b6-bbf2-3bc9-a6dc-44c9cbc803ad | -10.8495 | -49.11361 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3902ba96-1a29-3643-b600-f345af594c27 | -12.10935 | -44.97823 | 2025-07-12 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fe0a209-3fac-397b-bceb-26b45fd655c7 | -13.13746 | -47.2878 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb60bc3b-c3ec-38c6-b83f-a30e116e3140 | -10.9 | -49.20649 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| aad08012-da65-3339-b6cb-9082fdaec503 | -16.68057 | -43.88409 | 2025-07-12 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7998714-00aa-3357-b34e-135ba6e31958 | -12.41991 | -43.48655 | 2025-07-12 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57c3174a-638f-3769-9556-b4a24797aadc | -13.13841 | -47.31026 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 494278f4-162a-344d-a25d-2dfb7d8db64a | -13.11823 | -47.30457 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cde54cb-db2e-3123-9e68-32e00faabfd0 | -11.72582 | -47.4696 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a42f17a-8abd-38b3-ac46-28810e296741 | -13.11965 | -47.29729 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb1142d-cff8-3529-87a2-fd52b3f15d98 | -4.54352 | -48.01014 | 2025-07-12 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b604db3c-e9b8-3b9e-9747-d9971605055f | -11.9445 | -49.29616 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77039817-8636-3a35-92ad-b1e7ed3dc8c3 | -10.9001 | -49.21312 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 55c47adc-3337-3adf-a7c2-d009a4d4da7e | -12.49076 | -45.01654 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 550a6612-b287-344f-90bb-2c16b6ec0fca | -13.11751 | -47.30824 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4848321c-dec6-3312-857d-328f615e8d5e | -14.32019 | -41.76544 | 2025-07-12 03:49:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cbbfe7bc-65bd-3f77-9c95-4fb6fd86de5b | -10.90101 | -49.20856 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8d1fbb9b-5b7b-3049-b7ed-37696adb6375 | -5.8412 | -48.3964 | 2025-07-12 03:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 6518606b-e6f5-3f21-9a0f-37e0e8e95104 | -10.8986 | -49.204 | 2025-07-12 03:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 241385b7-356e-3b2f-9860-0a5ff62b496e | -19.47005 | -44.29587 | 2025-07-12 03:51:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 343fd19d-3c69-3a8d-b8fe-2a7004749350 | -22.20022 | -41.64721 | 2025-07-12 03:51:00 | NOAA-20 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5f5f4f00-162a-32b0-b42c-bddfb3fe4078 | -22.20084 | -41.64343 | 2025-07-12 03:51:00 | NOAA-20 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dba95000-3798-372d-9e36-58a79f42994a | -23.98209 | -48.91829 | 2025-07-12 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6541f3f2-9648-3b79-ad66-28bd448d5e5b | -20.75727 | -42.57712 | 2025-07-12 03:51:00 | NOAA-20 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b7ece73f-d731-3867-8770-207b4bb02417 | -19.43815 | -44.34092 | 2025-07-12 03:51:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 796296d1-aa79-3ab3-8c7b-a5102861aa26 | -20.55893 | -45.39301 | 2025-07-12 03:51:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38506b69-1d66-3296-baaf-1a007203f01c | -20.81617 | -45.18886 | 2025-07-12 03:51:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 93c8f2fd-ac6f-3631-bf48-2f65da71782f | -20.26811 | -42.02342 | 2025-07-12 03:51:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 886fd97c-9d61-3801-90f0-a45056079df1 | -20.31227 | -45.58415 | 2025-07-12 03:51:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d15cd33a-848f-3bfb-bc74-17f621a1805d | -19.43596 | -44.33851 | 2025-07-12 03:51:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1df5f10e-d250-34c2-a315-b0c5d5fbd627 | -27.45487 | -48.45224 | 2025-07-12 03:53:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| effb3276-2c9a-34c2-a169-0d387d904579 | -5.8412 | -48.3964 | 2025-07-12 04:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 561b4b42-7110-3923-935b-9e474efc9f59 | -5.8413 | -48.3748 | 2025-07-12 04:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4db7658b-1430-3357-aa56-96e37e7bb076 | -10.8986 | -49.204 | 2025-07-12 04:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f5a893eb-39ea-3afb-9744-afd1337e5493 | -10.8986 | -49.204 | 2025-07-12 04:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 68608468-52bd-38bd-b1e8-91142aeeacdf | -5.8412 | -48.3964 | 2025-07-12 04:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 857d2dd6-c92a-3234-b746-205dd931700e | -10.8986 | -49.204 | 2025-07-12 04:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 996f9eaa-a511-3706-8d4d-3f0530d8a32f | -5.8598 | -48.3953 | 2025-07-12 04:20:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 39120c60-129a-3cf9-ab31-6ca05cbc299e | -5.8412 | -48.3964 | 2025-07-12 04:20:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 5674764a-b0c3-33d2-91a1-9e28fcaf86e3 | -5.8412 | -48.3964 | 2025-07-12 04:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| d8156ce2-ccfd-32cf-8b48-3dd0491dddd8 | -5.8598 | -48.3953 | 2025-07-12 04:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6c4b6d63-c1fa-3ef6-be1b-257fec1a284a | -4.66009 | -48.1514 | 2025-07-12 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dd194fe-c69e-3c32-9f1b-48275425722a | -4.23791 | -53.49189 | 2025-07-12 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c1c79b5-d8c4-3efa-898f-c8494918bb4d | -4.11835 | -54.91742 | 2025-07-12 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbb94a2f-ba72-3bd7-bec2-e368095da0c9 | -3.66569 | -48.31503 | 2025-07-12 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67e57d1-77c1-3407-b33f-0cb625942435 | -4.66343 | -48.15193 | 2025-07-12 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632b4fe1-9dab-3eff-af8b-97a1742c448b | -3.75928 | -47.11302 | 2025-07-12 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c517722-1eaf-3852-afb1-04c2612d79e4 | -4.51244 | -43.26082 | 2025-07-12 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaedfca6-eb5f-3b2a-be1d-d85b8ff9283d | -5.03537 | -48.51757 | 2025-07-12 04:38:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66731e5e-bffe-318f-8709-d85955244edd | -4.4764 | -42.93559 | 2025-07-12 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbecac82-8f0b-3bfa-bfe4-d42a16383353 | -5.43601 | -41.46505 | 2025-07-12 04:38:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 88b9a4ab-e513-33c0-a70c-9dca87213da6 | -3.75586 | -47.1125 | 2025-07-12 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3ffea11-a7e6-3bde-a61f-9fef0400c38d | -5.43334 | -41.46635 | 2025-07-12 04:38:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 52daee00-3b19-3258-a1db-7e715b58774d | -5.78113 | -45.10614 | 2025-07-12 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7f3fc9a-dc0e-3b9a-93cf-4f69ffc876b9 | -5.62732 | -44.26706 | 2025-07-12 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb6d60ef-e563-371f-8cb3-b26e245850e3 | -6.24973 | -43.36915 | 2025-07-12 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc22e192-b6fb-3e43-9a3e-9e776c18dd62 | -4.1193 | -54.91409 | 2025-07-12 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 806b61f2-4d73-3252-988e-1836363e45b4 | -5.78954 | -45.10256 | 2025-07-12 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6de7d7f6-2e86-3550-8da5-334bce2623b1 | -5.48347 | -47.46553 | 2025-07-12 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee5b4287-4b3c-3dcf-9a3e-394edb1d7f6e | -6.27423 | -43.41545 | 2025-07-12 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cd37fd23-5fbb-338d-9f7f-93f6ea6b82de | -6.25032 | -43.36494 | 2025-07-12 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04e94293-9798-342f-88c1-14a80b547534 | -6.24865 | -43.36694 | 2025-07-12 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e4ec9c7-0f09-368c-9ced-90d577b9e39b | -4.38499 | -41.91579 | 2025-07-12 04:38:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f82fb864-a6b9-3104-9731-76b8f56253d0 | -4.40123 | -47.45353 | 2025-07-12 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e70ede-520b-3aa2-933b-535e7a749a9a | -2.54958 | -47.70636 | 2025-07-12 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3202622-af7a-316f-b752-28a9830560d2 | -2.91217 | -48.23993 | 2025-07-12 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6850e8d1-2b0b-3567-86d3-9afade36f694 | -3.38182 | -43.12248 | 2025-07-12 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a46f74aa-d164-31e8-a391-c396e7e8ad1c | -3.86956 | -54.23131 | 2025-07-12 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 07e30936-b36e-3498-943d-7be4f85fa0cc | -2.91548 | -48.24044 | 2025-07-12 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fc9d90d-12b4-36f3-b1c8-1adf4ed8f383 | -4.47527 | -42.93748 | 2025-07-12 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d51e1787-9210-3ecd-bab4-5100bb5896cf | -10.8986 | -49.204 | 2025-07-12 04:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| ac7dfff5-f6d7-318a-8029-dac1325e93ca | -5.8412 | -48.3964 | 2025-07-12 04:40:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 63a08ef2-d2af-3516-a8e7-9c2929c9426f | -5.8598 | -48.3953 | 2025-07-12 04:40:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f62d3f81-ec06-3956-9ea8-6f57ae390c64 | -8.0389 | -50.10821 | 2025-07-12 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b3691ea-4a8e-34a1-b95c-bb9ae0d645df | -11.3261 | -51.44228 | 2025-07-12 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1c86b07-30ad-3778-a68d-6d47e23d469c | -10.57527 | -49.1195 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 12fbdc17-d8a5-353a-8886-73683ac2d64c | -8.39117 | -46.9394 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50004a70-a10b-379f-91f1-cac96223e003 | -11.94428 | -49.29557 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fcc22133-3699-313b-b6fa-fbcb741f5a12 | -11.73319 | -47.46059 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f7cdaa41-fd07-30f8-be43-8973cbe6f252 | -7.10288 | -44.11274 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4681ed9-5a8d-3d39-a023-b6bcdeb0111e | -11.42176 | -46.41082 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06d04fa8-2416-3945-b8b1-21d7f2835bd5 | -11.80334 | -46.6606 | 2025-07-12 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36dd64d2-4ae7-3c08-a954-31c67e7c1509 | -7.9893 | -46.41993 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 103d1337-fc1d-38a5-a612-f5a7bc70be0d | -11.43959 | -45.10211 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bafda938-c3b2-3b10-904d-ee693733e372 | -10.96214 | -49.25343 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 073d362e-039f-3753-9fe9-053e6cb12dd5 | -13.12043 | -47.29445 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b06f161d-59f2-3802-b9d8-42bb2f75fcf5 | -7.18006 | -42.97993 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
