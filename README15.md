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
| 920b5e83-880a-3eeb-a62c-11d1c3cab6da | -12.92555 | -45.0559 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7081adaf-c999-3f44-816d-d83fe691d508 | -7.66513 | -42.58152 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59754075-de4b-3e30-8179-a5b0e8bb607b | -8.04154 | -43.91701 | 2025-10-10 03:40:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d1729188-b2f6-3959-acd4-bb9c985da194 | -6.45889 | -44.58115 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2926a583-21e2-3fc3-896a-a2d910952cee | -11.63854 | -47.52738 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e7e8f1c-8ae1-36df-a95f-24a9c87b829c | -6.74582 | -42.85132 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b86cd68b-dd40-3fe4-a6e2-b4ee3ea9623a | -11.5333 | -47.10234 | 2025-10-10 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0502999d-86ff-33d9-92d0-be4dfa27f5b0 | -8.20793 | -43.34838 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 915b105a-6981-3e3b-9192-3bfd3a226998 | -7.28325 | -41.97003 | 2025-10-10 03:40:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42fd1021-c071-3454-8da1-b86be51dbb03 | -12.73886 | -45.85865 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1792384-1552-3697-9720-44666570badc | -10.15789 | -44.60526 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 31011f23-5df9-3709-b0cb-64ebdcc029b8 | -12.85731 | -43.81752 | 2025-10-10 03:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c0192c-f20d-3275-993d-8dfe7f326d49 | -8.60348 | -41.40672 | 2025-10-10 03:40:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf129200-3c6a-373e-a06c-c8b0285cad07 | -10.15709 | -44.60949 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bd01e211-f1e5-3319-97b6-573160fb65e7 | -11.97162 | -45.20903 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2ccb45b-9612-3a5d-bc3e-0562a0f85f2c | -11.97806 | -45.20626 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b3f122c-c8d2-3523-b234-a40571fc1aee | -10.16727 | -44.55579 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 359960d3-1c95-3593-82b2-53875ebc1ae4 | -6.72986 | -42.87959 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5635403b-5ca8-3ee7-98f5-9099f7ea51c9 | -12.57792 | -43.85883 | 2025-10-10 03:40:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cae2fd8c-2d8f-34e8-9505-022669de30b3 | -7.14513 | -42.20116 | 2025-10-10 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 43dd0ef5-e8c1-394b-adf8-791379acbfb6 | -8.19968 | -43.33291 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c5971ef8-0bdb-35da-89c1-901005ebeabc | -12.43836 | -45.77757 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c707007-a361-3bb7-ac35-4f6a72ea9867 | -7.1467 | -42.19224 | 2025-10-10 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54449c35-e9be-38b8-b74e-be6b683c3535 | -6.66164 | -47.74802 | 2025-10-10 03:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0bfb0b4-cf51-3854-bdd6-fa39160dd3d6 | -11.78298 | -45.04239 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585f88fa-3f92-34d2-bce3-477e1de7792b | -8.51165 | -46.17516 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d723c59d-33b9-3adc-b272-e4e0aaa36304 | -7.61445 | -43.06676 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 18f8cf03-855a-3299-ab0b-b2e9af37094e | -9.2994 | -40.23405 | 2025-10-10 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c5c39d45-ad51-3e16-b4ca-c03054b3f814 | -7.40441 | -45.16348 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4205e61f-e2d4-38e5-b601-3aac37e45c7c | -8.82884 | -40.55149 | 2025-10-10 03:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 008cd064-6aba-3464-911f-9da624a9f8b2 | -6.45369 | -44.57557 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cd9c6c9-7c6c-38e2-8204-90eb3c8b26a6 | -12.43174 | -45.78031 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f39148e8-6fa8-3df1-8372-8fc806154c88 | -7.62799 | -43.05275 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6c3f01b-d100-3740-8438-e737f143948d | -6.74585 | -42.81974 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9b9af669-366e-3d88-86dc-25cf6e243690 | -5.33766 | -45.56897 | 2025-10-10 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3c73479-2b22-3fe2-a9bd-6b9cbadea18f | -7.70176 | -42.38134 | 2025-10-10 03:40:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 51b9812f-de12-34f0-a7c9-b36907887e56 | -7.26909 | -44.1058 | 2025-10-10 03:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e08ec24-da6f-31e5-9445-607161144e45 | -8.20731 | -43.35174 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ce3779c-d942-333c-a1a0-f4d7484b0891 | -7.40008 | -39.7891 | 2025-10-10 03:40:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 579f8b1c-d386-343c-b1ea-fac225009e0d | -5.33666 | -45.57442 | 2025-10-10 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2a2d514-d4bf-3fce-a57b-2f25a537c5a5 | -6.72863 | -42.88655 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 937f298a-dadf-3f5f-82ca-8df36c6d3028 | -7.80176 | -42.40865 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e1db7a72-2eb4-346a-8edb-f42a2e7cdccd | -10.14966 | -36.17147 | 2025-10-10 03:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 20dd6b44-de3c-345c-b453-c392613a1f40 | -18.64179 | -43.94117 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8297f3cf-bf3b-335b-96a8-5d7b2423cb32 | -15.238 | -46.37936 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 530d812b-1366-377d-8261-fbd4f0796ad4 | -15.91114 | -43.29093 | 2025-10-10 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 228499aa-207d-33f8-b7e1-cfa124665350 | -14.39184 | -46.00584 | 2025-10-10 03:42:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4e85fa9-77f1-38fd-b57f-202e7b961bd6 | -17.94442 | -45.03195 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1314007-dd27-3f7e-b9e5-4df56dc0703a | -14.93597 | -46.77066 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6f953614-4c68-3fad-9482-cf0a1a512b33 | -18.04768 | -44.98238 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bc764fe4-1b62-35e3-8763-18f40af5a494 | -14.26736 | -45.90907 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 680ced67-0dab-30c1-a559-df82848953fb | -16.17349 | -42.85882 | 2025-10-10 03:42:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41ffae28-202b-3e7d-9608-b302f545223a | -13.84735 | -45.8586 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 8621dab4-035c-31b6-8b7f-270706ddc300 | -13.83695 | -45.82255 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78b4f117-0a4e-32f7-a0dc-f6fa0307396d | -16.26433 | -47.16383 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99e3edb7-e1a0-33dc-821b-9528a2e61dac | -17.99152 | -44.98018 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 806e053c-ff4b-3d90-b112-0187977ab738 | -18.41726 | -45.24376 | 2025-10-10 03:42:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ac6826a-93cc-378f-8ee5-dcb16b322037 | -13.84562 | -45.86537 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| daf43de7-4b05-3d56-b959-50c7803dafbd | -13.83929 | -45.83997 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adbfb4f9-50e9-3d2f-806b-e7ca9a66cab1 | -14.26939 | -45.90292 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6c28c92-9b22-37e3-8b41-88aec90f977e | -18.64631 | -43.94271 | 2025-10-10 03:42:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f98fcbb1-2f6a-3ad2-9eae-e0ed310585c0 | -16.27164 | -47.17302 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8c41cba-0066-3bda-a237-e71809af9194 | -13.35525 | -47.60088 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fed4263-fcdb-3aff-9c6d-940036fef62e | -14.88886 | -48.24416 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| af999255-d73a-3a43-8622-cb2d3fff090d | -13.34238 | -47.75558 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c087bbe-fb6f-350a-9ae3-c339a40db351 | -13.5261 | -48.1229 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d9de399-abee-3897-8dac-f284867852cb | -14.85929 | -48.47443 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62841e3a-2d0e-3907-881b-a7e3a35df052 | -15.55306 | -44.32874 | 2025-10-10 03:42:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af5fbb36-afe7-37c1-ba56-c9ca59977d9a | -14.8779 | -48.23236 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5f52485e-6cc9-347f-aceb-e62ce2c2102a | -15.82687 | -43.77609 | 2025-10-10 03:42:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f67d8a93-12da-340f-89d1-fe3d0e75473c | -19.84169 | -41.80907 | 2025-10-10 03:42:00 | NPP-375D | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4e675c54-2416-331f-96ed-9afbfe50d259 | -15.00486 | -46.28824 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97198191-81ee-32c7-9db5-97391bc5e2c1 | -15.91009 | -43.29637 | 2025-10-10 03:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d4a0aa1-7e1e-3357-9e9e-33ae9f2af70b | -13.36206 | -47.60024 | 2025-10-10 03:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76e26caf-df64-3592-9ad3-ba8272441aa5 | -18.54121 | -45.06835 | 2025-10-10 03:42:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98bf9798-14e7-3b71-af28-70cbb6526a0e | -16.26771 | -47.16225 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 830c616f-b740-38eb-b71c-7a376abf76ff | -14.68505 | -48.06754 | 2025-10-10 03:42:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 48837ca6-396e-36f3-b15f-d3e8530ff86a | -15.75084 | -48.99152 | 2025-10-10 03:42:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f520e102-076e-3fe3-9647-cc629a243135 | -14.92858 | -46.77658 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0279a1a-57c0-35e4-bae4-c16d35494ed3 | -14.94713 | -46.77644 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aee39ede-6eba-34b7-a939-04ccee4f13bb | -13.31069 | -47.74568 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdf2c2f8-7500-30ea-9851-8a381c85c3e7 | -16.26672 | -47.16702 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30395da0-4191-3542-b54c-f99fdc874240 | -13.8359 | -45.88434 | 2025-10-10 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a80096-20ed-3be4-9125-7ea8e97e6910 | -15.74872 | -48.98818 | 2025-10-10 03:42:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cecfeeec-ba98-3831-b286-cc55a60af4ee | -17.93182 | -45.01676 | 2025-10-10 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| dee047cb-45e4-36c8-abfe-d9204b0660e0 | -13.8399 | -45.86424 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39e90558-861b-353d-99f1-a5b1d02bbafb | -18.02365 | -45.02298 | 2025-10-10 03:42:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ab050a84-2680-3ecf-b902-7de40b119633 | -14.88506 | -48.23055 | 2025-10-10 03:42:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6fe41df-5177-343a-8cec-5f88eddeb55c | -13.2706 | -48.02613 | 2025-10-10 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a68d7107-71f0-3616-aab7-11147657dab7 | -16.04999 | -48.08057 | 2025-10-10 03:42:00 | NPP-375D | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 211ee3c4-9356-3e29-a19c-9ef2e5325dd1 | -17.39029 | -46.87125 | 2025-10-10 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1a7a0af-2f68-38bf-aa92-05ddd3d2ccba | -15.32773 | -43.1969 | 2025-10-10 03:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bb915a95-1963-305f-9753-b22b747bfcba | -15.09094 | -46.59937 | 2025-10-10 03:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 759b42fd-0f27-3d0c-81bf-70d4179ca0dc | -15.24475 | -46.3743 | 2025-10-10 03:42:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85aaa37a-729e-349f-a946-ab123d291c86 | -13.83511 | -45.8883 | 2025-10-10 03:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 432c5be0-c854-36cb-9bbd-0d86a9eb94c7 | -15.42913 | -47.99252 | 2025-10-10 03:42:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7fdd56f-0b67-3b6f-84aa-6299cc925fc2 | -16.25321 | -47.1138 | 2025-10-10 03:42:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebcee1fc-5d89-3ff0-a4c5-4fb31d4cdc46 | -14.9453 | -46.7679 | 2025-10-10 03:42:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1eadf1d9-9689-3848-84e7-d3abc007e0fd | -14.26366 | -45.87345 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b66a357e-82fa-37e7-82d4-c39de9cf640a | -13.8459 | -45.83677 | 2025-10-10 03:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README16.md)
