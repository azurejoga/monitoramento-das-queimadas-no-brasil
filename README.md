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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c002cf-37b2-3535-97bb-0e38204e6b1a | 2.1767 | -61.8534 | 2025-01-17 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a29b29f4-f244-3d41-8722-485249a92fc3 | 1.3403 | -60.0271 | 2025-01-17 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6db5d0e8-d1e1-3acb-a08b-0c4aa5ab0680 | 2.1767 | -61.8534 | 2025-01-17 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0434ddad-6538-335b-b95c-9576a2eada47 | 1.3403 | -60.0271 | 2025-01-17 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9aade3f7-35b2-35f0-bc0a-26d8d15faeff | -9.9039 | -36.284302 | 2025-01-17 00:10:00 | METOP-B | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2e23456-b3e7-3512-bd60-ab8d585918da | -9.9 | -36.268501 | 2025-01-17 00:10:00 | METOP-B | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27a3484b-eda6-3f42-9405-e79c8619ce22 | -9.8903 | -36.271 | 2025-01-17 00:10:00 | METOP-B | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e2b866b-fa48-354d-820c-b123799d08da | -9.3482 | -35.957298 | 2025-01-17 00:10:00 | METOP-B | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c2a9692d-8191-38f7-994b-56044e3e5e79 | -9.8942 | -36.2868 | 2025-01-17 00:10:00 | METOP-B | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63e7bfaf-bcf4-3188-b0a2-89ec82cf68c5 | 1.3403 | -60.0271 | 2025-01-17 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f0495de3-5217-3488-988b-52818b393d36 | 2.1767 | -61.8534 | 2025-01-17 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b05852d6-876c-346a-9a8e-4c5b15426fb4 | 1.3403 | -60.0271 | 2025-01-17 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d2dadf5c-c830-3038-b294-a0964963a1ea | 0.8299 | -59.7065 | 2025-01-17 00:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3204b387-4db1-326f-8e68-cbdbeef56f8a | -6.427 | -35.1506 | 2025-01-17 00:30:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 107.8 |
| 58b7a557-7a7e-3524-8462-2850bfdba253 | 0.8299 | -59.7255 | 2025-01-17 00:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e14cb7e0-2699-381b-bd97-82b06c66355b | -10.22533 | -36.3391 | 2025-01-17 00:34:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 6c5a6843-8ced-34ae-a864-fd9189311173 | -8.89944 | -35.37988 | 2025-01-17 00:37:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.7 |
| a7ae40d9-15a3-36a1-a2f1-90343cfa4480 | -6.42742 | -35.17336 | 2025-01-17 00:37:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| 732c3e1e-cb2b-3a73-bd93-e7089073d891 | -8.89643 | -35.42112 | 2025-01-17 00:37:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| dbdce68f-e05b-3107-bf15-16a902db664a | -6.42119 | -35.1355 | 2025-01-17 00:37:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 139.9 |
| d6bf3277-d7be-35d8-9e7f-70f59790c7e4 | -8.90507 | -35.41263 | 2025-01-17 00:37:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 84214d72-cd7e-3b58-bb0c-75ab809f1773 | -6.41765 | -35.14125 | 2025-01-17 00:37:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 164.0 |
| 9b4b2e50-746f-3d78-a84a-3e52b8dda112 | -8.89102 | -35.3884 | 2025-01-17 00:37:00 | TERRA_M-M | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| ba316e25-3ff9-3edd-812f-ac81f2e661d4 | 1.3586 | -60.027 | 2025-01-17 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 70f92492-c3f5-3f36-810b-1e92a0cb7608 | 1.3403 | -60.0271 | 2025-01-17 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f979c0a1-715e-3ff8-8bdd-fb8a6ad32a15 | 2.1767 | -61.8534 | 2025-01-17 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1a415e29-7fda-3f18-90c8-c3f1a56389df | 1.3586 | -60.027 | 2025-01-17 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 716e2e65-57d7-305f-bc4a-0a9bc58026d3 | 2.1767 | -61.8534 | 2025-01-17 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8fc05413-03ed-3620-aedf-332368d78ab7 | 1.3403 | -60.0271 | 2025-01-17 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 065f3279-dfeb-327b-a5f7-750b50e4fc4e | 2.1767 | -61.8534 | 2025-01-17 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e99791b5-d3d3-3878-a300-1c29c1ac69a5 | 1.3471 | -60.0205 | 2025-01-17 01:04:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa0cd7c3-e240-35a8-8472-aeb959e549c1 | 2.289 | -60.2234 | 2025-01-17 01:04:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e5412a79-d810-3bc4-bf1a-d51fe10925dc | 4.145 | -60.2659 | 2025-01-17 01:04:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef465dd-786e-384d-9de9-8bbc2839d2ea | 4.2899 | -60.3521 | 2025-01-17 01:04:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 13ae88af-cbd4-32b0-bf35-8bb5ef544408 | 1.3451 | -60.029301 | 2025-01-17 01:04:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e5de60fc-11ec-3241-a492-7a113d9d6973 | 2.1805 | -61.839298 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4e0fe9b-3f57-37d0-ad88-d85b4a91df77 | 2.178 | -61.850201 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1b4d09-e0d3-30df-b667-72cf5d773fb5 | 4.1187 | -60.024799 | 2025-01-17 01:04:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0325d86-6c76-3f3e-b585-51caf21395cd | 0.8192 | -59.719898 | 2025-01-17 01:04:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4d190406-2a4b-3d9b-bf31-783dc63e2cd1 | 2.1656 | -61.859001 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6fff4fae-b06f-3ce2-8b78-0f97ef60b7a7 | 0.8211 | -59.711399 | 2025-01-17 01:04:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3ce317-f509-3e6d-b7f8-4f4656793ce1 | 2.1682 | -61.848 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a60b8a83-de1c-3ccd-8cff-be68b5c1074e | 2.291 | -60.2146 | 2025-01-17 01:04:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5904e789-3c4e-33b3-9175-65a83fefb83e | 4.2879 | -60.3605 | 2025-01-17 01:04:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 21f6e55e-92eb-3209-8a52-00e2f6c5e737 | 4.1333 | -60.271999 | 2025-01-17 01:04:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 17d0a710-8002-3e67-b52d-78fe38f140cb | 4.1168 | -60.033001 | 2025-01-17 01:04:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bf8bae3f-6be7-3c4d-9b05-dd2594351ee2 | -15.615 | -57.345901 | 2025-01-17 01:04:00 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4460eb63-19f7-3e0f-97b8-d8d89b7e24f4 | -0.1548 | -60.868099 | 2025-01-17 01:04:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3cae729a-3f64-326b-bf1f-53a1c71fd204 | 1.9015 | -60.5616 | 2025-01-17 01:04:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b6e7f1bf-d9f9-3ca4-8ebc-6be3554127f9 | 1.8994 | -60.570801 | 2025-01-17 01:04:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e95054f-810a-349f-aeda-b796ffb52355 | 4.1266 | -60.035198 | 2025-01-17 01:04:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4697da16-ac5f-3814-ae33-9c777ad3fbf3 | 2.1856 | -61.817402 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ad4588f2-524a-3217-9c24-7b55671a7827 | 1.3431 | -60.038101 | 2025-01-17 01:04:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 289327f0-81c1-3cee-a196-28e01ce0fb97 | 2.1754 | -61.861198 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fdb98a5d-68c2-3fee-bbf7-a9c9baa02176 | 4.1352 | -60.263599 | 2025-01-17 01:04:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2f38c742-2e0c-3300-bb7b-72e84ab07d19 | 2.1882 | -61.806499 | 2025-01-17 01:04:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe29581-ae9a-30fa-8cda-d337bebbdc40 | 2.1767 | -61.8534 | 2025-01-17 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 79b69294-4769-3a68-9cdd-e877d0bbe75d | 1.3403 | -60.0271 | 2025-01-17 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a83aaeda-7ef0-362a-ac74-db4810ed6128 | 1.3403 | -60.0271 | 2025-01-17 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d00dc9c2-9e82-3bde-a5c3-6a9b4b2215b4 | 1.3664 | -60.0266 | 2025-01-17 01:49:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 77eb0698-0f0f-3b24-bfe1-d4a937d19774 | 2.192 | -61.855202 | 2025-01-17 01:49:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7aadac45-1cbd-3481-8f17-134358c8181b | -8.9193 | -35.42616 | 2025-01-17 02:57:00 | NOAA-21 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7af51241-1f8f-33ce-85f0-82f7860a0ccf | -5.38241 | -36.46363 | 2025-01-17 02:57:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0e5b6872-a202-32f4-a77a-3565b53fd471 | -8.91345 | -35.42504 | 2025-01-17 02:57:00 | NOAA-21 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 02f4dcac-5efe-376e-ab7a-afc9eb9cfbdb | -5.3834 | -36.45798 | 2025-01-17 02:57:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 98a4454f-5990-38bd-b37a-91a19708d0d5 | -6.8031 | -35.17927 | 2025-01-17 02:57:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 11cfa958-f34b-304e-9858-e4a8fe7ae484 | -6.80469 | -35.17057 | 2025-01-17 02:57:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 55461e1a-49d5-3c5f-86f1-784f104c26d1 | -5.38109 | -36.45928 | 2025-01-17 02:57:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 572a868d-9fbc-34b0-89b2-373d3ce6df77 | -6.80389 | -35.17493 | 2025-01-17 02:57:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| cf636cba-0cb9-3af8-9ec9-7c598d0d2102 | -8.55349 | -36.62905 | 2025-01-17 02:57:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 082ca3af-037a-3c76-9346-06dc29ada40d | -22.67584 | -42.8649 | 2025-01-17 03:04:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 92a366db-aae3-3279-be10-8d5b6cf811d0 | -22.67768 | -42.85778 | 2025-01-17 03:04:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 3808651d-579f-333a-a82c-b96dbd351463 | -7.98085 | -35.21915 | 2025-01-17 03:23:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| d511cecb-a06e-3430-8f62-d209c94be573 | -8.55026 | -36.62949 | 2025-01-17 03:23:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3b637d9-b33f-35f0-ac02-7d62a50a58cd | -8.4941 | -36.37008 | 2025-01-17 03:23:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 89223e8f-9813-34a5-b1b2-ba8b0a9320ba | -7.03462 | -34.84405 | 2025-01-17 03:23:00 | NPP-375D | CABEDELO | PARAÍBA | Brasil | 2503209 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fb81d30f-ab9b-33fc-9594-e16c1e1b385f | -7.83988 | -35.20296 | 2025-01-17 03:23:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b2c9c8d0-4b36-31ea-9a6a-0ba8eff0e9ef | -7.82084 | -35.17511 | 2025-01-17 03:23:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f5f8abf9-510e-3d43-940c-e63bcd9264ba | -8.55083 | -36.62847 | 2025-01-17 03:23:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4addc514-e7a9-3bcf-b377-b21b434ca427 | -7.98166 | -35.21432 | 2025-01-17 03:23:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 65d0b2e3-ae6d-377c-8cce-8b001faf25a0 | -8.55013 | -36.63242 | 2025-01-17 03:23:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d50752ce-95ad-3800-9415-69e06f3c4909 | -5.38147 | -36.46061 | 2025-01-17 03:23:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1be92142-488b-3bf5-b2af-faba2b9a2a5a | -8.91258 | -35.42386 | 2025-01-17 03:23:00 | NPP-375D | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8e90d3e4-8dca-353b-bc0b-0888d07226e9 | -7.82002 | -35.17989 | 2025-01-17 03:23:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e295b5c7-b71a-3747-8cf7-d1a0d8679a81 | -8.91643 | -35.42453 | 2025-01-17 03:23:00 | NPP-375D | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 8f473f24-3ccd-39ba-9e13-6ceba9128694 | -8.49672 | -36.37003 | 2025-01-17 03:23:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 208d35bd-a79d-3063-b640-ba3ef4fc12a6 | -5.38217 | -36.4565 | 2025-01-17 03:23:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b1b5180d-6eeb-3d09-a65c-db0920b85c09 | -7.69724 | -35.18971 | 2025-01-17 03:23:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 08f8820c-5d29-37db-a789-6ddd476d7d86 | -7.98471 | -35.21976 | 2025-01-17 03:23:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0ddaac88-4076-311e-968c-b813e7c4cb93 | -5.30073 | -35.99202 | 2025-01-17 03:23:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40e3b419-8307-3ac7-8fe3-f8cf42a9d29b | -7.01863 | -35.17583 | 2025-01-17 03:23:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ce04e76-393e-356e-83b7-d04566b15eaa | -7.81514 | -35.17685 | 2025-01-17 03:23:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 193d739d-cefb-34c6-bfe5-697fd264a40b | -7.81899 | -35.17752 | 2025-01-17 03:23:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 78d07fcc-80ba-34d9-a99b-db72cbaea1b6 | -22.74953 | -43.33823 | 2025-01-17 03:27:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 454cd86d-2854-31da-84fb-2413a6fce074 | -22.67638 | -42.85882 | 2025-01-17 03:27:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e8bcf59e-e285-3849-b58d-d44b6e8a2d38 | -22.74999 | -43.33283 | 2025-01-17 03:27:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f42e3898-865f-3356-b397-9cdff9d817f4 | -8.49493 | -36.37032 | 2025-01-17 03:46:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e9d915f8-018d-35c7-ac0f-cebbdbee1919 | -5.38169 | -36.45601 | 2025-01-17 03:46:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d8124611-2b0f-3d35-bcd9-7aaf548f89f9 | -7.03465 | -34.84698 | 2025-01-17 03:46:00 | NOAA-20 | CABEDELO | PARAÍBA | Brasil | 2503209 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d9ba4ed4-b3cb-39b9-a975-e3fc483f571a | -7.81388 | -35.17802 | 2025-01-17 03:46:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
