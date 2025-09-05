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
| 979f2969-2ccf-320d-928c-d872e67ca52f | -5.6079 | -45.0265 | 2025-09-05 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 81a30f63-e9bc-3712-8e1a-1d9ce89fad7c | -6.5856 | -44.564 | 2025-09-05 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8bd82291-7e59-3e7d-9d4f-e5f02539e07c | -9.2477 | -57.0697 | 2025-09-05 02:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1496413e-82c0-3a1e-b570-1df0d30e4f6a | -6.5856 | -44.564 | 2025-09-05 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 795f153b-e5b1-3657-9928-60108f3b9ea1 | -5.6079 | -45.0265 | 2025-09-05 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 7702ed06-0516-3697-ab59-49f5a9193912 | -5.5892 | -45.0278 | 2025-09-05 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 20cff8c1-72b4-347a-8736-439a6d92edf8 | -7.9768 | -44.5268 | 2025-09-05 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7aeab700-c444-3252-b055-b779406b6198 | -5.6079 | -45.0265 | 2025-09-05 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| df9c3104-ac21-35c8-b17e-b45a9d3c60c8 | -15.2156 | -52.372 | 2025-09-05 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 4e1cfcf3-702b-32fc-a49e-35d0fb54f428 | -6.5856 | -44.564 | 2025-09-05 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| eee6bfb2-ce73-340e-b03b-79441479a695 | -5.4917 | -60.138 | 2025-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| ea773617-dbca-3f49-a7d4-cf00d6f8f324 | -8.479 | -45.0704 | 2025-09-05 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 737c8fde-a01b-3d4c-af00-ed13e04594f0 | -5.5101 | -60.1183 | 2025-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 2ac0e8b5-0c40-31f9-8fcd-0a16f95f1775 | -5.4918 | -60.1189 | 2025-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 34695448-f257-3853-980b-775bdecd91e6 | -5.4918 | -60.1189 | 2025-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 82bc94cf-7a06-3087-82dd-97b62089028c | -5.908 | -57.7311 | 2025-09-05 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| b3b2d1ed-ae83-3106-8f34-5a488c81a5a9 | -5.6079 | -45.0265 | 2025-09-05 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 2dcbf08f-95da-32b6-8342-b9157a3bf27d | -6.5856 | -44.564 | 2025-09-05 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 09230157-7da2-3766-a827-86e1b6e6cc75 | -10.2373 | -50.5417 | 2025-09-05 02:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6dcc799b-a719-3024-a96d-f6974fcf997b | -7.9771 | -44.5038 | 2025-09-05 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7cbb9f65-c585-39a2-9f6d-feb76e3f039b | -16.4624 | -45.2402 | 2025-09-05 02:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6550d04e-2884-36a8-b988-e814cc4e654d | -7.9768 | -44.5268 | 2025-09-05 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d352b513-dc19-3a3b-a9d0-9a5298b82ccd | -5.908 | -57.7311 | 2025-09-05 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2a24dbf4-495e-3728-b498-65d57b911586 | -6.6044 | -44.5624 | 2025-09-05 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 22475e75-54a9-320b-a43b-d721d20d9195 | -5.6079 | -45.0265 | 2025-09-05 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 309d45be-8bea-3f68-9b13-f9043e184e79 | -8.479 | -45.0704 | 2025-09-05 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| cdb0a6e8-37b8-3e0b-b155-ccf8ba597589 | -7.9768 | -44.5268 | 2025-09-05 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d5a12695-fbb1-360b-a461-59ae6afda7fe | -15.6141 | -52.891 | 2025-09-05 02:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d88f5eb7-a9c8-34e8-9485-b48635a94994 | -21.8053 | -46.7872 | 2025-09-05 03:00:00 | GOES-19 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| c4e0ae01-c2ea-3ee4-b9a4-53bb802b3f22 | -7.9768 | -44.5268 | 2025-09-05 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5b457747-0569-39cd-82a6-bc438230359b | -15.6141 | -52.891 | 2025-09-05 03:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 16c5a5d6-b091-35fe-8015-eec5c4980461 | -6.5856 | -44.564 | 2025-09-05 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 34c17f35-466e-32f7-a29b-424a47ad4a49 | -9.0762 | -47.0113 | 2025-09-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 04a8b008-f71e-3706-b94a-e3dd6e2f8510 | -5.6079 | -45.0265 | 2025-09-05 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| fddc5c31-4ffc-35cd-b5a8-060862c666e4 | -8.479 | -45.0704 | 2025-09-05 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5653eb61-491c-3a5c-9dc8-64cb00b910e8 | -21.8053 | -46.7872 | 2025-09-05 03:10:00 | GOES-19 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| e11c05b2-ba6e-33e4-9054-2f096b4c8f9b | -20.2471 | -51.3245 | 2025-09-05 03:10:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| 77df2114-da0e-3473-859d-8d4e2d26458a | -5.6079 | -45.0265 | 2025-09-05 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 4021d7dd-a490-33ba-bec6-5317051d36d5 | -20.2273 | -51.3061 | 2025-09-05 03:10:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 182b4d86-de6a-30c0-ad4b-1f3351a8adc0 | -15.6141 | -52.891 | 2025-09-05 03:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fdb2b45f-7cb8-3c7c-91ca-68ffea7f1bc7 | -20.2482 | -51.2798 | 2025-09-05 03:10:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 1728b31d-0f21-3fc1-b90b-600d84c30cbc | -20.2476 | -51.3021 | 2025-09-05 03:10:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 271.0 |
| 721e947f-6307-384a-9e5e-2747772f8f7b | -15.6137 | -52.9122 | 2025-09-05 03:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 31b95243-d476-3cab-ab7b-ee0eac8016d3 | -4.15184 | -41.67376 | 2025-09-05 03:15:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98f9ac22-508d-3f2c-8da3-89727ca19908 | -4.87718 | -37.48413 | 2025-09-05 03:15:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3569f80-3f7a-3145-a95e-74fb5489dd70 | -4.56107 | -40.35145 | 2025-09-05 03:15:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7613d5c5-0065-3373-aa84-42997dca31dc | -4.12575 | -40.5799 | 2025-09-05 03:15:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e6d17f2-c4ee-35da-9368-c6ca61b2b4d0 | -4.5659 | -40.34852 | 2025-09-05 03:15:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b05da0ab-cdcf-3118-b45e-a6ba252be303 | -4.88245 | -37.48498 | 2025-09-05 03:15:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4e45780-53f4-3055-8fb0-d5661e3f6b14 | -4.15286 | -41.66784 | 2025-09-05 03:15:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c28b4d7-83c9-387b-a7c3-d4818f01154e | -4.56237 | -40.34424 | 2025-09-05 03:15:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 50c38caf-8809-3a49-ac14-5b2b8c36c03e | -4.12666 | -40.57453 | 2025-09-05 03:15:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 58ed0fe4-4412-3946-8e48-e9c3cb12bd13 | -11.39782 | -43.60342 | 2025-09-05 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b43106bc-2e91-39c8-9cc0-742674104889 | -11.38968 | -43.6081 | 2025-09-05 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ab6ac3b-c97d-3e13-a8b8-6a28cfea86d9 | -12.8344 | -44.4533 | 2025-09-05 03:17:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8efb4cf-c70f-3731-bb11-2fd67b73dc40 | -14.2847 | -45.21625 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 13afa899-7ca0-3692-9228-233785cfa4e9 | -14.27798 | -45.22361 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17f9fcca-6215-35be-8c4b-1365867de071 | -11.87901 | -40.95447 | 2025-09-05 03:17:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 573b856a-9eb1-3e96-95a3-c705584f5b8d | -11.3923 | -43.59547 | 2025-09-05 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfca4375-89e9-325e-8178-35d70aa13661 | -12.11886 | -43.34572 | 2025-09-05 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48fc0d6c-6ee9-3614-98b1-20e2bcaeb691 | -11.39098 | -43.60183 | 2025-09-05 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9be065fb-98b2-36a8-b0cc-940d81166966 | -11.98169 | -40.86374 | 2025-09-05 03:17:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 090f90bc-ea09-3cfd-91ae-fa8702ef83cb | -11.98009 | -40.86978 | 2025-09-05 03:17:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bb4e5355-863a-3d25-8b5f-891b7bf01199 | -12.11996 | -43.34057 | 2025-09-05 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca49028a-a25f-3cd2-959d-d2cb1f1b0981 | -11.98096 | -40.86547 | 2025-09-05 03:17:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9ba0549a-965e-3985-9105-2bc82ad31e70 | -12.8329 | -44.46032 | 2025-09-05 03:17:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 797f42bc-01a8-3148-b6f4-f22470a2104e | -12.0162 | -43.79115 | 2025-09-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 713ca214-d4c6-3b60-a755-18f4686f237a | -11.87989 | -40.9501 | 2025-09-05 03:17:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dcf0bf7e-4a63-3de5-8c81-66ad1f9f5429 | -14.27434 | -45.22903 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b38b818-1f23-3102-b2d2-a4ee9c1d66c6 | -14.27598 | -45.22168 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f8fe3537-23ce-3139-adcb-ebcf2b5e5339 | -14.28675 | -45.21815 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c3eda9d5-4ed0-3bf0-bb8d-98beccce6ac6 | -14.2763 | -45.23094 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8f62e1d-c54f-33e0-9093-ce7de9110a33 | -14.28146 | -45.23079 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4eec9c17-8ce2-3296-b6a7-44d4911e6f63 | -11.39364 | -43.58901 | 2025-09-05 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cd89bd4-4c95-3734-bc6b-0ee6ad12bad9 | -11.98084 | -40.86809 | 2025-09-05 03:17:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 25d25cf5-d6ea-37a8-a0ae-6a7e474d6127 | -12.01761 | -43.78464 | 2025-09-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ca125c3-6272-34f0-9805-d16cf3e6a4d0 | -14.2831 | -45.22345 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cfa3e813-8b6e-33af-902d-ae2a18215086 | -12.01691 | -43.78924 | 2025-09-05 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3657d0d-9fcf-30b9-b2d5-9ab155b48dcf | -12.11564 | -43.34822 | 2025-09-05 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50c0c5df-5335-37a9-87eb-96a2c0748d87 | -12.11665 | -43.34335 | 2025-09-05 03:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc8b251b-11bf-380c-b46f-90928696eae2 | -14.2851 | -45.22536 | 2025-09-05 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 48003e9a-46e6-3170-a551-04af2886c024 | -18.56285 | -43.6109 | 2025-09-05 03:19:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ab822a4-ee5b-38e6-8019-1af7241fa73a | -17.48736 | -43.33691 | 2025-09-05 03:19:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e6042fa-f2be-3c87-90ee-22017e0732ff | -19.79175 | -43.55234 | 2025-09-05 03:19:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1326545c-b3dc-3315-981e-ec3f1700b8e1 | -16.45823 | -45.25022 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d35633c-2ba9-365c-986c-4a72789b8bb5 | -19.29736 | -42.12045 | 2025-09-05 03:19:00 | NOAA-20 | SOBRÁLIA | MINAS GERAIS | Brasil | 3167707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9f997921-6cb4-3e37-b794-5444f3d2cf64 | -17.48643 | -43.34114 | 2025-09-05 03:19:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4c42df8-baf3-3779-845c-335eec45c08d | -21.79834 | -46.8007 | 2025-09-05 03:19:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 492301ba-fb64-3808-98e3-afa1307134bc | -18.61596 | -44.26735 | 2025-09-05 03:19:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c288ee50-5124-3620-9ae2-77a936439079 | -18.8657 | -46.37414 | 2025-09-05 03:19:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5245fad-3cb7-3da8-ac66-43c508099e21 | -18.61399 | -44.26384 | 2025-09-05 03:19:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f1b00276-1a5c-3265-a8ce-a78851577672 | -21.36226 | -46.95245 | 2025-09-05 03:19:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55956db8-28a4-323b-b581-5c9d08b52c36 | -18.62029 | -44.26526 | 2025-09-05 03:19:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b58f65bc-24cc-30ab-99f9-a85da4e34386 | -21.79798 | -46.80428 | 2025-09-05 03:19:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 5633d64e-1c6f-308e-b4e5-22b73442138f | -20.52551 | -46.11496 | 2025-09-05 03:19:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd362378-6a81-361d-af92-103660aadf85 | -16.45319 | -45.23672 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7392a12-dfe5-30fa-a47f-c5437b562cdf | -21.79984 | -46.79699 | 2025-09-05 03:19:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| abcf00d4-7a55-3324-9a0f-2d6778ad8f97 | -18.86996 | -46.37414 | 2025-09-05 03:19:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5d741817-76d3-3dcf-8e67-f062b3b96bc1 | -20.36921 | -41.94125 | 2025-09-05 03:19:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93052c1b-29df-322e-ac1d-49e17f7a5a54 | -16.45289 | -45.24174 | 2025-09-05 03:19:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
