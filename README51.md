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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a50d21e-d6e0-3fd9-b753-794872612baf | -6.2784 | -46.24599 | 2025-10-07 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dda4f17b-8a3c-3fa2-b6cb-ec3e6acfa448 | -9.97942 | -48.01777 | 2025-10-07 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c65bab9e-979f-3031-8b16-c98bacdcf8f4 | -8.87883 | -46.77463 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f795e89c-f977-3500-8826-64708052e1d7 | -6.36478 | -42.86471 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6084455a-8cfd-3e2e-bb97-212915fbeb7f | -5.39811 | -45.91407 | 2025-10-07 04:36:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c2d875-6246-39b9-a99a-63cfdb122b84 | -5.26916 | -44.09426 | 2025-10-07 04:36:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 559e1bd6-477d-39d4-85f3-c0ebb9582937 | -8.18796 | -50.3009 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a3e1d0df-ffa1-3af0-b7dc-5118f6772748 | -7.51482 | -49.90741 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ac74a7-13e9-3fa1-b79b-50a6e1cde938 | -8.61719 | -44.93524 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 991897a6-7101-3864-b32e-e1d8a586b8e6 | -6.64142 | -42.75879 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8fe9e8fa-2b1c-3db6-bb99-036b781ac0e9 | -4.21562 | -49.99031 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc8fbc2b-b4e5-3ee1-ad34-9e923f0acbc0 | -5.89291 | -49.37126 | 2025-10-07 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83c97470-7953-3dbc-9671-33e74b5a899d | -5.77012 | -45.74545 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b435c13-7b0d-3391-aade-21856bcad7fd | -6.13629 | -42.6746 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 217d6733-87d6-38a1-97ab-026513fcfe69 | -8.1935 | -44.12108 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6722ed9-e9f0-3c77-abb3-fe957a5b5e23 | -5.33109 | -49.32474 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea295e1e-21cc-38fb-bf0a-4922bb0a3a5f | -9.18324 | -47.82757 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b6c7819-d488-3721-aed1-319d7108b3c2 | -9.3298 | -54.51456 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57beb18a-b4fa-356a-809a-aa1c6408f7ab | -5.80503 | -46.5548 | 2025-10-07 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a2b1b5a-7b59-3af3-a537-40c6744dc933 | -9.18772 | -47.84277 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 493bc131-e5d4-30cd-a740-a2f1db3067b8 | -6.98516 | -42.00657 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 016746a8-e41d-311f-b207-fc90e8f9f3e4 | -6.15927 | -42.57798 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c079c3b1-ce19-3b41-b272-244fc386335a | -8.17054 | -43.36084 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b7bccaa-d15c-3c48-8dea-83e692c7f0f2 | -6.25332 | -43.27318 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 869b2e21-0f23-36f9-bb68-3db2577846ba | -6.27805 | -42.91734 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34a6264f-e7ba-3663-bb02-ce00528d1efb | -4.58758 | -47.03568 | 2025-10-07 04:36:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74f3943d-1b95-3e9c-b36c-3b0534af51bf | -7.98518 | -49.95549 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d7ea6b2-3bd2-3d01-826d-a72bb5de0ede | -9.40303 | -49.37037 | 2025-10-07 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a62c12c9-3043-3795-a4fe-f09f5ff16903 | -6.73442 | -48.1744 | 2025-10-07 04:36:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29ed4470-662a-3627-80c7-5217c4280225 | -7.69636 | -42.39373 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d6a1acd-1817-3f2a-a4a7-e89392db1543 | -7.67529 | -50.21221 | 2025-10-07 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8779324f-fc15-3523-87ec-25a652693d48 | -8.41621 | -50.69765 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4199afe5-13a5-35fa-ba88-fce448674e23 | -10.67456 | -44.14691 | 2025-10-07 04:36:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fda7c2e9-30e9-316c-9ee0-f733bf59d4b4 | -6.9861 | -42.86365 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab068718-c647-329a-8fa5-76343acf8c47 | -6.72462 | -42.83716 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d580bba-6f71-3507-b711-858f486518fa | -10.0344 | -48.29079 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42ff249f-73d8-3238-bcd0-94fd23d9a59a | -5.19668 | -46.77667 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6c24ea-eac9-3b46-baac-38dcc491ddd2 | -4.59146 | -47.03272 | 2025-10-07 04:36:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbdca80d-e90a-3587-a0ad-a49af8e61a8c | -10.40578 | -45.37696 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c67dfd0-a9f7-370a-83bf-2e705f2ddae7 | -7.6958 | -42.3977 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4f9337fd-56b2-3713-9826-144c2eade9ba | -8.48426 | -46.27884 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81c0b079-0f84-3fab-8114-447fc886f3c7 | -8.55163 | -46.24158 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 25be7b67-9a0c-3adb-b31f-39c1a832debf | -8.17016 | -43.33539 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8c9f70a-a390-34a5-a68d-624c19420e49 | -5.84944 | -42.84743 | 2025-10-07 04:36:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| afd21534-4ce6-37b8-b908-4f47f86cc126 | -8.67879 | -49.94243 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7635dbca-b6bc-35a5-8550-373e7e82c1ec | -5.27573 | -43.2992 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ef46d3f-50c5-3ea2-8958-4b0fc85d3bc4 | -6.56722 | -44.15004 | 2025-10-07 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3acaebb6-7533-3417-bf60-fb1730b3516a | -6.70096 | -42.85637 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9dd6d64e-6c83-3ca7-8f31-2f8734704f52 | -5.25345 | -46.48833 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 589148ee-33cd-30ac-a608-9df292564034 | -6.49352 | -43.64238 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18bf5417-cab2-3fdb-9733-daf4e51a19d4 | -5.57685 | -43.57141 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ffdbf3f2-c459-344c-b814-ba60348f2a2b | -9.18827 | -47.83924 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5a92069-acb5-34d5-9705-c58ea1210224 | -5.66717 | -44.2636 | 2025-10-07 04:36:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eab2387f-11a5-32e3-b506-dd306f2d6e28 | -9.96627 | -43.7868 | 2025-10-07 04:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 92d1d2cf-786b-3b23-8a91-d3402ad29c63 | -5.71465 | -44.83511 | 2025-10-07 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0b3da39e-3e59-39db-bd73-ab843fd42205 | -10.22674 | -48.18369 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b99d11c-03ae-3719-b731-102434bfb681 | -6.13683 | -42.67103 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b939336-184e-3de4-887a-de1d7d1bf286 | -7.02214 | -42.7537 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c585064c-bef3-3fe1-806c-74ffccd41754 | -5.16901 | -50.64891 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 241c6f93-b52e-3067-af01-6aa0faf69d60 | -8.20336 | -44.19808 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82a582a6-796a-35f6-9c87-68e9bce73583 | -6.69933 | -42.19078 | 2025-10-07 04:36:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cfe90e14-fac3-390f-b410-1522965aa1a5 | -9.04513 | -50.69437 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00df0997-148c-39fd-a29e-3739dd9b6d03 | -10.21727 | -48.17863 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 419f7139-eb57-3eff-b56c-d6687671c96b | -6.37562 | -46.42819 | 2025-10-07 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89eedf7c-b5b9-3c10-817e-5a330f43df05 | -6.73775 | -48.17493 | 2025-10-07 04:36:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d95704dd-bcd3-312e-aaa2-72e44ce0c3c7 | -8.54411 | -46.24437 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 81c617b7-8e1a-33f0-9f4e-ee1a05410f3f | -5.67086 | -44.26415 | 2025-10-07 04:36:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49dc6737-62c2-3edc-9e9c-9704aecbac2e | -10.18214 | -45.53419 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7ccec0e-4066-3588-8464-3653985b41e5 | -7.69841 | -42.41012 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e0e30cd5-16b1-3521-a77d-50727ba0907e | -5.48828 | -43.07902 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf1b1fa9-f117-37f7-8fba-530d51904517 | -8.54758 | -46.24491 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8647df25-65fe-30ce-91d9-d148940cc30a | -4.56744 | -55.96129 | 2025-10-07 04:36:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a25e2d85-eb4c-3a42-a3c1-238f79990e21 | -5.4134 | -42.66278 | 2025-10-07 04:36:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 630a869a-2fd4-3572-929a-fce91565105c | -6.38052 | -43.29716 | 2025-10-07 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 556f0834-1f40-3e06-8678-cfa72e22e5f5 | -8.86971 | -46.78834 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d2a580e7-57a4-384a-81c6-620520b44da5 | -8.88101 | -47.66413 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fbb6145-1b1c-3377-9154-a8bad4223169 | -8.61383 | -44.90763 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ec2cb58-8c12-3bf2-80e8-d418ea91ba85 | -7.68588 | -42.41362 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 82007848-02ec-3f89-a151-847dac48cbe8 | -8.87085 | -46.78099 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c194fe62-50cd-304c-a0ca-ba8478b582b2 | -8.56955 | -46.24048 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25dc193c-8d5d-3a71-bdfb-15215168a02d | -8.48363 | -46.30605 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 660e4344-f4ac-3f72-8fa8-2f656cebc0ba | -9.18603 | -47.83164 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 11ff5ddd-c9a1-311b-9de2-171c94862317 | -8.50151 | -49.13091 | 2025-10-07 04:36:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f01da32-2173-35c4-b903-be4d32be5789 | -5.41508 | -41.07763 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0443bd37-4a60-3a72-9045-49614ff30cb6 | -10.60965 | -44.34403 | 2025-10-07 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37234053-0514-3aa8-817a-1be98c27c524 | -9.1972 | -47.8479 | 2025-10-07 04:36:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b135a653-1745-37b0-ac4c-2c7690746514 | -6.53295 | -55.04183 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cddb3821-1b5c-37ae-8754-9cd26e658068 | -9.57559 | -50.80404 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6797a8a6-86f1-371f-b0b5-487e96c25cac | -5.73926 | -49.13197 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b247673d-93f7-33b0-822f-3198335e0b7d | -6.70047 | -42.8597 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b3340749-4058-35b6-b30f-13345d0c5582 | -8.10657 | -55.07779 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 285043d7-55c1-31e3-9913-2bb7c758f561 | -7.68278 | -42.4051 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c88b7e96-de1d-3d96-94f8-04dd156e7c42 | -9.89801 | -49.9677 | 2025-10-07 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13bceb6c-ddf4-3d09-b285-575c5eb691da | -7.00485 | -42.84447 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fd96c75-a30e-37a6-9fd7-d56f5efed075 | -3.67713 | -55.5737 | 2025-10-07 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08bc2326-7961-36f8-9f9e-1754b944bfd1 | -10.15886 | -45.41882 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f1fa7e8-4d27-3ca1-bf5e-e37fb8a88cb1 | -8.66506 | -46.27793 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94471b99-1106-3cbc-8a7a-eb8e5d489d7c | -8.49339 | -46.33469 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3912b722-734b-3383-a593-fd24bdd7a383 | -8.85855 | -46.0894 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 619d8fe6-2ad4-3010-b65b-5d44204044af | -6.97338 | -41.99641 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README52.md)
