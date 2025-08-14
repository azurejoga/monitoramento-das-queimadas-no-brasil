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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b28923-acf3-384c-b605-9ba419a17d90 | -7.13749 | -59.64838 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa264f21-8de4-3c11-bace-92aa91fe2fec | -6.92289 | -59.14958 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 355c17e5-2b98-3ab7-bc7a-1935430c3289 | -6.09052 | -59.94699 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 521cc18b-a321-36a4-b1d0-3a61d520336d | -6.898 | -59.14522 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b3ada9ef-fc96-3834-9667-39d6b4aa136f | -6.52929 | -56.20586 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc31bc67-5c7c-3e06-b31b-388f06bf533f | -5.75631 | -59.88869 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a00e8184-3e45-3f0b-9969-fc4e22e63924 | -7.4614 | -59.88828 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03830aaf-a0df-33ff-85ac-18beb7d557d4 | -8.74369 | -44.03035 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 919f9e6c-b97a-3204-a222-737af7d5c8e2 | -7.28371 | -55.3076 | 2025-08-14 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8a1e453-8d9a-3e97-a2f0-96de1fc65e3c | -6.89603 | -59.15648 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c1e2b847-86e1-3e5b-96de-7b26ef9ab9e0 | -6.5381 | -56.20367 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f945eb45-19d3-325b-9c08-9da7166aed34 | -7.33812 | -60.62298 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21d1e60b-3ac1-3999-bf5e-c9a0a8c7075e | -8.52386 | -43.3007 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c515e491-7af8-3e95-a6fa-f7e4be7f4552 | -6.92786 | -59.15048 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ac4983b0-e558-3fd2-b526-3a2729e27830 | -6.91292 | -59.14787 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b329b81b-d0e9-30d8-89dd-f23cc3372b4b | -5.73112 | -59.89186 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb2116cd-eb52-3988-a105-c0081a02c7d9 | -7.72426 | -55.2066 | 2025-08-14 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f6c5ab2-c0fc-3d0b-bbcc-4483e822c175 | -5.75988 | -59.89961 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63d87c09-6701-3b2d-8268-0b021ae57daf | -5.75054 | -59.87461 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ece69ac-3e23-3492-bb05-e8fbc3d79114 | -8.52648 | -43.31852 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fd41aa9d-490e-3e29-8d4c-5979825dcb79 | -5.74943 | -59.88116 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0ce582d-2b74-3d6c-b826-898bb90f7b86 | -8.09413 | -54.98751 | 2025-08-14 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1002789-9a8a-3110-95a5-4fbe6c2f5650 | -6.77184 | -59.47557 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb9fee5b-18e2-3fce-87fa-b123854ea89e | -7.26288 | -60.00383 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c2bd026-42be-3966-8af2-d18d2ae394bd | -5.74797 | -59.87378 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cf90f07-c22f-3643-b804-a361970fdb99 | -7.32724 | -60.62208 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 656d0227-27fa-3d0e-94bc-0ccc0e3e2622 | -6.87811 | -59.14156 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ec45164-0304-3a56-bf91-8a36b6bed829 | -6.91092 | -59.12991 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6665dc6-9c52-3502-ab57-ee619b996437 | -6.85553 | -59.96703 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4316b1-c600-3a4d-82a1-a6edc7cde33f | -8.73155 | -44.01291 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a0e8fcc-2caf-3cd3-b0d4-f26b8268ac24 | -6.53872 | -56.19996 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa5b321-912f-390a-b6c6-93b78c3a8d5d | -5.76165 | -59.8896 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8b4876c-859a-32d5-b11d-4a1b0a4c670e | -7.23825 | -57.64281 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab000230-357a-320f-b9fa-4ff7f8171689 | -6.88506 | -59.13121 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d6c9450-561d-3e6d-add2-582fc4ac5f30 | -5.74386 | -59.89689 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6d93f6e-04c8-3290-9eb0-bed5d6bcac8d | -6.94013 | -59.63818 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e948537-4351-3606-8542-3369fb873b35 | -8.5257 | -43.3242 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18b0c6be-869f-3baf-81cb-1ad239b51bd5 | -7.2897 | -55.307 | 2025-08-14 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbecc8e4-83aa-3bcb-9d6c-2c0ac88dd146 | -6.64301 | -59.07733 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee00b84d-18d9-3cec-9255-27039c155450 | -8.52151 | -43.3178 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 506109b6-d0eb-3c13-bf5a-84a04be0c240 | -5.74204 | -59.87622 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6e621d4-5233-37a8-866d-c6348ffb2c4e | -8.26386 | -45.0626 | 2025-08-14 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7e0f2f4-16a6-3f6f-acec-11f262af858e | -5.74327 | -59.9002 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fc0a888-0d6a-397a-ae96-7892a4fd28d5 | -6.06989 | -59.93945 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aee2b2c7-06d4-335b-aa85-dff59daa2b41 | -7.33749 | -60.62655 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 936f92a4-6222-36fd-8c68-2054efa96a97 | -5.75929 | -59.90297 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fc77580-fd57-37a4-9a1c-b74e181a350e | -6.10239 | -59.94188 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d393e9d-3139-3384-8b78-c09fb4f49bf1 | -7.14152 | -59.65556 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71160929-048a-3364-8803-c2f8915ed26e | -6.0693 | -59.94277 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34206f2f-78d8-36e1-bd82-68877555cc92 | -7.12835 | -59.64026 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb1921f8-23f5-30c9-938e-cc3d8b6d02ac | -6.77384 | -55.48653 | 2025-08-14 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2a0b31-dfdf-31ed-ba73-5e52f74d54e6 | -8.52465 | -43.29494 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 9d57d5d5-f696-3f9d-a74e-8ab2e7c5d886 | -6.8791 | -59.13597 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88004d98-8711-3543-8523-683e081c693c | -7.33141 | -60.62914 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2578d3d-bbb5-3b4e-a429-0471dd48d9d2 | -7.46164 | -57.65278 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 98e45b0c-4790-3da7-867b-76159129afa1 | -5.74773 | -59.89117 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7836dfbc-c1e5-3d3d-a1e8-ebf9250b09e3 | -6.77805 | -59.47027 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fbe860d-5a77-3e32-995d-62f9a9bb2c2a | -6.08402 | -59.95269 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f2889ba1-8667-31db-aec4-f663f30652f0 | -6.7724 | -59.47247 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 859ec473-58c3-3424-ac4c-ad69db65f201 | -7.26347 | -60.00054 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b98a3191-927f-35a0-867e-26668af77b09 | -6.53748 | -56.20735 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2044f963-c9bd-316f-8015-ead896c7a660 | -7.13292 | -59.64435 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30a6f936-6d81-34a0-baa9-ee6c89c73c58 | -6.10355 | -59.93528 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9dbd78c-35f6-3090-bb9d-18282b5f7cda | -8.51966 | -43.29427 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b71eb46f-5ce9-3dfd-89c2-a013d1b38fea | -8.79356 | -52.03986 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997ab0c2-d41e-33a0-9a91-996644717b8d | -6.9189 | -59.14298 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 81561217-b495-3940-a4c0-a3d14162534c | -6.78742 | -58.78638 | 2025-08-14 04:49:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00049868-a69c-3e5c-81c2-8518062300c9 | -6.88308 | -59.1425 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64ae6e7a-e3f3-3767-9cb5-9e78fa50b571 | -7.1278 | -59.64334 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e05042a-516b-388f-892e-cba8f7d04027 | -5.73432 | -59.88865 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78a4fdf1-f775-3407-ab09-6e511919998c | -6.77696 | -59.47635 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb05e55-30c7-3ffb-bd02-4c79949c7448 | -6.11179 | -59.91955 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548ea36b-63bb-3121-a35f-240f6b4226cc | -8.79689 | -52.04039 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30715309-5c01-3226-ac89-f02d05566d99 | -7.14498 | -60.12353 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78bb8e11-0b8f-3530-b459-936df32068aa | -6.91391 | -59.14218 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0034de53-dc53-3f1c-87c4-6b4fb650d45f | -6.93497 | -59.63734 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 046cf0ca-e707-3650-a05f-30c99b2aef25 | -6.90099 | -59.15745 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f019c38c-080c-3111-b6bf-07d5d98ec877 | -6.534 | -56.20293 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc9602a9-ffa6-36cc-ac2b-a60f65056fd3 | -6.91193 | -59.15362 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e09f043c-f0ee-3619-8b06-6827d174053a | -5.75156 | -59.8845 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ce212f-235b-32dc-905e-2d1aa9d44228 | -5.75097 | -59.88783 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a45c6fb9-8ca9-3a4f-b63b-18916819aa22 | -6.53053 | -56.19852 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d40eded3-d5c7-331b-ba98-d04df84bf6fb | -6.90893 | -59.14134 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e5881f8-f3bf-3b4e-8ca6-dc96bbc05114 | -7.28588 | -55.30632 | 2025-08-14 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86d06be1-71a5-3cd8-abf5-cb9a23062b7c | -6.94066 | -59.63515 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe3e03a-378e-3e1d-90c4-49605991af5e | -6.90296 | -59.14614 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8c081a90-bb99-3bf2-a049-0fad45835430 | -5.7569 | -59.88538 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02cc8915-c6d7-367b-bded-680538cc7a82 | -6.77401 | -59.47789 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f36aba72-397e-3ab1-9814-89aa84dd594b | -6.91691 | -59.15449 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0c6731bb-ccfb-3130-aac3-127e16be71d8 | -6.77455 | -59.47479 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d063d78b-9385-3495-970f-8e8ca58e41d3 | -8.73966 | -44.02447 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3e2a21d-1c6e-333f-8df9-9aae476ced22 | -8.52307 | -43.30641 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b7b8310d-3991-3506-9fcd-3873909e2af4 | -5.74503 | -59.89032 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3edd619-34ea-37ba-8421-73f052ecdf20 | -6.10588 | -59.92199 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0fc40c9-7c7f-37bc-bcc2-f5c7eb1ba561 | -9.31798 | -46.2247 | 2025-08-14 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13d9618f-3c73-3217-8a0d-9c7eabe4f33e | -5.73647 | -59.89271 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa95a5ed-b1fd-313b-88cd-ca096fc9be57 | -5.75215 | -59.88116 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 622ff1e6-1c9d-3fd3-a2b0-09d8be8ea750 | -5.73872 | -59.87954 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70b9606f-fb9c-3499-b5c5-70938aa532d7 | -6.09878 | -59.93121 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 905fa5d6-5aeb-348f-b7a4-9b3be2ac9bed | -5.74321 | -59.86961 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
