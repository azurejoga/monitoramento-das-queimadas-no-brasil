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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47a9bfba-c47a-3fc5-93f5-d7ace00f182a | -9.4578 | -40.3392 | 2026-09-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.8 |
| a11b2413-b9f4-387e-9e25-a532e2900d3c | -6.9552 | -55.635 | 2026-09-01 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c1a08307-ad8d-3819-a85c-5dff8ad7b13e | -7.5447 | -46.1115 | 2026-09-01 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f96daf51-49ff-3e2a-8771-4576689a0f5b | -6.6976 | -55.4091 | 2026-09-01 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b3bbcfdd-fde6-3a77-bc73-0fb5d8e45899 | -10.036 | -44.7056 | 2026-09-01 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 736d3cf5-2e0c-3d08-a579-d8354d9b6a1f | -3.8605 | -44.0355 | 2026-09-01 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6a002d45-bf98-3834-92a6-c8204509ccee | -11.277 | -50.5815 | 2026-09-01 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 18b1ebee-56a1-3cf2-ac0a-2f8629433064 | -9.4765 | -40.3613 | 2026-09-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| e0b4158b-0449-3dfe-b50d-358116c9b657 | -17.3914 | -42.3744 | 2026-09-01 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 811ae5c9-b057-3ef2-b40a-7d4681f6f029 | -6.6035 | -58.6166 | 2026-09-01 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 2071f540-07d8-33eb-af33-76db795ce184 | -10.0364 | -44.6825 | 2026-09-01 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| de32093b-1566-3638-acad-43d557616d69 | -17.372 | -42.3544 | 2026-09-01 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| cf813128-258c-37c5-bb50-a0273d8fd83e | -3.8603 | -44.0815 | 2026-09-01 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| b982e104-8ccf-36da-a491-35540afbeeed | -7.5709 | -60.4835 | 2026-09-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 94625cb2-83c9-333a-b4b2-196a464ff100 | -11.258 | -50.5836 | 2026-09-01 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ffc5b8e3-9b2b-3472-ba30-0cd84e3f5849 | -9.4769 | -40.3365 | 2026-09-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 940978f4-f3a4-35b6-893e-f367fcd07e05 | -7.571 | -60.4643 | 2026-09-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 359.4 |
| 5e2c749b-9a20-3708-a54f-a0ff107dabb0 | -11.258 | -50.5836 | 2026-09-01 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 2c25845a-6682-3a65-aca6-9d36b1b5f629 | -7.5709 | -60.4835 | 2026-09-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 222.8 |
| 63687c2f-ba66-3015-89d4-5b3d3e034f03 | -19.194 | -57.3926 | 2026-09-01 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 87a13d64-31ab-3be5-81ba-15a7b906b864 | -3.8603 | -44.0815 | 2026-09-01 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 6eac33ae-f6bc-381e-b686-7ae26e172d74 | -7.5526 | -60.4651 | 2026-09-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c5f5c8cd-f878-3d3c-9132-e0b7eecb84e7 | -14.4587 | -52.5151 | 2026-09-01 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ec6f687b-ede3-3f58-bd43-27bfe7336051 | -11.2767 | -50.6029 | 2026-09-01 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 9d1e1c19-3851-3bcd-9375-2a36c3ead576 | -7.5895 | -60.4636 | 2026-09-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 330bf5f5-50a5-3c98-a559-8c5fd6b5c2fa | -6.6976 | -55.4091 | 2026-09-01 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fc435b1f-5bf1-32b7-ac78-890c2c5d6366 | -10.2025 | -50.3109 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| cf21bb0b-33d6-3484-be32-0b2b4487a272 | -9.4574 | -40.3641 | 2026-09-01 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.2 |
| bcddc806-cb18-3a37-85e8-d1843db77510 | -9.4578 | -40.3392 | 2026-09-01 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 844fdf16-d068-3d16-bf19-de20a0ebfc38 | -9.4769 | -40.3365 | 2026-09-01 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.3 |
| cc19c4c6-55f5-308a-b2ba-5e9b6ee1f8b0 | -10.1837 | -50.3128 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| d09b922f-3de5-3b74-aed1-0f79e0faeb37 | -17.372 | -42.3544 | 2026-09-01 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fa82368e-9fcf-3d93-ab09-9ba61363cbad | -11.277 | -50.5815 | 2026-09-01 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7bb3eb2a-b7d2-32c4-b46a-88ea4deacabf | -6.5851 | -58.598 | 2026-09-01 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 657973c0-cb12-30c1-8810-59b880b1b3a8 | -10.036 | -44.7056 | 2026-09-01 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| bfea21c5-dc64-3cb0-a61d-db0c9af4aeef | -6.1844 | -57.7395 | 2026-09-01 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| faeec5b4-23b7-30eb-a75c-15ebd33b4a3b | -6.6036 | -58.5972 | 2026-09-01 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| c99aa263-5faf-30e9-8649-fbc795b5cbab | -10.3574 | -50.0171 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7519b2a7-019e-3934-ae06-b8f057ca4c7c | -10.0364 | -44.6825 | 2026-09-01 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 74a473ec-40bd-3315-bc05-f4490fcf7625 | -3.8604 | -44.0585 | 2026-09-01 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8a6157c2-9c0a-3ec7-bddb-c5e616cb27a5 | -17.3914 | -42.3744 | 2026-09-01 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 72895a02-9f61-3be2-a694-2db187e5ac87 | -11.2584 | -50.5623 | 2026-09-01 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ba9b8da1-550d-33fa-927b-775894f4e707 | -17.3921 | -42.3495 | 2026-09-01 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 74586d0e-bf9c-3973-b95a-011404ff69d9 | -10.8818 | -45.3534 | 2026-09-01 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e996da0d-9677-3763-9497-035f97f02702 | -11.2957 | -50.6008 | 2026-09-01 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| ca8cd4bc-fed0-3bcd-a653-3f1314b02ad7 | -10.2209 | -50.3517 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6dc01ee7-0ac3-32f4-b84b-65580c1631b3 | -16.0547 | -54.3908 | 2026-09-01 01:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| dc3333f8-5abd-3ddb-937e-ca26958ce131 | -10.8627 | -45.356 | 2026-09-01 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cb9b90d5-876c-362e-848f-7e245a8bf5dc | -6.9552 | -55.635 | 2026-09-01 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bce95720-e2a3-3ae6-b403-de23f46440f5 | -3.8605 | -44.0355 | 2026-09-01 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 05a78892-d1f7-332a-af34-daf76290e6a7 | -10.2023 | -50.3322 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 09e88e45-ccce-36c9-b8d0-d72de9fa5bb9 | -11.1126 | -51.5114 | 2026-09-01 01:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f000ab1f-ff15-38a6-aae0-8f9e8030a1d6 | -10.1839 | -50.2914 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e923c8bc-273c-325b-92b8-13447a66d5ff | -7.2005 | -60.6897 | 2026-09-01 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7a0a5c03-8eb1-33f4-b819-23e83bc01907 | -7.5894 | -60.4827 | 2026-09-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c005d62e-b621-39f5-a75a-bee888207290 | -6.6035 | -58.6166 | 2026-09-01 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| dbff3fe6-24d1-3be0-8c48-382a260b8476 | -10.2212 | -50.3303 | 2026-09-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 56f310f0-6df9-37ea-9588-2c6b83d198dd | -11.1315 | -51.5094 | 2026-09-01 01:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ba61cbd6-f0c6-3cea-b0ff-d7ae8b9a8587 | -10.5015 | -59.599899 | 2026-09-01 01:54:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7df7dce-6ede-3ece-8364-9fc4851cae9c | -16.0651 | -54.375198 | 2026-09-01 01:54:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1057940c-38a1-3497-b3d1-0e00d0b5bd52 | -9.3212 | -68.877403 | 2026-09-01 01:54:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1054681a-125d-35c4-93b9-c710e4be19f8 | -19.207899 | -57.318501 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca1b34bf-3e77-394c-954b-f11667854d85 | -6.7097 | -63.178101 | 2026-09-01 01:54:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ddd248d-0a10-32ef-93ce-bc78921dd843 | -9.3228 | -68.884804 | 2026-09-01 01:54:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 22556935-c561-3122-95ce-27e494acb951 | -8.2707 | -62.756401 | 2026-09-01 01:54:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7369e17d-d45a-3ee1-87d9-cba2e6c84c84 | -7.5676 | -60.454899 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 011f3c22-e639-3072-837c-75f5165e11c8 | -8.9355 | -62.3437 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd8003c-123f-3ae0-8fd3-26b833a470fc | -8.5834 | -66.967903 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a79b8c9-5285-366e-9167-8c4fe9f49a88 | -8.719 | -67.111 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cbf26e6-26ab-3f44-80bb-4b3b62bf4d1a | -19.182899 | -57.341702 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b666222e-3ab6-3d60-850b-8f0197d92b23 | -7.1866 | -60.6661 | 2026-09-01 01:54:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fedc3b4-45c2-3df9-8304-23b7a884901c | -7.9145 | -61.325001 | 2026-09-01 01:54:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1e1c83c-274b-3ff0-ac17-27d946d0bd2e | -9.0073 | -67.7938 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e83d7776-8532-320c-84ce-232bba75e61b | -9.0052 | -65.4356 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf915465-6008-344a-97f5-032c7423117b | -8.935 | -63.289799 | 2026-09-01 01:54:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7cdb31ee-a926-38b3-bb9d-aeaa36bd0524 | -8.6077 | -70.210297 | 2026-09-01 01:54:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c1cb79c1-6571-302f-a4c4-d6c15c0bd9cf | -7.5745 | -61.368801 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32338696-619f-3493-b0c0-904715915741 | -6.8151 | -59.076698 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a300e2e-3696-3715-b538-2ab8143d6626 | -7.3515 | -60.581902 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 316fc710-70a4-3eda-a44a-2a6ee693130a | -8.585 | -66.9748 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6845385-02dd-3082-9130-1484d6f4a08a | -7.5738 | -60.4384 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa177bc-9fc1-3896-a604-8c92c37f9ea5 | -16.048201 | -54.3521 | 2026-09-01 01:54:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be26a9ef-782c-3585-9a55-4412d3105820 | -9.1528 | -59.530998 | 2026-09-01 01:54:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 860ae239-b3ce-31c4-8bdc-6052298178ac | -8.8858 | -66.892197 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bab01bd2-c708-3b0c-9b83-9e5fdde53b4d | -8.8688 | -66.772598 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca09dad-04c0-32b9-8775-546ae1287b47 | -3.1256 | -61.228699 | 2026-09-01 01:54:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f1aabd1-57ba-3c95-bf89-bed2cb27932a | -8.9448 | -63.287498 | 2026-09-01 01:54:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8af0574d-1bed-3484-891a-6717d8e46a74 | -9.0088 | -67.800797 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebbac6a6-a5f7-3b70-98d1-c6d445c73b39 | -3.6201 | -60.547699 | 2026-09-01 01:54:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a982d78a-510c-386d-b7de-ee6b4a6ed070 | -8.7745 | -69.334503 | 2026-09-01 01:54:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8db3fddd-9d4d-3d83-9d0f-f23471d58567 | -13.5444 | -59.733898 | 2026-09-01 01:54:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c772769f-f9a9-3206-881d-961892ba9daf | -7.588 | -61.3396 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a59ce1d6-a7eb-371c-9194-aa69d6206b8c | -19.204 | -57.303699 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e497442a-8383-3709-bb72-624221e4df64 | -8.7963 | -62.4944 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd19ce4f-bd07-360b-851f-4964fe7b4b7f | -9.3245 | -68.892197 | 2026-09-01 01:54:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c7651ebd-a696-3537-a945-be803776d647 | -10.439 | -67.841698 | 2026-09-01 01:54:00 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ebe0376d-57e0-36b0-918b-8db95ef2ae81 | -6.1915 | -57.7318 | 2026-09-01 01:54:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3e71d15-5cbe-3a90-8d16-9fdd3c7b6db5 | -7.0431 | -59.208099 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34d91996-ef4b-3ff0-8fe0-3ebee1f85d75 | -9.0377 | -65.3974 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20b0d8d8-197f-34e2-ac5f-b28b0643d174 | -19.188601 | -57.3242 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README15.md)
