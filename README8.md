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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56bc961f-0e85-34d2-9818-dbd995b7eab6 | -8.3397 | -44.1658 | 2026-09-27 02:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 3b8e590f-66ed-343e-93ef-bab28b107cd6 | -9.2745 | -67.6433 | 2026-09-27 02:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 350a1131-4498-3eb7-9e49-9bb5c91c8079 | -12.0365 | -50.6233 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 00812860-254b-3d66-ad3c-ebc80dcfe498 | -8.3583 | -44.187 | 2026-09-27 02:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 9e658e3b-1b23-3d4f-998d-a768be384924 | -5.162 | -56.0129 | 2026-09-27 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| cdd6ab82-95e6-3a00-a1d4-db89189dd6a6 | -12.0556 | -50.6211 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4eed7e0a-1ffc-3fad-9c52-a09f3eed20fa | -12.3085 | -50.2904 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 533b4ca7-82f3-3d6a-bffe-0ce71fc5f303 | -12.2894 | -50.2927 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| d2a04c7b-a8a0-3c88-b295-62818faacfa0 | -12.0559 | -50.5996 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 2d2603ae-062d-3330-b722-b6b9038d91ef | -8.3394 | -44.189 | 2026-09-27 02:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| af30e63d-a28e-3a4a-bddb-b111fd600c1c | -12.289 | -50.3143 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 4b6d52e0-4c90-30fc-b97c-e9ea394382e6 | -12.2699 | -50.3166 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c6dc9c0a-9419-3825-b934-0d96314f7594 | -8.3589 | -44.1406 | 2026-09-27 02:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| e1d47940-3a37-38d0-9a29-3632c46bd0f4 | -8.3586 | -44.1638 | 2026-09-27 02:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 390.6 |
| b7ab9420-a143-3200-a4d9-c647aa0172e4 | -12.3082 | -50.3119 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| b6de0153-652f-34f2-b889-35544cf06fd5 | -12.3082 | -50.3119 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 3d35ec6d-4e6a-3a91-b3ef-f8433e6b3f13 | -12.2699 | -50.3166 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 83252295-3312-36ba-a5fd-f892541241fd | -12.3085 | -50.2904 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| db9e2371-4169-39d6-be4f-10057cb748fc | -12.0559 | -50.5996 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 215.2 |
| d3e7e46d-595b-3968-8586-d57a972d7704 | -12.0178 | -50.6041 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a8112c4e-4bdd-36a1-bbea-37657f1799f8 | -12.0372 | -50.5804 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 6900f9a1-51bc-3df9-bbbe-468dcedab855 | -8.3583 | -44.187 | 2026-09-27 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| be9864ec-8326-3793-aee6-981041c1148f | -12.2894 | -50.2927 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| b024c07e-7c3c-3703-97d2-b5cf5e778180 | -8.3589 | -44.1406 | 2026-09-27 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b4c49e6f-e353-3404-a865-3b7b2f4d4b7e | -8.3394 | -44.189 | 2026-09-27 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4b2eafbe-4f8c-37f3-905f-aa3edb2e5b36 | -8.3397 | -44.1658 | 2026-09-27 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 876b9277-c2c8-393d-921b-84065f55912a | -9.2745 | -67.6433 | 2026-09-27 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 02f4a354-24d3-36fe-a9db-b377e2d07893 | -12.2703 | -50.2951 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e066a725-e927-3d43-ad06-ee5294fd49ef | -12.0365 | -50.6233 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 93ba130e-f3da-34f7-b5a6-2782cc338787 | -11.8669 | -50.5147 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6a10bb5c-ec5f-3410-84a1-b94efcc56127 | -8.3586 | -44.1638 | 2026-09-27 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 348.9 |
| 961473b4-f42b-3a9a-b184-b917cde78686 | -12.0369 | -50.6019 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 355.1 |
| 33559a0b-5369-3562-9185-80ce8e2f8ced | -8.3775 | -44.1617 | 2026-09-27 02:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5031a5ed-75ca-398b-8d40-7c3af78d25d5 | -8.0373 | -54.8926 | 2026-09-27 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| fc3b1eb0-3c13-312f-beb8-21af0c77ce8c | -12.289 | -50.3143 | 2026-09-27 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.7 |
| e7fc99cd-b8c2-38d2-a62b-7c159cb5caee | -11.94 | -50.5 | 2026-09-27 02:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d44d065c-8447-31c5-8111-e6140f51583d | -8.36 | -44.16 | 2026-09-27 02:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5c2e222-48fa-3bf5-b3da-669c9ea07a2c | -11.91 | -50.54 | 2026-09-27 02:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39d7f45b-ef90-3fd6-85f0-71122b9d78e3 | -11.94 | -50.55 | 2026-09-27 02:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8aa51b8-191f-396c-85e7-cdd6b9313739 | -8.33 | -44.2 | 2026-09-27 02:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 63278d65-3c4e-3bcb-981d-71838f5d5c7d | -11.91 | -50.49 | 2026-09-27 02:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a4b040a-77bd-3af4-8664-0bff89bfd28a | -8.36 | -44.2 | 2026-09-27 02:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9984e072-677e-3240-8748-7f146c656a65 | -8.33 | -44.15 | 2026-09-27 02:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3122d14c-3ec4-35c8-afcb-d8ba6c273cfa | -12.2894 | -50.2927 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 67295043-0866-32f0-8dae-93c9922f7777 | -12.0178 | -50.6041 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 43ace0d2-c195-3827-ae85-c153a2d1e019 | -8.3775 | -44.1617 | 2026-09-27 02:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c2757eff-df38-3407-b6df-f23e9a86b5c5 | -12.3082 | -50.3119 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 270.6 |
| fcf6efc9-9246-3e64-b0d8-ed0b71fac8ae | -12.289 | -50.3143 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 4b359df6-4859-34e6-9b20-64ff7969d8be | -12.2877 | -50.4004 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| bb7b96c5-c8fe-398b-8989-bec180fcd145 | -8.3397 | -44.1658 | 2026-09-27 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 168.1 |
| b1be66ab-2a34-3ac6-9030-c6f429755787 | -8.0373 | -54.8926 | 2026-09-27 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e33778c8-d243-3bde-aa4e-748b08fad306 | -12.3085 | -50.2904 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 9f82f4e2-2952-37c9-9ad6-df6a357886f9 | -12.0369 | -50.6019 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 260.0 |
| 44b7ad10-cc4f-3e2f-9d4a-3945afa4c79a | -12.0559 | -50.5996 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| a553d8ee-384e-31ad-a2c9-9985b28d4862 | -8.3583 | -44.187 | 2026-09-27 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 297870a0-36ee-3d7f-9072-9a4eb3681618 | -8.3586 | -44.1638 | 2026-09-27 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 309.9 |
| 337f306a-01fc-3b7f-9602-7bd926925f02 | -8.3589 | -44.1406 | 2026-09-27 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 1a263f1f-30aa-3db7-a60e-0625d7b676a2 | -8.3394 | -44.189 | 2026-09-27 02:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 19cf2222-f19e-32e1-8c6c-d77bce97c84f | -12.0372 | -50.5804 | 2026-09-27 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bf7f1c52-1140-344f-bcb3-a06ee864347c | -8.3397 | -44.1658 | 2026-09-27 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 7607ecd1-0a46-36f1-92bc-256b402bb7dd | -12.0369 | -50.6019 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 3f91f7b7-1fec-3f0e-93db-96a672187b92 | -12.0559 | -50.5996 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| de69a7de-9993-3ff6-bca7-0fe42a7f4fd3 | -11.9428 | -50.5273 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 315d8406-5d81-39d8-94c3-d912aa9d0666 | -8.3589 | -44.1406 | 2026-09-27 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 6e029a4a-57ec-3a09-b52a-e04e372a5186 | -8.3394 | -44.189 | 2026-09-27 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 925cd00c-7cf3-3730-853b-b2566bd02988 | -12.289 | -50.3143 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| a971f8d8-d962-3124-8de8-31b5c04d0bfe | -8.3586 | -44.1638 | 2026-09-27 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 371.4 |
| 193c126a-6668-30f8-990f-260f05be3cd2 | -12.3082 | -50.3119 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 228.7 |
| ffabfcd7-0e47-3244-9c7c-37ca38494af6 | -8.3583 | -44.187 | 2026-09-27 02:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 75767e46-fdf9-30eb-843d-182dd3763307 | -12.3085 | -50.2904 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 12dbd566-be55-3e04-a71e-3438b1bf2d12 | -11.9431 | -50.5058 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 06f8aa05-7e4d-3cda-99cd-7e64050caf15 | -12.2894 | -50.2927 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 4a3256dc-2603-3fcb-a818-eda1f1b67300 | -11.9619 | -50.5251 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 28d37834-1660-3c58-b555-e7229e88645b | -11.9425 | -50.5487 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5e4694d0-f858-3474-ba84-c545a6e4c50c | -8.3775 | -44.1617 | 2026-09-27 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 22188588-fbd3-3213-bcb2-93187580b7f5 | -11.9622 | -50.5036 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7dc14897-23b4-3801-a781-e7687b5b6dd7 | -11.9615 | -50.5465 | 2026-09-27 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 373e4fab-b8f5-31de-9d29-c0d5909cdd7d | -8.0373 | -54.8926 | 2026-09-27 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 85a9e05c-28ea-3e92-a5ff-d5e54b706e56 | -12.289 | -50.3143 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 47bb9e1b-25b1-30aa-a40e-2ddecf122d6f | -12.3085 | -50.2904 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5f3c0a72-f9c2-3c63-8e8a-9bd9c0700c97 | -11.9619 | -50.5251 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 14799255-771f-3c57-986d-5e48b10d3a68 | -11.9431 | -50.5058 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| be347d04-9812-379e-9baf-a07a83dc85a5 | -11.9615 | -50.5465 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 532a543b-927b-36ec-b04a-728fb38b44bc | -12.3082 | -50.3119 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 49eedb1c-21cf-341a-b41c-3488c24aae5e | -11.9428 | -50.5273 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| dd973087-3172-38e5-848b-a231148bdea8 | -12.2894 | -50.2927 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 9abb3783-ff8f-3d1e-84a2-f9a77e8dcc6a | -11.9622 | -50.5036 | 2026-09-27 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f3a7f684-29da-32e0-8384-cd8852e61618 | -11.9431 | -50.5058 | 2026-09-27 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| f3252b31-425d-36ed-844b-6b1dc71af527 | -20.9552 | -49.1439 | 2026-09-27 02:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| d4d31539-a396-32dc-a69e-0094e54c8afd | -11.9622 | -50.5036 | 2026-09-27 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| e4284d6d-110e-3100-94f8-8f3d7b585558 | -11.9619 | -50.5251 | 2026-09-27 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 254.9 |
| 92e42ac2-efb3-3690-b55a-94601c81438a | -7.3998 | -55.6511 | 2026-09-27 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 973a7d1f-cb98-35d8-ac62-2360ad1759eb | -7.3999 | -55.6311 | 2026-09-27 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4c05b128-479f-3d9a-b96c-beca552a5fb8 | -11.9428 | -50.5273 | 2026-09-27 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| a58ac1f2-e30c-358b-81b8-c050cd6581d1 | -20.9346 | -49.1485 | 2026-09-27 02:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.9 |
| d47b7f2c-d544-359d-aeef-9569409706af | -12.3082 | -50.3119 | 2026-09-27 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 673dc1b7-f64c-3407-ac61-c7b0f532789e | -11.9809 | -50.5228 | 2026-09-27 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7476c1a8-91c4-308c-a346-afcc4bd6d193 | -11.9431 | -50.5058 | 2026-09-27 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0a69af3e-ce3a-37c6-b6ae-5e409f43bf80 | -7.3998 | -55.6511 | 2026-09-27 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b0ccf89d-67ee-306d-ad39-61e19b5f7e19 | -11.9428 | -50.5273 | 2026-09-27 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |


[Clique aqui para ver as próximas entradas](README9.md)
