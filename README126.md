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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e81757-e7c5-3ff9-a20a-7af53c019a73 | -5.8569 | -42.3407 | 2025-10-17 14:10:00 | GOES-19 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| aa5bfbc0-ccb4-3c0d-9310-dabba79a4744 | -5.9251 | -43.0662 | 2025-10-17 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 123.6 |
| 4a30aa26-44d5-361a-b846-4c525567c0cd | -6.4066 | -41.8882 | 2025-10-17 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| cf3229c4-c478-34aa-9249-903dd1b9292b | -11.5724 | -44.0736 | 2025-10-17 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 440395ab-ff7c-3414-a613-5145b7a08ebe | -13.0483 | -47.3356 | 2025-10-17 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 2e9e2ac1-489f-3247-88f9-74c2be9cf1fd | -12.4678 | -45.4694 | 2025-10-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| c0dca864-6e21-337d-95a3-8f9b64f34626 | -11.5921 | -44.0472 | 2025-10-17 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 5755d643-3965-3cc6-a6e2-2766727b1a20 | -14.0905 | -43.6235 | 2025-10-17 14:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 80b01299-3226-3a51-bfc2-2049cecd1e3b | -3.9822 | -42.4924 | 2025-10-17 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| 999362b9-185c-3778-9cdc-0b3599f73028 | -12.0879 | -47.4277 | 2025-10-17 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c98ea36c-f4cf-3810-8025-98df5918f918 | -12.1678 | -45.0771 | 2025-10-17 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 412957fc-b5bb-36cb-82ef-c85fa8e88974 | -6.8419 | -41.7032 | 2025-10-17 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| e1267272-139a-3ce8-8238-7a897b02aaa4 | -6.3878 | -41.8899 | 2025-10-17 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| db7be94c-e95e-344f-8fa0-b8a941d5f6df | -11.3992 | -44.1229 | 2025-10-17 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 86e69444-d465-3b50-be2b-60466c869455 | -10.938 | -45.4146 | 2025-10-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| ca69857d-afb1-3e42-b688-0f1b8ee753db | -6.3919 | -41.5052 | 2025-10-17 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 596e50d1-a501-37b8-89ce-962a6a705f28 | -6.4107 | -41.5035 | 2025-10-17 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| edb20e86-7356-31ee-beec-ec0158126336 | -6.3921 | -41.4811 | 2025-10-17 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 1c08c2b4-2159-3b34-85aa-3148a8205e37 | -11.3988 | -44.1464 | 2025-10-17 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 0e341c9a-10b6-36c4-b52e-445feca1bac9 | -10.8987 | -47.9134 | 2025-10-17 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| bb3b448e-390e-3d74-a5cb-e838237a8c99 | -12.9175 | -47.1303 | 2025-10-17 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f6484255-e913-341a-97b6-623011927071 | -10.534 | -49.5471 | 2025-10-17 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| dffb7123-b622-31a7-aa18-b788146e4def | -12.5059 | -45.4866 | 2025-10-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 364.7 |
| 1fe3f550-602d-3790-9667-02874c05623f | -6.2012 | -41.7389 | 2025-10-17 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 9ac4e755-ad43-3e7f-a473-a7890512a764 | -3.7626 | -41.7207 | 2025-10-17 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 05b7047d-a7c9-3286-ad3f-748a36d72578 | -5.799 | -42.5112 | 2025-10-17 14:10:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 3d15f2c0-fcb0-3850-88ef-7981a01b3443 | -10.3126 | -44.043 | 2025-10-17 14:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 56c529e2-ed18-3603-bb83-8f9e37fb776d | -14.8854 | -52.4167 | 2025-10-17 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f4b30076-d6f8-378e-b22f-55f8e8072b27 | -6.4448 | -41.8368 | 2025-10-17 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 0a5f1f40-c603-31a3-94f4-e26022832ae3 | -13.9127 | -45.5808 | 2025-10-17 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 3cb92b69-0663-3e66-9863-4682597d0b11 | -12.9259 | -41.8363 | 2025-10-17 14:10:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 179.4 |
| 01ea65da-8831-3ce8-99e4-f0759570f607 | -5.4561 | -41.0054 | 2025-10-17 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 148.9 |
| b99f7bd6-07e9-3457-b4d9-6e6c43c62b34 | -10.2939 | -44.0221 | 2025-10-17 14:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 446.4 |
| 7b5c6915-a6ee-3f0b-97be-689b787ae036 | -11.0214 | -47.3443 | 2025-10-17 14:10:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e0917942-e057-3eec-82e7-db1a179ba209 | -10.1063 | -47.6525 | 2025-10-17 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 798d88ff-ccac-3aa6-9e7c-fb966aeeaaa6 | -5.7992 | -42.4876 | 2025-10-17 14:10:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 0826c3ba-9780-3d6c-b8ee-89817c9c3051 | -10.8101 | -43.9275 | 2025-10-17 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| baaec233-33d8-37e2-8e9b-6dbae13e3c0e | -11.083 | -45.8742 | 2025-10-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ac18baf6-e470-314d-973f-490ce01460fc | -10.5136 | -43.4052 | 2025-10-17 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4d50b57a-457c-3c91-af23-71f6b984d66d | -9.898 | -47.6758 | 2025-10-17 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 23b2460d-b2b1-3c1f-8f02-62bfe3e00794 | -6.6816 | -40.8714 | 2025-10-17 14:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 922d0223-8463-39ac-a047-9094fce1296c | -3.9635 | -42.4934 | 2025-10-17 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 134.7 |
| 84673f03-c3fc-3d80-9259-a3fddf2eedd3 | -6.4064 | -41.9122 | 2025-10-17 14:10:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 7f007cc3-d168-3d2e-9e28-399152d692ab | -10.6028 | -47.3955 | 2025-10-17 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 0a83c82b-d5f1-3553-9ff2-c558872070be | -12.1682 | -45.0539 | 2025-10-17 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c292aea3-e306-3de3-8c3d-95d374aa8ca6 | -14.1754 | -47.9252 | 2025-10-17 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e8b52b31-f30a-3360-b167-ce8a870f7625 | -5.839 | -42.2472 | 2025-10-17 14:10:00 | GOES-19 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| b8d5b31b-a6af-32ec-855a-ce1466b49030 | -10.9189 | -45.4171 | 2025-10-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f5fb592f-1266-3ac0-ac8d-550413b27fcd | -12.9607 | -47.9294 | 2025-10-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a40b5716-20c5-3a71-be1e-0b5092c7c3c1 | -10.6214 | -47.4155 | 2025-10-17 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 43783313-c333-3093-86cc-0a92b87119f7 | -12.9265 | -41.8118 | 2025-10-17 14:10:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 219.7 |
| 337bc887-d69c-353d-8ccd-f722a27bbc18 | -12.9065 | -41.8399 | 2025-10-17 14:10:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 313746ef-c795-3f2b-8de1-219ecfd3b11c | -11.1419 | -55.1869 | 2025-10-17 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9cfa145e-cc75-3afd-a726-8bcf343b1125 | -12.9459 | -41.8082 | 2025-10-17 14:10:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 96.1 |
| a6c0540f-46cd-3507-8787-e7e2e8d71396 | -10.4945 | -43.4079 | 2025-10-17 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ef5a3038-3a45-32db-acf4-53c4375c0c25 | -6.201 | -41.7629 | 2025-10-17 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| a7828bf9-f357-392c-8eb3-f46f8d41b73c | -10.2558 | -44.0273 | 2025-10-17 14:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 7bf318c3-3cba-32e2-963d-73d210957b75 | -10.9938 | -47.9019 | 2025-10-17 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 98a05f8d-d42f-3ae7-8b07-46d3d6d43a4b | -6.2198 | -41.7612 | 2025-10-17 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 05264d34-f009-3cfb-93f6-83d0f02989d8 | -10.514 | -43.3815 | 2025-10-17 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 83be601c-f890-373f-9f64-719b80a684bc | -11.1419 | -55.1869 | 2025-10-17 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ebb3fa94-aa68-3df8-be54-07cc46ebfb43 | -9.898 | -47.6758 | 2025-10-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 13145b5b-8023-38f0-a6de-fe2e18fdebda | -12.4866 | -45.4895 | 2025-10-17 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f5a67f99-28f2-3315-a30b-f85122091c8a | 3.7512 | -59.9924 | 2025-10-17 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0b784730-8f66-3a86-aa57-305c2b4c2513 | -12.9265 | -41.8118 | 2025-10-17 14:20:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 203.2 |
| c81a26d2-0f8f-3f16-8496-0dee392015cf | -9.7155 | -44.5612 | 2025-10-17 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| db7786f0-9cd6-312e-9239-3d140cc790f6 | -6.4064 | -41.9122 | 2025-10-17 14:20:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| bb1e23a5-4fdf-37ed-a6f8-aa4b66b25eda | -13.4412 | -47.9483 | 2025-10-17 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 7c2710c3-3b21-39ac-946f-68dd6c3e89fa | -10.5132 | -43.4289 | 2025-10-17 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| c280f3a0-f025-3d11-83a3-f204d2964a1c | -14.1754 | -47.9252 | 2025-10-17 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b8831239-7863-3037-b267-05434e9ee5c1 | -11.6274 | -47.5561 | 2025-10-17 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b2b0f992-5432-3c5f-b1cb-ecd9f54f311b | -5.872 | -44.7573 | 2025-10-17 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| d65bc759-1ce9-307b-b110-537f350bd09d | -5.8797 | -43.9075 | 2025-10-17 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 87eeb61b-efb5-3e94-82f3-364713cc43f6 | -11.4193 | -44.0731 | 2025-10-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 1b592f18-4cd6-38ac-b9f1-7614c5f3c7e7 | -3.982 | -42.516 | 2025-10-17 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| dd35f51e-8565-33bf-ade4-fba406ffe41e | -10.534 | -49.5471 | 2025-10-17 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f54a98d9-dbed-3510-95fe-df04def39926 | -10.5337 | -49.5687 | 2025-10-17 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 11c6078d-c8d0-3e13-9fd8-333d40a2e6ee | -5.6987 | -45.337 | 2025-10-17 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e556075f-1c5e-388d-8595-e2a3c42fbd9c | -10.2748 | -44.0247 | 2025-10-17 14:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 30ae4673-f735-3fce-9dae-96c38aeb38ea | -6.3544 | -41.4846 | 2025-10-17 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 7e8fa48d-a56e-3b84-b465-3d3c8604ba28 | -10.5331 | -43.3788 | 2025-10-17 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ea1a45c6-c859-3170-bc39-5f083cf28010 | -12.699 | -48.6299 | 2025-10-17 14:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 44466bd9-a5e9-3251-8bd2-73b254fe6be5 | -10.6726 | -45.3355 | 2025-10-17 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| bdfa57a2-01ca-3aae-a6a8-711c6c74193f | -9.9638 | -47.0256 | 2025-10-17 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 6e68e0d5-7bed-3e65-ae90-6a9d50193f02 | -10.2939 | -44.0221 | 2025-10-17 14:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 401.7 |
| a15f00b3-73f6-31f5-875c-e32be5d5320c | -10.5136 | -43.4052 | 2025-10-17 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 272d1bd9-f2e6-3f8d-ba95-fe96913ab176 | -12.9065 | -41.8399 | 2025-10-17 14:20:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 91.2 |
| bfa2d4ee-8883-397e-9967-bf25615482d5 | -6.823 | -41.705 | 2025-10-17 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 4d67bd1b-4ed2-3be9-9eaa-0ef0de13caf1 | -6.8419 | -41.7032 | 2025-10-17 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| f1348a85-9377-3fb7-9e9a-cdbbf4e3842c | -3.9635 | -42.4934 | 2025-10-17 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 355fc52a-bacb-3bd6-a4ff-108becf1d213 | -11.5921 | -44.0472 | 2025-10-17 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 60055039-b198-35a5-b105-41623f7f7534 | -6.3924 | -41.4569 | 2025-10-17 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 7f94eaae-5de5-3d05-834b-39c918d83444 | -10.9938 | -47.9019 | 2025-10-17 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 68da2b84-297a-39f6-a37b-ea2b3b845686 | -13.4416 | -47.9259 | 2025-10-17 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 6752ab4e-0853-3ae1-8bfc-e9fef0391192 | -9.6389 | -45.9186 | 2025-10-17 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0668a16e-bd32-3c99-b1c5-797b6d14468f | -12.0687 | -47.4303 | 2025-10-17 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 42ddf4e2-07d6-35f6-9fd4-642c7e4ba8b5 | -11.496 | -44.0617 | 2025-10-17 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 93edaabe-8360-3ef5-9980-5818ba9e0c21 | -5.9251 | -43.0662 | 2025-10-17 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| ff3d4dac-dd00-3eca-8aff-cf3700c17620 | -6.4066 | -41.8882 | 2025-10-17 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 20490d8d-da1a-3250-acaa-6c1093511f1f | -4.5917 | -43.5563 | 2025-10-17 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |


[Clique aqui para ver as próximas entradas](README127.md)
