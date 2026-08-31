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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcb0bd09-b435-316e-8dbc-d1aafd76ff0a | -5.58743 | -42.32587 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7e762c9d-8111-3168-92d1-3f84e3319e0e | -7.99479 | -44.27685 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8c7dc145-e1a6-3a4d-9175-7f24bb3daee6 | -8.04784 | -61.73812 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 624fe42e-c5fb-30e1-9306-5c549f7b1599 | -8.44593 | -46.90429 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e83a2853-9aed-35a4-ba00-09a57a15035b | -9.4214 | -45.68359 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6f6d6106-c3b8-3fb4-9f31-ae91c2d65839 | -8.61468 | -54.78571 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e19997aa-f1bb-3731-ba5f-c215de839fe3 | -7.56623 | -61.37435 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 11938b77-6e0d-305a-a051-0284e5eec2a1 | -7.48793 | -55.29945 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f89791b2-f887-32c4-8345-fc6dd80bc3fb | -7.99173 | -44.28244 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| c670b46e-e0de-37f9-af56-964971e88372 | -12.10541 | -47.27214 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 77a494c6-c4d6-35e1-9e05-548d0b57efef | -11.07129 | -51.5165 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 38b82586-47e1-3a20-a23f-f2c5337ebcd1 | -7.91538 | -44.236 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1b61ba02-4937-3c18-93ef-ee4184774a3c | -9.67545 | -47.933 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1518c010-4440-35c7-ac4f-f809975d28a1 | -6.81408 | -43.52897 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5fc4014d-a29b-3c8a-8831-e02bb6212dae | -7.29901 | -46.17809 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 043d189b-17ac-3401-a597-b60676cc0359 | -10.75606 | -54.0668 | 2026-08-31 16:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5aeabbbf-1147-3981-8934-d72415a6663b | -9.16229 | -59.51072 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e73b5344-d186-3a82-927c-48abdadd3dab | -11.6981 | -47.64625 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10f9c7ee-6109-3ae1-8d1d-0e8fce138eab | -5.80506 | -43.64473 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d9b20785-567f-3141-b33e-50d62f944250 | -7.62324 | -44.94087 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 765b056d-e35a-3dd4-8e2b-28b9465feb1d | -7.05587 | -45.41862 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f3cadff-af02-3fc9-8f4f-ff452bde9a75 | -8.80799 | -62.4922 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 330c9605-fe9d-3bfc-a3a9-38986a088a66 | -14.12179 | -52.80303 | 2026-08-31 16:50:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6a497114-af1f-38de-ad26-f24e55882608 | -9.47965 | -57.01517 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7ceb9b3a-87b7-3f59-b78f-33c057b33ac4 | -4.91674 | -40.66627 | 2026-08-31 16:50:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 46c62d2e-8025-34c7-bb8d-c8fe5d42f1d5 | -12.38518 | -48.16943 | 2026-08-31 16:50:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f8cf9066-9bdd-3ca7-b24c-87db23d43d95 | -10.10772 | -50.30218 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 49d8d4e3-2052-3cc4-ad33-b38938525c26 | -9.68647 | -47.93845 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f4713a04-ce53-3259-baa9-5163d8a346b2 | -11.63274 | -49.4215 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| feaf0984-1d30-35d1-9f56-8cd717734363 | -11.03 | -49.67545 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1847b0c1-062b-3860-8157-aa5e1fbccc81 | -8.73903 | -39.0049 | 2026-08-31 16:50:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| df062e90-24cb-3bb4-b27a-e47d019c4079 | -11.72075 | -47.63908 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ee25b03-c336-3542-91c5-b43e61f31209 | -9.29867 | -45.39295 | 2026-08-31 16:50:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 756fb188-c605-3ef1-bf4a-214aefc8cffb | -9.80208 | -60.16012 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1565c455-76c1-38d1-bdb2-b1316ef521f8 | -11.25212 | -45.10636 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 548d6bb2-718f-38fb-99a3-73a7042e9c95 | -10.55894 | -46.17142 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 19cfe5c3-3cbf-395d-95ae-bd27577229f6 | -11.20136 | -45.06398 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db71c340-2a21-314b-b36f-3d9a19e60f92 | -8.13709 | -45.57759 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d5414fc5-d8bf-3c0c-9c0c-28020a184c45 | -10.79922 | -41.30612 | 2026-08-31 16:50:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5f92c159-2fde-3a7a-bf1e-51fdbe46620b | -8.76749 | -46.4572 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1f6eaf6d-2b3e-33a2-bfaa-a83da3281f12 | -10.85221 | -45.32241 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b8bbdc16-d0a9-3f6b-86af-7d7ac29c19a3 | -11.51922 | -46.9498 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 42a23187-0763-38cf-8afd-8e343288f052 | -5.7616 | -44.12902 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1a3802ed-f5b0-3316-b9c1-319973466fe8 | -11.32616 | -45.20826 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| eb1483fd-b0ec-30e8-9c8c-a00f48e4398d | -5.77799 | -44.12617 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fa81c7bc-c5a6-3e63-aba5-f09147bd731c | -11.20773 | -46.084 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b8521431-dfc8-3b33-8964-a76294b5fd66 | -8.38063 | -45.76463 | 2026-08-31 16:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82f1dcff-cebb-3e45-9c8f-6740c424deb6 | -11.22895 | -45.14381 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4754057f-f31b-31ac-a9da-7de9eaf9e892 | -10.46823 | -46.54938 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 3025bd5b-79db-3c7c-b6df-400fd39a8f78 | -8.16714 | -54.9287 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4c28c3c7-96e0-390b-b798-9b4e30b6c2c2 | -9.18888 | -51.56002 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 0cd5ae26-5a88-3bf9-96e5-7c2c9e1edf48 | -9.22646 | -59.58064 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f015533c-a7cb-3552-afc0-0ce5de924614 | -9.99907 | -46.39735 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aeac7bb0-08aa-32a6-92b3-f6e5a2b0dba2 | -7.0092 | -45.45753 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18d9294d-9e2c-3e18-94ea-40bbd8f43298 | -11.32129 | -45.20067 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d6a1149c-15e1-3a45-90ff-ad5361e6a262 | -10.04097 | -48.68243 | 2026-08-31 16:50:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 65b4febb-b745-3f53-af90-e374c50d2ed1 | -10.84902 | -45.34785 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 65f195d4-15f2-3820-b9fc-d53cf0bd8300 | -10.79102 | -50.51008 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f19a7b5d-0357-32db-a2a6-7522bfd9463c | -7.95068 | -44.25605 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c8201357-19d1-33bf-b87a-834ffaeb6595 | -11.24213 | -45.11237 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d67a5eda-69b8-34da-bfcd-26783e6621af | -9.78486 | -46.61526 | 2026-08-31 16:50:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d59202e5-df17-39e6-86f2-640d6cc2708c | -10.35328 | -49.97439 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2d26445d-d048-3668-b8cd-ef2762287748 | -8.8303 | -50.60007 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9ad5bd4b-164e-35db-9093-7724dbb3c084 | -7.10273 | -45.78484 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f276991-817e-3ef9-a0c6-9abe082a22d8 | -7.36029 | -55.18763 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 30adfe54-f8a7-3534-a5dd-cbad8e6b5bda | -12.90521 | -45.84501 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4019fd74-c033-35ee-be19-89d37db90d18 | -6.98387 | -45.3946 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee814d12-adbe-3032-919f-13c9e7d7949a | -13.30055 | -51.59404 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9f00847e-48ee-30bd-ba8a-e53bb93c8675 | -7.91394 | -44.2516 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1b1c6069-39e8-3d26-8634-f692f5a22b60 | -10.86051 | -45.3751 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 74289a38-800c-3bb6-a838-aada24788f4d | -10.12965 | -45.89774 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77e417a5-79d6-3ea5-b3b2-081b05524d69 | -8.82918 | -50.59256 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| d77de353-eece-36c1-a64e-2d9629607f0c | -8.81221 | -62.50061 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 93547db2-0b10-3114-ada3-321422291be8 | -5.07168 | -42.73581 | 2026-08-31 16:50:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7eb7d274-8936-3435-bb74-b585f4ffaf7b | -7.02617 | -45.86102 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fc87980-f8c6-3241-994e-6457ed14bd29 | -10.15115 | -45.69062 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a05284b4-c0da-308b-adf9-6670da20fcfd | -7.6296 | -56.7659 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0f865438-4da4-3266-a41f-83ebf74064ac | -13.46451 | -57.0401 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 8bf2941a-e336-3fa3-80d9-1f2d2f11454f | -7.02246 | -56.53922 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c80f5b1f-0da2-3613-8e75-67c76f7b56b6 | -12.09736 | -45.00319 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 8cd431d2-ff28-3d66-a695-463de433afe3 | -12.09952 | -47.14604 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 15c2e2d7-8c74-3731-82b0-1e9469301c51 | -10.08078 | -46.62808 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1d2bf76a-199c-34a8-b6c3-f9bdbaede251 | -5.80575 | -43.64423 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c3280054-a12f-3845-a6f7-5a63b3583c54 | -8.92618 | -45.03627 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2ea1f7db-8351-35bf-bd26-ef50e471eda8 | -10.1117 | -50.30544 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5dc767dd-6230-3b7f-87b4-3df0a430210e | -13.9651 | -54.41214 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| f053adaf-438c-3238-aa4b-f64733b0575e | -8.13348 | -45.57815 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4c499e5d-8465-3ff9-abc9-6681dc6dcd31 | -11.35196 | -45.23306 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dffb296d-c9b5-3d46-b6e8-e672738d8b9a | -12.09525 | -45.0576 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 600b02ec-44c5-38dd-b0a0-ffa577f8c532 | -8.13121 | -45.58707 | 2026-08-31 16:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 83191a78-be90-37f6-ab5d-b8acce310d09 | -11.32365 | -45.17049 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 5b70166f-019a-3f1f-b742-1ae5247e3f1b | -11.21478 | -46.106 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2abf303a-5efe-3435-87da-9f28bcac815d | -13.42624 | -51.69371 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9827e366-08f4-3c8b-b4ad-76b5d8218437 | -11.37565 | -45.19978 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4c7db4ff-54f4-33f5-9d13-66e57eac902f | -6.61495 | -51.93514 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1afbb515-a2cf-30c8-a932-bfe07a6accfa | -11.22455 | -45.09403 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 49127fb7-e1a8-313d-a6d4-cc00d766a019 | -8.77094 | -46.45666 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9884e827-9a81-3315-b48a-b50fd425e5ad | -12.78981 | -46.46164 | 2026-08-31 16:50:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a1819af7-4924-3e71-89a1-82f5e007c69d | -12.08118 | -47.20348 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d3430bcf-e5ad-3dde-9df1-f41f1c5857f8 | -11.57665 | -47.71646 | 2026-08-31 16:50:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README160.md)
