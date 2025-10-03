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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e661dc8-f8e9-3a4b-a3c0-b7b389d2717f | -7.75878 | -42.5667 | 2025-10-03 11:38:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 0c912a48-3ed7-390a-9a5e-099f39859b2f | -9.94044 | -43.57298 | 2025-10-03 11:38:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bb7ab954-ac84-37c9-b9c3-0992f41e1bd1 | -9.584 | -40.33207 | 2025-10-03 11:38:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 015e2464-7229-36a6-b493-1659e7d16d9f | -9.27792 | -40.59491 | 2025-10-03 11:38:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.5 |
| f7a81677-51ad-3a7c-8d81-68478a1e8018 | -10.16499 | -45.49081 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4f6a51d6-9a7c-37cd-98aa-8f2dd4b78d8e | -7.29275 | -45.25255 | 2025-10-03 11:38:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 69fb8d71-5f33-377c-a88c-16b95091703a | -6.64489 | -42.78812 | 2025-10-03 11:38:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ea32464a-7ea8-389e-a64f-7810f0932555 | -7.71757 | -40.41142 | 2025-10-03 11:38:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| a791923f-d5c6-3f40-92e3-0f808886a057 | -8.59377 | -44.7723 | 2025-10-03 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f9476bab-1397-3e25-9f69-f093084ae9ac | -12.26143 | -40.25688 | 2025-10-03 11:38:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b3376884-1439-3d6c-a2bf-160fad7380c7 | -8.90228 | -46.60543 | 2025-10-03 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 94f56902-91ae-3acf-a270-5a73529c5b50 | -7.7798 | -42.50645 | 2025-10-03 11:38:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 37.4 |
| be947b41-17ea-3188-b979-1ce1badf6f8e | -10.03131 | -44.00557 | 2025-10-03 11:38:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2d65c005-92f4-3a22-b92d-8f4f56656585 | -11.91805 | -46.3357 | 2025-10-03 11:38:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 5ce326a0-9d26-3b61-ba00-92a75837dc5f | -10.31095 | -42.38833 | 2025-10-03 11:38:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 684e0955-0ff7-3439-b840-3ae59d8d90ed | -10.863 | -47.21862 | 2025-10-03 11:38:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 9563fb6e-0778-33f6-ab3d-c6e4bdbae415 | -11.13082 | -47.88526 | 2025-10-03 11:38:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8e4e7d03-0864-39ca-8cf2-044b8f7d80de | -9.9451 | -43.58067 | 2025-10-03 11:38:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ef59ba5e-dbab-363f-ad31-12cb5c4d59e7 | -11.8603 | -44.96992 | 2025-10-03 11:38:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 21465294-09e7-36a8-9a22-a6e7bcfe96ff | -12.5305 | -47.2988 | 2025-10-03 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ac154137-25de-34bd-9acb-0bbfd1bcec80 | -12.6135 | -46.9499 | 2025-10-03 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 08157494-0937-39af-8975-ea5469051e23 | -8.8343 | -46.7694 | 2025-10-03 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 40718ac5-53b6-3a27-b05d-be6cea2a8c38 | -12.6131 | -46.9725 | 2025-10-03 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| eeba1387-a81d-3314-8cb8-70e2c35f5f58 | -12.6127 | -46.9951 | 2025-10-03 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ea50f56c-07cc-3112-901e-e716ace3a9eb | -9.9962 | -50.2248 | 2025-10-03 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 24d7bf99-e3cc-326c-a29f-0351dbb4b57d | -9.9182 | -43.7212 | 2025-10-03 11:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| d14f2e58-f05f-3b49-a8f9-26409a488c5f | -12.5301 | -47.3213 | 2025-10-03 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a1cd4cc7-ee56-302f-a0cb-5da0b6aab65b | -9.9965 | -50.2034 | 2025-10-03 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 2101d043-1182-36d8-81c7-189d25ea8a7b | -8.8932 | -46.5848 | 2025-10-03 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 039e957e-3beb-33cf-82c7-eb7861ce29e3 | -9.9959 | -50.2462 | 2025-10-03 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 0bac719c-7b88-381e-b7c6-2d2df2a5bcb1 | -12.6319 | -46.9923 | 2025-10-03 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d6eac000-4434-3535-8113-893bae4679e0 | -11.9155 | -46.3272 | 2025-10-03 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 2f7203da-3363-3ae1-8bf6-e5dbb717fc57 | -12.6323 | -46.9697 | 2025-10-03 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 60bc849a-bca9-3be2-8d8d-759882c392e2 | -14.88868 | -46.99 | 2025-10-03 11:40:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 599e4b8f-78e1-33f2-b1e9-f3f52bf263b0 | -12.6204 | -46.96908 | 2025-10-03 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 423af722-d056-374f-8e94-b5d0e623609d | -14.90495 | -46.95927 | 2025-10-03 11:40:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 645db3ac-262b-37d2-80c1-e1f3f26fd0c7 | -12.60623 | -46.96209 | 2025-10-03 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4444b188-b574-3a24-a06f-484920332343 | -13.58274 | -47.58215 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 76088026-1922-38eb-8ab7-c3c8803f82ab | -16.2478 | -44.04995 | 2025-10-03 11:40:00 | TERRA_M-M | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c873b26f-d6b9-38b2-b68f-1bb9e9910a17 | -12.85973 | -42.74802 | 2025-10-03 11:40:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 19a3af6f-a0c3-3aef-8b1e-ba99490acfa8 | -14.8964 | -48.29181 | 2025-10-03 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ad76877c-3456-323f-a359-953322522a24 | -14.74443 | -48.11736 | 2025-10-03 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 18ee328a-3eb3-37e3-948f-05c5e57becf6 | -16.23675 | -44.04803 | 2025-10-03 11:40:00 | TERRA_M-M | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9df6761b-3a82-3b73-ab63-e850a5d29fef | -14.72862 | -48.11595 | 2025-10-03 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| a0ed88f0-422b-3a2a-9e67-c66480f74368 | -12.53007 | -47.31483 | 2025-10-03 11:40:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 23577888-f10e-3306-82bc-4cd0e9d6fde6 | -14.90764 | -46.96658 | 2025-10-03 11:40:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| e3af9b58-3d81-36fa-b05f-7da64f9d2b58 | -13.31132 | -47.57416 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| e46aeca5-c650-3ed4-b9f6-65a49580efb3 | -14.8862 | -46.98257 | 2025-10-03 11:40:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 6289d7e1-691f-38ab-be6a-68fc0c6bba32 | -12.63524 | -46.97189 | 2025-10-03 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| cfce3e48-b8df-356b-98f3-d9d46650348f | -12.94288 | -48.42778 | 2025-10-03 11:40:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 61093336-f402-37c3-9857-7d5e515629c2 | -14.37868 | -45.94988 | 2025-10-03 11:40:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 3d431066-541d-3b0e-b4a5-d78f8207af59 | -13.76817 | -47.57454 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4568fe42-9e53-3695-88ea-e409ceed927d | -14.68809 | -48.0985 | 2025-10-03 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b3d69adb-3f4b-3f34-b896-7f954ade41a6 | -14.68208 | -48.10675 | 2025-10-03 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 24775574-cd0b-3539-a3b6-e95871904a57 | -14.93601 | -46.8904 | 2025-10-03 11:40:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 42ece9f3-1a19-38cc-a600-a1b92065712c | -13.33833 | -47.58232 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 37c84c58-61a0-3992-a689-31d643a383d4 | -14.12506 | -45.66196 | 2025-10-03 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ae57f9d5-ed5d-365c-acc6-3399033f2f02 | -16.03841 | -43.84544 | 2025-10-03 11:40:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0b60252c-6e73-367c-9a82-bd779cfd0a3b | -15.71945 | -46.27243 | 2025-10-03 11:40:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f3f01e2c-0763-3383-a6f2-a86da0db718e | -13.33677 | -48.09697 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 8cd7f63b-02cd-3ee9-9d56-ee7cc2178d70 | -12.60125 | -46.99128 | 2025-10-03 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 5f04e448-66fe-3e08-b8c2-5a92373f782e | -14.29061 | -45.92658 | 2025-10-03 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2b208736-a42d-3f9a-af8d-a0c089961232 | -13.32287 | -47.58008 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b45d066c-001b-390e-b1f0-e92340ddb381 | -12.52651 | -47.32008 | 2025-10-03 11:40:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 18ec9a93-5dbc-37b2-a861-a85c5db79693 | -13.75944 | -48.06341 | 2025-10-03 11:40:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 11ee5ab4-67c8-3d60-860e-3596b852e97e | -13.77427 | -47.54135 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6b517548-9aee-3c99-a419-342dbeaf71e6 | -14.75434 | -48.12711 | 2025-10-03 11:40:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| dd1d59cc-60b1-3e80-aacf-3d147e4d99f0 | -14.29812 | -45.88325 | 2025-10-03 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| cfb35797-cde1-3247-b426-96a750cdbadb | -12.60526 | -46.96792 | 2025-10-03 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2201d985-347a-34f4-ab7c-d8a3feb1a833 | -12.61502 | -46.99949 | 2025-10-03 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 4b50e46d-e325-38ab-a931-be64fa602b02 | -15.53474 | -42.00162 | 2025-10-03 11:40:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| bcf83cde-77eb-3cb4-9908-0a596bd4894e | -13.77154 | -47.56847 | 2025-10-03 11:40:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 00bc5fb8-e341-3d0f-9c70-22d6ade93fbf | -21.06821 | -41.95567 | 2025-10-03 11:42:00 | TERRA_M-M | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| dc588e77-fbda-34c2-b589-61cf15aaedc4 | -20.10022 | -41.81953 | 2025-10-03 11:42:00 | TERRA_M-M | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| cc53202e-385e-35bb-80a3-d1dedee9743f | -21.06973 | -41.94564 | 2025-10-03 11:42:00 | TERRA_M-M | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| b25b6593-5ec3-3818-a6de-0b13089ba845 | -19.96928 | -41.65252 | 2025-10-03 11:42:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5ceacffc-cb04-3132-9759-76964d12675a | -17.6345 | -44.45341 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2d8c04ce-ccba-3724-bad3-14a8e57d6dda | -21.93607 | -42.79095 | 2025-10-03 11:42:00 | TERRA_M-M | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 2cd28db1-2c35-3df2-a606-146141c6a0c9 | -20.8225 | -44.09853 | 2025-10-03 11:42:00 | TERRA_M-M | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| b67d0004-9ba2-37a3-a4a6-f1ec21b1bd7c | -19.97836 | -41.6541 | 2025-10-03 11:42:00 | TERRA_M-M | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a16abdaf-05d3-3078-8df4-310557a92256 | -20.10175 | -41.80961 | 2025-10-03 11:42:00 | TERRA_M-M | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| dacf0e73-411d-3560-bc80-b87722f64cfd | -19.72489 | -44.87191 | 2025-10-03 11:42:00 | TERRA_M-M | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 8620a00c-fc0a-3832-ad94-03db4b0c3dc6 | -17.86107 | -44.68927 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 702588cc-0899-3206-a76b-60ef3ecea57a | -17.63201 | -44.4686 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c78ec997-7f1f-39c9-8009-9b8dd55ecd2c | -17.62346 | -44.45727 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 5f73b419-8e94-345a-ac3d-3543ac1bb9d8 | -20.04597 | -45.75579 | 2025-10-03 11:42:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 239.8 |
| c4b61e93-94ab-3015-8deb-61a7373c3248 | -20.2985 | -41.67109 | 2025-10-03 11:42:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| dca5db48-7961-3f94-b67c-223aa0b47a45 | -17.85946 | -44.69622 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 5397809c-0ee0-3fb0-b519-35c61eafe1ca | -22.79983 | -42.34024 | 2025-10-03 11:42:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6d1e4ede-3468-3247-a28c-6d0a788f720b | -22.77221 | -42.98281 | 2025-10-03 11:42:00 | TERRA_M-M | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5e2d900a-ffa8-329e-8ff0-1d6651620c01 | -17.96982 | -44.38545 | 2025-10-03 11:42:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a93ae080-c494-383f-9dbe-3d22f14a7f3e | -17.62345 | -44.45112 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| e9a01eee-3246-34f1-8a69-1fc0e9e59873 | -17.8584 | -44.70533 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cc4c7a57-6deb-3f79-a0ff-f303c6de0ded | -21.93777 | -42.78008 | 2025-10-03 11:42:00 | TERRA_M-M | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 31082f6d-b602-3456-b99f-a922eeb29513 | -22.82113 | -42.79515 | 2025-10-03 11:42:00 | TERRA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 8ed056b4-5eec-35b3-a77a-3e99c0cc4f64 | -19.4674 | -43.6515 | 2025-10-03 11:42:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 575b1ac7-a7c0-3939-a60b-4ae0c4f90115 | -16.93332 | -43.1315 | 2025-10-03 11:42:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| aa0aa0c4-dc9f-3bc3-9864-9c581e73d2cc | -20.19144 | -45.11554 | 2025-10-03 11:42:00 | TERRA_M-M | SÃO SEBASTIÃO DO OESTE | MINAS GERAIS | Brasil | 3164605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.5 |
| c52e750d-8920-36cb-a6bd-fbddfdbd7eb7 | -20.04786 | -45.14571 | 2025-10-03 11:42:00 | TERRA_M-M | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 141.5 |
| 42f9e24f-bd5e-3767-8b67-763b1e0a7726 | -20.19101 | -45.12217 | 2025-10-03 11:42:00 | TERRA_M-M | SÃO SEBASTIÃO DO OESTE | MINAS GERAIS | Brasil | 3164605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |


[Clique aqui para ver as próximas entradas](README143.md)
