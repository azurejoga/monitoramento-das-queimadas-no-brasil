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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed3aebf7-9efc-3f9b-a59c-7a6bd95431ba | -6.28894 | -46.95607 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc09d0ff-2826-33e1-9e4a-d773f7bf04ab | -6.48667 | -39.34536 | 2025-11-14 04:25:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d431d2da-a49d-38fe-a74d-7a844b430f3c | -5.33637 | -43.03638 | 2025-11-14 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407f6934-2943-3d90-9915-172246a5fa5f | -5.25362 | -46.18149 | 2025-11-14 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f96d168e-5f8c-377a-bdd9-7d6ce2de4d64 | -11.98719 | -43.83649 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca34eb9b-9fa3-38f3-b02b-23347458e01c | -6.07885 | -41.62996 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2f4820f0-1c15-3494-92aa-92a96403c5bf | -11.80381 | -44.26046 | 2025-11-14 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 250a08cf-57da-321c-b540-71e0d8986863 | -5.51919 | -41.74729 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 071dd5d3-f925-389f-b161-d2cba01f3a82 | -13.33539 | -43.18849 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2326fab-8bdf-334e-b10d-925506cf2c13 | -6.47893 | -39.34048 | 2025-11-14 04:25:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5eb1076e-4455-3964-9405-200e68e85283 | -3.84576 | -50.20842 | 2025-11-14 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc46f711-6ca8-36e2-955b-5661308bcc13 | -4.93704 | -48.54744 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ec83f7b-e23b-3a06-9c6b-f08c1aa4d59e | -5.49001 | -47.69514 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e22dffc4-bd62-3582-8191-fe93579551ff | -5.63432 | -45.33519 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c183e7d2-5bb9-3017-acf4-020527c7d688 | -6.10999 | -41.52858 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bddb1949-be2e-37a9-8a99-8420550731fc | -13.97893 | -40.6045 | 2025-11-14 04:25:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0be0276e-57b9-360b-8c75-552d620ac264 | -12.00242 | -46.76525 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd085acb-5e77-3fe9-b7d7-639b68e409b4 | -13.28699 | -43.86006 | 2025-11-14 04:25:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d4d12d9-fbf1-3e7d-937e-81c73f4fa410 | -5.90403 | -42.74595 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecd00602-7328-379f-a0c8-6599d199d1a4 | -5.72132 | -42.35452 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| baf017c6-2beb-3b17-a572-f630b3e480ad | -11.14317 | -44.81795 | 2025-11-14 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d30184e2-d1c8-3be9-a325-aeb556d98564 | -5.36574 | -46.28603 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d5fadd80-a5dc-3286-a35b-046e2509431e | -16.03232 | -44.97202 | 2025-11-14 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3c95a77-90a7-3228-a47b-bb909e838a8f | -11.80722 | -44.261 | 2025-11-14 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fdae07a-36db-34e4-9c34-80f8721ecd61 | -6.15176 | -48.05035 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3ba557fb-9142-3588-8f55-23359ac03c9f | -6.5177 | -41.93097 | 2025-11-14 04:25:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 26f2b27a-5c0a-3939-b5d5-d762bd128fb0 | -5.03067 | -43.24582 | 2025-11-14 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e738992c-482e-3aed-8e0e-fd1b0b0ef53a | -12.6876 | -45.43201 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ffad01d4-e0f0-3f5b-9284-2d6d6efb4e59 | -6.66866 | -43.49037 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a65bdf8-e49d-3025-a3f7-f630e4a17c9b | -6.88867 | -42.85516 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| b5570d55-c712-3435-a96f-cd0ca90aecbb | -6.24338 | -46.23962 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 619add43-d367-36ed-8956-b126f951dc7c | -6.28852 | -41.72864 | 2025-11-14 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 33405ecc-7149-31bf-a319-027611a07c8b | -14.67718 | -46.88999 | 2025-11-14 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65af50ce-4953-332e-b171-e07c7cb7c6b2 | -6.09397 | -41.61061 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5b13eef-7abc-3893-b1bf-c3e76479c49f | -12.06314 | -49.40445 | 2025-11-14 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e65088a-5810-3e64-8d10-884a17c63337 | -5.59524 | -45.17845 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 956f283e-9081-3caf-a071-00fcb261115a | -12.01186 | -46.77048 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aca8157-0fc4-365a-947a-5b67fcd5e7d7 | -15.24974 | -47.94347 | 2025-11-14 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b6c1f10-13b8-36bb-bd69-ad8774106c04 | -6.97741 | -39.17017 | 2025-11-14 04:25:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c23bb95-8071-3565-9cc7-4fb03e206990 | -7.06585 | -43.58097 | 2025-11-14 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ce49c91-54a3-3c76-a68d-4f3a67506c89 | -3.41697 | -52.73141 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faa9ed66-38dd-36e2-bfb1-02cc2edaa101 | -12.07815 | -47.88464 | 2025-11-14 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b3d21e11-b103-3b6d-b4e5-e6c00bd4fe9c | -12.66965 | -46.74349 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6979d5c-df80-324d-bd7e-2f87f2a2ad5a | -4.88628 | -49.38847 | 2025-11-14 04:25:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58a7b939-0693-31ba-b820-2a1fce82f17c | -11.08481 | -44.84919 | 2025-11-14 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 450faa03-fc0c-369f-b0a6-7f8890ee1565 | -4.61059 | -45.96463 | 2025-11-14 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a3eb2a2-b829-3284-898d-9f6e1b1e94fa | -15.26184 | -43.59183 | 2025-11-14 04:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 213c21eb-2d3d-3d80-b831-467da2c6a533 | -4.70801 | -46.44389 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f76ad9fd-96fc-325d-9d35-310f33d71d1d | -16.59113 | -42.21568 | 2025-11-14 04:25:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1179866d-f3b8-38f1-aadf-6fd855266408 | -4.29521 | -48.24098 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5471557b-d4e2-3acd-b4ba-57545dccdbc2 | -4.33359 | -50.81913 | 2025-11-14 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60bf7c2c-2bb9-324b-9b7c-b98e29eee75e | -12.06241 | -49.40879 | 2025-11-14 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31c1fe48-6109-3164-bc55-706575491b79 | -18.32262 | -46.65479 | 2025-11-14 04:25:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b6fa804-038a-3bf9-a1e5-6e7c0bc183ed | -6.06667 | -41.7434 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5f48fbe0-8bcf-379e-9ff5-b4639289ca6f | -6.23881 | -46.24633 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 658f6780-741b-370e-aae5-8e6416591f9e | -5.46086 | -47.09792 | 2025-11-14 04:25:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c62fb2d-a905-3b4b-92d1-e9b0121762a5 | -5.06477 | -49.87182 | 2025-11-14 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dcd3624-700b-357d-90fa-16384e897747 | -6.88466 | -42.85838 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 94292ae5-ed14-3b34-a0c6-67cae3b96a84 | -5.72538 | -42.35122 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2656b135-f49f-3ab8-abca-eca06649f531 | -4.82137 | -49.72805 | 2025-11-14 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f43be96-8d9f-380a-aba1-ae23fe3c0a47 | -6.80689 | -40.08868 | 2025-11-14 04:25:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd3bf4ba-816e-33e8-a130-3b10a8a90a03 | -5.25599 | -43.18935 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02d66756-021e-3595-839a-96f5d88ce511 | -7.1487 | -41.25547 | 2025-11-14 04:25:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 11deb2f6-2c9d-3076-adee-6f14e8ab68b3 | -11.73829 | -48.53897 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff92cb75-b030-3c80-8858-e19fa592810a | -13.46305 | -44.03079 | 2025-11-14 04:25:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b906f6be-2a5d-3385-87e6-7dfa019d33b4 | -12.48992 | -47.29274 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea07961-5240-3e81-a54b-80cf8713adf9 | -4.72991 | -46.73 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47eaaefa-7093-3097-a76e-b625e9e91ad3 | -4.65782 | -45.47355 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28609ee0-4729-34e2-af2f-34f4c74e5db1 | -16.28695 | -43.82859 | 2025-11-14 04:25:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 817f262b-c499-3c9b-b76b-578c28662bc2 | -4.2204 | -49.11607 | 2025-11-14 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 91856e1d-b983-334a-ba95-8dba6fa3e805 | -5.24833 | -42.20253 | 2025-11-14 04:25:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbeff124-8b05-37ec-afd3-99e61e1cb9a2 | -14.67501 | -46.56411 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02d998a2-1a8f-3824-b1db-8aca09510425 | -16.54645 | -49.35318 | 2025-11-14 04:25:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbbf19ee-e1cc-35ad-884e-07dd0034e51b | -6.18392 | -40.87704 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ee127642-a596-32cc-9ef9-9acd785003b4 | -5.26961 | -43.77226 | 2025-11-14 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6db6c68f-2179-309d-a843-5ce6020110ed | -12.13634 | -48.01871 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3031a81-fcb0-3386-8430-4904e468afc0 | -4.95513 | -43.72701 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 660d5c37-e889-39f4-9ceb-c89577c181cf | -4.33284 | -50.82365 | 2025-11-14 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7132b7a7-e5ac-3151-839b-81b2577c2c47 | -5.8878 | -42.26107 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0de6b38b-5882-3603-ba92-2564950cdcd1 | -5.59942 | -41.06735 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30eb635b-8d74-3576-adfa-2ca091ce05e5 | -11.03319 | -44.65014 | 2025-11-14 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 177e7e85-3efc-3c16-bce0-0aa27a324541 | -6.07823 | -41.63398 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1df707d4-1999-3d61-91d1-62d6889c85be | -11.24676 | -47.4972 | 2025-11-14 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb41a402-c96b-34ab-961c-98507c3fa327 | -10.48003 | -51.86605 | 2025-11-14 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9c3f82-2b46-3149-8c8a-3d77b04740ee | -5.84244 | -47.68386 | 2025-11-14 04:25:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01196d7-250e-3868-9600-76bc2b8198e6 | -12.6926 | -45.42186 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1680838f-0d61-36fd-b2c0-2538f48c944c | -12.39214 | -49.97484 | 2025-11-14 04:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfb2b383-6afe-3f9f-86c9-ef064dfdbb98 | -6.06876 | -42.85744 | 2025-11-14 04:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 03df819e-2c44-3598-b667-d5a1c88f5a1c | -15.3341 | -47.35734 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1944d227-734d-3f48-8dfe-7bb8b0c0302f | -11.73896 | -48.53497 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c98b737f-5259-375a-8dd9-29dbe1caf627 | -17.96976 | -47.25433 | 2025-11-14 04:25:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 254b916c-d9c4-398f-99a2-91b02a986f89 | -4.70455 | -46.44334 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fc51bab0-1ad9-32bd-bf0a-d4295d8e80f1 | -12.71316 | -45.42151 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 047a36ce-1b42-3bd4-9974-adefa39afe81 | -6.10852 | -41.58733 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 87d0ceaf-f824-3391-ac3c-950461487e9f | -12.00576 | -46.76581 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e16554e-e0cf-39ad-a3a1-e40cc92d9df9 | -6.09001 | -41.70993 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a865958e-4029-3be3-bfef-be265f2b9953 | -6.38979 | -42.31946 | 2025-11-14 04:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7fc5621-5b01-3291-8285-cc83e3d766ac | -7.14704 | -41.71067 | 2025-11-14 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5dfd5db1-5185-3f86-9594-40ceae41395f | -5.97821 | -42.76494 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1f43027-4402-3c0b-94d2-762e0ecf4664 | -11.03488 | -45.29502 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README33.md)
