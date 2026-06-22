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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8323676-0f0d-3610-be62-60a931845f2e | -13.51778 | -52.16831 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b36b392-f3f6-3c8b-a1c4-3dac904eb8ed | -10.18003 | -51.65996 | 2026-06-22 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e4846e1-700d-3ddb-b7fa-aaaa337f0a6b | -10.5629 | -46.23421 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a4e8e7-ace6-3e67-a2fd-c0807dddb6db | -11.10259 | -54.14516 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f410ac40-d908-3d2d-bd29-4fa7da216fa7 | -10.56483 | -46.23916 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ffd94a4-9d03-33a3-87c9-16c38e719698 | -11.11086 | -54.14152 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5042cc74-92fa-3bb5-aee2-f590fa0696e6 | -10.05769 | -48.08854 | 2026-06-22 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cf3996e-9f02-3ccd-9d31-e5377f381696 | -13.51389 | -52.16319 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d994ef-56c9-339e-bf55-c326b4042615 | -12.20062 | -47.97211 | 2026-06-22 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bd99799-ea7a-34d8-8c7f-b90ae63f7547 | -12.22234 | -57.28324 | 2026-06-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a80a0b3f-4483-3755-8339-feb858c63bcc | -11.09945 | -54.13988 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab1e8b8f-ee40-3b39-933c-208608fbb4ca | -10.27555 | -60.54956 | 2026-06-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e24e0c2-2242-350b-ba1c-7a17b0d4e07a | -10.55476 | -46.24827 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 385e67df-6344-3c3a-912c-c74b25c66c1f | -10.53955 | -47.72703 | 2026-06-22 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ba4e98b-0053-3b6d-94e8-3ffb26d5d488 | -13.30632 | -45.2256 | 2026-06-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09124feb-8a44-3c6e-907c-be9cc49ac7aa | -10.17503 | -51.66366 | 2026-06-22 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 695d5768-6674-3490-afc4-b611f38055c0 | -9.18844 | -58.05745 | 2026-06-22 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d01ceff9-7d04-3b8f-97c2-ec6662f5372f | -12.06408 | -58.0494 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbb62270-ab5f-3863-833d-70889be84cfb | -11.0512 | -52.48138 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a554891-3129-3381-891f-6d57445fad1c | -13.52729 | -52.16505 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5199b9bb-531f-3461-ab35-1164584d6ef4 | -11.09879 | -54.14462 | 2026-06-22 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43e2b3ff-61d0-3dc1-a1e8-9b1cc9d7f255 | -13.2945 | -45.20368 | 2026-06-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09217831-2f5f-3ee5-b241-c088da90b350 | -10.5623 | -46.23922 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951ff7e0-7995-3c2e-ae1e-608ae3c51417 | -12.43435 | -58.40446 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 477068d1-27a0-35a6-b7b0-556bb28d28b1 | -13.52225 | -52.16894 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5137a8b-b302-3c40-a736-c06c69543b95 | -13.51332 | -52.16764 | 2026-06-22 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e2443a7-08d5-3437-af2c-d39673c59987 | -11.05651 | -52.47414 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80655ac3-c4cb-325d-9309-b7f6e8760cf5 | -8.88131 | -46.94349 | 2026-06-22 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4a2c3c3-fafd-30f7-ba81-2cb206cc34e3 | -11.05963 | -52.48267 | 2026-06-22 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3080e30f-a0c6-3d36-bb4f-da871f806e88 | -12.22179 | -57.28686 | 2026-06-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f666e40-01f3-3f02-94ee-f8c6289d710a | -11.51064 | -56.12121 | 2026-06-22 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 558d04f6-52d5-3645-82eb-7de2e3ec387b | -10.9115 | -46.32191 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a95fa18-ab1d-3a97-bb07-f8e3b668bc12 | -12.4338 | -58.40797 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8890ceb7-c4de-3425-8d73-1100342ca18f | -10.93821 | -46.42361 | 2026-06-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8509a17f-cf87-31c0-8d00-0c448fa9f92f | -13.30008 | -45.21787 | 2026-06-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1535c0af-e2d2-3dda-bed4-f4fd43428f96 | -12.43874 | -58.39797 | 2026-06-22 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb9b0e45-c5ae-381d-82b2-e2abe107395b | -18.25473 | -51.27809 | 2026-06-22 05:14:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d328bcce-f437-310f-826d-2819946b8f58 | -15.38896 | -56.9701 | 2026-06-22 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaee3645-78d0-362d-8a2c-75e1881988b2 | -18.25439 | -51.28122 | 2026-06-22 05:14:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a3c48ce-76e6-3935-9c36-f8377f58d1fa | -2.32525 | -60.06127 | 2026-06-22 05:44:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ab983c-3773-3e8a-a3a4-81a5df8cbfd5 | -0.94071 | -62.49754 | 2026-06-22 05:44:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db2538fe-5e36-35a3-9bb4-568f5a694766 | -9.18375 | -58.05864 | 2026-06-22 05:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d359a8-a006-3891-83b2-3bb9e9f753c3 | -11.05956 | -52.48853 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8544f54-4b08-3cee-9e03-20fe08fb774b | -11.05295 | -52.48764 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c702a09-a429-36cc-a409-8c1d29052fd5 | -11.05425 | -52.47639 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f081553d-fb93-38b7-b23f-5be6c16e8214 | -10.17743 | -51.66598 | 2026-06-22 05:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd3cec1d-ccea-3e9e-9168-84cf67f4d61b | -11.0536 | -52.48204 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5064f18e-6577-3ca9-8654-e4273ffed8f2 | -11.06087 | -52.4773 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cac0079-cf24-3625-8b6d-2a4ed5ff57e2 | -11.1098 | -54.1434 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41798a01-a89e-3288-ab91-ffbff9db024e | -10.2741 | -60.54918 | 2026-06-22 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d220ef86-9cf7-3cec-a35b-88a9b3e15bae | -11.05721 | -52.47717 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73962f28-927f-35d3-8c8b-b335ea6df5c9 | -11.10926 | -54.14776 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b7328f5-03f8-3f2e-b987-62c10d420269 | -11.05062 | -52.47615 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c31641ea-b89c-308a-9fd7-69a7d746a2f6 | -9.25263 | -60.33209 | 2026-06-22 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99602ab9-0326-3dc0-bc6d-10f3b27d0eae | -11.10381 | -54.14275 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31f1494b-addc-3545-8286-90f4940d9577 | -10.17821 | -51.65963 | 2026-06-22 05:46:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03486e41-05df-398a-9f4b-e3d301911e12 | -11.04993 | -52.48176 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb0c8c0-66a8-395a-9283-e0163a495460 | -11.05583 | -52.48839 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90d8b311-969b-307d-8d1f-d531e4765550 | -11.09728 | -54.14643 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e7de6b-7c05-3321-9de2-3427a6983d5a | -9.18822 | -58.05931 | 2026-06-22 05:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33d4dfbe-4e7b-308d-a6b0-ed27bf683b7d | -11.04924 | -52.48734 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b4e5f1-4963-372d-a95b-a380eb8a15b8 | -11.04766 | -52.47526 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42fa8d1c-b74b-33e0-a65c-0992a7e71e75 | -11.11034 | -54.13901 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f2a463a-99e5-37de-8371-bce0465cda4a | -11.05652 | -52.4828 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cebc9a65-11a1-391d-aefb-766ffed67ecc | -11.04702 | -52.48087 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eccd017-b3af-309f-9de5-e718a08833be | -11.11525 | -54.14847 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e990010-7581-37ac-bae6-dd077977adde | -11.10435 | -54.13836 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dcbdbf0-e8b7-3fbc-a3cb-9526594f7f59 | -11.09782 | -54.14202 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d0d968c-e2e9-398d-b616-9e3b6613c9ff | -9.25005 | -60.33364 | 2026-06-22 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56a07eb5-7f3e-3507-895d-91b94ec6ee28 | -11.10327 | -54.1471 | 2026-06-22 05:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 008e77ed-fc57-346a-8053-96b8e95c315f | -11.06021 | -52.48294 | 2026-06-22 05:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264a3ea1-b479-387d-bdc6-188cc2ba50c0 | -12.22534 | -57.28165 | 2026-06-22 05:48:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bdc5ca8-2b56-32d5-aa09-09ecd6bb686b | -13.51758 | -52.16481 | 2026-06-22 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8c278f3-ba68-353a-bfd5-012bfa662fed | -12.46944 | -55.13175 | 2026-06-22 05:48:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c60b4642-ad78-3699-b1b9-8a37427a6e8f | -11.51279 | -56.12161 | 2026-06-22 05:48:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 263dc9b8-040c-351f-89d6-5dbcdd645b12 | -12.46895 | -55.13577 | 2026-06-22 05:48:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3174113-6469-3695-996a-b6661990b381 | -12.43067 | -58.40961 | 2026-06-22 05:48:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a70a5962-5349-3f76-b608-a5e568b68b76 | -12.43586 | -58.40551 | 2026-06-22 05:48:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0b0e096-d519-3fac-909a-2e7d9532f9bc | -13.51693 | -52.17095 | 2026-06-22 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e753ff1-92ac-3008-9839-8d148382ea5d | -12.43647 | -58.40083 | 2026-06-22 05:48:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 97a41942-2249-3350-876e-4b61a5109184 | -12.22334 | -57.28467 | 2026-06-22 05:48:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a755ced-ce31-31ec-a29e-1f0e68a69a9a | -11.93079 | -57.0411 | 2026-06-22 05:48:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa156515-37c1-3372-8072-7bbfc575fe3c | -12.43005 | -58.41433 | 2026-06-22 05:48:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e684c69-17ab-3875-90d1-11a2045fbd5c | -11.51236 | -56.1249 | 2026-06-22 05:48:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a890a372-5b7a-316a-937e-b2b6c4d0d599 | -13.52452 | -52.16556 | 2026-06-22 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8896d68-9732-3d3a-b1fa-dfc66bfb4e77 | -12.43128 | -58.40491 | 2026-06-22 05:48:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d82a7c0-0531-3b83-a64e-9ee3d28078a7 | -12.43051 | -58.41283 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 914472f3-3422-33fb-b3aa-c01d93cdc42f | -12.43117 | -58.40666 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f66ec79-b4bb-3a96-ba3c-ced9b423c1f5 | -12.43 | -58.40318 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9247b96-26c5-3a6d-9235-e8babaf62663 | -12.4286 | -58.41548 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32afc4aa-458b-3bdd-ac4a-9a2842f03305 | -12.43182 | -58.40055 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57c3527e-44d7-30a4-8f68-8781a8facd2d | -12.43681 | -58.40384 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fc69839-20fe-3170-a9f3-0ea760b03ec2 | -12.4375 | -58.39779 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f393e5ca-525f-3881-8ca5-0840725e1201 | -12.42984 | -58.41908 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0ed3e49-7a77-321a-b4c0-9fa086e8d935 | -12.43864 | -58.40118 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4f6ea12-8160-3bb8-8d2c-28f740fcc8db | -12.4293 | -58.4093 | 2026-06-22 06:05:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7b61e3b-65b6-3a57-ba3c-1884dcda997d | -3.51151 | -48.03331 | 2026-06-22 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2136b268-9fc5-3d46-b428-393189cf4da1 | -3.50142 | -48.04076 | 2026-06-22 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1b795719-4f93-3801-9a74-c739a4bae0dc | -3.51283 | -48.02453 | 2026-06-22 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42e4a77a-f3e4-304b-8467-23bf4203c037 | -3.50273 | -48.032 | 2026-06-22 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README9.md)
