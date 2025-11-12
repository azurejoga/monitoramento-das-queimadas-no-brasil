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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 565d5fc9-edc4-36c6-b5c2-d3197347b56d | -10.53356 | -47.99041 | 2025-11-12 04:33:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 612ae9b5-c35b-3022-a43f-40089d55c0cd | -14.34301 | -43.54464 | 2025-11-12 04:33:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb038654-126d-39ce-836e-a75b3fceb04e | -17.62489 | -46.70373 | 2025-11-12 04:33:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 524bf8e1-efb6-3708-95d4-4d1a319b0667 | -17.12984 | -44.65437 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7ff8f15-6e4e-3a02-8d9e-37a700ef9e02 | -16.83263 | -46.08266 | 2025-11-12 04:33:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67401861-d0da-3726-b90a-1001c71474d4 | -11.54052 | -49.80885 | 2025-11-12 04:33:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3f03cd5a-babf-3876-8776-454f71766f62 | -11.05456 | -45.39664 | 2025-11-12 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 966918b5-7b87-3f37-9cb3-cc605b736a83 | -13.91935 | -43.29264 | 2025-11-12 04:33:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6812533c-4cc0-3f84-b364-d660ba2c65de | -11.51544 | -45.00061 | 2025-11-12 04:33:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe111edb-57f1-350f-8142-ef7a3397d26a | -10.50328 | -44.94299 | 2025-11-12 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6ffa34d6-8682-3257-a19e-38e9e2fba592 | -17.15047 | -44.65712 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 238e2260-257e-332e-ba79-0698caff907d | -11.06028 | -45.35777 | 2025-11-12 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fc11f3e-a42f-37da-9abc-3572427aa847 | -17.14369 | -44.6444 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc845db-f448-3e04-b241-1756455d0c47 | -11.84426 | -57.84922 | 2025-11-12 04:33:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83d86267-0d9a-35ee-8803-24be70b780d2 | -18.22383 | -44.19785 | 2025-11-12 04:33:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 80140878-3862-396b-a9a5-7db173471eb5 | -15.84935 | -43.34625 | 2025-11-12 04:33:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94bf32ec-d1ed-37fc-a2ee-066c9bf5485f | -16.28938 | -52.93447 | 2025-11-12 04:33:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47757eb0-c35f-3c3b-996b-e0a09ff528af | -14.40876 | -44.37998 | 2025-11-12 04:33:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6388d286-a900-37d1-a4ef-33a90d5781c0 | -15.45301 | -43.08121 | 2025-11-12 04:33:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c5ba0d54-e3d7-317f-98b8-b163c23ef023 | -16.41796 | -53.15807 | 2025-11-12 04:33:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e0bbae0-c4b7-360c-87a6-4222b2dace59 | -16.45416 | -45.01109 | 2025-11-12 04:33:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c82622-2ac3-35ed-bbf9-469c9afb8a97 | -14.25979 | -51.11967 | 2025-11-12 04:33:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82574f6f-a6d8-30b3-bde3-2d22f6664478 | -17.67676 | -46.76209 | 2025-11-12 04:33:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b79b29d-7780-3cd1-982d-1cd29d5e009d | -16.22081 | -45.66386 | 2025-11-12 04:33:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6ad0dca-e1c5-36a4-9e37-fac2f3838eb3 | -12.95466 | -51.61197 | 2025-11-12 04:33:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f19d7b6-d109-30e4-90db-143014ad1ba1 | -13.04219 | -43.37314 | 2025-11-12 04:33:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0780c31d-5c16-3e8c-8a04-705ce7860cde | -15.51426 | -43.01234 | 2025-11-12 04:33:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 307759c2-bdcf-311d-b5a6-cc01927fe440 | -12.00934 | -46.76896 | 2025-11-12 04:33:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7a6a8d8-2ac0-359c-893c-751d346d26b4 | -17.21401 | -47.65583 | 2025-11-12 04:33:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f9333a2-3068-368e-84b3-1a70e35d779a | -13.62513 | -44.12785 | 2025-11-12 04:33:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a015f798-b0f9-31b7-8419-0cf5f861b92c | -16.83639 | -46.08321 | 2025-11-12 04:33:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a765a06c-9ab6-33ad-9a92-e29f16f5e867 | -10.50706 | -45.07471 | 2025-11-12 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4581001e-25a9-3468-af0f-e93ed8e57a7c | -18.22814 | -44.19839 | 2025-11-12 04:33:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 327577ff-836d-38af-a249-ce54bca595b8 | -17.62856 | -46.70428 | 2025-11-12 04:33:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 488439fd-55bf-3c9a-9fc2-edae15b0ce1d | -10.50391 | -44.93855 | 2025-11-12 04:33:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fac3e2d2-94ee-3ce4-9a38-cfc825073fd8 | -17.31063 | -44.92822 | 2025-11-12 04:33:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f679b6b9-b137-3987-9728-d6bcb8c9afbf | -16.45109 | -45.00343 | 2025-11-12 04:33:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 592fe955-8575-311f-bb0a-7c0bcb8d9506 | -16.89038 | -51.6497 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cdf18d4-9024-3fbf-a34e-4aa50c060f49 | -10.55725 | -44.83147 | 2025-11-12 04:33:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 834b46c1-4307-31cc-abbf-6e881480371c | -15.29786 | -42.93418 | 2025-11-12 04:33:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ac5bfea-4fd2-3d7d-a613-f7d47482958e | -15.51874 | -43.01297 | 2025-11-12 04:33:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2a79edf-7303-385b-a957-fe01d364f47a | -16.48861 | -52.48323 | 2025-11-12 04:33:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cebb668-831f-3497-8f97-b930c4e964b1 | -17.14635 | -44.65656 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b8887de-8e3d-3179-903a-3e3e40ee1afc | -11.04664 | -45.39993 | 2025-11-12 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| edf1ea90-38e3-3bc8-8414-fad401e642c4 | -17.21051 | -47.6553 | 2025-11-12 04:33:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b69124fd-5498-33b5-8fee-ff0c4cdb1dd3 | -17.24182 | -48.11351 | 2025-11-12 04:33:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb8450f-8f46-3296-888e-7305571465f0 | -10.53024 | -47.98988 | 2025-11-12 04:33:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa5cfeca-30ba-3e36-a0da-de188a51ef75 | -11.5372 | -49.8083 | 2025-11-12 04:33:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79091537-a292-3baf-8bb3-aa269623a2fa | -14.8207 | -52.97555 | 2025-11-12 04:33:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 806e0836-9181-3539-a6a5-ee41379cf3c9 | -13.33458 | -43.17697 | 2025-11-12 04:33:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61481fba-7a92-3d20-b131-ac31b90ea1c3 | -12.01279 | -46.76948 | 2025-11-12 04:33:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7cc10de-c70c-3115-8047-4347370e2c4a | -13.16509 | -42.95913 | 2025-11-12 04:33:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45c6aeec-387e-3644-b288-db851e44f4c9 | -16.88027 | -51.64798 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 298cea6a-9a56-3a48-b429-04f285f68fee | -16.48795 | -52.48719 | 2025-11-12 04:33:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 928f2507-23b8-3777-b11b-d9039a5db047 | -16.89375 | -51.65028 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba62bbd0-a083-3db9-b655-3e2304b7a21a | -17.12572 | -44.65379 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85e7a022-c43c-3804-aeda-7f58e0a27ccb | -16.87965 | -51.65175 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41cac185-b675-30ff-b769-1f764a474c6a | -16.28513 | -52.93801 | 2025-11-12 04:33:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36622764-7d0d-3549-b570-d22b922428c0 | -15.59809 | -46.27801 | 2025-11-12 04:33:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6399d92-8030-3445-88d1-0c6339b7f173 | -14.40471 | -44.37949 | 2025-11-12 04:33:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c15b0f6c-71f0-3fe0-97d1-e85006c682ef | -16.88302 | -51.65232 | 2025-11-12 04:33:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6116cd31-62fc-38d8-9c05-127fcdcccef4 | -13.46926 | -43.07005 | 2025-11-12 04:33:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b22b7403-ccd4-3a92-95c6-d36152fa6d68 | -10.65684 | -44.73211 | 2025-11-12 04:33:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1622c39-7d4c-32be-afc9-c1f880219ed8 | -12.81193 | -46.42882 | 2025-11-12 04:33:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e5e9ebc-3d0e-393a-a418-3715681476f9 | -10.55351 | -44.83092 | 2025-11-12 04:33:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6b485ca-b2bd-3f8e-88ac-d9540d161cf8 | -14.16076 | -50.00202 | 2025-11-12 04:33:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc099be0-7157-3981-a120-03f7daf389a5 | -12.65732 | -43.25379 | 2025-11-12 04:33:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 543791eb-8204-383c-be67-bab0e03d841f | -17.13033 | -44.65052 | 2025-11-12 04:33:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aacf7ba-5548-3cfe-87f8-f2c2d2ab2f8e | -16.29058 | -43.82883 | 2025-11-12 04:33:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01bf165f-4d8c-3f0c-b642-977af36bc31d | -13.54124 | -43.63972 | 2025-11-12 04:33:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3370a8aa-f8f8-352d-8b09-af79ca35b097 | -11.04727 | -45.39562 | 2025-11-12 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 69fdb8b5-677e-3d47-93c5-3cc380513f0a | -19.79793 | -57.97761 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fb877e80-9a8c-31e2-9b45-d0226e5b1c4c | -20.89414 | -50.09886 | 2025-11-12 04:36:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3e10f763-1c6e-3cf0-9f5b-fd43b6537860 | -19.81042 | -57.9853 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 636d3438-6137-3759-9b4d-eea760eb4d62 | -18.08457 | -54.02434 | 2025-11-12 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6d8ac14-7db3-3cb5-84ed-d12ad07bb75a | -22.47696 | -49.13908 | 2025-11-12 04:36:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bb78fb8-08ef-3ff8-adbf-234e1746211b | -19.78898 | -57.97566 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e20089f3-8ea0-3ca7-8a9a-1a5748774382 | -22.36872 | -47.05798 | 2025-11-12 04:36:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2184f468-0c46-3abc-959a-d40d52b30d0d | -20.89748 | -50.09943 | 2025-11-12 04:36:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 13f990a5-ee83-30f3-b0b0-c026c80f023f | -18.15944 | -54.55852 | 2025-11-12 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d94a16d-0d44-388f-8584-a3854e647821 | -19.72342 | -58.03852 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d2f65e27-f085-3642-bea3-8c806329f001 | -21.5229 | -42.27023 | 2025-11-12 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bcc400f9-cc53-3821-8ae4-d0cfe8d76b53 | -20.03546 | -46.16202 | 2025-11-12 04:36:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c91a9394-69a5-3f22-8726-0444fb4bb15d | -18.4789 | -53.39835 | 2025-11-12 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be877dcf-9757-3290-b3fc-66a75a5bbfc7 | -21.81059 | -56.30014 | 2025-11-12 04:36:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a58a37ea-404e-3b5c-b23c-202f3347d384 | -17.56301 | -54.01343 | 2025-11-12 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fbb7bbd-d8a1-3614-9bf9-b822b4e3782b | -20.5132 | -47.26525 | 2025-11-12 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c191620a-f63d-32c3-8d28-44bfa0b804b5 | -20.22957 | -50.90692 | 2025-11-12 04:36:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f867990b-ab85-3a58-ac27-ac550a7d2a95 | -20.89024 | -50.10204 | 2025-11-12 04:36:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 460a1db3-5444-3a8c-b806-4cdd62ffee35 | -23.59856 | -49.01401 | 2025-11-12 04:36:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4072771c-e81f-30fe-a5b8-032cb9bb1c96 | -17.24301 | -56.01944 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22728a61-c9cc-3606-9f8a-84373c0d9a34 | -21.30665 | -48.54663 | 2025-11-12 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5c628d0-2626-37a0-95f1-0160669442be | -23.59446 | -49.01765 | 2025-11-12 04:36:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a514e01-fd2e-3cc4-8f1e-9899178feacd | -20.50953 | -47.26456 | 2025-11-12 04:36:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5e27854-ab5c-3087-b1e1-0381da8dcd9c | -20.23014 | -50.90326 | 2025-11-12 04:36:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b117d251-7fc3-3127-ad62-020f96d2ce42 | -21.16976 | -48.69852 | 2025-11-12 04:36:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8a2b187a-ca4c-308b-939d-3218010327a2 | -19.74701 | -58.01365 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e97a06a3-bf75-36ff-af8b-9d0f6319c52e | -22.32547 | -47.09227 | 2025-11-12 04:36:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dea97b8-0828-3801-9269-bb4eba328a68 | -19.74805 | -58.01646 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e180700c-5ba9-331b-b474-a4cbff8dc61c | -21.2439 | -48.83939 | 2025-11-12 04:36:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
