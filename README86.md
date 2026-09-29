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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dbc7a65-70b5-3537-b601-4b682f4cdcbb | -1.3008 | -49.0613 | 2026-09-29 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 7b809265-73de-38ec-9bbe-5e55022b3722 | -10.2067 | -49.9898 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 18367475-c9fa-3dd0-920a-a6b5dc41e056 | -11.9845 | -50.2864 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9d2a6aac-56e5-393e-aa6e-fba80cf91d00 | -10.2446 | -49.986 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8e72f882-fae4-3e1f-991e-90b2f30dcfc6 | -11.9803 | -50.5657 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 8c053827-2d22-3991-ab4e-54ef6936dd31 | -9.9266 | -60.7171 | 2026-09-29 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 920d7310-cea8-3179-826b-f8720000ec7b | -15.735 | -46.0384 | 2026-09-29 15:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 219.2 |
| ba64e630-e0e8-3186-9edc-a5ce458d65d3 | -12.1741 | -50.3497 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 27012ea6-7f7a-32e7-b427-24177660b2ff | -15.3998 | -47.9261 | 2026-09-29 15:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 92595ed9-2971-34e7-a670-9cfb1bd2f54d | -12.0559 | -50.5996 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 27724239-5509-3451-b833-6991c933ca87 | -12.1543 | -50.395 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| dbd1b080-4724-3ece-9bb2-879e1dcbdbb4 | -10.207 | -49.9684 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f636a47e-af77-3f8a-9503-3d3b55851b6a | -11.7887 | -50.6521 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 660d03fd-a8b8-32a7-a1de-ca27380a7ebd | -12.1557 | -50.3089 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 38726522-f248-3cbf-a5d7-5dccf1370e93 | -11.4788 | -49.7646 | 2026-09-29 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2938009a-4fb8-36b6-bac3-7286a91681ac | -10.6892 | -50.6445 | 2026-09-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 024e4081-afb5-3fb4-83ec-ee8bc694838b | -11.8608 | -50.9212 | 2026-09-29 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 36027f00-539a-30c1-96c1-d29e6df7fd18 | -10.3895 | -61.231 | 2026-09-29 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 4e13a86b-82f8-3ab0-bc06-45dd2a5e3048 | -10.9671 | -49.7152 | 2026-09-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e00ebe4f-65f4-3054-9cda-fe93efa81055 | -17.2931 | -44.5157 | 2026-09-29 15:20:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 147.0 |
| f9fed01a-c08a-376e-a4a9-6f58886f14f0 | -10.7064 | -44.4317 | 2026-09-29 15:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 5d4f3476-b422-37ed-b6cf-68e5e3935d8d | -10.2824 | -49.9821 | 2026-09-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f023a367-0d43-3964-9ee0-e247b9011ab7 | -10.9722 | -50.6998 | 2026-09-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3212369a-df2d-3fd1-a550-1c53ac4ac296 | -20.8373 | -57.6891 | 2026-09-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 142.6 |
| 5e33a1db-a714-3823-a34b-2a0e4f332c2b | -12.1744 | -50.3282 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a8c89324-32e2-33df-ba85-94f5f027ccbc | -12.0317 | -50.9442 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| aac47b71-cf0d-3f3b-ae6c-1df989ea5291 | -11.7824 | -51.0791 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 07aa887a-5e36-3549-ac8b-5e189bd58d72 | -12.3092 | -50.2473 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c1db4c89-9002-32b4-978e-ed12d8bdb7d8 | -12.1547 | -50.3735 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 566aaaad-400b-36a6-8af3-7321f4c3c676 | -11.7887 | -50.6521 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f2dff0c2-8618-32db-97d6-b5c1446eb9e4 | -1.4672 | -48.931 | 2026-09-29 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 516b5fb4-f1a5-39d4-ad59-43b5800fba2a | -12.288 | -50.3789 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c3a34b86-a6f2-3231-9738-f9f61679340f | -12.3679 | -50.1539 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 8340fa1d-437a-3de3-beda-f6a4fac9d001 | -10.2067 | -49.9898 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 8997e1e8-b2a7-35fc-b784-2ea9ab30b44b | -12.1734 | -50.3927 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 751fa4e0-fe30-32cc-bcb7-9320302c0b2a | -11.1331 | -50.0409 | 2026-09-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 2e2671c2-a8c8-38c3-bb4d-ca8c4856f77a | -6.9795 | -71.755 | 2026-09-29 15:30:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| c1d4fa64-0485-3c67-96be-78a7d671ad76 | -12.1185 | -50.2489 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5bda3ede-7145-3629-8580-9579fcf989b7 | -9.9393 | -50.2518 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 839a9224-2d64-386d-abe5-81cc56d8fa16 | -12.2897 | -50.2712 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 45d0156c-5b56-3a74-8051-74f43f67d839 | -10.2446 | -49.986 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| a66e8e82-b6fe-3f41-ae3b-1a53c15bb559 | -11.1517 | -50.0603 | 2026-09-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| fb163e71-8237-393a-9edf-f71ea4dc1964 | -10.9156 | -50.6845 | 2026-09-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 5b857c6e-1f99-38aa-986e-243b28f91b9b | -11.8862 | -50.4911 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 719cf015-fe31-3397-a61a-d746b8b28c87 | -9.9598 | -50.1217 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a975dd03-f667-30a5-8095-770c10d784e0 | -11.8478 | -50.517 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1c899582-2a8f-30b5-a9da-5f41991febb5 | -10.9912 | -50.6978 | 2026-09-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 03545295-69d8-3f41-939f-d65570355289 | -10.9864 | -49.6915 | 2026-09-29 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| f8e0ae1a-35a4-39aa-9218-3a04e108f451 | -1.3193 | -49.061 | 2026-09-29 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7e76fe05-562f-30f1-ba99-eb0e3150c1d7 | -9.9787 | -50.1198 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4332acec-5e23-31c7-b9e6-a03e43c1e504 | -11.7828 | -51.0578 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8961f883-4d7b-33db-b5f8-f228d41f1d3a | -11.5625 | -50.5283 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ad8366f4-004c-38b0-8b73-6094d0d73192 | -12.2901 | -50.2496 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a6e48940-4fa2-3b8f-8a62-921d20046e41 | -11.9373 | -50.8912 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3e100d8a-7383-31ce-ab9d-154668948fc9 | -11.9183 | -50.8933 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7f44597e-feb0-39b1-8d00-5cbc2b390426 | 1.8587 | -55.5648 | 2026-09-29 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| eaa27608-7819-346e-a6af-ae3fcdb7f15a | -15.3807 | -47.9068 | 2026-09-29 15:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ff13190c-24df-38d9-a424-6f573dd423b0 | -20.8373 | -57.6891 | 2026-09-29 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 155.4 |
| e9384dd2-e860-3554-8cb4-62311fbb157f | -20.817 | -57.6919 | 2026-09-29 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 133.8 |
| d32682a8-c197-359e-ae6d-fe2e9f1e6cf7 | -15.3998 | -47.9261 | 2026-09-29 15:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ebaaa242-d389-3dd5-b24f-42ac4335e57a | -10.2065 | -50.0113 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ef3343ca-b1e4-300b-90db-8fd14a49c811 | -11.8024 | -51.013 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b74615ea-fd4e-3a04-9562-d16928575d08 | -11.1707 | -50.0581 | 2026-09-29 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| cddbc4c4-9787-361f-a0ec-7f8fbf230945 | -11.8421 | -50.9021 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 07927679-55f0-3ac1-a97b-8755242de357 | -12.2703 | -50.2951 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 58a85a11-bb5a-380d-b8b6-76700ab809a2 | -12.2894 | -50.2927 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 7f114344-f196-393a-9879-0422add5189f | -11.8678 | -50.4504 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e84d41d6-4d52-334e-9964-23d639f0b1d3 | -11.8611 | -50.8999 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| cd5f4f8d-9384-3ef4-8b7d-9441caded7a6 | -11.8427 | -50.8594 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0158f35c-9f77-3cbb-bf21-d94b87fab8bb | -20.8369 | -57.7101 | 2026-09-29 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 125.4 |
| 764c6886-578d-3dfa-9ba2-0693c1e35620 | -10.9159 | -50.6632 | 2026-09-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f5afb8c1-2005-3dff-b017-3b42fad3f6e6 | -12.0314 | -50.9656 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| b50b671b-ca2c-3ee4-a6dc-df51bfda0fe8 | -11.8608 | -50.9212 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2b38405e-2690-3bb0-8089-15fd7bd7c6a9 | -11.77 | -50.6329 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b8bb1fba-3b2b-3173-954d-eafcbe626bf3 | -20.9159 | -57.8246 | 2026-09-29 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 132.6 |
| e2e3fd7f-2126-3b6d-9a32-3e3e741d98ac | -12.155 | -50.352 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d75928e4-061f-32a4-b620-8987dadd136a | -3.2955 | -59.4284 | 2026-09-29 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c45099dd-24a0-3827-b46f-21d96380cb2f | -15.3802 | -47.9294 | 2026-09-29 15:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 78d566d6-1b60-3a1c-a1ca-b81ee8c78a79 | -10.2257 | -49.9879 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7d1c22b1-5aeb-352f-9dc2-37dacdc8fee1 | -20.6905 | -57.9607 | 2026-09-29 15:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 3e530e48-a896-3df2-8fb4-1b85ea429d17 | -12.0997 | -50.2297 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| c159aeed-4f1e-323a-9846-bd8861219d79 | -10.934 | -50.7252 | 2026-09-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 03bd37bb-0bba-3ea0-8b17-7923ef9fbb8d | 1.8587 | -55.5846 | 2026-09-29 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 41d2e413-bfb8-38e9-afdd-eaf4b9300108 | -11.8481 | -50.4955 | 2026-09-29 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1eb24dd0-ac03-39f6-aed0-ea905ad5bb4d | -1.4303 | -48.9102 | 2026-09-29 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f2ce10a9-701e-32fd-8db7-7a451a024292 | -1.3008 | -49.0613 | 2026-09-29 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ad53e356-200f-33e4-a6b8-ae82ad047930 | -11.058 | -51.3482 | 2026-09-29 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9aeb40a2-5ddd-3140-aa8f-e002b51e39a3 | -11.764 | -51.0386 | 2026-09-29 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4ed9c293-bc43-3c14-ae3c-1f74d320e0cc | 2.2371 | -50.8973 | 2026-09-29 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d405055c-af2c-3d69-a2e9-67241e5d35b2 | -11.9596 | -50.6751 | 2026-09-29 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b918fe33-1a81-3555-afa7-31841f59a178 | -6.9795 | -71.7732 | 2026-09-29 15:30:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 388.6 |
| 4c8a73f1-29e2-3809-90d3-2abdfdd4f95a | -9.9582 | -50.2499 | 2026-09-29 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 00f9752b-fea2-348e-b272-cdd66683c295 | -10.3894 | -61.2502 | 2026-09-29 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 5b5bbc20-7b58-3ebd-8f4b-b202ec25a206 | 1.6476 | -50.8874 | 2026-09-29 15:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1920f0f3-2bbe-3d1d-8eed-0f70d7ac136c | -12.1547 | -50.3735 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b51b8ff5-ffb4-331f-8203-b6753f1a476d | -12.1737 | -50.3712 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9803fba3-1458-312a-8c8a-3849e658f797 | -11.7831 | -51.0365 | 2026-09-29 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3bd0a2c0-dafc-3c21-b82b-10e33411334c | -6.9795 | -71.755 | 2026-09-29 15:40:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| e4893f65-265a-34c8-a3e9-fa49fd91c6d7 | -20.8373 | -57.6891 | 2026-09-29 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 146.9 |
| ba9f3e3b-63d8-3e38-b9df-921e7beb38dd | -12.3679 | -50.1539 | 2026-09-29 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |


[Clique aqui para ver as próximas entradas](README87.md)
