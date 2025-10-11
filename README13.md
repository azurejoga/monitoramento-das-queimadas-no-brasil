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
| 5ba4b50f-5bf2-3436-b725-1974fc453708 | -15.70011 | -46.64359 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 699f1155-d5a5-3933-b135-87d46ec290d0 | -14.92969 | -46.75725 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b40cb93-c8e6-3ff3-931c-f4f515c5d2f9 | -17.26032 | -46.90387 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| fd2bd062-bf68-369e-be0c-80e318270387 | -13.68539 | -48.08418 | 2025-10-11 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 640cb7a4-78d3-3e9d-80de-2b0e35329eda | -13.3005 | -47.12345 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c7953b0-7309-306a-9678-5ddce19ecffc | -14.91989 | -46.77817 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af509dff-cf01-3f03-8b9d-eed409137aa5 | -14.93719 | -46.75414 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 121aba99-355e-3735-ae4a-88a465639cc6 | -13.79544 | -45.38828 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a261084a-4995-3ed1-82d5-96117fbf6695 | -15.6967 | -46.63307 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adaf4246-1447-3a59-86c1-1aba23670b20 | -17.39803 | -46.8678 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc3f9fb7-10b0-35c5-9259-47dbfac3d880 | -16.81742 | -46.73016 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 167933e8-5d7f-3279-ab23-d33d0b7b6771 | -17.20753 | -47.33368 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7df886f-f7b0-35fe-8ec5-372230f7ed65 | -16.5351 | -46.729 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4f5b5f9c-e85e-339e-b8a0-6cb43145eb36 | -16.37285 | -40.75169 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f124f83d-2110-3f7c-8a52-853b4b339668 | -15.7084 | -46.62977 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26247825-c077-3b7d-8953-1af93f27571d | -17.37071 | -46.65858 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bce87d5-cf48-3af8-8354-2311e45dd16a | -15.58067 | -44.02202 | 2025-10-11 03:45:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f16dffb4-21df-3235-9463-9c221dc7dd08 | -14.96382 | -41.69032 | 2025-10-11 03:45:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 903d80f6-778d-36e9-8b10-9b856f413183 | -14.94151 | -46.75443 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d171fbf8-1e32-3990-87b7-d628baaf1d14 | -15.00784 | -47.57323 | 2025-10-11 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55fb59a5-8e6a-3517-8e03-11b3c674fd11 | -13.85605 | -45.84705 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a192ced-1ff4-3e85-968b-b8481898a424 | -16.31173 | -47.15454 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b36c110e-0cbd-35a0-8359-f289fb1ae0fe | -16.70165 | -41.50091 | 2025-10-11 03:45:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6be8f1e-e14a-3972-861f-6561763110f8 | -15.74363 | -48.97155 | 2025-10-11 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87446e18-b45c-3dab-b90f-819733a4a975 | -14.74335 | -46.13403 | 2025-10-11 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18748e7d-2724-336b-a836-4185a314cd66 | -15.11121 | -42.47129 | 2025-10-11 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bef0adcf-9ec0-3624-8439-2fddf7e1e94b | -15.70138 | -46.63723 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7971cbd3-7133-3420-a913-c4bd642f19a5 | -18.13435 | -44.34326 | 2025-10-11 03:45:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 999a430c-138e-3f00-913a-a58e83a92edf | -15.91032 | -43.28207 | 2025-10-11 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef1c3f32-f36b-3aab-9b01-689eb590265d | -13.67414 | -44.28322 | 2025-10-11 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 240ada9c-8eaf-3eef-9f18-23fab7e1979b | -14.92827 | -46.7644 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a41a122-3726-3fb2-b760-4bc11660dfe6 | -15.73624 | -48.97628 | 2025-10-11 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b78bc1f-65d9-344f-a6de-a5970db04e74 | -13.78146 | -45.41582 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 946118f0-bf8e-395a-a55e-20e61f7ca7c7 | -15.70615 | -46.63294 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 050d15f2-944e-3d7d-a523-649741757cd8 | -15.67886 | -48.13666 | 2025-10-11 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 958df122-6c06-3c35-b905-4fc81a2e4db9 | -15.06822 | -46.60459 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35f40787-4b20-3bd6-9373-a3cc1e04ab9a | -14.92555 | -46.75589 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a82f7a04-f81e-3c82-bfed-ac862cbb7c6f | -13.8567 | -45.84376 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1420192c-2174-39dc-ba99-74e9106af569 | -17.26164 | -46.89741 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 18efa918-9ef8-3c0d-9fc2-e6643d4537c1 | -15.06275 | -46.60414 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 504ac310-0f3d-34ee-bbbe-97d5a94ccfe7 | -15.69075 | -46.63524 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52c3bba5-fc5f-32d3-b230-ddb05e330ce3 | -15.39179 | -47.2922 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88d9d203-500d-3920-b04d-234d67f00e5f | -14.92803 | -46.77126 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fed6e9a5-007e-36e5-aab7-fdff8bead482 | -15.70737 | -46.62704 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7198f9cd-2711-3f35-a742-db036d514179 | -13.85148 | -45.84278 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2a9b704-4e42-3cda-a36a-2ecf86f32222 | -15.70075 | -46.64039 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fc6d929-c601-3f42-bdaa-0ff359f916a9 | -14.71099 | -47.43715 | 2025-10-11 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b873a193-e125-3a84-bd50-157c2ad95cd5 | -13.318 | -47.12505 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d892191-32a5-3c77-bff1-bb20e6e789d7 | -17.39402 | -46.8608 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f159ed-7a03-36af-b0dd-0f75ae6dd02f | -14.92899 | -46.76079 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f219ff2-56ee-3cb5-b6b1-0149f22ee172 | -13.32476 | -47.12696 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d50855d2-f0a9-3fb7-badf-077e4fc997f6 | -13.81562 | -44.13085 | 2025-10-11 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4d4496b-f919-39fc-802b-094e66e713ab | -14.95387 | -46.7553 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13dfc210-01e8-35fc-a58e-494bb5706b0f | -17.20604 | -47.33192 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a2f3bcd-f221-3f26-bf93-9d041b326e4c | -14.2747 | -45.89751 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eaecdf71-b158-36c5-ad5b-9879453efa31 | -19.73523 | -43.92686 | 2025-10-11 03:45:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4c55571-f2b7-3b7b-8461-6b418516e95e | -15.58662 | -44.5108 | 2025-10-11 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cceec70-5ef1-3f0b-830d-6e7027440005 | -13.85213 | -45.83948 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f839410b-5479-31f6-a57c-eb64de998dc7 | -16.24638 | -44.05508 | 2025-10-11 03:45:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9ed34fd-940b-35a9-9ac1-011ab59e127d | -13.81098 | -44.12987 | 2025-10-11 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c3193e9-701c-3e77-8071-0df95638e6e0 | -16.59576 | -41.10963 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4ff19088-5bbb-3834-acb6-504de85a6431 | -14.92754 | -46.76807 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33536489-6a79-365a-901b-232c8185552f | -14.95026 | -45.59177 | 2025-10-11 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67bc062f-b73d-3648-a045-12975698eae7 | -15.7038 | -46.62518 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f258de39-16cf-3cff-af93-21029a6701f0 | -17.39865 | -46.86473 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9f4e8ab-cb46-389e-839e-7d80bc89222a | -16.24549 | -44.05974 | 2025-10-11 03:45:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1906efed-a140-3518-b01e-cd29a4d97d8d | -19.09137 | -46.41407 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f64dc60c-5d56-3ad2-8b69-6229f78f66e8 | -13.83586 | -45.78521 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9dbedea-53e2-3e26-b6f4-7149aa1e048c | -13.24965 | -46.4897 | 2025-10-11 03:45:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 543f367e-97c9-3634-b6cd-8f3214a2f0cc | -13.77584 | -45.41766 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abcea3bf-d25b-3b0d-9c74-119367e30cae | -17.34948 | -44.45252 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e637ff6a-c10a-378a-bddb-dfb53cc8e02c | -17.48643 | -43.33597 | 2025-10-11 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 06a65581-9c40-3a3b-bc9d-6ca09d07480b | -14.01696 | -47.06534 | 2025-10-11 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4def76a1-337d-3e25-a21c-baa082fe4835 | -15.60539 | -42.67588 | 2025-10-11 03:45:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7bb65d75-20db-38c5-bac6-c1713ca2b838 | -13.77866 | -45.41984 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8c0a169-9007-300e-a139-7b4b6ee66655 | -15.31842 | -46.18978 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 33c3d185-a180-3242-a275-f399df8d7f64 | -16.2978 | -47.16728 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9cd8366e-921e-33b9-8820-a957ef230221 | -19.33031 | -45.79569 | 2025-10-11 03:45:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da9bd0e4-7552-3b6e-8354-642e5032db35 | -16.82261 | -46.7314 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecca8726-d96d-311e-909c-be0900a8352c | -16.37206 | -40.75629 | 2025-10-11 03:45:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6e541b2d-cbe3-3803-b429-36748700c1d1 | -15.39251 | -47.28873 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff6e1202-09f8-39b4-b4e6-b9e0c991bab5 | -15.91459 | -43.28275 | 2025-10-11 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b95e2a-c1f3-3c99-a90e-2846d005dfa6 | -14.94996 | -46.74683 | 2025-10-11 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 999e4dbb-2d24-3dc4-bbaa-d96f1cfaabdd | -13.30751 | -48.49202 | 2025-10-11 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55216e3b-0b1b-3920-a801-da2b63dcd589 | -13.07075 | -46.80955 | 2025-10-11 03:45:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6ec2587-fbd0-3a9e-9d5d-e83238425934 | -17.26097 | -46.90066 | 2025-10-11 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 1e95cd78-7905-33f6-a4da-358d9b533d87 | -15.70676 | -46.62997 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2572c436-acce-3c30-8bba-803e36210619 | -13.68643 | -48.07922 | 2025-10-11 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84d2998c-1069-3107-a054-7a849394c590 | -13.28702 | -47.13145 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8e6108c-2f28-3e0c-823a-6bc55e796b7e | -14.31953 | -44.68278 | 2025-10-11 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bf2ce37-c4c7-3de8-a3f3-c900560127fc | -15.7078 | -46.63276 | 2025-10-11 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21d75bc3-2823-30e0-b4b1-5f46de2c96c0 | -17.64035 | -44.4339 | 2025-10-11 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbd26b31-d438-3020-a082-fd109be21bed | -17.21329 | -47.65742 | 2025-10-11 03:45:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e11cbbde-6d2c-3956-927a-4489d2296747 | -17.48718 | -43.33198 | 2025-10-11 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 66010df5-8090-34bf-8fec-29f25dffd45b | -14.26747 | -45.87963 | 2025-10-11 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9183a66e-2a6b-3b0c-a1d0-b72de7b9cd4a | -14.95173 | -45.58986 | 2025-10-11 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0fae300-98ef-3023-ad7d-6fbf9d457205 | -14.98748 | -45.56195 | 2025-10-11 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52fbd39c-7aef-36ea-9e26-a9106bec9e04 | -15.01493 | -47.56769 | 2025-10-11 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff1e0b8-cf21-3b71-9a3e-ea4eb3020afd | -16.29861 | -47.16336 | 2025-10-11 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86f0f104-069f-333a-9d83-29d52fa3c631 | -13.41842 | -47.25657 | 2025-10-11 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
