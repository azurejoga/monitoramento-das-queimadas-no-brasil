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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0ca6301-6560-3f08-9bc6-cfd44d51cb77 | -7.2661 | -45.8443 | 2026-08-25 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| ce510097-61ed-322c-89fa-01549af125af | -7.2471 | -45.8685 | 2026-08-25 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 46cd0860-3a8a-3848-a579-1fcedf04a48b | -10.3918 | -45.0512 | 2026-08-25 01:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4a03f08f-93cd-3606-bcb9-36eed0027736 | -6.6226 | -58.4995 | 2026-08-25 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 41ab012f-7ed1-3c9a-9d01-23afb61d5b68 | -10.9291 | -51.0866 | 2026-08-25 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d2e42b8b-0a60-3840-9594-f66a6f2ca50d | 2.5983 | -60.697 | 2026-08-25 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d5af0979-cfc9-36b6-93a0-86110b2eb3fe | -11.1447 | -44.4632 | 2026-08-25 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 731c7fda-1bc3-3fe8-9ab3-120228abd867 | -10.7799 | -50.9325 | 2026-08-25 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 3c8d7d72-ce9e-30c7-840e-6b6da9757bac | -7.0057 | -59.2575 | 2026-08-25 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 191.7 |
| d6742097-b3d3-3584-be81-404e9679f527 | -11.4494 | -44.5353 | 2026-08-25 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 36c422d2-1004-3a03-9468-66d7728bb16d | -10.37 | -45.03 | 2026-08-25 01:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b37eb004-58a4-30ce-89f4-e3a6daa194ea | -12.77 | -44.29 | 2026-08-25 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9159cb35-c5a0-3aee-8000-29563247d30a | -10.37 | -45.08 | 2026-08-25 01:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa63ed4-183f-35bc-8399-086c8afac521 | -12.77 | -44.24 | 2026-08-25 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ff2a48f-2902-34d1-8333-c0d481fd5352 | -6.6227 | -58.4801 | 2026-08-25 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a9516b43-1734-3aa2-bdb5-ce4ea62ca271 | -10.9291 | -51.0866 | 2026-08-25 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b094b608-52be-3970-90ac-26c88871b235 | -6.6225 | -58.5189 | 2026-08-25 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e50faff3-1bcd-315f-9e2d-122031759f01 | -3.5221 | -48.1896 | 2026-08-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b701d6d4-124b-3299-b2b2-18f9cf4721f0 | -7.4286 | -43.1182 | 2026-08-25 01:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| c70bec28-e85b-3d80-bee5-b7b09e277b38 | -7.2713 | -45.37 | 2026-08-25 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 30b1f156-180a-3b74-921c-e936a77582d1 | -10.3731 | -45.0306 | 2026-08-25 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 462e75de-7f79-3ed1-bcc6-1b7a96837373 | -12.7802 | -44.2341 | 2026-08-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 1e3440a3-a154-3231-a6f3-91d1e02684d0 | -9.4578 | -40.3392 | 2026-08-25 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 0c35300e-6ff0-3cb1-951f-758ff071721b | -11.4306 | -44.5148 | 2026-08-25 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1c59b1ea-039c-3df4-a0e8-378f848d3495 | -12.799 | -44.2544 | 2026-08-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 8d6d9295-6f17-32bd-a037-fb87cfb6f831 | -12.7603 | -44.2608 | 2026-08-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0b9d7d58-589c-3826-9e18-3ab760bc77c4 | -7.2471 | -45.8685 | 2026-08-25 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| ac91cbdf-4b5c-3af6-a73d-3a19d4bc0738 | -6.1464 | -57.9359 | 2026-08-25 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8133f25f-7d02-3cd2-a890-b3cb88ff89e3 | -11.1443 | -44.4865 | 2026-08-25 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| bb722f33-6a11-36a5-a376-b2f50ce29b40 | -12.7986 | -44.278 | 2026-08-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6a2099a0-c930-3ea5-a536-f2fab19f3172 | -11.1447 | -44.4632 | 2026-08-25 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 2ebd7002-196b-3b81-badc-250a20f04184 | -10.9101 | -51.0886 | 2026-08-25 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7e4e5b7e-2667-30ba-b70b-d010b2e1562f | -3.5407 | -48.1673 | 2026-08-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 28721c45-b3e6-3771-9351-6de6cdc2fc58 | -7.2903 | -45.3456 | 2026-08-25 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a5b2015c-18a9-3885-8f0f-52706200ba0f | -7.2856 | -44.0875 | 2026-08-25 01:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3cfec588-8a7b-3675-88a6-b4c6f5d3c1f6 | -12.7797 | -44.2576 | 2026-08-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 272.7 |
| 0cd12155-0867-3a64-80f9-5e2934635915 | -6.641 | -58.4987 | 2026-08-25 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 262.1 |
| 62d18a22-177d-337e-a2b4-bbac7292187f | -7.529 | -61.3635 | 2026-08-25 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 95abbad8-e13c-39e6-8a78-ca573b2c7045 | 2.5983 | -60.697 | 2026-08-25 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 275a00f8-62ee-32c1-a3e9-697ae66c988d | -10.3723 | -45.0767 | 2026-08-25 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| b7107a68-329e-3ad1-b9d7-aa25c1ff3619 | -3.5406 | -48.1889 | 2026-08-25 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 8211ec20-aaa8-305c-b35b-260844039265 | -7.2901 | -45.3683 | 2026-08-25 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ffd46382-fd6b-3b5a-af04-f37441795ec7 | -10.3727 | -45.0537 | 2026-08-25 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 308.8 |
| d5c88880-6cfd-311c-b568-91d430a4553c | 2.58 | -60.6973 | 2026-08-25 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ac0d5a25-fe2d-3a83-b93b-030a684e03d0 | -12.7792 | -44.2812 | 2026-08-25 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 6c9469a3-1eb6-3c2a-afad-f2009d914097 | -6.6409 | -58.5181 | 2026-08-25 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5d178bac-52d7-302b-bfee-c3425678a5b4 | -7.2659 | -45.8668 | 2026-08-25 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8ee52426-8bb6-3d56-8f94-dfa33b3d1d7e | -10.9104 | -51.0674 | 2026-08-25 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 475d5ab4-600b-31d0-b49a-5024c2bd13fc | -7.5475 | -61.3627 | 2026-08-25 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cea89486-84d6-3897-bb24-127faa5a1a9e | -6.6226 | -58.4995 | 2026-08-25 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 673e4b94-d4fe-3a66-ac31-5102e4fac7bd | -7.2474 | -45.846 | 2026-08-25 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 58460039-eb41-321a-ac9b-da15dd3ea25e | -7.0242 | -59.2374 | 2026-08-25 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| daf5bd7b-e835-3c34-978a-e1402bbb8cde | -11.4302 | -44.5382 | 2026-08-25 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b8418583-e58b-35a8-a00b-b54e463d5a43 | -6.6411 | -58.4793 | 2026-08-25 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 61a4f60a-5ac5-3422-9181-22d3a03c0b5a | -10.3536 | -45.0561 | 2026-08-25 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3df8c975-f668-3475-b1dd-bd12982fe731 | -7.0058 | -59.2382 | 2026-08-25 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 3db99318-216c-3f99-a6ac-3685a3f74833 | -7.2858 | -44.0644 | 2026-08-25 01:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c305ecc5-8893-3c0e-b29d-fb062a2f6cff | -7.2661 | -45.8443 | 2026-08-25 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 413747d9-d0cf-37be-ad9e-a8e9633d6db1 | -7.0057 | -59.2575 | 2026-08-25 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| cd1c7d3f-be09-3854-bd8b-b590fab276c1 | -16.3946 | -49.9191 | 2026-08-25 01:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 99719bf0-f8aa-3a85-84ab-915dcd0b422c | -3.5406 | -48.1889 | 2026-08-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 07928a52-595a-3a67-90d0-0f9d639c2e69 | -6.1464 | -57.9359 | 2026-08-25 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 153609ff-2739-3a28-8644-210016395e0f | -3.5407 | -48.1673 | 2026-08-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 90542067-a9f7-377d-a564-10e31e1516f9 | -12.7802 | -44.2341 | 2026-08-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 200f0d38-1cfd-312c-842a-ebcc64f7c55f | -7.2661 | -45.8443 | 2026-08-25 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 79c30e74-f06d-3ff2-b480-4ed1b900704b | -10.9101 | -51.0886 | 2026-08-25 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 33aed779-5fba-3238-8a76-e43b924e6bd6 | -11.1443 | -44.4865 | 2026-08-25 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 542ee89e-07e7-3767-8af3-ef752664b0d2 | -7.2901 | -45.3683 | 2026-08-25 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 873bf6b5-62ad-3702-a15d-d488ecbe421c | -3.5222 | -48.168 | 2026-08-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 233fd737-28cb-3385-9398-7bdd98a020d9 | -6.6227 | -58.4801 | 2026-08-25 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b2821372-52be-374c-a057-4dd184cf876d | -3.5221 | -48.1896 | 2026-08-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 24d01bae-cb77-3c70-96f7-9d4ebee96e73 | -7.2713 | -45.37 | 2026-08-25 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d151cdd5-fc4f-3f62-9c86-bb14e33afc85 | -16.3749 | -49.9223 | 2026-08-25 01:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 607d66d0-b393-3502-92dd-0dc650817a52 | -7.2903 | -45.3456 | 2026-08-25 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 46b6f1cc-c15e-3522-b40f-2467eeed6842 | -11.1447 | -44.4632 | 2026-08-25 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| d55e2afe-297d-3e58-b99e-01d45b66971d | -6.6226 | -58.4995 | 2026-08-25 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 422eaadf-a710-3f43-8656-48c223850cb6 | -11.4302 | -44.5382 | 2026-08-25 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4ea34823-e71d-3b61-89d0-e7e295bc18d4 | -7.0058 | -59.2382 | 2026-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 5ee2bc09-eabe-365a-a854-3666567d5f97 | -12.799 | -44.2544 | 2026-08-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7290b6e9-f3ce-3647-9361-de89758092a9 | -6.6411 | -58.4793 | 2026-08-25 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| f25ed7be-2661-3ea5-9457-3eb4f5ca9cbe | -11.4306 | -44.5148 | 2026-08-25 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c8b99a33-36ec-3d70-8ff6-1cbe31aaeddb | -6.1286 | -57.8198 | 2026-08-25 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ca33e4f4-2a28-3d77-942c-f72096cfa29c | -12.7792 | -44.2812 | 2026-08-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| dd8d94dd-d7b8-377a-a56b-7346f86cc088 | -6.6409 | -58.5181 | 2026-08-25 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1edd2f9d-292a-369c-ad70-29830bea03a8 | -7.2659 | -45.8668 | 2026-08-25 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fb073228-0d4b-3920-9513-65be95dc82ae | -16.3951 | -49.8969 | 2026-08-25 01:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d03f9006-3a19-37a0-94e3-76673557a003 | -10.3723 | -45.0767 | 2026-08-25 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 77c371d6-f986-3a8e-af9b-86b17fe5b40b | -7.2471 | -45.8685 | 2026-08-25 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| b49727e7-6233-31bb-9be8-1edaaf7b0c3e | 2.5983 | -60.697 | 2026-08-25 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 36c6a0d9-9eb4-3c71-bd4a-24343fe44529 | -7.5475 | -61.3627 | 2026-08-25 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 0b811d12-8b87-3ec7-a968-53ff35341d88 | -7.0057 | -59.2575 | 2026-08-25 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.9 |
| ae066644-7e47-309e-88a1-655db64e8b08 | -10.3731 | -45.0306 | 2026-08-25 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1d62d55f-2b76-3739-9ef3-bb7a7ec46c0b | -7.2858 | -44.0644 | 2026-08-25 01:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 106f77d6-1cfb-3234-b385-62db8ca8d4c3 | -7.2474 | -45.846 | 2026-08-25 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3aed464e-6f45-3ecc-a40e-97c2c6357fc7 | -10.3918 | -45.0512 | 2026-08-25 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9918fe34-348b-3a23-b05f-8cabe89cad19 | -12.7797 | -44.2576 | 2026-08-25 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 320.8 |
| 16d6d1fc-8ba8-31d6-b134-bf29827deca9 | -6.641 | -58.4987 | 2026-08-25 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 88c6f5d1-827f-3eee-9245-407e37f1fe44 | -10.3727 | -45.0537 | 2026-08-25 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 283.1 |
| ab02a0cc-8906-3eb2-8978-48b8e4f18fb2 | -12.7603 | -44.2608 | 2026-08-25 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ec5b03eb-7e44-33fc-ad06-d646f147e2a9 | -7.5475 | -61.3627 | 2026-08-25 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |


[Clique aqui para ver as próximas entradas](README13.md)
