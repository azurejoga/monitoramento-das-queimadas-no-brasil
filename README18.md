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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bcb2e0b-399d-306e-9b57-e27f4b2e17c8 | -4.5057 | -42.5325 | 2026-08-14 04:30:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 88313420-af67-3278-9858-00f0cc2c3ae9 | -4.40695 | -42.14359 | 2026-08-14 04:32:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 13ea2092-b0a5-3af2-b648-7c1c1c8b4a23 | -6.4085 | -39.2631 | 2026-08-14 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bd65bc9a-cea4-31c4-ba95-80d0b95b6127 | -4.49521 | -42.54808 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 27099393-a28b-30ad-9781-c360da74ead4 | -6.60663 | -56.34754 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c22b1ec7-e5e6-3441-8517-e24186bc01ca | -6.7788 | -58.75393 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f75ceeb0-4828-37a0-9aa1-91c9c0e0180c | -6.60235 | -56.33957 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df3b4f65-0e8a-3036-90bc-54f875cc5ee9 | -6.85799 | -42.90448 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6c61709-166d-3b53-bfc4-e94351616516 | -8.01851 | -55.1195 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 916577d6-0ed8-3238-b4d2-d798e7c6f49c | -4.21487 | -46.43461 | 2026-08-14 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29d9cbae-1545-36b6-b247-1ccea11d35d2 | -4.10784 | -50.44641 | 2026-08-14 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 505df577-8482-39f1-bd9e-7bf82c3d0a3d | -3.26445 | -49.52439 | 2026-08-14 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5354f09c-e74a-37e9-884f-de1abd91ab3f | -6.85601 | -42.92851 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94126ab1-ef2b-3af7-b433-e7ff2c1c73bd | -4.10395 | -50.44575 | 2026-08-14 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 66f6924d-4421-3f18-a804-09e9cd4eda13 | -9.48256 | -51.62175 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 616089d8-9de0-32e1-a811-ed5cd75ab467 | -6.78948 | -58.76583 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8abf189-348d-31a8-b0e9-ab12c6c6ef22 | -9.48418 | -51.61945 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d769e3e-781c-38b1-a3c9-643b3230f528 | -4.48654 | -42.55555 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fbb6559a-65e8-3d46-ae18-984e2f645eec | -6.24276 | -55.62038 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3b71ccb-e8c8-33fc-bf12-f679cd0ef218 | -3.56637 | -50.29174 | 2026-08-14 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c472fe4-0a95-3a0f-bf67-409d6e4e0b70 | -6.61605 | -59.05431 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 79966772-7694-3c4c-b0d2-aed2c5ced2b7 | -6.99571 | -44.82623 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 432735ab-2be5-3633-b6a4-359494a378b1 | -6.40782 | -39.26801 | 2026-08-14 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c08176d1-ea34-3877-a48d-d637a6f87f22 | -4.49888 | -42.54865 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e3feda25-7ba7-3af4-b16a-e2b8f82268df | -6.93304 | -52.78881 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71bff31f-d600-3463-9261-2313f8b3f0b5 | -6.18565 | -47.3301 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c64d5dc6-4e0b-3913-b213-5b95dde76f17 | -7.6112 | -46.46488 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc8a51a4-0ec5-3288-82d2-158fb1718a31 | -8.23593 | -49.96046 | 2026-08-14 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b7e26c4-bb21-31c2-9d35-45c179d88e1c | -6.61818 | -59.0427 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21e31276-a224-3e8f-a7db-d6045fcd8464 | -6.83114 | -56.42478 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae826375-122c-3113-a568-956614873a5d | -6.60103 | -56.34682 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf29ff3-4119-3674-a58c-d4a23b28dd27 | -6.18509 | -47.3336 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3de3ed7-0412-3d8c-b769-dfa6d06473fd | -2.79218 | -49.52114 | 2026-08-14 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f994df5e-7570-3c5b-a2cc-496b33799149 | -8.5213 | -45.33437 | 2026-08-14 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fabee1fe-0e8a-3311-afb0-f51cb7c8750b | -7.02846 | -41.44537 | 2026-08-14 04:32:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 708da898-b2fe-3358-89cb-06832de3baca | -6.26825 | -43.27956 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e21816b6-ee26-39b2-bed5-cc910a51af7f | -6.19175 | -47.33466 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 17c40318-0d72-31bf-a6aa-931e52089bf6 | -6.88458 | -41.95564 | 2026-08-14 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a492ec1-0f1f-3846-a06e-07c44b42cb50 | -4.19602 | -46.80907 | 2026-08-14 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e87d663-3e6d-3887-ab37-62bcd89f80b4 | -6.41011 | -39.26576 | 2026-08-14 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 32a15397-4cde-3fc3-8c7d-e687a61d946a | -10.36057 | -48.2762 | 2026-08-14 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a42fd17d-e49a-3d00-8d88-51bc236e9616 | -6.2481 | -55.62125 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ac8f2cd-392f-3bac-9a00-da7c0f1f7ca8 | -10.74594 | -47.92638 | 2026-08-14 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef8fe1df-3233-3d72-806e-0aa9d488c32c | -5.22014 | -49.33994 | 2026-08-14 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 713bf459-0966-39f9-ac69-f038ec0d4f50 | -1.77722 | -55.53281 | 2026-08-14 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca2ebce7-a5f4-3f62-ad26-b94d233b9eb7 | -6.59375 | -56.36323 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6f1e463-5254-324c-97d3-d546ad481ded | -3.05366 | -48.74194 | 2026-08-14 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b339599-e850-32ba-ac01-66c9cba781bc | -4.49654 | -42.53945 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 7b56202d-651b-3fdd-a47c-1b9f86e89c9a | -6.63339 | -56.26315 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e73fdd40-0f88-3bfa-b141-f8b669cdfb5a | -9.48936 | -51.6355 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfc31d7a-e37b-3220-9b74-435029228210 | -3.47186 | -47.68933 | 2026-08-14 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ca26597-bd4c-31be-865a-d82ea0ff5128 | -5.66428 | -48.12355 | 2026-08-14 04:32:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89eaef66-1b77-3d5b-b05b-5a9c8a2c9067 | -6.59437 | -56.35965 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45037e0f-7064-3522-be1c-b4b2983e233f | -6.60429 | -56.32896 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4941faa4-10a3-3e39-ba9d-a3fd8db258c1 | -3.84572 | -49.03638 | 2026-08-14 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f37b3462-7024-388a-b5f2-7bb04b61e7a8 | -6.59946 | -56.3306 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f263b188-05bb-3531-9e9a-e5f4d7c8c5c7 | -6.61241 | -59.00036 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ec44677-2765-3611-8ece-b89c56ba62de | -2.79386 | -49.58185 | 2026-08-14 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 86a2d346-58af-337a-9fe0-dd3d45da0886 | -6.61058 | -59.0471 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10a7b9ab-d180-3b34-b2ae-59e0ed9a6b59 | -7.70571 | -46.23061 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f2d98a1-15e6-3af4-8e8c-686749607fbb | -4.64382 | -50.92646 | 2026-08-14 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9493677b-b6a4-329c-bed0-8250003deb54 | -4.49021 | -42.55611 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b5c075c4-90d1-336d-bf5a-3f2b12af112c | -4.49388 | -42.55669 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c566bcf3-f448-3e4a-af9b-e8b4d3987a84 | -6.59278 | -56.36055 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09a86fcd-c681-3987-8106-410632f4cca8 | -6.60252 | -56.34586 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3adafa90-8ff0-3c12-8a70-db7d92d65299 | -6.60118 | -56.35351 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd02562c-2254-3d90-a517-31ce497da973 | -9.4949 | -51.62654 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b5d5cfd-d99a-39a6-8608-adadc8b9f7f2 | -6.7002 | -58.95888 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13b241cb-8218-3be5-a371-cea1d3cfa1ee | -6.60315 | -56.34225 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee71c57-066b-3ef7-b2e9-9c2f0a7344ad | -7.37797 | -59.97399 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcb7126e-ce3d-3023-bc7c-75fff1a6ff1f | -6.26526 | -43.27484 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ee5d782-854a-3fe7-9060-0f3b288c31b7 | -6.97549 | -41.46738 | 2026-08-14 04:32:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89e62c58-61fa-3da4-9caa-e7ad60c39820 | -5.73219 | -44.50365 | 2026-08-14 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 664ef48f-5795-31a7-8e47-53e89188324c | -3.84865 | -49.04112 | 2026-08-14 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9254de5d-62db-3d58-bcc8-a843ee8c24e5 | -9.05541 | -50.62806 | 2026-08-14 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86eccddc-7c74-3a74-adc3-8bc128ad1bb5 | -4.49154 | -42.54751 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e37fe9a6-5b06-37cd-8ce7-4ee0475775b5 | -7.60779 | -46.4643 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9e33a37-7ee2-3839-a200-1d7618af755a | -4.57771 | -45.66603 | 2026-08-14 04:32:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 510b854b-3923-3869-82c1-20bea2eaab84 | -4.42405 | -48.75692 | 2026-08-14 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a17b3a2-ff8b-3655-b06a-82258e6c745e | -9.48806 | -51.62007 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb9bcd16-6196-34a9-a249-1897af6d6df3 | -6.78595 | -58.74874 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb321d19-11b8-3e05-b919-3c82817d3087 | -6.60793 | -56.3404 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a50c5cc2-4b8a-34ea-91ff-aace9f3711ae | -6.1141 | -44.02962 | 2026-08-14 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70e9d08a-c41e-3887-82c8-79296227b3cd | -9.12296 | -46.39718 | 2026-08-14 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d27f28d8-5c33-3a40-9996-1d0c593e9a3f | -6.61676 | -59.04211 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1eb8b148-9401-3383-967b-459c9e787baf | -3.84504 | -49.04053 | 2026-08-14 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecddd9a5-9416-36d3-ae1b-dc44e492695f | -6.18898 | -47.33062 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f29376f3-e8f3-3f80-ab05-0110f647b9ab | -6.18396 | -47.34062 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5634ba9c-8737-3328-b708-f9f74f3e1b7d | -4.19213 | -46.81204 | 2026-08-14 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b92e1e2-9438-304a-91ce-31523a048081 | -7.71179 | -46.23514 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b44f6e43-81b6-3bdd-9d63-17a60924cc7b | -6.60875 | -56.34295 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6244983e-0d5d-3710-8b2d-b489b8c9934a | -6.61567 | -59.04781 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1302fcd1-6214-3eaa-a61b-e7b3d5d64acb | -7.70516 | -46.23409 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9984838c-5105-381b-b258-853a054bdd94 | -6.62472 | -59.04408 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dde89be6-0434-3358-a5a3-990bd695385f | -7.7151 | -46.23566 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2134a4c-e398-333d-bb87-36ec4ba7b2db | -6.70231 | -58.94753 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fdbefc1-a47d-3b75-87ef-7917d1ff913f | -8.55088 | -54.6 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1019c40c-0386-36a8-870f-547804b918bb | -8.01903 | -55.11666 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5673420-da36-395f-ba56-7618aeea9377 | -10.18231 | -48.73996 | 2026-08-14 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f39eec1-86f5-3572-8558-57690a679c80 | -9.12683 | -46.3942 | 2026-08-14 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
