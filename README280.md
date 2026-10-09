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

## Dados Diários - Página 280

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82b628ad-647d-32ca-a346-a001cd9a5307 | -9.9333 | -43.56662 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| df395957-464b-306c-afab-8ebf6ae33db1 | -10.50105 | -47.34717 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 381beb26-06b6-3138-871e-b2426be3a646 | -9.9263 | -44.813 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8c307a40-6721-3ba2-8b6d-89c74a6a4523 | -10.88769 | -44.7982 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| de69074f-314d-3993-ae05-9f1c7746e64b | -11.04464 | -44.03292 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 277.1 |
| 37598409-fd5c-37d3-a9e6-1b3ad950caa5 | -9.90721 | -45.70618 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a30d60dc-bb10-309c-a09c-802f19088caf | -11.05203 | -44.04488 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 34072f12-962f-37a1-8a58-c5f61b37362c | -10.47496 | -47.24469 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b656ba6c-b4d7-327f-b88b-34110ee3f2a6 | -5.70726 | -41.67324 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| bea0720b-a81a-3122-a1c9-1ca1ec567139 | -6.89617 | -41.47936 | 2026-10-09 16:01:00 | NPP-375 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4c5a3fe8-037d-3fb0-9c63-d416256efa2a | -6.86134 | -41.74535 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| b196f776-03a0-3893-ba43-6cce9fef9942 | -6.9625 | -43.85793 | 2026-10-09 16:01:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af315e11-4db3-3c09-9fbe-71eaf11fb95d | -10.92739 | -45.3791 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 07398b41-8179-3e81-a8fc-96ea2af11cc8 | -10.88902 | -44.80355 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 25454ee6-730f-3b79-9432-0348630665d3 | -11.20159 | -45.30332 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1304c56a-71fb-3428-b85a-5aed3251c747 | -7.48302 | -40.53695 | 2026-10-09 16:01:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b27eae17-f3e8-33bd-ba67-de90553bc15c | -7.47294 | -42.81519 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 141a6f81-ccb3-37b5-95f9-f75a6e9582e4 | -7.82884 | -44.56676 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dbebc122-dc3b-3130-b61f-46a17563261a | -8.94167 | -45.13889 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bb93412f-6f7c-3b3e-afe1-187aa96bcfe0 | -10.96824 | -45.38382 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e2e9f680-2158-3439-ba5c-e0bcc089fd62 | -11.05609 | -44.07848 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b5d10a4e-639f-369c-8d11-5fc1833cee18 | -9.90465 | -44.78764 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b831eb97-4acf-393c-bbe7-57ff49f5f142 | -6.00519 | -40.96368 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 4ac72ef0-23ff-3ea6-927e-ea6d3a966ac3 | -10.89309 | -45.52769 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3fbd00a0-9de9-3198-8e32-a3c464b60c91 | -11.05813 | -44.09538 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 214ad643-2445-352d-b058-dd13c89af9dd | -11.04384 | -44.07567 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09f904ab-26b2-36b6-bb33-37168c29ab1e | -9.02728 | -44.36341 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ca019a04-808f-3b29-91cb-f502ecc8a232 | -5.96252 | -40.91755 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d2750be1-9630-3d2c-9a61-78905aea809a | -5.36697 | -42.88244 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 427f25ff-8056-3870-8f66-9e90b900641b | -9.91492 | -44.86961 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d8472371-2e8b-3e9d-b320-2aa4fa361176 | -9.88302 | -47.487 | 2026-10-09 16:01:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| bfd11983-50c1-3259-82c5-06e471fc8ef7 | -8.31797 | -45.45895 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6918525b-15cb-3c7f-8afd-70de316c5adb | -9.54132 | -46.84793 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| c1329b3b-2bb5-3ef6-bde9-e9f452d960f2 | -11.21466 | -45.25026 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3dd4dd5a-1b4a-3957-821b-a74cd01da4eb | -10.8821 | -45.54519 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fbaa3e14-966f-3495-b801-b75dbede8ea6 | -7.72189 | -43.96311 | 2026-10-09 16:01:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 762591ac-8b99-3cbd-b8f7-9bd612932c06 | -9.02109 | -44.36189 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7965a2c2-a25d-3ee5-bebf-70da06f306f5 | -10.52933 | -47.31466 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e3e128ea-34e3-335c-bda6-3a1216c2191d | -6.70621 | -44.11323 | 2026-10-09 16:01:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 36878ca3-038f-3929-9630-1be213f04593 | -7.37233 | -44.02776 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de55c281-dd43-30bc-9eb5-3589b3e0ebd5 | -10.1602 | -45.35099 | 2026-10-09 16:01:00 | NPP-375 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ede8d99f-eba8-34ca-86d3-ad5120b563de | -6.97043 | -43.79262 | 2026-10-09 16:01:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 21c3777d-affb-3a8f-8861-ee077e6ac080 | -11.26363 | -45.17764 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e5ca2ddc-91d0-3883-b6cd-c6927aa02e43 | -6.38731 | -42.5349 | 2026-10-09 16:01:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 90f5dda1-d678-3676-86f4-59d85b56de41 | -7.49147 | -42.79771 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b7446808-4dad-3928-ab03-9b632a3b58d5 | -7.08306 | -43.08752 | 2026-10-09 16:01:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b9e37e22-23bb-36fa-bf5e-77d3b6eb5b12 | -11.08372 | -44.10951 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e3a6a9a-0879-3fbc-823f-f3d17f5fc306 | -7.32052 | -43.97892 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cec55796-d14e-3e07-aa5d-82280b194c7c | -11.07453 | -44.13217 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 6bae643d-d062-36ec-9dd9-b41b3762ac2f | -9.85995 | -44.87645 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f1f781a9-0584-33fe-94c7-9df6c1b6f01d | -6.99942 | -44.13563 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4af13285-6cfd-30a8-a027-f6cb56a613d3 | -6.32251 | -37.46282 | 2026-10-09 16:01:00 | NPP-375 | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| edf53f33-a203-3468-9000-765f3f9cc461 | -9.91072 | -44.78707 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e4c5a406-72d9-33f2-8694-ba928275002e | -8.96427 | -45.91037 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9abcc80f-878b-3573-aeca-4e32c437a0ab | -7.29729 | -44.01184 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bd8cf6a1-92ac-3f2a-bd1e-c7f9b259e1b3 | -9.5421 | -46.85434 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 130ae858-496a-3d3d-8ae4-9d4b75596983 | -6.86562 | -41.74747 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| b1a350c4-0ceb-3daa-b149-27815e0de3da | -11.04566 | -44.04134 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 1127a19a-6380-3a33-b6d3-c9e58d595248 | -5.99761 | -40.94264 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3e07040b-76de-36ef-8bbf-9eab5373c744 | -7.11195 | -34.96068 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3598aafd-595c-30a1-a5d0-d15cfe1ab92c | -7.39888 | -44.74593 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f4d4619c-2480-3106-878b-47b769d58bfd | -11.07629 | -44.09751 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 014bf64d-f86f-3a6c-96a6-616a96983bd0 | -11.04616 | -44.04554 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 00fc1c88-25d0-36d5-94a2-4b07b89136b0 | -10.40308 | -42.57256 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5240e006-f845-3977-ae23-41e59bebaf43 | -9.41074 | -46.44755 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d8742561-5c95-348a-ad7d-89fbb7f7d5a1 | -9.93829 | -44.79871 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c6269c20-eac9-3dd9-b706-79ed6a28ccaa | -6.0845 | -43.99425 | 2026-10-09 16:01:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 28918b9e-69f1-3223-a383-dcd342c33d39 | -8.90484 | -45.23879 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 76e280cd-5506-31a2-83b7-aaf58a871d3c | -5.71245 | -41.64334 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 8dd71423-c880-33c0-a689-5dbc611cb50b | -11.2747 | -45.18882 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8772f853-8152-3a26-ab51-5b76fc3a3ce0 | -7.47824 | -42.85466 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| f4c47ffa-b5d8-3c63-8af1-c3c226c7e850 | -7.59717 | -47.03891 | 2026-10-09 16:01:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3f9f82ec-b420-31f1-a922-ddd415ed578b | -6.35681 | -44.05902 | 2026-10-09 16:01:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04add163-d0c2-3c5e-85df-5f149ff14726 | -9.91619 | -44.78168 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 06976279-cc97-3b77-9d6a-6ac5b2b21707 | -9.4041 | -46.4486 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 13c16deb-877e-3144-93be-ba9702b6f992 | -7.39274 | -44.74732 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8c7d603-e00c-3aa4-ab51-7a6eb5e4944a | -9.98537 | -45.97602 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f5767ed-1b40-34ca-bb9b-80c8835ddea8 | -10.05449 | -45.89203 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9144c7a4-1bfe-3920-a0cf-3c2b456093bf | -9.17358 | -43.392 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| b5dac286-0da7-3d53-ba34-7cf73bced279 | -9.72361 | -45.54411 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9aaf71f-2dce-3028-9e26-7464dbdb0198 | -9.17402 | -43.39543 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 41b9791e-3181-3276-a746-f4017e61e550 | -5.84202 | -42.68048 | 2026-10-09 16:01:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 89845932-6fc1-38f1-a892-7e484e24393d | -8.66617 | -44.88709 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 3d647c00-f31a-31c5-b29e-cef8965af024 | -10.50112 | -47.22308 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| a472bff6-668c-36f7-848f-42b13218bf7d | -10.63927 | -40.03655 | 2026-10-09 16:01:00 | NPP-375 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| f7d62940-5fc0-3d6d-88a8-c4265ae0b6a5 | -5.7548 | -42.08615 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 59e34b52-bf63-35fc-a760-d0b3bd9bf56f | -10.17181 | -46.7321 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5771ae67-8b54-36b0-886a-ad0413625a2d | -7.82483 | -45.48902 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7c2a57a9-a7ca-37b5-8e2a-71eb42cf6890 | -6.57171 | -43.05309 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c92514cd-d579-3711-942d-5f8f7334a85d | -7.22675 | -44.16111 | 2026-10-09 16:01:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 21efc1f8-637e-35c7-9db4-7e1119b6cc8d | -10.51098 | -47.21304 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2167d91b-6c7c-36b5-a895-1e2b3300cd93 | -11.20888 | -45.25574 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d6594c80-ada4-39b3-8a3c-a67ac93c1d23 | -5.81761 | -43.27191 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1b3b275-1106-3f4d-a8d3-22bf9f07a139 | -7.32149 | -43.98613 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1a43ba9c-541e-30ac-adbb-486dc1bb47aa | -8.79616 | -47.26569 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ee4a50b8-dad0-3992-8a80-9c26c00af1a5 | -10.33014 | -39.49186 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f9a70dbc-4d6d-38cf-879f-eee6f4d2b8c6 | -10.97303 | -45.20447 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bfcd867b-e103-3cb9-8f47-cb01e3b704b4 | -6.88938 | -44.90893 | 2026-10-09 16:01:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d3511565-8598-392a-8f70-39724e78f398 | -10.46271 | -47.2 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 18a96342-875b-3e2c-a26b-78555af8eb43 | -11.06989 | -44.09397 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |


[Clique aqui para ver as próximas entradas](README281.md)
