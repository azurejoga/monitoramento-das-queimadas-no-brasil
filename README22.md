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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81ce2cf4-c916-3403-99f1-9a82831db528 | -8.89563 | -46.14799 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cbfe515-8ec5-31f7-b8f8-c60cf6b48dae | -7.27276 | -46.57924 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2321eeb5-76f3-3c46-9460-c8a12fc598d8 | -9.14956 | -46.94387 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbf2d78b-a118-3705-8ba6-6aea8639a346 | -6.39928 | -43.34826 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cb11916-4ec1-3883-938a-22422beecca4 | -6.40554 | -43.35307 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 310632a7-d188-33ad-be48-5c088452714d | -9.08719 | -44.94709 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69a2ee81-2487-3051-a456-d3b62601dd0a | -7.30923 | -43.96783 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb27f882-9f28-3e3d-8a81-80d2d318f9b1 | -2.26189 | -47.84448 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb0a2809-b90b-3e81-804d-5c358bd81a1e | -6.12261 | -43.33573 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b48d6a4e-a976-3646-93a7-852708732734 | -9.08006 | -44.9459 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70556177-63f2-3647-b144-e8bee22b4e4e | -8.0153 | -45.65439 | 2025-09-17 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61fd22a3-d3e8-3466-99fa-23919568130c | -4.59533 | -45.58636 | 2025-09-17 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be21fd32-a68b-338f-a414-e33af40b419c | -7.00489 | -44.57823 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa765ceb-48db-3f70-8086-d4a33eef02e3 | -5.3274 | -44.99504 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38e38a36-6317-3cb6-bde4-391650c8c300 | -9.54325 | -46.29747 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7377303-b3f1-3440-a6b0-c8117bacd48a | -2.92432 | -48.30527 | 2025-09-17 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9120b8c-4e6b-3e10-9131-e04b0d3ad90d | -6.48038 | -44.54372 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d1973d1-406a-3b31-8d50-fc47e0fb2b41 | -7.57503 | -44.56956 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4f708c5-5ac8-3c7a-a71f-05ec7bdd4b4b | -7.396 | -44.60907 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40f237f2-ff92-3217-ab4f-61c988ba35a2 | -9.05771 | -44.83817 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 961ad1e8-0b6a-3995-8574-8c15fd39c8f2 | -4.63174 | -42.17576 | 2025-09-17 04:10:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de47d8ad-b151-360d-8826-d5b341e5e4f5 | -7.76602 | -44.72364 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5abfc40d-423a-3731-8f69-7db36231ddcd | -6.39867 | -43.352 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf2cd369-d26c-3a2e-883a-5b59cde8545f | -6.95405 | -42.44233 | 2025-09-17 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 41b91a0d-8118-3204-ae25-63a65554a5e5 | -2.92346 | -48.31054 | 2025-09-17 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee945def-50aa-3572-a533-118b6b9904b0 | -6.86869 | -43.97009 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19813890-8734-3296-9059-65a07c910a9d | -9.54521 | -46.29975 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 498af095-552b-3650-8afa-21f245dc9295 | -8.67572 | -46.35952 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71dbf0e5-7aed-3201-8958-d9661eebf0bf | -9.09448 | -44.90283 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ceadf6d-12b1-3b8e-87f4-2d6588343d92 | -9.14254 | -46.93707 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c871e94b-b29f-3295-9619-57d05ccd01b7 | -8.96685 | -46.01943 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54145968-1491-3386-8f51-d8164bd85c38 | -3.17938 | -48.80997 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6172c6d6-21e6-3fe5-b2b7-118b83251d51 | -5.989 | -45.85001 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2531daee-54ef-35fe-bb36-fac5b015cbe2 | -9.06223 | -44.8768 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2b2fca0-e2b3-3729-b80b-9807a55e8f5d | -9.00811 | -49.78183 | 2025-09-17 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94bae0b1-9fd1-31f7-96f8-5c34b0f36bf8 | -6.67872 | -46.30288 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 049b8f8b-d6fd-31e1-8187-f949bfab859c | -8.62537 | -46.44635 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c7665bc-482a-3883-a2a7-48d4df958d1f | -8.56325 | -46.36535 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32925779-a5ce-3576-9c6b-cd2a1e8f5f4d | -9.04957 | -44.88704 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edd61dbc-9ada-372b-8b4c-85de1bab86c4 | -7.26305 | -46.58791 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9dd62128-fa3e-3d0f-9386-85c60cb9bdb8 | -9.08362 | -44.94649 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72da4d4d-f087-3e52-9e91-21746d068e35 | -6.24859 | -43.45868 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0d2c463-7ffd-3bb4-a831-fbb77a63ee61 | -7.6053 | -47.47213 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b18cdc88-d610-3970-8d14-c60c5690541d | -7.58861 | -44.57592 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f473dd6-bce3-34a6-ad39-442e6a5222c2 | -9.54629 | -46.30272 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4391d53a-d39e-3ac7-b147-2cad7e421f23 | -7.58794 | -44.57996 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74197f2c-3dbe-3e79-b32d-08c6e6e88dfa | -6.68183 | -46.30865 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| da59172f-cda1-3bd1-b9d2-9cc1d1e9f7fe | -5.40102 | -46.53173 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43459509-6be8-3920-a78b-7aa69de86b0e | -5.77406 | -45.89087 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fa0ffc0-7b6c-3a6a-a402-43c6ea225155 | -7.34087 | -44.58712 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a641963-0ce4-37ba-9aed-96d79ffc9b56 | -9.12558 | -48.1104 | 2025-09-17 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3878f07-b456-3e8d-865c-dccdc5dad370 | -8.00019 | -43.82027 | 2025-09-17 04:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74a67ecd-3656-38d5-a554-7bfb9bedc578 | -3.07306 | -49.46414 | 2025-09-17 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d284cba7-01c3-3b1c-9144-8ec028d0f406 | -6.96203 | -44.45836 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e406627-20bf-3580-a95f-daaa0b2ea9c9 | -6.21769 | -43.91263 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e7edec2-3893-3356-a5a6-7e011be68bcb | -3.68669 | -49.01884 | 2025-09-17 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| beb30158-2e36-3cc9-a8cb-25b39e265d0e | -7.06664 | -44.3467 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc444c96-92ad-3948-b0b9-a19527f91fc9 | -7.33621 | -39.71272 | 2025-09-17 04:10:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eab3c63a-c330-3b4c-a1b2-41c26e0fffba | -8.79253 | -47.80639 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab2b769-a676-39a9-b5c2-1bbd3921dbb2 | -7.60905 | -47.47173 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48705111-afe1-3ec1-a0f4-467c5697fef7 | -6.2113 | -43.9076 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25fe63d7-4cda-3fa9-aff9-a0dab37dc29e | -7.52711 | -44.73824 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 279feb16-bebe-3c8a-8126-f027510dc1c6 | -6.57187 | -44.08691 | 2025-09-17 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a641000e-7d41-327c-8681-a7b11c1b7ec9 | -8.90523 | -47.8792 | 2025-09-17 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2650e25-899a-3860-b48a-e73e87c8c9a9 | -8.5707 | -46.33964 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ad44c78-f9fa-36c5-8854-51b5e1a94fdc | -5.90659 | -42.74632 | 2025-09-17 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9db0747b-3a32-3f4a-ae80-ebbd0dc4a0b6 | -7.61505 | -47.46572 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa127fba-2189-3106-b0ae-f9bab6431c13 | -7.06597 | -44.35072 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1fe16655-8463-3b07-85eb-26babc592b11 | -10.66674 | -41.28907 | 2025-09-17 04:10:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05244146-6ee3-380a-b5ef-c2e165b40fab | -3.39303 | -44.75321 | 2025-09-17 04:10:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b79af47-d388-3726-944b-8956fe7795c8 | -6.98526 | -44.60833 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb14026d-9e87-3e34-b88c-639ff0f85bfc | -8.6599 | -46.407 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00498a41-3084-3a11-823d-418a7995030d | -6.6097 | -45.5824 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74d59441-d41f-3427-ba3a-87cd2aed05a6 | -6.2223 | -39.24859 | 2025-09-17 04:10:00 | NPP-375D | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13cf895a-77d8-32db-9c37-5149e64d1ead | -7.64903 | -44.4747 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b0c156-cdb0-3c81-bb54-2e2ef15f6de3 | -7.82785 | -46.16388 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4034e65f-44f3-3fe2-8643-05c547649389 | -6.87855 | -43.97568 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b244380f-433c-339b-9ade-c6818d5af420 | -3.6089 | -41.35719 | 2025-09-17 04:10:00 | NPP-375D | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5f476ab2-b34b-3100-9edb-bc76bb24fed2 | -8.907 | -46.27769 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca4a32b2-0195-3cf3-9eb8-ceb55ccdf46a | -4.05759 | -47.50263 | 2025-09-17 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 65759011-b413-3f2b-99a8-3855c7d271e0 | -7.88692 | -48.17402 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfefe0cb-55f2-3026-99e8-ab82d3876a1e | -5.80138 | -45.92078 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17171b4d-bbd2-3804-8199-9b1d20690f0c | -9.122 | -44.891 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e545278-23db-39ac-9600-a716398cc578 | -6.38284 | -42.8442 | 2025-09-17 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 41bc22e9-329a-3262-b28e-2eb49070e971 | -5.21095 | -45.1825 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd76cc5e-f61d-3db7-9526-ea850a72d57d | -6.97574 | -44.5313 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bcd1d67-95dd-386c-b2e5-6d27cae0d05a | -8.65683 | -46.40146 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c522e773-0c58-3eb2-a3b1-f7e24fa93ffd | -7.21523 | -44.39087 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cc2e2de-3b10-3ef6-9192-85959432ffbd | -7.58304 | -44.58745 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7ac6ff1b-999a-32ab-b153-e6a8846e4d5b | -7.65546 | -44.47987 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b61ae70a-8663-39a1-8c63-98d74661f20c | -7.96453 | -35.24619 | 2025-09-17 04:10:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eb7e2188-8310-369c-ab86-b80b52183bef | -8.47023 | -44.72648 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b3a970a-e649-3137-82e2-fe83c2c9e440 | -6.87917 | -43.97182 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4a59aa9-606e-33c0-bf2e-5c4e04de94a1 | -6.86171 | -43.9689 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb11d6f7-aecd-3e2f-a9f3-c44110c7e9c2 | -9.1475 | -46.93204 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00f97330-d823-3e57-85ca-68dbb87158b8 | -9.04672 | -44.88221 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 906cfdc4-8fde-35f8-911f-4f11f7c8a7ed | -6.1023 | -45.94139 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2a9e7b7-1be8-3297-8718-bee2c97c5ae9 | -9.17927 | -46.93771 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 87b19d3d-423f-3e8a-9913-d5af2c3eb1ac | -6.19128 | -41.19648 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c391b5f4-aa84-398b-ae04-c5f91d33cd9e | -3.76027 | -38.70257 | 2025-09-17 04:10:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
