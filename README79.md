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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26f882ff-38fa-3266-a0ae-b15067e265de | -1.35494 | -54.6311 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f94a78c3-3b11-3288-85ea-10553d216b7b | -2.80298 | -52.90888 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 26ff2226-4ee5-3003-89d9-67f2b82665f6 | -2.24978 | -53.62356 | 2024-11-27 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d6e5e3c5-8a9b-322f-b862-8df099c3f805 | -1.95999 | -54.13455 | 2024-11-27 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1be98058-e2cf-36bd-90f6-79a7072a0199 | -2.60239 | -51.83036 | 2024-11-27 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 828bbcdf-cce5-367e-a70f-fefe834ae2fe | -2.79669 | -52.91164 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc253e16-4ed4-36cc-ad75-28735c1138ef | -3.75643 | -51.60036 | 2024-11-27 05:35:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e08697b8-e960-3fec-a843-c33d98d54037 | -1.80433 | -52.75111 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4340db52-81e8-39b1-a03f-576ba48f65a1 | -3.72184 | -50.19008 | 2024-11-27 05:35:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e615b9e-95aa-3abe-aa0b-8b90357d0de6 | -1.68877 | -52.61125 | 2024-11-27 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e113fe06-a5d8-3d48-9843-dcc9dca0534e | -2.80177 | -52.91687 | 2024-11-27 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67b7aad7-27af-3e88-b45f-5dd1df97cd7c | -6.48342 | -54.91785 | 2024-11-27 05:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daf955ea-54a0-3151-a6a5-ff6a6f460b15 | -12.6822 | -52.2671 | 2024-11-27 05:37:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7f3f05d-39f6-35d9-b64a-4283d33cedc6 | -9.18737 | -65.36952 | 2024-11-27 05:37:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09e09c83-04b6-373e-85d2-c78e51fca45c | -4.45199 | -59.95699 | 2024-11-27 05:37:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 078a7f4c-35ed-3dab-8052-9aa65e802605 | -12.68896 | -52.26819 | 2024-11-27 05:37:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3fe75e7-0452-3ed8-9a04-c32c676b0dc6 | -10.09813 | -68.39079 | 2024-11-27 05:37:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d63927e9-4944-3553-a8c3-da7066a6a683 | -9.38482 | -58.23251 | 2024-11-27 05:37:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbdcb0a2-73b6-37b5-b452-4f23929728ef | -4.45263 | -59.95263 | 2024-11-27 05:37:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9cf7090-9012-3598-ba2a-bbe0650813ca | -3.1691 | -48.4394 | 2024-11-27 05:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| cfe31e9a-7bfd-32a1-93f9-420cb3c2e1d6 | -2.8346 | -54.1326 | 2024-11-27 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e74a5e47-4404-3e61-aacc-86e967046f6d | -3.1876 | -48.4387 | 2024-11-27 05:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f5ba42f9-52f8-3288-a375-d5fa51e3c612 | -3.0949 | -53.2385 | 2024-11-27 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2b74665e-b58b-3401-ba0a-46fc26725bbc | -3.9674 | -48.0851 | 2024-11-27 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3c80cd71-dca1-3e5f-ab49-a2cbd0de4b52 | -3.0949 | -53.2588 | 2024-11-27 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 180.2 |
| 11dc7968-435a-3eb0-acef-512275f67656 | -5.9975 | -45.3607 | 2024-11-27 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7a856138-be72-310a-8b76-4782dc1b0fd2 | -3.1133 | -53.2381 | 2024-11-27 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 26a0bdb7-bd22-3ef3-99d5-5f7a5d357762 | -3.1133 | -53.2583 | 2024-11-27 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 4fd79b16-d93f-3f42-b3db-d581399ea403 | -2.8347 | -54.1125 | 2024-11-27 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cf4910e8-c636-32ab-a7dd-170a5def8ea3 | -5.9788 | -45.3621 | 2024-11-27 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d39d4c20-71a2-3305-bed1-5e2979212b1e | -12.70082 | -60.4412 | 2024-11-27 05:40:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 678c6c17-8c56-35c0-893d-a03acbb3bd66 | -17.56836 | -57.47486 | 2024-11-27 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e41d3771-2372-3759-8311-7d4ba978bf0e | -12.70032 | -60.44472 | 2024-11-27 05:40:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66d43a29-d456-372a-bac8-8c2804520223 | -18.01725 | -54.00726 | 2024-11-27 05:40:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34b91448-0c61-3ade-b3ea-7a3b0ab91668 | -15.29307 | -56.52551 | 2024-11-27 05:40:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23bd3566-aac5-3e06-97d3-e58d35d38077 | -17.22623 | -54.43972 | 2024-11-27 05:40:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c1896a4-96a9-33df-b6ca-ac23fa3e7d19 | -18.01076 | -54.00652 | 2024-11-27 05:40:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b627c6a0-145a-3afd-82f7-9596d8ee8907 | -17.568 | -57.47813 | 2024-11-27 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d19e7768-efc5-3c09-bb1d-2f00859df15a | -18.01705 | -54.00927 | 2024-11-27 05:40:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cdde8b8f-475f-30b8-91da-673cdb4d7fbb | -12.70481 | -60.44175 | 2024-11-27 05:40:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1aba5d8-3efa-36f8-b4fd-56649246bc2f | -18.01752 | -54.00377 | 2024-11-27 05:40:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0e17ea9a-63eb-339b-b8ff-53ada8846816 | -21.6091 | -57.49689 | 2024-11-27 05:42:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 397df26e-b949-3254-a4f7-ee8b165b3e53 | -21.60779 | -57.49725 | 2024-11-27 05:42:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f406e97-4dd8-3c5a-8799-b058fe2fffd9 | -3.0949 | -53.2385 | 2024-11-27 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| bfa9b139-d70d-3a0c-8b6f-956a39968872 | -3.1133 | -53.2583 | 2024-11-27 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 540dcaeb-2208-3531-87eb-c8a9b4879d5e | -3.1691 | -48.4394 | 2024-11-27 05:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f5a1c2ee-a2d1-3969-b777-a23913530af2 | -3.9674 | -48.0851 | 2024-11-27 05:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e1d551fa-16ce-31c3-9bf9-99245b99c28c | -3.0949 | -53.2588 | 2024-11-27 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| dfc8df13-5f44-329c-bc15-6cd2e2343e5a | -2.8347 | -54.1125 | 2024-11-27 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b00411dc-b367-3780-be4e-c03f586091cd | -2.8346 | -54.1326 | 2024-11-27 05:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2dbec8c5-00ba-327a-a6fe-4dbfa635de5f | -2.5956 | -54.2181 | 2024-11-27 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 91ff6028-2fab-3b11-8d63-d9dc3660173a | 2.08383 | -50.6321 | 2024-11-27 05:59:00 | AQUA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d89f28a-43ac-3b34-bde2-2861f5e6431a | 4.27823 | -59.75904 | 2024-11-27 05:59:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 435bf2c7-33c2-39e3-944d-4624bd554b66 | 4.38127 | -60.82446 | 2024-11-27 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d0361ca-eac1-3e04-8ef9-56ca99bf83a6 | 4.37707 | -60.83088 | 2024-11-27 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1c3e415-9c70-3c97-b84e-90021f36c538 | -3.1133 | -53.2583 | 2024-11-27 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| c064845e-2b1e-305c-bf25-7873cda2c5ed | -3.3114 | -45.7377 | 2024-11-27 06:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9ed41273-84bd-3959-80c9-d892b5aa4dda | -3.0949 | -53.2588 | 2024-11-27 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 621ddb5b-d43c-3469-8483-81a7536d0b4c | -3.0949 | -53.2385 | 2024-11-27 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0310b00e-6754-363d-a1f3-b293f694f8cd | -2.8346 | -54.1326 | 2024-11-27 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6136d33e-7815-3c55-8d2e-d9e34049f735 | -3.9674 | -48.0851 | 2024-11-27 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 4811fef0-2901-307a-b112-a298473e14b3 | -3.1691 | -48.4394 | 2024-11-27 06:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 54a6c995-f3c9-35dd-ab71-14e4058a801a | -2.8347 | -54.1125 | 2024-11-27 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 48270fc9-ced2-3ea1-bb59-a9d50a203be8 | -3.33 | -45.7369 | 2024-11-27 06:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5154a47a-2cc6-3907-a62c-2a1f7e007f86 | -2.73069 | -54.13162 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1da4707d-cf6e-372c-8601-a477a6fba4c5 | -1.71943 | -52.48769 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76373b16-8391-3354-95ca-d33a8585a347 | -2.59624 | -54.05027 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 69be393b-a600-338b-9f63-358124365835 | -3.1141 | -53.10491 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f5038fc8-0d19-3c25-a5b0-11d5e7ffbbae | -3.45209 | -50.28518 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 47b50009-cfda-3865-b4aa-96474c79360a | -3.10039 | -53.26263 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9a5a5eea-b0b1-3642-96a6-8d19a1cf83b2 | -3.11251 | -53.24455 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 26bb468b-4edf-31c2-8427-bc019eb3624c | -2.93894 | -54.78569 | 2024-11-27 06:01:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0d4e4dbe-4029-31ea-a4af-3b26268b9e29 | -1.07204 | -53.3736 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d8fc8dc8-8b31-3fe3-a0a4-0023720d0687 | -3.04087 | -48.49249 | 2024-11-27 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d94e3809-9b8b-36f1-b033-553bde91947a | -3.06058 | -53.2766 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7d7e457c-7f80-3fd5-a559-74b85ff3d2e9 | -3.05368 | -53.26995 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c1a1c234-9ae1-33f4-8448-a15f6b4dd805 | -2.8056 | -54.12986 | 2024-11-27 06:01:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1009a3a0-c8e5-3c31-9bf7-16c6a6d99367 | -2.85956 | -53.9526 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7b82f64-902f-3262-ae55-12cbd0647fc2 | -2.24211 | -53.63309 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 770fe212-1f0e-3bf9-9521-25478628efed | -1.73292 | -52.03405 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 446fc7d1-89c1-3492-9b03-a89c225d7f1f | -3.32742 | -45.72764 | 2024-11-27 06:01:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c7f8d9ab-d2a1-36f5-be69-154227ccdf3f | -1.10536 | -53.39455 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d0ec688a-4e07-3e4f-b315-26aa15818ef2 | -5.9822 | -45.33671 | 2024-11-27 06:01:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 422935bc-4f14-3fec-b022-9a832d562557 | -2.18284 | -53.78369 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dbf4433e-5ae8-336c-9c4e-97fefdcbec44 | -3.37415 | -50.11005 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d4c904cb-7c3a-3783-b4a8-d427b62f630e | -1.15759 | -53.66939 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fc295f2f-012b-37ea-825f-b56b0a1fe1ff | -3.90144 | -50.59798 | 2024-11-27 06:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7e68a170-5bd2-3380-b593-b81c1f1021b1 | -1.62537 | -52.27209 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 428a1299-c92d-3d6d-b7a9-0bc1a745b6f5 | -3.10963 | -53.26398 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| cb7ff1e3-eb58-38be-9b32-0f25918f20db | -1.08109 | -53.37484 | 2024-11-27 06:01:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e427ff1-51f2-38d4-a8b5-1d292207c91b | -2.85822 | -54.02402 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c086f45-b378-3d74-8093-2fb6c045c6a4 | -3.97462 | -48.05712 | 2024-11-27 06:01:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| fe82063f-5323-35f8-b35a-0323e3ac585e | -2.53976 | -53.99016 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cf667fb-051a-3bac-be46-f0f2005ee7b2 | -2.58597 | -54.05796 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 854ec7a7-bdd5-3d74-8f00-0f2c0c6b70b7 | -3.31676 | -45.73378 | 2024-11-27 06:01:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ade1f66a-7dc6-3da1-aed7-9d21efd68155 | -1.78511 | -52.73005 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9f573d8b-0b9f-3ebd-b598-f955fb52d9c3 | -2.09945 | -53.35258 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 74ec265d-afc2-3dea-bba1-43cf33feae2f | -3.11107 | -53.25427 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| dd85c31b-eb29-3e01-8baf-7b59fa5a741a | -1.6907 | -52.6179 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 79a3ba36-3c6f-3bb6-9a64-6ce6bafd9867 | -1.80237 | -52.74268 | 2024-11-27 06:01:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |


[Clique aqui para ver as próximas entradas](README80.md)
