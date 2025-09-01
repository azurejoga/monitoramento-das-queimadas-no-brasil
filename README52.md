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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8949504-23cb-37eb-9849-a9a4d0f9f019 | -7.06833 | -44.34401 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7d4619b8-5894-34d3-8eb7-f82df48080ab | -6.81621 | -43.34083 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3fd3bca-119c-3395-918a-fe225ac81d16 | -6.80156 | -52.81608 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 658dfeac-ae8f-316c-8885-f3a5609591e3 | -6.30113 | -43.62777 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 635d39fd-a886-3d83-904c-8240dcebf09a | -6.71385 | -42.25373 | 2025-09-01 04:32:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8798c893-c084-3ec2-807a-6c20497f74d7 | -6.46115 | -42.42086 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d3abc8ad-0618-31c2-b195-8ccfe42270db | -6.85743 | -52.79893 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df865198-f7ec-3249-a34e-a5ea280aa9dd | -7.25231 | -44.0677 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2fc5278-1e58-342b-a62b-b022f9f0968c | -9.63668 | -47.81448 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1046de76-d234-3e87-80eb-d93a7efb8445 | -7.73427 | -50.25727 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06cce689-9e61-3f80-985e-6bd0faf8cb57 | -8.82594 | -47.83089 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88b268ab-41ea-3ea7-b384-445c1e7157ee | -8.82977 | -47.80636 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06f1dd5f-e636-3a7b-8b2b-6c8bce3f3be4 | -7.41518 | -47.43021 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b80542aa-ecbb-3a78-9897-457e8127b284 | -6.27473 | -43.52775 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3af49ad-4993-3362-b76b-2e3c3da54e3b | -6.92717 | -45.56727 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff8e001a-b185-3305-96ea-96e24e94fcfa | -6.83243 | -52.82675 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 530e51e1-828c-3c11-9f7d-75148cdf4154 | -9.14429 | -45.19857 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edc0ac9c-f989-3f6f-a0c5-4c42e8acdd6e | -9.66895 | -47.04741 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e5cba60-ef86-30c1-a93a-666d6e079561 | -8.87305 | -47.94256 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 911a828f-287d-31c3-8f5f-babd2e914ff3 | -6.84777 | -52.8081 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac2cfb39-3edb-303e-9878-a9ee84cd12b5 | -7.56102 | -45.70213 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d6c387d-cb12-3c39-a8f9-99bd69291e4f | -6.26936 | -43.54951 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f3cf3cc-0abc-3123-9515-a913bc2b5c3f | -7.59083 | -42.68776 | 2025-09-01 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5e7de111-8d24-355a-98dd-ac7380386eb1 | -6.18032 | -44.14576 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2261f831-9ce3-3ae5-a61a-81b8786c38ac | -6.15306 | -43.32829 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa852994-eebf-39ac-9efe-dc43b4c24a10 | -5.3308 | -47.49055 | 2025-09-01 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e20adba3-8338-3541-a961-3fa71befe3fb | -8.84743 | -47.51694 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00867bb5-b1a3-329f-88a4-e2a6877f29be | -4.15436 | -46.78519 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6aefea-43c9-3c08-adb8-bc533f61010e | -6.26937 | -43.53703 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b516b07-33ed-3c61-ad07-87c26156f64a | -6.85004 | -52.81898 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0138809-cda1-3583-b573-0d93da14a5b6 | -6.98151 | -43.12083 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13f0e49b-3a92-34ca-9ee0-db186bfe07d3 | -7.95356 | -46.44962 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 435bee0e-26dd-38e7-9b5d-ea0a09ef9e08 | -7.1063 | -45.34249 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14e7aa85-7c98-349c-80ee-653e766093fc | -7.94958 | -46.45278 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c6c6d86-523a-3fb5-93cd-5b668e5a54fd | -7.71591 | -50.26614 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde7e9c0-0a27-368f-bec4-2ff2b34b795c | -7.55812 | -45.69771 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7eb9f683-0cbd-3829-81dd-42f7c9b5ed24 | -9.12552 | -45.19968 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46b0d2f1-5bec-3375-90c0-25b33ece63ff | -8.8475 | -45.72988 | 2025-09-01 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15ae365e-257b-36c4-acd3-58401eeeeaf2 | -3.81048 | -48.95143 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ade3cbb-4828-362b-930c-d20cf1155e93 | -6.4948 | -43.56746 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44cdeaa9-9436-37b2-9b0f-ae09a2985754 | -6.82846 | -52.82609 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1f757c13-b350-31c5-b28c-4d67dc1e5b8c | -8.83031 | -47.80285 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7311f4d-3b35-3be2-aa71-c09e198f14fa | -8.82262 | -47.83036 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d15beaf-4dcb-3469-a09d-71f6709ca22b | -7.69128 | -61.48024 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6301693c-abf5-32e1-9562-c59afd0bc79c | -6.92368 | -45.56674 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18ba8e16-fb5d-3cc5-96e4-ba78ae4e008f | -6.79949 | -45.69106 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9823354a-b45d-338a-98f2-596df92de6c0 | -8.87691 | -47.93958 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c76f8171-0862-3108-aa0b-5732274aec40 | -7.07512 | -44.34948 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2071d9d2-e073-3c2a-a31c-aa4cacc5d1f7 | -5.83462 | -46.13358 | 2025-09-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7a7a21b-db26-31fc-9597-36e13b410be0 | -7.87326 | -45.17446 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 587a3075-7088-367e-a41e-a6fdef00cfae | -10.60675 | -44.33204 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 8b59370c-05c0-3992-810f-51e0b158b85b | -6.43348 | -55.62111 | 2025-09-01 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ae168b6-9d1d-3f04-9b3e-56ed551055ad | -7.14713 | -45.14265 | 2025-09-01 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b040e00-ca31-3e78-b7c1-e23eb27f03b0 | -6.82053 | -52.82466 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 83025b22-8f56-3e04-a1b5-978224020c2f | -5.61527 | -45.14099 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b779544-6424-3afb-a8d4-fe0c16e17294 | -6.3358 | -42.54092 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7b7b891a-03fa-3120-939b-65d8f2224127 | -6.30185 | -43.62292 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1e10e40-b50a-347c-89eb-7ae9a314e734 | -7.76279 | -50.32042 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7790f8b-cedf-3552-88da-b5ae53fe3c87 | -7.6318 | -44.03426 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af846c9c-f15d-39d8-ad55-ef378a5647d3 | -5.73357 | -45.3811 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4de415cb-f272-3ff8-88f3-7040ad5b1a98 | -7.72398 | -50.25983 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d56d796f-0216-3d12-9b89-4067f032b382 | -7.67128 | -61.09142 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8072b2c2-3a21-3b75-aac7-56123fda0e26 | -7.7634 | -50.31664 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44ec64b2-61ff-3029-9187-fc0df2033408 | -7.23783 | -44.06096 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b80309c1-3f30-368b-9e4d-bc0cb68cd3b1 | -9.23929 | -47.06431 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13be7c22-f831-3539-94e2-f57a51c6fc0d | -8.83408 | -47.51485 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61c087ec-c77b-3465-8672-6e84391de04c | -7.07139 | -44.34895 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d9ddf94-3b5b-3e21-bae4-80daf415e55a | -7.08629 | -44.351 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| b38fdded-7313-39d5-888a-6def7c6aff02 | -6.27603 | -43.53069 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 963f74aa-9046-3e02-8a6f-d43be0aeb9a4 | -5.82728 | -51.37817 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e2e52e0-a5be-317a-bbf5-f128e67fef26 | -6.86223 | -52.79453 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2828af2b-eeeb-3cd6-8832-3a6215c57e4f | -11.03267 | -45.14128 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d239e17b-03e2-3aba-85da-04ff9a7ade50 | -7.42156 | -47.43149 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad29c41d-e3af-3419-96d4-ba936be8c2ac | -10.66828 | -46.26178 | 2025-09-01 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15cccea0-86a0-3fc9-895e-c7e2a2215b91 | -7.09096 | -49.92212 | 2025-09-01 04:32:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b8d4754-0413-3c38-9e35-9cf164e3cbe3 | -6.80008 | -45.68722 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0d38efd-cc65-3459-bb0b-624306ab5dae | -7.69813 | -61.4815 | 2025-09-01 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c8aa941-4f97-3a94-8be7-c793aa833eeb | -4.91694 | -43.1842 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7be04502-4c51-3901-acdd-953607bdb37b | -7.46302 | -44.8267 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6e08e3-d0c1-3d15-a9ce-8e9ca86eeeda | -9.64548 | -47.81942 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92da97e0-4808-3f4a-be50-47a7e5bbbb70 | -4.04428 | -48.9362 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef5e5831-b534-374b-9caf-d30d426e0fe1 | -8.49807 | -44.7444 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ef1b625-a3b8-3f63-ab5f-495ea71fe591 | -10.0413 | -48.11292 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfe79455-40a4-3354-b416-2c641cd30928 | -8.16771 | -45.03479 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8671a33-015d-3715-a00a-ec89a443cd60 | -4.91765 | -43.17931 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cf1335d-c50c-30d8-a877-0926758ee3dc | -6.76787 | -44.82998 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a15c7c36-cf7a-38f2-939c-2bcfc8020038 | -6.50299 | -45.41021 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd8bb974-998c-3128-8024-420dd8d17efe | -6.81079 | -43.35025 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9a426d1a-b956-3506-9092-a7c224d207c1 | -10.60286 | -44.33147 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 2d5bd01d-b630-3352-b451-19726f789bc0 | -7.65997 | -49.85025 | 2025-09-01 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4735337-9dbb-352f-96d2-9dd67f729e1d | -10.03743 | -48.1159 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41e0294b-ca26-3c1e-b471-2faf1ed83558 | -6.40951 | -43.62565 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c808182f-57a8-34f3-bf2b-67350607b607 | -7.10528 | -44.84559 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81d9138e-8cd0-3d86-820d-2c36d62e5552 | -8.84294 | -47.50177 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db2adf3f-803c-3eb6-9ac9-8c619a202be4 | -6.30325 | -43.61346 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ac591b4-532a-3da9-ba48-37140ab7d096 | -6.56668 | -43.66704 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3035fad-d6e9-3ead-886c-cbe297973290 | -6.80554 | -52.81672 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5e2caf4-a281-3258-a34e-4b426cb2cf9d | -7.48939 | -46.71176 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a3e8589-3584-30ec-ac97-cf065c98d0bb | -8.84737 | -47.4952 | 2025-09-01 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd091819-2a35-3181-8620-7dde6633531c | -6.4955 | -43.56264 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
