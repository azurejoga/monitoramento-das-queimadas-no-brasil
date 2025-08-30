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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34e62a9a-ac14-3bf8-91c2-66dffae51b97 | -5.18857 | -42.71621 | 2025-08-30 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e2e2f98-f7f8-3ba6-8939-b74e0d31f8e1 | -6.00464 | -44.71349 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5fb9d58-047f-3bc3-8d1e-544f1b90dcee | -7.02087 | -42.03069 | 2025-08-30 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1902c9ce-059d-3949-b901-d389c62f9757 | -6.32226 | -42.52837 | 2025-08-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0ca06e3-cd35-32c1-8ac8-686279e24ebf | -7.71603 | -50.27756 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62f677c3-01f3-36b4-b607-280f26b82c51 | -7.06872 | -44.27765 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1732d8cc-3aba-3445-b3a5-01b70669a935 | -9.0614 | -65.4355 | 2025-08-30 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 4fa86098-ac53-3b32-8a23-ecb666343c73 | -9.462 | -60.549 | 2025-08-30 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4818e49b-278d-3a08-9b23-ac9b109ae6ef | -6.4208 | -44.1643 | 2025-08-30 04:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 79529364-04bb-3fc0-b4b3-6d35bcf245d7 | -9.0799 | -65.4349 | 2025-08-30 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9dda2c42-e72c-34f8-b6dc-cac1209e3ff1 | -9.4433 | -60.5499 | 2025-08-30 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| f8017229-ff9d-3e47-b06a-321e2bc3c741 | -6.1853 | -43.3257 | 2025-08-30 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 2ed5a1bd-5c64-3df2-8c43-532dc3fa6b87 | -6.1665 | -43.3273 | 2025-08-30 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 320638ba-502f-3f32-826f-62185547e0b3 | -9.1156 | -65.7513 | 2025-08-30 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d5a007d4-9189-3965-9e6e-cc092904827d | -9.1155 | -65.7699 | 2025-08-30 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9380db30-3d17-3170-9dc0-8f4fc6a951af | -9.4432 | -60.5692 | 2025-08-30 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0f8b6044-fa45-3a40-8bed-c9a9c59fcf25 | -9.4435 | -60.5307 | 2025-08-30 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| fa0fcf8c-e167-3556-9095-40f72e1c4654 | -9.63455 | -48.29898 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8dad6508-9fbf-35cd-81ae-787e82dc71b6 | -11.27589 | -44.92501 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39f79110-5fa6-380d-aebe-048d96ba67ec | -12.85251 | -48.17363 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63cd762f-c25a-373b-a08c-c24ca1be485c | -11.8806 | -46.37431 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea9a690d-bb6a-32c0-8022-b44310467f63 | -13.73124 | -45.531 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58a52fc5-8339-38a0-8d0b-4feb7fac18ae | -10.03227 | -46.03459 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1f7f007-1e89-316e-bc48-7959b1754e3a | -12.01041 | -43.98542 | 2025-08-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| edad0893-5585-3770-a3db-7b9f18c6f15b | -11.28311 | -44.92247 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0aa437-d6c7-3916-bb1e-c0e847a0545c | -12.845 | -48.13373 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4f7860c-f002-355d-9ac3-89038e1fe242 | -15.07678 | -48.15853 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f87f811-84dc-3387-8f69-00e4a6b3ecb7 | -11.3576 | -43.54888 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d06c0ec-feb9-32c6-b466-7dcfd2dd5b5b | -13.37112 | -51.75236 | 2025-08-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa449c57-8162-3669-a807-219f10e8c296 | -10.37591 | -57.84097 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d51a9ed9-c2c2-3637-be52-08316e7cec1c | -13.55139 | -46.95275 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a60216a0-aba7-3a2b-88d9-5bedff8d2eb3 | -14.37482 | -47.84802 | 2025-08-30 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7206c785-3762-3ea7-b428-3e0642ec55d7 | -11.73242 | -51.75415 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56418009-fac2-320f-9151-af2b3ee58020 | -12.83542 | -48.12818 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f1f7493-5168-3ded-89b9-2e2de93eedaf | -10.36629 | -59.20498 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9eb87e5e-fd88-300c-a9bb-9d694138caf0 | -14.62248 | -48.08114 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 865a261b-ef18-3b92-8954-d3cf8c155681 | -13.35637 | -46.8735 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cac2b5e8-937b-32cf-8f69-9a3e7da4b522 | -9.57546 | -54.49535 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 586b2966-052d-3c98-b331-249dc8428ca3 | -11.07444 | -44.59538 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 940eab18-d063-3842-8df1-1848a31a883d | -13.4974 | -46.84212 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d203040-3785-3587-97ff-78c6e7ebe6d8 | -11.15077 | -47.15667 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83eed14a-e3d2-3c8a-ba41-baeeb849c9bb | -11.22666 | -45.00129 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 056f9996-0813-38ef-a49c-131f9210ed16 | -9.58416 | -54.47159 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e36fb03-43ef-36a7-bca5-fae635a8f19e | -9.57844 | -54.47358 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bda6f8a4-8451-3c46-a3a1-d9197041eb02 | -13.55912 | -46.94678 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2027c7eb-5bce-3185-a5a1-fa77dfdc31c4 | -11.07316 | -52.03592 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4159a4a1-4f51-3318-aae0-7f9ee5962a22 | -13.19801 | -45.28826 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c4c056d-9c2b-317c-a5b9-058eed5b29fb | -11.30264 | -43.63222 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1930e32d-97de-3493-bca2-4cddce8aaef0 | -14.00758 | -44.57123 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f702cdf-0fb7-3c49-b788-db7b19749386 | -10.02897 | -46.03408 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd24ee20-75be-3eb1-965c-a80c78bdeef1 | -13.3971 | -47.00381 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 828ae613-3412-3c81-95b0-4b5c259b0d4f | -11.0717 | -44.61343 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 427a3279-84f4-30fb-b7ec-2fc1de17ddad | -11.58261 | -46.36526 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a178e3a9-9813-3a56-990b-dcd9a01da413 | -13.37788 | -46.97513 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80a745b9-63ce-385b-96c2-3a3e3818608d | -9.65047 | -48.33451 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4de25c28-3e3b-33f3-83d8-f9966afcd2f5 | -13.36517 | -46.88227 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26a0529d-622f-3e3c-aa75-7cf26b83ab58 | -12.85191 | -48.17738 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc1cd16c-8bc4-3bf8-be58-66b4c15f84a2 | -11.34573 | -43.28836 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3eefc33e-fb30-3d7d-8ca8-5c0d5921d074 | -11.83092 | -46.45277 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c36b5c36-ab4e-3b67-bb4e-edc05e763405 | -13.99794 | -44.58913 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b475c8b4-cc34-33df-ba47-5abae472ad15 | -13.69132 | -46.90694 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 382679d7-5599-3f5d-9b54-fb38a1b3b8b3 | -11.8392 | -46.44328 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cf2744f9-cd83-3af7-8a54-e7c51b69a2ea | -9.62811 | -47.80158 | 2025-08-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7d83ab4-e54f-31d5-8d0a-25a96e8a7353 | -14.47369 | -48.38711 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78950208-4762-33f4-88f9-4709dd1c8656 | -12.803 | -48.17694 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abcf634d-d036-3791-8d23-7392c68e6603 | -14.02182 | -44.54612 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 141bf8d0-cea3-3967-86cf-f8ed1b526a59 | -12.84851 | -48.17674 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58fd7882-ce15-34df-a456-322ef4c204ce | -12.92371 | -48.10439 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2034e134-d33e-3534-b98f-47ddd8e71d0d | -9.51451 | -54.4425 | 2025-08-30 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa17901-3055-3b84-8330-7da18a84de4c | -14.45838 | -52.02482 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17af1e4b-99fc-35b0-b39c-71cabb448039 | -9.5039 | -45.39349 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52c9b67b-2433-3a4c-8388-d73955c88710 | -12.89841 | -48.89792 | 2025-08-30 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36de6589-8b73-3ef3-b59c-90c9e2b84662 | -15.10672 | -48.18638 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 697af226-2d37-32db-b47f-f35db047317a | -13.43981 | -46.94885 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53c9b0b2-5089-3773-af35-793efed227f4 | -11.41508 | -44.68116 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ac0b52b-6f2d-3e5f-bf54-ab641a58dc3c | -12.6908 | -48.15384 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cf708b3-2986-3e9c-8da1-8ded5ce7a31d | -11.32748 | -43.60823 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dce37bd-f797-34c6-87e8-e4462a441237 | -9.68646 | -47.05156 | 2025-08-30 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 184156f4-3b82-344f-b29d-f1109fc89558 | -11.06672 | -52.04738 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af0e544d-f8e6-3505-bca2-d5998ed345f3 | -12.85033 | -48.16555 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1e1963f-b50b-382a-80ab-7e0a2a5687ce | -12.40626 | -46.47126 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dbd5370-8c72-3040-b0cc-ae05d3a0d5c6 | -9.17458 | -59.58389 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 385cc3bb-e199-3235-afcb-370105c125a7 | -14.83401 | -46.75782 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87035ac0-a614-33cf-b0a1-951e71196565 | -13.39153 | -47.01747 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b586476b-b683-3a9a-a733-fe1062c55ab8 | -10.03414 | -48.07196 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a02a1932-5fc5-3288-8978-5795cdf8ad0b | -10.66809 | -48.72553 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5875e1b1-92ad-30dd-9769-efd32db92a77 | -9.13894 | -49.62376 | 2025-08-30 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 179a1d41-2d0f-3730-a57b-d3496b56ad3f | -12.70006 | -48.14 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd9b0e78-6640-3f7b-ab6f-fe6455b76c5d | -11.413 | -46.92076 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4a82966-e467-3660-91ba-42c06d637c67 | -11.35932 | -43.58522 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7b3d3b06-8643-3478-b4b0-36c507dba399 | -10.72491 | -47.00984 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e546dbbc-2383-3352-8d26-dbd872c96460 | -14.24912 | -43.67971 | 2025-08-30 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9973c489-bbd4-3f82-8e11-50225c9682c2 | -13.39929 | -47.01146 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b7326e5-016e-31cc-8f75-7a3111aea87a | -15.0473 | -47.06675 | 2025-08-30 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b4515843-352a-3e4d-980f-8a8e57e12808 | -13.57964 | -46.90292 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bef5496-a388-3754-beb5-a3da69069b96 | -12.90011 | -44.62354 | 2025-08-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48fe680c-ad9a-32d1-8756-9b270e570914 | -11.91456 | -46.69797 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d8995af-58b5-30e5-99a6-237cbb6309d3 | -11.14742 | -47.15613 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fc4b349-ae09-335b-8fd3-e2465c35217d | -10.57248 | -44.78928 | 2025-08-30 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec8cfd99-5625-3dd9-89bb-2e53bbf785f1 | -11.86019 | -46.39624 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README27.md)
