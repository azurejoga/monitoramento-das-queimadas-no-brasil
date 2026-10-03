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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84d2fb82-00c0-3d1e-ad4c-dfcdc8d10565 | -4.28003 | -50.7758 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1530be40-9b0d-3312-bda4-fd589747f369 | -4.29297 | -50.78154 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc37aa5-b858-3983-a9cb-9434d6ba460d | -10.36322 | -39.49969 | 2026-10-03 04:40:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 257b340b-0eea-3670-b9de-f6e869864249 | -6.92905 | -49.62136 | 2026-10-03 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 792a7d91-b3e7-38f6-a89d-1d856bb2abcb | -5.75175 | -45.14428 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 862a2240-b5cd-31c3-800a-b3dc54c5cc33 | -4.39734 | -49.96774 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0ebbff8-66e4-33ea-a0c4-1ab3aa551c49 | -3.67383 | -54.18938 | 2026-10-03 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df9cd174-1a5a-3700-980d-98175ab1b019 | -6.91912 | -59.27744 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5b32f20-144e-3a16-8c65-fadda37b9c26 | -5.9468 | -43.64802 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0cad40a9-e690-3485-87d8-912872d2a781 | -5.13888 | -45.57988 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26a83d0d-f030-3378-810d-374665424200 | -5.48405 | -44.6315 | 2026-10-03 04:40:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a73a216-7763-3bda-bbfd-848b2470c33a | -6.50674 | -41.74588 | 2026-10-03 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c0ec8c6e-122e-3de9-a350-4c5c0809c789 | -11.71682 | -43.42522 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e16af413-bbf8-33c4-a945-c6219f880581 | -6.01241 | -53.54311 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3208465c-faaa-3e2c-b7b2-fd34f488fc81 | -4.42676 | -55.74617 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fec8e6bb-4caf-39ef-8f2c-007ffb870173 | -4.26377 | -50.7474 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ed34347-9ecd-3dab-a0b3-3b3dbcf3e952 | -5.94739 | -43.64405 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 93f315c3-ef36-3531-a9dc-9ee83dfb654f | -5.89121 | -55.48368 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a00ee41e-dbca-36e0-9d0a-3f85439c7fe1 | -6.15762 | -43.68542 | 2026-10-03 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c979dfc5-cc1e-32bd-8c81-75321147e823 | -5.85526 | -53.48004 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85bcdb39-7852-3ee2-8fee-26c4b8fe0096 | -6.86187 | -59.25318 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6bfb933-ce7f-3ee4-a0cc-ddbcad03dd9b | -5.95164 | -43.64473 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 51fd0d11-d6d5-3766-8778-2e4af0617a5d | -4.28168 | -50.78722 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3599ed60-2b5c-3d9a-9acd-4c6b74600932 | -6.32024 | -43.34447 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 81f84970-8b17-30de-8e92-e2209328b7a8 | -4.9861 | -45.64518 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f2be6381-dfc3-3fac-aefe-0fc9955f7d8f | -9.45922 | -40.37143 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| abc6e9b2-c1ca-3b37-844a-7166f3abfa95 | -5.74557 | -45.05445 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4e3c21e-cb18-3ba2-a88f-b880023e4c14 | -6.16539 | -52.76298 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e960ff3-75e3-3c89-8ae0-471b6cd1dda1 | -3.84955 | -55.80526 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3609bfc5-fd75-3224-8e6f-8eb26d1d1415 | -6.23532 | -53.14431 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50b4df08-603c-3e64-bddc-810c8eb70cbb | -11.72358 | -43.49949 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 20481f52-5d42-3ae9-b01d-ca72e330d42d | -5.11935 | -48.4363 | 2026-10-03 04:40:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81676dee-fce9-35be-99ed-2f960b5ebd49 | -4.81113 | -49.86945 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e551af6a-c36a-3404-ab6a-9205401d3e8b | -6.01011 | -53.53353 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d771099-4adf-3397-ba00-f2be52ed99c6 | -6.91368 | -59.27655 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0de0e9aa-8644-3035-beac-3cbf371d2487 | -3.51832 | -54.602 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1dc32384-8750-37a9-b606-d310ec603a78 | -4.53815 | -50.78306 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a3193e-7780-3228-b445-c4ebb441b47f | -5.25171 | -55.92082 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfd66d58-78d2-3bb0-8730-67d83c2aa3e8 | -5.73945 | -45.14742 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e02cff50-f796-39ed-bd49-80825cfe45d9 | -3.95919 | -55.32382 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ae59887-e847-3332-9f18-59bf5f4ab39a | -6.84226 | -59.26002 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f34c659-8409-3655-86f0-c02f0898e9b7 | -5.74274 | -45.13961 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f00eca57-da0f-3807-841d-e916a5f65185 | -3.8521 | -55.96827 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7aebda00-e91f-3616-adc0-8c2fec4b9488 | -5.74257 | -45.15285 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 22713143-a9fc-3867-890f-4ba9cfb7e42d | -5.74404 | -45.14313 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4d11e678-0980-3918-9111-f4201df9a7cd | -6.33625 | -43.36225 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 279bfa85-295b-3900-9478-fb7be10ff640 | -9.44896 | -40.36219 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11f5a611-dfec-3dcb-b9c9-36e68a3caea1 | -6.23463 | -53.14856 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1edb598-4586-3613-9c39-a943e947a4ae | -5.76736 | -43.98711 | 2026-10-03 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7aac339b-28fb-3279-a86a-d00b6ba5ce63 | -5.89411 | -55.49252 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33e4863c-e7c9-3923-970c-20fbce45fb4f | -3.64098 | -55.49957 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5839bca-e86c-3f7b-b167-b7f82ab44c98 | -4.26829 | -50.74069 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 694533ca-eac9-38aa-b32c-e6914835e455 | -9.79663 | -54.10765 | 2026-10-03 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 189714ca-f648-30c1-b10a-5cc1b36ad408 | -5.13719 | -45.57734 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 90b5c6d4-c238-3950-bfa7-b5e4fe4dadc0 | -4.30144 | -50.77176 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1622d528-8034-3d9a-8e49-0fc09ca789f0 | -9.47141 | -40.36537 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.2 |
| e8688feb-e6bf-3f09-aa1b-4b4318ce2bec | -4.20921 | -53.56379 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4d50f0-74fe-3088-bfbe-9be55d0fb07f | -9.45873 | -40.37524 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| a7a9d1b5-a70d-3eb7-af18-df75d1ebde33 | -5.94563 | -43.65594 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| a5d9a052-72fe-3916-930f-afaa6c006304 | -4.27109 | -50.74484 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 779f44f7-c420-31b0-890a-a4366b063263 | -4.28959 | -50.78102 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0567cfe6-383b-3784-a922-182386c0ae93 | -5.74716 | -45.14854 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4934aedb-9d69-3393-a0f0-992f98d2e6b3 | -6.15705 | -43.68929 | 2026-10-03 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbeceb58-2fd4-33c0-b667-138470f23612 | -11.6507 | -42.41503 | 2026-10-03 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 770d5506-8907-3fb1-a924-c2c550d67272 | -5.10026 | -56.25577 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed99281-25c7-31bd-8e2a-d769dd72b9d0 | -5.85603 | -53.47524 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 756ad0cf-c118-35e9-949a-7988500f750b | -6.51501 | -55.38981 | 2026-10-03 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1176b8df-6bd3-3efc-901f-1c357c5618b6 | -6.20029 | -53.26816 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff179886-88c3-355f-b0e5-0b108380e7dc | -5.13655 | -45.58168 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28c9e749-34ad-34f4-a42a-aae7774d47e4 | -5.95356 | -43.66121 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2160d71-b131-3504-b5cb-6dd1b6ae4fe0 | -5.39621 | -45.39403 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b29e334-206c-3ddd-9844-fba32ce2e32d | -5.88985 | -55.49176 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 962ba2f5-f819-3cc7-ab23-525070aee89f | -5.74519 | -45.14988 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 592d1b1a-fde0-3ed6-82ec-4a90f842eae6 | -10.2744 | -57.73609 | 2026-10-03 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b41f9ca8-31c2-3948-9821-ba41fe08e8ee | -4.45409 | -49.69283 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 043a5fbb-1f80-39ac-a32d-e81c79ed0bf6 | -4.28902 | -50.78465 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d7cc34-37c8-3a3f-b972-e765ff9f6a74 | -3.67847 | -54.18641 | 2026-10-03 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9d7e119-feea-34be-8306-88542ccd69de | -10.35697 | -40.56223 | 2026-10-03 04:40:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12e0b18e-5931-3fdf-9b18-53a8107dc422 | -5.82917 | -45.00862 | 2026-10-03 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f453f987-3434-38bc-bb96-109c0d4274c3 | -7.02955 | -44.63565 | 2026-10-03 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1956ae0b-4948-3f07-bb2a-951ab5cf1341 | -9.46531 | -40.3684 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.2 |
| a18ba268-c67c-3bb5-bfd0-04d973013aff | -6.2201 | -53.26289 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10170da7-deda-316d-b4e8-c61af9ee4a28 | -5.13347 | -45.57671 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| baf81ee7-96d1-320b-af9f-002366985bbb | -9.9585 | -55.32816 | 2026-10-03 04:40:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f711fb52-c535-3547-864c-b37859f6392e | -4.98981 | -45.64568 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cacdcbb-43cd-3e2c-bfcb-2aa459ebffa0 | -6.8489 | -59.29426 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7b33248c-0fb3-3108-bc06-5bf8eaee9300 | -5.93221 | -46.34998 | 2026-10-03 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed382c0-505c-352a-b517-8d6846319dcc | -5.22153 | -46.02081 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f5b44ff-4eec-39da-8d56-a4381f3d903a | -4.81398 | -46.8229 | 2026-10-03 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4f51293-9179-3e5b-b487-cf7d4bab607e | -5.59535 | -44.90837 | 2026-10-03 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7cb899a-9cb6-3909-b4c4-c6df5390bb00 | -9.47044 | -40.37301 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 9bf5acfb-174c-3806-a1ff-9b278ad9c9d3 | -6.92852 | -49.62481 | 2026-10-03 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ba30b86-2fbf-3097-9805-512701aad393 | -5.73705 | -45.13719 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a92dbe48-1631-3f72-963b-02e8f49547c2 | -5.74975 | -45.1456 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 268717ab-16dc-35a8-950b-7eb4022fd505 | -6.01316 | -53.53849 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93bd82dc-ffc4-337e-a41c-75a7ad60030c | -5.8575 | -53.46604 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 650073e6-96b9-3985-9577-e5dacfa73e2b | -7.48422 | -47.59149 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 367455d8-1965-31ad-9012-b7b35dc97e8b | -6.22382 | -52.68751 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b89095f8-af67-3dbd-951a-1b971154a38e | -6.84376 | -59.26053 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a18b04d-b6c1-3400-93a5-ae4d394c26f9 | -4.12285 | -55.0174 | 2026-10-03 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
