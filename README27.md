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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f948e14f-2078-3744-b24f-4715ff86bb39 | -16.57965 | -57.25002 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 665f88a2-a697-3653-a493-053e53962be8 | -16.57398 | -57.25732 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 9eadb253-9e43-3bc3-8517-4bd772961054 | -16.56574 | -57.25159 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| d2264a02-7658-3c4f-a5e3-7d8e62f00e19 | -16.56008 | -57.25887 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| 7aff7879-a408-3536-bdd0-426e0a925867 | -16.55743 | -57.23447 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 09072f11-d2c1-39a0-b39e-f270035babbc | -16.45975 | -57.30005 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 1907c923-57a7-3ff3-bf8c-5d0262e39bf1 | -16.42825 | -57.4038 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a6aff969-223e-3631-8f6a-3b3f6c551a87 | -16.41421 | -57.40531 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| bab80c8b-54de-39ec-b41b-a6d610deb59f | -16.41165 | -57.38041 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| f5b612fc-ef68-31af-9621-6d8701c6c82b | -16.40931 | -57.41243 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| d310239d-636f-38fb-889b-28a08d3ea825 | -16.40659 | -57.38759 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 13528cc7-a28a-336f-9e08-4b09372ea8af | -15.88502 | -57.15578 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| cad5fa6c-2acd-3722-978e-07a8fccb9e7c | -15.88269 | -57.13424 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 70b67706-f576-311e-a742-cb1452f8db27 | -17.14982 | -57.41079 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 9557a22b-576e-398d-a25c-8ec2608ace6a | -17.13955 | -57.40528 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 9db4122b-08c2-3a7f-a2c1-2bfed38dac67 | -17.12687 | -56.74602 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| eb311f63-6618-3524-9d13-43e701602f0b | -17.11829 | -56.79333 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 423feb86-509e-30d7-85fb-e28127af5980 | -17.10477 | -56.79484 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 93a9a8a1-0736-38ae-a147-4aa2b1f82581 | -17.09126 | -56.79638 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.2 |
| 9ceec88d-b614-329e-b534-ada825f827b2 | -17.06972 | -56.80545 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| b78b0235-ce81-37ba-bed9-a1b0d889f6ba | -17.06424 | -56.79951 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.7 |
| eec8f400-7ce9-35c9-84bc-633cf1f2e209 | -17.0562 | -56.80695 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| bb307061-8e35-319a-ad7c-82491a169fc1 | -17.04148 | -56.70981 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| b9065635-3fb4-3683-8aa0-e99e18735422 | -17.04021 | -56.78555 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 76bfa3b2-f3fd-3556-825c-ebae884948b3 | -17.02672 | -56.78711 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.2 |
| 525ede0f-244c-3680-b0ff-9f0f7c2576b9 | -17.02428 | -56.76426 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| ac7ae09a-d09b-365f-bf57-9807b8938bc5 | -17.01323 | -56.78864 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 384.0 |
| 11c9cd1d-25fe-36e4-bfe6-c60ccec194e9 | -17.01082 | -56.7658 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 181.7 |
| 111306af-5d20-35a2-880d-d35a7d4c2ee6 | -17.00841 | -56.74305 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 2a06b07d-2b5d-38a7-8bf7-1808f5757bd5 | -16.99974 | -56.79018 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 33caf934-803b-350f-bfa5-d2ffe14e5f59 | -16.99735 | -56.76734 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 164.0 |
| 8ef192d6-834c-3be6-bcb1-11ad37f54f28 | -16.99497 | -56.74461 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| e639b3d0-ff9b-3e17-9694-87af8dde177c | -16.98897 | -56.77378 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 75a2cec4-09d5-32cf-98f9-2d81f9205def | -16.98643 | -56.75108 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 8135bd32-9e15-3f9c-8cb4-7f204f797a31 | -16.98389 | -56.76889 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 7d73f54a-6014-37f3-85d6-10e2b98021c3 | -16.78966 | -57.39057 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.2 |
| e4ab0076-d1a4-3d45-8ec3-4a85abe77080 | -16.78708 | -57.36536 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| b96c6a66-017c-396e-bccd-bfca68570a54 | -16.78523 | -57.39763 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 7fa63a2f-fcbb-3735-8bbb-7edab53de5db | -16.78247 | -57.37244 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 56f08183-83ff-34c8-8d2b-e0ac56c8afa5 | -16.75237 | -57.77086 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 8a59d981-8564-3744-a199-5d9863564db3 | -16.74961 | -57.74392 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 6ee1d5d0-6227-31c2-9080-98f566aba9a3 | -16.6875 | -57.46527 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| debc4e59-903c-39a3-9c0f-857440c1ba9c | -16.65713 | -57.31606 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| b602d940-13b7-3dc3-8e3a-4dd6a67bf261 | -14.79566 | -48.02741 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f0edc06f-a0c2-3796-84c5-9bf4853664d5 | -14.78935 | -48.04881 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3a2647a3-42e2-3459-8970-6bf244c5f829 | -13.8265 | -42.16116 | 2024-10-04 01:09:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| aa51bb5c-e53b-3ae9-98af-ed237a05c47e | -7.74858 | -43.06531 | 2024-10-04 01:09:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| b2b135e0-71b3-32ac-b4e3-cfdca0f887bb | -7.69168 | -42.99051 | 2024-10-04 01:09:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| ad854438-0b66-30e2-a5d1-8c31a361044e | -7.68884 | -42.98564 | 2024-10-04 01:09:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 96a07722-2af6-37e4-9ca8-7c68d3bdb202 | -9.15587 | -43.16327 | 2024-10-04 01:09:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 22f45fe1-7dc1-360f-8f26-0ef8e07b9b6a | -13.47616 | -43.78344 | 2024-10-04 01:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 72f026be-cd4f-37b4-aab1-8ca2830ee41a | -14.90892 | -45.12636 | 2024-10-04 01:09:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f0461a77-5bbf-31bf-81df-0159340fa255 | -14.16345 | -44.66145 | 2024-10-04 01:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9210a779-ce38-3e9c-af4e-c6f5f0587ea0 | -14.16069 | -44.64481 | 2024-10-04 01:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 24fa6a71-98a6-395b-8fb1-4da20a1426c1 | -13.9926 | -44.03965 | 2024-10-04 01:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| fd7a67c4-fb0e-39a7-a389-8005c6c0fad2 | -13.98946 | -44.0208 | 2024-10-04 01:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 71b0c239-60b8-34c2-a98e-067eb6cdc73f | -6.25633 | -44.14119 | 2024-10-04 01:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6e68aa39-c76a-3088-ba50-80df8aab5f65 | -6.25318 | -44.14748 | 2024-10-04 01:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c90e0089-ba3b-3250-a186-5ee634a8857d | -6.24206 | -44.14323 | 2024-10-04 01:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 9b6357fd-a554-3fc5-8401-bd9fbeeab1b6 | -6.14629 | -44.14397 | 2024-10-04 01:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| ef34119c-6fb8-390e-a235-1676ee4337ad | -6.13508 | -44.13939 | 2024-10-04 01:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a0f4c587-964f-323d-a7b4-4c7c6a9d6bc1 | -14.78635 | -48.02867 | 2024-10-04 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| cc3244cf-27f6-3856-9acc-8bacf4d56d08 | -7.84931 | -45.33545 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bdd77dd9-cbd7-3b19-9b91-93036b44ad65 | -7.85516 | -45.37306 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 20dea855-5a30-3fd2-97a0-84a5efd56fdb | -7.85227 | -45.35448 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 67afbf7c-40eb-387f-b08b-e2acce3d7ca0 | -10.79159 | -45.59986 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f2ba65f4-9069-314e-befc-3729bcc274ea | -10.75675 | -45.60601 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a78cae22-12cd-3187-b238-1b4b10dd5c8a | -10.74842 | -44.63528 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 98f0eae9-3480-3f5d-8cc0-a9a39d52815a | -10.6258 | -45.20005 | 2024-10-04 01:09:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9729eab6-1284-37c1-ac93-7d6dc982b284 | -10.80162 | -45.60854 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 016f7d20-20cb-3039-bfdc-76d4d5e28784 | -10.79885 | -45.59132 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 79170f01-2a50-322e-9874-4695b296aed4 | -10.79415 | -45.61649 | 2024-10-04 01:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c6388e76-603a-3e1b-9501-a2efc75eff10 | -13.17154 | -45.43524 | 2024-10-04 01:09:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2c287481-5913-3883-9079-009987c1a90c | -13.13668 | -46.29934 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cd14f437-ec3b-34a5-ae11-8ebfddb2cdd8 | -13.12815 | -46.31391 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 925b7ec1-4acb-3978-97ad-5bdb4aa23b2d | -13.12616 | -46.30138 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5fe13397-adec-3c02-b553-0eb0421735e3 | -12.26407 | -45.96119 | 2024-10-04 01:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 71b84267-f0e3-3e9a-a9bc-af1fbf76b3cd | -14.20003 | -46.47348 | 2024-10-04 01:09:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3c73816f-f7c4-31e0-a426-f3f82a0110ae | -14.18975 | -46.47501 | 2024-10-04 01:09:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 70439217-ff7f-3f02-bbbd-86053dcc8229 | -16.9392 | -47.13881 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0b876b94-ad2f-3596-9ad3-1468e263008e | -16.93755 | -47.12811 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 310e0c7b-372e-39a0-ba40-9b2477c22edc | -16.93591 | -47.11748 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4c4734ca-acb1-3e3f-bb3e-024bb66b3ee1 | -16.92976 | -47.14052 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| df2dfc68-edf7-329f-9182-511c3a469593 | -16.92811 | -47.12985 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 181.8 |
| cc613077-9b54-3126-87ce-bbfe985b17e7 | -16.92645 | -47.11909 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fcd3ece5-2a84-315f-b994-edb4e36c5dd4 | -16.92423 | -47.13688 | 2024-10-04 01:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d30d06f2-9a25-3c4d-a4a7-10eac901f6e2 | -7.61846 | -45.54421 | 2024-10-04 01:09:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 97a6c5b5-d3be-3477-9f62-41845cf12aed | -7.22295 | -45.61188 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ff25e234-51b1-36af-8499-d0a0d5c2f58c | -7.22006 | -45.59344 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e947e14a-ba7b-3f4a-81ed-76cbfab8ac66 | -7.70002 | -46.15643 | 2024-10-04 01:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| dc14f336-22c0-3ccf-99e6-f739050d9ee2 | -8.75705 | -46.81303 | 2024-10-04 01:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 75710c43-4a7e-377f-99ba-740680435294 | -8.75573 | -46.81972 | 2024-10-04 01:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2d6a6c3b-895b-301b-b197-eaa0dd7b98a3 | -8.75358 | -46.80535 | 2024-10-04 01:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f16d8543-bc1b-3109-b655-6a1d60cf06de | -8.59618 | -46.52276 | 2024-10-04 01:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 468f23a4-1499-353f-9ecc-db509d2004b3 | -9.84464 | -46.78615 | 2024-10-04 01:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a6c9e4a1-193a-3630-aa7f-271a0b8500a7 | -9.84261 | -46.77267 | 2024-10-04 01:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ad4a2955-3eb8-366c-aa29-cdd2d9ca9cd0 | -9.84054 | -46.75901 | 2024-10-04 01:09:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9c3efd2d-4df5-316a-856e-5922e277071c | -11.71281 | -47.69977 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6594fa03-d28d-38ac-a7fe-abd3168b9e84 | -11.70305 | -47.70175 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 160e1f83-29c5-3a6c-882b-d98f4b11812c | -11.70133 | -47.69035 | 2024-10-04 01:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README28.md)
