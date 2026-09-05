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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2261848-abac-347d-8a6a-c12251187378 | -12.92659 | -42.43291 | 2026-09-05 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 59b8e1a0-b139-3a2b-b23f-0d10ed82c186 | -10.15215 | -36.19025 | 2026-09-05 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 76c62a67-94ba-3795-b519-2a7b854748a7 | -12.77962 | -40.82726 | 2026-09-05 04:02:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 91785126-983f-3b23-8f2f-8df3423689dd | -12.43943 | -43.27407 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e22574a6-d685-32ee-a8e2-f7e3a4b259e9 | -12.1058 | -41.61946 | 2026-09-05 04:02:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c323edad-21a9-38b6-8d6e-0b4eb1577ab8 | -12.43881 | -43.27762 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0d2c40b-3fcf-3ab2-afa0-74021bdf5a29 | -15.32573 | -43.65763 | 2026-09-05 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a06db290-d314-387a-a7c4-33948b274fb0 | -11.86462 | -42.5464 | 2026-09-05 04:02:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f0c659d-3b56-3c43-a41f-b495a5f2e72d | -14.74009 | -47.14848 | 2026-09-05 04:02:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 647b9c56-0980-3cd6-bb5e-c2cc4d966cfe | -9.61642 | -48.56394 | 2026-09-05 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1012f94c-a2db-328b-a966-1e89a3373d2e | -14.91463 | -44.67236 | 2026-09-05 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 66b4da69-f0f3-359b-8272-e6f9a80db5f3 | -9.78439 | -42.00233 | 2026-09-05 04:02:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 43f95722-64ba-3322-84f5-814324f40143 | -9.61044 | -48.56287 | 2026-09-05 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f245278b-e8f6-32f6-ae5a-196d22da7995 | -10.14876 | -36.18972 | 2026-09-05 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 87a6d863-67ed-30f9-875a-7f41ab5db21b | -20.14809 | -46.31849 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9219b73a-1bdb-3f7a-bc82-23306d6ab534 | -20.17488 | -47.39107 | 2026-09-05 04:04:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c8b66eb-e912-3906-961f-b6f98ffabe13 | -20.66033 | -43.52926 | 2026-09-05 04:04:00 | NPP-375D | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff1107a2-cc03-3189-86ae-292821559048 | -21.51796 | -50.03643 | 2026-09-05 04:04:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9aef1eb8-353a-32fe-9475-de41e344c8fc | -20.9887 | -45.80675 | 2026-09-05 04:04:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7eb65810-f49c-34f7-a4a3-b3bf27aae3cb | -21.2417 | -46.84777 | 2026-09-05 04:04:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| acc85581-9ed3-3abd-961d-cfade2531338 | -21.45547 | -45.76984 | 2026-09-05 04:04:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79deeaef-020f-392e-a4a5-90317590e9ec | -17.24126 | -39.62216 | 2026-09-05 04:04:00 | NPP-375D | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 174fad62-1c72-3031-891d-3b89844c1d4c | -21.0478 | -46.97779 | 2026-09-05 04:04:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a2d40b6-9ab2-3969-9f3f-79153fbfec2b | -20.14223 | -46.32594 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc30f03-1ace-3950-ba05-cba8ed1304e7 | -19.25465 | -46.86443 | 2026-09-05 04:04:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c0f7db1-0d7b-3fe1-88a6-3a961055dd79 | -19.75222 | -46.67775 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3698edc6-c520-34fd-aea9-73ba9ac1d9b0 | -20.2956 | -46.31304 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29cd78f5-af01-35a7-871e-34a993a42f18 | -19.75268 | -46.67992 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 843e8e3e-30be-302e-a5d6-0ac0b4acb3f9 | -19.7476 | -46.70071 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f78d9ea7-8cfe-3104-987f-b4c54837c10a | -20.14499 | -41.81937 | 2026-09-05 04:04:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1a67aeed-6624-33c2-941e-3cd1286eb2ae | -17.30132 | -43.34596 | 2026-09-05 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48316784-800a-3219-93ba-2e39614d4291 | -21.51815 | -45.77049 | 2026-09-05 04:04:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 963a2062-0219-3f1b-89d6-ae18ea60f968 | -20.25739 | -46.33664 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 490d60af-2452-386d-b363-fa0075e8383f | -19.75712 | -46.68061 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d50b3a5-38f7-3cb9-9868-d93080f14b93 | -21.10718 | -46.27835 | 2026-09-05 04:04:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b98794f-ada6-3df9-904a-0a09498666ea | -21.53647 | -43.19324 | 2026-09-05 04:04:00 | NPP-375D | GOIANÁ | MINAS GERAIS | Brasil | 3127388 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4212ce20-8cfe-33e7-b38d-76fc595e91fd | -17.7901 | -39.70482 | 2026-09-05 04:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 69b8fb91-7c03-3ee2-a7d1-0135d3bee21a | -20.14142 | -46.33017 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2832480f-9933-3556-a6f1-65db4d796ca3 | -21.45556 | -45.76917 | 2026-09-05 04:04:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ae2e57aa-932e-3697-bb34-97d21d2b445d | -19.71486 | -40.07016 | 2026-09-05 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4f396fef-31fc-33db-8edf-0f1ff6de7555 | -18.06556 | -49.04898 | 2026-09-05 04:04:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55ca9619-1ca2-3add-8204-08821da22516 | -18.58542 | -46.42337 | 2026-09-05 04:04:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f8a5eaf-6e62-3ba3-9bf7-04a0dbc72cfe | -19.48206 | -40.2792 | 2026-09-05 04:04:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03c28835-8a97-338c-856e-b8c1ea461d71 | -19.7491 | -46.69846 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa1769f-7f10-3a08-89f3-65689c1df615 | -20.60506 | -46.37565 | 2026-09-05 04:04:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6608b19-926c-3cfb-a720-46c75e0277a8 | -16.77096 | -50.61689 | 2026-09-05 04:04:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de145a93-0741-34a4-95d8-4d751b3ad3aa | -19.74941 | -46.69169 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03acb51e-c8b9-31e5-91e6-7ff67b06047e | -21.55054 | -44.05467 | 2026-09-05 04:04:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6cb995d-b498-3498-99b6-ef9368e2fc6f | -21.51872 | -50.03294 | 2026-09-05 04:04:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 100d7661-b78b-3ae6-92ae-7ca6ad05b8cc | -21.24813 | -50.00443 | 2026-09-05 04:04:00 | NPP-375D | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f383ba7f-dcd4-3ae0-ae28-a912dc2f95dd | -21.24608 | -50.00744 | 2026-09-05 04:04:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f0c2ff7c-bde7-356d-b290-8997db5bfc57 | -19.75035 | -46.68706 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b63b287c-c084-3371-b675-50690848257b | -20.34258 | -47.59821 | 2026-09-05 04:04:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc21e850-5cc2-3f51-b8ac-e9be2697b9de | -21.2474 | -50.00785 | 2026-09-05 04:04:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 92c5354e-9b32-37e0-8fb7-7704813e30c4 | -21.39281 | -45.50911 | 2026-09-05 04:04:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ce1438a0-6b37-3654-a4e8-03f921bdf97b | -20.60184 | -46.36953 | 2026-09-05 04:04:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7e95bfa-d090-37c7-9cd4-101e60257043 | -21.38883 | -45.5083 | 2026-09-05 04:04:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5abc28ea-0438-35ea-a900-4ebb804c46a2 | -19.7485 | -46.69627 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07535b3d-8202-3766-8c99-3e377b1c172d | -20.15013 | -46.31797 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8418d65c-4a9c-35e7-8df0-afdf6c93884e | -19.75087 | -46.68927 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 176a1dd9-9558-32ee-a768-317887bade0b | -16.77504 | -50.61542 | 2026-09-05 04:04:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5753df9-2679-376d-aec0-a81d915d3fb0 | -17.29762 | -43.34501 | 2026-09-05 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a25193f0-d89e-31c3-a959-9a9f4fc1689f | -19.83454 | -42.70333 | 2026-09-05 04:04:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fda21739-2417-32d6-abd9-bfc76df213bf | -17.79343 | -39.7054 | 2026-09-05 04:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a7fab9bc-5a1b-35b0-9b71-557a92b47349 | -20.98334 | -45.06205 | 2026-09-05 04:04:00 | NPP-375D | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20bad372-1d5e-3719-ab82-22efa5763cc9 | -19.23409 | -46.73277 | 2026-09-05 04:04:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| abd307d1-edac-371a-a5c3-4d294c35da35 | -19.25818 | -46.87024 | 2026-09-05 04:04:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65b4ca59-a93a-361c-90db-45a43f20687c | -21.51948 | -50.02945 | 2026-09-05 04:04:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| be00fd98-af1a-30c8-8871-17a580d1dd0c | -19.74554 | -46.69321 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31b9a98f-5eed-3f82-8cfa-2fab4e3b687b | -21.55421 | -44.05534 | 2026-09-05 04:04:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7af6a31c-72b7-3ef6-8cb2-4f99624471ab | -17.21074 | -53.82912 | 2026-09-05 04:04:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b0e0261-b4a6-3df2-9a4f-26ea7c676cc4 | -20.74088 | -47.14738 | 2026-09-05 04:04:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf812e0f-6c80-3f39-a9bb-ed0a25c0e52d | -20.34142 | -47.594 | 2026-09-05 04:04:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d44f32e-11bb-3369-8ab6-1333bad50ae8 | -17.76271 | -42.42516 | 2026-09-05 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3dc46f48-780c-3b2e-951f-7568b35d55c8 | -21.39192 | -45.50764 | 2026-09-05 04:04:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 480ac72a-5dd2-37bb-be85-231379fbde1d | -20.60597 | -46.37101 | 2026-09-05 04:04:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8619341b-9434-30a3-8aac-11094b057c28 | -21.24759 | -50.00059 | 2026-09-05 04:04:00 | NPP-375D | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e1e5be8-98d0-3512-99a1-461f56fbefd9 | -21.5801 | -48.65415 | 2026-09-05 04:04:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22e127b8-f711-3abb-8123-70ed611cc1ca | -18.13014 | -42.78499 | 2026-09-05 04:04:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 01574d66-02e2-3130-8baa-c87161605f9f | -18.89779 | -47.0484 | 2026-09-05 04:04:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc33c26c-e7e8-3c2f-903e-ff537c23eeac | -20.14588 | -46.317 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bac5548a-e972-3585-bf3c-461f2fe04bc6 | -21.24043 | -46.84947 | 2026-09-05 04:04:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 910783ad-43a6-317f-b823-07a14bb23a71 | -21.24683 | -50.00402 | 2026-09-05 04:04:00 | NPP-375D | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3498f961-406d-318c-bb3e-1c5a30eedf0a | -21.38794 | -45.50684 | 2026-09-05 04:04:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf98118f-288c-3255-b161-9e2ab976dc4a | -19.75952 | -46.61862 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac5ee36b-919a-3896-acba-f577960dbb55 | -16.77197 | -50.61234 | 2026-09-05 04:04:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83e2c110-379d-32bb-8a69-0069eebef382 | -18.17008 | -42.94144 | 2026-09-05 04:04:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fcf8306f-bda0-329c-bac2-bdd992b8868d | -20.82592 | -46.3147 | 2026-09-05 04:04:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c3c8880-6cd6-3a97-9f46-88f606265244 | -19.74824 | -46.70292 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f870435-dc8e-3e87-ac9d-65bcb6e9c5b1 | -20.98942 | -45.80291 | 2026-09-05 04:04:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 041cbb70-e04b-36c1-aaa1-234c99800de0 | -19.75958 | -46.62061 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2089f82c-52ed-3e4c-8027-b1d342695246 | -19.25911 | -46.86551 | 2026-09-05 04:04:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ba965ae-aa59-323c-81df-3aa8ead9791d | -20.17029 | -47.39024 | 2026-09-05 04:04:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0af538f9-031d-3f6d-8280-1e18d3702e0c | -20.48158 | -47.53562 | 2026-09-05 04:04:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d73c518-77d2-3d0a-96cd-dc9afed1346a | -16.76912 | -50.61395 | 2026-09-05 04:04:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f05bdeb1-567f-389d-81d9-4593ab3fbc94 | -20.25585 | -46.33488 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aaf7d79-ad0f-3b67-8d58-58ec118bc31f | -19.46088 | -40.28296 | 2026-09-05 04:04:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 547f60d8-5bab-3833-b958-526303ec68cf | -20.25501 | -46.33909 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb435f6e-9542-34e9-8c3f-3468df0c83da | -19.74998 | -46.69391 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecf055e8-de5a-38d0-b38b-c784d92952a0 | -19.75574 | -46.68301 | 2026-09-05 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
