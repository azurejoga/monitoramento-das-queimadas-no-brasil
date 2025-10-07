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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04ad3fdf-047e-354b-88c6-9d6977169d01 | -9.1789 | -47.818 | 2025-10-07 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c9a18d53-f5b4-3ee2-9738-9459e89b1af6 | -11.7409 | -45.371 | 2025-10-07 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 55735623-39a1-3a3b-88fe-11c4d7f2605f | -12.9103 | -54.7352 | 2025-10-07 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 270.9 |
| 97d0f60e-008c-3018-8bd6-9b6ad2bde863 | -6.9893 | -42.0004 | 2025-10-07 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 483777f0-07f3-329a-be6e-1d3760ec1af0 | -9.921 | -50.2109 | 2025-10-07 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 81e29351-88c0-360b-b4b6-4b0ba056da2b | -9.1786 | -47.84 | 2025-10-07 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| c22204ed-200d-3437-b22c-beb0a1dc5b3b | -11.7201 | -51.4465 | 2025-10-07 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e949ee34-0a42-3a8f-b60f-9be2341bb8d4 | -13.2229 | -51.6957 | 2025-10-07 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| c24bd37f-40db-388e-9d9c-caa3b57c81e1 | -12.4919 | -54.7158 | 2025-10-07 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 8d21dc83-a438-32ca-91ff-7256d1f2bea1 | -13.0029 | -51.0838 | 2025-10-07 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 40043fe8-ad76-35bd-a716-5e216c6798e6 | -10.2129 | -54.1262 | 2025-10-07 14:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 19d4a403-e633-355e-829e-7461e943166e | -12.7637 | -50.4921 | 2025-10-07 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 80777987-39ba-3740-9fcf-71d4ee3565e7 | -8.1702 | -44.1377 | 2025-10-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 952416a8-1e5b-3111-a4c0-b3aca3a50be5 | -10.1569 | -45.493 | 2025-10-07 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1e576a17-ce8c-3e68-9219-7889eafea780 | -9.1975 | -47.8381 | 2025-10-07 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b7e5b28c-61b7-34b4-b1d3-efd6f71b7d1c | -14.8641 | -51.4373 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 074be10d-60af-3509-99eb-4c65cb6c2bab | -13.0228 | -51.0386 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6caafa1a-6d48-3e6d-8be9-6d3e8c599046 | -7.6648 | -45.4471 | 2025-10-07 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1c86d363-ef17-3f63-bc81-5746779f770d | -8.4819 | -46.3361 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 4d676848-6a53-3d87-b928-610ef8ba0cdc | -8.8903 | -46.8081 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0f2a9832-e9f0-34f2-a02b-83dbb9c59bf3 | -15.3783 | -48.0197 | 2025-10-07 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 4df3382d-14a1-3934-8cb2-3f82b6465492 | -14.8451 | -51.4185 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f17e6953-7b3d-373b-8f98-bcb3e5db67d5 | -8.9759 | -47.4864 | 2025-10-07 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 86f62ffa-98c7-37a1-86a8-c14b67f382ef | -8.6397 | -47.2769 | 2025-10-07 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 75ae2a9e-3ac6-3b8e-bd52-ff0a099284fd | -6.9704 | -42.0023 | 2025-10-07 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 837afddc-0723-3aa2-b62d-89eb7c00d225 | -11.2623 | -50.2838 | 2025-10-07 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 234b59d3-15b2-3f45-9c79-8ed9547edd05 | -10.9303 | -47.0882 | 2025-10-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| b66aedee-ac80-3ad7-a81a-77543c85f190 | -3.6328 | -41.536 | 2025-10-07 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 489cc1fe-fe53-3b2e-9b08-17b3d901de39 | -10.3854 | -47.9956 | 2025-10-07 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 263075e2-824d-3c39-97d6-c36dd8baa01c | -14.941 | -51.4695 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 51c42bfa-572b-3b85-b2aa-c972ef5acbe4 | -10.1573 | -45.4701 | 2025-10-07 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 5f7abf04-ecb3-36ec-8232-0bbc93658cb5 | -9.6804 | -45.6645 | 2025-10-07 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 9316e0a2-9913-3b40-8afe-14005a62a35d | -18.9846 | -47.8282 | 2025-10-07 14:10:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 127b1b39-5ed7-3236-8d31-b4df52641a2f | -11.0448 | -50.926 | 2025-10-07 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 52fbdd6e-89e0-3977-93f7-122737469e80 | -13.004 | -51.0195 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b1a2ecf0-d02f-3b0c-9e47-a897f246117b | -14.6327 | -48.3219 | 2025-10-07 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 78eb2543-f958-3c61-80a7-f17f63431c77 | -11.2626 | -50.2624 | 2025-10-07 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 78018fca-ce59-3abe-8395-4dfa334a707d | -11.8823 | -44.9583 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 92216252-f0d8-3e70-98ac-b3b34a3a2808 | -11.0451 | -50.9047 | 2025-10-07 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 9b4f74a4-0eba-3f77-9165-edaed7e7c60c | -11.7217 | -45.3738 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d9f28788-1d0e-3f0c-a91b-518717eb457d | -14.3339 | -45.8545 | 2025-10-07 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3e6a782b-8631-39e7-98dc-aa156f07b0f1 | -11.7837 | -45.1115 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 19377edf-efe3-3889-8b1f-f7616c23ad93 | -13.0939 | -47.9992 | 2025-10-07 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 61f33ba4-4ea8-3cb2-b048-61acb92d99ea | -8.6208 | -47.2788 | 2025-10-07 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1e6ea58f-a683-31e1-a8dd-c9b2bd6a88f7 | -8.2077 | -44.1568 | 2025-10-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 242.1 |
| d083b3c8-30d4-356a-bcd0-1ccc8807d614 | -7.4672 | -43.0438 | 2025-10-07 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 1cfdb4db-ac1f-3b97-9c4e-8d5aaf8be925 | -19.0295 | -44.7327 | 2025-10-07 14:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 045643a6-e970-38aa-a769-89f6c0a87756 | -15.1357 | -45.7104 | 2025-10-07 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 52ded317-5720-31c8-8d42-d2b28d350a0d | -12.9294 | -54.7333 | 2025-10-07 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d5a2594e-a355-3ed5-a7e9-fc2366b961c0 | -9.7463 | -47.7144 | 2025-10-07 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a3bd3c48-9355-3a9a-a384-917a119da3a0 | -16.0012 | -50.9674 | 2025-10-07 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 0df681f0-2472-3650-90fe-8f27b28044df | -15.1352 | -45.7337 | 2025-10-07 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f882f450-6b00-36a1-8ac2-9fbc0663ba39 | -10.2129 | -54.1262 | 2025-10-07 14:10:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 8f7a7c0a-22a8-3abc-b078-3fd1af015a42 | -7.4669 | -43.0674 | 2025-10-07 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 8b993b0d-a9b8-3ed2-b288-6150ab5377c0 | -10.4477 | -50.3285 | 2025-10-07 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 23042552-c924-3eb2-9407-abe679aaabe4 | -8.921 | -47.3595 | 2025-10-07 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4ac22e0d-c95a-307f-bfc8-13e652af6623 | -15.6198 | -52.5715 | 2025-10-07 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 11e092a6-6fd0-3af7-96ca-4a74a4e47f1f | -14.8645 | -51.4158 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8b9c4cc1-9e37-3aec-9629-ac2f2fa0b5a8 | -11.7641 | -45.1375 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 0a4f3efe-7e72-3af8-a37f-880c92e8c5fa | -11.7409 | -45.371 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1c37b7e9-c4d9-3604-b27d-d37cabeba416 | -8.5207 | -46.2425 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 2b55ad49-c872-3a36-9f83-6f60a8ced0fb | -9.2164 | -47.8362 | 2025-10-07 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3d4a6bb6-3da5-393e-b72f-797a399833b3 | -14.8637 | -51.4589 | 2025-10-07 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 56a9638a-0ea5-3987-83af-0685ff5fa52d | -8.5395 | -46.2406 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 6f39d84a-d47c-34ea-8410-8af2001531d5 | -8.2266 | -44.1548 | 2025-10-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 567fc335-578a-30cd-ac1e-6d3da3d59597 | -9.1978 | -47.8161 | 2025-10-07 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 944beaef-663f-3b8b-898f-d90da5a27074 | -15.1548 | -45.73 | 2025-10-07 14:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 30240bfd-cc8d-3c8a-b635-1c6a8aadcd6a | -7.7933 | -44.1304 | 2025-10-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cc3e062f-2fd0-304a-9657-35b9426afbb1 | -9.1786 | -47.84 | 2025-10-07 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2a8a8257-5ab3-322c-a904-e06a51b7db94 | -12.9816 | -46.7824 | 2025-10-07 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e6d6df90-16c6-3b0e-946b-b2d634b9ee37 | -11.8447 | -44.9176 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b3452a15-9e5f-3f1c-9e17-2e0e8ac6d44a | -11.8635 | -44.938 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 817d53ad-0456-3ec7-a41f-be5277923c52 | -8.5941 | -44.9209 | 2025-10-07 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 038c4e8b-966e-3bf3-8c37-7ba76ce8154c | -13.8667 | -42.3164 | 2025-10-07 14:10:00 | GOES-19 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 8bf994aa-04c7-3fc2-84ed-c516bb75a934 | -10.9296 | -47.1329 | 2025-10-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 718f6933-7a82-351e-8cb1-a783b77d2999 | -11.2436 | -50.2645 | 2025-10-07 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 9bd9d160-a4b4-3509-9195-186c84814723 | -8.613 | -44.9189 | 2025-10-07 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 00fd34b6-8047-369b-aac4-4402ec5c9bf1 | -8.4824 | -46.2912 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d1b7a71e-b7e8-3f51-8073-f31ed4d87fa1 | -12.3158 | -45.3776 | 2025-10-07 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0c2e41f1-3627-38e3-bc47-553bcad68a9e | -11.9519 | -46.4352 | 2025-10-07 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d01b5e0b-1afb-332e-bd36-434ce2b414f1 | -8.8714 | -46.8101 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0c72b01d-579b-3e5f-9c6e-ca3e849fa709 | -8.1894 | -44.1125 | 2025-10-07 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 282.7 |
| be850bc9-f5fa-32ec-a8c3-07aff839d657 | -11.2433 | -50.2859 | 2025-10-07 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 0c006d0b-8140-30e9-8488-251a6c8b4640 | -9.9024 | -50.1914 | 2025-10-07 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3c45c7c5-f808-39cf-8f39-38ae8568a752 | -8.4821 | -46.3136 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4b083df5-3386-36cc-930d-ce9b73b07df9 | -8.8618 | -46.0949 | 2025-10-07 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 1d1551d4-fcf6-3baa-820d-b33b8e6a0467 | -11.1644 | -54.8804 | 2025-10-07 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| bc6976f0-7885-336d-9c1d-da0ae0225288 | -10.2968 | -50.3226 | 2025-10-07 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c7e7c53e-3e28-3662-b0b9-be2b15ef34cc | -10.6513 | -46.6978 | 2025-10-07 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 085aa16e-3749-3968-977a-6653e30288df | -10.4054 | -45.3931 | 2025-10-07 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 2e54de51-ba7f-3f49-acbd-3767fe8cccc3 | -15.3737 | -47.3201 | 2025-10-07 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 37f8d807-009f-352d-988a-9e5d0e61cbbe | -12.9103 | -54.7352 | 2025-10-07 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 208.6 |
| ef479287-828f-31a8-a3c5-4cb6e996522c | -11.2228 | -47.8516 | 2025-10-07 14:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 265893b0-4133-348d-b921-3b582c99467f | -8.5584 | -46.2387 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 9cf51d27-2363-3103-90b5-d1a122979091 | -12.6159 | -44.7519 | 2025-10-07 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 4ef056ae-5c4f-3c98-8cbb-5ada1cd7bdfa | -3.1306 | -40.9824 | 2025-10-07 14:10:00 | GOES-19 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 118.5 |
| b6e8310d-94fa-3b46-9e05-055a4b1cd261 | -8.501 | -46.3117 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 0263e30f-b23f-30ab-a9d9-8073e6fde320 | -6.9893 | -42.0004 | 2025-10-07 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 7c54455f-4647-347e-90f8-c334c762a846 | -8.5393 | -46.2631 | 2025-10-07 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e9f165b1-fbb4-3341-8626-d98f1b99048e | -11.8029 | -45.1087 | 2025-10-07 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |


[Clique aqui para ver as próximas entradas](README127.md)
