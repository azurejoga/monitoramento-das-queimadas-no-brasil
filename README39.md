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
| 5e34b206-6f38-39a6-b1e0-2013b50318c5 | -17.71396 | -57.5136 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8be41dd4-a096-3b34-bc75-db294198e4ae | -20.76384 | -46.76928 | 2024-11-11 04:23:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f28155d-e6d2-3f34-b728-6ea070fca281 | -19.49841 | -44.27545 | 2024-11-11 04:23:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37ed1fbb-446b-348c-97b0-3c2d7d06ef70 | -17.28474 | -57.31171 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f6e7829d-f556-3f1f-a9a4-f86a07a80dd5 | -17.62524 | -57.52983 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 23a54e71-08c4-31d9-bdda-057010086790 | -17.59891 | -57.54396 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 8de028d2-f9bb-3b5c-82b0-29240506583e | -17.28439 | -57.30695 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 22520dbb-2169-35f6-9a01-99744014ebbd | -24.63227 | -52.88282 | 2024-11-11 04:23:00 | NPP-375D | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d46b7b4f-884d-368c-a131-196cb2bce63f | -17.63324 | -57.51953 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3e1cd564-c3e8-392b-b041-924e50c3d035 | -17.63206 | -57.44257 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 203f39d0-c886-303a-a181-24b61faac4c5 | -17.67826 | -57.51731 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9f85e3a3-9b38-3b39-9f56-5459203edd07 | -17.24719 | -57.49324 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 174acf8d-d618-3e5b-98e7-1d1d4da53e96 | -23.92813 | -54.04367 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 46091fdc-c07a-3ab3-8ede-212e7324b83c | -17.24171 | -57.47871 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a0607f3c-34a5-368d-a36f-0d8414a6194c | -17.28073 | -57.48782 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 835e1810-724b-3f30-99da-41af3350e12e | -17.62997 | -57.53503 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 43779ae4-f58f-3180-b98a-a9c5e4cd7905 | -17.59358 | -57.51423 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e85d4996-8a86-3a45-b1fe-b4a68ebfb481 | -17.62442 | -57.53371 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 35b9b11d-f126-3dfb-8c7b-044f07dea8c1 | -17.29105 | -57.49433 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 34d956fd-a104-36da-8c41-281402a0d40b | -17.2408 | -57.49583 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e5204ade-64f0-3746-827e-2aa81512cd1d | -17.23522 | -57.49453 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4230f1ae-1821-33b9-b890-c153b72668ae | -23.46736 | -51.86354 | 2024-11-11 04:23:00 | NPP-375D | SARANDI | PARANÁ | Brasil | 4126256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2682e09e-ccb0-3e3d-8dae-46457ae11d7a | -17.59276 | -57.5181 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 124b6169-ce21-3ed7-a80d-359a60e5ede1 | -17.29188 | -57.49043 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 01e839cb-904f-35bf-8c66-a6f0d8d28719 | -23.92147 | -54.03823 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ec668136-4ab8-359b-abe3-6dd3ccc83092 | -17.6055 | -57.51298 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 105a562f-fbd5-3423-814f-7b8ab1e83b6e | -17.60632 | -57.50912 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8dea7a4b-5ea2-39b6-b2ef-a5d31688190b | -17.25119 | -57.48912 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b369ad7-f1ab-3d93-8981-15d6ab3f83b1 | -17.62735 | -57.43743 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8e921eba-d91c-3297-8b09-17103c88ff37 | -17.23603 | -57.4906 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 99583bfb-6f15-3181-917c-c39afa7eac56 | -17.29993 | -57.48002 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 93ae24f6-3e71-3c6b-8651-daf817fa9873 | -17.61712 | -57.43104 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 80ac0100-5bc7-37d5-8a1d-6dc0a30ac009 | -17.63634 | -57.53247 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| c6bb44a6-c95f-34ab-9e74-7304f292794e | -17.60529 | -57.5414 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| de2c2c1b-fcfc-3999-8631-7b8eec8e5e4c | -17.24645 | -57.48391 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 79eb4122-fd01-33fc-a27b-1034f2fd43c7 | -17.60835 | -57.44503 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a6f45a34-5ae0-3f8b-83eb-218500dbf4ea | -17.59423 | -57.42967 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1cd9506d-fab9-3012-b739-24c69d6334eb | -17.3086 | -57.49435 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 18e7ae85-b4aa-3be0-bd25-64e1350a8bad | -17.68793 | -57.49939 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 09d3b9f4-175d-315c-aa1b-b609ab62e617 | -17.2991 | -57.48392 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 41903e79-1634-31c4-9344-cc28de6f6288 | -17.29745 | -57.49173 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 571fa9b6-7be8-3549-8c51-6c9e7130437d | -17.68296 | -57.52249 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1ea996c9-ca8e-3101-80f6-3546d92ff563 | -17.2799 | -57.49172 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3855fa40-8bf0-30e9-a430-f6756f7948af | -17.61469 | -57.4425 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bc26805a-0038-3c14-aab6-6dd230483793 | -17.24729 | -57.48001 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5d49e6b0-1e23-3187-a9e7-91cac7e6bcb4 | -13.73278 | -48.96644 | 2024-11-11 04:23:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ada7cfc3-db87-3788-80b2-701113176a71 | -17.29103 | -57.3092 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c4f52027-a599-3e1f-9d2e-d47860f697dd | -17.60364 | -57.4399 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eeb2517f-25b2-30b1-969a-757e1203bdbd | -17.59341 | -57.43349 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0219927a-c469-3869-85b7-0fbc6a16207f | -17.595 | -57.5349 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 30596719-b43d-3f5c-b39e-42c228df1333 | -17.2899 | -57.30823 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e2a270eb-44bd-320f-9f70-e4221312bd90 | -17.59831 | -57.51941 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 3da37a57-d493-3eb5-8c66-6cb9eebb4737 | -17.5926 | -57.4373 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| db7906dd-3d84-37d7-8b5d-2d578fec4f55 | -17.25357 | -57.49065 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e9a2f3c9-ae89-3517-8b91-6675ac3a4287 | -23.92017 | -54.04183 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 57b71838-a4c2-32fb-a55a-2e42b5095630 | -17.23919 | -57.49043 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1b733579-da74-3859-9f75-0112fe9d3abf | -17.24962 | -57.48151 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f6b32924-4df6-397c-a7ae-87b3508c1b59 | -17.63242 | -57.5234 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 53ee15f9-f9d2-30bb-bbae-d7399421daca | -17.6022 | -57.41952 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 43e62eb1-bfc5-3921-b85b-099fce1a2eee | -23.93231 | -54.04657 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ba03b64b-b4e7-3a1b-b097-145382767830 | -17.24561 | -57.48782 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dfa99039-fd0d-36b5-9f32-c4d36e755413 | -17.59913 | -57.51554 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e29f7727-1229-392f-af5f-f28e50b52563 | -17.35828 | -57.43913 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 80b923ac-da2a-33b0-a0e6-f56e7b65f709 | -17.58789 | -57.43219 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 793e5b30-f8e6-3897-88f9-ca57ff78d27d | -17.59193 | -57.52198 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| a83a053d-aa2f-38ed-a2cc-def764160092 | -23.5199 | -46.97392 | 2024-11-11 04:25:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1655154c-6a43-3d26-ac25-c9b57dadebf7 | -20.95194 | -51.25959 | 2024-11-11 04:25:00 | NPP-375D | MURUTINGA DO SUL | SÃO PAULO | Brasil | 3532108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 818a3409-3936-36b1-967b-c0de74bf9040 | -21.55972 | -54.19502 | 2024-11-11 04:25:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6f399e2-72d6-3b99-84b6-05ee2c46e383 | -23.40351 | -46.55575 | 2024-11-11 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d55e087-9737-3278-bf7e-beb17da9605c | -23.02564 | -46.49119 | 2024-11-11 04:25:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26701f9b-56f0-3f2d-89fd-5f2c9aec39c4 | -23.70604 | -46.47755 | 2024-11-11 04:25:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e136d2ed-00ee-37f0-bc04-861d46b4d05f | -20.9513 | -51.26169 | 2024-11-11 04:25:00 | NPP-375D | MURUTINGA DO SUL | SÃO PAULO | Brasil | 3532108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| edf349d8-0191-3c4e-bdbe-442821de289c | -20.99508 | -51.79186 | 2024-11-11 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0814a765-4f76-3234-921b-e620221faa7d | -22.5394 | -48.81385 | 2024-11-11 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d733f638-04c5-32c8-a4df-af28c2728b16 | -29.5798 | -53.30602 | 2024-11-11 04:25:00 | NPP-375D | AGUDO | RIO GRANDE DO SUL | Brasil | 4300109 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56b818f2-843f-3d74-bbab-baef8926f4b6 | -23.59371 | -47.43782 | 2024-11-11 04:25:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90e11d27-6653-3604-be47-5fe899104300 | -23.40696 | -46.55629 | 2024-11-11 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 939fa3ca-921b-3f1b-93f3-5b205a63ae02 | -28.63346 | -51.30356 | 2024-11-11 04:25:00 | NPP-375D | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be05265b-3929-3f6c-a0b7-77f3ce0470e0 | -28.58615 | -49.44238 | 2024-11-11 04:25:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 168b287e-206d-3954-8251-6d5d7f1e0522 | -23.33983 | -45.45452 | 2024-11-11 04:25:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16e380f6-d2e8-3aee-ac52-6c5ba9b7c018 | -2.2259 | -48.4021 | 2024-11-11 04:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 49775413-b2ac-35d7-9ed0-cd519df8af7d | -2.248 | -53.7224 | 2024-11-11 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f6fc99df-335f-372c-8acf-4451ed34854a | -2.189 | -48.3815 | 2024-11-11 04:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ef47746b-8b0d-372e-8545-593b900526fb | -3.128 | -45.2285 | 2024-11-11 04:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2ecdd682-8a64-3cb0-b79c-ec4251fee2af | -2.248 | -53.7426 | 2024-11-11 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| dcc5a305-97b0-3c52-b111-d0e750507f65 | -2.2445 | -48.3802 | 2024-11-11 04:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ffc431a1-8a7b-3730-8f14-8794a5683d0f | -2.2298 | -53.6623 | 2024-11-11 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| b942ca8e-49cc-3f3b-8b2f-87137b353284 | -2.2075 | -48.3811 | 2024-11-11 04:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5df4050b-270e-3be3-af9e-5fe3f089a8bf | -2.2663 | -53.7422 | 2024-11-11 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 293e5acb-97de-340a-95e5-79798a5d74f5 | -17.2933 | -57.4857 | 2024-11-11 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 222a2537-c1c6-3342-8b26-cb00b266f1a5 | -3.0295 | -50.9815 | 2024-11-11 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c7db6a18-16c8-36aa-b9e7-bb2d8434a4f3 | -2.2297 | -53.6824 | 2024-11-11 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4bdf3ce1-7ab3-3d99-b361-0a2f55a0c172 | -3.1458 | -54.4859 | 2024-11-11 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f753eff4-c838-3acc-8e17-08d6e417f54e | -17.2936 | -57.4652 | 2024-11-11 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 98923195-7e39-37bb-8a79-9341981fee5a | -23.9312 | -54.034 | 2024-11-11 04:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 5676a2c5-c9d5-3503-8a2a-21a6fd6ecacb | -17.313 | -57.4834 | 2024-11-11 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| f2780002-bcd9-3333-93b1-68d4643f2d57 | -2.226 | -48.3806 | 2024-11-11 04:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| b6e958c9-028a-3150-a3ac-400cb9822b4b | -3.1458 | -54.4859 | 2024-11-11 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c2103ef6-2217-3b9d-a725-46abd48a0856 | -17.2933 | -57.4857 | 2024-11-11 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 3d81d2cd-75d3-3207-9d6e-b51a1bf73758 | -2.226 | -48.3806 | 2024-11-11 04:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |


[Clique aqui para ver as próximas entradas](README40.md)
