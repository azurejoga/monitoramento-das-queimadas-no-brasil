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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6a89b14-bd48-3492-8699-89c089bff391 | -6.53525 | -55.15748 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cf56705-b4d4-395a-a49e-43783d1e0fa6 | -6.42103 | -55.79579 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d4e6123-92dd-32e6-a669-7a6489a1fc2c | -11.5579 | -47.70999 | 2026-08-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 400d78f0-617f-380a-84e4-852633dd0e14 | -10.8819 | -50.15538 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4deec1c-8767-3eb6-bac3-9d6e95df0dfe | -4.28333 | -48.03833 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c312367-892c-35bf-9f4b-f517aa7049b5 | -10.91483 | -50.42717 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40b5942d-7b81-32e5-8031-17326c277db3 | -6.00091 | -44.70107 | 2026-08-05 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88976978-1d8c-38bf-ab13-2bb34d37243a | -6.89552 | -42.41987 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8493076a-bd79-355a-bd0f-01c89458695f | -4.37056 | -47.77214 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7df32605-9617-326c-a830-0be53b4dd991 | -4.36762 | -47.76758 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a6566786-1a0a-302e-bbba-3fd2688c7728 | -7.15316 | -44.71907 | 2026-08-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be9abdf2-cd5a-39c1-89c7-17a0da8e41e0 | -9.48388 | -40.37008 | 2026-08-05 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4802ef12-1944-37d3-9321-ddbacfbcf4ab | -9.60891 | -47.76755 | 2026-08-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14a74b7d-57e1-3b51-8b23-d78d639b0ea9 | -6.54585 | -55.16383 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01736f4d-e839-3d7d-8b89-5a7653f4c1c4 | -6.01785 | -46.51261 | 2026-08-05 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9800e2bf-5c19-3c6e-9e0b-f0c32806f059 | -6.89681 | -42.41061 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ca9ed3e-73e8-3a1a-9ee1-80252be88fb2 | -6.24437 | -47.147 | 2026-08-05 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2d8a9ec-3080-30e2-8171-8f7fa7fd0869 | -6.5557 | -55.15125 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4448ee9b-80a4-3062-9254-509e4a3680b5 | -7.74491 | -45.05227 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e73594b7-9034-3173-a320-dbb14ecd6b10 | -7.74477 | -45.0505 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3d2ef502-e0f4-33ab-a757-bd3d76322c76 | -10.79325 | -47.70536 | 2026-08-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8edf19ca-6919-34e5-99e5-d4d60bc918c6 | -6.90115 | -42.41751 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 09ecb5df-b8da-3186-90de-6bc257938b4a | -9.60444 | -47.77169 | 2026-08-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5e18bee-dbcb-3baf-9c25-a459125d284a | -11.04698 | -50.43205 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c21f600-b9e7-3557-a9e4-d9586cb246e1 | -6.58437 | -56.53696 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b90da3db-25e5-32b5-b735-966579d72907 | -4.04683 | -48.09481 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81b3dfec-f6e1-376c-884b-fd14ac8c953a | -6.55342 | -55.16509 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d88633b9-de63-35b0-8e3e-a867c7366d46 | -10.60853 | -52.22381 | 2026-08-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deabf26c-09a2-33cf-b45d-5a9bc2515d68 | -6.56787 | -56.53431 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1554c125-903d-34f9-a0f4-d6846264ee9f | -9.84358 | -46.8082 | 2026-08-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d6b3add-703e-3cc7-a7ca-e12ac0e1e82e | -10.75439 | -42.09318 | 2026-08-05 04:46:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d7872039-05c5-3d9e-ac17-b99a5862a61b | -6.54057 | -55.14887 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f65b9ef0-fbaf-30f9-9079-93db58479d0b | -9.16968 | -56.94655 | 2026-08-05 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f6e2fa5-2be7-3ebe-9cca-faa4aaa073a1 | -6.65274 | -43.9059 | 2026-08-05 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 211a8574-a5e4-3e8b-8154-1cdf4374a05e | -4.05541 | -56.23159 | 2026-08-05 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 713628ad-97b4-3548-accc-3be132c63a55 | -9.14777 | -49.66357 | 2026-08-05 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41b2805e-69a3-34ea-a235-71a6fb6f9712 | -6.90245 | -42.4082 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2bfa5325-9b4f-3f44-95a3-d62a3128a4f2 | -10.88532 | -50.15591 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a24d231d-5feb-32d2-8814-b5c71d739698 | -6.71721 | -58.9437 | 2026-08-05 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9371b4f7-1235-36c0-b73a-cd7ef54eace9 | -7.22486 | -43.35183 | 2026-08-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1ab7c971-299e-34c2-8648-7f8720816678 | -10.45786 | -50.22896 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62b9c250-365d-312d-bc17-a49b84d854ae | -6.55721 | -55.16568 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 639b0af6-a11a-3699-835d-dc190f72f5f3 | -8.66122 | -54.97028 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75f85595-15a6-3ce0-a4bc-4c63a01439d3 | -6.64737 | -43.91015 | 2026-08-05 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55e7733f-5a7c-37b1-8d67-c4f78df6bcbf | -6.53904 | -55.15804 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c233b347-f01d-3817-ae67-bcd278c46b06 | -10.27147 | -46.35625 | 2026-08-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a808fc4-38bb-3fe0-b332-2e427ea57caf | -9.14378 | -49.6668 | 2026-08-05 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96f4d779-9d70-3e67-a8de-2c24ea52f7e0 | -8.34559 | -45.97589 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36c76e64-3e5c-39a1-b74b-1b5f63642519 | -6.54964 | -55.16446 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86be0189-0355-36cd-9f33-006bc740ed03 | -9.16748 | -56.93508 | 2026-08-05 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81dcfda1-4d6b-35c6-841a-8edaef2c9788 | -11.2983 | -44.78675 | 2026-08-05 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afd80d6d-61c4-3a00-a2e6-5c5a4bc10c0e | -6.55116 | -55.15523 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb6731fd-46d5-339f-bf9a-a34dba2ffcec | -6.55949 | -55.15182 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45cbbbd3-5bd5-3218-aae5-851034dd851f | -6.54662 | -55.1592 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c0c6268-3814-33a8-992d-a2c629f652a9 | -7.36292 | -49.5535 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3bb8927-08aa-3687-bd86-356decd57f67 | -3.99488 | -48.39577 | 2026-08-05 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 471dda3a-28cf-3196-8dbd-8ce2034f8d2a | -6.90158 | -42.41444 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fcc53fee-e199-3ae4-9a38-b5f2f5ddd298 | -6.56482 | -55.14306 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d0c857d-34fb-3fba-a6c8-e3eef471ca44 | -11.55012 | -47.70877 | 2026-08-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cf68ac7-71c5-36d1-a9c1-abdfe4ed3a9c | -7.50241 | -49.74666 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 081867c7-5616-31e5-991d-6152f17af46c | -6.57386 | -55.15886 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e53dfd50-2bd9-318f-b966-86e8d91b533d | -4.4609 | -47.91542 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 48a7a89d-95d8-3d48-95ea-43a895d3203c | -6.90072 | -42.42059 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 43683784-dd77-36f2-80da-982edc0be6a1 | -4.36701 | -47.77159 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0afe4f77-063d-3f43-a503-c6a216600f20 | -6.42184 | -55.79076 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a3c3585-d0dd-3243-81c3-b09cd079225a | -8.34143 | -45.97523 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b65fdb15-07ef-3299-9309-fedf759dc39e | -11.30166 | -44.79756 | 2026-08-05 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c9326ba-a446-3012-a3bc-884a36dcd851 | -8.66051 | -54.97457 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c56039f7-e75b-386d-b4da-bf42050611ea | -6.55643 | -55.17035 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6d868a1-c078-35ef-a4ae-148257f677db | -6.1277 | -49.32736 | 2026-08-05 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 956395c3-c122-327f-93cc-5d5bd7146914 | -6.57008 | -55.15824 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2f39b3b-5337-3205-b1cc-3b7aaa410b3d | -9.88158 | -58.44117 | 2026-08-05 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da2671e0-3f49-38c3-b2d5-c4078a5508c9 | -7.00716 | -45.85314 | 2026-08-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83de2894-51c4-379b-8dba-b850d93c55af | -10.61347 | -46.37798 | 2026-08-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef9914c-5dab-36f2-9d51-b22cb9b66047 | -4.27983 | -48.0378 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6ebf629-ff49-3c7c-bc2b-d1b6ee410152 | -10.78618 | -50.89885 | 2026-08-05 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c5a993c-4a7e-3cf8-92bf-aec02227ead2 | -6.90722 | -42.41204 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92731319-9505-3d4c-9d14-b709e2e54d9a | -3.81998 | -50.63409 | 2026-08-05 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad81be84-26ef-3f60-ada3-a46887da6145 | -10.88589 | -50.15215 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f190132c-3b75-3bea-bd0d-065737d55acc | -5.93383 | -46.35155 | 2026-08-05 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0e97728-0edc-33c2-bf3f-b86b9f938cb7 | -7.17794 | -40.17241 | 2026-08-05 04:46:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a99ad373-d64e-3e6b-b011-a8e0a2906917 | -6.4208 | -55.79357 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5114bbc0-c48f-3fd0-aa1c-ccf6bb7c860f | -7.36687 | -49.55034 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f66262c-78c0-3ce6-8d5e-58b5a79c3b43 | -7.00662 | -45.85693 | 2026-08-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13e9b4f9-633f-3dcb-9c95-22d30f7bdbd9 | -8.94668 | -47.61294 | 2026-08-05 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7026c3c-01f1-33c6-9ef9-588398a213cb | -6.4775 | -42.22641 | 2026-08-05 04:46:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ab05b9f-19a2-3439-8fa0-4a42bfb36628 | -6.89637 | -42.41375 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 606513fb-b273-3576-82c6-544f641897ca | -6.64953 | -56.41957 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9a0915e-a578-39f6-8c2f-58bd11d19a5b | -10.46071 | -50.2332 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc59f72c-7356-3c94-9202-8034696f1b84 | -7.67835 | -45.95917 | 2026-08-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eec5d786-ec9c-31fc-abfd-cd4c557f72b4 | -6.1472 | -47.17616 | 2026-08-05 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2db31b08-156d-3f28-8101-1846d272e3a6 | -6.5849 | -52.21862 | 2026-08-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 59dcb358-58fa-3b24-81d1-570bca528b31 | -3.99449 | -48.39493 | 2026-08-05 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23452a30-1f0f-348c-989d-1107ffcc5ff5 | -11.29426 | -44.78102 | 2026-08-05 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87fa8787-979b-33a7-9685-73d614391667 | -8.34033 | -45.9829 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be6406b7-b0a5-3d8d-a719-0f4866aad8a2 | -6.55268 | -55.14605 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 13879d73-7eb1-3101-887c-ceb5d6e42ad7 | -7.62718 | -45.31545 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3d169bf-abe5-396f-9995-d0ac0d1f9422 | -6.65423 | -56.4166 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f2d95c-e7b0-3cf3-9ac0-e654d93ff0aa | -7.22385 | -49.5928 | 2026-08-05 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347e7e6b-5296-309a-83b8-4ac715faae69 | -7.50296 | -49.74302 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README14.md)
