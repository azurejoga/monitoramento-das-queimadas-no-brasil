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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90a294c2-0cce-3988-a17b-7a108d78a9fb | -2.81652 | -54.12523 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e8a9b204-c775-3bd2-a340-c43b087745cc | -4.26602 | -46.3665 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| f0ad0771-343c-3e04-a1b2-0f8cd2cfb6d8 | -3.15848 | -53.07155 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada98d1c-67b8-3655-85c5-d369f353521b | -2.82168 | -50.50293 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3cd7294-c35c-3020-ae6a-d659ba14947a | -3.00497 | -53.87868 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66bee121-e209-35a4-9ad8-c775f7b0cf11 | -3.08206 | -49.54189 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6216d2b-66d3-3421-aa01-909ecdc74d75 | -2.99099 | -51.04301 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b199268-f3ba-3d3e-99a1-cae62ced7511 | -2.92732 | -54.10519 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0136ebb-78e5-37c2-ab0f-cb388bfdbaab | -2.75093 | -51.54996 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef729a74-a023-3629-8533-d876971b46cc | -3.1209 | -53.72546 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 25aed478-932c-3823-9afc-cec5deebf7a7 | -3.70493 | -50.65546 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03efcce9-59a5-3900-a514-67ddb0232e49 | -2.58957 | -51.84799 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1b336010-47a8-3bed-9ba4-dac2dcbd797b | -4.12626 | -46.82558 | 2026-10-04 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d58bbe93-a590-3933-9a36-6c9c9d4e6362 | -2.98056 | -54.09814 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50392594-de61-32fe-a8e7-91d2fa006b15 | -3.70353 | -50.66395 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 773a9b15-8b01-363f-9005-92925863b3d5 | -5.78065 | -50.20407 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83075735-adde-3bf8-8577-11b845fa91da | -2.97588 | -53.26469 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51688792-42e1-3675-b92e-481029ab90b1 | -2.21723 | -53.70842 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d049388-085a-3aab-86c0-052ebd291372 | -3.1295 | -53.7416 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaa0c0d5-be13-39ac-83dc-a023db957841 | -3.11675 | -53.7506 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 589cbd50-1d68-3f61-982f-d80cc57be333 | -3.77118 | -51.86207 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e211de4-f897-3ed8-bd6f-24431f834e0f | -4.20512 | -53.45736 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df99b3d3-2ff1-3e9d-8187-23b49b84d841 | -1.01649 | -48.79856 | 2026-10-04 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c76730eb-add5-318d-b2c6-c32cc0bd63a3 | -3.08148 | -49.54559 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08dfcaf8-b82d-3761-9f32-4eca9f9a48c8 | -2.25824 | -51.93806 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2199a376-fc45-358c-8b2d-2e3166d3cf2d | -5.99887 | -53.55243 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1f12384-9c77-3694-b384-ee255d539108 | -5.96026 | -55.34728 | 2026-10-04 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eff0dd4-4260-32df-aed7-23d8cc5bf457 | -3.52183 | -54.61904 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1903a484-995d-39cd-918d-9761ea1040bf | -3.1301 | -53.7028 | 2026-10-04 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fb76a42a-b4dd-3eaa-8b16-17b8490bbdfb | -3.0721 | -49.5313 | 2026-10-04 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0ff5ecf1-d037-38dd-89ad-f61148293629 | -2.8164 | -54.0929 | 2026-10-04 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d9be60c2-dbcf-39e8-a32b-dfaa4f27477d | -4.2888 | -50.2465 | 2026-10-04 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 286.3 |
| 7c31ce3d-99d8-3243-8df0-aeb9579f829e | -4.2887 | -50.2675 | 2026-10-04 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 524.8 |
| 68b49779-bfe9-3c7f-85cf-662aacec346a | -2.5842 | -51.8623 | 2026-10-04 04:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8f286b2d-e868-383f-9382-34db1d360fe2 | -4.3072 | -50.2668 | 2026-10-04 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| bba1a1f8-6adb-3838-95c3-f9a97396d62f | -3.4762 | -50.0883 | 2026-10-04 04:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6060fa2e-d142-335c-8223-85f08a528175 | -3.1116 | -53.7234 | 2026-10-04 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 4a4a3021-95a3-3552-865f-2bda1461a13b | -2.5843 | -51.8417 | 2026-10-04 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8d7d4cb5-c6e6-370b-add1-65967d139155 | -3.1116 | -53.7436 | 2026-10-04 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 16595516-2acd-3b82-89ee-3e6a4acaa691 | -4.2886 | -50.2886 | 2026-10-04 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0958fc7b-8f78-3dca-b3ff-bab1b4825833 | -4.2702 | -50.2683 | 2026-10-04 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 335.7 |
| eecd8a85-21e2-334d-9cc7-426f04287ac4 | -3.13 | -53.7229 | 2026-10-04 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 6734d287-601a-3bd7-be2f-b4a4c54502c3 | -3.1117 | -53.7032 | 2026-10-04 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| e3973663-d1d1-325e-b0de-8e8c82c8e702 | -4.2703 | -50.2473 | 2026-10-04 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 73aaf1ba-f1ee-354a-9c3d-edb3c618a8d4 | -3.8757 | -55.7986 | 2026-10-04 04:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d28cbd13-b1af-394d-8c28-e7b4bce64bca | -2.7979 | -54.1134 | 2026-10-04 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2596c3bf-c41a-37bd-92e6-12ec159b8b5a | -2.8163 | -54.1129 | 2026-10-04 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| adc0d5db-0c44-32ea-883e-c3106ea28a84 | -2.798 | -54.0933 | 2026-10-04 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 7d2c8972-0dbd-31c3-932b-36f85f4ae5b0 | -10.2445 | -49.6539 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 820c8c94-d20b-389a-b773-967d9f1dbc05 | -10.24823 | -49.65455 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0276eed9-1f48-308a-8eb1-c3cc411e2365 | -9.50557 | -54.63526 | 2026-10-04 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7932142f-34ce-34a6-b774-bb5afb7f8913 | -10.24458 | -49.66195 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c8accb8-ad4b-3144-b123-e3e2ad6d51ee | -11.63006 | -41.83078 | 2026-10-04 04:21:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1377515-39e0-3a7a-829d-f804858de432 | -10.9968 | -59.15085 | 2026-10-04 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35dbdc9b-0f41-356f-9efd-8c96fb99e2ef | -11.72164 | -43.42747 | 2026-10-04 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88534dad-d0ee-3f6e-aad1-f7e39cd6aa9b | -9.23623 | -46.68585 | 2026-10-04 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8aa540c-f8f8-337e-9a0f-efe2d92f046a | -10.24536 | -49.65741 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e572761-1b20-301e-8870-e379820fc8fc | -8.54415 | -50.0693 | 2026-10-04 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3d7f46f-e4a5-3353-9d30-f2b7ccb7262a | -8.54362 | -50.07146 | 2026-10-04 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40e94d0b-5a8c-328c-b3f0-f6e741fd698a | -10.99262 | -59.13672 | 2026-10-04 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0891d2a1-0fa4-3cc0-b320-eb8cdceba236 | -9.70075 | -57.4576 | 2026-10-04 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcced48d-a606-3c66-a076-6eaaca217bfb | -12.18926 | -57.10398 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3d7bccb-7dcf-3777-9d9f-ea6e1f22feec | -10.24909 | -49.65805 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abacb1f4-cc9a-3f30-9527-06f51bf2f888 | -11.34801 | -44.85717 | 2026-10-04 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cd4937c-3d91-3eb2-a80f-a8e5b5c740e0 | -9.51141 | -54.63292 | 2026-10-04 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 955dac3c-636b-3d8c-a1cd-b14c3921efab | -9.51077 | -54.6364 | 2026-10-04 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56410cbc-21cf-32bb-a830-6e0cb10cfc4a | -10.35397 | -45.02526 | 2026-10-04 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81b68421-f312-307a-b6a8-6ffcdcc21078 | -9.69928 | -57.45417 | 2026-10-04 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bd6260a-e6f5-3652-ae7c-454496d69813 | -10.60018 | -53.96897 | 2026-10-04 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6971584d-bb15-314a-97cf-087e4a864b32 | -10.22274 | -59.08949 | 2026-10-04 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1224656f-0d01-30f4-a95c-0a85e3183a03 | -9.50742 | -54.62529 | 2026-10-04 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b0001247-df97-38df-b8a4-a2f974ffbb0b | -10.99137 | -59.14297 | 2026-10-04 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c49f234-c543-3c1e-9e03-b951261383e9 | -8.54023 | -50.06862 | 2026-10-04 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0204cbaa-1a10-3deb-a5a1-3c55b9ec8cfa | -12.55226 | -54.95195 | 2026-10-04 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4306f56a-473a-3271-9462-97e1fbd6bbec | -7.75371 | -49.20359 | 2026-10-04 04:21:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99c773e8-cd7b-3a73-a11b-6e9e9e31e0bd | -8.27198 | -47.8863 | 2026-10-04 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 315c2738-bdcd-304d-be64-b6826aa6d2be | -10.24987 | -49.65351 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 747537e4-f245-33b8-bc39-8e9cbc0b3626 | -9.7017 | -57.45261 | 2026-10-04 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41545166-f366-3fa5-9fa0-6b1d07b4c408 | -9.50402 | -54.61451 | 2026-10-04 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 739e07cc-1a6a-338e-97fd-b38fa1a49cee | -9.23566 | -46.68942 | 2026-10-04 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf9a0e4d-0bba-3bae-b2d6-de88f57564dc | -9.10118 | -44.28214 | 2026-10-04 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9ccba4d-a20e-34b4-aac4-74d7c72dc290 | -9.50681 | -54.62858 | 2026-10-04 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e642c89f-d7b8-3c90-ace1-94c80d130fe2 | -12.8142 | -60.49522 | 2026-10-04 04:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7435251a-1913-3ea8-b3ad-230684588364 | -12.19759 | -57.12323 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cf78c03-cd66-34ed-81cb-f42b5981a081 | -12.81696 | -60.49555 | 2026-10-04 04:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 815bbbac-2147-3d65-b8dd-c4d390e954f2 | -12.97701 | -41.17473 | 2026-10-04 04:21:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69b2fa86-dd36-3388-b8d3-cd7739e78278 | -10.85618 | -39.24597 | 2026-10-04 04:21:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 39ce7eee-7a28-3a9e-9a6a-c81dda6e2d2c | -10.9901 | -59.14933 | 2026-10-04 04:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 960b7d86-8678-3eb4-8dd9-6025f08b9078 | -12.18341 | -57.10285 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 301fa434-5f42-3370-9a3a-2370d9267c6f | -12.17756 | -57.10175 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 750b199a-bebd-36bf-9ea9-e608f280abc2 | -12.19842 | -57.11903 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 532d204c-154c-3778-a006-d24adbe0ce12 | -8.5397 | -50.07079 | 2026-10-04 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a41a404-ed90-38b6-bfcb-1f87b7410f63 | -9.50341 | -54.61777 | 2026-10-04 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51395796-381e-33de-8006-24fbcf31f712 | -10.35065 | -45.02475 | 2026-10-04 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffbb40ca-e198-3512-bc32-9dd82a0ae2b8 | -9.69978 | -57.46268 | 2026-10-04 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71ea9a9e-ad52-3c3a-9237-919aef0e2f20 | -10.25205 | -49.66325 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b35b68a9-dcc5-3d5c-aff6-44001612d01e | -10.24162 | -49.65678 | 2026-10-04 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad5c50b2-631a-31bd-9e8e-aa919c7c3794 | -9.69828 | -57.45921 | 2026-10-04 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb37ba87-300b-389d-8a6a-65f76ac0e5f3 | -12.1951 | -57.10516 | 2026-10-04 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d730c961-15a8-32e9-abc4-8505abf60892 | -10.74039 | -45.29882 | 2026-10-04 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README33.md)
