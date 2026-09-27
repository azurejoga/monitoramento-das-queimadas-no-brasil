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
| 3c62c2be-03c9-365e-aceb-51ba9e502209 | -11.16131 | -62.86761 | 2026-09-27 00:56:00 | TERRA_M-M | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d493e96-6ece-3445-a4b1-82a276676729 | -10.25237 | -59.13838 | 2026-09-27 00:56:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 157ae62f-9e23-30d4-ab89-8c708fe55dec | -11.02577 | -54.05698 | 2026-09-27 00:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c2612365-79d2-3daa-9c77-7b240aa6168b | -12.8884 | -61.71687 | 2026-09-27 00:56:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a23f7af7-04fa-315e-9fa1-a0e41f79f7b9 | -10.81993 | -60.73316 | 2026-09-27 00:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 7c65626b-0866-3b63-a4bd-eb4cbf6e7160 | -11.99473 | -57.60779 | 2026-09-27 00:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 02cc4f0b-19b5-3b60-b923-ed77f2b3665b | -9.92852 | -60.71668 | 2026-09-27 00:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5c3912a5-d5e5-36aa-b9f4-f2e426b0e22e | -10.80883 | -60.72399 | 2026-09-27 00:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| ed1b3f79-d736-3a7f-b155-24ecb8d3169e | -10.247 | -59.13163 | 2026-09-27 00:56:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| cfb27ccb-940e-3dc1-8636-c3541dbd4126 | -10.80728 | -60.71338 | 2026-09-27 00:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f250b403-dabf-3d41-a38b-2525fb433135 | -12.89868 | -61.72482 | 2026-09-27 00:56:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b87bb2f4-3252-3113-bac6-b13a6481eeab | -11.98306 | -57.60992 | 2026-09-27 00:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 20d26fc2-b682-351e-bfc1-0b01cdb1b4e3 | -10.81684 | -60.71194 | 2026-09-27 00:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7477151e-6a0a-33ae-9674-712fa2a4e250 | -12.89736 | -61.71552 | 2026-09-27 00:56:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f0d34543-ef30-31b3-aae2-e61082a2493c | -10.81838 | -60.72254 | 2026-09-27 00:56:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9bdb1d8c-e469-30ce-a6d1-03ab04e7acae | -11.27685 | -54.45058 | 2026-09-27 00:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 72cee29c-1077-3d7f-89a7-c013854ffa14 | -10.25024 | -59.12463 | 2026-09-27 00:56:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5ceb9c45-2a9e-3b25-9aa3-e08f4b75be38 | -15.43399 | -57.41397 | 2026-09-27 00:56:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6d9185c8-6192-3cd6-a0fb-948dfa495e88 | -16.17732 | -57.37235 | 2026-09-27 00:56:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63d6e712-c684-3128-be01-442e9dcf0c83 | -11.27161 | -54.42001 | 2026-09-27 00:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 29131fe1-1eec-3e43-ad54-4be14985b8c7 | -6.06113 | -57.82812 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 6a90c7ac-6cfa-3468-b002-3925a6cfe28c | -6.07289 | -57.82085 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 135dffff-2a50-3a43-a9d9-25fd313cbaba | -9.5717 | -62.7075 | 2026-09-27 00:58:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e7ad5f0f-ce3a-3f7c-a28e-372a695926d5 | -2.78948 | -57.69923 | 2026-09-27 00:58:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8864171f-00a9-3a70-b58c-48f642c378c0 | -6.08687 | -57.82431 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 72f8da8b-354c-38fa-9905-d273fc182812 | -9.28605 | -67.6426 | 2026-09-27 00:58:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c754f0ee-b7ea-32db-b3fa-39af187b8d36 | -8.60704 | -63.93513 | 2026-09-27 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14f52979-f81b-3165-bdcf-d75d9b8a53f9 | -7.69541 | -54.76969 | 2026-09-27 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| cac37bf4-5ba0-3a86-8a0a-c647a663b514 | -9.0741 | -66.10126 | 2026-09-27 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc27bacd-d550-30b1-bca4-2d6566cfb99c | -9.04025 | -66.0638 | 2026-09-27 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 11111634-dbbc-35eb-8d68-6bdd65f366cc | -2.66498 | -56.45379 | 2026-09-27 00:58:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c9280a8e-6f69-3cd2-b418-9cce1a324cc2 | -3.96429 | -59.35374 | 2026-09-27 00:58:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5d984072-fb75-30b2-8fd3-84c9e94b1cbc | -9.03891 | -66.05348 | 2026-09-27 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 980baced-a371-33b3-9cdf-8151e47516e3 | -9.53751 | -62.2724 | 2026-09-27 00:58:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 83b0778f-d741-3c18-919a-46fc522a9a5c | -8.90956 | -61.48425 | 2026-09-27 00:58:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6763f68a-a11f-3548-a36d-ff36ae1e309c | -7.68838 | -54.76406 | 2026-09-27 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 184ec9db-4c7b-33dd-869e-effaf7d55586 | -9.57042 | -62.69843 | 2026-09-27 00:58:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 714f8c84-51ad-3682-863f-4eec9fa9d299 | -6.08574 | -57.81882 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| b00fd1e5-5865-3b3a-9779-d0c9adca45cb | -7.71076 | -61.24801 | 2026-09-27 00:58:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de1b590f-289b-3f95-bb7d-c9a2d1ea2fe6 | -6.07102 | -57.80618 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 70d89740-f20b-3d87-bf2d-2ac75bda3037 | -2.66751 | -56.46024 | 2026-09-27 00:58:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 579cf346-1de2-3860-b8cc-26048965b82d | -8.60583 | -63.92627 | 2026-09-27 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72636d05-e2ed-3528-b286-6e014f922c2c | -6.0839 | -57.80423 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 73cf5ef6-4841-3ccf-8a90-43ca6e9c0b91 | -9.08835 | -61.44531 | 2026-09-27 00:58:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f1189059-7715-3fa0-b73e-1180431b000b | -9.08221 | -66.08963 | 2026-09-27 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 434789cf-e0f3-3c3d-b34c-23db9ad113f6 | -6.07402 | -57.82634 | 2026-09-27 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c4dd45b4-6a7e-3605-befd-2dd5d4fa4f3f | -9.53619 | -62.2631 | 2026-09-27 00:58:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 449b703d-e34d-3a05-9c26-d79a7fc1580b | -3.96188 | -59.33728 | 2026-09-27 00:58:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5f6e3356-1d1b-35f7-abfb-a6086dfbb9e4 | -5.3011 | -60.08727 | 2026-09-27 00:58:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 31d86dfb-2935-3e33-83f9-a1d3d830079e | -3.83532 | -55.92021 | 2026-09-27 00:58:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| dfa27de2-52aa-3a2d-8d65-97a61371ce80 | -9.15701 | -60.77806 | 2026-09-27 00:58:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7f436885-b4fb-3c8f-8ebd-aef91b8cefa2 | -11.0396 | -51.3079 | 2026-09-27 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1ff0ac7e-77c1-3b4e-8ae0-31fb440fb54f | -11.0393 | -51.329 | 2026-09-27 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c58963dd-971f-3233-aa99-d1f78241015a | 2.6359 | -60.1648 | 2026-09-27 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6323c874-91d1-3c9d-be54-ff265b5001fd | -10.8052 | -60.7257 | 2026-09-27 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 94067170-d75c-3b68-b3ca-6b01677c4c6b | -10.824 | -60.7246 | 2026-09-27 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3f6de7c9-38a3-364b-8975-df48df81398b | -12.289 | -50.3143 | 2026-09-27 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8bac02e1-24e9-31ee-8e34-ceeb86d6ddb0 | -8.0373 | -54.8926 | 2026-09-27 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 002d4493-bd41-378f-bcb9-b37e9304a417 | -9.2745 | -67.6433 | 2026-09-27 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ca50f87e-b818-37c9-9280-f5aff2434494 | -3.9228 | -43.0123 | 2026-09-27 01:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| fb739d7a-3208-3f9a-a29b-f9d6ab71719a | -11.2829 | -54.4417 | 2026-09-27 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5ee27bfc-7ef8-3684-a287-c4da23053ee2 | -1.61283 | -54.81686 | 2026-09-27 01:00:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 40472f36-2596-316e-9440-c675c9646fe6 | -1.61234 | -54.82192 | 2026-09-27 01:00:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 36835279-f98c-335f-8440-f1294cd8ad09 | 2.65005 | -60.1817 | 2026-09-27 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c80c89c8-0508-3c8b-940e-591fc25e0829 | 2.63497 | -60.17305 | 2026-09-27 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| cb3dd345-c55f-3434-a372-1016434136c5 | 2.64733 | -60.17471 | 2026-09-27 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ebb98752-e54f-3ef5-9961-ba18e2906179 | 2.64483 | -60.19288 | 2026-09-27 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 70cb0697-d169-3e47-a062-050848f228ca | -12.2877 | -50.4004 | 2026-09-27 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7f80bef8-8ad3-3255-a8cf-746670341e61 | -10.8052 | -60.7257 | 2026-09-27 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 4672c6c5-7885-3813-93c5-6ccb683df364 | -8.0373 | -54.8926 | 2026-09-27 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1d610169-1df3-34e4-bd10-d88fc459537f | -10.824 | -60.7246 | 2026-09-27 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1a0736e7-f1ba-37e9-9cb1-2cb223e60967 | -12.288 | -50.3789 | 2026-09-27 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 02a8f0d1-bd86-3303-b9b3-f1b01919815b | -11.94 | -50.55 | 2026-09-27 01:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 766931eb-4d32-3bb7-b245-d339fe58e5e2 | -8.36 | -44.16 | 2026-09-27 01:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71235446-18c3-342e-bfc9-033619f159c3 | -8.33 | -44.15 | 2026-09-27 01:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87715980-d98a-3a15-a259-38849ce79e1b | -8.36 | -44.2 | 2026-09-27 01:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 880e5773-c84e-3c67-a848-77207086aaf3 | -8.33 | -44.2 | 2026-09-27 01:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 861accfb-dda4-38dd-88b6-93a77f861d6c | -11.91 | -50.54 | 2026-09-27 01:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbb3dfad-7a79-3c75-acbb-6c5e508d0879 | -11.0299 | -54.046299 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e65d7b9-1f0e-3c29-a862-31f8830b7c80 | -11.9765 | -50.595299 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bed9964a-2073-3322-ab9d-24d6ffd66192 | -8.0401 | -54.9011 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4682b6fc-a7cc-3e10-8751-3e3e2fba69f7 | -1.1458 | -54.085602 | 2026-09-27 01:15:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94752dd4-16ca-38eb-9db0-aebda7478b17 | -3.6994 | -51.362301 | 2026-09-27 01:15:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36e03e91-7bd2-323e-8c13-e003ef44cc0e | -3.718 | -54.646301 | 2026-09-27 01:15:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfb8a73-9cfa-3f00-a968-7944244e4093 | -11.9542 | -50.548 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a042b8a-597d-3a0b-a7ba-38ac4734943c | -11.9091 | -50.533001 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eff123e4-8aab-36f3-9d18-1055a9821b05 | -1.1122 | -57.273602 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33972047-9bc2-3c1b-9e4a-8ab96b6582ca | -11.9348 | -50.553001 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b515ba65-3ab5-39b1-a341-0d764446603b | -2.6532 | -56.445301 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5f6a4fd-b89e-32e1-91ec-3000d1ef4e4a | -13.34 | -51.331402 | 2026-09-27 01:15:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29a641cd-ff38-314d-b175-9b9733de97f0 | -20.8354 | -57.705601 | 2026-09-27 01:15:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8deebb28-cc08-33ae-82d7-447592826f89 | -12.1783 | -50.328499 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14939412-9764-338d-b3a2-a3b2121b6e92 | -21.635401 | -50.071098 | 2026-09-27 01:15:00 | METOP-C | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2078368-0d14-350e-a3e6-69d2f39f3ea0 | -7.6972 | -54.7612 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c96ccaa-6fe9-3f14-a157-27e66c286092 | -11.9188 | -50.530499 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4658988-21b5-37b4-83b9-f69477f3561d | -11.8993 | -50.5355 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26db29d0-9e8c-3342-a3da-d6fd709580d5 | -11.9317 | -50.540501 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6e5cd82-58e5-3424-b7c0-7de110de97eb | -10.7996 | -60.722401 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24e57f7c-5a19-3162-a7e0-41b2fdd0e175 | 2.6376 | -60.1632 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 088bb090-f00a-3deb-81c0-60172371df8b | -1.0536 | -53.557301 | 2026-09-27 01:15:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
