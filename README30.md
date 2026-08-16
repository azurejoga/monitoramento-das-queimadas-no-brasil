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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67ac1453-2efa-3e64-8a41-79e3e4d583a5 | -13.79685 | -53.79456 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 247333e7-221d-374e-b008-68e7a7a73b9c | -14.42082 | -51.84599 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb65dab3-bcd9-3647-beab-88a497f542b1 | -13.80037 | -53.79506 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86324d5d-7757-3172-8103-4faf3801a23e | -14.52666 | -53.28598 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d185178d-cee9-31db-95db-fdf469974c42 | -18.30754 | -44.51116 | 2026-08-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f0004d0-7880-3ca8-9728-e45d34a34db0 | -18.59165 | -47.13241 | 2026-08-16 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cb1e5af-67b4-3dcb-a927-13038fba4602 | -13.80427 | -53.82004 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f33490c-d6f6-324a-b634-4f3e991be932 | -12.68063 | -48.45329 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6f6cc10-cfbc-370b-bdb6-fbe90e9da717 | -12.68314 | -48.46851 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 526fb54d-dedd-37b5-a376-30534c1b7038 | -14.96602 | -46.63283 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbb8cc62-ba84-363e-9153-8faab326852d | -14.49343 | -51.96769 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abbe8a6e-de0a-3b99-9a8b-1a30a7ce6167 | -14.40178 | -51.92336 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d667017-07a1-3199-b78e-c38a3d1e3af1 | -14.22141 | -51.81633 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fa56c1c-5be0-3be1-9ebc-e358027279df | -14.29228 | -51.94924 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4a46acb-7353-36df-93c3-c95cfdb82c98 | -15.70576 | -47.6284 | 2026-08-16 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 33e56368-0ac9-32a3-8557-8db6c472827d | -13.44077 | -43.84367 | 2026-08-16 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ad70d2cf-4e26-3805-8e32-45a0b32e57ef | -15.0481 | -47.02686 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93672680-922c-3633-b5a4-d4d15747ab44 | -13.77818 | -53.82044 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c3a43e6-2ebd-3ea5-870d-1ed2be1bd3d2 | -14.48634 | -45.67902 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9919498-6ae4-3933-8f58-70e812efa74e | -13.50595 | -48.22216 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 389ebbf3-e590-3a4b-92fd-94c0812d76a3 | -18.31706 | -44.5125 | 2026-08-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9cff7e3-4f92-370d-bf82-c0de20e58b15 | -15.10048 | -48.71585 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 417a994b-1775-3812-84eb-8a17b7fc0974 | -15.1202 | -48.07898 | 2026-08-16 04:42:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8ab412-c88e-391a-b6f3-c91f24bd3887 | -13.49704 | -48.23368 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45052532-7972-3145-b5cd-cbc6b5b3748f | -13.65611 | -46.24385 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 369ce400-a2ba-3272-869a-70c9aa334c8d | -14.04728 | -53.66146 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae08fcf3-ed4c-37fb-9146-55c56de22b90 | -12.74941 | -48.43093 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e39bfd-f4d4-332b-81e5-d5b79fbc17ac | -14.06454 | -58.74469 | 2026-08-16 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f8451e36-1e28-3c19-87f1-48469a5cbdc3 | -16.10383 | -49.85197 | 2026-08-16 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cf1b733-532d-341e-a0e1-8f9d6a21b679 | -12.70167 | -48.43918 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adf235ca-9716-34be-af2d-f0abb3410c70 | -12.70532 | -48.48808 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c26186e1-34ae-3740-8487-22f0f3210a5b | -13.78869 | -53.82224 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8feb4c13-bc11-3f11-8171-ec2b07b01314 | -14.77777 | -56.95464 | 2026-08-16 04:42:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9155584-cdba-38ab-a2ab-bc6b2b4115b0 | -14.9084 | -46.64144 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f18c8fb3-68bc-3ee8-9f47-eaecf228bee5 | -14.10492 | -54.51807 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 672c29a4-1ab8-3b0d-844d-d5a0890f548a | -15.27059 | -56.12334 | 2026-08-16 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 620b9fd2-6d54-3141-a9d4-a0fb90efc485 | -15.49105 | -47.6445 | 2026-08-16 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93d1982b-ffdc-3be4-97af-617ba76128a0 | -14.91981 | -46.61611 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3c4361d-7cd0-3d86-b1d1-e7e7024407a3 | -14.39959 | -51.91567 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48ce348d-b971-392c-b74c-2fe8e30c8ed3 | -12.70351 | -48.47594 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 113cc93f-711a-33ee-8cf5-a9ca5152ed71 | -14.53007 | -53.28654 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a536991e-a1b5-3c2a-957f-ce8ead601251 | -14.48115 | -45.68628 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a7d66dd-c216-3737-ac3d-7c3370624c80 | -14.32587 | -53.31081 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba3a54c-d5f1-3eea-a476-2fff14a80fe5 | -14.42694 | -51.82873 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05202ca7-91f8-3799-9413-f4981b524288 | -13.81605 | -53.76528 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d54a54-0704-3b39-8f4f-455f03df6e18 | -12.70643 | -48.48041 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9241a9b7-e413-37b5-91bc-339953b90483 | -15.17593 | -50.06803 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4f4f064-d20a-3f30-97ba-75666eefc0c5 | -14.37806 | -51.90111 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7154d6fe-051d-30c7-9dd6-58ccaa89e94c | -13.91023 | -53.94529 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eaf0771c-1113-3d3e-9ffa-1b7df4f74c91 | -18.62784 | -48.60276 | 2026-08-16 04:42:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d09d7d50-9886-3569-bc34-36eb07f89b4d | -14.4684 | -51.99654 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d60320ff-c35f-3814-867e-7d2a80628273 | -13.43979 | -57.0357 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff9ad94-2e99-31a7-b69a-67c28c1147de | -13.70712 | -51.88473 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa6db1c5-88d5-3578-bc90-d77a0557e852 | -14.05891 | -58.7489 | 2026-08-16 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcf743d4-322a-3f52-8d5a-6d3927f8d4ed | -14.38752 | -51.88438 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b4b9d1d-eb3b-3611-8ecd-de290813da75 | -13.43274 | -57.0508 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6c953ba-e848-3ca4-ab70-45d8dd895a11 | -14.90649 | -46.62532 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 506bd5bf-c011-32ae-8853-4b932c6f5895 | -17.17691 | -46.11555 | 2026-08-16 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a5b6268-3ffa-31af-b7f6-b2657b77b630 | -14.42526 | -51.83941 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e19904d2-3464-38e9-ad28-696017aa8f11 | -14.39352 | -51.911 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08cf832e-95f6-3b7f-be88-6dfa9244fb42 | -14.29137 | -53.07178 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b535359b-9b17-36d8-a065-662028c2d55f | -15.04603 | -47.02303 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb8a2895-9bca-3ba0-8777-c92f24751524 | -13.44397 | -57.06116 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ccbe091-5474-3524-8652-c07c6d7dab39 | -14.38477 | -51.88026 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9356499c-a062-3be9-818d-b0a70d0c7fca | -14.93237 | -46.61278 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b93bc386-7565-3264-a29b-bdb9ca9f3874 | -14.46509 | -51.99599 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faacb8bd-5a8d-3fc9-b5d3-a131aa9e79b4 | -12.71162 | -48.4693 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 322a96b7-39b5-3f3b-9622-d0fe273f5584 | -12.67019 | -48.4514 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5df93721-59dd-3b4e-b807-0579f9eaeed3 | -18.30813 | -44.5059 | 2026-08-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ebf1504-0075-30d8-9cf7-a8eda7c6249a | -14.33183 | -51.9777 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5bbf580-cf23-37d0-9309-691a316c5002 | -14.96205 | -46.63232 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f72f551-83c1-33ef-a460-8686f16f06a0 | -12.72324 | -48.46315 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cc129d8-9602-3027-a314-b886f0e78942 | -13.68994 | -46.2507 | 2026-08-16 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d822958-34da-34d8-929e-35b2f29f01e6 | -13.65415 | -46.24488 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 29bd6414-401e-3b61-bfa2-93e0b79dfddb | -14.49165 | -52.00041 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d91ca463-c378-3120-b62b-04c6349d32ab | -11.57991 | -54.68622 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afd872d4-e0c9-3aac-aae0-3ce503ef4081 | -12.89772 | -52.82743 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f152cf-efd9-3045-95ba-509478478002 | -11.58478 | -54.68475 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e80ae53f-4cea-3898-bbaa-758c23ca98b1 | -14.71406 | -52.88712 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fcea279-86fb-3a47-ada0-4c7c3aa6b50e | -15.16918 | -50.06698 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bceef511-08a9-30b4-97ce-ac0d840b1e29 | -18.95283 | -47.32508 | 2026-08-16 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a616013e-e14c-3458-99eb-4e9af5ee565a | -13.54876 | -43.59378 | 2026-08-16 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e12961e-b7dc-3240-89d1-0481b237107f | -14.90316 | -46.6506 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 09c8b0fe-ca20-3953-bcd9-81f309a1fe5c | -15.06987 | -47.0219 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b42ae769-8270-3bdd-9599-362f6dfd6466 | -13.91443 | -53.94185 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ea55d15-cc3a-3622-9112-bf9fee2a7097 | -22.77435 | -47.09433 | 2026-08-16 04:44:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e4ee070-9482-3338-acf2-fc9155c196c5 | -21.53441 | -46.76147 | 2026-08-16 04:44:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f07a9a99-52bf-3c86-8a9a-778362d6dcac | -22.79543 | -51.40089 | 2026-08-16 04:44:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fe1eb348-5a66-3ec1-b06d-5be8bb3d8a4e | -21.43432 | -45.188 | 2026-08-16 04:44:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 44b54e84-d8cb-3af7-b6b3-7893e3f6924b | -21.79535 | -57.32916 | 2026-08-16 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74ba048d-0045-3f59-8f1b-f8916be3acf1 | -20.33545 | -46.7261 | 2026-08-16 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfc50d2f-bce7-329a-bf88-9aba3d5c586c | -22.21988 | -48.62451 | 2026-08-16 04:44:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 41ea49f9-39b1-3719-abac-580936962dde | -22.79942 | -51.39747 | 2026-08-16 04:44:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 814bd2a2-f7f4-3b29-8030-1ac8e023d4d5 | -22.79657 | -51.39286 | 2026-08-16 04:44:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 5c64a52b-fc0e-3f70-b01f-f9d936f1251e | -18.7312 | -51.00756 | 2026-08-16 04:44:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f25be805-898d-3045-ab10-c6893af851c1 | -20.34554 | -46.74909 | 2026-08-16 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c64f81a-0bba-31c9-baad-d1e323450963 | -18.73064 | -51.01135 | 2026-08-16 04:44:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f884a0d-e923-36b3-8917-01dd8cac39c0 | -18.92512 | -48.21864 | 2026-08-16 04:44:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51ea5f8c-14e9-3c8e-b564-d110086cc9dc | -22.21922 | -48.62973 | 2026-08-16 04:44:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d9f60c23-dde0-3369-8ba4-7f711a0026ab | -20.87155 | -47.01611 | 2026-08-16 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)
