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
| 0efbd347-9592-33e2-8ba0-6b37dc6bd630 | -6.14011 | -42.96244 | 2025-07-24 04:40:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b3825c84-8e2c-311d-9f74-92e39c683a32 | -2.38704 | -47.63099 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 636b1f0e-6adf-3b49-a959-fc467f8ee252 | -4.05513 | -42.51105 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 99c7af17-0ef5-31e6-bef1-2a6a1447d819 | -3.16855 | -49.45513 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 76503011-2d28-3705-9156-09633c131dc9 | -8.04164 | -47.65159 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e94a4eda-3e1d-3018-8edd-b0c749aaf327 | -3.94817 | -41.48959 | 2025-07-24 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dda14bfa-d9f6-3c38-99b8-9777056e5502 | -4.0533 | -42.51294 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| dc5d897e-8f73-3851-a242-9080c7c392e1 | -6.26474 | -45.26987 | 2025-07-24 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bb626bd-5048-3d7c-94be-cefa6058876a | -6.26091 | -45.26938 | 2025-07-24 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c71901ab-b7e8-374b-95ac-d5726a038572 | -7.71885 | -43.9538 | 2025-07-24 04:40:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2c730ed-fcc0-3c44-be5d-292706b3a81e | -4.0609 | -42.52288 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 868e5305-9977-3b82-a0c2-560d0542ba9d | -7.10823 | -43.32931 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78e3c31f-c0d3-363a-b8ae-cb17d03e658e | -7.26102 | -43.07495 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| c99656a5-a1d7-3555-a7cf-8e13e67044b0 | -7.25463 | -43.08761 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d2d19926-c80f-3885-9c62-237e1fa4d535 | -4.05004 | -42.51471 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 872ba20d-6336-3be4-895d-6c058698d8d7 | -3.17966 | -49.44972 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 91fed2aa-029e-348f-9eb9-efdd560d54d4 | -3.12042 | -47.01161 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec5357d4-5bf2-3bda-9ff9-96c7d3c06fb5 | -7.25272 | -43.06915 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 2b5e850d-e85b-3852-96ae-146023e2beec | -3.17244 | -49.45216 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 63660e95-c79f-3a91-9ddc-eb7b1bf60034 | -7.15532 | -45.23907 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bc59240-8038-32e2-b237-9e5e2f202f97 | -4.51302 | -42.08285 | 2025-07-24 04:40:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3fed354-4ffc-3b09-9931-f180cbe0e91a | -4.05447 | -42.51537 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0ef53343-f282-3992-abd5-6ef4386afe8f | -3.03036 | -49.42633 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f87aac49-7b80-3906-8007-728e9d60f839 | -3.04208 | -47.37876 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49673c2a-56d6-3e37-96e9-84b8e3e5cffb | -7.46426 | -49.40498 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7e39e289-d7a8-3cee-8d8f-40326fba6707 | -4.05137 | -42.50607 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c09db432-50b1-3615-bc23-0707305d82c6 | -5.68243 | -43.6668 | 2025-07-24 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b89ebe53-bad9-3b42-ac07-7da47838634e | -3.04152 | -47.3823 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8aadafd-441c-3023-acca-0b27a9dda9c0 | -2.45654 | -48.15414 | 2025-07-24 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70c313c4-48a3-3d80-aec0-1a4373fb0929 | -8.03704 | -47.65865 | 2025-07-24 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19455494-96f2-3a10-a15f-83271f9202a0 | -0.74962 | -47.75269 | 2025-07-24 04:40:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90a0afa6-91e3-3792-a310-f32bc8e2f120 | -5.13998 | -45.16853 | 2025-07-24 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77d73578-a068-3a05-8fe0-fc8d92d8e2f3 | -5.89136 | -45.19424 | 2025-07-24 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab938d33-07ad-3923-a02c-c898b09826da | -7.718 | -43.9523 | 2025-07-24 04:40:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 867b8298-29ad-37b7-ae67-2501e26a40a7 | -5.74139 | -41.01704 | 2025-07-24 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47efe0ff-a6da-3b90-a1bf-82bbd47ac787 | -7.84251 | -44.4855 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9930310-dda6-3d24-a4ca-381e34a3721e | -7.24187 | -43.08115 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 14d5b206-a231-3f0e-953b-82a1e6f5e666 | -4.30192 | -48.10012 | 2025-07-24 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 493eb343-3a19-306f-8339-7a09e6f74644 | -3.58454 | -47.52395 | 2025-07-24 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 774c2610-4a77-3285-a540-ebc1e2f38503 | -5.65365 | -42.58061 | 2025-07-24 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 467eb519-1b96-3cbf-aaf9-8bae927a31d5 | -7.46258 | -49.39403 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed7f68ee-157d-3931-a6fa-135c89f3ba2b | -5.75083 | -47.96543 | 2025-07-24 04:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f3ff228-1cef-3a8a-900c-257edd2fd275 | -2.58635 | -51.92037 | 2025-07-24 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ea2e1f4-8cf6-394b-99a4-f24ab27b82e6 | -4.81058 | -43.21677 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c8057e4-ddfd-3567-ba01-bf267893f5bd | -6.88599 | -45.24848 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4198b99-30d3-301c-a45a-67aa20de9658 | -2.58565 | -51.92465 | 2025-07-24 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 025d741c-dbe4-365b-b80b-112cf1692f6f | -5.9106 | -43.46277 | 2025-07-24 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed365ef3-0f9f-3f0b-ac97-a76171283f91 | -6.89026 | -44.20294 | 2025-07-24 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6b06e7f-59c0-3071-b91a-0b2b730cca84 | -7.94702 | -46.29027 | 2025-07-24 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a2dc64c-4d88-3ff6-ae91-1b8a4957562b | -3.17688 | -49.44571 | 2025-07-24 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f71e7a0a-eed7-3b63-8c8f-cbb9bab6bbe1 | -3.47077 | -42.85444 | 2025-07-24 04:40:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c6947fa-319f-3c6b-8828-c00af4a0d613 | -3.10794 | -47.49411 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08cf2b11-917b-3892-a203-c7bdef83e38b | -6.53803 | -44.65933 | 2025-07-24 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62b78427-0a81-3468-9b43-f49840a71cd4 | -4.17101 | -42.02509 | 2025-07-24 04:40:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b37e137-2e08-3837-8dc0-a8fd0d5b9904 | -6.88972 | -44.20663 | 2025-07-24 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f3e2c58-b49f-32a1-9210-22b918794a58 | -4.04825 | -42.51659 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5557ebaf-a548-360c-95c8-718792ffb98b | -4.77862 | -45.33665 | 2025-07-24 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| cb3c24a9-8431-3f32-9943-6850d0311020 | -8.29675 | -44.96894 | 2025-07-24 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81a4ed47-cc3e-310a-9c58-b651d5ce50cb | -7.88267 | -46.89279 | 2025-07-24 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86ec46e-3169-3c35-9aa3-a5747ea13bb1 | -7.25207 | -43.07365 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 16126f2a-db79-340f-a39a-b82531923d4d | -7.54306 | -44.46097 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a58265ed-3d99-3476-8964-47cada476213 | -7.06982 | -43.91857 | 2025-07-24 04:40:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb48008f-7f53-3340-819f-28b09879fc1e | -4.81173 | -43.20886 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f6e08b6-114b-35e5-926b-240a875c6fad | -3.88334 | -54.24449 | 2025-07-24 04:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88621bc0-50c8-3625-b753-00dfc8d64427 | -3.47284 | -42.85199 | 2025-07-24 04:40:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba71c752-edaf-3ead-acf3-f6ca37a5d2e7 | -5.18806 | -44.9569 | 2025-07-24 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28bc7244-202f-38c0-b12b-0d8e9e2002af | -4.51372 | -42.07815 | 2025-07-24 04:40:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 334c2331-5a4f-3277-9d3f-07d145fb662c | -4.1756 | -42.02583 | 2025-07-24 04:40:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1c8f4ac-22bc-3e55-bd65-86deeb628215 | -3.04544 | -47.37927 | 2025-07-24 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9c6f9ae-3279-331e-934d-49670e01fe7f | -4.04365 | -42.52689 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0bee2cea-460e-3532-968a-fb4a7c576706 | -4.80746 | -43.20821 | 2025-07-24 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71bb99b0-6839-30c4-a81a-8d84dbb2833c | -3.79701 | -40.99986 | 2025-07-24 04:40:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44ed2ab2-53b2-35dc-b295-aed2df36cebd | -4.77489 | -45.33604 | 2025-07-24 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3a814fd-424f-300f-a078-4c29b06bf198 | -5.69457 | -50.04776 | 2025-07-24 04:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a07537d4-b28c-3e3b-a883-0ff56cf50771 | -6.82283 | -43.99038 | 2025-07-24 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04662cbc-cbc1-3cca-9941-1115933f1795 | -3.93318 | -41.49249 | 2025-07-24 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f85903d4-af94-36e5-8e93-f49931bcd190 | -6.89325 | -44.2112 | 2025-07-24 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76411d16-f969-389b-9777-e065e8ba1a59 | -4.05957 | -42.5117 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d898b54d-1024-315e-b891-e5ba450cbbc6 | -4.10646 | -48.20577 | 2025-07-24 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 482d48b9-c7a0-316a-a9fe-2b6d882e8451 | -5.9825 | -45.35741 | 2025-07-24 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd30066c-5dcd-3b38-9d0a-a7b709361d28 | -7.16737 | -44.37327 | 2025-07-24 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c03511-d61c-30ca-8d12-7e6a7e68116b | -3.95542 | -52.20381 | 2025-07-24 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3be7dbd3-6a35-38b2-9e64-299596717de2 | -4.04562 | -42.51404 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 90978106-c25d-3b40-b678-973d2deaf00d | -7.36408 | -48.13818 | 2025-07-24 04:40:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0251a29-0d75-395a-83c1-463e332b0bc2 | -7.24696 | -43.07742 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| dd3385ca-d658-3ca5-b212-bce1dd80469b | -5.97872 | -45.35683 | 2025-07-24 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5d3f4a8-9d0d-370e-b272-c1cfa6e55562 | -6.88307 | -45.24971 | 2025-07-24 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 499759ab-3482-3719-adb3-a1026cf3fe60 | -4.88575 | -44.96007 | 2025-07-24 04:40:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f70eab46-1b7b-3bdf-98f6-452085123af9 | -6.82171 | -43.99796 | 2025-07-24 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 968ad9c2-d8f3-3cd2-aa52-02e3fc091305 | -4.05315 | -42.52397 | 2025-07-24 04:40:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ffb4770-7de5-3ba6-a835-609a22f8229b | -7.46203 | -49.39751 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dfa9c5d-1558-3e2a-8927-ab38bd6d0a97 | -7.97619 | -49.95688 | 2025-07-24 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9369cdc7-f20f-3337-ada1-79aa43b196b5 | -7.14642 | -43.80592 | 2025-07-24 04:40:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a51ef2-e07d-330d-bea2-2e88f6496d01 | -3.97855 | -47.88153 | 2025-07-24 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8feb2c03-3f56-37d6-9935-9e0624158c94 | -4.06217 | -42.51425 | 2025-07-24 04:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a8e89e4c-e623-31e3-8b33-3b0cfeff6966 | -7.30898 | -49.57257 | 2025-07-24 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52336ec7-2aff-339b-82d3-333cca2e8357 | -8.07073 | -49.72245 | 2025-07-24 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 683444e3-1a66-397d-91e2-e3aa7b3e966b | -2.65881 | -47.39942 | 2025-07-24 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e35e705-8b09-3842-b0ca-d7c466fefa4b | -7.25654 | -43.07431 | 2025-07-24 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 60a6e25c-5611-3494-828f-ccb39c351b51 | -6.46595 | -44.58395 | 2025-07-24 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README16.md)
