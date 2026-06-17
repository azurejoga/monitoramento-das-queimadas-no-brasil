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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bb99a26-7a66-3400-8acd-f055e86c2ab5 | -9.3423 | -45.4765 | 2026-06-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 0b80429e-dfa2-335b-b327-bac5b9a623da | -12.8548 | -44.3625 | 2026-06-17 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e4e894f3-994b-3692-b796-24ce9f9c871a | -12.8548 | -44.3625 | 2026-06-17 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| cb534605-47ec-3863-8fd8-4d8d82a16f5e | -12.8354 | -44.3657 | 2026-06-17 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 11305cd6-8f6b-3b96-afc7-b27ec6c37099 | -9.3423 | -45.4765 | 2026-06-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.3 |
| c731eff3-5c93-31a1-a949-e3da2235d973 | -9.342 | -45.4993 | 2026-06-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 31b6915e-713f-3e03-b206-3439267d4e7b | -9.3234 | -45.4787 | 2026-06-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 13f7fc92-1492-396a-960f-08ac70db2531 | -12.0756 | -54.6131 | 2026-06-17 03:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e33eb6cf-9873-3718-a48b-7742649b43c4 | -9.3423 | -45.4765 | 2026-06-17 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 4eafcad6-d268-3531-af47-a74889417ef2 | -12.8354 | -44.3657 | 2026-06-17 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d8a5db01-ce05-31f8-a6ca-ffc4daca0974 | -12.0756 | -54.6131 | 2026-06-17 03:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0b4814ed-9099-3776-bf36-1cff9a248200 | -9.3234 | -45.4787 | 2026-06-17 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8cfb5200-8fcc-33d8-9b0e-e8a5416f6bcf | -12.8548 | -44.3625 | 2026-06-17 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 10a39d73-58b8-3917-8849-f20929d01b7f | -5.52172 | -37.62198 | 2026-06-17 03:57:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 414ba887-7f9b-3fc7-b6e3-d1dc0d485b2a | -7.07033 | -43.40108 | 2026-06-17 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 087f3444-4edf-3c3e-b3d4-de89b5ab06b4 | -3.77972 | -41.59388 | 2026-06-17 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18c0864e-4e27-31c2-9e20-bbf16634849f | -5.79233 | -45.08398 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d757baad-211d-3453-af49-570ebc424ec8 | -4.3501 | -47.76234 | 2026-06-17 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5dc37ca-6bdd-318b-8693-cb8262b2770b | -7.83877 | -48.39415 | 2026-06-17 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa23c8d3-66f9-3672-ba9d-9f30e8e8f58f | -8.49554 | -39.39222 | 2026-06-17 03:57:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d2ce3df-ff5c-3ae7-a658-74c129a34532 | -6.28964 | -43.63297 | 2026-06-17 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c77b78fb-b380-30d8-82bf-a5cc2fe65913 | -5.49431 | -37.24494 | 2026-06-17 03:57:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1039f04c-4aac-3e26-8b07-974437fe9d3c | -9.07988 | -40.38381 | 2026-06-17 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 536ce774-e464-35fa-8839-6dcb9c794404 | -5.79132 | -45.08986 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9cad81b-9845-31ad-9640-66521bf50a24 | -5.79633 | -45.09083 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 74e84bbc-9f54-3882-9e51-006a39124c93 | -7.76108 | -47.56487 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1305a8c7-6acf-3a61-8c0a-d39a9fc40f64 | -5.79735 | -45.08493 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42ffa724-47f8-3007-8715-a3346967c981 | -6.14338 | -48.51387 | 2026-06-17 03:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a8e0653-1f64-3a37-8cf9-19adad1380b6 | -3.77561 | -41.59324 | 2026-06-17 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1c0a0c06-57f1-3fd8-b782-564f3eeab3e7 | -5.98078 | -47.07278 | 2026-06-17 03:57:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de2e9fe0-3b30-371d-9578-2191e4640eeb | -7.35135 | -49.86571 | 2026-06-17 03:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2374c9e-497e-3894-a784-fce2a12f9743 | -7.71375 | -44.1637 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 205cbe3b-7d39-32dc-9a93-ba6257b062ca | -7.71947 | -44.15718 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cc7b8c2-1b46-3b14-96b3-4e55e1741ebf | -7.83782 | -48.39144 | 2026-06-17 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ab12fa2-8b51-32c1-8931-5eb271a0ab13 | -5.79335 | -45.07809 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c59c0478-f211-3cbe-8bdb-c6eef9ab6c60 | -7.83698 | -48.39606 | 2026-06-17 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b411663a-daf5-3843-8979-21e5039fbbc5 | -5.34483 | -45.18526 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bad616f0-a343-389e-bb84-a75dac2f3b13 | -3.77912 | -41.59752 | 2026-06-17 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8873c06-bc3c-358a-b709-5fe3b53e0c00 | -9.14873 | -37.81125 | 2026-06-17 03:57:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 40b033ac-8f01-3f8c-a1fe-f11908ba69b2 | -7.76166 | -47.56623 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d44743c-6a01-3ad7-a1a2-b1397fbf52ee | -7.83188 | -48.39759 | 2026-06-17 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7625282d-c4db-358f-acc4-ac567fd977fc | -7.71864 | -44.16184 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7268da89-1c27-36f7-8022-db3455b4cbf8 | -7.76611 | -47.56985 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c089ce22-0ab0-3a04-8ce4-1381dea764f6 | -7.71295 | -44.16839 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e48f2e23-5a36-35a2-979a-8d1019adc262 | -8.19388 | -46.76274 | 2026-06-17 03:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1cea9c1-0088-3f2c-938a-71766a5926ea | -7.83094 | -48.39497 | 2026-06-17 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37bc3334-1964-379d-8619-a149694c229f | -7.72401 | -44.1581 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e15b44a3-fa1d-35db-82ef-144693e3ee36 | -7.71833 | -44.16449 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2fe56047-f4a5-3453-9a91-c89e59c9a2b2 | -7.63121 | -50.02433 | 2026-06-17 03:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1adb8519-2ce7-34dc-9fd7-bc22d0168bb5 | -7.63784 | -50.02579 | 2026-06-17 03:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e21d2ab8-63dd-3242-bd0e-de3256dd8674 | -5.79937 | -45.07323 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cfb08b8-62bb-3e13-86e5-d279f761eda8 | -7.71913 | -44.15982 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8017fe89-7210-3f2b-9619-1c5e82a5bd57 | -4.35544 | -47.76793 | 2026-06-17 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 751fa3a6-f53b-384b-9d6c-534e22e00612 | -7.71323 | -44.16573 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fcb2d1b5-59cb-3cee-8734-3c9351912cce | -6.14257 | -48.51833 | 2026-06-17 03:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f4ff385-9473-39b6-8612-328c1f435a08 | -3.77501 | -41.59687 | 2026-06-17 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ee047563-e51e-3bc8-9521-f0440afa61df | -7.7178 | -44.1665 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 96ecffc9-c139-3206-917b-bfdd815fe780 | -9.28368 | -40.24277 | 2026-06-17 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63123311-5931-3f38-a9d8-281b43634b3b | -7.358 | -49.86694 | 2026-06-17 03:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2f57d57-b91a-3b9e-adf7-8900e99b417a | -9.05351 | -37.30457 | 2026-06-17 03:57:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e04482b0-d55e-344f-94d0-7caa5da2fbe6 | -7.7232 | -44.16265 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc821543-c245-3e0f-a19b-4bf5b6ee29f6 | -7.06522 | -43.40454 | 2026-06-17 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63c61050-00e1-3ae0-a111-7befbf29d5ff | -7.06594 | -43.40031 | 2026-06-17 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2ca4494-aff2-3725-8828-0aae76cb3617 | -6.14952 | -48.51557 | 2026-06-17 03:57:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9e8afe1-ce8e-3856-a7ef-efddbf11d374 | -5.61032 | -37.53168 | 2026-06-17 03:57:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9938b2d3-4f77-35dd-9e39-514389708684 | -6.62866 | -44.5782 | 2026-06-17 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79095785-cef3-3005-b65b-7323d8761690 | -4.35625 | -47.7633 | 2026-06-17 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5edc15e4-5b4b-33bd-9760-dbb9c72c4f4d | -8.1891 | -46.75832 | 2026-06-17 03:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c5208a3-9087-30c1-8f64-debee456086a | -7.72369 | -44.16068 | 2026-06-17 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e44f4de5-b510-38bb-8bea-d0d9984820bf | -7.83274 | -48.39301 | 2026-06-17 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 512caca5-8ab9-35d1-9001-f14c1246f87d | -7.76739 | -47.56727 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d741ea2-3ac2-3b4a-a32f-5e0df8a6b763 | -6.63823 | -44.57996 | 2026-06-17 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2915c87-6ff1-3f7c-b979-2e8edc699fd5 | -5.83675 | -43.48642 | 2026-06-17 03:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac24fe0e-50b6-3f01-8955-0c1840336616 | -6.63344 | -44.57908 | 2026-06-17 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6418731-65e8-382e-8242-bb18748d834c | -5.79436 | -45.07227 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9ce4d93c-0044-3066-b6be-f78a1f08a5f5 | -5.79836 | -45.07905 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| daa3a757-f669-3cd1-9e7b-b6cfd2ed492e | -5.34992 | -45.18619 | 2026-06-17 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6141ef00-2097-3f38-8f82-874235f7f3a7 | -12.8354 | -44.3657 | 2026-06-17 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 263da04b-2893-3056-9731-9cba87affa8a | -9.3423 | -45.4765 | 2026-06-17 04:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 5aec8af4-3046-3647-a651-48b318b5499c | -12.8548 | -44.3625 | 2026-06-17 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| dd8b5981-0873-3ae6-9b43-c68d7e901af0 | -9.3234 | -45.4787 | 2026-06-17 04:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 63a7b686-0a74-3ec8-9317-dc0790afd46b | -9.30355 | -45.47083 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eeeb7446-ce79-3829-b860-fe5c41408fc0 | -9.33263 | -45.47653 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 052ae8fa-b96b-3ae4-b95b-6f96998aee50 | -10.98118 | -46.48613 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28ee7c78-c01e-3a35-a89d-fa1b802b740a | -11.89031 | -43.8303 | 2026-06-17 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b4b40f9-1d93-37ef-b433-679f2d9ecfa4 | -9.30839 | -45.4718 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e274e98-e85c-31ad-ab4c-a13a2db3dd68 | -8.56862 | -45.99463 | 2026-06-17 04:00:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53c8feda-1829-3b60-82b3-c5c339bdb0a3 | -9.25858 | -48.54513 | 2026-06-17 04:00:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f00bd04c-740a-3279-8efc-ea08b2f837c5 | -10.97178 | -46.45333 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9d1598c-bb41-38ab-8f62-026330fb2dc5 | -8.99059 | -46.98769 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 370fc196-a684-3e34-a126-9826658fd3c0 | -12.17077 | -52.78685 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0a266196-0727-3801-9b8a-d8063f47a47b | -8.97048 | -47.0056 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8c0c471-0b88-389b-b9a5-18914c239351 | -12.20203 | -52.78442 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bcd24af-e116-3088-8dad-daba7c458067 | -10.97337 | -46.45225 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2436f6f3-8a2c-3b69-9f52-17c279177cd6 | -12.84384 | -44.3771 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 2473f11b-8202-3108-8d37-04e101dca1d8 | -8.27827 | -48.22235 | 2026-06-17 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5ab4b0d-68d8-3836-8183-6209018c9106 | -11.02928 | -44.3174 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87a85ff0-a444-3216-abe4-d660b9ff4569 | -9.31324 | -45.47276 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38089c5c-b3c4-3f5a-8b39-4d1b15bcc9a0 | -8.98649 | -46.97968 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dde0f509-2dba-3b47-9e70-71c56626a381 | -8.96688 | -46.96501 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
