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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44f59a2a-e35d-3e6f-8d5f-0eb6c05f92b2 | -11.62117 | -55.1795 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 28f3f799-76fe-34d4-9e4b-c07f9910db00 | -8.87908 | -48.49883 | 2026-06-03 05:01:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 970e77ea-44a5-3423-88c9-ed91c77dc67d | -6.98584 | -42.87691 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a91f972-cf7f-35af-9fef-26b782a9ec29 | -6.99228 | -42.87975 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 88a181fa-7b7f-3a70-bbbc-f09b49deec18 | -11.81102 | -57.35861 | 2026-06-03 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d26bdee9-0af2-3669-b492-3cb07098f1d5 | -10.87078 | -53.73497 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bc8805b-780a-3c4b-afcd-6cc28e94ed7a | -7.50687 | -55.00559 | 2026-06-03 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15b442a2-d043-3638-ad18-45846d15ad47 | -11.62337 | -55.1873 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfa0843b-45fb-3304-8865-66a10ee99b84 | -11.75817 | -47.07418 | 2026-06-03 05:01:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0134e4bf-f760-31cd-ac0b-52244c13ecde | -11.32059 | -51.3877 | 2026-06-03 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 531661ed-7016-39e2-a7e7-27e5412eacd2 | -13.96335 | -46.03185 | 2026-06-03 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80fa1349-5685-3994-9e01-87f7fef1d52c | -11.98941 | -45.15079 | 2026-06-03 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12f17914-83ff-3e35-9cb7-5eab539c6ed4 | -12.73705 | -54.20742 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8f8d89d-39e7-3102-93ca-383272bd085f | -9.08561 | -48.65304 | 2026-06-03 05:01:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca447305-f44d-3a11-a745-a1dd49fa5ae1 | -8.20762 | -49.8437 | 2026-06-03 05:01:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ada9c99-9807-39de-a4e3-fd67b79513cd | -11.48045 | -57.10638 | 2026-06-03 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93fac9c0-4775-37de-9b70-1ae4f0a2a021 | -10.55226 | -46.62819 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29fadace-f537-37ce-867c-894c549746e5 | -11.85594 | -46.64382 | 2026-06-03 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fce8b5d-60f1-3276-9a4d-ef5fbe79ffe7 | -11.13372 | -45.14632 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cdab8ce-8706-3642-af86-95da6df37666 | -8.23555 | -47.09862 | 2026-06-03 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67bd2c25-1fe9-308e-8417-f8dd456aa996 | -11.99725 | -43.78495 | 2026-06-03 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c239970-c014-3fe2-84b1-b1ea2a867474 | -11.94926 | -43.40686 | 2026-06-03 05:01:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d43b11de-8184-3c64-bbd4-3509e383fde9 | -11.26051 | -48.35894 | 2026-06-03 05:01:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b91e7e10-785b-320b-88ef-d6d25cbc6eb1 | -9.08959 | -48.65363 | 2026-06-03 05:01:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd4f97a1-4e4a-372d-82b8-2ff394670f3d | -12.17265 | -54.54002 | 2026-06-03 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be0eb1ae-1f8d-3f35-840b-35db7b5016ba | -8.23181 | -47.09355 | 2026-06-03 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ddd5f4f-aa9c-3c01-9cbd-0ff4dfb6e648 | -11.81466 | -57.35925 | 2026-06-03 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebf75c0-fb09-3577-86f6-d3df2f4abe98 | -11.5759 | -56.3448 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d46c972-032e-3f71-98b9-f9b64fe07bd7 | -11.62907 | -55.17339 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce892d5b-514d-3266-9400-91c224871c68 | -11.62512 | -55.17644 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d384b716-e274-3798-9434-21fe51f8c9a9 | -11.62571 | -55.17282 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 060f304d-226b-3a66-a072-93ad67b9edc8 | -12.73649 | -54.21096 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 784cddf5-5abc-324d-a7b7-aa06479be546 | -11.32915 | -53.9571 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3467bcc-f157-3e49-9d5f-4046ef0076dd | -10.90565 | -54.13389 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bf2aa80b-9463-3a71-8192-5850fdfa4a83 | -9.18176 | -58.05444 | 2026-06-03 05:01:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f0f41235-321f-396d-923a-2109a692e7c7 | -9.89066 | -52.44244 | 2026-06-03 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f98df8a-09b9-31b5-90ce-2d0d442e8685 | -11.43603 | -54.09341 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e82475af-7c98-30c2-9e8b-f5e9dd96541e | -11.56478 | -54.57878 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd870321-af41-3e59-87e5-b28cf0bc5715 | -9.17783 | -58.05377 | 2026-06-03 05:01:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a85deb52-f35e-3597-96e4-6b21b3707694 | -7.04582 | -45.06188 | 2026-06-03 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4f24007-de1c-3aa2-b0ec-e913665833e3 | -11.26607 | -53.97226 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67243460-92f9-3e6a-ad33-670ee46c1f2a | -10.57016 | -57.31856 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d9add5-7e69-316e-8cac-f6f51863ad26 | -11.62175 | -55.17588 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b64abd7f-2abf-39cc-bdbe-2e5f956b242a | -7.83576 | -55.40409 | 2026-06-03 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef97cbee-b3f9-361c-8976-3b4f8dce1738 | -11.79696 | -47.33329 | 2026-06-03 05:01:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e813e3ce-0c3c-3c01-9e6b-5b3d15777534 | -11.26663 | -53.96874 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82160351-ca23-3f8d-a2b4-34e2f76e5735 | -7.59709 | -46.46372 | 2026-06-03 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7111f79c-3883-3ef3-8c1a-cb16dbbf515e | -7.27132 | -46.80791 | 2026-06-03 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a055f0a-73e7-3ade-b1a2-dd244bd0cfc7 | -11.99148 | -43.78421 | 2026-06-03 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77320ac6-36b1-34ed-9511-66592c4946a0 | -8.87604 | -48.49983 | 2026-06-03 05:01:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48a4697c-b7ff-359a-8e54-d16439fafc7b | -5.28148 | -56.01797 | 2026-06-03 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0e8e33e-69b1-3e7c-9507-64462cfc31a0 | -11.26558 | -48.35841 | 2026-06-03 05:01:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48002d0e-9970-3b4a-8671-84b14e86bf94 | -10.31676 | -55.10325 | 2026-06-03 05:01:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 428fcb2a-a043-3e73-ac16-79122bccd118 | -10.85801 | -53.75095 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 313aae47-eb34-3894-a61f-84ddfd810ff1 | -12.74206 | -54.19733 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fca776c1-81ec-381b-87c5-d1c7d97b8e6c | -11.88509 | -57.84127 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd85898-667f-3cfa-8f8c-91ad48f309d4 | -11.6178 | -55.17893 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f6b43975-4fa9-379a-8978-33440fc11fcc | -11.80087 | -47.33846 | 2026-06-03 05:01:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec56073a-f28f-3783-a8fc-853f33d1b2ca | -11.04764 | -54.19347 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3affd5-ab9a-3914-89df-44cf640e60ec | -10.8569 | -53.73634 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54f61e28-6edd-3cd6-b011-1fc3157462d7 | -10.54572 | -46.62603 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfd2024f-cf76-3cd8-bceb-5d1e24467193 | -11.79614 | -54.02194 | 2026-06-03 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a9eb05-47f4-3fb0-9e7d-2a5f0e28def8 | -6.98708 | -42.87502 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0860c7cb-4141-3203-b4bd-4d2c3e32aaec | -7.34866 | -46.21402 | 2026-06-03 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 210260a2-36aa-384e-9d19-70a78124f8bd | -10.98003 | -45.0991 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e73571ca-bbbf-33c5-8710-27bd3f998f84 | -6.74672 | -47.12658 | 2026-06-03 05:01:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee350a36-326b-3fbd-a722-7d076b8fe0fb | -11.79634 | -47.33784 | 2026-06-03 05:01:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52d0843c-496c-3081-af7c-005a0015603e | -11.57655 | -56.3409 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52ddfccc-be50-38e1-a3f5-7090b21c47be | -10.90898 | -54.13444 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d3ebde28-96ca-3e83-b6d3-90be6a76c05a | -8.87507 | -48.49823 | 2026-06-03 05:01:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 081c0ed8-0665-30bd-adf0-bad7209a272c | -11.57202 | -54.57634 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f011542c-6659-3b12-8257-448281defeec | -11.12585 | -45.12551 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ed1066e-94be-3ecf-b1c4-d1f17d82d5c6 | -11.63244 | -55.17395 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b7b0836-bb31-3c4a-a748-3ace4a031189 | -10.85302 | -53.73932 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 067bf5e6-edea-36be-90e0-7605a8bb83a1 | -10.81766 | -49.23943 | 2026-06-03 05:01:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9abaef1d-6a32-3430-a6bc-13af946c781e | -11.57145 | -54.57989 | 2026-06-03 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b7c698d-d361-35a4-bb09-e095297c2250 | -11.61722 | -55.18255 | 2026-06-03 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b00b6aaf-50ca-35c8-a9a8-1ec83136f912 | -11.13414 | -45.14314 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ded9ef8-d78c-3bcc-a868-c89ec6b6a22f | -12.46604 | -54.46488 | 2026-06-03 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 234adbeb-d796-32d1-a7fd-f7472e8cc639 | -11.88959 | -57.83745 | 2026-06-03 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77179e06-9d01-38d2-a70b-9faceb11a4d8 | -6.98655 | -42.879 | 2026-06-03 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f0de796c-4c85-3b06-b4b2-d70fcf001cda | -12.73137 | -46.97163 | 2026-06-03 05:01:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e186c88-f28f-383c-b869-4be81e0cf439 | -11.32412 | -51.38824 | 2026-06-03 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b1cbfb7-401a-3886-a8d5-529723789eca | -10.54292 | -46.62697 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 638be2b2-ab01-3b3d-abd5-2ed4a0c60087 | -12.73761 | -54.20388 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a16b1b-6973-3040-8dbf-58ec0360222e | -8.86927 | -50.19462 | 2026-06-03 05:01:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb294109-fbe5-3c32-85c3-18dd6512288b | -7.50343 | -55.00505 | 2026-06-03 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c48c67e8-b27c-3644-82fb-70a2cd3dc7d8 | -11.57241 | -56.34419 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26fc721e-2313-3dc8-8ac1-bee5097c0db8 | -9.18962 | -58.05577 | 2026-06-03 05:01:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cd9e812-9818-3d8d-bf96-db266cc3ce58 | -10.53761 | -46.63117 | 2026-06-03 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ee22d4d-a3be-31f1-8763-c7395c8e05ec | -12.72982 | -54.20987 | 2026-06-03 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1a7ade6-3823-3dbe-9438-91c57a020749 | -9.08637 | -48.64768 | 2026-06-03 05:01:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462c21ea-df48-3642-8ebc-45c58cc6206d | -11.57721 | -56.33701 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 355e936f-983a-39fd-8373-90997056fade | -10.86023 | -53.73687 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b0af2b4-a06a-3ff0-8850-5387a2d3c669 | -10.89899 | -54.13281 | 2026-06-03 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 60c6777f-86ec-3abe-8bbb-b93d3f251772 | -9.22064 | -48.57278 | 2026-06-03 05:01:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcb707ee-021b-3fe5-b7cf-8231c33393a2 | -7.2707 | -46.81216 | 2026-06-03 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 343364e7-62c5-3c61-b99b-79a15cddf5d2 | -10.81128 | -56.59591 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78e1b13b-bd09-3fb9-84de-a253ad02b981 | -11.13892 | -45.14712 | 2026-06-03 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fda5c3f5-e940-3b31-b37b-363e2066f381 | -11.57307 | -56.34029 | 2026-06-03 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README8.md)
