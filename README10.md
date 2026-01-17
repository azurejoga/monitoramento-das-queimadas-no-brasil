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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70763479-e106-34f1-9de5-c598b32da7a6 | 2.68075 | -59.98784 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27a6712d-288b-3194-8afa-581039034f91 | 2.75738 | -60.31716 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ef39dde-0b53-3818-bf81-6ec89b980ad4 | 2.70481 | -60.05149 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce5b1c0b-8ab8-3daf-807d-a40ad57ce1f2 | 3.98246 | -60.72417 | 2026-01-17 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b4af073-fd0f-37e6-b95a-18c2db5249c5 | 3.98301 | -60.72765 | 2026-01-17 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c80cc521-8e8a-3586-a889-a94e4eda6aec | 2.69066 | -60.16862 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00bb51ed-c53c-3228-99ec-ee9164bbe53a | 4.05195 | -61.4685 | 2026-01-17 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1876c534-ad7f-3582-9a97-06d884fdffc7 | 2.75682 | -60.31358 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1ca4dfa-bae9-346a-9f68-abcd0516e126 | 2.82575 | -60.57594 | 2026-01-17 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c565aee2-4467-33fe-bc1f-8042c65f5311 | 1.33319 | -60.71371 | 2026-01-17 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59f0519e-4671-3d77-955a-b65b180da386 | 1.33208 | -60.68467 | 2026-01-17 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d9cbb62-e960-3006-b930-56aa97a07fbe | 1.32872 | -60.68519 | 2026-01-17 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f750cdcf-bdde-3faf-97af-f9b0e4f5bb82 | 3.98133 | -60.73858 | 2026-01-17 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c92859ca-5f9e-37b1-b27b-5562dcc9cd2e | 4.05141 | -61.46507 | 2026-01-17 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f1a1f91-675a-3032-b063-52864dcc7584 | 2.74729 | -60.31874 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 678c60d6-9431-367b-83de-b73505478f3e | 2.70142 | -60.05202 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02d555b8-9a97-3322-973f-2c449d63ed8d | 2.75625 | -60.31001 | 2026-01-17 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9d7110f-79a5-3bc1-8b4d-7cc444fd6288 | -2.15125 | -54.39579 | 2026-01-17 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bc28bc1-3187-3a04-9ad7-649fc36d4b8c | -1.60475 | -53.98731 | 2026-01-17 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1e6c158-2dbe-3f59-806b-52ee17db061d | -13.69874 | -55.68275 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fef428be-51fc-3784-ae34-99d1df910775 | -13.69433 | -55.67309 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a55b6558-6bbf-38da-a0d8-6084ab24f23b | -13.69833 | -55.68646 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6256c728-8b1e-3d84-b719-8e00dd92971c | -13.69344 | -55.68059 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7e847702-1054-3e91-8454-57f981b8aabf | -13.69389 | -55.67685 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f14b80e6-b885-381e-820b-0255859f4d3a | -13.70494 | -55.67834 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0986e7ac-8fff-3e0e-b7f1-1c5fa254de8a | -13.7045 | -55.68203 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5fcc2b5-50d9-3650-86b3-add2cece08c5 | -13.69853 | -55.68501 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a43df8aa-9467-35dc-910b-422c7c740157 | -13.70469 | -55.67979 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d4ddcb8a-1d4f-3ca3-bbaa-2934a76f5fe0 | -13.70427 | -55.68349 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b04c1f7-278d-3536-b93d-be8c0506143e | -13.69957 | -55.6753 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cfedc361-a956-32c2-83d2-8e5d7f461058 | -13.7003 | -55.67013 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6979f92-bccb-360d-b30e-fa10221f6dc8 | -13.69809 | -55.68869 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d376c5b-09f4-3eff-8c47-bf94d0d4518e | -13.69897 | -55.68132 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 51c6a830-76a3-30ca-89ff-61b1cd6074ac | -13.69999 | -55.67156 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6f3a34c-7e25-356c-b210-9ed95266febf | -13.69986 | -55.67387 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ae2162b9-fffa-3484-9934-b5dfacf62dfc | -13.69941 | -55.6776 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 133e95da-1a9d-30ef-a4e5-7d0f83353f33 | -13.693 | -55.6843 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fb9bdbc8-e80e-3c83-842d-20457c767fbf | -13.69916 | -55.67905 | 2026-01-17 05:37:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5a442ff8-cf20-38f2-b9f6-6fb4c65f203d | -20.44128 | -57.87875 | 2026-01-17 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9da42ac7-aed5-3942-a2bc-9ca78a3a2c69 | -15.61288 | -57.31911 | 2026-01-17 05:40:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3648f332-0fee-30f4-9b85-394c14c027d0 | -16.11025 | -56.75451 | 2026-01-17 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9320614c-a47a-3b82-98e2-60c6756a2df4 | -20.43572 | -57.88145 | 2026-01-17 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9dcb5728-adb5-33b3-b248-e15dd16ad4ef | -19.17216 | -57.54187 | 2026-01-17 05:40:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e55e09a4-04a9-3d19-b95f-25ea037f21fa | -16.3122 | -57.56118 | 2026-01-17 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 130f719b-c618-3655-9507-4269252b4d44 | -16.31725 | -57.56186 | 2026-01-17 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bc2e2703-b71b-32c9-86ac-1c8c64422d51 | -20.4081 | -57.84059 | 2026-01-17 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 395ac19a-d4cb-33d3-a898-41dc170a5035 | -15.61252 | -57.32223 | 2026-01-17 05:40:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 037cb255-87c9-3d58-a7f6-87cc4d07b431 | -20.44094 | -57.8821 | 2026-01-17 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d2fa78aa-2fbd-3b9a-bbb7-ccd453a9c697 | -16.58477 | -57.80243 | 2026-01-17 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 09ee2a18-1fd9-37c7-a0ee-7ba85dc4194e | -20.4406 | -57.88544 | 2026-01-17 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 26cbae4d-3273-301a-9816-f545f48cf6bd | -16.58976 | -57.80307 | 2026-01-17 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 378d058b-8fe6-3d40-b63b-1f3e4fc71167 | -16.11558 | -56.75512 | 2026-01-17 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0e4b57e-3127-398c-8b2a-1bb3f57d8df9 | -20.43085 | -57.87745 | 2026-01-17 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 65d5e114-674c-3454-b33b-f0b792a1c073 | -16.5891 | -57.80888 | 2026-01-17 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 98a4a955-4956-39c7-a8cc-f5a90a06c1d3 | -6.98861 | -42.8633 | 2026-01-17 05:44:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 1de2e637-b570-3919-aba9-74f6c994e5e2 | -12.65314 | -46.76695 | 2026-01-17 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 93686198-0a22-3354-bd3b-fee4a55fa8ae | -12.08338 | -43.7683 | 2026-01-17 05:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b72eafad-3f2b-3e44-8c64-ce1f7c0981f7 | -11.793 | -45.36349 | 2026-01-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| da6de6e2-083e-3bf4-b6c9-dca2692c18be | -12.65609 | -46.74989 | 2026-01-17 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 93eeb6fd-1ee2-3dde-b6bd-2741799fc591 | -11.79528 | -45.34975 | 2026-01-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0ba290c7-f614-3be1-a9f0-450276c88fb9 | -12.0851 | -43.75751 | 2026-01-17 05:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ce0fa04d-9b28-328a-8cb0-3994cb94a083 | -14.78205 | -45.93547 | 2026-01-17 05:44:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5f370fc0-f37f-3166-9c38-2b534faeac1b | -22.73912 | -42.00512 | 2026-01-17 05:46:00 | AQUA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a00d5546-ec2e-363d-9064-df144712da8a | -11.7984 | -45.3627 | 2026-01-17 05:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 04342219-6583-3f10-8022-bdd8f36ce5fd | -13.6993 | -55.6773 | 2026-01-17 05:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| dc9be76c-c641-3e11-a897-4cd93e38e6f2 | -13.6993 | -55.6773 | 2026-01-17 06:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| aeedd8a7-9aa5-3ec1-9127-b0077465dc64 | 4.0533 | -61.46801 | 2026-01-17 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec06fcdb-7257-3587-b421-575d913f3f90 | 3.97928 | -60.73719 | 2026-01-17 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 804b3ce6-6a5e-342f-a783-bcc0f91fc526 | 3.98315 | -60.73154 | 2026-01-17 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37dbb1ce-85b8-319b-a143-49d588f38911 | 4.04888 | -61.46874 | 2026-01-17 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93218aa1-439b-3d2f-8c19-d22087444eb4 | 2.748 | -60.31747 | 2026-01-17 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e419ef1a-d3a6-3cc6-8f99-d6036b609de7 | 3.98236 | -60.72671 | 2026-01-17 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff3ef985-7188-37d6-8dc2-572bd251cb8e | 1.14226 | -60.51089 | 2026-01-17 07:20:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 860f2c43-fb3d-396c-99ec-0bb625fed60d | 1.13294 | -60.51226 | 2026-01-17 07:20:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37ad2220-e905-3359-a5fd-d8a31c0479d2 | 1.13444 | -60.52218 | 2026-01-17 07:20:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f2df636-b522-3fad-9b12-e400e949a915 | 2.75708 | -60.31208 | 2026-01-17 07:20:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc5d7292-9089-35f2-8ea3-86ceb86b6122 | -13.69982 | -55.66274 | 2026-01-17 07:24:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| eef82fce-6dd9-35e2-babd-b617cbfdf0dd | -13.68501 | -55.66899 | 2026-01-17 07:24:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 2ef88ab5-bad6-3642-aae0-99247b4861c9 | -13.7021 | -55.67101 | 2026-01-17 07:24:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| f3337bfd-b9c0-3710-8c38-d1d52f289756 | -9.65737 | -46.23202 | 2026-01-17 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 0acc0621-462c-3fd0-a728-9420065bac94 | -10.56239 | -44.32171 | 2026-01-17 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 01489cb4-fa37-3f9f-8f92-59fa915eb97c | -11.81772 | -45.36953 | 2026-01-17 12:14:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6a2a920a-8838-329f-b354-8c3b8798f3a0 | -10.19168 | -44.89999 | 2026-01-17 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d19b5844-8d1c-3849-9991-6dde721fd238 | -9.63613 | -46.24055 | 2026-01-17 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 967bf00a-7acc-3d8d-87e3-d8574a386c71 | -10.41208 | -44.88902 | 2026-01-17 12:14:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c0dbaeb3-3b2a-3b5f-8100-a1523c7c49ce | -11.8416 | -49.20033 | 2026-01-17 12:14:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e82f060-9aa8-32fc-a3b0-d9f81ff35c7a | -10.53846 | -43.62236 | 2026-01-17 12:14:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 961ae226-93f5-3be9-8be1-3a8ba8105df9 | -9.50885 | -44.42376 | 2026-01-17 12:14:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a0776289-17b0-3fde-8856-bbcbffb461fd | -9.63764 | -46.2293 | 2026-01-17 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 892c4d2c-23a3-3bc6-9dee-8890ac17121d | -10.56534 | -44.31634 | 2026-01-17 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3cae8a3c-809b-3b2a-b820-70c0f0b95928 | -12.07789 | -45.28681 | 2026-01-17 12:14:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8ec32821-1b46-3a7c-83cc-c67468c5a541 | -11.15345 | -43.30421 | 2026-01-17 12:14:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| ee98981c-fbcb-3fba-b3f9-876e737b978b | -9.6475 | -46.23071 | 2026-01-17 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3c4d094f-186c-37fc-8945-5a5ccddee32e | -9.64598 | -46.24197 | 2026-01-17 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f49c0591-4350-32b0-9973-888a1d6132eb | -10.56431 | -44.30593 | 2026-01-17 12:14:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4f49fa2e-e8c4-3171-94dd-5756231ef980 | -10.19354 | -44.88572 | 2026-01-17 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 6054d029-ff7c-3156-a8ff-f6a2b1e4105a | -10.52627 | -43.62069 | 2026-01-17 12:14:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ae622890-b12b-38e0-8506-3527f1aabab9 | -14.74898 | -45.89836 | 2026-01-17 12:16:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ba91cde6-7ca1-3f32-84a6-f2fed656a7ac | -15.67218 | -43.48897 | 2026-01-17 12:16:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 13d4af59-45c1-3700-a432-64396c122d71 | -13.46859 | -45.70605 | 2026-01-17 12:16:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README11.md)
