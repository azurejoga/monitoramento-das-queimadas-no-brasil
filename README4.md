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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4acf79f6-c37a-3156-8fdb-cf7c7f7cd12a | 2.71218 | -60.23476 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a90bb7ca-1086-3e7f-8346-d2e26f9d0aa7 | 3.04721 | -60.12956 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b37640c4-864b-30ce-8974-d343063d68f3 | 3.48051 | -59.82937 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04f6161e-3048-348c-89d2-79b9e5055e74 | 3.22667 | -59.94916 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 495d4358-8d4e-3d91-9907-120f09510e36 | 4.14405 | -60.88198 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c10569fe-3d34-3f5a-bb9f-c520e95883ea | 4.14459 | -60.88049 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2357535f-a1ea-387c-b9e7-635dda14c5c2 | 4.14025 | -60.88744 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f761dab1-301f-38ac-9bf8-058a09227359 | 2.68999 | -60.22163 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e830820d-b626-36e9-91aa-2a45b309fb45 | 3.21057 | -59.97491 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0fb4288f-193a-3f52-8ea8-3d1c113d4b0f | 3.28455 | -60.10435 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 051f11ac-9c17-38a5-b8cb-af8c554170b1 | 3.44841 | -60.74446 | 2026-02-22 06:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8369cc-9f07-3a00-a1cf-1b0518af0b8d | 3.04659 | -60.14168 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0dc68d1-8b9b-387e-a2d8-756ed9b43ac2 | 3.04972 | -60.12991 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 168f1583-5f91-352c-946f-f25d80a53db6 | 3.23967 | -59.93541 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b841b6c-6403-33ab-9413-591b79af73a3 | 4.08109 | -61.14745 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 657f4ea9-b694-35d1-8549-8a51ccb5df42 | 4.08631 | -61.15111 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a2c7f5d-a302-39fc-a103-0af48c596481 | 4.08787 | -61.14831 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21a37b39-bb75-3966-88f3-62fef667ba03 | 2.64254 | -60.11643 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 074c67c1-f718-30f2-9fc7-5d7c8f7a22f7 | 3.0506 | -60.1354 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4efa96af-2c3b-3695-bc70-c15369326043 | 3.2192 | -59.95553 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84fbcf74-9539-3cbe-a184-c21501306eac | 3.22412 | -59.95467 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5327ad95-53bb-3411-a69c-395d268f9ee7 | 4.08338 | -61.14902 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c75b978-0278-3ece-8765-3d67e4b8d70f | 3.04813 | -60.13506 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5fcfc66-006f-32b5-8548-09e5cb086dcc | 2.76879 | -60.2863 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| acb2a914-d3e6-355b-9b60-ec07a0180a7a | 4.14102 | -60.89218 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| db7c859f-aea2-3864-bcaa-846a761ee913 | 3.20967 | -59.96934 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4b2405d2-2106-3a44-b1dc-2228d4f4a29a | 4.21333 | -60.12471 | 2026-02-22 06:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e6ee3bd-6f1e-3942-9641-35351688a023 | 3.04905 | -60.14051 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b756a40-95e9-362a-aff0-bdffe7122df6 | 3.48499 | -59.8257 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65965667-1f12-3dc2-b1d4-2ec2258faa73 | 3.28362 | -60.09873 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8dc7c53f-2033-38de-9b2b-e6218f59931a | 3.21369 | -59.96293 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c86fd702-2bf3-377b-86cf-b0c1c756372a | 3.22014 | -59.9611 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c17a9784-e2e6-3757-96f0-740cb19ad89f | 3.24596 | -59.9337 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 740c024e-e968-34de-bc85-ebd483669dc9 | 3.19156 | -60.43167 | 2026-02-22 06:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eea29ec1-8073-3004-b5d5-adb4216160e3 | 2.7073 | -60.23561 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c6561f29-0255-36ca-b229-79b8c2947987 | 3.22925 | -61.19736 | 2026-02-22 06:01:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b16cc17a-2edd-301e-b7a3-38449c3ed0ae | 3.21862 | -59.96207 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14e8c7d5-a250-302a-8e1f-3484cadef5da | 3.48546 | -59.82854 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27cb0649-0992-3719-bcfc-6bb0e947c88e | 4.14163 | -60.89067 | 2026-02-22 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 495c4686-2f62-343f-bfc7-8943e42dc317 | 2.76969 | -60.29171 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26fca326-a961-39e7-9aa4-04d7124ef55c | 3.22264 | -59.9556 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e71cd0b-2da9-3fdc-ae0d-54db84dbb43e | 3.23026 | -61.19537 | 2026-02-22 06:01:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 950c10e5-ae96-302c-a49c-41816dcc3aa1 | 3.23102 | -61.19994 | 2026-02-22 06:01:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 578a6f7c-88a6-3f48-8d18-ce8bd82706fe | 3.04571 | -60.13624 | 2026-02-22 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d3d7638-02d2-3556-bf40-36e0413b35b9 | 1.4316 | -59.9503 | 2026-02-22 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| f86e4aa1-aa6b-3dc4-b3e4-b13979b12e85 | 1.4316 | -59.9503 | 2026-02-22 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 041a9158-c1fd-3439-81f8-aad117eaef88 | 1.4316 | -59.9693 | 2026-02-22 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 4313e78e-526b-3a68-8a90-208ee77c451b | 3.29541 | -60.20361 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6baa19ce-638b-3774-8b5e-b8aa4b1fea50 | 3.27946 | -60.09968 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2ddbaa70-e840-37a9-abc1-974e84574baa | 3.21171 | -59.95837 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64758fa8-3fd2-3551-9192-c3ba6c6ce1a7 | 2.70839 | -60.23679 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 16762801-28c9-3222-ae50-f81885fefb01 | 3.05303 | -60.13173 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 96cf623f-c36c-30ea-a22e-f3f406074dc4 | 3.2209 | -59.957 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a328fec7-d93c-3df8-9d7c-d1e4943f71c6 | 3.21317 | -59.96802 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8b2f0ce5-be9a-35c1-b230-3e9ac1d51593 | 3.28858 | -60.09833 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa6b8f61-f51e-3f5b-8d43-e4a5b268dabb | 3.22235 | -59.96665 | 2026-02-22 07:22:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 424b7d6f-1cc0-31a2-b9c7-75fd8c5d2c3a | 1.21192 | -60.61485 | 2026-02-22 07:22:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eee94d45-3b9c-39b2-bd3b-7cd87ac457f4 | -19.8861 | -57.8615 | 2026-02-22 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 2d49851d-bfbd-39ac-ac3c-dbb38109e201 | -19.9062 | -57.8588 | 2026-02-22 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| e25d6b17-7f54-35b9-bf13-71a1d3c06e81 | -19.9066 | -57.838 | 2026-02-22 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 1bca02ef-0ee3-3461-9824-5f981be7f10a | -19.9062 | -57.8588 | 2026-02-22 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 8e0c0b70-72dc-3c4a-aa61-d47068297ec3 | -19.8861 | -57.8615 | 2026-02-22 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 8709dfab-5614-3092-81a2-72a0a983126e | -19.9062 | -57.8588 | 2026-02-22 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| cfa801e0-303b-338d-bbc9-d58a6b39d1a5 | -19.9062 | -57.8588 | 2026-02-22 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| df78425e-8983-3c69-91c0-d1109ed0e7c6 | -19.9066 | -57.838 | 2026-02-22 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 12f673dd-2e28-30a0-97c3-5185077d71a8 | -19.9465 | -57.8534 | 2026-02-22 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| e35b28ae-c9a7-3172-b05e-bac24fd11ce2 | -19.9461 | -57.8742 | 2026-02-22 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 5ce435ee-a0f3-37f6-bcb1-633dbe8bdb0a | -19.9062 | -57.8588 | 2026-02-22 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 4d94b53c-3b1d-3180-a483-7d433d136739 | -19.9461 | -57.8742 | 2026-02-22 09:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 95b4a369-6517-3fe2-bf2c-8e52153b4cb9 | -19.9062 | -57.8588 | 2026-02-22 09:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 947490c1-7cd0-3f7a-be40-8a3660160356 | -8.02863 | -36.34339 | 2026-02-22 11:12:00 | TERRA_M-M | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 4a2b6773-e282-3faf-9869-b01a0d341a46 | 3.48125 | -59.83083 | 2026-02-22 12:46:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 03062320-c0cc-372f-a67b-0aa43299ac27 | 2.76964 | -60.29482 | 2026-02-22 12:46:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4079998a-a685-3bbf-ac4d-19e8d90b8ac6 | 2.76786 | -60.28231 | 2026-02-22 12:46:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 92b68535-90e1-3520-9d68-334b50c17671 | 3.27529 | -60.11212 | 2026-02-22 12:46:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b28864fe-c24d-32b8-b5d5-e4e45023b161 | -11.77474 | -55.47273 | 2026-02-22 12:53:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4b3226dd-017f-3383-9f69-8b7ecde2c689 | -19.89419 | -57.85562 | 2026-02-22 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a004cd2b-c916-3a31-bff0-644cb1225159 | -19.91425 | -57.8583 | 2026-02-22 12:55:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.5 |


