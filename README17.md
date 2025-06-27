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
| a3c6c610-3ff6-3e9d-86f9-f793d218f45b | -6.9793 | -42.8798 | 2025-06-27 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 9c1c35c8-eae7-3d85-a2c9-7ba10d417d81 | -6.9602 | -42.9052 | 2025-06-27 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 266.5 |
| 4df62c7b-8ce7-31fd-a9fa-48ba99de0822 | 2.74944 | -60.36658 | 2025-06-27 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8340eb3-ee83-3ff8-8bbf-ccc0a8fb29df | 2.75013 | -60.37143 | 2025-06-27 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec574fec-0d86-3a15-a12c-31ed729ce954 | -7.26257 | -46.9467 | 2025-06-27 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 342e9f94-d860-3d3b-aa19-d1b16bf4d027 | -6.21503 | -43.3627 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca15dc5d-896b-3e2e-a999-13f5cc345db8 | -6.96318 | -42.88853 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| bc299a63-3233-3ff7-888b-c4f05960d6c3 | -5.4401 | -46.56427 | 2025-06-27 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 259a8bc6-5e09-3c17-841a-5a15db5e6bca | -6.9729 | -42.89289 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e16d8f88-981d-3435-a8ea-f64218fd00ae | -5.0085 | -56.1758 | 2025-06-27 04:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1aab851e-3237-3b82-9987-e830791ade78 | -6.68858 | -43.06987 | 2025-06-27 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a10e0e7-6a8a-3ff1-b27c-213172551cc9 | -5.17589 | -46.11051 | 2025-06-27 04:46:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988e4973-b5d0-3057-900c-9d5b1f00b2e3 | -4.68752 | -48.86594 | 2025-06-27 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47eb64e2-96e8-301e-b1dd-953e97e94597 | -7.55983 | -45.63436 | 2025-06-27 04:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 042ed28b-6e82-3a87-89e5-d162b2355d7d | -6.47668 | -43.74739 | 2025-06-27 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54dd090f-9dc8-30e7-b9cb-45c468b157fd | -7.21218 | -43.07449 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 82ff1eca-7609-3d0d-baf4-5f1e984fba0d | -6.17629 | -48.08359 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| eb60ad48-3225-35e1-b340-fb2c68ba332f | -7.21134 | -43.08032 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e8812d1c-24b4-3a16-99ac-157eb2c4b6b8 | -3.03239 | -49.43429 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4654be29-accf-3af5-a085-52a202f675c8 | -6.18048 | -48.0801 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 738ccfdf-48b0-3e5b-b97d-cd22b9875437 | -6.47596 | -43.7523 | 2025-06-27 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f80931ce-2478-3806-96a0-cc36925e1fe1 | -7.53602 | -45.82687 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 32ebca27-9975-3889-88f8-f5067995fd93 | -6.17568 | -48.08765 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e7dd6266-60ba-3479-861f-166615f69f90 | -6.97332 | -42.88992 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 822b0269-f218-372e-af20-aca2c799022e | -7.55155 | -45.83709 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f427aa8e-83a0-36eb-bf54-39ae8c5aa507 | -7.20589 | -43.19249 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ebeb951f-267d-39dc-88d4-4eb11fe52fd7 | -6.57581 | -55.00246 | 2025-06-27 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f20721ea-4246-342c-a743-0b6371ff6cb2 | -3.31434 | -48.71846 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98f0ac71-6ae5-3d74-8196-48d386915b71 | -6.5012 | -49.31963 | 2025-06-27 04:46:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc13c01d-c2a6-3b84-ba9f-1a3e57798187 | -7.26185 | -46.95157 | 2025-06-27 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49714562-a737-37d5-8bed-80d98fc54f71 | -6.77582 | -46.32607 | 2025-06-27 04:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f845b817-5057-3acd-8096-865fe1828f9d | -7.19496 | -43.19405 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b081c6dd-9d7c-38d9-a90e-d1a2009041ef | -2.53132 | -53.95861 | 2025-06-27 04:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fc5b087-4486-3f14-84c1-3c59d5ceee09 | -6.95648 | -42.89956 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 1c30941e-7b03-3f14-93d2-53d864f236d4 | -5.91865 | -43.46854 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8df735f2-8389-3c0f-b2ad-5ee46d5857a5 | -7.21635 | -43.08105 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a555602e-3102-3862-812a-08e2c7b0ee88 | -6.4729 | -43.74832 | 2025-06-27 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c335ff8d-db65-358f-9bb5-489127d0f61f | -6.96742 | -42.89513 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 8179123f-0154-37c8-91aa-b3891ed378fa | -2.54685 | -47.70071 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e03fa94-2b9b-35c9-bd1b-d59560aa82cd | -7.01812 | -49.17926 | 2025-06-27 04:46:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bf6e15e-6146-30ea-a7a9-d42f68e22197 | -6.96784 | -42.89216 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 516fa2f4-f327-3e4c-9d2d-4e3b72cdd1f6 | -7.20491 | -43.19549 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cba9650b-2039-352f-a13b-3fa25454a783 | -6.57655 | -54.99793 | 2025-06-27 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd118554-8feb-301e-9ade-0b3a0e013db4 | -7.19517 | -43.1967 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb5b65f5-53b7-3ba5-961b-8bf9f2ccac20 | -3.02959 | -49.43027 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6510cc40-caf0-32d3-aef0-a58976b565be | -3.03573 | -49.43481 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 173895e5-cfba-3fee-a173-0315102e9798 | -6.95304 | -42.8872 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 270a05ad-7e93-36c1-ba1f-5a86dd9cb739 | -7.21069 | -43.08275 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 06128526-7682-3ee4-927c-d923e9ea56f3 | -6.77507 | -46.3312 | 2025-06-27 04:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7db044b6-fd69-3e5c-aa80-321784446444 | -6.96277 | -42.89149 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5c62f5c9-b7de-367f-b9bb-8e37a287e3b2 | -7.54434 | -45.82822 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2c99c3f-d487-3472-91b9-05e1ea02a216 | -6.96826 | -42.88919 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 11c7352d-fffe-3fcf-aef2-9b9b8277d7f1 | -6.47766 | -43.74881 | 2025-06-27 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 362c0f3a-b12a-35af-bced-2a2c3361e73f | -7.53962 | -45.83139 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0dfba4d1-83ab-3565-8765-9ddbc8bc5b80 | -7.54378 | -45.83201 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a732241-2ff2-38e0-9211-c1d31b5cb9fa | -6.68997 | -43.05909 | 2025-06-27 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8f87356-a494-3a7b-92da-20cb312666d9 | -2.91822 | -48.0667 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c653519-34ba-3946-90a7-9624501289fe | -6.96701 | -42.8981 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 85a6ef16-ef1b-3909-83f5-634d4f48f796 | -7.21228 | -43.07108 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 574618d1-1688-3cef-867b-42da8629b0ca | -7.53545 | -45.83073 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17d69ccf-c7a0-3d29-a568-0bebe31881e2 | -5.91645 | -43.48381 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb8cfba1-74ae-3808-b1c8-d8a1697cae27 | -2.28552 | -48.57721 | 2025-06-27 04:46:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5af443e6-52a6-3d8a-86e0-71ea84132210 | -4.18924 | -48.14854 | 2025-06-27 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 204eed90-b78d-380e-a9a7-8a6d5239741f | -5.91718 | -43.47872 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 691f7f69-9a28-3641-bc54-12e1d4bbe5c1 | -6.95183 | -42.89594 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| c792e655-8dd1-316c-a7f1-be37727ec2d1 | -7.20717 | -43.07379 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 08af54da-a1ed-3f49-a065-b9fa5588b708 | -7.20092 | -43.19176 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 65b0ccb9-17f4-3860-852d-de2fccffe0c5 | -6.27703 | -43.6798 | 2025-06-27 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 37cb10c1-c7b0-3916-a8ed-45fb7105aeac | -2.88978 | -51.47756 | 2025-06-27 04:46:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23761c3f-9f38-3d78-af46-defac3009002 | -6.95143 | -42.8988 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 2946a44d-544a-3b42-a093-8cbfb60f44e9 | -6.27229 | -43.67904 | 2025-06-27 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0017dffd-994f-3e33-91af-e955faf8b210 | -7.22071 | -43.08425 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 12af2f08-30c3-3f26-8ec7-48dc2dd95d51 | -6.95689 | -42.89668 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 14da6d59-ec0d-31a5-a479-769bdf9b3f55 | -7.20567 | -43.08207 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| daa5f8c9-5816-334b-af3c-8496d128d51b | -7.5474 | -45.83639 | 2025-06-27 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23653367-9f27-3af4-9de7-fea483ea0bfa | -7.19994 | -43.19477 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 44e0da3f-fb9d-38af-8d31-cc09d19dffc4 | -6.68841 | -43.07041 | 2025-06-27 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1092a5da-234d-3042-91d1-45e67202438e | -5.91791 | -43.47364 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cb0ae314-0d00-387d-b490-caa0f94b3b93 | -6.22226 | -43.36124 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 34227e71-a6f5-3355-8a55-ffbb9c44d45c | -6.47192 | -43.74688 | 2025-06-27 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e2bd12b-a75e-37c9-b995-a910616d8f42 | -6.95223 | -42.89303 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 7c176ee7-309c-3950-8a9d-c04393cab3b0 | -7.09774 | -49.17916 | 2025-06-27 04:46:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 039939ba-52cc-3aa1-80e6-0140a76eaaee | -7.2157 | -43.08349 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2e0f89d4-0d24-38a6-ae23-d5805602d5ec | -6.50063 | -49.32331 | 2025-06-27 04:46:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42520fd7-dd97-3aab-b7b0-1ae0e2824025 | -2.44292 | -47.46586 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c677cc2c-6141-355a-95f4-a5c5e9b0584e | -6.77108 | -46.33059 | 2025-06-27 04:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba30cec2-9636-349a-bed1-7238ba82d149 | -6.21261 | -43.3596 | 2025-06-27 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c043a26-8dc1-358b-bcdf-02f04f5e90c1 | -6.69495 | -43.05982 | 2025-06-27 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a66c432-b651-3577-af95-b52cf83b440a | -4.06322 | -57.71865 | 2025-06-27 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e26fc3f8-55af-35fd-a470-6efaa8510a8e | -2.55036 | -47.70124 | 2025-06-27 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 416e94ca-2185-34d5-b80f-f56cf7a2967d | -7.25795 | -46.95119 | 2025-06-27 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b328a151-fd67-3d60-a437-d04e32fe48f2 | -6.17987 | -48.08414 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4c233064-9bdc-382b-b3d4-e010b29120cb | -6.27773 | -43.68133 | 2025-06-27 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8de9b7f9-fa0a-3184-9fba-508e6df973f1 | -6.96236 | -42.89445 | 2025-06-27 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 3ef86492-275e-3500-bd71-fa51f59ea3c4 | -6.69521 | -43.05929 | 2025-06-27 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1feb75ad-ea82-3108-8962-3cb5339bf7df | -6.17271 | -48.083 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee8646a7-15ca-3c9a-bc96-6ef0dec7b332 | -3.02904 | -49.43377 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1eed84b2-4aa7-33f5-838a-916f5fb4e0d9 | -6.17926 | -48.08818 | 2025-06-27 04:46:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bd786d58-aa81-3870-853b-92d49668914e | -3.0285 | -49.43727 | 2025-06-27 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91c713b5-320a-3185-8196-82fc70ee75d9 | -3.88433 | -54.21429 | 2025-06-27 04:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
