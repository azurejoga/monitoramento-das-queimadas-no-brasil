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
| 1495308d-f06c-3a6d-91ae-3b192a51a933 | 1.0663 | -60.6174 | 2024-11-13 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 53f56374-0940-37bc-a541-0f1f2078ac0e | -2.7033 | -49.33 | 2024-11-13 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 67f2a2b3-10da-3fd0-a58e-5280db3bd5c5 | -2.248 | -53.7426 | 2024-11-13 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| e07c4e64-9ccc-3dc8-98ac-f621af8606b0 | -4.4265 | -48.8395 | 2024-11-13 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a904f255-0cec-36df-9ea6-c95785acabe8 | 1.0663 | -60.5985 | 2024-11-13 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 366b8f68-25bd-3fc2-b17e-793633250ef5 | -3.5316 | -54.4957 | 2024-11-13 00:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| a4440e30-6404-3962-b168-f647a145aad8 | -3.5743 | -53.0015 | 2024-11-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| b940b3e7-d31a-3a98-bc83-957038cd8ce6 | -3.4914 | -50.8213 | 2024-11-13 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| cabf4db0-dade-3a70-aa10-809f4dadb2f8 | -2.7374 | -45.2877 | 2024-11-13 00:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6433430b-68ce-3070-acaa-a2095f237994 | -3.4913 | -50.8421 | 2024-11-13 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 11988e4b-fce4-3238-ac77-5f9c111a293b | -3.0688 | -50.3536 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 27d6587b-d096-3513-9cad-f687d975d334 | -2.7033 | -49.3513 | 2024-11-13 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 83b951ab-cdf2-30d6-ab6d-d45ff3bc0224 | -2.7777 | -54.7343 | 2024-11-13 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 373484c9-c5e9-35db-947d-78f498824537 | 1.048 | -60.5986 | 2024-11-13 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 56c22024-46a3-3bd5-9443-1edf4ffcb7ed | -3.5743 | -53.0218 | 2024-11-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 2337fddf-07f5-3b49-a8aa-046d5a2e65c5 | -2.2112 | -53.7432 | 2024-11-13 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 48796ff6-0c44-3374-af12-de67b816e8c0 | -3.132 | -59.029 | 2024-11-13 00:00:00 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a511e806-6827-357d-87e8-9d26d0e99007 | -2.7189 | -45.2883 | 2024-11-13 00:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0bab11ae-a543-398b-b4c6-2e8338db91a9 | -3.5099 | -50.8207 | 2024-11-13 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| ea5c1762-ee33-3374-b30c-8d9f579b3e58 | -3.0504 | -50.3332 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 1fb56e4b-218c-3cb9-aa0f-3faffe4d0312 | -3.5098 | -50.8415 | 2024-11-13 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 48303bc1-a0eb-35d4-9b18-06eb42f7aa0f | -3.0504 | -50.3542 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 9a000e25-8270-3697-80af-48d73c836992 | 1.048 | -60.6175 | 2024-11-13 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c13d90bc-bd94-3c5a-8a84-a2a007afdc21 | -20.6364 | -47.4087 | 2024-11-13 00:00:00 | GOES-16 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1830b14f-884e-3cea-a3a5-0d2d66067241 | -3.3519 | -48.9475 | 2024-11-13 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b04ed3cf-1044-34d0-b10d-3ac69f266f77 | -3.6791 | -50.1653 | 2024-11-13 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b1fc0974-3e56-3ab9-86c3-cdd50f7d19fd | -3.1501 | -53.2371 | 2024-11-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e27ab42d-86c7-378e-acdf-e426e3312a22 | -3.9483 | -48.1724 | 2024-11-13 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 53e536b8-fe8e-39c0-bcb5-68accfb2d239 | -4.6551 | -45.1325 | 2024-11-13 00:00:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 97acaca6-45ef-3933-be86-179e652ed9fb | -3.1096 | -54.3066 | 2024-11-13 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 20b01ee3-f2bb-3832-a76d-f009b08fc1ef | -4.4264 | -48.8609 | 2024-11-13 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4358f4b5-d3bd-3368-ba56-e2a9203701db | -5.3587 | -43.529 | 2024-11-13 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 6664db08-1232-3f79-805b-1fb106152e35 | -2.9821 | -53.9684 | 2024-11-13 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f99fc6a0-7cf2-396c-b298-cd09413eabcd | -1.6627 | -52.5357 | 2024-11-13 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 370737fe-737e-31b4-a9df-f41df5c435aa | -2.2479 | -53.7627 | 2024-11-13 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 2dae43ec-3e29-3551-a0d9-d398ef244fa2 | -2.2296 | -53.7429 | 2024-11-13 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7c7c904a-4d31-34f2-bfc1-2b42feb270c4 | -3.1602 | -50.5812 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 587725f0-5cb8-394c-9e7d-bebffb186a9a | -3.1501 | -53.2574 | 2024-11-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| e4860ea8-947d-3191-b4d3-0fbe1aaa8101 | 1.0481 | -60.5796 | 2024-11-13 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9e11a913-dca5-36d5-a8f1-0ade17882f2e | -3.0689 | -50.3326 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3362e50f-e65b-3ced-9219-78672cc6ae0d | -3.769 | -50.6863 | 2024-11-13 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 4ae4e67e-8549-38aa-9c1c-549ce9aba6ef | -2.9925 | -51.0242 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 80570747-0a29-3590-999b-fe0f0399cfce | -2.9924 | -51.045 | 2024-11-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6152fa9f-fc4d-372e-a58b-6e9c0e212748 | -1.6444 | -52.536 | 2024-11-13 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7193740b-429c-3d0b-bb77-5907d992148e | -3.1321 | -59.0098 | 2024-11-13 00:00:00 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| dbd4be0c-10fa-33b3-bcce-de369ae5a6c4 | -10.56183 | -36.72754 | 2024-11-13 00:00:00 | TERRA_M-M | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| d96b43eb-8724-394f-af00-10f07182a1a2 | -10.82825 | -44.36734 | 2024-11-13 00:00:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 10e5e9c0-3809-36df-aac9-f08db18a785c | -9.0108 | -36.1222 | 2024-11-13 00:00:00 | TERRA_M-M | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 0361f346-efcf-374c-af4f-0e126df83768 | -9.03712 | -35.6355 | 2024-11-13 00:00:00 | TERRA_M-M | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 37ba0707-9b1b-3c86-9e8c-08ec197361f3 | -9.03837 | -35.64472 | 2024-11-13 00:00:00 | TERRA_M-M | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| af186e01-4188-3728-986f-91f44e221bb9 | -8.49536 | -35.24859 | 2024-11-13 00:00:00 | TERRA_M-M | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| e6916a45-0e61-3cfb-b491-7c250ca02700 | -10.04449 | -36.35889 | 2024-11-13 00:00:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 97a9fcd7-de01-302d-ac82-8d9998ea3ff4 | -9.50796 | -36.05183 | 2024-11-13 00:00:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4d01b3c3-0bd6-3572-a7d6-f90dec715b45 | -10.04318 | -36.34891 | 2024-11-13 00:00:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 5.8 |
| efadbf52-767e-39da-bda0-60ef1196c6e8 | -10.04581 | -36.36887 | 2024-11-13 00:00:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 190293d4-ca1e-354c-a666-6192dda697b6 | -9.01994 | -36.12093 | 2024-11-13 00:00:00 | TERRA_M-M | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 465f67a4-844a-3799-a41d-3cf0e54588fc | -9.50926 | -36.06138 | 2024-11-13 00:00:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 09292393-6c8a-3637-8e88-ad782c40f377 | -8.00678 | -35.11185 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 8e745405-d11f-3888-9998-a99a9a9913d8 | -8.11742 | -38.62336 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 85b61a3f-e407-39e3-99ff-67cb35f0c758 | -5.2469 | -37.68926 | 2024-11-13 00:02:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 66.2 |
| b7c00b15-54e8-31da-a29c-0dda48442f72 | -2.71712 | -45.27795 | 2024-11-13 00:02:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| a26ea3c5-a1c2-34dd-a120-6e23e2080d96 | -7.56036 | -35.27843 | 2024-11-13 00:02:00 | TERRA_M-M | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 8a0ff10c-5d20-3f3f-99b9-a1a8359bd76c | -4.20491 | -42.33513 | 2024-11-13 00:02:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| ba978656-e5ea-3a42-8747-aab8614b8407 | -2.72175 | -45.3127 | 2024-11-13 00:02:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b681cc26-69ef-35b5-923d-0ff8a92f516c | -3.54722 | -40.72282 | 2024-11-13 00:02:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ab71f048-2834-3406-a48c-78eff590cca7 | -3.43377 | -43.46099 | 2024-11-13 00:02:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5fb2f170-316c-39ff-a65d-1ff856e4cbf7 | -7.08032 | -35.26857 | 2024-11-13 00:02:00 | TERRA_M-M | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 29428ace-3513-3349-a57d-2ffbb3f479a0 | -5.60271 | -35.56687 | 2024-11-13 00:02:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 26ec2b3a-48d8-37a8-8e0b-6b58fc8f71af | -2.73174 | -45.31695 | 2024-11-13 00:02:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c924065b-4ce8-3997-a8ae-1e09b2224eaa | -7.47009 | -37.52227 | 2024-11-13 00:02:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0c6d9ece-0998-3421-8446-4a77c75ef08f | -7.00693 | -34.93541 | 2024-11-13 00:02:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 38a90af1-fb9c-355d-a57b-d888ec63aa8a | -3.25522 | -43.26843 | 2024-11-13 00:02:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 00def27a-58e3-3c9c-9a91-bcd3c22382ac | -5.24274 | -37.69608 | 2024-11-13 00:02:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 877ded16-f62e-3e75-8825-4b36074c4157 | -5.31571 | -39.63546 | 2024-11-13 00:02:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 167218a2-550f-3196-9f88-ae90dbf37aaa | -5.35653 | -43.54741 | 2024-11-13 00:02:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6a0e901f-3508-3217-8d9c-42049b5494f2 | -5.24827 | -37.69951 | 2024-11-13 00:02:00 | TERRA_M-M | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 6f66d75b-2cd7-30f4-9127-7dfca9ec4b36 | -7.08155 | -35.27746 | 2024-11-13 00:02:00 | TERRA_M-M | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 80.5 |
| accac03c-5868-37f7-bb32-198b31f809bb | -4.68211 | -44.5734 | 2024-11-13 00:02:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| bfecc97d-2e41-3027-8724-f453a3560c2a | -2.72685 | -45.28231 | 2024-11-13 00:02:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| f022d4b5-d230-3e08-a58e-f7671eeec8a1 | -5.35291 | -43.51973 | 2024-11-13 00:02:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 07c3864f-acec-3bdb-ae73-71bd617f51b9 | -7.74679 | -35.29436 | 2024-11-13 00:02:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cfe1dc66-a605-3587-a89f-a0aa4acd7cb8 | -5.79796 | -35.58129 | 2024-11-13 00:02:00 | TERRA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 9522a76c-2064-30bd-bd6e-11f67b8468ff | -4.67346 | -44.58103 | 2024-11-13 00:02:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 877c6533-e570-34b8-bc4c-ac356b39e496 | -3.34773 | -42.48207 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ef2911d7-62a4-32d0-86d8-541c9b5573de | -3.25095 | -43.27563 | 2024-11-13 00:02:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| c061abb2-44b9-36db-a14c-60617c9d4aaf | -3.31779 | -40.04321 | 2024-11-13 00:02:00 | TERRA_M-M | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f3e759ce-1df9-32e0-a36d-fbb34e3c8082 | -3.34493 | -42.46101 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d7858503-7c02-3459-87b8-ab3e732be8fc | -7.99792 | -35.11311 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| f7a6b53d-86e2-3579-941d-08b1734c474a | -5.35602 | -43.54219 | 2024-11-13 00:02:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d144cb89-3271-39ed-bbf1-158318d7da72 | -5.60148 | -35.55801 | 2024-11-13 00:02:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 623db773-494a-3bfc-a7ff-a90178571342 | -4.20203 | -42.31396 | 2024-11-13 00:02:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| c8699506-5243-3315-9ccf-bdce5a917c1c | -8.123 | -38.61639 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e664a431-b79b-3200-a004-32f74f8189f6 | -7.99668 | -35.10421 | 2024-11-13 00:02:00 | TERRA_M-M | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| dc1bc4ec-c8a5-3aba-9681-8a3408b97d74 | -7.50994 | -34.8507 | 2024-11-13 00:02:00 | TERRA_M-M | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 9a546746-feef-3d4a-b50f-fe61d6d79da2 | -4.20106 | -42.32907 | 2024-11-13 00:02:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 2c1ba52e-c175-34d3-be71-6f47db5046d4 | -2.73815 | -45.31066 | 2024-11-13 00:02:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 203c83e0-8715-3b23-b1ff-79c298a7a68f | -6.7358 | -35.03738 | 2024-11-13 00:02:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 039cf292-c37c-3c1e-9343-d57e378dbe58 | -7.00816 | -34.94427 | 2024-11-13 00:02:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| a79ad042-e63e-34e3-b28d-0a49067543f9 | -5.61024 | -44.88049 | 2024-11-13 00:02:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| b4df6e30-7d0e-3e46-8841-b5ec7e3e450c | -3.24757 | -43.25126 | 2024-11-13 00:02:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |


[Clique aqui para ver as próximas entradas](README2.md)
