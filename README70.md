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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fb05b1c-7066-30f4-a71e-73ff4da495ec | -8.60487 | -64.1018 | 2026-09-16 12:46:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6bbed24c-1d64-364a-a9b1-7468fbcadc54 | -9.01543 | -61.01735 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e63910d1-6ad0-3426-ac52-0d6682c31858 | -7.65603 | -67.1575 | 2026-09-16 12:46:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9e06b5c3-c5ca-3b14-9a94-55f90a90a7fa | -10.38154 | -58.31384 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 884e929f-f30c-344e-82fc-1524a4f78493 | -9.06141 | -65.91953 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6a2a4e28-d5db-39de-811b-56d19ad0186e | -9.28467 | -60.65181 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f643c05c-e67f-3afb-963c-48b39da7b1b5 | -13.45513 | -54.60877 | 2026-09-16 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 52fc9f9c-aeea-3ba6-a14f-02462769879e | -10.14284 | -61.18057 | 2026-09-16 12:46:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c84587e-cf0d-39c1-bc4d-74bfd7a65cdf | -10.39486 | -58.30026 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 298.8 |
| 648b9581-a8bd-35bf-9658-8b3e4ef7d476 | -9.3798 | -60.3104 | 2026-09-16 12:46:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ea92074a-d0d4-3b4f-a5ac-6a1a652ecde5 | -9.02305 | -61.01431 | 2026-09-16 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7fd291b8-0b2b-3e50-99c2-1b67a9a79e16 | -9.10759 | -65.55267 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7415df6d-77ab-36d0-8f65-c16be245ad5d | -11.80589 | -58.17139 | 2026-09-16 12:46:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ca6f1f69-b95b-3dbc-a04c-847e4fb31a8b | -10.39288 | -58.31536 | 2026-09-16 12:46:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 694.9 |
| 5869a5bf-ad70-3477-8bc8-32c2391ebb04 | -9.13144 | -65.85156 | 2026-09-16 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 4b69fc9c-6d7e-3f64-9e9e-62e1a0f951f9 | -13.46745 | -54.58144 | 2026-09-16 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7f955de6-4ad8-3c4d-a39c-fbb2e8077afd | -9.38947 | -60.31166 | 2026-09-16 12:46:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9e2fe324-ed63-3500-9e33-431e95f3237a | -23.1925 | -55.36532 | 2026-09-16 12:49:00 | TERRA_M-T | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| f7fd723c-724d-3227-97cb-5b126e107eae | -11.5624 | -46.872 | 2026-09-16 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ac84c767-f5b9-3a2c-81a6-a2c7cc58eae3 | -11.5436 | -46.852 | 2026-09-16 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 419d598b-319a-33c0-8a69-23bf4cce863e | -9.3564 | -50.201 | 2026-09-16 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fb3e1ac2-cf0d-3fd2-ad52-d032c9cce13c | -6.8216 | -59.1686 | 2026-09-16 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 74508348-9539-30b8-b4ee-7fd211ef79da | -6.8032 | -59.1693 | 2026-09-16 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 286.0 |
| bebe0501-66cc-3c94-830e-beb5c9a06a86 | -8.8585 | -44.9149 | 2026-09-16 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 07c4ed43-7ee8-36f0-b1f8-f417a8dcd616 | -5.144 | -55.9345 | 2026-09-16 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 18bd0150-7503-3efd-b809-b02244b790f3 | -7.0454 | -42.0427 | 2026-09-16 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 369.0 |
| 5a6c8ff3-5566-38cb-9d25-cac46fda5ece | -10.0982 | -45.6141 | 2026-09-16 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| c897dcab-ebe1-391b-8260-7cec09d7a82c | -6.7892 | -48.6563 | 2026-09-16 12:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 110.9 |
| aa944d62-1212-3ae2-b4f2-bf55c67b681b | -10.8571 | -50.8183 | 2026-09-16 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 015a75c0-ec5b-3469-ae02-b5550365190d | -10.8495 | -46.1771 | 2026-09-16 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 61c22877-4373-31e1-98a4-4b7a9a7c30b8 | -10.8492 | -46.1998 | 2026-09-16 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 0a54664d-cdce-3469-8683-6b2bc540846c | -13.287 | -51.2832 | 2026-09-16 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 90e57f3e-29dc-3fdd-92a2-fb7170d55bca | -10.876 | -50.8163 | 2026-09-16 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b3141205-3cea-3fd3-b75f-1492744ef7b9 | -7.3373 | -44.4973 | 2026-09-16 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 673591bd-c5f1-3e23-97ef-d4f4ab5d84ff | -11.5432 | -46.8745 | 2026-09-16 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 2630377a-7df4-31ff-a2c8-1bffeda4da92 | -13.2047 | -51.6342 | 2026-09-16 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4142f926-fcd1-375d-a64b-10c4147f4279 | -12.6064 | -50.7691 | 2026-09-16 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6b22cc7c-b800-3311-9a14-0b1318454377 | -13.4468 | -54.5968 | 2026-09-16 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0b59f6b7-601b-3981-9e20-5c5fd71fa9fa | -7.0265 | -42.0446 | 2026-09-16 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| d0e16f0f-7ed6-34df-b528-950b081dac31 | -9.3567 | -50.1796 | 2026-09-16 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4809846b-fdca-3757-9f10-744d9a0f9644 | -7.3561 | -44.4956 | 2026-09-16 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.6 |
| d5e2c2bc-f2e7-36a5-8ce0-b6c73649481c | -11.4167 | -51.4371 | 2026-09-16 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 255.2 |
| b5314528-04c1-3837-ab99-a1a48282d214 | -11.417 | -51.416 | 2026-09-16 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| aa705594-6d6b-37c9-936f-0985e0514837 | -12.3277 | -47.9513 | 2026-09-16 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 315d67d7-38b0-34ed-8963-5f3f54e8fcea | -13.1855 | -51.6365 | 2026-09-16 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 85ac282c-c3e0-37ee-a9be-64749c7f1801 | -6.7892 | -48.6563 | 2026-09-16 13:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 1ab0ca41-0245-3e7c-b265-b7eaa2bf1570 | -13.287 | -51.2832 | 2026-09-16 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5bb063b1-51fc-39a7-9efc-cc8a71e74348 | -11.5436 | -46.852 | 2026-09-16 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f35acfb5-6376-3262-bde7-b8daaeedd3e6 | -5.144 | -55.9345 | 2026-09-16 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9b8dc4c4-4566-31d4-bd80-12208f5e12ce | -9.3564 | -50.201 | 2026-09-16 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b64ab11e-c43b-305f-8ab0-7bb306c92d11 | -10.0982 | -45.6141 | 2026-09-16 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| a83ae2fa-7b9a-3042-b5b1-30eb5ee61994 | -6.8216 | -59.1686 | 2026-09-16 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 782e43a1-a4c2-30e1-92fc-a72b71f9f967 | -5.8695 | -52.0455 | 2026-09-16 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2e63e101-7c50-3721-9ede-6e0285d2f57e | -7.3561 | -44.4956 | 2026-09-16 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| aa78113a-075a-324b-9ce5-1dae4af217cb | -11.417 | -51.416 | 2026-09-16 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| af7ba8e5-e06d-3602-8f73-ff2267338be6 | -13.6337 | -45.9732 | 2026-09-16 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c0d914cd-1d03-35b6-b241-921428fa280c | -13.2047 | -51.6342 | 2026-09-16 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| dae7b8f5-c430-3ad8-ab1a-cfb11e6ab52a | -15.5195 | -53.8527 | 2026-09-16 13:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 70071e2f-09bd-37ca-9a8a-f734dfb24821 | -12.5341 | -47.0964 | 2026-09-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 012c7742-3d31-3c23-80b3-3471f282156a | -11.5432 | -46.8745 | 2026-09-16 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ee80dd39-ff7f-359f-8710-cae95f391dc5 | -10.8492 | -46.1998 | 2026-09-16 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| acb899f9-06c0-3bbb-a976-d0a073eefbc5 | -10.876 | -50.8163 | 2026-09-16 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 39d61096-6de5-3590-8030-c42d774418f8 | -11.4167 | -51.4371 | 2026-09-16 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| d9d41c75-0a18-3c59-a41e-6ce9653611b0 | -7.0454 | -42.0427 | 2026-09-16 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 28969a47-bb37-38c5-8b98-a55decd4fe10 | -11.4857 | -45.7508 | 2026-09-16 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 9aaa82bd-12bc-3743-ae48-ead578c965bc | -6.8032 | -59.1693 | 2026-09-16 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 372.8 |
| 92368078-1501-33e0-a46f-6fec0da882ac | -15.4623 | -53.7972 | 2026-09-16 13:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 42d78d01-9f30-3fbd-ba18-38f7b82ef875 | -12.3277 | -47.9513 | 2026-09-16 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| f3c0b0a6-7668-3032-8f4e-ee8396d65207 | -9.3567 | -50.1796 | 2026-09-16 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 198e51e5-0f38-325b-81df-f0f29aa6e9fa | -9.1337 | -65.844 | 2026-09-16 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1129522a-350d-31ef-8cc2-7ec0ecb9c41e | -5.851 | -52.0465 | 2026-09-16 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a893340d-a59b-3872-8b49-4f58981ad185 | -10.8571 | -50.8183 | 2026-09-16 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 98303c68-9900-3972-b2f5-bdc23fb6a93f | -9.2311 | -46.7055 | 2026-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 542042f0-c705-308c-95cc-585096a346b6 | -13.6531 | -45.97 | 2026-09-16 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f6a911e4-f58e-3b5e-8a2a-a258f41a4d0a | -12.3085 | -47.9539 | 2026-09-16 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6f839d2a-9f90-3f01-9714-5c3d56f0a29c | -10.8495 | -46.1771 | 2026-09-16 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 0bd87c9c-cd43-318b-b6b2-12d15549a51d | -11.3642 | -43.9407 | 2026-09-16 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| a5072d33-a433-3417-a9b4-8c1112d890b2 | -9.3567 | -50.1796 | 2026-09-16 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 212.3 |
| be01c0ec-cd63-38ad-80a9-f0f497fd2f38 | -6.8032 | -59.1693 | 2026-09-16 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 459.4 |
| 514846fd-8c38-3fad-b92d-7b3bc79d744a | -13.6531 | -45.97 | 2026-09-16 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0a5a4474-a5a4-3b9c-a415-da410c94c984 | -9.3379 | -50.1814 | 2026-09-16 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 40532cf6-a387-31aa-96d9-8cbcec6f4454 | -6.8216 | -59.1686 | 2026-09-16 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 376.3 |
| 6c7035a2-85bd-3201-83da-0196e144aa4c | -11.5436 | -46.852 | 2026-09-16 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2a2c8964-c5d1-3df8-aed4-ba8f56f9374f | -10.296 | -51.8655 | 2026-09-16 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5e33352a-d1ef-372e-b545-c4b91a65e085 | -9.2311 | -46.7055 | 2026-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8a7bcb55-c5a1-39cc-a3c7-7127f4054626 | -13.2047 | -51.6342 | 2026-09-16 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1a95986f-b130-31f3-bd7c-ec7b7e54c15f | -13.287 | -51.2832 | 2026-09-16 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c37f9376-0dc7-3959-b9ff-daae73ec58b9 | -15.5195 | -53.8527 | 2026-09-16 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 48c3e2b3-c9f2-3086-8c31-f6f19765e8df | -5.1439 | -55.9543 | 2026-09-16 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 47347813-44aa-3a6b-8a4a-63efa92521d5 | -12.3273 | -47.9735 | 2026-09-16 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 927df55c-8b1d-3af4-be04-03632debcfa0 | -10.331 | -45.2883 | 2026-09-16 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b0b5461d-8335-3b9b-9626-630f5d564f0f | -15.5199 | -53.8317 | 2026-09-16 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b8f363a7-a672-3d71-99b4-46e76ae6c13f | -15.5001 | -53.8552 | 2026-09-16 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b15bf5ba-efa1-38e9-ac34-a4dfb93a8b0f | -9.1337 | -65.844 | 2026-09-16 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 00a99a9e-7255-3211-afd8-fdfaf2e4f10d | -9.6922 | -52.0041 | 2026-09-16 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2683ae96-2a13-3f01-9e28-0cb7634245d2 | -10.876 | -50.8163 | 2026-09-16 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f302aec0-b214-3191-9107-afc50d18b683 | -7.2691 | -45.5737 | 2026-09-16 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 6cab2ac9-254d-300f-b153-f1b1d536e1e5 | -12.3085 | -47.9539 | 2026-09-16 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| fecffd24-6374-3c9b-a2f7-baae906628da | -2.6966 | -57.6084 | 2026-09-16 13:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 211aa351-b9aa-3624-9ffa-6678a63185e8 | -10.8301 | -46.2022 | 2026-09-16 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |


[Clique aqui para ver as próximas entradas](README71.md)
