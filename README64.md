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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3724a2e6-9e35-37ba-a333-3dd6483a5acf | -11.81987 | -47.59555 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 487cd1fe-764d-3c68-9daf-4659817ed92d | -11.4687 | -45.06213 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54a2b21b-9263-3643-a067-1bd33b7f63ac | -8.51493 | -47.82624 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a6f9f78-32e5-3e8c-ab5e-314cd9f1122f | -11.58267 | -47.66219 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b50799c-d1d5-3861-800a-582a9940520b | -11.46473 | -45.01711 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8fa54bf-cde0-36ab-9d63-5c4d32f944a0 | -11.87048 | -45.02273 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 342db218-b889-3689-a72a-be0dc809f372 | -10.20578 | -50.2708 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1f8de285-9eda-3f61-927b-0a8b5064e12a | -6.71094 | -44.62645 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bd492cf-2606-3a8d-95e3-52a57e9a302c | -11.67084 | -45.32547 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2187a3e5-da6f-3f96-b654-1e5209425185 | -7.56149 | -42.40364 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 596648eb-4659-389a-940c-bcfc0beb9585 | -11.921 | -47.0611 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d984e5e-9e44-3fe3-bd90-557256f8f4ee | -11.44407 | -43.89425 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65a94737-bb41-3d92-8953-5d35e29d1a9e | -10.83793 | -46.63144 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f4b3d1e-245a-37ec-95b5-034700f8b5de | -6.66282 | -42.79644 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 38b4507d-c8bd-3e0c-9db2-9732ea623784 | -12.75563 | -39.73521 | 2025-10-02 04:29:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3ea7dac4-9740-39e0-be94-26baeb7417fc | -10.83738 | -46.63498 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 11215e75-f348-3174-beca-a5cfd16664c5 | -11.81888 | -45.03082 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87ebfa59-60e5-3ac0-8b38-822477abd09e | -9.9379 | -43.73669 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a0d1250d-0c3a-3f0e-a9f1-73239962cb23 | -11.17628 | -47.27869 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5b534f5a-2364-3b07-aae8-474bafc3cb92 | -6.0267 | -46.35055 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e90ff9f-a583-37e9-9e33-01a7754494e2 | -6.66717 | -42.79272 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2e5c8c0d-d193-386f-b111-650a21a2ac7d | -10.6522 | -48.50348 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7533c61a-4f6d-36c9-8c02-91a873ebe334 | -10.93157 | -48.5869 | 2025-10-02 04:29:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370bc21c-c2b2-39e0-be41-7b35697f517d | -8.90367 | -47.60104 | 2025-10-02 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe295db9-cdc9-3471-bd9a-2c7f89261e3b | -8.90006 | -45.03482 | 2025-10-02 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fc0d3cb-7198-36f3-8334-608a695b359f | -7.01908 | -44.50906 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ca4157c-20f2-3b6f-86ea-ebb9214e84c1 | -11.08244 | -47.84869 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f38b7d7-4706-3e1c-a721-4dbc315c1082 | -8.82371 | -44.78888 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d49ee8d2-1db6-3a58-a08a-4b5799172c90 | -10.69228 | -48.57687 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0501399d-3f97-3fe9-8473-bad2ade2e6c1 | -7.75267 | -44.78975 | 2025-10-02 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5a0028f-6695-37df-9ecf-c7f7094d4b91 | -11.00543 | -46.5814 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8dd057f-2feb-3c60-b4ae-827b1c6f6dab | -7.40843 | -45.19126 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13f1b62f-5319-3ae6-892a-5e9f1f64e6f8 | -11.35709 | -44.96521 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13edb53e-0d38-3d77-8212-90737218ef76 | -7.56533 | -42.40417 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4bce219-0b73-3b29-aee3-aca153048522 | -10.42923 | -47.47194 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3470688-e43e-3743-8db1-39c3ad5e712e | -9.4541 | -45.47422 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c985405d-c6aa-343b-ade0-c8a5b00c6831 | -5.84013 | -45.75516 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2cd36bc-b3c2-3ed6-a554-0d63fc8e606d | -11.53505 | -46.95277 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4bdec82-3c5c-3291-b66c-3506ddbb0cdd | -11.85702 | -44.992 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 933bd78f-6ca6-3b24-b0ac-f5d6d1107931 | -11.46414 | -45.02106 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec940b10-4686-3113-b9f4-76268d944019 | -8.90423 | -47.59751 | 2025-10-02 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f682795-0111-3ea5-b662-fcbdc2ec2207 | -10.25502 | -50.31202 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| da633178-7045-36d2-b6cb-c8d56a971d98 | -10.88704 | -44.28031 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ac182d3-31eb-3dba-9d29-54fc86f7d654 | -11.59184 | -45.05526 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9ba2065c-c363-3caf-86b1-aae7bdd322bb | -6.68917 | -42.82318 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b11303ca-55ad-3fc8-bc72-58f8cd6e199b | -11.26776 | -47.81714 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99f78ed1-b16a-3f54-a3d0-3233729c23f4 | -9.93899 | -43.75448 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78a75840-d4d6-3a8c-be13-a9786ab1c31a | -10.8329 | -46.61974 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b1c03bc-c562-3665-91a9-c7a41665b99b | -9.69649 | -48.94157 | 2025-10-02 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 725ea8ee-d3dd-3856-819b-02a9207683e6 | -5.8368 | -45.75463 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15c952d3-fd9c-3bd2-813a-e29a1cacaf77 | -10.8852 | -44.29285 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72ac8b0f-e15d-3435-af4c-6983b60c8c1a | -12.11405 | -43.43277 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ca903a6-cd32-3896-841e-e9abe1e26184 | -5.88046 | -45.81913 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1453016-1f0a-3ce0-b70e-5efdf20df839 | -6.32839 | -43.04703 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f67a7c0a-4afe-3dcc-abfd-93227077a9d4 | -11.27386 | -47.82175 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc1a64f4-f5cc-3ce7-83a1-f6194d9cdf59 | -10.23482 | -50.32151 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fb4ea469-bd5f-3849-916b-d37de3be70ae | -7.01506 | -44.51229 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96dea6c-0e3e-390c-922c-a419cfa2c75a | -9.00094 | -46.70778 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf3ca27-d22d-3d75-8dd9-058f90782e6f | -11.6006 | -47.22398 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4eb0bc5c-cb26-3220-bea5-16e7d51190bf | -11.14965 | -47.19534 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9a7bdd1-a9bd-33d5-947f-df47570c65f8 | -11.26278 | -47.80545 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4abab40c-7344-3150-90fb-1ba65572b864 | -10.22878 | -48.22048 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80baf2d3-979d-3e33-8491-db626099d65d | -10.63578 | -48.5193 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dfb2120-8e3f-3711-ab6a-8d28385bf842 | -9.41897 | -47.35572 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af181b4c-7090-3dc9-b435-bccea343e891 | -7.29054 | -42.81789 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01e78105-883e-3bca-b1f4-eabd510024aa | -11.53128 | -43.55149 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 218886a0-1f25-320a-a1b3-9681ca0361fa | -6.963 | -45.31823 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee1e60c-888b-3a35-8c88-c7b79ef185c4 | -10.68726 | -48.56505 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a175240-6124-3576-9e7c-103f73c0e8dc | -10.25863 | -50.31264 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3108b9b1-30c9-3055-b078-fe422f50dd73 | -9.95021 | -43.57832 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6419dd12-dbf4-3f4a-8bf9-2a0d860ab0b0 | -9.93579 | -43.77583 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cdfee882-c872-3ecf-9082-7164028045a2 | -11.59782 | -47.21991 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 628a525d-598a-3845-8c1e-f6def3822a63 | -6.52382 | -49.76451 | 2025-10-02 04:29:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a87422fe-af69-3581-9c70-e0d1cd6f997a | -10.29098 | -47.93067 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3ca241b-5add-3eb3-ad0a-c8d9cb047c01 | -9.8444 | -49.95791 | 2025-10-02 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8711935-c817-308a-a23f-ce6a0ef660fd | -11.81489 | -47.58387 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a2f7647-7d83-31f5-8e53-e7656fad0998 | -9.89607 | -45.95416 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 321cf151-1751-3e47-a175-5b287d9c5bb1 | -7.03608 | -43.33624 | 2025-10-02 04:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9dbab0d4-bf47-3e18-8976-d7b94289867d | -11.17517 | -47.26408 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 81935a42-5175-359d-a920-424615df4af2 | -6.79805 | -45.96638 | 2025-10-02 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d0444a9-95b5-3e04-b4f0-3e58e9457699 | -10.89663 | -44.29029 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb7fcd94-2960-35fb-9e4f-de44e2591f33 | -11.77314 | -46.83401 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac004018-d430-38b0-90bb-883855a1fa13 | -9.40623 | -47.3285 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f20298-7987-3554-96df-f15bd052ec5d | -11.17905 | -47.26111 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 365ebc2d-f834-3670-992a-85224adabafc | -11.00208 | -46.58087 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdf49d0e-d96b-37ce-8c08-eba670944a53 | -8.90605 | -46.66416 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e86b899-34a8-3406-ab86-11f146d7cc72 | -9.9269 | -43.73503 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 727400dd-cfa4-386d-ba1c-4b4bd06a808e | -6.49126 | -44.28889 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22fff10d-b198-3fc2-bbbc-f59727c9fb24 | -11.99663 | -46.57558 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d3f636-268a-3518-a978-a688fe51549d | -8.90327 | -46.66013 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c57022a9-6bf5-3e8d-ba5b-4a37958c59e7 | -10.83124 | -46.63038 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5ec79b1-ad82-3058-a533-c2a039899911 | -11.29138 | -47.83221 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8301b769-4401-3240-a8bc-01ae1e40d106 | -9.04689 | -46.65416 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ba195f2-7948-3a00-9621-e749bcd1729d | -11.8294 | -44.98365 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a870b4b-ceaf-3888-a84d-7e90ce36815b | -11.1563 | -47.19641 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0aeb498-b20c-3a8b-b5e5-f2601273eac0 | -10.30867 | -48.24825 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d45ff8-9caf-3c28-afa8-af8f22568872 | -10.84127 | -46.63197 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4b0ef3f1-2d4f-3954-9242-bfbaa0fe5933 | -5.96236 | -45.71069 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1221194e-2696-34c3-813c-0618e59a766f | -11.79931 | -44.9683 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7518bd89-5c19-34ca-9064-6bfe6ba7ad11 | -11.06364 | -47.81656 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README65.md)
