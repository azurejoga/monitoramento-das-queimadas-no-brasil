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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 767ef6de-c05f-3f07-b2dc-25c7b991dc5c | -18.25022 | -56.60219 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| dae90009-691c-31c0-9c09-f981faadca56 | -18.2496 | -56.60788 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 3461e218-9333-399b-902b-cff78fe50e9a | -18.24897 | -56.61358 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 235f2bdd-1f2f-3b28-943f-97650c9c7418 | -18.24888 | -56.6018 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b7bc1c53-5366-3e92-96ce-885776397ae8 | -18.24821 | -56.60748 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 73c94ea7-c166-30ae-8739-5b9f22302aaa | -18.24754 | -56.61318 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| bc5efd75-0f0b-3a70-b016-b7f840969bc7 | -18.24531 | -56.60155 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c3a8d446-5400-3b14-afe4-ae32a1c8a1fd | -18.24405 | -56.61295 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 91e462f4-7786-3912-9911-155aa95dc5bc | -18.24397 | -56.60117 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 488a70b4-e10d-3ead-956a-86dc562a3344 | -18.23943 | -56.33532 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 910ecf89-cc09-3330-8baa-4ca72114bcbf | -18.23443 | -56.33469 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b25f3116-faf9-33bd-8780-e95ceebbaf5c | -18.20413 | -56.3788 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 43a097ae-749a-3c9f-a705-6bab914c7756 | -19.55592 | -56.95155 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7291452a-6633-3f01-858d-d312f35746d7 | -19.55103 | -56.95094 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6e60cbb3-36a7-3438-b3ca-6cc0f954a183 | -15.65321 | -57.67067 | 2024-10-17 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42d4b1ea-ba24-39ab-87e0-b8a9eb61553e | -16.06838 | -56.98788 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec318a09-d203-3afd-9bbe-4839ff984f6c | -16.06633 | -56.98518 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 039b4e78-dd79-3069-a1f1-0e1a1600e775 | -16.06571 | -56.99007 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c51111b6-b604-3405-9112-68dd6e0bed13 | -17.97737 | -57.424 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 0e125f96-cf6c-3480-802d-4faec4421d8c | -17.94346 | -57.44722 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1315afa6-753f-3b8d-a79a-8c65c777ee1c | -17.94203 | -57.44457 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d397f8a4-ee6a-3a62-94c9-beb30c993346 | -17.94146 | -57.44954 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 578bb907-2dd3-3630-8bdb-e4ac444d84a9 | -17.93883 | -57.44663 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ea4a6c1c-2c23-34f2-afd1-d72728cf8a18 | -17.93822 | -57.45159 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 98e1b68e-afc2-3bf3-a3d2-822a125b9df6 | -17.9374 | -57.44396 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ddb6d64-4fbc-324d-b442-101d7683d466 | -17.93683 | -57.44893 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1ecf12b6-ddd6-36bb-9d74-40b4c958cdbf | -17.93019 | -57.44046 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7d910270-f053-3f8a-8553-61c00f79ecf0 | -17.92677 | -57.42992 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8bf0c89b-17a2-3ef9-a24e-8c707e3c7895 | -17.92616 | -57.43488 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6186d0e6-1407-3e2e-bd39-4c12431e1e25 | -17.92556 | -57.43985 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f32fcb42-15f3-3371-8c8f-d467f066ea19 | -17.92093 | -57.43925 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bef9afdf-89ba-3740-a515-d673539b852e | -17.9157 | -57.44358 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fe86ca41-e321-3c82-9c30-b7ea2d7ea180 | -17.9151 | -57.44853 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 689ecc57-4881-3d98-885c-a4e9c3981d11 | -17.91047 | -57.44792 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 716b7ee3-7b7e-3ff9-92cc-efc1235873d5 | -17.90987 | -57.45286 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9a0140e7-4832-3312-b723-fede836d134d | -17.90525 | -57.45224 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 1dac28df-ffb9-358e-8f28-28ad4779f72e | -17.90123 | -57.44669 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6fd5b97c-06a6-34bc-ae43-b914719cc66b | -17.87378 | -57.23889 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 08cea50d-745b-3f90-91d6-aa3392374349 | -17.87318 | -57.24401 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d5388d1d-20b6-36d2-b007-c3ac60212478 | -17.87259 | -57.2491 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 53b73e3d-ad00-3bd0-9b3f-b494b9c0b93c | -17.87057 | -57.24722 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c688e1a2-790f-30fd-85e1-03cd235e3a4c | -17.86791 | -57.24848 | 2024-10-17 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| dc4ca11f-2fca-3f36-9ea7-cc09c577e920 | -17.90063 | -57.45163 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 1eb57a98-c11f-38ad-b97f-d65604f19b2c | -17.89601 | -57.45101 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d04fb6ad-6752-3de2-b5bd-5d4dc6400739 | -17.89541 | -57.45594 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7ad85792-2d74-3f62-8082-606ae483434e | -17.89139 | -57.45039 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ab32e754-9c4f-37b0-a8ee-28fe225862c2 | -17.89079 | -57.45532 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ec5ffccd-3224-32ce-ae69-f0a15c000f41 | -17.86652 | -57.46213 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f42a9a8f-1f37-33be-8e35-aaaba9603a96 | -17.8567 | -57.46583 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5513df83-9973-3c3f-b4cc-408967962cb4 | -17.85209 | -57.46522 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7a3ab45b-1969-32d9-b61f-bf8e78ce8516 | -17.84689 | -57.46954 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 217a5a74-9ebc-332a-acb3-74bc2d0f4c93 | -17.8433 | -57.46728 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0d64923f-f1f3-31bf-9004-d6822e2d06b8 | -17.84269 | -57.4722 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fb16519c-65d3-36ae-92aa-fd9c0c47a2cd | -17.84227 | -57.46892 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e60f9e42-6981-3015-a0e3-82e47e7328b4 | -17.83869 | -57.46668 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c0e92142-e6f5-38ca-be49-5c2258d41043 | -17.83766 | -57.46829 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9fd4fe15-df41-3826-9450-6130d27d7655 | -17.83468 | -57.46115 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f0d5fd5a-4793-376d-970f-d41130f547ad | -17.83407 | -57.46607 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| ad5f06e8-eb9a-324c-9379-fe3498c551d3 | -17.83362 | -57.46276 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f99bc529-4d65-3045-a926-7ca3a25c1f0a | -17.83305 | -57.46767 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3447aba9-ace3-3d04-814f-36638e2727f8 | -17.83007 | -57.46054 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3745696d-50f8-35d8-b2bb-bc7f087342b7 | -17.82946 | -57.46546 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 737f2200-a4e3-3d7a-9bd7-f788ceb0ae82 | -17.829 | -57.46214 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3013289b-338e-352a-a63f-d7bc79a5fef8 | -17.81502 | -57.46855 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| e5f8766a-e1b3-3062-b6b1-11d4027fe227 | -17.811 | -57.46302 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 90af8f21-f0f1-30a2-a847-50d2b8edd428 | -17.8104 | -57.46794 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| c57aa352-5b49-357a-8d8b-dfa5cf93f58d | -17.80699 | -57.4575 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 6d73c28c-337c-3d45-aab1-a682d1c4b97f | -17.80297 | -57.45196 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 25e3e58b-7e87-393d-b17a-ff3114a63fe5 | -17.80255 | -57.41679 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 879875f5-0254-33ed-906e-c0638204e2e6 | -17.80238 | -57.45689 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 35b08012-b7de-32e2-8624-4b9b6f64108a | -17.79955 | -57.44149 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 63f00c0c-d6aa-32e1-a02d-904fc51471a2 | -17.79896 | -57.44643 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 3836c863-9642-3516-b79e-dc42e357f140 | -17.79836 | -57.45135 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 1971e2b9-cabe-31d5-b91c-7e17bcf3f158 | -17.79792 | -57.41618 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7e21c010-35b5-3fd0-bb32-2e3219a3026d | -17.79732 | -57.42112 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9ded0b11-49ee-32fd-a2d6-0a6a8d9c131b | -17.79613 | -57.431 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3a7b3697-99c2-34a3-9805-b613df879bb5 | -17.79553 | -57.43595 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bf9c25d6-4a15-3fe9-858c-1f63fb5f6cf3 | -17.79493 | -57.44088 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| b11fd60e-8e8a-38ef-ad28-0b18731857c2 | -17.79434 | -57.44581 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| d4e39147-0ab7-391f-b8d5-93f65fdbccf4 | -17.79269 | -57.42052 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 3eb72096-4b1f-3b2e-9a06-cfc4bd7d4f8e | -17.22615 | -57.31197 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a214df4f-0583-3867-9cfd-fde4f96f72df | -17.1922 | -57.4805 | 2024-10-17 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 20f2c8b9-91d2-3743-b6ad-c4d34613d268 | -17.19171 | -57.48356 | 2024-10-17 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2cb7d0ac-661c-3cd6-a68b-dfef19f9628a | -17.19163 | -57.4853 | 2024-10-17 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b0e6e298-e6bb-3278-b728-a4abe978afbc | -17.18714 | -57.48296 | 2024-10-17 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 92c3a4da-5c8a-3c79-a9f6-663417b858d0 | -17.16198 | -56.82436 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 49561d34-d882-33f5-9c2d-097dec7dc351 | -17.16189 | -56.82875 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1d2fda20-8acd-3b02-a5f3-54bf7f5cd0a1 | -17.16136 | -56.82969 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0c99b0ef-fe3a-36b2-81dc-57a5f19875a3 | -17.15994 | -56.84465 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 93de5d6e-dab4-3d69-8282-56ddb857e7ce | -17.15953 | -56.8456 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e71a2d4a-ebb0-3113-b109-903ef545ee3a | -17.15712 | -56.82815 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7f1092a4-0d96-39a3-b4ac-cb14a38222a8 | -17.15659 | -56.82907 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7ff27733-7576-330f-a815-efde71e33215 | -17.15355 | -56.85554 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 09246faa-9d98-30c1-aea8-3377072be8fe | -17.15324 | -56.85986 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ba873c18-0e28-3b60-ae6b-eb807cd370d1 | -17.15295 | -56.86082 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dbe24494-f85d-33bf-a9c4-71a3766477a6 | -17.01374 | -56.8497 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b8b5ab96-c04e-313f-a017-d6d487d10160 | -16.97402 | -56.81782 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9de89b88-a0ad-34fd-b141-6975b721f34a | -16.96926 | -56.81721 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 37e5f4a7-84a6-3dd7-8dd9-ce64452b8967 | -16.95847 | -56.78806 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 83ccf304-ea27-3890-934c-b47f6f68a5fd | -16.95803 | -56.78891 | 2024-10-17 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README58.md)
