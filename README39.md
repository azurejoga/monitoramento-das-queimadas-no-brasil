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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdc24b79-efa5-3a6e-a384-e6385ffe6276 | -11.2853 | -51.3454 | 2026-09-23 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3e833972-e20d-3cbb-98ba-4eb72980bd3d | -12.4212 | -46.9777 | 2026-09-23 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| eb24e53d-87f8-35f6-85bf-46adbff34be3 | -6.6815 | -55.0703 | 2026-09-23 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 9d50ace3-13f7-3020-9580-53b2e201e39d | -8.4538 | -48.6944 | 2026-09-23 03:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a3dc63d0-be96-3d37-91e2-11c12a4dad3a | -12.4216 | -46.9551 | 2026-09-23 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 01ad8ae8-7c52-3316-ba48-c21736caf274 | -11.8871 | -45.7623 | 2026-09-23 03:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 5d0427fa-8225-3f8b-ab43-0d8be139e658 | -12.3488 | -50.1563 | 2026-09-23 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 50f3ab8e-fbcb-3dc4-b506-0c6faa0ba0bc | -9.8407 | -46.3686 | 2026-09-23 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| cdebfca0-d5d4-32ac-865e-5a3f75aeba86 | -6.6146 | -59.9272 | 2026-09-23 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 028c7381-5057-3271-8e60-50888e833e75 | -8.9165 | -61.4767 | 2026-09-23 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b88f54a0-5e28-3794-bda6-d4c395f4abe4 | -7.8811 | -61.1779 | 2026-09-23 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 68c070ef-56c4-31af-8b6b-6b0b2e978708 | -6.633 | -59.9457 | 2026-09-23 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4ab94ff7-78c7-31f2-897f-014810f52cf7 | -14.6307 | -45.617 | 2026-09-23 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1626ee30-7f0a-3f3b-ab90-f487b7ce44ad | -8.935 | -61.495 | 2026-09-23 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 265ef7cf-b1f6-3bfb-961b-648d42a7db97 | -3.6946 | -60.5835 | 2026-09-23 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0e1453d5-0d53-3ab5-91a9-8f3ff2570157 | -6.2038 | -47.371 | 2026-09-23 03:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| a0aa4953-498e-3f7c-b081-0820cd043623 | -11.3037 | -51.3858 | 2026-09-23 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 33a37c8a-3eab-3005-b721-bc5de455b73a | -9.8404 | -46.3911 | 2026-09-23 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0bfeafd5-e79c-3c09-9068-16f1921db7fc | -14.7536 | -47.1548 | 2026-09-23 03:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 116.6 |
| c5b5bbda-0071-352c-8e73-a77e7c7286b5 | -6.6331 | -59.9265 | 2026-09-23 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 104034b3-2ebe-30be-a9de-90b6a1fd3965 | -5.7754 | -45.1053 | 2026-09-23 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f76c04af-6a95-3bee-a11d-0de4857374f7 | -14.6297 | -45.6635 | 2026-09-23 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ab23eeb9-3082-38f3-81e2-cd855d498dab | -14.6106 | -45.6438 | 2026-09-23 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 368faf58-8160-3600-8963-85b7007a865b | -12.1192 | -45.6368 | 2026-09-23 03:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5eb8a116-98c0-3797-afe5-efa1067d1bc5 | -3.6763 | -60.5839 | 2026-09-23 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6da4c93a-6190-3b8a-919d-7e498916203c | -11.304 | -51.3646 | 2026-09-23 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3bb3e5ae-1264-3f2a-9af2-1c7cce3f6ddc | -6.6148 | -59.908 | 2026-09-23 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7beaf42c-3bc1-3e0d-9f33-1f8de748246b | -14.6302 | -45.6403 | 2026-09-23 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 2862cd7a-8e07-3a83-bb86-370fe43e212c | -3.2313 | -46.9596 | 2026-09-23 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7015cfea-2df2-3c93-8c99-c3c7e446f860 | -6.1109 | -57.684 | 2026-09-23 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| aeb3eaaf-cd48-38fa-a21a-6fe78568d140 | -3.2314 | -46.9376 | 2026-09-23 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 2e4d7aad-ab28-3d09-a82f-26393eda704a | -3.6947 | -60.5645 | 2026-09-23 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4934671e-8cc7-3177-8f79-8e56fdf25e91 | -9.1025 | -61.4299 | 2026-09-23 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3f647e18-798d-38f6-9f8e-981b092fda7b | -5.7567 | -45.1067 | 2026-09-23 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5057e338-e09a-3cd3-805a-976c77e75451 | -12.3676 | -50.1755 | 2026-09-23 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 67fdec5b-a926-349a-9cba-8431241f2ab6 | -8.4726 | -48.6927 | 2026-09-23 03:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 13068619-562a-328d-bc54-8cd58c7e29f1 | -9.1024 | -61.4491 | 2026-09-23 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f7e5b337-824e-31cc-be0e-115bf99b6487 | -9.0839 | -61.4308 | 2026-09-23 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 31e09e35-ec9a-3675-8f18-07f95577f823 | -3.2314 | -46.9376 | 2026-09-23 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| fc26805e-9207-3844-a871-606500e12bf1 | -6.6148 | -59.908 | 2026-09-23 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f6154a46-a277-3df9-8f4c-6682e0db3d10 | -6.6317 | -43.73 | 2026-09-23 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fbdba054-ea44-3408-a0e1-bac850635539 | -6.5939 | -43.7565 | 2026-09-23 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7afe713c-b52a-33bd-9645-6007ba0c594c | -7.8811 | -61.1779 | 2026-09-23 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d300851e-f6b6-3b4f-85b5-8bd49bb0fc80 | -3.6763 | -60.5839 | 2026-09-23 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b1512b5d-533f-3ee9-89ac-35ec9026febf | -3.2313 | -46.9596 | 2026-09-23 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b76adc89-91b8-3ac2-a118-ef69960d014e | -6.6146 | -59.9272 | 2026-09-23 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 9aa6d64c-130c-3cd2-8955-593b5f5162ba | -6.6315 | -43.7533 | 2026-09-23 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 03459e6e-500e-375b-bdd6-ba3f0175beb7 | -3.6946 | -60.5835 | 2026-09-23 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c5ae2d25-7a5e-36eb-8fb2-3592fd29419c | -8.4538 | -48.6944 | 2026-09-23 03:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 28ec9ff5-188f-3141-a499-94ed8ec5e1f7 | -12.3676 | -50.1755 | 2026-09-23 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 49d5ad8c-fe70-35eb-ba61-66f7cabece39 | -3.6947 | -60.5645 | 2026-09-23 03:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9269bd07-c1c5-3aab-a1e1-857173f7d257 | -5.7567 | -45.1067 | 2026-09-23 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e519849e-7e4e-3b14-9228-ff450c46609e | -6.6331 | -59.9265 | 2026-09-23 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 133.9 |
| d9c8b556-4bdf-3c67-b79e-013f70f8016e | -8.9164 | -61.4958 | 2026-09-23 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 308f4f04-b232-316b-a52c-ed5319bbca2f | -5.7754 | -45.1053 | 2026-09-23 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 25014841-b969-3da0-8d0b-1f4485e422ea | -8.9351 | -61.4759 | 2026-09-23 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 170e588e-928a-385b-950b-8cf1ddee21d5 | -6.5941 | -43.7333 | 2026-09-23 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4b14d81d-058c-3d91-83b3-fb842a4d1b18 | -8.4726 | -48.6927 | 2026-09-23 03:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f3daa687-bbf8-3699-a68c-06e262f17c4f | -6.6145 | -59.9464 | 2026-09-23 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 07961b5b-a8da-33c3-a5dd-5a1f49b17875 | -11.2853 | -51.3454 | 2026-09-23 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| fc8d0996-b6a7-3e02-a988-e8bce4a49b7a | -8.935 | -61.495 | 2026-09-23 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e4ea0cc3-edb2-37ba-98d7-54ae4fd7461a | -9.1025 | -61.4299 | 2026-09-23 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 5ecbcf75-81e4-357a-b6a4-dce6285eebf0 | -5.6246 | -45.2518 | 2026-09-23 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2531ef2a-00d5-336e-adec-309a992d45c6 | -8.9165 | -61.4767 | 2026-09-23 03:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 6542d730-c4a2-3312-ba76-f99320d692e3 | -12.3488 | -50.1563 | 2026-09-23 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3435b055-fb07-3adc-9ef7-491832cd406f | -11.304 | -51.3646 | 2026-09-23 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e6ca9a14-49ce-3681-96a4-957dda41e79b | -12.3679 | -50.1539 | 2026-09-23 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e854fbbf-b540-3674-b367-0163f9ce236c | -6.633 | -59.9457 | 2026-09-23 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 4af6166d-d4cf-387f-82f2-bfee8cf20e46 | -11.8871 | -45.7623 | 2026-09-23 03:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| e0b780a8-f45a-3f5a-bc5c-8fc95a91b3a0 | -6.6129 | -43.7317 | 2026-09-23 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 219.2 |
| fc44fb1d-02fb-3d3a-8812-3858a9e99b77 | -6.6127 | -43.7549 | 2026-09-23 03:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 243.4 |
| 6741b1c9-9566-362d-acb6-6315dca30e81 | -11.3043 | -51.3434 | 2026-09-23 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 01c1eeb5-0ce7-3c0f-9fa5-55cea757f9db | -7.47369 | -35.14127 | 2026-09-23 03:21:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 46025f2f-03db-339d-b359-2c49f70e894d | -9.39992 | -40.30594 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c1851481-c616-37c6-9d80-60f3f2117f68 | -10.0016 | -39.17248 | 2026-09-23 03:23:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7251e449-5cb7-309a-9477-bb9f8034ac88 | -9.39792 | -40.31258 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 88b7d257-b82a-3ff4-b2ec-03ff4f3dbff6 | -9.40641 | -40.30724 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b0506cec-fbe9-3a9d-9f20-9e3e5a6e7d38 | -9.40536 | -40.31268 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b6c915b9-3150-359f-85ad-641ce70d6122 | -9.40551 | -40.30837 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 517b6a3a-fc28-3970-bae4-735895f61ed2 | -9.39887 | -40.31141 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2dcc065b-6099-3c1b-83e8-0191f55c8f8e | -9.99559 | -39.17133 | 2026-09-23 03:23:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9ba7452-4f55-3264-a69d-7239eae01b32 | -9.99472 | -39.17581 | 2026-09-23 03:23:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f9d95c88-40ea-3643-854f-3fb2b105b6e8 | -9.39901 | -40.30713 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 351eb698-749c-3d3d-987c-3fd63f2c0790 | -9.40442 | -40.31382 | 2026-09-23 03:23:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 976f65e6-c35f-3bbc-9a0d-bcf090590248 | -8.81972 | -37.35115 | 2026-09-23 03:23:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cfeb0b15-4107-355c-a7e0-97b5704fe2f0 | -11.93815 | -38.29176 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3f0a3576-98b9-3bdd-9bb3-ff90dd564c00 | -11.93745 | -38.29541 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 9a651d4f-12c1-357c-b521-9db6d4507777 | -11.93267 | -38.2906 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6f197f1b-e0b6-3177-b642-2511c130c0c6 | -11.93776 | -38.2916 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| c03eef27-34b2-3f4a-887a-b64059cfe5aa | -11.93704 | -38.29523 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 758900af-7533-3fbe-8fa9-4ca0215f2153 | -11.93198 | -38.29423 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 259c71df-fae2-3a64-a2e0-f9ff41bee927 | -11.93229 | -38.29046 | 2026-09-23 03:23:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8876c234-76b4-3c25-add5-33b25edb8e92 | -16.8462 | -39.18651 | 2026-09-23 03:25:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8812f82-8240-380d-8b70-a2bfec299572 | -15.73975 | -41.89104 | 2026-09-23 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1562ace6-e8c0-3729-a946-fb171dcc2629 | -16.64574 | -42.33139 | 2026-09-23 03:25:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d3db0e0-dc6c-3983-a34d-168954836e62 | -16.63928 | -42.33009 | 2026-09-23 03:25:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90b9376f-5e90-3276-ac45-27d0ab4036be | -15.74088 | -41.88578 | 2026-09-23 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b97eeb9a-80d6-31c0-a5c9-441955059c5b | -8.9165 | -61.4767 | 2026-09-23 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 2b51936e-f90f-3538-beae-72d323862700 | -14.6302 | -45.6403 | 2026-09-23 03:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 39eb3e76-2332-30fd-a096-eae12d3d6a34 | -12.4212 | -46.9777 | 2026-09-23 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |


[Clique aqui para ver as próximas entradas](README40.md)
