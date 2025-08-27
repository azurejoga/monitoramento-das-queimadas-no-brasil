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
| cb91b447-d4ea-3182-970f-dbffc6ee6ae6 | -8.9028 | -60.7498 | 2025-08-27 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8b585464-84a5-36ac-b618-26ae8d3141a0 | -9.8101 | -64.2642 | 2025-08-27 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f28bf077-5d87-3d11-9246-33029859be74 | -9.1007 | -49.5835 | 2025-08-27 01:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 298e8689-8e9f-3603-80d1-a09b5ff176ea | -9.1529 | -59.5609 | 2025-08-27 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 482a7c57-944e-35ac-8c2b-6bcc3813399f | -9.1715 | -59.5599 | 2025-08-27 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b42b10f6-6cc7-3969-a1af-c7c81c7ca312 | -21.1071 | -48.8334 | 2025-08-27 01:00:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.8 |
| 3a7d767e-e320-3b75-bca8-293c7618c318 | -22.55156 | -49.7671 | 2025-08-27 01:05:00 | TERRA_M-M | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| ca2f715d-8627-3a11-8bb3-be3b464a6032 | -21.36978 | -44.23167 | 2025-08-27 01:05:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.9 |
| 57cf7e85-7154-3c75-bf58-78d65409b540 | -15.64074 | -52.74221 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e1364066-2863-3fc7-9f26-cb0747bb4cc9 | -19.56235 | -47.54861 | 2025-08-27 01:07:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 523ba252-da0e-36c5-af05-7db4d1aa22c4 | -15.61953 | -52.7342 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 198778da-da39-31ef-b08b-feb6d86772d9 | -15.09102 | -48.56002 | 2025-08-27 01:07:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d0aada0d-1ba9-3c0d-bdee-d6bd514b473b | -16.02428 | -48.0998 | 2025-08-27 01:07:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9d80acc6-9533-3468-863a-9adb22afc34c | -21.58525 | -47.4765 | 2025-08-27 01:07:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ad3e8996-90f4-3c7e-93f8-f233aa790b13 | -16.70926 | -50.41677 | 2025-08-27 01:07:00 | TERRA_M-M | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c8e0cbb1-537d-3518-9887-c104e037988c | -21.57366 | -47.4862 | 2025-08-27 01:07:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7960e3e4-af6f-3f15-b5e1-3d410a98664e | -19.56276 | -47.53135 | 2025-08-27 01:07:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 912c1c80-1809-3093-907b-d48539cebb49 | -15.66158 | -52.73242 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 766e0da4-f0f9-381a-ac1b-f7662f2cf761 | -16.91601 | -49.44278 | 2025-08-27 01:07:00 | TERRA_M-M | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1f34f73e-bbfb-3753-b78a-50307b51ea5f | -21.58628 | -47.48293 | 2025-08-27 01:07:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 53efde34-534c-3926-8a13-b0703673d9a5 | -15.37774 | -52.75284 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78ae0651-ef6e-387e-8599-60467c862252 | -21.57741 | -47.50692 | 2025-08-27 01:07:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 24f466f8-7b71-39f3-8d49-66380f8cabdd | -16.49786 | -49.47576 | 2025-08-27 01:07:00 | TERRA_M-M | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| dec5d388-54f7-3281-b1fb-538e2359a2a2 | -15.37602 | -52.74174 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e733736d-7d01-3989-abb7-ac179e739197 | -15.66331 | -52.74361 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ccf59b1f-c767-3800-ae4c-fce28e9c0910 | -15.6082 | -56.17238 | 2025-08-27 01:07:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e0c42b24-bf43-3d64-b559-5047ef8491c7 | -15.8411 | -57.86465 | 2025-08-27 01:07:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e142cbfb-64f8-37d3-99bb-1d624ac7df00 | -21.34124 | -46.94703 | 2025-08-27 01:07:00 | TERRA_M-M | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| de1fb269-c3f5-3ff5-83d2-97688b434ace | -15.62931 | -52.73271 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e5d414cd-abd7-3295-9c35-879328429af2 | -15.61783 | -52.72295 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 4c6f09cb-75cd-3de0-948e-5cc4682df6a6 | -16.50088 | -49.49397 | 2025-08-27 01:07:00 | TERRA_M-M | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fc344a0f-5b83-3558-beb7-dcfb9a2720bd | -15.65358 | -52.74532 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 378bddbd-6600-3d27-b887-ef34fd2d31ac | -20.32696 | -46.88866 | 2025-08-27 01:07:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b814159e-0819-3996-888e-4c92f99b7f63 | -15.61612 | -52.71165 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7a7990ee-784d-3743-9f93-7033a93284e2 | -16.50441 | -49.48784 | 2025-08-27 01:07:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| bb69c5b7-d211-350e-aad4-3f972c7111ae | -19.55805 | -47.52563 | 2025-08-27 01:07:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 906bbd70-2e3a-3831-9c7d-16509c1dbc3e | -16.48907 | -49.47168 | 2025-08-27 01:07:00 | TERRA_M-M | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b0c058f2-9d9c-3601-b7ae-d3438529fc47 | -21.61086 | -49.69609 | 2025-08-27 01:07:00 | TERRA_M-M | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 524b4327-f837-3e50-97d3-42ab67770b89 | -16.49223 | -49.48981 | 2025-08-27 01:07:00 | TERRA_M-M | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 048dacd9-9430-3d2f-8071-794cad45fe34 | -21.58253 | -47.46211 | 2025-08-27 01:07:00 | TERRA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f4ea375d-aa0c-32df-9c25-ce2e578ce2a3 | -19.56684 | -47.55415 | 2025-08-27 01:07:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 003bbc69-04c0-30f3-a6d5-0953f931949d | -21.61542 | -49.70392 | 2025-08-27 01:07:00 | TERRA_M-M | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| f80ac1ad-f73b-30a0-a702-edcfcd8840f5 | -15.64383 | -52.74691 | 2025-08-27 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3087624a-cbcc-3b41-acb0-61b7dbcfe323 | -9.25333 | -56.90525 | 2025-08-27 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| abb3dbee-2d06-309f-a48e-ca50f486ec41 | -7.27639 | -57.67243 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a56628d-4859-3de7-adc3-df8fd4280c9b | -8.91856 | -65.91112 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 72d81d8e-764f-33e7-8864-d7c334f87195 | -6.70804 | -58.55894 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ce743b1b-56c5-3f69-b1f7-43512dcd96d2 | -9.23353 | -60.92194 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 35476974-19cb-320e-8a17-d480ae1544a7 | -9.17601 | -59.45959 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2eecbdca-b88f-3df6-b1a4-3a970cbfdc34 | -9.41495 | -60.49873 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| a97c6d8a-5d9a-3c51-bae0-3ef94bb173ae | -7.16982 | -59.73287 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e9d6ff1a-0aa8-33c0-b75b-f9b5d943905c | -7.2563 | -57.65724 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38b14c75-6584-3309-aadd-cf0b7e98a1a4 | -5.35648 | -60.40068 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1a1c4fb6-09fb-321d-a467-e9c359820437 | -9.08186 | -65.73396 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| a5423b73-52a9-3a3c-bb26-7f278127c6e4 | -14.37228 | -53.3532 | 2025-08-27 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 64d969eb-c3dd-3600-b552-2728c600e72e | -11.03074 | -52.03254 | 2025-08-27 01:09:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b013ff58-602c-32f4-8d62-62cd6f7f1cb2 | -9.41651 | -60.51065 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| eec97c84-f4bc-3b15-a9f5-f338c58d0b3e | -9.07186 | -66.04501 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ceaa44fa-e1a6-30ff-bd1e-5ca9b1a452b6 | -9.17503 | -60.77102 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 49b03ee8-49d7-3e99-b801-8d600142b402 | -8.88832 | -60.76472 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 389.7 |
| 0d1db293-c684-3dae-a543-f7633e80d694 | -9.15167 | -59.56832 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b9255aba-8c7c-3374-a22b-f1af8f7cf417 | -9.52083 | -60.5276 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7f972f15-6557-356e-84f6-bb4aeec90817 | -8.99854 | -65.42202 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 3ab37f1d-ba2f-33c3-8d14-f4f380371d2d | -6.83613 | -58.96156 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 76be9455-0e82-3469-a69c-0d2c94314bc9 | -9.07364 | -49.60712 | 2025-08-27 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 88da0b7c-5373-3a04-a322-c547f7e50bd1 | -10.0867 | -62.89141 | 2025-08-27 01:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5a664248-9e56-3481-b3e9-fc76dfffa2f5 | -6.68374 | -58.85701 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09d5d92a-b379-324a-9958-dc2cf7f2ebb5 | -11.36749 | -55.36707 | 2025-08-27 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 868b31b8-a097-3d1a-b734-6a568db70910 | -14.76832 | -59.72483 | 2025-08-27 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9d6a8fc0-d563-31d6-8a1b-0f2fae177885 | -10.28371 | -64.50851 | 2025-08-27 01:09:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| bf182d44-d935-39e6-bcca-9899440c591b | -8.87965 | -60.77831 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b2681d40-9e2b-3ae3-a4cb-00727eb9160c | -7.74671 | -61.0834 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| fe4d41f4-7596-3bd9-9ee6-34ab764503cc | -7.36232 | -57.62685 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 18d2d3fe-8a83-3db3-9f71-7ede026d7099 | -9.18547 | -59.45828 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 39143fdc-a4c0-3a72-b116-7abab5979f7a | -7.34491 | -59.66622 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 89c75266-5d26-3be3-9a28-736a7a2f5e92 | -8.88673 | -60.75248 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| ea692937-9f4d-3598-b457-d65df9e82138 | -10.52389 | -57.98167 | 2025-08-27 01:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 12a51ef7-a1e5-3ed0-917e-04d16dc8fce1 | -13.06233 | -46.33452 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 786b1f46-00d5-3121-808f-e04da8346b64 | -7.62857 | -61.0425 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd9b0168-4c29-37bc-8787-09553d755f54 | -6.81678 | -58.95479 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bbbc00f4-6021-32ea-b700-50d30f257da1 | -9.07557 | -66.07674 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3328e608-10ae-347c-bdad-65726fe35c07 | -9.80064 | -64.27964 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 9bc58abd-c994-3ad4-b0f5-630b6deb1979 | -9.13307 | -50.78355 | 2025-08-27 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 142291b1-db3d-3068-ae4c-51acd64a8949 | -9.39822 | -62.50658 | 2025-08-27 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 19b4dec3-7e0d-3a43-948b-ea068f09de45 | -7.47109 | -61.40656 | 2025-08-27 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2f286455-dc5d-31d7-b7b0-8068addaa9e3 | -9.58891 | -55.3738 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 35dddd24-7476-3908-aaa1-c5a84cc2ab21 | -6.92002 | -52.86371 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f2c78e6f-ef43-37d5-9607-1ca6e1add337 | -8.91423 | -60.72408 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b183d5e0-49c9-3a0f-83c4-54c9c3c6b44e | -9.28106 | -56.91032 | 2025-08-27 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 07d7b35d-9cdb-3ec5-a870-94982b91756f | -11.31739 | -55.2114 | 2025-08-27 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0e42478f-5de1-3f7b-a546-a7164629d5bb | -9.40481 | -60.5001 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 234.3 |
| 9722a2bd-0563-315a-be09-62ab6523e873 | -7.34357 | -59.65616 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e6a15543-6895-3923-8d23-c076a8492041 | -8.07018 | -61.53089 | 2025-08-27 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 10ea99a1-908a-3e76-a925-92b613729b6d | -9.19018 | -60.8066 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f5bac975-e13b-3832-9622-02a78351dc2a | -8.95662 | -65.9689 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 431.8 |
| 8d327dc3-e10b-38b5-a178-1802037c7f1a | -9.39611 | -62.48991 | 2025-08-27 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| f79c5dbd-d41e-3b77-b2c9-f757a1b97b61 | -10.59987 | -54.89671 | 2025-08-27 01:09:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c3859c97-b4e4-3b5f-a10c-e978a83ae739 | -11.51798 | -52.12688 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3d7c501f-7829-3f88-be52-927ed43af132 | -5.42612 | -60.16599 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0894c28b-9212-398c-925a-b123258dd6fc | -9.06133 | -66.0511 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |


[Clique aqui para ver as próximas entradas](README9.md)
