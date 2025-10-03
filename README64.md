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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8a076b7-bf81-31ba-860f-5fabb1beea9d | -11.1218 | -43.38454 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 756fec8a-27c9-39ee-9641-d81ad75bcdcc | -9.92622 | -43.72823 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd2ed4b9-c309-337a-8b5c-8432bcc5c97d | -9.8804 | -47.81647 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f55c28a5-2088-39ca-b8e1-969095e78a3c | -12.80251 | -46.87607 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b436fa98-2272-38a8-914e-86d85c93ada2 | -9.71303 | -48.95022 | 2025-10-03 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 797c2702-3704-3807-90e1-d816ab6644c9 | -9.9507 | -43.57612 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e750f9c7-67ee-39f6-ad65-affa618bad40 | -13.19487 | -47.79501 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d461d78-eede-32e5-80e3-1dde89a50c11 | -11.44524 | -43.49955 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 403d507e-9833-369a-9d09-edc5d7fb372c | -10.92631 | -46.71862 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 745d79e7-81d5-3beb-83db-f0b9c7a52795 | -13.13453 | -47.89106 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| e140515f-87be-3519-98d9-654be1264003 | -12.75629 | -44.91122 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 97172b9e-cb16-3e8f-a66d-d5f37aac3d8e | -9.90592 | -43.72488 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1951c723-bebe-359f-9c57-5fbd5280e1e5 | -10.10248 | -50.34951 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ca8a45d-e22d-3ed4-9df4-45c7adf9df4f | -13.31335 | -47.57935 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 291d9622-50f9-336a-adc2-549e39cd3aba | -12.36783 | -46.52215 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47166ce0-6673-3c0a-8ada-70ea71e53079 | -11.44189 | -43.499 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a334d06-e990-30c9-84bf-4dec595f8186 | -10.81496 | -47.9697 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6742af39-854b-3393-aad9-0df43f9570ed | -11.90146 | -46.30088 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9cb476d-5586-3851-b97c-3dcfe35132f3 | -11.14402 | -43.39571 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7ea3df6f-a108-308d-aa29-f82874690fea | -8.79736 | -46.67388 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71ec657b-ad7d-329c-b13a-a4226309fc03 | -9.9296 | -43.72879 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c332f18-c030-3863-b964-3509a3eed6f9 | -9.91387 | -43.71869 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a429b7e-b690-3007-b721-ad76fdea702a | -13.96548 | -48.10743 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf23540b-862c-34cc-a9b4-157e20066bb1 | -10.85545 | -47.25119 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01f3f239-8fc8-33d3-bf5c-f899568ace03 | -13.30846 | -47.58213 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32a82786-10eb-35ad-a8a1-a1136688bff2 | -10.28042 | -44.32774 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 258d1104-1f23-3424-b9cd-5cf5e64e87b5 | -11.80945 | -45.03046 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71405601-aa08-363a-9a8e-63ee8e6714c6 | -10.94396 | -46.70708 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6cfae605-e629-31a1-8afc-551c37945144 | -11.91015 | -46.26543 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a04c5f89-70dd-3609-a5c6-f29d51650f66 | -12.77968 | -44.91921 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 673bd8db-85da-3cd2-bf50-56afebeae293 | -12.91261 | -47.15904 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16c23f25-0ec7-3c17-b5f0-c7c7563befcd | -10.01452 | -48.50297 | 2025-10-03 04:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95faf39f-aecf-388f-8dde-9b96f7e122bd | -9.32455 | -45.66986 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e93fe9e7-f300-32f3-a548-2fd96ccb03e0 | -10.83937 | -46.59446 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6b92d64-f609-391e-9628-7fe628046fce | -12.62574 | -46.95853 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9668618e-dab6-3942-ada7-319b99ebefa3 | -9.95557 | -43.70334 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ac8fb91-388a-3a20-92d1-e1c45b8f3207 | -13.3402 | -48.12676 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d47bd477-cf7a-38c6-b596-3c00bdc8f9dd | -13.33023 | -47.59676 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3a26222-f025-3c91-89ff-d72b31792fa4 | -14.1891 | -46.6867 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51efc305-49e2-3b2e-a179-ebb41a052220 | -12.90363 | -46.89707 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0578cd9f-6496-367e-a277-2150111a8d1a | -13.75253 | -48.07343 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2ac6e436-bceb-3175-8236-5d29f64b0580 | -11.43855 | -43.49844 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a3dfd03-adf2-3619-8a42-88cfc2ec817b | -12.11329 | -43.44812 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd3d772c-8438-3d61-8f36-b0bf56c797c1 | -8.90872 | -46.61102 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 991eb0f7-10e5-34ad-a2bc-4d4c845294c6 | -13.1633 | -47.90379 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cea6715e-630c-3111-8b37-7132431d8c04 | -13.76344 | -48.08125 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 092afd9c-2f28-3f8a-a082-b95dc760bdcf | -14.19132 | -46.67366 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b64117d-30f8-3c85-a7d5-ba3f13771e0f | -9.17234 | -46.539 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31457b1e-c6b0-3dc6-9ea1-a9d3a3723516 | -14.20007 | -47.01087 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51915360-dbe5-3f65-8f9d-e4e377284608 | -10.85055 | -46.62067 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e14dea1-c3d2-3c28-9277-9c2b0eb47b0b | -11.49363 | -44.99808 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 346d363d-e646-3a61-a09b-eb8ef18d7f83 | -13.97064 | -48.12399 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d1efc3a-67ed-3785-a342-1ac5e6df409a | -11.09825 | -47.86804 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 789bb5c7-bdc7-365d-b67d-36b78ad9bab5 | -10.92932 | -46.72398 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4b832365-e23e-324e-978a-b2852ca1140e | -13.26452 | -47.26677 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40e25c2c-7ad4-302f-8c44-1668513e7bcc | -8.6498 | -47.71038 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cbcd8118-15a4-36a9-a17c-5242be236db4 | -12.60979 | -46.96085 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f7b5765c-7ace-351f-8721-3c5e84fa048b | -8.69288 | -47.68627 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91b9eacf-a9a1-329f-b208-74750a03b2e3 | -11.91451 | -46.262 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 072e1b77-17ad-3c8c-858f-7fa5e1359483 | -9.47815 | -47.86839 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1a5a44f-0439-3244-9352-afdd5fedc6d2 | -10.06743 | -48.18306 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dcaf567-09c8-3861-ae9e-dd729d08b412 | -14.21684 | -44.95429 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55b68532-1da9-3025-b478-402014d7aa04 | -10.301 | -48.28413 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c57e2648-94ff-34b8-b8bf-0a0126f49585 | -13.75643 | -48.08704 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e918e69-2c05-369f-8a45-d7b031fcb09e | -12.71708 | -48.57538 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e97d9c58-8f44-3f54-b887-fef7e42619a3 | -11.53458 | -43.55452 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 879c0ebf-10fe-3f95-affb-6217d4a64ebc | -11.74187 | -44.4279 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b87baf54-5d32-39eb-a252-4bf5131c7115 | -13.1267 | -47.84248 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8de781de-0b12-3d27-b271-cb00ea50b290 | -14.46129 | -48.40398 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd3b49ef-287d-313b-a704-c491d9ac0827 | -13.15344 | -47.89046 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7abea08-3645-3d20-a265-d5323b20d85b | -11.45212 | -44.96041 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17d05786-1c37-30f5-901c-c6ef1990651d | -9.95191 | -48.78038 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87ba2a97-069c-3d51-a627-9ea2eedb2da2 | -12.90809 | -46.9158 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c6ede71-ad50-3833-92e6-81651dcfad23 | -10.92529 | -46.74766 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b18c5e4-ac5e-3329-a76c-cb86ba6b0bb4 | -12.61086 | -46.99988 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b4ef1c3-79fb-38bb-9dbd-32f371591db2 | -11.13677 | -43.39814 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb464a5a-8df3-3bf4-b219-0a2716f557b2 | -11.50134 | -43.50508 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fa47602-d909-3120-b93e-323b187397c2 | -11.86847 | -45.04078 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eca807a7-ee8f-396e-a898-94dfb9dc833b | -13.23789 | -47.3504 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b7064fb-3c1b-3512-ac79-a82d21569288 | -12.67725 | -48.57801 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c330b6d-ee59-3003-8566-313cbfff9c5b | -12.64179 | -46.99842 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f4f8b73-2910-3326-a7c5-e214923180b7 | -13.21642 | -47.83376 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d04892db-1279-3498-96e2-20951b741b6d | -11.08165 | -47.70507 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79905e1f-5df9-357d-9b99-658c9601cc23 | -11.13965 | -47.18304 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 630bc1ba-f2eb-3f5e-bd8b-9fa02eec20b6 | -10.75769 | -45.34046 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 216aa87f-1125-3b98-a686-eabf67ade5d6 | -12.93811 | -46.37503 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fb3f137-5381-3313-8a4a-1bdb9c8a35e6 | -11.41905 | -43.49157 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa1cf2d9-e7d6-33ec-ac7f-abb0b3ebbc60 | -12.94687 | -46.38974 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 221b7688-fe66-36e1-b08a-4d9442036746 | -9.92511 | -43.62755 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 268c8fec-aa1c-3a62-91e5-45a0a658b77b | -12.807 | -46.87242 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc00cfa6-73b3-3a75-9c17-9cd317475adc | -10.92089 | -46.72738 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f264f37-9bd0-3dca-b337-a7fac99d1d72 | -10.8606 | -47.22097 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dac9f2b-a375-3974-904c-1f664ab1a364 | -11.79575 | -41.19383 | 2025-10-03 04:12:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eee93286-e9f5-344d-9df1-74e044882e3b | -11.72581 | -44.44047 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5a1b5aa-5120-3bea-911a-8d61d8a694d9 | -13.77889 | -47.57938 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 218e0055-ccff-375f-88f0-586141c1a9cd | -13.29492 | -46.9815 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4188b8c9-8da8-3440-b60b-c837e50cc5af | -11.55813 | -46.99512 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da38b08e-654d-31d8-b96c-eedf6961494f | -12.93102 | -48.4388 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3752f261-b87d-3d48-abec-9c6e2dcd69f3 | -12.8592 | -46.99648 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e77c8187-04ad-3704-a46b-c1132e1a4974 | -12.90966 | -46.36584 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
