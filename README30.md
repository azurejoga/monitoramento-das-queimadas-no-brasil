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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3001199e-d4e5-3ff6-aece-09db8c08c92d | -4.90642 | -37.29465 | 2025-07-18 11:49:00 | TERRA_M-M | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 25.5 |
| b0e3508b-0e20-3614-9c48-6fb58c80fe72 | -3.28721 | -42.53734 | 2025-07-18 11:49:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5808fa89-4aea-3897-941f-7200e323e640 | -6.96019 | -42.87996 | 2025-07-18 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 705eb297-c48a-343e-960f-d4b3eca5c42b | -4.67804 | -38.05441 | 2025-07-18 11:49:00 | TERRA_M-M | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 442a7cd2-88f3-3997-9e88-5e286bf1e45c | -7.1894 | -44.07238 | 2025-07-18 11:49:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| aa9bb41c-0a04-3763-bf6c-71fe008c10a0 | -5.6567 | -43.7161 | 2025-07-18 11:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 796b4285-0522-313e-ba37-cd480b64fca7 | -11.94349 | -46.36328 | 2025-07-18 11:51:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d313c562-4bdb-3f87-aa56-8531ec884e72 | -11.94773 | -46.33525 | 2025-07-18 11:51:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a17445bb-4331-3396-b1e3-2943dcb56f87 | -7.91486 | -45.89961 | 2025-07-18 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 447b9505-f3b0-3d1b-9eb2-58ed66b442f8 | -8.82329 | -44.53838 | 2025-07-18 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 0a1c9b44-3330-30bc-b2e3-b4eb209cb0b0 | -14.22733 | -45.48678 | 2025-07-18 11:51:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 39605399-3613-38e6-b20e-6136e0223c96 | -8.82578 | -44.52211 | 2025-07-18 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d471bac0-1010-304f-a0c2-b1d42737fe38 | -8.82168 | -44.52749 | 2025-07-18 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 13e0fd6d-d4f3-3cf1-9aac-de4cbd3403e5 | -11.57337 | -47.07346 | 2025-07-18 11:51:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| c5e48de0-4406-39ee-b432-bec6429df72a | -14.7106 | -45.07246 | 2025-07-18 11:51:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 4d6f3d50-0b05-359e-865b-9c3fd79ff79b | -14.20397 | -45.34967 | 2025-07-18 11:51:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 6c0db54b-f758-32be-86a0-b1bb93dba87d | -12.57157 | -44.74544 | 2025-07-18 11:51:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ba1441a2-7b50-3fca-8094-e3411250fd4d | -12.58023 | -44.7619 | 2025-07-18 11:51:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 22f625aa-877e-3270-a52f-161c0d009cc4 | -11.99783 | -45.29757 | 2025-07-18 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 83cbd457-f596-3216-b704-c42c329386f2 | -14.71285 | -45.05853 | 2025-07-18 11:51:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 266a0ad0-16e3-3a00-b910-734cc436e210 | -14.20644 | -45.33443 | 2025-07-18 11:51:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0ddaee0f-3bab-358e-a98d-48dfb98dbd50 | -14.72375 | -45.06036 | 2025-07-18 11:51:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| a029c9bd-1e4d-3d57-8f6e-90392fa59999 | -11.99518 | -45.31407 | 2025-07-18 11:51:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a45ced13-7df4-3d1b-b3a9-84d8e1e0e80d | -12.58263 | -44.74725 | 2025-07-18 11:51:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5bf53000-3916-38b9-8cbc-52f5404a378c | -14.72528 | -45.06746 | 2025-07-18 11:51:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 2948a3dc-83ff-3124-84ff-3f4ef3ddb353 | -11.79017 | -45.2187 | 2025-07-18 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1ee424d3-325c-3918-8a65-9e16951b6717 | -12.46171 | -44.4932 | 2025-07-18 11:51:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2743d3c0-ddf5-3dd3-a316-824b0e9dd707 | -11.94429 | -46.35653 | 2025-07-18 11:51:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 39d32fa7-93f2-3bc4-bbfb-27155baeee5c | -13.79976 | -42.19861 | 2025-07-18 11:51:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6371a904-0f41-3eaa-b084-bbae31fd47d8 | -11.94696 | -46.34286 | 2025-07-18 11:51:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| c69c0b7f-61a6-3249-86f9-72d7c3155804 | -14.72147 | -45.07455 | 2025-07-18 11:51:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| f4e98554-4215-3583-97c3-d4013d2fb148 | -8.81906 | -44.5437 | 2025-07-18 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 50b3b14a-b3b3-3ed2-9f70-bb0299c8a3e3 | -12.47259 | -44.49494 | 2025-07-18 11:51:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| b88672d7-d027-3eeb-b92f-ef735d6ed200 | -12.56915 | -44.76009 | 2025-07-18 11:51:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 96cad7c4-e954-38ab-97d3-c1123e27383e | -16.32642 | -43.62191 | 2025-07-18 11:53:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3502d394-2c68-3a44-b724-9e28802c974f | -16.78788 | -43.89691 | 2025-07-18 11:53:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 80b1d329-9f3a-36e7-a31e-54de4562a6a3 | -19.53808 | -45.06009 | 2025-07-18 11:53:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4f6e2ab1-d910-34d8-8a87-f457c290f422 | -19.64745 | -40.71166 | 2025-07-18 11:53:00 | TERRA_M-M | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 64498d57-c1ed-349d-a05b-e9257f45de5c | -19.53952 | -45.05385 | 2025-07-18 11:53:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 35adfa66-1e63-3bed-82d6-96ca9d4f5d66 | -20.48375 | -42.39781 | 2025-07-18 11:53:00 | TERRA_M-M | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| ec8408a3-b70a-359d-b2d4-18a9257e0416 | -20.48235 | -42.40734 | 2025-07-18 11:53:00 | TERRA_M-M | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| 915073e1-2108-394e-9284-d67ce9b4e39c | -19.61654 | -40.72969 | 2025-07-18 11:53:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 18d32d9c-e30d-3b60-8dba-c731cb7dfc3e | -19.67154 | -48.97753 | 2025-07-18 11:53:00 | TERRA_M-M | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3ee380c3-5814-377d-807e-dc89e47e15b9 | -19.53761 | -45.06579 | 2025-07-18 11:53:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d108a5b3-085a-38d2-b31b-0a69a97a9d43 | -16.22222 | -41.18883 | 2025-07-18 11:53:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4120852f-36f3-37c6-b8f0-12205aafc22b | -16.6456 | -40.6243 | 2025-07-18 11:53:00 | TERRA_M-M | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 19e54ed6-a416-3b13-8372-2e3f0b0c54ae | -22.54599 | -47.02544 | 2025-07-18 11:55:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7cffca73-bbbe-3873-9ae5-106c6c4cc689 | -22.54465 | -47.01829 | 2025-07-18 11:55:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9634d39a-0096-389f-8b1a-411b7d8c39bb | -14.7207 | -45.0649 | 2025-07-18 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| eb81ce61-3b2e-3383-986f-feae04680b86 | -12.5773 | -44.7581 | 2025-07-18 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e5103525-baf7-3be4-a25f-e227c74cb874 | -5.6567 | -43.7161 | 2025-07-18 12:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 1dd28d09-dcbf-3b65-a918-326d350f3bc5 | -14.7207 | -45.0649 | 2025-07-18 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 620996f2-0c84-3de4-8259-fb33d3b38c38 | -5.6567 | -43.7161 | 2025-07-18 12:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 77468ed5-7513-3d27-b705-b50d1630e887 | -5.6379 | -43.7175 | 2025-07-18 12:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| bf1d84ec-90a1-3341-a56e-4f3680fcfe1c | -5.6569 | -43.6929 | 2025-07-18 12:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8632813c-95a4-351b-b055-294fbc6c3d1e | -12.5773 | -44.7581 | 2025-07-18 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 5b8059f1-8ed6-3275-b91d-c27df8100804 | -14.7207 | -45.0649 | 2025-07-18 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d2f27a4d-792d-3b19-9b73-743b1ab467e8 | -5.6565 | -43.7393 | 2025-07-18 12:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 81833204-03fe-3966-89e2-74f25ccde033 | -5.6567 | -43.7161 | 2025-07-18 12:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 27a2f82f-cf25-3f73-a40a-4fa2a8ee4fe1 | -5.6567 | -43.7161 | 2025-07-18 12:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 294.9 |
| 085f32c5-9697-3047-9b7d-613a1c5507ac | -12.5773 | -44.7581 | 2025-07-18 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| cd9dc661-8be5-3082-bfa5-2819db3d92f3 | -6.9801 | -42.809 | 2025-07-18 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 48e9bd43-8bec-3dc6-a8d2-c22ce05014b5 | -5.6565 | -43.7393 | 2025-07-18 12:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 61bf1a9d-a4da-3d93-a539-f58dd52589ff | -5.6379 | -43.7175 | 2025-07-18 12:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7ba62691-3bb7-3370-b42d-1f515b55809d | -14.7207 | -45.0649 | 2025-07-18 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 6b7a8fff-f2fd-3b5e-804c-040ffa23deb0 | -14.7207 | -45.0649 | 2025-07-18 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| bd66dd22-b742-3afb-a37a-c988bf9f8fd0 | -6.9801 | -42.809 | 2025-07-18 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 8e91d7e6-6c17-38df-830a-8217dee917b6 | -12.5778 | -44.7347 | 2025-07-18 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4f5c5786-3523-3d73-a1cf-f0c6b2e9ef41 | -12.5773 | -44.7581 | 2025-07-18 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1e8f88c6-0e70-3236-8624-4f89d5568d80 | -5.6379 | -43.7175 | 2025-07-18 12:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| b3b6d82c-532c-3911-95c9-22a0dcc83ffa | -5.6569 | -43.6929 | 2025-07-18 12:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 43d7c89c-8bf2-3850-a5cc-218ae971469f | -5.6565 | -43.7393 | 2025-07-18 12:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 503fd2bc-861f-3a4a-a653-b7262a632788 | -5.6567 | -43.7161 | 2025-07-18 12:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 501.7 |
| 7354b76d-2496-3b9c-b40b-5d1f07553b01 | -5.6754 | -43.7147 | 2025-07-18 12:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 953a6d68-c971-3fbe-8933-cabb2239aa04 | -6.9801 | -42.809 | 2025-07-18 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| daaebce4-fb88-3c06-a8af-4bb45b08d37a | -5.6567 | -43.7161 | 2025-07-18 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 491.2 |
| 32ac409e-da5a-3d34-8482-087194fc4da4 | -12.5773 | -44.7581 | 2025-07-18 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 86a7983d-1dc8-3db4-9659-0bb2e9aed3f1 | -12.5778 | -44.7347 | 2025-07-18 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4716b716-5e6b-3307-81bc-73dc404ed3cd | -14.7011 | -45.0685 | 2025-07-18 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0e91d88b-60cc-38be-9d77-a017847850e1 | -14.7207 | -45.0649 | 2025-07-18 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| f7bc8ee6-60bd-3c27-8e7e-a9859fd88add | -5.6379 | -43.7175 | 2025-07-18 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 41788625-311e-31ce-a23f-5741e1a036ac | -5.6565 | -43.7393 | 2025-07-18 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| ce126aa6-8730-38e9-b282-da31c588f229 | -5.6754 | -43.7147 | 2025-07-18 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f3c2c93b-d56e-3ea3-b4b6-88b083cd3c1d | -14.7011 | -45.0685 | 2025-07-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 11fa785c-1f66-3ef7-9a34-a67b528a4fb4 | -6.1444 | -47.7688 | 2025-07-18 13:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| de82e222-c112-32b2-bef8-10a61ca83569 | -7.1917 | -44.0732 | 2025-07-18 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 444a43b9-6143-31ce-be58-37d8936d963c | -5.6565 | -43.7393 | 2025-07-18 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 865e55a0-71f8-36b0-b194-b3c83481d9fd | -14.7207 | -45.0649 | 2025-07-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 166.6 |
| a4cc8d8d-1424-37ba-8a93-cf01e2d4c5fd | -12.5773 | -44.7581 | 2025-07-18 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5c43ecd0-2b76-3a23-b160-e7c4529b9db6 | -5.6567 | -43.7161 | 2025-07-18 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 392.1 |
| 960d361d-b35f-377f-9551-ff6bb5537ef0 | -5.6379 | -43.7175 | 2025-07-18 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0bc73fba-991b-30f3-8f51-03a83f2717c6 | -5.6565 | -43.7393 | 2025-07-18 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 5b67a5ad-1325-3afb-9a7e-94d2cf1d32a7 | -14.7011 | -45.0685 | 2025-07-18 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 94abb598-e701-336c-ad44-a40a144287ba | -5.6569 | -43.6929 | 2025-07-18 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 442eeb16-35e4-357f-b0e5-f4f2a37bd563 | -5.6379 | -43.7175 | 2025-07-18 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c98653e5-7825-386d-b027-4f645fb0c42d | -5.6567 | -43.7161 | 2025-07-18 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 297.1 |
| 866ec6e2-5baf-3639-96d5-c25150e4f05e | -14.7207 | -45.0649 | 2025-07-18 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 881c8842-3049-394c-bb7a-14f4a879dc59 | -6.1444 | -47.7688 | 2025-07-18 13:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| dccf449b-19dd-3ab6-aabe-376acd6a2bd0 | -5.6379 | -43.7175 | 2025-07-18 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 4d777725-b4af-301e-ae09-a1866a9b70a9 | -5.6567 | -43.7161 | 2025-07-18 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 241.9 |


[Clique aqui para ver as próximas entradas](README31.md)
