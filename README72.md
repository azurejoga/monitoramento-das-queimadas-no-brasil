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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1008c0a-270f-3062-a992-95dfef87e4a7 | -2.94443 | -54.13111 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| fcf13070-dfbc-391c-bea0-1e2f56dbc778 | -2.44837 | -50.25278 | 2026-10-04 07:03:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a826825a-39b6-365c-ad29-db39039c741f | -3.20637 | -50.7409 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d978ce71-c1e0-3fc3-991c-77bdeffe99e8 | -3.08519 | -49.53041 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 183b847b-7146-34a2-8489-7205ccc18d8d | -3.12682 | -53.74427 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6bf5fc4f-96cc-3582-90c9-32c95aead6c1 | -4.26019 | -46.36509 | 2026-10-04 07:03:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 26.3 |
| dd6cf1d3-a402-39a4-9eb8-7e56e9f5524c | -3.47211 | -50.08854 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| d85cd333-402b-3592-9fbb-9fce6adc2352 | -3.69991 | -50.65753 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| c3ee33b5-986d-3848-8b77-1d09320610da | -2.82166 | -54.11928 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5017f5d5-d9eb-390a-a803-934b8341aa8d | -3.11865 | -53.73139 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 23495265-cca9-3ad3-8a9f-78e9036a5c12 | -3.5158 | -54.60778 | 2026-10-04 07:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d89a5892-0173-32e7-b0ed-7f7af20ddcad | -3.10697 | -53.74127 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| e88a7b32-0048-3383-978a-c54c9b7e0706 | -3.11049 | -53.71855 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| e1125fd1-bbb9-3827-9795-a70acb76cf99 | -2.58552 | -51.84621 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e8264dd6-5669-3d79-bb59-b186850c519e | -3.10873 | -53.72991 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 3ebe61a0-6c10-30d3-a103-06fd4eba45d9 | -2.99305 | -51.04543 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cf9eb748-ddf4-3bcb-b106-a7d1ae3962b1 | -4.29494 | -50.27394 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fb6405bc-e879-3d59-beac-f9da81431cc2 | -3.06746 | -49.52783 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4c300e4f-dca4-370c-bf1d-00dee99f77d0 | -3.20504 | -50.74961 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 182a42a1-27df-3806-81ce-671d27f7fde1 | -4.76882 | -42.55934 | 2026-10-04 07:03:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| b5c95fdb-075c-329c-9710-18322243b03a | -2.25556 | -51.88323 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03809924-72e0-3842-bbb5-f6410afc7dc9 | -3.01351 | -53.8856 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 67b16bbd-3e3c-3b2a-b155-82deb0c91a66 | -4.27738 | -50.27136 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 531.6 |
| 0c5c4aaa-f738-34a2-828f-89d72ccdf78d | -2.82359 | -54.10712 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e55a6d9c-e6f5-327a-9a11-36195d9d2c40 | -2.22021 | -53.69926 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 0c418c25-0f38-38b9-8ee8-caf491b55d5e | -2.58131 | -51.8739 | 2026-10-04 07:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 225bf5d6-78e2-3db8-9888-fea94089d34a | -3.11514 | -53.75416 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 6de4a423-8657-3a7e-a3ec-6f4b3f712900 | -4.78488 | -55.70746 | 2026-10-04 07:03:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2a46b354-318a-3ce9-9de0-c222b8bc90d1 | -4.28484 | -50.28143 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e3f77977-ed63-3eeb-8bea-c32337eab17a | -4.10609 | -49.06805 | 2026-10-04 07:03:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6fdf9873-4aa0-3e0a-a764-f27fa50b0d80 | -3.11689 | -53.74277 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 05d129fb-2b65-34b0-97c2-a8ed54257241 | -4.28616 | -50.27265 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 246.8 |
| c254ee73-8553-3170-8a50-039b7e1100db | -3.10521 | -53.75266 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b3a04132-c852-3ff3-92ab-b7d75c3c8f44 | -3.0515 | -54.16637 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b2a641e7-d6d1-335d-a629-cbfccfb259a3 | -3.00627 | -50.46996 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 4b667ff7-80a7-3eab-9179-65ff8aac27f3 | -3.76315 | -49.56326 | 2026-10-04 07:03:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 88ae5939-4773-3136-a215-0397fa77707a | -4.28881 | -50.25509 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| db867edf-6af7-3dad-918b-c0d2b444a654 | -2.79651 | -54.0962 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5973530c-7670-3063-939a-9524f9747b15 | -4.27606 | -50.28014 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 961d0857-b607-3fd0-92c5-969e3cc3cd69 | -2.58271 | -51.86467 | 2026-10-04 07:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f448c712-671a-3891-8a68-3b3742613af2 | -3.86983 | -55.79875 | 2026-10-04 07:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a52d3316-f319-37bc-8cfc-24ab895adbea | -4.27376 | -49.97658 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 603a2dbd-8214-30d6-bfe4-05e68bbc84bc | -20.22418 | -57.99457 | 2026-10-04 07:09:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| a2c95585-00bc-327e-aa66-89865e86efc0 | -4.28 | -50.26 | 2026-10-04 07:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1f2e9c-b34c-31b2-b9fb-3f610ce569c6 | -4.28 | -50.26 | 2026-10-04 08:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 239ee70f-84e9-3419-b8e6-7faf902bc3a2 | -4.28 | -50.26 | 2026-10-04 09:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 081e48e5-2386-3c79-8569-695817efa307 | -3.26046 | -41.27394 | 2026-10-04 11:19:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 538c0a6c-d2f9-32df-b57a-0af0c62e6b7a | -3.37654 | -42.19276 | 2026-10-04 11:19:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 12.0 |
| a7aaba15-272d-397d-bc43-fb49b817afaa | -7.07057 | -41.46527 | 2026-10-04 11:21:00 | TERRA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 02229e59-2e90-35e1-b1a0-5ecb3f6c7423 | -6.5716 | -44.1598 | 2026-10-04 11:21:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fbdedc44-c67c-34a9-a523-ef754398af03 | -8.33306 | -45.48785 | 2026-10-04 11:21:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1427fb83-68fb-36af-888d-9938364ebd37 | -8.32143 | -45.49789 | 2026-10-04 11:21:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 17c3b5b6-f0d1-374f-bbd4-27fab4b2a7d9 | -7.76458 | -37.19143 | 2026-10-04 11:21:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c4665767-4dbf-3e96-a994-7e9cf98549b0 | -6.32183 | -43.34074 | 2026-10-04 11:21:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fafbce9c-62b8-33b2-8085-333c71c3fe12 | -4.54024 | -43.53427 | 2026-10-04 11:21:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0152d926-d5bf-3b42-aab0-0e324f7f3645 | -7.77596 | -37.19303 | 2026-10-04 11:21:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 416780ce-b1d1-3490-929a-588f6fcafff3 | -6.57306 | -44.14978 | 2026-10-04 11:21:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 82ab6489-a078-3409-9e9b-7fed712e685c | -8.32312 | -45.48658 | 2026-10-04 11:21:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d39cb0c0-d3cb-33bc-9a8b-ded3abc4033f | -7.76633 | -37.18505 | 2026-10-04 11:21:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e22fa111-18b5-355c-bc46-a01f87a307e6 | -15.79024 | -42.33109 | 2026-10-04 11:23:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| 1a666d30-3e62-30e2-8e9b-b8b6bc02e9c5 | -11.8218 | -43.54095 | 2026-10-04 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| a72eb3d3-bf2a-32f3-85d9-c4faf891ecbe | -11.81297 | -43.53973 | 2026-10-04 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 07ee2a36-3d4a-3b34-9024-1ea4a2a409fd | -11.82309 | -43.53202 | 2026-10-04 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a5bf996d-063b-3066-bc63-246d73f45ca5 | -12.91317 | -42.75179 | 2026-10-04 11:23:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 28aff87c-69fe-3916-8925-14036c1f747e | -15.78892 | -42.34076 | 2026-10-04 11:23:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 80310f6e-e1ce-3974-964a-3db072b7eae0 | -12.9119 | -42.76081 | 2026-10-04 11:23:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| aecfc5d0-a94f-33ed-9f2b-ec35d98a42cb | -12.865 | -42.29576 | 2026-10-04 11:23:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3ebb408e-a303-34bf-8566-be33a86a0cfc | -12.6308 | -43.44035 | 2026-10-04 11:23:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8705e460-7851-37e3-8552-e2c1812dd5e4 | -3.11 | -53.75 | 2026-10-04 12:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 100f56bd-bede-3d29-a7c3-12a2d4c53ef2 | -11.2817 | -44.2804 | 2026-10-04 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 01a74885-429a-3d05-8cc7-acdb448e1e53 | -11.3204 | -44.2514 | 2026-10-04 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 8bc3ba53-3818-3231-9f34-a8323d4b93d3 | -11.3009 | -44.2776 | 2026-10-04 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 2f55863a-3cb0-3f12-adea-7448e01071a5 | -11.6771 | -43.587 | 2026-10-04 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| a516737e-e13d-3af6-81a3-09aed0db011d | -11.6968 | -43.5603 | 2026-10-04 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ee7b29ea-025b-3f91-b7f2-3ee22f698d0b | -11.716 | -43.5573 | 2026-10-04 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e42d3f1d-e2c5-3bf3-9b03-27cf1ee7285b | -11.8123 | -43.5422 | 2026-10-04 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d6f447de-7bb3-341c-8e6f-8474684332c0 | -11.8123 | -43.5422 | 2026-10-04 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 64d58595-fc3e-32da-96b5-f632009ed157 | -11.4499 | -43.4329 | 2026-10-04 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| afd2dc5c-ceac-37f9-b713-b9d6434a51b1 | -11.4302 | -43.4596 | 2026-10-04 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| ca53e588-c515-303a-ba54-11742a68b2eb | 2.51402 | -60.99324 | 2026-10-04 12:57:00 | TERRA_M-T | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0e219491-0d84-34a3-9903-96c0b512f74d | -3.83905 | -55.86052 | 2026-10-04 12:59:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| d17f8db7-03e3-333b-a6ce-ed946302a3ea | -3.84647 | -55.82778 | 2026-10-04 12:59:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ca3fcdef-ea1b-3b1d-99d5-4571deb5bb75 | -3.84444 | -55.82034 | 2026-10-04 12:59:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 24e4dd23-ce28-32a4-b6e6-0a1d93c1fdc4 | -2.05819 | -56.87225 | 2026-10-04 12:59:00 | TERRA_M-T | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1ab9e8a9-7245-383e-8284-5a35845edde3 | -1.21163 | -55.84268 | 2026-10-04 12:59:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 125edd4e-debf-39d7-881d-c0eba573f62c | -8.59202 | -66.8195 | 2026-10-04 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c371a50f-722c-35be-920d-67e406f366e8 | -8.51519 | -67.10609 | 2026-10-04 12:59:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 65e09e06-b3dc-32cd-b9ba-386b504efba0 | -8.58455 | -67.14036 | 2026-10-04 12:59:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4983cb63-78d0-37d1-b472-13e68bb9c9ff | -8.4907 | -57.62019 | 2026-10-04 12:59:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f5dd0042-4135-3ef4-bd9b-e53f9793069f | -8.58582 | -67.13152 | 2026-10-04 12:59:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ddb85864-4012-392f-b026-3b6ebfa0be16 | -8.59328 | -66.81067 | 2026-10-04 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| b642dd26-cf5c-362c-8196-709ecc84ad8e | -8.55797 | -67.05805 | 2026-10-04 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c0ea7dbf-31c0-3c3c-a616-28fe5e38088a | -8.5655 | -67.06812 | 2026-10-04 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c093318f-5d86-3090-ab6e-0b752b925e97 | -8.91656 | -64.14223 | 2026-10-04 12:59:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4d0abe38-cda8-3219-a91a-f6415eb2be65 | -11.793 | -43.5452 | 2026-10-04 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| cd903bd5-908e-33cb-bd98-ffd640d28d85 | -11.8123 | -43.5422 | 2026-10-04 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 970e405b-c2d2-3a6f-a0c7-a2c3980959d9 | 3.4155 | -51.3021 | 2026-10-04 13:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7a6b4f54-a999-3485-828b-4f25ac7a621a | -9.12976 | -65.89008 | 2026-10-04 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8366b3d-a7dd-3957-b26f-27b5aac4ac80 | -9.13542 | -67.92547 | 2026-10-04 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9521256b-4304-3cf4-8905-772abf4f5bf6 | -9.9195 | -65.03922 | 2026-10-04 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |


[Clique aqui para ver as próximas entradas](README73.md)
