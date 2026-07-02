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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81d31172-9da3-31e3-a8f1-cd3247767da2 | -11.80629 | -57.00714 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a4cb2d7a-e91f-3acf-b4c1-ad164b32f22d | -10.38535 | -49.93134 | 2026-07-02 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 076d0d71-4c14-37ff-ba48-daa3eaf11711 | -12.86388 | -44.34557 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 717f82d7-a0b6-3d34-bc73-9132baf880a9 | -10.3806 | -46.66983 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cafc21b-5440-39c2-8ad1-850c76835bb9 | -10.37144 | -46.70758 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| b8f4e25e-693d-3a8e-87b4-db81247eead5 | -8.71644 | -48.33504 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 44d51c13-c002-393d-adbb-8a0fc874ddbc | -10.69483 | -49.61099 | 2026-07-02 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0513969-b8c1-3c53-bb5a-7c1fe27c4a17 | -11.41827 | -56.05362 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6540567f-c39b-39c8-89d0-39275faa9260 | -9.20408 | -45.32277 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ae30393-bcb6-3deb-b846-eab7687ba40c | -8.72251 | -48.33957 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29186c5d-7a11-38ed-97b2-31cec67633ea | -7.90898 | -48.24113 | 2026-07-02 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496c3e93-bad0-3dc4-888f-f09652216d75 | -12.75008 | -44.47403 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7ff61aa5-9770-3b8a-b7f1-32bc349e2c0b | -12.51989 | -48.28645 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55bd973f-7e5a-3af4-ba57-ffdd14f262bf | -10.37487 | -46.68456 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 74306adf-338f-3754-bdd0-0f2fe6a91476 | -12.74958 | -44.47752 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 823bafdc-fd9c-3fe9-971e-5e8d5e46dcc9 | -9.02653 | -59.53685 | 2026-07-02 04:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e9b48de-1aec-3d82-a131-b6e38b4161ba | -9.17527 | -58.06337 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ffd7917-03ac-3250-8fac-f985eb380f78 | -7.55619 | -43.22029 | 2026-07-02 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb849ade-5fca-3b78-a197-3e1f68f4e1c9 | -12.78654 | -44.48983 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e3598fc2-3df6-3746-97c9-7491d521e4f8 | -7.09666 | -46.50899 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e20c3a3a-ac82-3fce-bb75-f92851c9c1ac | -9.2588 | -46.42996 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0e7bc7c-a533-3aa5-bf0e-9958cea02b29 | -9.74468 | -49.02837 | 2026-07-02 04:38:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8503641e-aa24-371b-a6fc-6c20d634e767 | -9.1892 | -58.04826 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ab3df56-a8d6-3030-9fa8-aca7dd791db6 | -8.87451 | -50.18587 | 2026-07-02 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8b7a408-90b2-3d0a-b51e-9584b4b9d0d3 | -12.75114 | -44.48116 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| be1d1b66-7742-3983-b9b2-f7d216498bfd | -9.19999 | -58.05022 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3130fc75-61e4-3415-b3b0-7851a8de82c6 | -11.35806 | -55.42399 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1e47aac-ae1d-3827-95bc-0cb353f7e909 | -11.53845 | -47.4591 | 2026-07-02 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89d63e44-f306-3e19-aa7c-78f4cae562b3 | -10.66741 | -54.52129 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddfaebea-e5ed-3db4-889b-8097f31b8cb5 | -9.81718 | -46.44208 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 264a4fdb-7a86-30ca-81c3-d96f774294f0 | -10.37283 | -46.68069 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 752a3789-3025-3b81-8765-93a5c514a642 | -11.41562 | -56.06781 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 99a29df2-1cb1-38b9-8e93-6611f2614aa8 | -11.04557 | -56.93189 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b31ce9c4-2278-3374-9b6e-6fad53fc065f | -13.12791 | -48.61406 | 2026-07-02 04:38:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cc5561e-9f65-358e-a941-b0c528e3d7d4 | -12.45014 | -46.91371 | 2026-07-02 04:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a547952-6104-3b8b-a6b8-4e9b194f89e4 | -12.85132 | -44.40553 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57b9969d-9183-309b-bd44-ebe709414ae0 | -11.4162 | -56.06012 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 55f72058-e1bb-38f7-aeae-cfd5131e6650 | -10.1225 | -52.08709 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2410b8ed-a6c9-3a89-ac3d-2d124123ca8f | -10.80369 | -48.56208 | 2026-07-02 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 957afe48-3952-37b4-b9cb-ece06dfdd4ab | -8.72624 | -47.84035 | 2026-07-02 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d6070bc-191b-31f0-85f6-c242ea57e6be | -12.75863 | -44.48581 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5d5f9064-778c-3f3e-ac4a-984e36f85e40 | -11.35728 | -55.4283 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3dfff11-f4c9-355b-9263-602759b9e356 | -10.78245 | -53.54148 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf710c2-38a7-36d3-b429-08102c545c8e | -8.71865 | -48.34252 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3bb6176-9a1a-34b9-b630-3314c0d7bed8 | -10.3693 | -46.70366 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 6032ae90-42e9-36e3-8f2b-9096b471cba2 | -9.19383 | -45.31689 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b312a1d-3aec-33de-bbeb-b8d8ec33f19a | -12.86035 | -44.34142 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4c790a78-7410-3508-9fc1-85455b340cb9 | -8.65632 | -49.71193 | 2026-07-02 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5cca96e-38c6-36b5-b83d-b9339e843f8a | -13.46529 | -47.86782 | 2026-07-02 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2b1224d-e3df-3035-8283-d2dd6f73da17 | -8.49367 | -47.19588 | 2026-07-02 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a9f39f7-7560-36ec-bf6b-39f165df123d | -10.13124 | -52.10167 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2ecb53-071e-3270-a8c4-cd1c7c0f8c92 | -10.02793 | -46.66908 | 2026-07-02 04:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7afa84f7-36c4-3b3c-a71b-a2f535704b9c | -12.7456 | -44.47694 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e5879e3-d0ce-3a96-ad7a-9ce72784b4bd | -9.53429 | -47.75444 | 2026-07-02 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab01a04c-fa06-3900-901c-f4d4187445eb | -11.86909 | -45.60576 | 2026-07-02 04:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e6a36be-93a7-3537-a018-203c953582d8 | -10.36871 | -46.70749 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 990f6355-afd1-3dd8-bb19-55e15ac4804d | -10.37216 | -46.70804 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| e2db4841-f1f2-3b2f-94a3-96cb90b3b5d4 | -12.84978 | -44.35817 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a66e1396-2eb8-3393-bc7e-596d8ce44192 | -12.61904 | -44.66232 | 2026-07-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e4cea5b-ab86-37a4-a089-8acd4f14d3d9 | -12.76968 | -44.52383 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa7d30b3-39ab-310b-ab43-ec8b3e50c646 | -11.35215 | -55.43179 | 2026-07-02 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba88a38-bded-351e-af38-9e8f8432c803 | -7.51169 | -45.86007 | 2026-07-02 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efdeabac-07cb-3356-a5be-706e14e763d3 | -8.41686 | -47.40991 | 2026-07-02 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 193d0048-8f86-3b97-9ccf-d1dd7d5931b0 | -11.84897 | -48.23916 | 2026-07-02 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5cdf6dfe-a58f-3ee1-8e41-482bc46f6f4b | -10.36527 | -46.70695 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 852c30c9-4eae-3405-88b3-53bd7cfe6f7d | -9.75587 | -47.88004 | 2026-07-02 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abf167be-8c25-301a-8bc7-f18f6c31458f | -12.61855 | -44.66365 | 2026-07-02 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 873a15f2-266b-337d-9790-175a12fab1e0 | -12.85833 | -44.35575 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| f024f0aa-a65f-353f-af61-5eab24fcf73a | -11.42105 | -56.06385 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ca2bbb83-62ef-3d8b-ba6c-8639f03f3453 | -10.37107 | -46.69217 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f83ced30-f8d4-32f4-9b3a-808dce5110b9 | -12.518 | -48.28238 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf9ea752-3655-3b8c-a0c5-d7e51cfb4c1e | -10.77856 | -53.54081 | 2026-07-02 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d742401-a5b8-3d13-b45e-d21282f8981f | -9.24615 | -46.42019 | 2026-07-02 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 985b9e4c-f21d-3c95-a113-af61d23e1d9d | -9.18027 | -49.66493 | 2026-07-02 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 241df352-c9af-3b46-bfc3-4b4b2e06be2a | -12.52658 | -48.28752 | 2026-07-02 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 92613e14-c4df-39e4-a9d2-5b7d9dc3930e | -11.79293 | -56.99899 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| bdc85c43-2724-3caa-974e-743ed360e9ec | -9.16316 | -47.2363 | 2026-07-02 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79ff23d1-2095-373a-a03a-02225c2b5f09 | -11.80742 | -57.00593 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5a1b82fe-1861-3364-9a99-3e4f3debadda | -11.40991 | -49.0047 | 2026-07-02 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97176281-71d8-31dc-8861-23f2ae10c360 | -11.80731 | -57.00175 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 952c3ad5-d966-3a6c-8299-274f4954d740 | -12.75209 | -44.47415 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2e48f030-4446-322d-9135-86848dc498ba | -9.21859 | -45.32492 | 2026-07-02 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98e09fe7-141c-3f48-9e3d-b16b2964a203 | -7.09384 | -46.50483 | 2026-07-02 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ecb0b80-d237-302c-a731-edecdf5629e4 | -11.04754 | -56.93001 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44c80e08-9514-33a7-b22c-122c369228ae | -10.1247 | -52.09618 | 2026-07-02 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60e0919f-7b6f-3917-87c9-5e8d24cfda4e | -8.71975 | -48.33558 | 2026-07-02 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 57dd3ff1-3d69-3a3e-b823-475fac88b836 | -9.18003 | -58.06782 | 2026-07-02 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 452a8dba-a55f-393c-ad40-34410e0795d6 | -12.74821 | -44.48711 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3498532d-aea3-3847-bd22-e41d008c2c80 | -10.37373 | -46.69223 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bae6dd82-d266-30f1-8c29-88c5ad1873c5 | -9.28022 | -50.2177 | 2026-07-02 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 024e5fee-5048-30c0-97e6-32d6cbe1e072 | -11.40605 | -49.00767 | 2026-07-02 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a287b00d-178d-31c9-a24c-3604b047d2c3 | -12.7556 | -44.47823 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b462d812-dc71-38a5-83e6-8e93eb15638b | -11.41705 | -56.05538 | 2026-07-02 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c8dd3942-9ecc-3474-b7a3-ebfd5ba482cc | -12.74099 | -44.48074 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a18374e1-ae38-3655-93ba-a6bddf7089be | -10.37603 | -46.70045 | 2026-07-02 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 52436c85-7958-3bf2-aa08-338d1f5c5fe6 | -12.84776 | -44.34329 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bb8a7014-1330-397d-acc9-083a3ddecf3a | -12.75618 | -44.48828 | 2026-07-02 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b1121a45-b10a-3cc9-a777-73db3721f0e2 | -7.54217 | -49.49955 | 2026-07-02 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93f8a1ee-d959-3a28-87df-70f39cf08f94 | -11.85175 | -48.24326 | 2026-07-02 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3d8183e8-edb0-3e52-b6f7-b483014f9d82 | -11.79302 | -57.00315 | 2026-07-02 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |


[Clique aqui para ver as próximas entradas](README18.md)
