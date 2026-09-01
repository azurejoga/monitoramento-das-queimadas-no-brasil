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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6595e174-192b-3ae9-95ae-ead3ea7b8dfa | -5.49275 | -57.14599 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e63b061-18c1-3354-9cf2-9d5cb3f293ae | -8.59576 | -54.77213 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1354d461-c13a-3ad0-9657-41ae4bdf844d | -10.40476 | -48.23353 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd2aa7ce-3c81-3928-8b8f-fc1a94b08ac5 | -9.1488 | -61.09475 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7380e440-0aa0-381d-a233-af5faf531ba2 | -5.88235 | -52.07196 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c8e29f9-4837-3247-8d29-d9a737d722b3 | -9.15422 | -59.54716 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e6fc94f-a19c-39ae-944a-92f328385244 | -11.30978 | -45.193 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eb6bf61-dec4-35c2-aede-f83c059fd04a | -8.42119 | -44.9969 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbe15fd3-29c7-3d9f-b351-e8b3533b24ec | -5.57842 | -60.23233 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d71803d6-04fe-3e77-966e-924a257c704c | -11.20768 | -45.08851 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8e6a34c-6f95-3f04-a410-ca14343aa2ff | -6.94977 | -55.63854 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1987f4be-cfd7-34a5-a2a2-b5684373bb67 | -7.34383 | -60.58923 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4d9af9c-bdd7-3889-a0a8-8739e3722270 | -7.29048 | -49.83986 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5dd8d680-1d56-3191-84b1-def9f0926526 | -9.67476 | -48.31747 | 2026-09-01 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56d8f9fa-b72e-32b5-ae6f-faefdca7b2d0 | -5.25013 | -55.9062 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb29c387-ecc1-3e36-817f-01fb94e6364e | -11.25099 | -51.25896 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 925afebe-149e-3ad7-a05a-93a93b6f7b6f | -4.79622 | -55.9765 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d0b83a0-ff65-3123-9f84-a0b4a6dec757 | -10.0188 | -44.69153 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3457d47-7aa6-323a-9ad5-36ba165ddb8d | -5.96164 | -57.68175 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e83d50bd-0613-3752-9564-c892b82f5586 | -10.78444 | -50.50402 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcaacaaf-2fca-3890-b19b-888736df0ad5 | -3.62438 | -60.56402 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ce16ae15-c840-3947-9f57-ceaeeb3887f8 | -9.4578 | -45.62238 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| afb29e40-3919-3782-b9b5-84fa34a53417 | -6.1609 | -52.63563 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e23f76a-1b41-327a-a330-e9d5f28a20b3 | -10.74398 | -54.04934 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5479ef8d-586f-35a1-8778-149a536f60bb | -11.79016 | -47.67595 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55d56056-2cfd-3013-b3bb-87dc364efe34 | -10.00737 | -46.4437 | 2026-09-01 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74b73dc4-64ad-34fa-b9bc-3864e100e617 | -6.92486 | -55.63039 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85fcd700-79bd-32e2-9b42-5e9379eaa0fb | -7.73607 | -55.22363 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9927e1a-5139-318d-85de-0691b14a2ee2 | -8.50325 | -55.30851 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7249a574-4edc-391f-ab97-12cdf6c483eb | -7.53126 | -61.38278 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c285efb0-ce4a-3bf3-9183-667cf1fb4a2a | -3.62032 | -60.5634 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25a73e2c-51a5-3568-a6ab-fd17a034c472 | -11.28981 | -50.57824 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b6ce3a2d-ed87-37be-9308-5f574e9248ec | -5.48985 | -57.14193 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb308e19-ff76-32a7-a102-904024c7186c | -10.06176 | -48.70287 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cd6e57c-587e-38d6-8b03-6f0234dd940c | -6.68492 | -41.66433 | 2026-09-01 04:40:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 73163fa2-e2f5-399b-8996-6c940341dbb4 | -6.21148 | -53.58629 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a10bdb3-8fa2-3ecf-9bb7-f085a1ab043e | -8.27964 | -54.92596 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f09961e8-1db5-3f4d-88b8-c057dab69106 | -9.18726 | -59.45901 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 987d056c-44ef-33d1-8d26-de6358dfb55f | -10.74407 | -47.98549 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fd0df12-e529-3657-a5ce-ea4e6bc2a157 | -7.60488 | -44.88536 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6e7ee2ac-c78d-3493-9cc4-b680678192ee | -11.29202 | -50.58577 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ae730a59-b658-34cd-bfa0-a935f41a9ea9 | -11.09921 | -51.57198 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52e0a46c-7cfe-3869-a652-9962f4f61d7d | -6.17904 | -57.73476 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 23566c5b-034e-391f-b828-f5449cac94d0 | -8.79168 | -62.51245 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef763c6a-fd7b-394e-bf03-d9fb99692e04 | -9.45854 | -45.61728 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 28eff259-5f9d-3a02-80b3-d60fe82db901 | -5.80536 | -43.64264 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9080597c-c0d7-3614-ba44-2b06de5b480b | -3.79283 | -59.34712 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fc0f118-fa5c-3923-8ef7-146bc298fb15 | -6.15784 | -57.40448 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 622546c9-ab00-3054-8cc5-eb3194fd85dd | -6.67466 | -52.86721 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02d8e782-58e5-356f-b8bd-c9c1401d4a6c | -7.88341 | -47.0807 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a29305b-6536-3134-b409-d426b9bd1dee | -9.15281 | -60.94485 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8a469e60-efa0-3bf0-baee-34b85e80be7b | -8.77243 | -46.44909 | 2026-09-01 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13538f2e-4414-30d5-8b9d-555e889025b8 | -11.37017 | -45.2328 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0184388-67b3-3cc1-89c2-096b001ba431 | -11.21504 | -46.08223 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18144395-afe9-34e8-a22f-55235551633b | -9.39959 | -51.60705 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b8366d5-e833-308f-8f76-506bc7e1f5f4 | -10.39577 | -45.08205 | 2026-09-01 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94829d05-9ef2-345c-ba20-2d7d71557205 | -4.97393 | -55.84943 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f07c375-2c3d-3d64-901a-1f5b1deb03ed | -5.91919 | -47.05399 | 2026-09-01 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1778ce8-364b-35dc-aa95-e31ac322f084 | -10.99445 | -48.395 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dba2afa2-586d-3cf2-82d3-26bc1c485d60 | -6.62236 | -58.38507 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf924de6-d610-3914-a35b-9a195fd8d8c0 | -8.70888 | -52.36377 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04650d36-edf3-3e2a-aa26-2fc8129613de | -11.92252 | -45.0937 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 062b54fb-0422-3f67-8831-8c0d011ae027 | -7.28385 | -60.66079 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb1eaf60-01d1-3b9e-a468-fccbc61ed3e5 | -8.79918 | -62.50829 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce8adc9f-0251-361b-9ee4-07e4482c2c62 | -11.27883 | -50.6052 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c58061e4-6250-34b5-8ff6-5e6bc7639197 | -8.27671 | -54.91907 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 791eae15-708a-3105-9731-3aaf2932caae | -10.05836 | -48.70238 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c281ac3-ad20-3d8e-b891-b2e247798bfe | -11.93894 | -45.10347 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 277fa81d-7a0d-3c0d-b8ff-bbd97bdf29eb | -7.56416 | -60.4701 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b00b0b9-6fba-39eb-a62a-436b35a41e2c | -6.78968 | -55.63854 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec01c868-1d35-3373-bd35-8b7ff40c3845 | -11.68163 | -47.15181 | 2026-09-01 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b2aeb63-2e73-3a5a-9bcb-bd05bed8ff03 | -10.20184 | -50.36041 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1d0767f-56b8-3119-89bf-3cb19fc7ecaa | -10.03531 | -44.70062 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cad8ef27-e536-347d-85e5-cb50f541a71a | -8.49325 | -44.75393 | 2026-09-01 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3b3e74d-66bb-3ffb-878d-5c5a142c6b5c | -9.67521 | -50.85577 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 349d86d1-6415-33d4-9be5-1dafd1eec316 | -6.13162 | -53.55183 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6284c0bb-58d7-384a-8066-b75a291a15dc | -10.04306 | -48.68853 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61e18676-7bf4-32af-935b-838b24198a82 | -9.41612 | -51.67657 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e54fc707-5424-3130-8707-e7df2cad7db7 | -3.59993 | -54.55297 | 2026-09-01 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f45421b-145a-365d-a8e2-cf42d79f824a | -6.57498 | -49.89309 | 2026-09-01 04:40:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9888e403-a469-3372-89f5-d3b1513adad6 | -5.96036 | -53.62754 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d747073-aa07-3ee0-9d29-5ebe09942585 | -6.48691 | -49.88996 | 2026-09-01 04:40:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65ae7fe2-4835-3b39-baa0-497e930505d2 | -10.68424 | -46.27589 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d27b14c-e596-3abc-b33e-7d54c4dbe7e2 | -7.64883 | -46.71381 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7ed8b4f-6c57-3f98-92df-8a09fc03c751 | -3.61641 | -59.07778 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb708424-cae2-38e5-a29d-e1ea68502de7 | -9.1484 | -59.53144 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56208ce4-ca4a-3704-8478-613d66bfb0ca | -10.03164 | -44.69602 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b5e69adc-2656-397b-a825-aa4849aeb177 | -8.86139 | -48.82557 | 2026-09-01 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b53660cf-bdcf-303d-8b02-013560eddc19 | -5.87333 | -57.77501 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18dbcb68-94e1-3a04-a589-b3b1364cbbeb | -6.73956 | -56.33774 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa2c68ec-8a36-34cf-9fe5-56e498582ef0 | -9.47581 | -57.02113 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51f334e3-6640-368b-ad44-da8088d870af | -10.13595 | -45.72501 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7bd3b4a-1f24-33dc-8ccb-f29322a93ae1 | -9.15314 | -59.53572 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89d45c14-309c-3849-98f7-58b6a58ea40e | -6.92633 | -55.6274 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05bdf92a-af79-3156-8bb4-39de29fe094c | -5.58818 | -42.31559 | 2026-09-01 04:40:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c11a2742-0601-3c89-a10b-e37864b3b3c0 | -11.92305 | -45.08989 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0e12d49-b6c9-3701-82c6-044471ca34ed | -7.28306 | -60.66512 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f04553cd-e4a7-3665-939f-66c3f787b116 | -9.15849 | -59.53669 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e3bd86-fac2-3a48-b0e8-85addbe8f642 | -10.03951 | -44.70121 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26b7d312-fb4e-3dfb-83a4-12d8f1aebabf | -8.79933 | -62.50766 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README42.md)
