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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c72828b0-4c67-3ace-b27e-cd5c1234843e | -7.86015 | -54.69483 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a2dd8bc-2bf6-338d-8f43-8dc2d28113ee | -10.55924 | -44.60986 | 2026-09-13 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa28e5be-a388-34e2-8921-377e3c8200a7 | -9.68277 | -43.42478 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 238c8549-8f99-3bbf-b9da-788109488fd9 | -11.19692 | -42.7855 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 42ec9d7d-47ba-33d1-a911-65a2bce09d66 | -13.45265 | -48.50604 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f505269-3c1c-3871-b90e-182efc22c188 | -15.91486 | -42.55498 | 2026-09-13 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ead9d4d6-3fe4-312d-b922-37006c462e83 | -8.54207 | -54.70307 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c55c7a9-c80a-3415-b826-d12c976799f8 | -9.88424 | -47.59074 | 2026-09-13 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd279a11-f718-3fcd-8fd1-6fe6a2047f05 | -13.6264 | -47.88408 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cdab35c-71a1-3770-8535-9a2a42814b15 | -13.45939 | -48.48866 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35c4ec03-ee5e-3588-9aeb-0e2ddf8012cd | -16.67454 | -41.85214 | 2026-09-13 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| be19c438-e828-30f7-b568-18393a9afbcc | -9.71012 | -54.36089 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8a8ebb-e4ed-324d-92d8-39eff03c4488 | -9.36932 | -50.09442 | 2026-09-13 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc4961e-d248-3f3f-8b2e-b02fc22e9bfd | -9.78275 | -43.43739 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 761c9c7a-b5e6-3828-a1df-effb25ebcf00 | -10.83476 | -50.59585 | 2026-09-13 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90408ef9-10ac-3e7c-a31c-a0cb243d7fe5 | -12.15968 | -48.96592 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 657342f7-82cb-3099-9fc5-086eb5a2eeea | -11.7204 | -46.7359 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67beac5a-4b41-3d56-9a36-7720f7fe29d2 | -13.4623 | -48.49372 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78687207-5244-3598-bc3a-b1e0c38e452f | -10.50298 | -53.57102 | 2026-09-13 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c282f10-ab7b-3adc-a39c-d15aeeca08a9 | -10.53962 | -45.2286 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4b1070c-56ef-3941-a7c7-7fd34122e1d6 | -11.56704 | -46.98799 | 2026-09-13 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e26b301b-ae43-3ac9-972b-3b62455b57ad | -10.35708 | -46.66641 | 2026-09-13 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d7e024-47f7-3578-8b40-b217d9c2c0c2 | -10.38088 | -45.13324 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf2fd7b3-3b48-33cd-80e1-95641d740b23 | -9.71439 | -54.35859 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 167d1b5c-3a81-352f-8b22-a9323147489d | -13.61365 | -47.89451 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc771e41-5fcc-3ac5-a279-224b0a362310 | -14.27624 | -45.6503 | 2026-09-13 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e458e44-a79b-35bf-b1aa-797362b48a0c | -12.1567 | -48.96027 | 2026-09-13 04:17:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f1a5888-000e-3e8c-9061-49f81a8a3cfa | -13.4667 | -48.4901 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d2e9f10-a391-3b4e-959b-34c177fbc1d2 | -10.91224 | -47.82066 | 2026-09-13 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 991af9eb-5dc8-3395-91a1-d054975bd672 | -13.98459 | -54.07716 | 2026-09-13 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4adde3ef-caf0-3643-9ec2-04b52bac76e2 | -10.62681 | -50.57306 | 2026-09-13 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68a9c342-c310-3b2a-a309-fb9e1ec081ae | -9.61164 | -46.73886 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c07b8ff-de2c-3ae2-961a-3842cc9481e4 | -10.81086 | -48.55165 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01723950-cc32-35f2-b90e-467a666d4040 | -13.60089 | -47.88876 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbe132dd-7366-3155-89d7-b8118489e620 | -10.94939 | -48.3549 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 60072837-2cf8-3a04-a916-a1ebc14cf0a2 | -16.2288 | -40.29646 | 2026-09-13 04:17:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce56dad4-ef83-3d61-8e55-8a5d0b0a9faa | -10.21888 | -45.19111 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15969909-1421-3035-8527-7b7b3ffa6abf | -9.69758 | -43.39479 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8a41193-981a-3e22-b500-2d5ee3be3f62 | -10.47153 | -48.6487 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0ad4ec4-89e7-3f38-9128-915f8102d016 | -15.23905 | -49.45819 | 2026-09-13 04:17:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b4db357-2818-3159-94e5-44b1dd02d7db | -10.55005 | -51.33113 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b31f368-0c3c-3cc9-baad-32ba880c46b1 | -13.3155 | -51.72214 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12e72336-143a-3123-93f8-0af50bd87083 | -13.46907 | -41.31343 | 2026-09-13 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77aaab84-9c40-36ae-bd86-c4ecbff8604b | -9.49819 | -44.54219 | 2026-09-13 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e432731-a717-3a0d-b9ec-6499ccd106b6 | -12.49457 | -47.15621 | 2026-09-13 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e29707f7-6687-3860-95bd-e7f43fadf251 | -10.21832 | -45.19463 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e43960d-4588-3d34-a848-95dae6b7f71b | -11.57178 | -46.98807 | 2026-09-13 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 10ca7d60-e030-3823-9530-0a4321ae65c7 | -10.4731 | -48.63946 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8bebbddd-da4e-37c2-b3e2-55629d3ae0ba | -14.10481 | -46.35792 | 2026-09-13 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1184dc13-c336-3720-97f0-e62d071b654a | -9.92094 | -48.5224 | 2026-09-13 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c4a0021-4b75-3977-bf66-9037352521bd | -13.45498 | -48.49238 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 160d24df-0b38-3bff-b31d-eb5529754baf | -10.53681 | -51.2995 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d1675d4-ab60-3f88-b45e-2cf45e30c517 | -13.4001 | -57.02879 | 2026-09-13 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d833a3d0-034b-318f-abe6-91dcd783da98 | -10.98442 | -49.70535 | 2026-09-13 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 048a5b67-0f12-3023-a072-c11525f2e9f5 | -11.18567 | -42.79124 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e754b36c-abe6-3b68-8b72-10b359f934a0 | -10.54357 | -45.20369 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7b9282d-de2b-3342-b1e6-cb978266a64f | -8.53964 | -54.71614 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce28f72e-86dd-398f-8ff1-7e67c481d986 | -12.00062 | -44.95934 | 2026-09-13 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28b99ed3-684a-33c0-a3f8-36dda2bd1138 | -10.69231 | -54.17535 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 623a61c1-69d4-3d2f-9ec9-b7bd961fbe49 | -10.63674 | -46.00695 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a301a63-93a3-3a98-8de3-a7bddae8d5b9 | -10.30822 | -45.29307 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4fca2c4-820b-398f-9644-5ee7fde51e08 | -8.02554 | -54.85477 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63e45e24-2bcc-30d0-8259-2d115e84b43a | -15.23801 | -42.78815 | 2026-09-13 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9567704-7f57-3476-83b0-e6fc1ce35e10 | -11.72579 | -46.74001 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae0c2aa6-e7e3-30cc-af60-ab6cda9dda1a | -7.87053 | -54.7057 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50e3b46f-15c7-31f6-8473-08c2e0a43cfd | -7.86465 | -54.70396 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f40ca81d-e201-3ff0-ab38-9197425fba66 | -10.89681 | -47.82274 | 2026-09-13 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68019032-957e-3865-b6f1-1a3b7272fcf4 | -15.25773 | -42.79964 | 2026-09-13 04:17:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5df16f9a-dec2-3bc4-8b4d-6a9e1e10bfad | -11.43399 | -45.14475 | 2026-09-13 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4071ef10-81ff-348d-a31e-0a637c8e1b00 | -10.54747 | -45.20065 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0be4d345-3fad-35e8-9207-b88f8a465354 | -13.98522 | -54.07391 | 2026-09-13 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b83e4c8-e60a-37b1-9dc4-28c10c7e2819 | -8.02738 | -54.85284 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 921d5fb5-c658-3864-ae7f-bb1f9c16f875 | -10.56255 | -44.61038 | 2026-09-13 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20deec25-d667-3f05-b24d-171a1fae8bcc | -9.71133 | -48.11008 | 2026-09-13 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb3c9bb-bbc2-32b5-b375-fa4aac532dfe | -11.81506 | -46.39103 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7cfcca5-c716-3f8d-bb01-171993526c5c | -8.54127 | -54.70741 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49cb3ec4-708d-3ce2-968f-e1b8727144e8 | -12.15287 | -48.95959 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d7a74c7c-50c9-3111-bb76-a94546973446 | -7.86975 | -54.70989 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4870de8-c171-37af-b2e5-aab52402f773 | -9.25036 | -48.23975 | 2026-09-13 04:17:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eab748ed-cf77-3966-bb8a-13ecbadd52ef | -8.12382 | -54.81401 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbf36e9e-6633-37ed-8955-42d1a79caa5b | -11.71758 | -46.7314 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14aecfaa-12be-3a57-8a24-52d1db885355 | -10.54295 | -45.22914 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7484c4d-0d3b-3620-9f03-daf219260be6 | -9.69703 | -43.3983 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43f7d994-5ff7-398b-ac76-7cb045237e95 | -13.37946 | -48.01074 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b59024e1-3f22-330c-b547-1c4d4eb28389 | -10.69444 | -54.16408 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ba59933-fd88-32af-bec0-9e8436fe83ef | -10.47392 | -48.63465 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e25dd13-ccae-3e2a-84e5-c355f28fbce2 | -9.89231 | -47.58759 | 2026-09-13 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3eafd30c-9803-3fc1-b9a6-afb9625f3f79 | -13.31469 | -51.72659 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34880313-993c-3b9b-8397-14a946e19cbe | -10.31156 | -45.2936 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49a3bb68-39d3-3200-8e9f-587842b96d12 | -16.67516 | -41.84766 | 2026-09-13 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8f9188ae-e865-321e-b2f5-6774414d264d | -8.11956 | -54.80367 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91a80405-0d79-3b52-a439-d98e77c13671 | -9.71086 | -54.35703 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52b55657-1b07-3dad-8a64-8623c4a10fdd | -15.30078 | -43.07657 | 2026-09-13 04:17:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| faab7571-4d6d-33cd-ba77-76895a916211 | -9.51701 | -45.45356 | 2026-09-13 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 724ff578-0f5d-3978-a3f0-b611b4ad5e1a | -7.87133 | -54.70137 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e81e8d63-9e63-31f1-acf7-02b5f8cf033f | -16.67145 | -41.8471 | 2026-09-13 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ea5c6275-e454-329e-ad3c-c9b53c3e5570 | -7.86097 | -54.69043 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cefc8afb-f3d8-3cac-ae73-774af4c3862e | -12.91194 | -53.89825 | 2026-09-13 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bcad486-9d89-35ce-9a34-22aae404d395 | -13.33382 | -51.62223 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8a93015e-ab88-340d-a88d-df65bf8a59e6 | -13.62288 | -47.88325 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README26.md)
