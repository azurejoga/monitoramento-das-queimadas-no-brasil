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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 806a53f0-495f-3230-a38e-5c04a94f766b | -9.97332 | -48.24195 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 431e4484-aaed-33ab-9e86-bde4f21eb5db | -8.02556 | -46.32729 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2a3bb0a-65a0-34db-9da3-ab707de9c8fa | -10.87605 | -56.43683 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7503087f-8753-3ba5-8756-911a460f083a | -10.12931 | -52.35233 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcbf5eb5-4bd9-3985-8ecc-f546fdc9296f | -7.44371 | -49.77533 | 2025-07-01 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86309cce-70c7-367e-8218-2d9c0887ffe7 | -8.0296 | -46.32814 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e4885c8-673a-35e0-bf71-0d521b659aab | -7.28942 | -45.37641 | 2025-07-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68727fcb-5bb4-3755-b5e4-7dd6c52cc1dc | -10.12601 | -52.3518 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0003953-9e21-3957-b1fb-60c199e82cfe | -10.87664 | -56.45652 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb5ccfa4-ad43-30a5-a827-f67a928ab56a | -6.21065 | -43.35725 | 2025-07-01 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8c4a708b-4c31-3ec8-85b4-936ff568bfb3 | -11.57504 | -47.43312 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6261290-d36f-32ad-b84e-bd366037b547 | -8.5501 | -48.25768 | 2025-07-01 04:46:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95f60115-3fc6-3981-ae99-0c8a6eb37cd8 | -8.67549 | -51.47134 | 2025-07-01 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 092d3ee5-06a2-3950-a881-62ecad98f089 | -6.17747 | -47.27596 | 2025-07-01 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e4692f-47c4-322e-9a4d-5f520650b4f8 | -6.28739 | -43.68293 | 2025-07-01 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 1150c592-4756-3f81-95dc-82f98912f080 | -7.54873 | -45.83112 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b43c7055-b433-31f9-b4a6-f6b9e246b7a9 | -11.83348 | -47.50867 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9aa05c39-bc83-3e1d-9473-6f1b7bc8583f | -10.51035 | -49.77881 | 2025-07-01 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdd826d6-40cb-3498-b167-3517838fae23 | -7.2937 | -45.37706 | 2025-07-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fdae1dc-d2c4-3f47-b00a-7a42cc74087e | -10.29823 | -57.12826 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c2307b8-5785-3cf2-bb90-b402f6777e94 | -7.30229 | -45.37823 | 2025-07-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93b2c173-cfb4-37a7-8052-657af4744b7f | -10.87301 | -53.7734 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77e862e2-9833-3040-9bef-e575371ed70c | -9.71309 | -56.18376 | 2025-07-01 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab918bf9-490f-3edc-9a69-b203af6e550d | -10.88286 | -56.44292 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d0b3d1f0-4dad-349f-84ec-03d1684c697d | -6.48029 | -43.73893 | 2025-07-01 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f062b6f4-1244-3e0f-b82d-fcff720be7e7 | -10.02155 | -54.32122 | 2025-07-01 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94d5aaac-f951-3bd6-9170-7179bf1d6eb0 | -7.55405 | -45.82388 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ad6e7d3-5d99-3d67-9189-ba1a0ec92877 | -9.25127 | -58.76347 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02640444-2768-33d5-8a70-8e50076747d6 | -12.28193 | -50.1119 | 2025-07-01 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b6fcbf4-6149-35ac-8cfb-e7669f7274d9 | -10.79935 | -48.28575 | 2025-07-01 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a20da3b-27ad-3738-9e7a-f3ff7cce217d | -10.87242 | -53.77707 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5475318a-5f2f-3c85-9219-8265eb89475a | -10.93503 | -55.32311 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dbdc0d8-26a7-3abb-b189-7f3cef8bc1fb | -9.96961 | -48.24137 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a40a97e5-fe20-31b0-8c32-507d08e347db | -10.55363 | -52.03461 | 2025-07-01 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e47f140-e8be-3c34-9da5-9a942805f5ab | -10.12049 | -52.34377 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e281886-435e-338c-89c1-1b7a1437bf15 | -8.72534 | -47.98307 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f99fd353-6f6f-3b6d-97cb-2c2ea609782d | -7.29119 | -45.37349 | 2025-07-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a464f7a4-9b1f-3e2c-8923-e85dcca86f82 | -11.12463 | -55.44866 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08047e14-1555-315a-ac63-0a29c91276da | -10.87416 | -49.54691 | 2025-07-01 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2641e0a7-86e9-3370-bf13-1174cf2a989a | -11.58129 | -52.11744 | 2025-07-01 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2a1dfca-5dc1-3f01-9851-298593ad1044 | -9.79166 | -48.61654 | 2025-07-01 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 626d7da1-ba1e-31f3-80ef-292911c65df5 | -10.51002 | -53.57936 | 2025-07-01 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55bf0bf0-5ef6-3118-a275-83d538db7f96 | -8.67603 | -51.46787 | 2025-07-01 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4af3b7a9-a572-3e69-bdcd-cebf968218ab | -9.70162 | -56.18188 | 2025-07-01 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 863530cf-6ef5-3d68-80a9-a43d9ccf173c | -7.0942 | -49.16546 | 2025-07-01 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34c34495-6f0c-393e-a56a-1078c9f19b7b | -11.1423 | -43.32875 | 2025-07-01 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf1a6475-16ab-35b4-8785-07c38f263c3f | -13.0138 | -44.10268 | 2025-07-01 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84232083-cb77-3033-8897-a77bfa326c92 | -10.08842 | -52.74076 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b45fe29-df27-384e-beb1-724e17a298d6 | -10.87217 | -53.73567 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6f4042b-5ce1-331e-96a1-b3712de89b4c | -8.72839 | -47.98804 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 811eb5f9-56f3-3ebe-ab21-f0dcabec4f6d | -9.08315 | -59.48918 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f36bbfa-947e-3b4f-9fd4-7595613c07fd | -10.86964 | -53.77283 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84da4f02-996f-3d4d-b26b-f75ac35eafca | -11.1415 | -43.33519 | 2025-07-01 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32c3e4ab-040f-3d87-b377-47b6c68607fd | -6.17439 | -47.2709 | 2025-07-01 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14191369-f5f6-340d-b707-a724c7b2b767 | -10.30006 | -57.0461 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 456dd261-dcc9-3bab-9d12-1ef37fb0318b | -9.24549 | -58.74317 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d412744-510a-3df0-a8b9-6df41fa628e9 | -10.88969 | -56.44899 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 366a4108-4361-34b1-a97c-5ed319f2f312 | -12.28541 | -50.11243 | 2025-07-01 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef0a8736-06c6-3604-8b3f-779a42d14b7b | -5.67518 | -44.82547 | 2025-07-01 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 620124c5-a4a9-3e5e-91e6-8558de39c058 | -10.12893 | -57.77532 | 2025-07-01 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c906dcf-fd49-3ab7-8403-74eab0e3ffdf | -10.08897 | -52.73723 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b16c5b9-743e-383e-a207-0f49d5cc49aa | -9.98139 | -48.23862 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1697da70-26f7-31b9-a618-c875ef88d789 | -9.24588 | -58.7674 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0caebb7a-2fd1-3d47-9cc2-b2e621ee8eb6 | -7.29426 | -45.37302 | 2025-07-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08b7e62a-6a3e-399c-925e-41cfdd93e10b | -11.1419 | -43.33196 | 2025-07-01 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85847898-9d58-3668-8fd8-ab45297ed2f5 | -9.57171 | -49.10571 | 2025-07-01 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c4ae9fb-644a-36c4-bbe9-6a214785f1a5 | -12.02157 | -47.76582 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0fe1821b-0e91-3621-99ea-c5a7fe1efe90 | -9.68245 | -48.33752 | 2025-07-01 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e325838-e18d-322b-adef-342dbc0d7a6c | -9.70544 | -56.1825 | 2025-07-01 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 202440a6-0260-3caa-84ef-34f32fb593d6 | -9.70926 | -56.18312 | 2025-07-01 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4befa1a-629b-3d42-b422-ebe2ab6a630f | -9.23805 | -58.73228 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbf0ec32-c5a6-3f42-a728-559a954dcf42 | -10.88667 | -56.44358 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aa0b1749-6be2-3f25-940e-10029a586ae0 | -10.86762 | -53.7424 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f5fe1b9-289a-3c51-8625-431b62f64c6e | -10.62524 | -51.79207 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53d0000a-441c-3b06-bb8d-ca75b47a5405 | -10.99043 | -49.54294 | 2025-07-01 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a7fcb4-5f94-33b8-815d-2b6bdb7b59da | -11.20068 | -49.00248 | 2025-07-01 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e62aea-28b6-3341-bd2d-ed85413eeca2 | -10.17329 | -51.65938 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2885685-b80f-3ad5-b767-93b51183feb5 | -12.76677 | -44.40753 | 2025-07-01 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70f856cd-25fc-3d6b-ba04-a936128264f8 | -9.98074 | -48.24308 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ffe658a2-40a2-3211-86bf-b7622325ffad | -12.01621 | -47.77546 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 060a310e-d3cf-347f-b177-740f52201692 | -9.57562 | -49.10489 | 2025-07-01 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 494757f7-6fc7-3828-a7a3-88cfafb8982d | -10.28125 | -52.8338 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a18c5804-0715-3f79-bb48-7930daf74c48 | -9.65426 | -50.74387 | 2025-07-01 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fed3dfb5-860a-358a-a00d-0f5be691979b | -12.29797 | -48.80964 | 2025-07-01 04:46:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4978ee9-5516-32f2-96f8-8a5a5f49fb51 | -9.57208 | -49.10434 | 2025-07-01 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14b91b11-b675-3838-97a2-5d365cc83db5 | -10.69891 | -51.80066 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77965057-2c45-3bdb-b66e-11f653d07642 | -7.97175 | -45.93628 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2ceb0b7-aefe-331b-9175-295e5781734b | -10.29701 | -57.13531 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bff3591-7fee-36aa-8ca4-498403bece33 | -10.12765 | -52.34134 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68a07ba1-a221-371b-aa82-3b2b776bfd97 | -8.86125 | -47.95088 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bce7eca8-69bf-3528-b9df-f0eda303bb49 | -10.87443 | -56.44638 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5d00ba1f-b4af-393d-a678-d8fa5a43afe3 | -10.16722 | -51.65484 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23dacfc3-1db7-31b9-9ed4-2af57d73f1ae | -9.57503 | -49.10891 | 2025-07-01 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e5624244-8813-3eb2-8fd8-75324573c46d | -10.30442 | -57.1403 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e6b559e-430a-3799-a631-ee11c9a6e383 | -10.87554 | -53.73622 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f31acc-a132-3e0b-ac32-e6a77b9745e2 | -10.12986 | -57.77467 | 2025-07-01 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dc2eb0d-cd5e-3ef2-8f40-095590b8c564 | -8.67219 | -51.47083 | 2025-07-01 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52675474-9286-3a43-bc83-811f4ac4dbdd | -10.12407 | -57.7785 | 2025-07-01 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67ebe78b-662a-3321-ac5b-3945c64d45cf | -8.72469 | -47.98748 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba1aabc5-ba45-3988-b4fd-6d86b0280965 | -10.87473 | -54.04686 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README10.md)
