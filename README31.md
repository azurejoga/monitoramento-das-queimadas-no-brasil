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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 133ac2bd-1e59-38c6-b73f-4beee97af85a | -9.38854 | -48.01315 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aab2c1b2-6e42-380d-9e2d-ce785ae70c60 | -6.26925 | -43.5488 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43a9579e-2e12-3bcf-a360-18ad66b0e403 | -6.16221 | -43.3317 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dd3ed80-109e-3e26-b2d8-dbba5b4b36fe | -11.20556 | -45.03717 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccdbf90b-a397-3d6b-a2db-09105dee37a5 | -6.63909 | -43.95865 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89b318ac-4848-3d79-bc5e-14cb6e73f398 | -5.99509 | -43.36666 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 870e6061-56fa-36bc-a7d3-c07001ca10fc | -6.53552 | -42.96021 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecf56d88-db8e-320a-b212-404d3b658cd9 | -11.28321 | -44.91695 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74fa7dec-251f-3ad3-8cb1-9e84c21c7ac6 | -8.19607 | -46.76777 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49bd03de-879f-37cc-a827-cbf7bee0d3b3 | -10.88893 | -45.80247 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ce5651e-41a9-34b2-a52c-b5e6db937d59 | -10.27638 | -54.2506 | 2025-09-01 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae39baf-29f6-302e-bd7a-624ee1202a9e | -11.03605 | -45.14507 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 27ebb266-c0ca-3eed-8945-6a431ec276c2 | -11.37268 | -43.5985 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0d38ef8-642b-3ac6-9193-7c49e1ba0801 | -7.94515 | -46.41294 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba49ed8d-bdeb-3ef9-b619-6918de4c39d1 | -11.05464 | -46.91544 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8835a9-e542-3ac1-b2ab-9a4eb8b9c1d8 | -11.07405 | -44.65575 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d79ccb-d119-33c6-b169-1fb8077142ef | -6.15637 | -43.34615 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6249daf-ea61-38d2-b0ba-8588a5ba21a5 | -9.26887 | -47.11124 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f038fcb3-d026-3051-90c5-37eee631fe55 | -11.80205 | -44.94482 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ae7fba-57ae-370d-84a0-c00b104b8d13 | -8.90417 | -45.1209 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eccb57bf-eb6b-3bf8-a60a-ed1e19d4e507 | -6.30925 | -43.78758 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d77c10c5-e1db-3c97-842c-7e0d63bdfd85 | -5.80221 | -42.54794 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e48f333a-b1b1-3089-a22c-e3fccf21d060 | -5.7533 | -43.67803 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a772976a-065f-35ca-a279-7bbe4248fab6 | -11.48581 | -46.81146 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3942f28-24f3-308d-ba52-bb34ab3bd9f4 | -6.8723 | -45.14566 | 2025-09-01 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c9583e8-d059-3cb1-b423-5cfaeb1ff536 | -6.56722 | -43.66915 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f7b66f1-1a0b-3fb1-8f8e-52d6cf737357 | -11.37014 | -43.55027 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c0079c2-7206-3c92-9a42-f5ee885039f0 | -6.95936 | -44.34164 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc806977-f8f2-3bb8-98bf-1512307a3f2b | -6.53833 | -42.96437 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a9e348e-b85c-3f09-b0b4-93f546aed169 | -6.58052 | -43.71881 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4af060cc-4002-3c19-b2d8-f8bc74690091 | -5.96067 | -44.13393 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48b1cf6a-eb7a-3009-9534-304be2844ecd | -11.28669 | -44.91755 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 605e475e-aeb2-3c63-89a7-f20260099e15 | -10.36944 | -52.29246 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4b02518-d707-3ca5-8b95-e5e1abd85f80 | -11.01245 | -46.83692 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ace133e-d7fc-32df-bcb1-92f0bb049f0b | -11.04858 | -46.90423 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83f126c7-5463-37af-a169-bb28ea8f66f9 | -7.48286 | -45.99553 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb916b8d-dce1-3a8d-a41c-daccbb1a0a7e | -6.82931 | -52.8277 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b0351af0-f6ec-3613-9f10-1a89db5a50be | -11.85377 | -46.79156 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 148244ae-015a-3ca0-adf5-45da2391d3d0 | -9.64152 | -47.80589 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bdd8c95-295d-39b7-a5c4-c6ad4bed786f | -9.64281 | -47.82492 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1703d74-ba7a-3272-91fa-44079b5a19a2 | -8.77518 | -46.1058 | 2025-09-01 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cbc70cd-ce01-3b87-aabd-4cf794c64671 | -6.44905 | -43.97292 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ce4156a-809c-335a-b3ac-94ccb21eb558 | -11.87662 | -46.70306 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac0fb47a-ae9d-35e9-afa9-452053c7dc1e | -10.57812 | -44.85567 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47676a65-3895-32eb-a084-e12c786922b0 | -6.52507 | -43.50394 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a68aa94-e0d3-3b78-9594-eb21604b93b3 | -6.56786 | -43.70885 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35a1e31a-7a17-35ce-81c5-097b96b449db | -6.23916 | -43.39334 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 506e6a48-abe4-3d8b-857f-7ca4bfca88ef | -11.03012 | -46.9418 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76c408ba-fec3-3eff-8e3b-a0572b901ec2 | -11.3692 | -43.62006 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 775df4d2-1d24-339a-885c-b9b9079cacb0 | -7.62616 | -42.65228 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c396f26a-a4ed-3ae2-8a5e-cf5a672386b4 | -6.93565 | -42.01674 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74dffb8c-f40f-3fe3-a27b-5fbef9c613c7 | -6.82928 | -43.32617 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| cdc47017-e422-3e6b-b3c3-2294b74748da | -10.04724 | -48.08313 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33cb3b57-4a7a-388c-ae9e-decfbd16a789 | -6.15697 | -43.34239 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f88bbff1-9dcd-3053-b216-415f482c6b4f | -10.28085 | -54.25048 | 2025-09-01 04:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04d345e-ddbb-3f5d-a2d4-8ab20398cc7d | -7.71694 | -50.26064 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2630c39-0a7c-3085-a33f-efe1116d53ad | -6.95229 | -44.29525 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0234ddca-0c3a-361f-b546-8249a556b8c5 | -11.9027 | -46.6819 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e2027ea-e1d7-3d67-a98b-76136b608619 | -6.83553 | -43.33096 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a99b4196-d8ad-3f35-8a46-a00ad6f50ae5 | -6.81793 | -52.82285 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45f5bfd7-1b76-3740-a1db-187f8b9c34c8 | -6.50777 | -43.56697 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 288dcaaf-c71e-3ee3-bdaf-92b9ea2b6f58 | -7.37202 | -43.3854 | 2025-09-01 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07f96e8-a763-3d28-a2ab-6883008cb476 | -10.24112 | -51.12064 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9314e00f-bb22-35d7-b1e2-6d672c23b009 | -9.63575 | -47.81601 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4520919-83be-3f1b-8f34-d995272f0c0a | -11.88652 | -46.75202 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0255b9d7-b74a-3101-98a9-6a89aa91eda6 | -6.16341 | -43.32422 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52c4757e-9662-33db-bb55-a4a4d4579d81 | -7.60786 | -46.03874 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3df4c15-92a2-381f-ba36-b310a6a21754 | -6.30987 | -43.7837 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a20fdf9e-8983-370c-80df-4aa2bcf016e5 | -6.95584 | -44.29582 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60c6f477-ac94-3a5d-aac3-6094e6ccd6c7 | -7.55983 | -45.70226 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37b7d566-a01e-353c-8617-92ffea25dce7 | -10.57876 | -44.85176 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b462dc-88ec-32a3-9057-9b9778c8ca9b | -5.87706 | -42.99485 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ec789f36-c426-3ff2-9b1f-d104d727c2b2 | -6.80145 | -45.68594 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 308e320f-b5a8-3062-bf59-8338233f1e78 | -6.82868 | -43.32986 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2b02253a-ca00-3fb8-9d55-d03ab5894291 | -11.89197 | -46.74325 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c95a0b84-7ac7-3be4-9296-afeb3ce43174 | -6.28941 | -43.55603 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4050ffef-9805-349b-a806-58bd59e47277 | -6.45548 | -43.69131 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08e5e1aa-4d6b-3953-a09b-4d5e6fa625ca | -9.63551 | -46.60945 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53d2a650-c25c-3862-bd75-58449be17432 | -11.80488 | -46.41764 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b1baf747-b8bd-38bd-807c-8f3de2db6a3e | -9.64271 | -47.80119 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4191318-ded6-3798-805b-7b41eb06e36e | -11.04238 | -47.01023 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2ed6a08-1a0f-3c3f-a18b-65e808790b31 | -6.83613 | -43.32727 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5141f06f-da0d-37df-b41e-d9eeaca45f10 | -6.17027 | -43.31699 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 41c4b586-ab05-3955-b284-f990006c0b80 | -9.67355 | -47.82233 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30bb0036-43bb-3f82-8166-3c3679b5fc4b | -6.28892 | -43.29793 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17d0c35-335d-36df-ba20-4b254d8ee45c | -10.60727 | -44.32915 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 4021e07a-3fcc-348b-80b7-2f2fde3260d1 | -6.16042 | -43.34297 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc93661-cf2f-340e-9148-2df6c1b7104f | -5.42958 | -49.99461 | 2025-09-01 04:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e724c3f-cef5-332c-84f9-bcee1d7456b2 | -6.24591 | -42.41756 | 2025-09-01 04:10:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 891eb14e-93fc-31a5-b433-dc7748e621ce | -7.08162 | -44.35988 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 27449bbf-8196-3702-8c1e-d6fe816a3f78 | -11.90511 | -45.04272 | 2025-09-01 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 485b06ee-f31a-392e-be82-d08374e31e4a | -6.30079 | -43.63982 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 217d1255-793f-3613-b425-fa6d885debf8 | -6.29814 | -43.61208 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c0c5474-9c17-332a-945a-bf3e770c93c2 | -6.63722 | -44.25936 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85772077-342d-3905-95ff-d41139d56e2e | -9.21863 | -47.11345 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68821ec3-a5db-3ab6-97b4-6ebcb55a1c7c | -6.16847 | -44.12019 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99436366-88cd-38ec-a4b3-666e565bf548 | -11.08671 | -44.62229 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f52daf40-d2ad-3c51-beda-e1694a40b45c | -6.30141 | -43.63599 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4f38162-685c-39af-8809-c46d49646bf6 | -8.91594 | -45.87071 | 2025-09-01 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dda848ba-5f26-3f41-88e0-f0d41312192f | -6.45514 | -43.95768 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README32.md)
