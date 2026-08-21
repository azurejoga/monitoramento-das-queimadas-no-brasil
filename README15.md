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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e93816-c799-330f-9522-49e3cf595f2b | -10.7781 | -50.3074 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cf44c5e-c737-3b25-aa44-9e27df20e6d4 | -6.8777 | -43.745499 | 2026-08-21 00:42:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72f8b98f-02b2-39bb-a029-a79a79db8216 | -7.7213 | -46.165298 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aec65c72-a13d-35db-82a3-39104ba30d7a | -12.7942 | -48.398102 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a729275-56b0-3578-827f-0dcd0011a420 | -11.2085 | -55.043999 | 2026-08-21 00:42:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aebdb3fb-acd6-35e9-98a1-ec791de98e6a | -11.3712 | -46.363499 | 2026-08-21 00:42:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4749f76-5f98-30b8-9c1b-4b89a84bfbd8 | -11.1702 | -54.0159 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18e5e1d0-726a-32ad-b9e9-c9ce943ff93a | -9.997 | -48.559101 | 2026-08-21 00:42:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d634bf3-f283-36d5-a6de-3a184aeb652d | -10.6577 | -49.022202 | 2026-08-21 00:42:00 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddfcfa53-5e1b-3628-a415-efa080b8c6b3 | -11.484 | -45.084099 | 2026-08-21 00:42:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2bff6c6-50d1-3f88-8c03-09d192fdd4fd | -7.38 | -45.811699 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7023ba59-e49c-3bdc-b62a-11bb5ae7698e | -6.868 | -43.747799 | 2026-08-21 00:42:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80312884-9d49-304e-8f58-bd880237500b | -18.0315 | -44.616501 | 2026-08-21 00:42:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a06d436a-c452-3e72-9355-d5a40c410376 | -11.486 | -45.0924 | 2026-08-21 00:42:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02081cfa-19d2-3ca1-bd52-f94b1110116b | -10.27 | -50.287201 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ff237bd-9ca2-3122-b8e3-1446b254fed7 | -19.698 | -46.936199 | 2026-08-21 00:42:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 250ecede-435a-3b8b-bb61-83b7e8cc3125 | -7.3487 | -45.810101 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fa7392a-f6b9-3b75-bcd3-c149b58b9f23 | -4.111 | -48.931 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63c02b70-965a-3f1d-bd32-1d80f8d6b3ad | -6.8898 | -59.419201 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43334f65-4d23-3162-90f8-4e0fb86187e3 | -8.4457 | -46.968899 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 369919be-855a-31b8-9c30-ca029d38e346 | -20.835501 | -47.3535 | 2026-08-21 00:42:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fb6df43d-d263-351d-ae8d-7d55bea5e45c | -3.9637 | -43.103001 | 2026-08-21 00:42:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1cb856-cf3e-3f50-b79a-9196aaa348e7 | -11.2015 | -55.059799 | 2026-08-21 00:42:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef62c30-f6d4-3995-a8e8-50c470ccf9ad | -20.312901 | -44.605 | 2026-08-21 00:42:00 | METOP-C | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ab0cc9c-7f13-3cea-b39d-6ea88e8cfe75 | -13.4357 | -51.797001 | 2026-08-21 00:42:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 567b74aa-2fa3-3a5b-a3a6-6689b1c6d695 | -8.0694 | -50.109501 | 2026-08-21 00:42:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c872ce6d-7e36-3ce0-a666-48dc93ddae34 | -12.5038 | -54.766399 | 2026-08-21 00:42:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d318a85c-16ae-3adb-bf2e-fd7f96ea77f5 | -3.546 | -48.179199 | 2026-08-21 00:42:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f45674f-2990-3199-93eb-bc4b6607ee0c | -11.1565 | -50.7687 | 2026-08-21 00:42:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ced7dd4d-5c6d-3044-abbb-bb6862883eb8 | -5.3246 | -50.955299 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37304ac-0b39-3387-9379-6be1814c7e08 | -11.6633 | -48.362301 | 2026-08-21 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93068cad-ba42-3127-8d0a-aa2b9fc93350 | -18.206301 | -50.749298 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56d6b0b9-b1fe-3a77-8d1d-9391fa2bc27f | -7.2585 | -49.893501 | 2026-08-21 00:42:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179bd4bc-6508-388c-9f64-e1b1eaa1fd32 | -7.3788 | -45.8344 | 2026-08-21 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 59d8d7e0-b285-33bf-b52b-c4bc6d20a393 | -10.7693 | -50.3162 | 2026-08-21 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 7c960923-b140-3c7f-9a5b-233f051c3089 | -13.4117 | -54.3737 | 2026-08-21 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 109ca9cd-efec-33fb-8297-2a99b8a11e7d | -10.769 | -50.3376 | 2026-08-21 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2631c57c-6ce1-35a2-ab68-48bdb5478285 | -11.1745 | -54.0421 | 2026-08-21 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| dfe53db1-46a5-37c8-9bd4-194abe82fb01 | -6.2155 | -55.6316 | 2026-08-21 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ee7493cd-303d-3e7d-98be-0dddb734b631 | -18.1934 | -50.7554 | 2026-08-21 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4ccfe752-99fa-3131-bae4-21fab77f83ec | -11.1558 | -54.0233 | 2026-08-21 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 28e5abe2-ace9-31cd-a56b-e76e8a3c92a7 | -10.7501 | -50.3396 | 2026-08-21 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| d4175f77-2816-3fa4-979a-35c546cba191 | -20.9552 | -49.1439 | 2026-08-21 00:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 6fea977c-7424-3653-9f25-54f76c0821e4 | -3.5591 | -48.1882 | 2026-08-21 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6667eca0-3053-3b77-8ce2-c2edaa7494a3 | -10.7504 | -50.3182 | 2026-08-21 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e52e8c08-e6bc-3012-89df-b72c5f6d49f6 | -13.3923 | -54.3965 | 2026-08-21 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d1ab1caa-f710-3bf6-bfd3-dec40002ba41 | -7.3791 | -45.8119 | 2026-08-21 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 317.6 |
| 9db1a2ff-37a9-3b62-80d8-543e00388480 | -7.7887 | -61.1626 | 2026-08-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 77e15563-4c1f-3f3d-99a3-608ab68e718e | -7.36 | -45.8361 | 2026-08-21 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| f3eabb57-bff3-358b-bc91-91cb36f93742 | -3.5221 | -48.1896 | 2026-08-21 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 29d2ae18-6a13-363b-921e-b290613a2285 | -18.054 | -44.413 | 2026-08-21 00:50:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 1567798d-3155-3e5f-a401-8b8c1ec0dcba | -9.2071 | -59.771 | 2026-08-21 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c6593591-68ea-3ab5-92cb-ee2aaa8a9666 | -8.3903 | -62.6963 | 2026-08-21 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 08c6d0c9-aa0e-3ed0-af92-482a5a04bc2e | -18.0533 | -44.4372 | 2026-08-21 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 10280a63-1ec2-38f1-9f68-7e863e6564a3 | -10.2595 | -50.2838 | 2026-08-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 907cda77-73a2-3ad9-9313-217224c23a73 | -6.2156 | -55.6118 | 2026-08-21 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 723ed8c2-a8d3-39a5-8b7a-97d34ea456f1 | -13.4114 | -54.3944 | 2026-08-21 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 83867b09-29bb-3be1-b0b0-ea5514e5a7f2 | -18.0741 | -44.4083 | 2026-08-21 00:50:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6532af8c-1488-3481-aa4d-41d618dfb3c4 | -6.1361 | -59.9063 | 2026-08-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 22a471c3-d3dc-362b-a23e-a99f6eb58855 | -12.5104 | -54.755 | 2026-08-21 00:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 61f810f1-de20-32ee-a6e7-d9d4a53919b6 | -6.6938 | -58.942 | 2026-08-21 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 4f6b50c3-9ccb-3bb4-88c6-274789b02dd1 | -11.175 | -54.001 | 2026-08-21 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| a06671bb-1026-3a84-9547-8e17191380cf | -6.2341 | -55.6109 | 2026-08-21 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 5eda5a3d-d821-33fe-a532-893a6a920b4c | -6.9517 | -59.0086 | 2026-08-21 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 214f6aed-ef77-33ca-9584-23a285fed867 | -11.1747 | -54.0216 | 2026-08-21 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 209.4 |
| 3bdd83e7-af5a-366d-8465-3a82ac2e1a7a | -6.7123 | -58.9412 | 2026-08-21 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0a4ebbad-6926-3a00-9787-6b2bc1ab09cf | -6.9516 | -59.028 | 2026-08-21 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 893e1322-e537-33b9-a08f-4949d118a511 | -13.3926 | -54.3758 | 2026-08-21 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 9b856e39-4455-3f55-94fc-2077513a3adc | 2.5983 | -60.697 | 2026-08-21 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9649b68c-1a7e-38ae-8764-4adb693b28da | -6.6939 | -58.9226 | 2026-08-21 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a277f231-58ae-3497-aea1-e8495fcaeb97 | -3.5407 | -48.1673 | 2026-08-21 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 7fb14ea8-6d67-3d78-8076-ffdfbea01f3d | -10.2592 | -50.3051 | 2026-08-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bb4bbc30-3f94-3f41-a00e-cd1395ad6509 | -7.3603 | -45.8136 | 2026-08-21 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 338.4 |
| 85f429a4-5dde-3ce9-9a64-e57a3d679339 | -10.3148 | -50.3848 | 2026-08-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f7d69e0a-3027-3eba-8ffd-3cbfe122784c | -4.0943 | -42.5097 | 2026-08-21 00:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 036a6d8e-0622-340b-8f6b-ddc871d31091 | -3.5406 | -48.1889 | 2026-08-21 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 198.4 |
| e8989f53-f087-3db5-9aad-bb32b130a3a8 | -6.1177 | -59.9069 | 2026-08-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 79587540-919e-3efa-9c7c-0a2efcb1c01b | -7.7702 | -61.1634 | 2026-08-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 505abc6a-7635-34dc-b581-f85e7c2b7edf | -10.7311 | -50.3416 | 2026-08-21 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| bc76e562-232b-3fdf-b594-14f4b27bdf8e | -18.0285 | -44.6113 | 2026-08-21 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bb02c609-6e94-329e-bc2a-75677fd87667 | -18.2134 | -50.7518 | 2026-08-21 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 7e36ece4-e5fb-3e2c-9721-adcadb026016 | -11.1747 | -54.0216 | 2026-08-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 238.1 |
| 2e984bd8-2486-3daa-8f5d-81a68aafcf52 | -6.1362 | -59.8871 | 2026-08-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 21c47dc6-e01e-3621-9ad8-110d2e638403 | -13.4117 | -54.3737 | 2026-08-21 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 19c1c0e4-087c-316d-8b7c-61be1b2273ff | -7.3788 | -45.8344 | 2026-08-21 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| c39def5d-ec91-3014-b2d9-e206d6afdf58 | -10.7311 | -50.3416 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a872f527-3cb9-3bfd-aee7-8b3e24c7fbab | -10.7504 | -50.3182 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 829069ba-283d-3303-a176-1163bc5d08e0 | -10.8075 | -50.2907 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6928d152-2ad1-3043-af5d-508ee2c03a94 | -6.2156 | -55.6118 | 2026-08-21 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 092f46f1-5a98-3d10-9ef2-1125969333af | -7.3605 | -45.791 | 2026-08-21 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 51fd9c3d-5341-34f0-92b0-ebe9d598af4d | -4.0943 | -42.5097 | 2026-08-21 01:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 9537ebc8-0590-3baf-b414-6722301cecf8 | -12.7401 | -48.47 | 2026-08-21 01:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| be73cd4b-f9ed-3080-8e3c-7ca99343b3be | -18.2134 | -50.7518 | 2026-08-21 01:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a24808fe-8af8-3328-8dd2-c1a63dcf846d | -11.175 | -54.001 | 2026-08-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 20ca8124-bb79-3600-840a-9ee8c4415a53 | -6.1177 | -59.9069 | 2026-08-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 53524927-5a91-3a0a-921f-aee079f667e1 | -3.5407 | -48.1673 | 2026-08-21 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3ad3b6e8-b996-3d6b-a230-35d4bf0b81cf | -6.1176 | -59.9261 | 2026-08-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 5f3c6f42-18db-3767-8b56-48113f1a68c3 | -7.3791 | -45.8119 | 2026-08-21 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 352.2 |
| c9a4393a-1558-397b-b6e3-eb91c47cb269 | -7.7702 | -61.1634 | 2026-08-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f7db9a98-5794-3a7e-baf4-67b433df4b15 | 2.5983 | -60.697 | 2026-08-21 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |


[Clique aqui para ver as próximas entradas](README16.md)
