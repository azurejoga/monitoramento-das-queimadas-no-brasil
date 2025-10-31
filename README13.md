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
| bc3ed237-6deb-3372-8756-75e6a46f6d17 | -5.70739 | -44.53109 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5895396e-59f6-317b-b6f1-5f92d25d8d2f | -13.43033 | -47.36016 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b6c818a-422b-3a72-8b16-3ad06b39cc0b | -14.12368 | -44.18732 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bca9756-2228-37cc-bbd6-1698d08421d4 | -5.2617 | -45.51688 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43db30f3-d677-375b-b63c-9f162097aca4 | -9.52633 | -47.26963 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb7eb076-700e-37aa-88a5-2c0f66b8fcf9 | -7.08251 | -44.93452 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e417ee97-1a16-33b7-8b77-94648423cfed | -10.64241 | -45.24926 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c312404e-41b8-3cc2-8f0f-1b9a772cbbf7 | -10.53475 | -45.04623 | 2025-10-31 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40dabb6c-9ca8-3ab2-8930-e681eb6d2ee5 | -6.00918 | -41.97356 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 831548ff-1e9b-3a29-aa6a-9c199461ac82 | -9.31934 | -43.09178 | 2025-10-31 03:47:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a32b4d83-80f1-3ff3-b773-790968158c40 | -4.94274 | -44.92567 | 2025-10-31 03:47:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5bbe5e4-07c6-3236-b2fa-738376fd0e78 | -5.85533 | -39.51294 | 2025-10-31 03:47:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 806585a0-beea-3dae-871c-69461a8bce96 | -16.37063 | -45.24751 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 199ac1d1-6e35-321b-9e94-a657bb5b954a | -7.22127 | -44.32154 | 2025-10-31 03:47:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb4ba36d-698d-34dd-acb8-c283dac5acb6 | -7.08376 | -44.92743 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14652fa5-6a56-3447-95b3-249cd2030ef3 | -13.67843 | -44.71236 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faa69266-a1db-34fb-9ef6-7ae0048db6d2 | -13.68223 | -44.71864 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9be4b1f8-6546-37d3-a712-043b9a2f8f6d | -5.5439 | -48.38438 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc161408-201e-3c7c-858a-b86533766ddb | -7.08128 | -44.94155 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e3e5f1ec-46fa-3e9c-9958-1a8b0d0e4b88 | -6.36805 | -40.96974 | 2025-10-31 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e53eafa-92fb-30f4-a0fd-8a5eb15844d5 | -4.9434 | -44.92199 | 2025-10-31 03:47:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d346df2a-3fa5-38d0-854b-26c046485933 | -11.3506 | -42.2602 | 2025-10-31 03:47:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4595726d-c37a-30be-9c4f-5f0898d133e0 | -9.88389 | -44.86568 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f5c223f-f0c4-398d-bfe3-0c155795c923 | -12.93237 | -47.93318 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| daf9b1b6-5836-3788-a344-8aedc28179a8 | -13.93964 | -44.04145 | 2025-10-31 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f9e1489-000a-37d1-86a8-33fed733da2f | -10.25041 | -44.59721 | 2025-10-31 03:47:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 31f5958a-4110-32bb-8f9e-f7da9963fd19 | -7.75562 | -38.46966 | 2025-10-31 03:47:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9d3a2ae8-ae45-3683-93dd-4f9698119204 | -9.93034 | -44.90529 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e290f0c-c645-35ad-8558-3447de201142 | -4.13036 | -43.98288 | 2025-10-31 03:47:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a529013-e8bb-3a4b-be1d-d3f5929387dd | -5.80465 | -40.82534 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 25dc6f9a-84ec-364a-9330-3e6ea22219f4 | -4.79296 | -46.46949 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54283964-4a5e-3a43-bd22-db8d823fb294 | -13.80245 | -47.06339 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e566f58a-5505-373c-ba1b-368d11f2a368 | -11.35819 | -42.29119 | 2025-10-31 03:47:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 290065ff-87af-3755-9eb1-b70764419770 | -10.9543 | -44.17379 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c987f2f-4419-396c-92c9-c4adecd39868 | -4.70669 | -46.49867 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32dabbe0-6519-3ffa-a65d-87776be3b92e | -5.64337 | -41.08821 | 2025-10-31 03:47:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a0d385fe-c813-3177-aa8a-c87e95083092 | -9.89329 | -47.45901 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7e3593-83dc-3b0b-9b5a-8f16345249d7 | -3.52958 | -47.54761 | 2025-10-31 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f143b7d-f3f5-31a3-b13c-597522bd816f | -8.16115 | -45.50482 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18a1dcfe-0faf-3d9a-96b0-c187d20982ed | -9.86132 | -44.87154 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f266574b-fb33-3318-bc89-b8e08d056829 | -4.47989 | -46.57442 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57b04985-697f-3107-a1c9-f31d0b0736cb | -5.36566 | -45.52399 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| daf6d565-0cd8-355b-99bf-6adeec8004a7 | -4.4264 | -43.71422 | 2025-10-31 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9562082e-8046-3ac5-85f7-a93be2c8f0dc | -6.21383 | -43.93929 | 2025-10-31 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97b9267c-8eac-3974-a3c7-48c9babd42c4 | -4.67565 | -46.52713 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9c0380-bf31-311d-8b68-748a360107e2 | -13.8956 | -47.33973 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc520fb2-93ec-3e39-8a98-bd4e6c490062 | -12.84144 | -43.47438 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33c762d2-53c6-360b-bf71-d3f91cdcf11a | -11.65093 | -43.90983 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 258968b4-a367-387a-8d8a-ec647f2a08b9 | -12.20467 | -42.91954 | 2025-10-31 03:49:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c806c03b-b152-368c-880c-781ed9a7c874 | -12.80564 | -43.48386 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b67c93e-d454-3cb9-8c7e-93be8e7dfea7 | -12.29539 | -43.18992 | 2025-10-31 03:49:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfd865da-b943-379b-9552-ab9c693955fe | -12.1069 | -47.12418 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29c8be06-a6be-3cea-ae96-11f526039278 | -13.60261 | -41.07821 | 2025-10-31 03:49:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85100666-2f3c-3079-a04c-a5f92b71540b | -12.50175 | -43.95915 | 2025-10-31 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff84a122-e5c1-34b7-91a0-7a64cf9cadc9 | -12.84207 | -43.46251 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cef70937-7d60-3be3-a3b2-661b71014f11 | -11.81427 | -42.8352 | 2025-10-31 03:49:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0661f08c-9da4-33ea-a07f-a18c7639c950 | -12.1373 | -47.15287 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d086bb1-92a3-3ccd-aef0-5b77229a5722 | -11.02796 | -45.49221 | 2025-10-31 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd713c54-052b-39f5-bc24-f0288fc40af9 | -12.06431 | -47.33935 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f2a8587-fdde-3701-82dc-75ab8cfdecf2 | -12.11423 | -47.11742 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8212c529-cad4-339c-80b3-281194acabea | -11.87838 | -45.3291 | 2025-10-31 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37417c81-4735-347d-8dce-aa291e3e02c7 | -12.06345 | -47.34364 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98ede2a4-b1a9-3e25-b30a-b2ee7fef9c3a | -12.8003 | -43.48759 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a641b7-f231-37c7-87c6-97b012855a67 | -12.10851 | -47.11601 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6879bb67-d333-3dce-9ee7-d70325b5e08a | -12.58314 | -43.36528 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fed92b82-ce88-3a54-91e1-23948bb96233 | -12.82811 | -43.48821 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 916b104b-3757-3b31-84e0-718551fec841 | -12.56667 | -43.95931 | 2025-10-31 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e23f385-bdf1-38ec-ab0c-b97679161f47 | -12.92062 | -45.04724 | 2025-10-31 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c78fdad-fa5c-3be3-89d9-14bceddc4c10 | -12.1365 | -47.15701 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b99539b-3105-3b7a-ac6e-9a348cb4df7c | -12.29293 | -43.78826 | 2025-10-31 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f1771fd-8201-3eb7-ac42-21aee18af601 | -12.72572 | -43.00757 | 2025-10-31 03:49:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 102e4598-05b7-30cf-9a62-339f78571e6d | -12.5365 | -47.54745 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4ccd45c-5d08-3ce2-9f8c-cb9261208ae7 | -11.12817 | -45.16056 | 2025-10-31 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14d3e436-eee1-331f-9b7c-750767368ed9 | -12.12891 | -47.1629 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 546be188-01fd-394b-b427-417772265291 | -13.03582 | -40.51188 | 2025-10-31 03:49:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1dec6ee8-2aff-30ae-9d1e-2886a86099f9 | -12.13071 | -47.15586 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13fee65c-b1ba-3913-8f78-bb63c4a38c1b | -12.12975 | -47.15878 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0058d6a-61eb-33a6-b2f4-30bfe91042a5 | -12.39738 | -46.83246 | 2025-10-31 03:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59a8194f-60d5-3716-b186-184dc0e4e6fa | -10.54264 | -48.71309 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0671063b-07d5-3e59-ac34-5d7d140ae8e3 | -11.71832 | -43.91928 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76c0d908-8f5f-38fc-b6b6-c317c4d76a0c | -13.60485 | -41.07676 | 2025-10-31 03:49:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 917da4cd-abf1-34bf-abbd-d620f7416158 | -13.66887 | -43.0799 | 2025-10-31 03:49:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e7019e46-c2f2-3a4b-afa3-962c9b747b0c | -11.12879 | -45.15735 | 2025-10-31 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be9b9ce5-0ede-3c00-bf7f-9a267b57f015 | -12.60431 | -47.53173 | 2025-10-31 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29184018-88ca-33a8-b691-cd630c5f32ec | -12.11504 | -47.11332 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e033aea-9c43-34be-99e5-bbf2da1e000b | -12.13058 | -47.15469 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08069a08-ac9d-3394-a740-f0f4b1b3688b | -12.15768 | -45.22062 | 2025-10-31 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b03e99b-3f03-3204-9ac1-6b40f214cf4a | -12.5353 | -44.88149 | 2025-10-31 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee855722-df30-390e-81fa-a87db63b4eb8 | -12.84316 | -43.46526 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96f690c2-c3c8-34a7-ad14-c768a6739900 | -12.29383 | -43.78344 | 2025-10-31 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3340a618-5eae-30f2-9a36-023084d77c7f | -11.50674 | -43.2574 | 2025-10-31 03:49:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f2cca521-3d28-3253-8a28-e7ff38fdc403 | -12.84372 | -43.45337 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2a49402b-178a-395f-89ea-5f49f27a7132 | -12.84574 | -43.45157 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 344622fa-70de-34c8-bd0b-43a46d6acec6 | -10.53609 | -48.71188 | 2025-10-31 03:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8875254c-121e-3516-b67e-3bc952ee3788 | -12.80479 | -43.48846 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d124030-57d8-3fef-81fc-3484c0880d0f | -12.84124 | -43.46708 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 001dfdb1-5b28-3428-8b9e-6afd052ed30a | -12.10772 | -47.12003 | 2025-10-31 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e1e5f85-7832-3459-bdd5-35fcf5d47701 | -12.83959 | -43.47623 | 2025-10-31 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f11eefc-6a0a-36c1-bd55-16e036e49e29 | -11.12787 | -45.16066 | 2025-10-31 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ca25db4-01fd-3f10-91fb-60f282b784af | -11.71927 | -43.91418 | 2025-10-31 03:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
