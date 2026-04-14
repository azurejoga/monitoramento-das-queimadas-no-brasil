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
| 55e1fa1e-4b7c-3433-ab60-cdbbb88f3033 | -11.84839 | -55.01823 | 2026-04-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5adbfb4d-ca8e-380f-9b2e-0c082dd4ae92 | -9.45243 | -47.82241 | 2026-04-14 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d22c4940-9207-3916-a388-c18672f321ab | -11.13648 | -46.77965 | 2026-04-14 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 773b162f-d8b3-33bd-aeff-d43e8e2c4259 | -19.27666 | -55.15294 | 2026-04-14 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d1fd61-9880-32a0-b573-c2079fc502c9 | -21.47321 | -56.29967 | 2026-04-14 05:10:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a01e808-3f97-36a8-ba3b-311f67251644 | -21.71463 | -57.04684 | 2026-04-14 05:10:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28485676-549f-3ced-a61a-859fb4fa6c22 | -20.14294 | -56.34306 | 2026-04-14 05:10:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4929db4-3ef8-32b2-8fa7-59e8cc25fe6b | -21.7152 | -57.04284 | 2026-04-14 05:10:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb8b84bc-03fd-3211-8468-1388882b2697 | -21.6996 | -56.30608 | 2026-04-14 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec251db8-000c-3de6-8090-977ab33e3002 | 1.73663 | -60.35359 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b39653e-74fd-374f-a3ba-0c0eb58e3433 | 2.00921 | -60.66365 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51dc76f3-00df-3953-bc0b-fab8d1633007 | 2.94077 | -60.17491 | 2026-04-14 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 954c04b1-230b-3ba7-9bba-d2662bea6734 | 4.18624 | -60.79614 | 2026-04-14 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7864415-173f-34c2-a61f-cd6c35d0b53e | 4.22469 | -60.77933 | 2026-04-14 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05f8438c-ff3a-3a8f-ad8d-f583475121a9 | 1.92461 | -60.49341 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5886b95e-186f-3a1e-a9b5-b5352239eeed | 1.73222 | -60.34723 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43be1f29-a4d0-39b7-82d3-c2c633324c31 | 4.2528 | -60.77135 | 2026-04-14 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be63e803-904a-3b05-8cfb-1678fcf6d8b2 | 2.00866 | -60.6602 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecf4f4c9-2d52-3a3a-9c17-7d1f2890c0da | 1.88834 | -60.67194 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11094a3e-f4a0-36c2-a6bd-1b237128d247 | 1.73608 | -60.35014 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf21d562-53d8-3cfd-97e5-b1b225252262 | 1.73386 | -60.35754 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ca3c062-4f04-368c-91ce-8840e390714c | 1.92129 | -60.49393 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6449b0dd-2375-34ea-9e37-65df1636684b | 2.18182 | -60.83495 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01880b2d-3d42-38ee-9599-ff3b7fb8dbc3 | 1.48385 | -60.91949 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73b828ba-7353-3393-9bb8-a054e51a8253 | 2.94132 | -60.17834 | 2026-04-14 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcdf5dae-4354-3f38-b242-f2891a964f60 | 4.25613 | -60.77069 | 2026-04-14 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79a2e3d4-8e79-3c40-8280-a8387953e14e | 1.93123 | -60.49236 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebc7c73d-9f05-3385-9334-cdb929d0765f | 1.91798 | -60.49445 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88e6f639-c4b7-3de2-9186-13437d06f703 | 1.73717 | -60.35702 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f9a5e2a-db47-3bed-8b2b-507d7d13744b | 2.938 | -60.17886 | 2026-04-14 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe897e00-b183-3095-ab29-1d4d5c543b58 | 1.83891 | -60.82804 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 846d7693-c23c-3a78-a5fb-4f25005b93b1 | 1.92738 | -60.48946 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cda882ec-8498-3170-8e2f-8d459a479e9d | 1.73994 | -60.35307 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 902592f7-e66a-3585-8eac-b442d6c1ebc1 | 1.74048 | -60.35651 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cff75d2-6cfe-3de8-a6a0-3be97f2bc92e | 1.73331 | -60.35411 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46a84b9e-2649-3964-b44d-9ca5c2bca032 | 1.92792 | -60.4929 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6504dfbf-0e67-3a67-ab97-16cec6c2b8fe | 1.93069 | -60.48893 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91306984-4fa6-3056-b286-4e25a6340010 | 1.91395 | -60.57618 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9648e4f5-9387-3c23-9900-ca8f0d9147a0 | 1.84278 | -60.83097 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68f65a68-189b-359d-82c3-86af6a71b1ea | 1.3485 | -60.66142 | 2026-04-14 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a90a4053-c812-3a7a-be1e-d86f3e9e4408 | 1.92075 | -60.4905 | 2026-04-14 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad44bbc4-40f9-3d2e-a1e0-6bc44c68a77f | -21.4699 | -56.29724 | 2026-04-14 05:42:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b55e2eac-ef44-387b-a846-2b731252b9a2 | -21.47519 | -56.29788 | 2026-04-14 05:42:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 148ba36c-e4eb-3046-9283-c337e125306f | 2.1994 | -60.80927 | 2026-04-14 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7fe56f7-2e35-3598-a0eb-4ccacdc8b2f7 | 1.73257 | -60.35915 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 589409c0-9a80-3ad3-ae5e-4dd35e158ee9 | 1.73557 | -60.34982 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6af46ba-ef8e-3437-a2cd-78b110425ac2 | 1.73626 | -60.35406 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ea129c4-27ca-3c54-9c28-ee2863d26b20 | 2.00697 | -60.66325 | 2026-04-14 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5170ff5d-ef3d-39d8-b48d-487a82999dc3 | 1.84274 | -60.82597 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0bc1f5a-52b7-3eb4-a8b2-4c2d0fb52bf4 | 1.83912 | -60.8306 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45e3fd50-c575-30a7-9bfc-df081780bc3f | 1.73694 | -60.35833 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1693dd23-c0f1-3d40-a379-f5827b4e5457 | 1.91554 | -60.57598 | 2026-04-14 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a83bb690-2aba-3ccf-bce6-a7063af36a02 | 4.25381 | -60.76971 | 2026-04-14 05:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68df1af8-9e66-3f61-80b4-5808f670d57f | 1.844 | -60.83388 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e29de8cb-eb66-3b19-8414-9bea303522f9 | 4.25445 | -60.77349 | 2026-04-14 05:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8da84ab-a934-381a-a6e2-746544f7c4a9 | 1.74064 | -60.35331 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6194062-e979-35cc-b6e8-18e8550e5296 | 2.01344 | -61.08541 | 2026-04-14 05:53:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c0f08fb-c3e4-37d8-a739-fb4ab5691f98 | 1.85752 | -60.73487 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d79c69f-959c-3a4d-b5a3-2e608c06f7f6 | 2.01125 | -60.66256 | 2026-04-14 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b5680b8-61bc-3183-a694-8bdebb530355 | 1.84337 | -60.82993 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 475bf9b4-3417-3872-b327-4008c70d3f3a | 1.88623 | -60.85653 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7846cc9-71d3-31ee-813c-920a3a270c0f | 2.00877 | -60.59217 | 2026-04-14 05:53:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cbb38c1-5829-3398-889a-0d802e1aa5a0 | 1.85686 | -60.73081 | 2026-04-14 05:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19378a3c-d827-3d68-98a8-be46183519e5 | 2.0153 | -61.08621 | 2026-04-14 05:53:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e6bcd50-361e-3dbf-a1b8-d1a03d651655 | -16.5954 | -58.21498 | 2026-04-14 07:09:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 8faa36c6-5f09-3dd8-b4e4-e2ef0bcc6017 | -10.99805 | -44.85563 | 2026-04-14 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc493984-0835-3a72-91f3-03af29a285bf | -11.14429 | -46.77183 | 2026-04-14 11:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1232689e-9508-355d-9d5e-65a844d5b899 | -11.1426 | -46.78286 | 2026-04-14 11:45:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| abc49583-7df9-3247-be22-ad09a26ba7ea | -19.49494 | -40.16939 | 2026-04-14 11:47:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 1fa79b6f-b707-3ffc-8eb5-9139663ef84e | -20.14774 | -46.74977 | 2026-04-14 11:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 30bc9e4a-e4da-3866-8309-9b12281cac35 | -20.15665 | -46.75129 | 2026-04-14 11:47:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17b73cb6-21ad-38c4-89fd-9b17ea162977 | -19.60968 | -40.06645 | 2026-04-14 11:47:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 0785c1cb-4f0d-327a-8c02-e7744055e729 | -17.14459 | -45.08018 | 2026-04-14 11:47:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| abb3e467-af10-37fc-8435-6bc412c28f37 | -17.14328 | -45.08936 | 2026-04-14 11:47:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 11d5a6c6-c882-324b-89ba-1810215fcad1 | -25.40295 | -50.51623 | 2026-04-14 11:49:00 | TERRA_M-M | TEIXEIRA SOARES | PARANÁ | Brasil | 4127007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 03e54c25-7209-37bb-b173-7241ca195d4d | -11.1447 | -46.7699 | 2026-04-14 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d831f8c6-d42c-3fe8-ae8c-9ef58ae240a2 | -11.1447 | -46.7699 | 2026-04-14 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 53af210d-0149-3439-af2f-fc22463058dd | -11.1447 | -46.7699 | 2026-04-14 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| cde2e4fd-5648-36ed-a5cc-bfa0a131cd4a | -11.1447 | -46.7699 | 2026-04-14 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7f277c59-101b-3591-b4f6-0d4e9d300375 | -11.1443 | -46.7923 | 2026-04-14 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| dadd940c-ea3a-3220-8c01-2928ed0418cf | -11.1447 | -46.7699 | 2026-04-14 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 2c7e3e2b-6e40-3da9-9b45-06c4259cc52c | -11.1447 | -46.7699 | 2026-04-14 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 258c0e94-9758-362b-8a01-47e0bcbd9d6a | -11.1443 | -46.7923 | 2026-04-14 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e98b6119-b3cf-3aa2-bccb-454bc074abae | -11.1476 | -46.5896 | 2026-04-14 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 61896c27-63c6-36ca-980b-7241ce49f403 | -11.1443 | -46.7923 | 2026-04-14 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 4a485168-69a8-37b4-92c8-64e61ff25ad2 | -11.1447 | -46.7699 | 2026-04-14 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| f2b8607c-fa8b-33d3-9291-efdb00d899ef | -11.1476 | -46.5896 | 2026-04-14 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 7d1a4fd5-12b2-3308-a1a7-ce239ade6f89 | -11.1447 | -46.7699 | 2026-04-14 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 99cbead8-e108-3e0d-b182-1f4ae9d9f566 | -11.1443 | -46.7923 | 2026-04-14 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 57588761-e48e-3520-b8ad-9ffb466aea1b | -11.1476 | -46.5896 | 2026-04-14 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 98d6665c-1fa9-380c-be60-4fdd623929e8 | -11.1447 | -46.7699 | 2026-04-14 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 0f5551d9-9eaf-30b0-8a54-50bcee946eef | -11.1476 | -46.5896 | 2026-04-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |


