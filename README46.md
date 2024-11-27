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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddb9ee75-b9fd-3d96-90b9-f9ee658185b2 | -3.1133 | -53.2381 | 2024-11-27 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 90d9b63c-1a70-3c8e-a5b2-1edad828dfa1 | -3.1691 | -48.4394 | 2024-11-27 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 7ea8947f-401f-37d7-9020-00ed2a628978 | -3.1876 | -48.4387 | 2024-11-27 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2d28f732-a043-318b-a64e-ee630c0dae20 | -2.8346 | -54.1326 | 2024-11-27 04:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| bda3e951-0b6d-3e84-b4ff-213ca0e9d000 | -3.9674 | -48.0851 | 2024-11-27 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 65d12dba-43ab-3f1c-a410-613f17309000 | -3.9675 | -48.0634 | 2024-11-27 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| c37797f1-65ac-315e-a6b1-b0d6b08fd8b6 | -5.9788 | -45.3621 | 2024-11-27 04:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| fde7afa9-a324-3a69-af50-812ad6d4e5b3 | -3.0949 | -53.2588 | 2024-11-27 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| ad50a869-b8f9-3403-8fc1-174228fb49d1 | -2.1928 | -53.7637 | 2024-11-27 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 24b8e1be-8158-3bab-8f44-33130f2a3253 | -3.0949 | -53.2385 | 2024-11-27 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9cb1eb21-6248-3480-aaed-f7cc43cb48a2 | -4.23 | -50.8774 | 2024-11-27 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 1ad87ded-8c36-3ebf-8cd0-da6fb7ca1dc0 | -3.1133 | -53.2583 | 2024-11-27 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 591d2283-0f0d-369c-aba5-6ef43be21615 | -5.72421 | -46.16617 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cf39d980-f0e2-3af6-a777-6f0636b5d4aa | -5.97515 | -45.36018 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7af3c8a8-b4fb-3e5d-a133-d10a6f19809c | -7.68866 | -42.9708 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 375f7f77-c29a-3b1e-baf5-7a8255780cca | -8.74267 | -50.40278 | 2024-11-27 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cb82114-016e-3962-8a98-22717821cacc | -10.76074 | -47.51426 | 2024-11-27 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc1c5a1b-2349-3be4-8a12-ec40598ac145 | -7.85714 | -48.71366 | 2024-11-27 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609befe0-2eca-33e6-a35a-4985482d4d98 | -6.36914 | -47.35645 | 2024-11-27 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e01f504-7c8e-31ae-94c6-26813c9012d5 | -5.75512 | -46.25784 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f49fbcb2-ae9c-3118-9d59-9605d15936e2 | -12.33578 | -49.99862 | 2024-11-27 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 875435a9-cbbb-387d-850f-6ed52c24dd11 | -6.83108 | -44.39344 | 2024-11-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ba9473b-4be8-3820-86be-84d86b3ec380 | -9.23714 | -35.67841 | 2024-11-27 04:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2a483bc0-faeb-3103-83ba-08a98a095c61 | -6.63439 | -43.85899 | 2024-11-27 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bc61d77-300b-3600-be04-f6cbf031a943 | -7.69783 | -42.97987 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27343576-2858-3e50-b409-54b3331336d2 | -9.25179 | -50.6622 | 2024-11-27 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6054ae56-0933-331a-bb92-60df22cfd86c | -7.22158 | -45.3071 | 2024-11-27 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d462371-feac-32bf-b9a3-0c8a08d4254c | -4.06385 | -54.6707 | 2024-11-27 04:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91b387e6-b5c4-3c91-86f8-352e7450990f | -6.16265 | -44.42697 | 2024-11-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3179201e-d50d-301f-ab5c-4e5dc6e58ccb | -6.02305 | -45.80379 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98972e3c-0df3-3782-8a8f-8249a0a77fb2 | -7.69553 | -42.97184 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cf66d7e0-3dc9-3300-bff5-171df565c0f9 | -6.39649 | -44.27895 | 2024-11-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec141bce-3988-33c7-857e-532f78be444c | -8.13489 | -44.4699 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e24b1be4-bdeb-3ae9-b406-8f5b102c02dd | -7.5403 | -35.09811 | 2024-11-27 04:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7e598f3-2c3b-38fe-ae5c-847d16c057f9 | -5.72479 | -46.16253 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4c6d34f-5d1f-3e5e-8cc6-9ad32129cc39 | -6.99573 | -45.62318 | 2024-11-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7ee9d274-d6e0-3b74-9d40-5e9d4b9d844a | -5.19647 | -48.18446 | 2024-11-27 04:21:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 388abc23-cce9-3e04-b130-0acb4c76fb20 | -5.75825 | -43.07326 | 2024-11-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a04f9e25-a372-381e-9692-e28b35f3b4c9 | -5.82679 | -44.11138 | 2024-11-27 04:21:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02f3db10-4e06-3e49-bdc3-328c41820ff6 | -4.06312 | -54.67494 | 2024-11-27 04:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f85b67c-3f4c-349d-8fda-6e3595389405 | -6.70847 | -47.27005 | 2024-11-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98cc8ae2-dd3e-3886-bb7c-2fa11dc6a075 | -8.13102 | -44.47288 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb51ecf6-3048-3e91-add3-cbe404672290 | -5.61892 | -43.94744 | 2024-11-27 04:21:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8af0f1f-c008-3b5b-8d57-16ea64fbee9c | -7.24327 | -46.73488 | 2024-11-27 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2281b37-ecb4-3466-9f90-62f1768641aa | -6.38505 | -47.17106 | 2024-11-27 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dabe4d48-16b3-37ae-84ab-312e910c14b8 | -5.80664 | -43.00694 | 2024-11-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8453c8f7-33e9-3fa9-a1be-f5f6f91bbbe7 | -12.33659 | -49.99392 | 2024-11-27 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0a036b-c97a-370d-bc63-0e47c3b995d1 | -10.76012 | -47.51805 | 2024-11-27 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84eb7e9b-766b-3e2a-8f11-60a089eba04a | -9.92019 | -49.59978 | 2024-11-27 04:21:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee37024f-29fd-3873-af88-cf052d28ac2b | -10.02661 | -36.18206 | 2024-11-27 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4d6e524e-fe2d-3ea3-a3a7-8a7b2aac8986 | -5.79297 | -46.67928 | 2024-11-27 04:21:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38f7e51f-fd93-356f-9dcb-80a317de3118 | -8.02322 | -37.8475 | 2024-11-27 04:21:00 | NPP-375D | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60898c0d-1430-3ecf-ac1a-62b0d34d8c40 | -4.13941 | -54.33763 | 2024-11-27 04:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36f5ffdd-e146-36cc-8bcf-160185daf5d0 | -5.19426 | -48.19806 | 2024-11-27 04:21:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1be891e-6a01-338a-a152-b287d16f1353 | -6.19308 | -44.4282 | 2024-11-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1e74df9-5cb7-399a-9921-eb50d25d269a | -7.54232 | -35.09988 | 2024-11-27 04:21:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e2fe5d9-ba37-3fe5-aa75-a44d818b80d0 | -6.02248 | -45.80736 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 273b39e4-ef7c-3eac-8b3b-a4e1a829ee9a | -9.92402 | -49.60043 | 2024-11-27 04:21:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c8015da-5164-3bbf-acc9-704a994d68f9 | -5.98183 | -45.36122 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 559e19a5-7426-3082-a844-b7cadc7c10de | -12.03085 | -49.53841 | 2024-11-27 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f21d2c9-5bb3-3dc9-8d67-34be89a1d62a | -12.0301 | -49.54285 | 2024-11-27 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c733406d-05ea-3f53-9dfd-051eff823225 | -9.24264 | -35.67914 | 2024-11-27 04:21:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a16fede4-304b-32db-a2ec-a8f2d6a2bcd1 | -9.83985 | -48.14116 | 2024-11-27 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5ad2ee9-c599-349d-a7ac-a5ed1650ceab | -5.50458 | -47.16679 | 2024-11-27 04:21:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74ab201a-17a6-33c4-bb47-0ea176c994fd | -6.0027 | -44.62932 | 2024-11-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11429735-dbad-31a3-b7ba-d289fae3f093 | -5.90924 | -43.40701 | 2024-11-27 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ebb23a2-bf5b-3487-886d-7f8e546bc40d | -7.14886 | -35.26544 | 2024-11-27 04:21:00 | NPP-375D | RIACHÃO DO POÇO | PARAÍBA | Brasil | 2512762 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6effacbc-b6c8-37d2-a938-e82d66195be1 | -12.02269 | -49.5415 | 2024-11-27 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40d9fe22-713a-3c14-b6cb-00c46fd1da7d | -10.02122 | -36.18142 | 2024-11-27 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e621f527-b64b-3be9-8089-a59fb477abaa | -7.85341 | -48.71299 | 2024-11-27 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c9b238-36a5-3c61-9b21-ba31f70dd6e8 | -7.703 | -42.99211 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c93e22a6-e51f-344e-a629-af832e0de60b | -6.01171 | -46.57671 | 2024-11-27 04:21:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a54e704b-b4fb-395f-a14e-9e517fe02617 | -9.72941 | -50.3494 | 2024-11-27 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9080457-a065-32a4-98df-80f82780ed29 | -4.72731 | -49.50319 | 2024-11-27 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd5643a5-7703-3194-9bcb-19e855f087ef | -6.36624 | -47.91875 | 2024-11-27 04:21:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50c12e5b-c7e4-303e-97e7-4092314a4693 | -5.42974 | -48.48132 | 2024-11-27 04:21:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d83180df-bfc7-36f0-abd3-c5db3924eb74 | -5.23628 | -48.05724 | 2024-11-27 04:21:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f0953b4-ab00-38d1-9b18-b281a2dc070e | -9.91636 | -49.59912 | 2024-11-27 04:21:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff349cc1-6404-3a50-b6da-2415c2b77763 | -6.99238 | -45.62265 | 2024-11-27 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c50122c0-eecd-3088-89ef-a5b9e7a2fbc9 | -7.6869 | -49.12811 | 2024-11-27 04:21:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9da4433a-4a5a-3b02-afce-223db1edb630 | -5.90869 | -43.41056 | 2024-11-27 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 659ba545-ed74-34b3-a6cd-c60f46a16b77 | -5.92042 | -42.97243 | 2024-11-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d2475e77-d8f7-3028-b34a-e0ee530ee684 | -8.13713 | -44.47742 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 240f6ee9-86dc-3035-abc3-83689d2316fd | -6.69788 | -47.26839 | 2024-11-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bae58643-3317-3c12-9729-91a52d14d0d7 | -7.26242 | -49.50805 | 2024-11-27 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa75f26e-beb0-3e0a-9a1a-ebf86e1eff53 | -7.69496 | -42.97559 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ac9ca174-8f50-36fd-8f5d-2f337ec18633 | -5.98517 | -45.36175 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 080e09ee-7b72-39f4-91f4-52a9914ad8c7 | -6.15822 | -46.68109 | 2024-11-27 04:21:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6af2e70a-fb41-3c4a-9cf4-451b4ee36224 | -8.57227 | -49.20021 | 2024-11-27 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff036035-6933-35db-98fa-079ea54d717e | -5.73439 | -46.62306 | 2024-11-27 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93ddb892-ca36-30e1-bdd4-1e645c8d9067 | -5.99601 | -44.60696 | 2024-11-27 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eefab0fe-37ed-31ac-a721-b39078d4a83e | -7.16043 | -48.74495 | 2024-11-27 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b35fafa-7d5d-3b8a-96c2-c6c6d06bf59d | -6.13134 | -46.91261 | 2024-11-27 04:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bbd86d5-3c54-318f-9cba-4ec1e73e70f3 | -6.38411 | -45.68554 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7c5b775-689d-3128-aeb3-1b2c3f63bd27 | -8.13157 | -44.46938 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba26ad55-42ce-34b1-9414-f5e2960ef938 | -7.54284 | -35.09614 | 2024-11-27 04:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6910c00-7dd8-38bb-a223-27998c4c61cc | -7.98465 | -49.69165 | 2024-11-27 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a667995-47c1-3583-8160-a45e67f7e835 | -8.39917 | -49.17547 | 2024-11-27 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f75db67-3b10-3635-91c6-441aeaa0b70e | -6.90513 | -35.03802 | 2024-11-27 04:21:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a01b89bb-85d0-36f7-88b5-9b6d2b03fba8 | -10.53196 | -49.05129 | 2024-11-27 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README47.md)
