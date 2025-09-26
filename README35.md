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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97a7ff52-536f-3590-8f99-3af970f7bbd4 | -10.43962 | -48.20292 | 2025-09-26 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d964e0a5-2a5a-3ccb-8a82-4e7e9b5b9f8c | -15.99988 | -59.49614 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f15a1c4-58bf-3c9c-85b6-762f887188ce | -15.88817 | -59.33564 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59924ba4-6413-3524-b3e4-bee845f82cf5 | -15.8677 | -50.29766 | 2025-09-26 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82bbeae1-0e2a-3ebd-ad5b-ff9f93ce74f5 | -14.94771 | -47.49963 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33506464-381b-3446-9068-4403c8e3f3cb | -11.66669 | -44.45956 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a0358b1-dcb9-310f-a5c4-bab499b37c99 | -15.07086 | -44.98266 | 2025-09-26 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 483ea915-94d4-3e52-b185-cb44d80beac8 | -16.13103 | -50.76598 | 2025-09-26 04:44:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dbd8823-889c-3a66-b4ed-ec6de66d66f5 | -15.87769 | -59.33908 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33eccf8f-44a6-3506-a02d-5bdfef8a5993 | -13.54281 | -47.70655 | 2025-09-26 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93d17f1d-9666-3488-825f-bd3396eaa702 | -15.26009 | -46.44353 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0e3665e-ad84-302f-8a8a-d669ffb8bf33 | -14.57694 | -51.4065 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b234a1b-31a1-3c83-b4ad-f0147940b406 | -11.68569 | -44.41888 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee9ebdda-b516-3192-8688-fd894e096220 | -15.38695 | -46.11039 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18bf5605-cf85-31ec-836c-201567412eab | -15.93581 | -59.49929 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 190eedbc-a912-3ddc-bd15-660e46ef6eae | -11.02346 | -44.64833 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f044b9a4-02bc-38b5-bfa7-e70a1c1439fb | -13.62495 | -48.74652 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0420d17b-41d3-33c9-9b9a-c80b9a078c6d | -16.22218 | -48.80492 | 2025-09-26 04:44:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cdd6a69-8688-3ee7-b67e-3b8937d567d4 | -10.18299 | -49.5139 | 2025-09-26 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84b05815-f1a6-3232-95ec-d73cdac553e0 | -11.61654 | -44.43515 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 2e5a9c5a-7b42-3e9a-ad44-b98a21f465ec | -13.25797 | -50.66511 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f9b6b4-dd23-3c04-8e98-126454790580 | -11.96242 | -47.88174 | 2025-09-26 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 495ec51a-a862-3340-b527-b0d75f2530cd | -11.02173 | -44.34562 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1458e35b-8a2d-31c9-acb8-730fdee9474e | -14.95149 | -47.50015 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5562d1ba-7698-3751-910f-659f83dcf3d2 | -13.28267 | -50.69791 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c6f955d-7158-3a43-94ba-e141a3de805e | -15.91348 | -57.49276 | 2025-09-26 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52a806b0-277f-3a53-94a0-1bc746234651 | -15.73275 | -59.49876 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a68429f0-06b9-3a2d-ac21-741d59c504a1 | -12.0347 | -46.58942 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60169758-d449-3cc8-930c-b0c0888c294a | -11.66727 | -44.45532 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3551238-6e59-3971-851e-426bd57c26d6 | -13.33093 | -47.30488 | 2025-09-26 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65e91f21-9f75-332d-a288-b02521ff279c | -13.69716 | -51.16265 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3155721-4d3e-3029-b6b0-a7f7cca36d29 | -11.41652 | -44.96316 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a1c65f4-0f2b-35a2-9f40-3c7ad46e1a0d | -12.87283 | -47.09332 | 2025-09-26 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 784c7981-3e77-32af-ad9c-7e322336b06a | -12.06894 | -47.97883 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8debaf0d-9c48-38f0-b8c4-4c66cb937ad4 | -13.94572 | -49.25394 | 2025-09-26 04:44:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2fb9829-bbe2-30b5-b7d3-1011c4316c8f | -16.85801 | -50.50006 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 58b49edc-0fec-3271-ba81-b984436f1242 | -15.58849 | -51.68834 | 2025-09-26 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cab93868-864a-3fb0-b30c-6710832617c3 | -11.6819 | -44.414 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d2f5495-862c-3445-9dd1-f1efac7ad526 | -13.68653 | -44.2918 | 2025-09-26 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c68471c-c057-38cc-8695-2078711ec29c | -13.85425 | -45.61708 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91641437-e92b-3ff5-91ca-82e01c109015 | -11.06623 | -48.36428 | 2025-09-26 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04b9ae97-6055-33c3-afd4-2fa361de239f | -11.24207 | -45.54696 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44e1024e-c3dd-30c4-a74e-2b2faa6bbe37 | -14.82378 | -45.40976 | 2025-09-26 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 937bcffc-1130-3e52-963c-c56ae2088807 | -13.84015 | -45.62704 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1054e1a8-8a13-3fed-86c1-67baacdb9562 | -11.6851 | -44.42315 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77f4be88-9ad6-3c79-b184-4d346ad03396 | -11.78486 | -44.90562 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afefa6f6-e501-3825-b0e4-c7ec82884d6e | -13.84485 | -45.62372 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1557f1a5-9a0f-3b47-b05c-72d8c5539484 | -16.85406 | -50.50322 | 2025-09-26 04:44:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f16ca58a-9ec0-351e-9d30-f2438d0eea35 | -12.03663 | -46.58746 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49f2b465-b7f5-38b2-b7d4-0b45c6716110 | -10.61514 | -49.5554 | 2025-09-26 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 945dfa59-78ca-3303-937d-8049a001677b | -11.01919 | -44.64771 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb2beba2-0d87-3b2f-8c02-a2a4342ca728 | -12.07131 | -47.98756 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faaefa98-d1be-3fa3-90c9-dccff2e3892e | -15.98569 | -49.5573 | 2025-09-26 04:44:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d07db8c-618c-30a6-b9f3-7201f4d49537 | -11.38445 | -44.94697 | 2025-09-26 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52ac694e-a8f9-33dd-9e3d-ae8f0b95a5a1 | -15.51452 | -50.42045 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbeba7da-e080-348d-ba79-669075670770 | -11.69609 | -44.40485 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 543d0ac9-aa6c-33c9-bf79-045124a2e65a | -11.61711 | -44.4309 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3562cb7-f3cd-3a1a-be6a-f37d119f0c95 | -11.00922 | -44.33955 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 299d697d-f52a-3807-b56e-596f8527f987 | -10.80325 | -45.37852 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e76f87ea-5c95-32a9-b406-10790a0aab4f | -13.69884 | -51.15199 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0121be3c-c3c4-3ae5-9031-ca61af8b0048 | -11.01243 | -44.34859 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 042c7b47-1315-384d-aef4-2f5fd33a2030 | -10.54491 | -47.52027 | 2025-09-26 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8fb2971-c8d8-343b-93fa-c86d9e83f18d | -11.43746 | -47.7983 | 2025-09-26 04:44:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b19382c5-f5cf-3a30-a654-111d5ad52dfc | -15.76939 | -49.93254 | 2025-09-26 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 34.0 |
| e2968fb5-d591-32de-9271-c06a065daf38 | -12.33722 | -47.99213 | 2025-09-26 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a69b549-6e2f-35f1-9e13-e8ad16348a25 | -11.6154 | -44.44365 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fde1a0d-5298-34e7-93b9-eb29030f41aa | -12.84709 | -44.70462 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e007b3cc-9cfa-357a-9557-848050698c8b | -11.69683 | -44.40301 | 2025-09-26 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fbb541e-2300-3243-b8fe-ec6155aa9578 | -11.83253 | -46.62116 | 2025-09-26 04:44:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cd5e4e0-21e6-3c2b-bf2d-7eeef008c3f7 | -10.61849 | -49.55594 | 2025-09-26 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 67bea202-7214-35da-8c0b-8a8ad8a473e2 | -11.98439 | -47.01518 | 2025-09-26 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21ea6c29-acc3-338f-aa94-66205d0dca08 | -13.27125 | -51.90242 | 2025-09-26 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e52abe4-782f-32b5-a2c1-032b26befd4f | -11.24512 | -45.55467 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 69b5bfbb-324e-3aaa-b597-894732f3049d | -15.01719 | -49.53834 | 2025-09-26 04:44:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdc1bee3-11a4-3e3b-8ae2-817f98326bd1 | -13.27067 | -51.90603 | 2025-09-26 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c81ac166-3b79-3590-a08b-add33394c0c0 | -11.24305 | -45.53982 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 632b3811-dd6c-32e8-b8fb-b4bfda36f0e6 | -12.84237 | -44.71144 | 2025-09-26 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a8ea0a1-54ed-353f-b022-c20371037530 | -14.03738 | -45.50008 | 2025-09-26 04:44:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa1460b-a95d-395e-83a5-bc102ad815c2 | -13.2613 | -50.66565 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db35a317-6c98-3abe-b14f-66c9a965e12d | -15.26665 | -51.47355 | 2025-09-26 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8242def7-1cc5-3b30-a9d5-468c043ac105 | -11.25015 | -45.54813 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 95da220c-8aa3-3f01-bd43-73b52430c78a | -13.24183 | -50.70261 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2fdf5ea-f00b-3abc-85de-4db78e090f2e | -14.5995 | -48.25618 | 2025-09-26 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24cfdfd9-542d-371e-81b2-5f3a75cd5be0 | -15.51285 | -50.4314 | 2025-09-26 04:44:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62c3c9d5-c197-3b9a-91f8-04fc828c3b0b | -15.1416 | -46.43385 | 2025-09-26 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0ce633a-26e2-3769-a95a-d2995305a2e9 | -16.21922 | -48.80013 | 2025-09-26 04:44:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e2c63dc-444c-31da-82fb-3a0d2048975d | -11.23802 | -45.54636 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 005c5e68-190a-3345-b0ea-c18345b2a2d5 | -15.13094 | -46.42157 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3adbdb97-36fa-30a7-bb1d-49debfa5516a | -14.13325 | -51.20222 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8adfc16-6cf6-3dcb-a047-85fac1ee28b7 | -11.23606 | -45.56061 | 2025-09-26 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a145c4b5-eeff-3b38-a1d9-3354ba62ea07 | -15.13802 | -46.42996 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5de5f051-0a7a-3721-b185-3667d9d24be7 | -13.65332 | -48.09462 | 2025-09-26 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8ce345a-5c33-3abe-855f-f1c52ef03fe7 | -15.5338 | -44.33075 | 2025-09-26 04:44:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d818aace-c10d-3b00-a509-402504b0a8e7 | -15.90811 | -59.33664 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcf0d65a-1b1b-3396-9bd2-5ee62b98a40a | -15.38509 | -46.1244 | 2025-09-26 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1dbf093-655e-3bcb-a17c-10ca8cf90ab9 | -11.00864 | -44.34377 | 2025-09-26 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62d02c4e-db52-31d9-be85-e77fc9bba076 | -13.27532 | -46.97297 | 2025-09-26 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0789c317-f1c0-3bf5-b67e-10504a7e3ca2 | -13.70049 | -51.1632 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29895abf-7966-3e75-9d5d-569c696fbe80 | -14.12992 | -51.20167 | 2025-09-26 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77197841-53a3-32fb-bd02-21a8c348d61b | -15.88832 | -59.33731 | 2025-09-26 04:44:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
