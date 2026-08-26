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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26b80426-8d90-3f33-86ed-619dd1bde6b5 | -8.60973 | -50.01851 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be8b919d-2fc5-3762-b038-1ecff4691a00 | -6.76059 | -59.44524 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3896f12-bd37-31b5-ae0b-f772c22d9a1e | -6.97715 | -59.08107 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dc326c4-c57a-3d99-b560-a87dcfca31a3 | -7.02765 | -59.23495 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e6e0c78-0144-3992-bd1d-d2006095810f | -6.12693 | -57.8174 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55660fe1-9532-3d50-89d7-3182ce165fa4 | -6.63179 | -58.48813 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 720df179-922e-3884-bcc1-63ca334fcbb0 | -7.38018 | -55.18066 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7059df2e-bdfe-39b0-bebb-80c4c1dfb7b4 | -8.77292 | -49.96803 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0cc3c54-8f87-3c84-a595-724f1535c58c | -6.33541 | -54.73631 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e300fab7-c3ba-34b8-b9de-5bf7d946b8a6 | -6.80436 | -59.59492 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53478065-0b8f-3cee-9342-7df93d6e11b5 | -6.78761 | -59.74236 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 952ae0d2-935e-37ca-9bce-c4aef1e73730 | -7.07251 | -59.22849 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ece5987c-d453-3005-b9b0-ad617da6ecb7 | -7.02875 | -59.228 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db5e4026-4376-3962-b9f6-f8a8b63b3be8 | -6.63014 | -58.4986 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ec991b9-d732-3530-8d15-b3a14ce573eb | -7.51886 | -61.37597 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 92e50caf-f2e7-3976-9e36-c04d7435b6de | -6.53918 | -55.0876 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85e7a3d8-68f4-37e7-81ed-538b4dd1d2b6 | -6.6218 | -58.48654 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d97c7b00-6f57-3feb-8695-85be5945cff1 | -6.93865 | -60.08711 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f1c7d9f-b764-3b35-9004-9f952d3e7578 | -8.81453 | -49.60719 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45a61ac6-9087-3520-bd4b-468f4a898606 | -5.77368 | -57.55041 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e94dae4-0b03-3fac-bbd2-eb8098626898 | -8.59115 | -54.83293 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 148ffd20-46a9-3ff8-b79c-b8f3cc40b38a | -6.63292 | -58.51681 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03d80e74-d9cf-3f63-bb92-369f53a5ab26 | -6.25044 | -53.36238 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5bd91c7-e901-3f52-a7a0-370b25a1532a | -7.06974 | -59.22449 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 21ded97e-f0e4-31e9-b000-5243547bb7ff | -6.147 | -57.7107 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8644dca6-87dd-3892-af9f-65ba03120b41 | -7.47277 | -61.37614 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 125f9484-bc89-3b8f-ad74-93092cec78c6 | -6.99116 | -59.27184 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec1fde3d-fb0d-31ab-b51f-d0b8460465f9 | -8.56743 | -54.81149 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b53c3c80-e53e-3676-8614-158c9ca3ccc1 | -6.81989 | -59.58311 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87ff7715-0efd-3fb7-8af7-1959197fe3c5 | -6.30892 | -53.57484 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffe9c804-b1b9-3f41-80ea-b25343898f51 | -6.78372 | -59.74532 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73c5b374-3742-31f9-9704-293917e7bc84 | -6.63565 | -58.49935 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68cba7a8-a147-31dd-8ab0-fac85d1c51b7 | -8.68555 | -54.71461 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ac385df-37d0-3982-8b14-4e576fb5575e | -7.2598 | -49.85437 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38727a6a-6c4e-3001-bf22-81b17a757f9e | -6.77443 | -59.44387 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f13cde8a-aed2-3677-bb9b-b0760e09fa61 | -5.77762 | -57.54734 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a54e7dbd-11c3-3efb-b09c-ffcfec3a3821 | -6.69036 | -58.71518 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06dc5fc6-dd08-394f-a88a-60e319b878f8 | -6.15453 | -53.68608 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d576d50-660a-3e65-9df6-395dc14934b8 | -7.52046 | -61.38785 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 06c8157a-9274-31f2-b92d-dce33f5ad613 | -4.05969 | -56.34124 | 2026-08-26 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0377ad7e-2324-33ba-bf3e-dde5fc47c94a | -6.24988 | -53.36627 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0797b0d-a7b2-35cc-a574-e843d329244f | -6.11854 | -57.82703 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3ac17db-32fc-363f-a9dc-ff93d343207e | -7.00718 | -59.23525 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6301fdb1-f931-37d4-91d0-ec426967da9e | -6.60723 | -58.38385 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc248692-a6e0-32ca-8ed4-514d9190db5a | -6.68704 | -58.71465 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fdbb41e-c98e-3c85-83cb-23af09f0616e | -6.64734 | -58.51194 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d47a62dd-24ba-3887-b744-cfb4fb341b9f | -8.57137 | -55.27491 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2b7c236-2af1-3fd1-9a79-8065dc7d9c70 | -6.86031 | -59.71465 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 064da64f-fbff-3b2c-9aad-48bd9ce30b52 | -6.13593 | -57.848 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a6fb4a3-e58c-3bec-8866-80e6b8916d15 | -6.88302 | -59.44349 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dffe7254-56b4-345e-a530-9bcf6ab7b855 | -7.02266 | -59.22348 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a3b1da0-ea5d-369d-8c4b-895dce6c376f | -6.54859 | -58.51798 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e0d864-bf22-3722-a038-6ebbcbdf6ab1 | -7.26425 | -49.86222 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dbf48c6-6254-3807-9223-87f607284d0a | -6.61778 | -58.38194 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da1592f-9228-3884-af9b-3e1a22ddce72 | -5.85381 | -57.75335 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a14bfa8-add3-3ec9-8cb4-e21f8d091548 | -6.23341 | -55.4758 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 928f3d03-8197-3ac4-aadd-2057ddd8f71c | -6.12412 | -57.81333 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20223eb6-01c7-3c0a-8d10-d84f96500034 | -7.38057 | -59.99138 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5a1d3f2-71c3-3c1f-b143-2f022b6ec110 | -8.03028 | -51.81082 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| daf9bd0f-4c22-34fe-9509-db4e60ed8271 | -6.78427 | -59.74183 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 306a1094-1593-3e9e-8b95-887f0151727e | -7.49782 | -55.352 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8b495d4-b9bc-3bde-b377-fa5cd25b00e5 | -3.5323 | -48.18719 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41dc4ef2-3ee4-3cd4-b2b8-9fbefdf7a9f8 | -5.77312 | -57.554 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 447448d5-4cb8-341d-a624-d86dd48115b2 | -6.17349 | -53.47408 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ad6db38-61e8-357c-a868-d47c7e7e67ee | -14.79898 | -48.80202 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e0876bf7-5a84-3db2-a919-aabb44d95be7 | -10.76663 | -54.04185 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| ce9179f4-6d3c-356b-a935-151f6fc8e9d6 | -10.78565 | -50.9238 | 2026-08-26 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 228af958-736e-31dd-84b5-a621d9acb5af | -9.59669 | -60.52611 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf44bbf3-d473-39b2-bbf0-e4d849cf6b7c | -13.29638 | -51.45717 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 0f4c6029-dcd9-3d9e-b9de-ea83a4eca9b2 | -12.66261 | -48.41442 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 008ba4b3-3e9c-3378-8699-fa64d57c47a7 | -9.45278 | -60.53549 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b6dc2bf-4fc3-3a8e-a8d5-560f5e8150e2 | -13.2562 | -51.5203 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3a671c65-a068-37ba-ad08-9e231cc6ab82 | -9.17866 | -59.58215 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 649b4b38-7ed4-374b-bd65-f35e5d67d1fc | -12.08036 | -64.24384 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fac2975-91f4-3f46-9940-d704b6e25d5f | -13.17748 | -51.3422 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 518a77d7-da3d-3e6e-9967-7192e1e7d567 | -13.29596 | -51.46054 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| c5d4104a-4f4a-395f-9d3e-e34d031c71a5 | -13.21785 | -51.36829 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4553ba91-1eef-306c-94f8-2ac304451283 | -12.67597 | -48.41152 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 948f06c2-7675-3460-a963-1059f7025b33 | -10.76457 | -54.02467 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a36827ae-d3d4-385c-9283-8afb6b21c307 | -9.06281 | -60.43609 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de4c645b-2ce5-3043-9701-c832d8dce53e | -13.24787 | -51.36452 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8cd08128-cf6c-3863-ae65-93dbfd60c5d3 | -10.7597 | -54.02812 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 17056252-0a85-39b3-a9ad-284fc6949d09 | -13.23047 | -51.5101 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05262354-bf2b-30a2-9e2b-42b6f97739fe | -13.25655 | -51.383 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| ffa6fc36-7aaf-3ea7-ad26-37e0fd84a6df | -10.76288 | -54.0371 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 26fc1e41-5257-3fc4-913e-28d2a7641b91 | -9.60399 | -55.11269 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 659d3c1e-ee31-3ec3-a553-06d772821fe9 | -13.24007 | -51.38431 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cf3244d3-71f0-379f-9c82-401ce6f8b0f5 | -13.23908 | -51.52821 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ded3f2a-5575-349a-a399-0cc45f3e093a | -13.23634 | -51.36995 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| cc067ffd-9a49-3728-8f2a-21fc5fb7cfa9 | -13.23431 | -51.38702 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 262777bd-a1d6-3b49-a82d-d1a725b11ebf | -9.67011 | -55.09396 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e96b3520-c317-3f22-b127-c7efdb0863b5 | -10.75594 | -54.02338 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f2f0b672-9055-3ebf-bb2c-d41ad11a0429 | -13.18821 | -51.34361 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 6787851b-228c-3a18-a216-13e0a9c070de | -9.28007 | -60.90254 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2b0dfec-42d7-37c9-8a78-3a3f0b1036fb | -13.33505 | -48.21055 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7735ddaf-ce7e-31dd-8162-bd971238a77f | -9.44231 | -51.68471 | 2026-08-26 05:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed52e55b-2bc4-345d-9ba6-cc511dc76178 | -10.08005 | -58.54096 | 2026-08-26 05:29:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 606b19b5-aa57-336a-92b6-5c7cd59ece0d | -8.82441 | -62.33318 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96a2de1b-fe3b-36f3-bdbc-27fffbf5e40e | -10.7672 | -54.03772 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 368ef5ef-a1b9-36ef-9397-5b15e3d76534 | -9.19914 | -59.58185 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README60.md)
