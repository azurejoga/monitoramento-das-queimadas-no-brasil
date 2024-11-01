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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f703f576-bd41-34bb-b4c0-8f3b22054a7b | -2.87311 | -48.66272 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 610288ff-d580-3ad3-8dda-a7cdcc7b08b7 | -2.86814 | -48.66189 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9434c44-17c0-3577-b928-88d9c037a049 | -2.85819 | -48.66029 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b07852af-acac-3a43-8e5e-953e96288a16 | -2.83234 | -48.43874 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24856a08-e779-3d33-89ff-8eb2c9a4d561 | -2.83079 | -48.35542 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f009482-90fe-3e15-8b6b-688274e254fa | -2.82832 | -48.43248 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49e8da5e-6539-3115-bb91-02ae5b4e16a4 | -2.82745 | -48.43791 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f056fb3c-7405-3e7a-8e59-ed48d487ca02 | -2.7735 | -48.64494 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce91930b-e457-3daf-b8e4-139afe7c6b1c | -2.77258 | -48.65056 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 021a95c4-a1cf-39d9-baec-cad37d9ad26e | -2.76761 | -48.64974 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3212cb1d-72d8-3dcc-98db-bcb446ccf0c6 | -2.71328 | -47.99515 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e33969b-1da0-3759-8ebd-aa93f2501821 | -4.93058 | -49.1547 | 2024-11-01 04:06:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5934e819-ee4b-36af-aebc-4c9cccae62aa | -4.9136 | -48.64766 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 677960c1-f5f7-3566-8623-1c98fe4844ab | -4.87272 | -48.57366 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4fe0081-e24d-35d2-8dea-87024dffaee0 | -4.87249 | -48.5709 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54d4dca6-7769-3ed0-8b8d-5dd442b95e6d | -4.87159 | -48.57611 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d53b11a-a9bb-38d2-b21c-811efa712850 | -4.36373 | -48.2177 | 2024-11-01 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 564ffb5d-2aaa-36b2-b991-4e38985a6071 | -4.22002 | -48.06028 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d282570-fda5-3dfc-b703-90d15f4959ec | -4.21917 | -48.0653 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9387a171-7451-3998-9ab2-8a5cce1111a1 | -3.94154 | -48.34695 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c0f9dd4-3e55-39e3-bbd4-75bd27c8e448 | -3.94084 | -48.35001 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98355e51-4ed7-37b1-916a-b0ec428bd013 | -3.94071 | -48.35208 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b67c5d4-eb36-3653-b4d8-464d0323f263 | -3.93996 | -48.35515 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 40aa0550-0988-3a67-b9c5-ffaa64b2d584 | -3.93986 | -48.35732 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 676e4c35-9eed-3d0a-9f0e-e479448966bb | -3.93906 | -48.36046 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 323c90c7-2eff-3815-8fd5-8ad3f40f9c3f | -3.939 | -48.36264 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ac6ccac-5d21-3f6e-9096-f4519d492c91 | -3.93678 | -48.34606 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd1a274-393f-3e99-ab71-c64092b97a82 | -3.93509 | -48.35646 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aea44a9f-c10b-3b0c-956b-10fa814cc307 | -3.91259 | -47.93688 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa9e5333-47e2-36d3-ac9d-002d3a9ddf6c | -3.91178 | -47.9417 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f750a8c-94b8-3cb1-b01d-929858e42c08 | -3.90978 | -47.93972 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad6f85b-1d94-37a8-98ff-580aaa676d99 | -3.8751 | -48.36232 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bee7803-85df-3a41-85e0-ea5c5d6b4a2f | -3.8703 | -48.36161 | 2024-11-01 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28082681-bbc6-3f05-b5e9-fb6e74ab42a7 | -3.73273 | -47.64392 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f57be45c-06bd-35b1-8b82-5c51c6811c69 | -3.73203 | -47.64558 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e17630c5-d867-3f1c-adc4-f2f512710e98 | -3.73199 | -47.64854 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52024b7-a114-3db7-81a5-153d733fa041 | -5.38971 | -48.95665 | 2024-11-01 04:06:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48987460-cd9e-35d8-b845-cf2e2ec84fe9 | -5.31771 | -49.1329 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b544ab25-f892-390c-8de0-dc9408790e7a | -5.31355 | -49.13489 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7c5646a-82a4-3c02-81cc-067aec919b49 | -5.31278 | -49.13203 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfe069f6-e1a4-312b-9992-7353a598fcd9 | -6.39077 | -49.57263 | 2024-11-01 04:06:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddd04acd-bda7-30e7-bc2c-7e7170e64b89 | -6.38579 | -49.57169 | 2024-11-01 04:06:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b7b1327-1da5-3f64-9527-ae5819e30ebd | -5.98643 | -48.15023 | 2024-11-01 04:06:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25ca159a-6088-3d33-9a3c-ebb1b1c0428c | -5.71212 | -49.31861 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fab9dcb-24cb-316d-91cc-8bd82dd54194 | -5.71194 | -49.31585 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32010307-6df4-3b39-9d3a-4e6e1de89412 | -5.70913 | -49.30657 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e09560f0-b517-3972-8e6d-131364484cf2 | -5.70716 | -49.31774 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c46b3979-2ab3-3c2b-a8a1-273ea66c5375 | -5.70699 | -49.31494 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d286f8f-fbcf-381f-87d5-72be672bad09 | -5.52374 | -49.48958 | 2024-11-01 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b0883b-a9e4-3779-9589-4735dc9fe127 | -2.17086 | -49.11594 | 2024-11-01 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8b50004-a071-3251-b765-872c9ef22bf6 | -2.17036 | -49.11906 | 2024-11-01 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90932f68-c5f0-3902-b2a3-5c56aea0e532 | -3.27148 | -50.34167 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c13f2011-8793-33a3-ad6c-894aa1d2b23c | -3.27086 | -50.34527 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b55216-fc92-3c4f-b8c8-f3c1c93edf70 | -3.27023 | -50.34891 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e537a9f-4253-3917-8392-2bb0e5e060fe | -3.26754 | -50.33853 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7230783b-2356-3d9d-b96e-f3b123ae0607 | -3.26694 | -50.34214 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d5278084-88b0-3e16-828d-bfc6df0fdcb6 | -3.26635 | -50.34575 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0114951a-d45f-3c56-abdc-f125484d58ad | -3.26574 | -50.3494 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 529942f8-459b-3b19-a5ee-74659ce0986c | -3.262 | -50.33762 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25c6bcd6-a273-3bcb-9cbf-56f69ed9663d | -3.26141 | -50.34122 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5cdd798-9819-3f91-8334-09dbf3ba1c56 | -3.26081 | -50.34481 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53472e6b-80bf-3bdf-a0fc-f3be9d8df2ea | -3.26021 | -50.34845 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bd808d8-ef5b-36d9-8994-5baee847d4f2 | -3.25647 | -50.33666 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1a7d907-1532-3f7b-8fcc-3d82bb234b0c | -3.25588 | -50.34026 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6b7ac21-a27b-3a8e-bc8e-5ce3457decb1 | -3.25528 | -50.34388 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8de620ce-5216-349d-8753-cedf68829031 | -3.25468 | -50.34751 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a6b1d4-33ed-31e2-b275-0187142c9ab3 | -3.25457 | -50.04529 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fd09001-ccfe-3750-9136-3a9266a60a94 | -3.25398 | -50.04878 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 970b212e-acba-31cc-8bc9-1fcadcaa912e | -3.25095 | -50.3357 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 328393f4-db46-3e81-bddb-a37f6a8c0390 | -3.25034 | -50.33934 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efc20fdd-f96d-3b87-a13f-d7aa676a8eac | -3.24974 | -50.34298 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08cdaf4b-5b41-3dbc-8a10-379361d63a2c | -3.24915 | -50.04433 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ddb9cca-194b-3ff7-b6c6-b697b88679b9 | -3.24913 | -50.3466 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7f9d8a2-e3f4-358d-b140-545029a21079 | -3.24856 | -50.04783 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 375bf1dd-8ed6-3bb2-a0a0-ac379cbd52d2 | -3.24542 | -50.33477 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c26f0e3-881b-3614-ab90-aafe5a58bfb1 | -3.24481 | -50.3384 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9aa665a0-ab55-3956-b7cb-704555a307d4 | -3.18162 | -50.57867 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb0bf307-5e66-3948-8b33-b6fbf1a9d330 | -3.18034 | -50.58622 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd19b3ff-cee1-380b-bbd6-d1114f86ef60 | -3.17971 | -50.59001 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d7d3e89-8421-3163-bd14-f446c29c241f | -3.17536 | -50.58146 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1eb92d3-529a-3941-b99d-ad8625d2798f | -3.17472 | -50.58525 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c278247a-94d2-390a-a871-509a166a93df | -3.17408 | -50.58905 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bdd3652-5796-3564-af26-c10da2479bfd | -3.16909 | -50.5843 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be491be-3b94-3840-824c-29ee6307da4c | -3.16845 | -50.58809 | 2024-11-01 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b0a2c82-1ed5-36c4-a36f-f71de8e847b5 | -3.05456 | -49.48144 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7525efc-bb35-318b-b9c2-35ca368575df | -3.05404 | -49.48461 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5478048f-2ee6-3e33-85d3-9be4763edfec | -3.05351 | -49.48777 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a4f3f66f-cc7a-3dae-b24f-2af4369bd291 | -3.0509 | -49.47109 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f01fe173-f470-3f25-8af1-d1599f8cae6a | -3.05038 | -49.47421 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bca36f26-9264-3ca3-8530-41176b61cbb0 | -3.04986 | -49.47733 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 640ff85c-f984-3444-be20-3951b45d7262 | -3.04934 | -49.48048 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 98502e20-ac41-3009-a467-102c6ca93072 | -3.04881 | -49.48367 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ef85db85-67b4-3f09-a8d2-fe5919bbe61b | -3.04828 | -49.48685 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3c4fae20-6dc6-30e8-975d-21e23679c627 | -3.04775 | -49.49002 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 662eac69-e584-3711-913d-56c99dcd56ef | -3.04567 | -49.47013 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b02c51e6-ee0f-3c5f-9d94-0926828c79d4 | -3.04515 | -49.47326 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fb1bfbd4-15b3-379b-abd3-650db03ce740 | -3.04463 | -49.47641 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d7fcee15-1c22-3c84-8b64-5fa34ec0bd98 | -3.0441 | -49.47956 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c62ed079-2fc3-37ee-857c-0fef7be43457 | -3.04357 | -49.48275 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 69180a3b-06ee-3046-b856-2d2232ce6900 | -3.04304 | -49.48594 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README22.md)
