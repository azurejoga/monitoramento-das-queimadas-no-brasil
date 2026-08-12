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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c189696d-b6f9-3f59-abf2-cb7e46c88758 | -12.8541 | -52.04152 | 2026-08-12 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eac8b46f-7c76-33d8-a15f-a8502ef535df | -9.92389 | -48.67413 | 2026-08-12 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6163cc2e-030a-3df6-8514-85bdb8babfbd | -14.48025 | -51.86459 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c22885a-09e6-33f7-a9fa-6f00337ee356 | -14.35343 | -54.86745 | 2026-08-12 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4baac779-42f3-335c-87e1-74b459bae3ca | -11.9545 | -46.38221 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2901c506-ae9d-310c-8fd3-2887caabe731 | -11.94599 | -46.38614 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8202a08-6168-389b-90ab-d08866c9292e | -14.51573 | -49.28604 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 654b59a5-06f8-3ca5-8ddf-3cc356af2337 | -14.28003 | -45.27631 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47e45231-fc8f-373e-9867-80235f13d742 | -11.48105 | -44.57225 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| da5d656b-6e12-36f9-b927-9834e399ca05 | -9.36537 | -47.45179 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16a1c914-89f0-32ff-8745-fb2c22d86bca | -14.48585 | -51.85089 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e278aa63-05c5-3735-94dd-8e15f6d0c1a1 | -8.95485 | -60.54156 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea0fd454-0198-32c0-bd20-7a2e4d138be5 | -10.36618 | -46.38288 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e895c534-f88c-30d7-a972-fc7467a0bd85 | -9.34977 | -47.48248 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f33807e-13b6-333e-a9cd-7dead9fb7120 | -11.60174 | -54.66685 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 235e37e6-c9e2-3b6f-a4e9-315ebadb9625 | -11.9499 | -46.38665 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d9a70c87-9928-3da2-af74-815fdbfafd75 | -11.98033 | -46.39626 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef7b90df-0c70-398a-b824-ee1925be23b1 | -13.83668 | -53.80099 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3184e3d9-4dfc-339e-8bfe-321b598559f0 | -13.88615 | -53.8292 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6107ac88-a7d1-3a33-b70c-4d27927845d1 | -13.27997 | -49.67141 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c96dc177-53e7-3c03-b0f0-e65800496fd8 | -8.89895 | -60.58521 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92076bf8-34ae-3892-aaae-f345ca229651 | -13.89593 | -53.83526 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55553a6e-dc61-3b62-a6e2-cf3ce71d427c | -9.33594 | -47.52568 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1ebd89e-6e60-312f-93c9-55f0588a08f6 | -10.21957 | -45.91146 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8da9624-36f5-38a7-9ab9-844b905bdde4 | -7.40948 | -59.9974 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9f5f069-7311-3b37-bf12-5d47fabb4f24 | -12.72628 | -48.44054 | 2026-08-12 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f1888c2-86a7-32d0-b599-35ff53e27cd0 | -11.82471 | -51.85604 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3c51998-fd96-31b9-b3ba-a74d34143e8e | -13.8885 | -53.81428 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09a2d3ac-5ee2-3ddc-94a7-a95690463904 | -14.35799 | -53.23608 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f81da6b2-9373-3a49-9cd3-4db7b98f11f8 | -14.51515 | -49.29001 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0edc75f2-e79a-3d74-b214-e114d7495bd4 | -8.89995 | -60.5785 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af54cb5a-2b65-3258-9f24-10f47f9daf17 | -15.52211 | -45.85794 | 2026-08-12 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54708e57-0674-39c9-862c-a5e195be1168 | -10.70755 | -47.90499 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fcde9d6-e294-3d97-8a5a-acde4369f381 | -15.05926 | -45.32803 | 2026-08-12 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58a39771-ea14-3d17-98e7-0015dd19c48e | -11.98506 | -46.36332 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9da2897b-e8ee-31dd-893d-9aa458b88ada | -9.58262 | -48.41683 | 2026-08-12 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03063297-d52e-3049-8691-0f48d946ae53 | -11.88791 | -45.82729 | 2026-08-12 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6583113-8bb0-36e5-838e-2fe43936e02d | -14.51781 | -52.13553 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e89b2aeb-ec01-3cba-87df-987f8f410d74 | -14.50822 | -49.28893 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4bbd423-4e98-3dad-a2ef-c86822f9a74b | -15.1876 | -52.78508 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fbd1d74-2c1a-37b7-8a9c-4c57430074db | -11.88742 | -45.83086 | 2026-08-12 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f0d29fd-2e74-3559-ae3b-8230dbcad04e | -8.89703 | -60.56403 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ea3e63f-08ba-3cb1-829b-0b41b69df180 | -12.03547 | -47.80207 | 2026-08-12 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee75c158-12df-3f18-b4a6-ae47e95a46fb | -12.10879 | -47.18011 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da45ca72-9fc5-3193-8680-7a212c7f0bf5 | -8.54803 | -54.59215 | 2026-08-12 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c336c52-1493-375f-b2f7-3f3e4b3528ae | -10.35923 | -46.37708 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1194b90-004f-36f4-a0e6-5d9952e5b429 | -17.14291 | -44.80422 | 2026-08-12 04:51:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26678652-ab98-3ead-b955-be510e39d4ee | -11.98243 | -46.38165 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4a7b9d57-d55d-3145-803c-53bde02ef56d | -11.97396 | -46.38525 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ee43218-1d29-3e90-84e3-b631a92e9f61 | -11.55529 | -50.22689 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87145c77-8775-3d62-8421-0570443259a7 | -11.98562 | -46.38715 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b7aedfd-1878-35e3-81ae-4f0aa69e937d | -8.94566 | -60.52719 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4851c29c-3072-351c-aad7-82f1285f718e | -14.52057 | -52.13969 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d94ee69a-cb50-350d-88b1-48eeeec0eaa8 | -14.38369 | -51.98454 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3a83bc0-65e2-39b0-9faf-5739d832547f | -13.54909 | -46.2764 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 954f1c4e-a6db-32f8-bf0a-3dddb2b4cdab | -10.70288 | -47.89315 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c2447a9-3151-3a11-bbf8-84da4794dc8d | -11.9538 | -46.38717 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d0210d41-2d7d-3b05-b78a-19be1dbe1471 | -13.83734 | -53.79708 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01421a7d-8489-30f3-9acf-a62cbc44e759 | -13.88405 | -53.82043 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 130c639a-81c0-34f5-9d83-6124c244387a | -10.71698 | -47.91465 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66fef778-3962-3530-a5cb-2e12662e2585 | -14.53888 | -50.39793 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e86b599c-8e14-3888-b223-cf9955d6147c | -13.90225 | -53.84052 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d88ad49-b040-3c33-be57-2ffad6d56b0c | -10.6372 | -47.49054 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 361173e9-a247-3a2e-ad93-100da7c3609f | -9.37627 | -47.4441 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36e0f6de-0a2b-3b88-97d4-6cfdf1baae10 | -10.09559 | -46.22278 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e117894-9f88-3137-a3e8-4a072a36d7d4 | -15.16974 | -49.26662 | 2026-08-12 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3963f775-a9ce-3307-9baa-e82b35db9062 | -13.84283 | -53.7859 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84251a4c-94d7-3754-ad46-cb0882768e4e | -14.30308 | -51.99662 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07ad1bd9-717e-3286-9ece-b60d80401fce | -9.35244 | -47.53647 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb191701-224b-3e97-9c9a-7182f910606b | -11.78772 | -51.87202 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 432ec377-c152-3a31-90a1-4515f44e7ecb | -8.89398 | -60.58001 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f2cfecb-8645-31a9-8245-a1af698367e9 | -11.50051 | -54.60431 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d77c5078-8d13-3d38-a53b-98e5366f087e | -14.35863 | -53.23227 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 19a608bc-e5ce-302e-985f-da5776d101c6 | -14.29975 | -51.99606 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e73d0f8-7ce4-3c50-8bc7-11e4245f484c | -14.55065 | -50.39994 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c427d77-85cd-379b-a8a2-864a97df68b6 | -13.89027 | -53.78196 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1429d20e-14e4-3730-87e5-bd1d83563830 | -15.29925 | -48.87471 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 310f1625-2eb3-32cd-8dd7-451d8bdb6009 | -10.09626 | -46.21801 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7859fd58-ed2e-378f-a2d3-413d738735fa | -10.70519 | -47.90176 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cad6bc91-a0d1-3c17-9c8b-acde6b4dba5e | -14.28321 | -45.28537 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eee9639a-5978-3d54-977d-fd108fefa05a | -12.35407 | -51.21387 | 2026-08-12 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b3e3001b-e93e-3e77-a50b-4db1b978a39d | -13.53636 | -46.27989 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e8a4562-7ac8-3d63-a6ab-227f0cc10ffc | -13.85778 | -53.82557 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85ecf930-d9ed-3697-b47d-2fafebbce8d3 | -14.33044 | -54.04388 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cef63005-3d7e-3663-aba2-240be67056bf | -10.09494 | -46.21606 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c2124b0-62a8-3373-bf23-9124fc7c1a3f | -8.94641 | -60.52322 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29dab4f9-9b2c-3855-b381-c5548bcc5b67 | -13.52693 | -46.28925 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a77bf340-9511-3c5c-a84e-f3958eb23fec | -13.83192 | -53.82924 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fda2e86-89e5-3318-8fd5-a017f84efe83 | -14.35488 | -53.06529 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab626a49-99f9-3b1e-bb87-71cd7ad1d2d4 | -13.88678 | -53.78136 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d7eedbe-62cc-3d0b-a0f1-4b633dd881f2 | -15.3016 | -48.88336 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a99b11c-0653-358f-8359-0e724be89071 | -16.36025 | -48.9201 | 2026-08-12 04:51:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79269223-a640-3929-a94e-1276fbf495e6 | -10.22912 | -45.92818 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7db5920f-9b3a-3035-b393-1c3a691354d7 | -8.94444 | -60.50215 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77278433-0be8-32b7-994a-2e75dde409fb | -13.57188 | -46.25925 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c7fc174a-6f04-3d90-9520-29b5a9f6123e | -8.97932 | -60.53772 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9db4d09-6435-3d01-8789-8ebea7676b1c | -11.9513 | -46.37673 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f8d5940-f4d9-3a12-aa0e-78ef09e21c04 | -7.39878 | -59.99163 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dd4639d-4d27-3465-a467-9c9e0438146e | -13.90497 | -53.82452 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b00d8fb-9d8b-30e8-8250-d28a4584c122 | -8.8828 | -50.1801 | 2026-08-12 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
