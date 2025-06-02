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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dca87b28-baec-30de-adc5-242c806dda01 | -16.02837 | -43.67997 | 2025-06-02 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d8f4e8d-5f5d-3945-bfdc-7cafaeaee134 | -16.56599 | -43.92477 | 2025-06-02 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6344a98c-7e9b-3e24-9d01-ee6e37171aaf | -20.08636 | -50.97705 | 2025-06-02 03:51:00 | NOAA-21 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 086dd5ae-ce47-31bf-b3cd-c634a6eb20ff | -17.2568 | -42.66455 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fb87032a-fcc5-37b7-88cc-3a853836a7f2 | -17.28499 | -42.65177 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6ac80a33-6e96-3274-905e-097fca96cf54 | -17.27556 | -42.66345 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b334b310-3248-3d56-869f-850875d884e3 | -18.04162 | -39.92561 | 2025-06-02 03:51:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 101d3e52-5af7-3e91-9de4-21e15bf36f09 | -19.78326 | -42.09485 | 2025-06-02 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e5159d1f-65f5-31bf-989a-f676a44137a2 | -20.16071 | -41.66753 | 2025-06-02 03:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a246071-38a5-35a3-bd2c-bbccdd878ea0 | -17.25395 | -42.65956 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0357eb10-0074-329b-ab2f-9995f8010886 | -17.29578 | -42.65378 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0b6a5930-550d-326d-a6cc-f81dac4983a9 | -17.28425 | -42.65607 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4cb5add-7f41-3997-bdfb-f4accc24f32a | -21.91229 | -42.26403 | 2025-06-02 03:51:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 06ad8af4-8772-3945-bf9b-b8c6fb42b315 | -17.26984 | -42.65354 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b6fb80c1-9ae9-3eaa-ba9f-46b901320de1 | -16.68225 | -43.88621 | 2025-06-02 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 961672e9-e6d6-3a16-98e6-e8d9612b695d | -16.03143 | -43.67838 | 2025-06-02 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 353ac1ef-9ec7-37c0-84c6-93639d10dd07 | -17.29218 | -42.65309 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a3c50e2f-2de0-351f-b040-7467f79c3c23 | -17.69351 | -39.69548 | 2025-06-02 03:51:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 128e6f50-bbb0-38e3-a170-ca2cca63a21d | -21.25323 | -48.97562 | 2025-06-02 03:51:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 013b29e4-2b0d-375f-8f0f-2aed3dbe2d10 | -18.05656 | -39.91703 | 2025-06-02 03:51:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f9d46f2c-c6c4-3dc7-88ab-010c299e254e | -21.25419 | -48.97745 | 2025-06-02 03:51:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ba544467-1ecb-3e2a-b3fc-210ba8289ec6 | -20.76351 | -46.76794 | 2025-06-02 03:51:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7eda2d80-e3b2-34a1-a8e9-24ba2520e34a | -16.02755 | -43.67769 | 2025-06-02 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32feb201-24d9-3485-a766-a71f6d9146ec | -17.29503 | -42.65815 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f98e8cb5-e179-3370-8063-02e4259bbd68 | -18.69149 | -46.98639 | 2025-06-02 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6db1ce3f-421d-3579-982a-b81ea314613f | -22.53854 | -48.81438 | 2025-06-02 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9d13232-8f22-397d-8bd9-5e346314538c | -24.24304 | -50.7406 | 2025-06-02 03:53:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c0d9e10-4e21-35e8-95e6-448df8c67bfe | -23.33781 | -46.77198 | 2025-06-02 03:53:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4b5053c-fc8c-3c1d-83a5-8e6780821031 | -23.98476 | -48.91855 | 2025-06-02 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 167fd4b1-91ad-34fd-97be-365a5e027fc5 | -27.01349 | -51.27668 | 2025-06-02 03:53:00 | NOAA-21 | IOMERÊ | SANTA CATARINA | Brasil | 4207577 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 65eeea98-f1bd-3a79-a4b8-42ffb7235e66 | -23.42643 | -47.29658 | 2025-06-02 03:53:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c84deaf1-bcaf-3dec-b47d-85be44e25303 | -5.92018 | -45.52673 | 2025-06-02 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27be1cf1-5f74-3d67-9bfa-1ad965f3a478 | -5.18546 | -48.07881 | 2025-06-02 04:14:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 616b23e3-0ca5-3768-9ba9-fb79e34a2c97 | -4.78592 | -45.33302 | 2025-06-02 04:14:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 612883c4-9cbb-314c-a994-eb73f767d3db | -3.51306 | -40.35831 | 2025-06-02 04:14:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f48850bb-f391-36ca-b0a4-f54ce98d8a1b | -3.98639 | -48.41145 | 2025-06-02 04:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66612c3f-d132-3d00-8b5b-fc3452c8d4cd | -5.92369 | -45.52731 | 2025-06-02 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c5f2f84-1056-3531-9b8f-4f2fc1311c2c | -4.33214 | -40.18774 | 2025-06-02 04:14:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b49009f-aa8a-35a0-9cb5-efe287f6477a | -5.36719 | -37.33031 | 2025-06-02 04:14:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 912e3c63-373d-3e2a-b1f9-c3f4185cd987 | -5.91955 | -45.53061 | 2025-06-02 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12447d7b-8fc7-3ed4-b329-fcf1f2f7074d | -6.49466 | -42.85021 | 2025-06-02 04:14:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4a1a270-8933-3ae9-ad3f-400f9a379bf1 | -5.8309 | -44.09051 | 2025-06-02 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2394c309-2663-3c51-9960-d8e85b6ab2a8 | -5.76253 | -37.56598 | 2025-06-02 04:14:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 19164372-c097-33f0-8c9e-42c7330e642c | -5.92306 | -45.53119 | 2025-06-02 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2caa6c43-df39-3b09-99e3-a19805cf59a4 | -10.36153 | -47.97479 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab6d5c67-3980-383e-8d4f-a1320a969548 | -13.07967 | -45.2644 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bf943b0-3d3a-31a6-a5a1-9899720c8cf6 | -7.0689 | -44.92889 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5b19ac8-0b1b-33bf-8878-10281a388baf | -7.07673 | -44.94519 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee473753-b077-37e1-9817-3b8d7371585d | -7.95752 | -45.41939 | 2025-06-02 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76393779-08f0-3f0b-a669-0d771fe81b4d | -10.98362 | -44.62325 | 2025-06-02 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b0b3ca3-9271-358f-bd37-69deea3a5a1d | -8.03446 | -43.80731 | 2025-06-02 04:17:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1dc91388-165d-3326-8956-fca95facad14 | -13.0791 | -45.26797 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 008b80d6-fd2f-3c97-a1ac-f1df2fff75ef | -11.90937 | -54.83333 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e73c427-e51e-3711-a6d9-e179591fdbc2 | -7.00797 | -44.6103 | 2025-06-02 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a5ac406-89ba-323b-849a-6f8cbe53b13f | -9.32443 | -48.94922 | 2025-06-02 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dee6dd76-596c-39e0-b93a-1546b7b93edc | -11.91673 | -54.82856 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06a64d18-0546-3f63-99c6-37565d8e32d7 | -9.40156 | -48.42171 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7ad781d-edc7-3359-8216-a602cfa45a68 | -7.07009 | -44.92155 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8147c73-2a5c-3505-88c7-e5c1c8ed9079 | -10.82523 | -56.94295 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a6920ba-1dd3-3d49-a67a-376774b357b4 | -18.05442 | -39.91822 | 2025-06-02 04:17:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec57d0eb-c082-34d4-8c9f-56fa96c3727d | -18.0575 | -39.91681 | 2025-06-02 04:17:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86567d3b-44a1-3226-bc71-6231520f5c56 | -11.44415 | -55.00813 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44a5dd29-479b-3b8b-9be4-c7c56e6e87de | -11.91017 | -54.8292 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5863285-b5ed-3a84-851e-94e404bde866 | -19.96832 | -44.21742 | 2025-06-02 04:17:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 917e01e3-6da3-308d-80c2-9d630e5654c9 | -13.09692 | -45.26361 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03ba3910-504c-34c7-9044-05ff7663a82a | -17.25483 | -42.65942 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c32e8bb-598c-39fb-9a9a-fe8623305c44 | -7.56616 | -43.28293 | 2025-06-02 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52a15ddd-419a-3444-b6c9-de8030a5bee6 | -9.78532 | -36.99393 | 2025-06-02 04:17:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f48967ee-7258-354c-ac27-7dc1a4a71d94 | -6.73061 | -44.36417 | 2025-06-02 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b952cff2-3037-33bc-9e0e-060047c43f93 | -7.63224 | -46.11711 | 2025-06-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce1fdad4-99ee-32ee-8232-8e883beb66cf | -10.63335 | -42.69031 | 2025-06-02 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1304a5e-f613-345a-a990-196c9d8de3b6 | -9.37801 | -48.4177 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cbff8fd9-2b2e-303e-85e9-af3a33364836 | -13.10692 | -45.26529 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c307769-5b07-3bde-8cdd-ff622f914cbc | -7.06995 | -44.92142 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe632496-331f-3cff-8a44-d910f7269b52 | -9.16844 | -45.33575 | 2025-06-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e3848f5-245a-3d0e-9aef-7d7918ed9d97 | -11.45204 | -55.0076 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93523c4b-3967-3b31-97b8-0e939dfd2091 | -18.69101 | -46.98175 | 2025-06-02 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6cd8d6d9-f9cf-37f8-9f14-8a79397ac5d1 | -9.39538 | -48.41045 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dc8908e-d113-34c8-86bb-a302e4a0ca37 | -6.73003 | -44.36776 | 2025-06-02 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 405be5a2-fdcc-328a-b3f2-a5833fbaa1f9 | -17.25421 | -42.66368 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 347171e2-0fea-3fd3-bb1a-bd14c24652f8 | -9.40072 | -48.42672 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1de7c462-e11f-316b-90e0-8a4995ab9e07 | -11.45081 | -55.00513 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2146ad-9537-3c08-9fe1-16c2cc98940f | -7.0729 | -44.92575 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62e78102-667b-345a-b2ad-80fdc0e68641 | -7.01501 | -44.59254 | 2025-06-02 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52981906-944b-3f7e-b9de-cddff2e52834 | -7.38247 | -43.14001 | 2025-06-02 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 460aa79b-81a7-393b-9e00-9c32bde53dcb | -17.59647 | -43.20002 | 2025-06-02 04:17:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 839e3716-8455-30e2-b2d6-81db5e85d8e6 | -11.91755 | -54.82444 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1e82e71-b3b2-3741-a22a-64ef6e315194 | -9.16889 | -45.33548 | 2025-06-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9f3e717-1230-3b89-b6e5-8021592ed50b | -7.88383 | -46.22952 | 2025-06-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ca11edb-af58-3333-8f31-f6d74be19277 | -11.45124 | -55.01175 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49d4ff57-fe0d-3e48-ad4b-fb752b91ee8b | -9.40409 | -48.42451 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c58cf7b-b575-36e0-9010-d39b373aeddb | -10.835 | -56.9629 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b639a305-c5f0-3b3a-a542-f3f3c6defcf6 | -6.73254 | -42.9087 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b290ce8e-89c5-35c8-b540-ce0a2db7a8aa | -9.34497 | -38.2674 | 2025-06-02 04:17:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f3554bcf-2480-341f-9296-98b0b477c527 | -7.0735 | -44.92209 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6853bb0c-0e3a-3d65-af9b-0db5969323b0 | -7.2948 | -49.62444 | 2025-06-02 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78906996-60ac-39b0-b4bd-b81ad00c5b17 | -7.08418 | -46.55328 | 2025-06-02 04:17:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0311e683-bd33-39df-8a55-fd785db78c41 | -13.09244 | -45.2702 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833ccc19-5573-3596-9f62-865d0b9ae167 | -11.44621 | -55.00645 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f462bcb-388e-34f6-8aba-04d48931c8a5 | -17.25499 | -42.6663 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README4.md)
