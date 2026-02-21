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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16d68491-4287-317a-976b-b3f86387f86f | -0.15699 | -60.74756 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76de5746-fef4-3440-a91b-eac12399a624 | 0.73748 | -60.10692 | 2026-02-21 05:31:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8077ab47-41ee-3c9f-8c80-a5d0a3a303fc | 1.44441 | -59.9569 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de7ea512-1f88-3dca-b645-650774a21988 | -0.15645 | -60.75099 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b436642-5a75-3f40-8404-86b8a2f2e4a8 | 1.45158 | -59.95931 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0341e1c6-62b8-3319-9e32-93e827c5f586 | 0.94451 | -60.27907 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bc7cc0d-a11d-3348-bef8-c0fd1f20377f | 0.45109 | -60.40222 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84b318b1-0d7b-31fc-9923-48dd65b74382 | 0.45493 | -60.40514 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34de257e-f4fb-3d94-84f3-9a201f09da5e | 0.0724 | -60.65154 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efdaff4f-3ce3-3911-88cf-b1906acf5e92 | 1.05526 | -59.49745 | 2026-02-21 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a77383e-4bdc-39d5-868d-98ca9424366d | 0.45163 | -60.40565 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1db4464-188e-3fe1-81a1-e5afc8b29999 | 1.82963 | -60.84589 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759a35e4-5699-3584-b91d-c075d0e06567 | 1.82687 | -60.84985 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57edfd9e-c620-3973-8035-244e70e79c5a | 1.44772 | -59.95638 | 2026-02-21 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73fd01ca-7315-3e15-a239-e43034ca9483 | 0.07186 | -60.6481 | 2026-02-21 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4fead29-505d-3f7b-901a-9bd685e94f6a | 0.68148 | -59.55972 | 2026-02-21 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13e5b02d-439a-3957-93ac-451140089177 | -5.14817 | -60.372 | 2026-02-21 05:31:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c57447da-e311-3e3d-bf1f-d95edd378ba1 | -15.5971 | -59.29473 | 2026-02-21 05:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1893ce76-cf44-3b7a-93f3-59826233173d | -18.97022 | -52.92782 | 2026-02-21 05:33:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8aef2185-8ab7-3fd4-8925-bfb5f31e9282 | -15.60112 | -59.29534 | 2026-02-21 05:33:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e928041-744f-3cbb-bf2a-2e972a3e2173 | -18.97658 | -52.92832 | 2026-02-21 05:33:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c27261e1-f287-3947-a346-a3ecc324e689 | -18.97325 | -52.9252 | 2026-02-21 05:33:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79d566ed-381e-3067-9eb5-e87b2ef5fed0 | -18.97275 | -52.93073 | 2026-02-21 05:33:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b220418-b28c-36a6-9dfa-f190ccaf3d77 | 2.7088 | -60.2398 | 2026-02-21 05:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f0b87e6d-920d-3f0c-afea-d1fcecd8a4d2 | 2.56687 | -60.55886 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf31968f-845f-3aad-844f-49b022c5b902 | 2.674 | -60.40769 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 902dcaa7-415b-36cc-a32a-dbab0aa533c5 | 2.70492 | -60.23047 | 2026-02-21 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3996f884-af6d-3d32-b552-7c8ce6961119 | 2.55565 | -60.73066 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7aa42190-3e66-3b93-9a51-da5bb1212d94 | 1.93954 | -60.36631 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1708486a-f8e9-3d72-8d48-f4a2832efce9 | 1.94338 | -60.3708 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe4c97e1-17f6-3e3a-b411-f5d158c43193 | 2.67509 | -60.40649 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eab2d9b5-ff18-32eb-8465-36fbd2859fce | 2.67604 | -60.4122 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b27a51e3-1530-389f-a402-06257f2d7688 | 3.08228 | -60.09929 | 2026-02-21 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a46cc9c0-6caa-34ab-ba93-691cb7b90838 | 1.94246 | -60.36508 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09de2e9a-2a57-35e4-b4b5-69b97e19c653 | 2.54919 | -60.73175 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18d8cb9c-99fa-3687-bf5d-be117915ee3b | 1.9358 | -60.36628 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef382426-7e6c-3f62-bf59-336b045400f6 | 1.94051 | -60.37204 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fbd01e4-5bbc-34d4-b1a6-a3b0ddaa689d | 2.55657 | -60.73608 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e0b0121c-78d7-3bf9-abc1-c59b58a761fd | 2.68154 | -60.41222 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2fb29a34-b8b3-3c48-ad0e-82999c695ae0 | 2.6826 | -60.41101 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff945c96-7b4f-3bc0-ace0-4c29bf6a6eb5 | 2.54885 | -60.73369 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f3ac44ea-239e-3fb3-bc3d-fea0c2343df7 | 2.7059 | -60.23627 | 2026-02-21 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47d6195d-19d8-37d1-babd-ec82ed616ffb | 2.55012 | -60.73721 | 2026-02-21 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34402d99-38af-34fa-9f2e-da6eab8ce287 | 2.7088 | -60.2398 | 2026-02-21 06:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 24f4b980-f7a7-348f-9d70-cf6f499d012f | 1.3669 | -60.31221 | 2026-02-21 06:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a28ac83-000e-3d94-b6e1-a1bde015e7e4 | 0.45215 | -60.40456 | 2026-02-21 06:20:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36c4aa37-e0c1-3798-8d12-f6b2365a6f76 | 1.3766 | -60.31203 | 2026-02-21 06:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f65a286-5727-3e4b-bda3-67bec51d5d00 | 1.36985 | -60.31314 | 2026-02-21 06:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5257c0e6-a42b-3b9d-9232-58862cce16d5 | 1.37939 | -60.30381 | 2026-02-21 06:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8d3fa6f-bec6-3b6d-b4a2-43e8ba4d7e2c | 1.38232 | -60.30484 | 2026-02-21 06:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a67c671-be7f-303e-b2a3-96940e334e48 | 1.38037 | -60.30991 | 2026-02-21 06:20:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efb60ed2-7118-3013-ac8f-6419903a26b8 | 0.45118 | -60.39839 | 2026-02-21 06:20:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44045047-abd7-3437-b83b-4ead83830606 | 2.7088 | -60.2398 | 2026-02-21 06:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 969899c9-614d-3870-ba0a-5e685cffb3bd | 2.70236 | -60.22504 | 2026-02-21 06:44:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 27.6 |
| c6999158-2a6d-3744-ba26-8dcd209d6708 | -20.79648 | -52.06758 | 2026-02-21 12:14:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b337c1bd-58c0-38f1-8adc-c66ebd5da6f5 | 2.6542 | -60.1265 | 2026-02-21 12:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| caa41e24-8525-3ae9-95b3-5af12749048b | 2.6542 | -60.1265 | 2026-02-21 12:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 22ec6e2b-202b-33d8-8855-e6d64e862531 | 2.6905 | -60.2211 | 2026-02-21 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ee26643a-a44b-3fc8-bcb1-256fc29dcbf8 | 2.6905 | -60.2401 | 2026-02-21 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 22c85b3c-2bca-3fac-b5b9-9648920a6f0c | 2.6905 | -60.2401 | 2026-02-21 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5f746f60-2549-32b7-ae12-73915c21d287 | 2.6905 | -60.2211 | 2026-02-21 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 267b3438-2b7d-3f83-807a-e533832d9d03 | 2.7088 | -60.2398 | 2026-02-21 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b1161bbf-1389-3473-b825-3401e5031847 | 3.693 | -61.1521 | 2026-02-21 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f0613a5d-b738-3f7a-8db8-72ca1b134ab6 | 2.7088 | -60.2398 | 2026-02-21 13:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| fa232aeb-a485-3d81-95a5-577fa267e967 | 2.6905 | -60.2211 | 2026-02-21 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 347a1f80-dbbb-3908-99c2-5c5e8b4d1029 | 3.693 | -61.1521 | 2026-02-21 14:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 75da987a-d962-3027-bc65-05694a667a32 | 3.693 | -61.1521 | 2026-02-21 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0f28edac-0352-318e-b1e1-fb36273a2c02 | 3.693 | -61.1521 | 2026-02-21 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 114.7 |
| cf2b25ee-cfab-3fd1-bf1e-ca0e81f25b64 | 3.969 | -60.5778 | 2026-02-21 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| f0e67676-fdb1-3cb6-867b-c93a34a0ec91 | 4.0769 | -61.1633 | 2026-02-21 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ff059ab1-9ed2-3f7b-a98f-362738010ffb | 3.6937 | -60.906 | 2026-02-21 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8181c09c-8e13-3799-966f-209a2991aef1 | 4.0589 | -61.088 | 2026-02-21 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d6a3ae59-2e80-3b4a-ba66-371253aaddd3 | 4.0588 | -61.1069 | 2026-02-21 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7c4b0eff-07ee-3d12-a40f-172e297ceee9 | 3.9323 | -60.5976 | 2026-02-21 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |


