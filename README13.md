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
| 54f5d79b-e2dc-31c2-b854-beb5d70cb93b | -6.53417 | -56.54291 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d71959f-3d82-3745-a9e0-02bbffbe3274 | -6.55466 | -56.25368 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba6a6bf-b1b9-3208-92a9-b58141ba788c | -4.18227 | -49.40682 | 2026-08-07 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef0e61f2-80c2-3309-8072-ac939c6e56e1 | -4.26787 | -48.19656 | 2026-08-07 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| de2365ce-984e-3a2c-b68e-c55638efd409 | -8.08094 | -45.58215 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 791652e4-efde-369a-b311-0a1dfd701af0 | -8.33613 | -46.39459 | 2026-08-07 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aadb0966-b027-36e6-81e1-d58df2292e90 | -8.54062 | -49.55374 | 2026-08-07 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7065ac4f-e1f1-3270-86bc-e3d337cff918 | -6.54061 | -54.92727 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a2f7456-2900-30d0-9917-834235858a21 | -4.46117 | -47.91774 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 03e5bb46-dece-3a48-9229-ee44c7ba874e | -4.46062 | -47.92119 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2332fe0-6422-3002-9dc6-7410daaf3d3b | -6.64611 | -56.42941 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ca9ed5b-9f1a-37d2-bd76-a619b633810a | -6.94774 | -59.52431 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 912cd1d2-c420-3995-b238-7503bae602ea | -6.95242 | -59.52642 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64901328-1516-33e6-aa1a-4471939920b4 | -3.26411 | -49.52961 | 2026-08-07 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daee8dbd-40ea-3bda-b011-f43dd4010b41 | -5.42569 | -43.43364 | 2026-08-07 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc950182-420c-39e8-b144-0f300ce2d49c | -6.64662 | -56.42657 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c2bd0d-6348-3ebc-a13a-2029a0ce7d7b | -6.64475 | -56.40788 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74624142-f7ef-3718-89fc-da3e93be4429 | -6.54383 | -56.54779 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6397105-81b4-35f6-a017-6bc69c085a23 | -6.86089 | -46.00463 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 193d77a3-852d-33bc-acc3-33d865773cd0 | -7.15096 | -48.94591 | 2026-08-07 04:44:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 614d451a-8f7f-34f9-9ece-2fa7b5c542c6 | -8.47014 | -49.56415 | 2026-08-07 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1892a44b-ab30-3176-923f-3f88274d1831 | -6.47886 | -42.22657 | 2026-08-07 04:44:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a69bec1d-eb07-3965-b62e-cab0837de58e | -3.21087 | -50.92142 | 2026-08-07 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ea4aece-2bac-317a-aab1-bee3057623b2 | -7.75337 | -45.02991 | 2026-08-07 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d46f5113-5350-3939-b24d-7d90302f7557 | -3.02817 | -48.4105 | 2026-08-07 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4041e578-f017-3a7b-8a8c-7fa4bb8896b2 | -6.64977 | -56.40891 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6fb4c0c-2dbf-343f-a0ea-c0c3d682f01c | -2.87951 | -50.47198 | 2026-08-07 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2a5006a-ac9b-34fc-8b62-7411918f5230 | -4.4573 | -47.92067 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9cfe2ef8-bb31-390d-af4b-4de8ae4946eb | -6.71015 | -58.95383 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29f5f6cc-cc3b-3c27-9a43-927f26d407fe | -5.42642 | -43.42877 | 2026-08-07 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f80001a2-c746-3c9f-abbf-c01b10eb15e0 | -6.62562 | -56.37845 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539dbb93-455a-32a7-b536-717f4f4d4d25 | -6.86178 | -56.57441 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b90c4b99-6c35-3068-8a0d-a517902acda5 | -6.71112 | -58.96317 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40f67a24-3b37-3dd1-a122-a8ab4f16a197 | -3.39992 | -49.78279 | 2026-08-07 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20b26090-fe1e-30e1-967d-49ad2ce89f7b | -6.8594 | -58.93855 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71198b75-7e84-36ae-996a-83436b07e6b2 | -6.85684 | -46.00798 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 816184c4-369e-3886-a5f9-3f66a864c4c8 | -6.62154 | -56.37203 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29333a35-991a-390b-9f7b-85de50578f44 | -6.47946 | -42.2225 | 2026-08-07 04:44:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| affc81f7-43eb-3586-b657-c6986dc76606 | -3.58916 | -49.48697 | 2026-08-07 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a59bc5-dba7-3ae6-8f91-c6799e52c948 | -8.34016 | -46.3913 | 2026-08-07 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7702b847-812c-3458-aa01-fac3372958d4 | -6.9486 | -59.51951 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 124d23b6-c791-3651-a574-e560658930cf | -6.72822 | -58.58293 | 2026-08-07 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38c58aad-9321-3538-9c47-9ba76568b3a3 | -6.73399 | -58.58425 | 2026-08-07 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82fc89eb-5ee0-320e-abd7-b62125512e26 | -3.11919 | -48.58494 | 2026-08-07 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17fe3334-5267-34a8-9d5f-923fa0529c38 | -8.33496 | -46.40221 | 2026-08-07 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e1d50d9-dfc1-3475-b9c2-3e0cd52a3872 | -7.72014 | -46.22546 | 2026-08-07 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f9eddd1-4ed1-31cf-a838-13d6e6b32138 | -6.86533 | -58.93964 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c9712e1-8a27-3936-bd31-26d7a8954a89 | -6.64373 | -56.41359 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da919c0b-8aac-3bf2-a4ef-4cbd7e30ca45 | -6.54331 | -56.55075 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be533063-7f12-3018-9405-9482b674eb30 | -6.91005 | -42.42546 | 2026-08-07 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 48c90ba8-5f42-30b0-847e-99f87e0788a4 | -7.75036 | -45.0251 | 2026-08-07 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7fd766d-879d-3939-b279-fdb53fbbd663 | -7.74671 | -45.02454 | 2026-08-07 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df7eef9e-589b-31fe-a2ec-f9b5e68b8a10 | -8.37659 | -49.64453 | 2026-08-07 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b0dc135-b00f-3539-8431-b1d117b8a92e | -6.54395 | -55.14989 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4955c6d-01c5-3430-8cd0-6dfd41054ca2 | -6.86738 | -56.57236 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8c6266-f6fa-33d0-b5ac-4ba45ce3f6a1 | -7.75401 | -45.02566 | 2026-08-07 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f75b9d5-c6a4-34d4-9df2-615d7bccc509 | -8.08154 | -45.57808 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c613b71b-046f-3435-b393-6e99841d9d86 | -4.91291 | -49.23534 | 2026-08-07 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af342dc2-7c53-3b27-96da-8f0bfab4e1d2 | -8.54005 | -49.5573 | 2026-08-07 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32cb0570-361a-3973-81d3-79f0a6548947 | -6.65028 | -56.40605 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afc0dee2-e6d3-3ca0-be54-4db9a86c7eaa | -3.90486 | -54.58007 | 2026-08-07 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 078b72f9-9fa9-3369-97ca-63ab91ea1bb0 | -6.73326 | -58.58826 | 2026-08-07 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b28cf11d-b8f2-3e68-a51b-668272c5f5f4 | -4.11268 | -40.50169 | 2026-08-07 04:44:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0d8edd0-4625-3247-8dd9-d661d34069ac | -6.60351 | -56.35637 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cab22c4-1b8e-39e6-99e8-bb57da049bdf | -4.36657 | -47.76836 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 616ae692-ec93-3de2-906c-b86a7d433ea0 | -7.9495 | -47.06636 | 2026-08-07 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e75cd7be-248c-3db0-b021-49a8627595cb | -6.13516 | -47.17651 | 2026-08-07 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a3775e48-ea26-382e-ae92-af3a0bb99c79 | -2.50745 | -51.81338 | 2026-08-07 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0212151-725f-3a27-ab4a-319d73f8d44b | -3.40053 | -49.77892 | 2026-08-07 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2f468b5-32e1-35e0-83ec-77793c64fbd7 | -6.73611 | -46.40934 | 2026-08-07 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 093cddb9-ff90-3c0e-859a-eede1c9f70f6 | -6.53926 | -56.54387 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bad47318-f7b5-38e7-a27d-8b7252cde5cf | -6.72592 | -58.93433 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a5eb3e-7173-36d0-a40b-b7d76e61dae8 | -5.82436 | -44.13569 | 2026-08-07 04:44:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c373e86-1ed6-3360-b01d-83a41afb5b19 | -4.9163 | -49.23589 | 2026-08-07 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c0cf8e1-7a5b-39c7-9442-d366175c84ff | -6.64425 | -56.41066 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ee1c5f-89ed-33f5-a664-b0dabd445e75 | -6.72078 | -58.92871 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09738ae8-c1f5-3841-a92b-89227e31ec37 | -6.70683 | -58.95313 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 097d3c88-1eb6-33de-adb8-1ddb07185c5e | -6.53978 | -56.54095 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c891a42-1f19-349e-a2c3-d218f8c4d03c | -6.98663 | -42.90764 | 2026-08-07 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6b067677-7a69-3ea8-b209-14f983944169 | -4.3892 | -47.75423 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3539bf47-4b7e-3f30-906b-8fa2a8013472 | -6.99074 | -42.90822 | 2026-08-07 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5912b33-bf65-3fa5-8c25-f26008c71802 | -3.82059 | -50.63224 | 2026-08-07 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 175dbdf9-c6c1-30cc-99fe-de5519de6b0a | -6.54901 | -55.17558 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94c6be55-6183-3c9b-8319-2b91a348da51 | -3.02805 | -54.52794 | 2026-08-07 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a961bdb8-e80f-3d62-9c23-81c5ca04973a | -3.83701 | -49.16413 | 2026-08-07 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 809338a2-4e6b-3f4f-9881-b5e1c3d21001 | -6.64926 | -56.41177 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08545677-56cd-3294-af0e-382c408e9c7a | -2.87224 | -50.47078 | 2026-08-07 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e61476b8-58cb-3fcf-8f06-775505d1d2f0 | -6.6508 | -56.40313 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 402d8205-6ef7-3ecf-9afd-402f1b651810 | -4.48327 | -49.82297 | 2026-08-07 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91540d87-9cb2-3be0-9000-5897b40216bf | -6.99021 | -42.91185 | 2026-08-07 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 694dc8f8-7978-34e1-a1ff-cb850df59949 | -6.74024 | -51.1108 | 2026-08-07 04:44:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3370c878-5131-3649-900a-70bb7d7b8dfb | -7.04159 | -56.5114 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3d1735-0e61-3143-9ac8-31472de6bd7d | -6.4777 | -42.23454 | 2026-08-07 04:44:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 99f171fb-6d7c-3bba-a69b-e743dc4512b5 | -7.09132 | -46.54931 | 2026-08-07 04:44:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 911acda5-8626-3b42-8322-61b44394fed4 | -8.66269 | -45.85888 | 2026-08-07 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a8e5e83-2be0-340e-9ef7-2d7d78d4d1f2 | -6.71273 | -58.95452 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c004d89-f663-3094-b3fb-7900d8757f0a | -4.4584 | -47.91375 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 56baf5ee-e65a-3bd1-9a58-1a81e0b4290f | -5.82444 | -44.13866 | 2026-08-07 04:44:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ac8c6c2-5bed-3313-abd0-159545f6afdd | -6.92267 | -41.94682 | 2026-08-07 04:44:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1122da66-6f84-3832-b459-ea6043e2ee87 | -2.87233 | -50.47189 | 2026-08-07 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README14.md)
